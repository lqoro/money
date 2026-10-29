"""Paper wallet. Starts with $100 cash and simulates every fill the way the same
trade on Axiom would go: Axiom's fee, the pool's fee (pump.fun curve, PumpSwap's
market-cap tiers, or a Raydium-style pool), Solana network fees (base fee,
priority fee, Jito tip) and slippage from price impact, so paper results aren't
fantasy numbers. Prices come from DexScreener; no real venue is touched."""

from __future__ import annotations

import json
import os
import time
import uuid
from dataclasses import asdict, dataclass, field
from pathlib import Path

from .checklist import BONDING_DEXES
from .config import Config


def pumpswap_fee_pct(cfg: Config, mcap_sol: float) -> float:
    """PumpSwap's total fee for a coin at this market cap (in SOL)."""
    tiers = sorted((float(a), float(b)) for a, b in
                   (t.split(":") for t in cfg.pumpswap_fee_tiers.split(",") if t.strip()))
    fee = tiers[0][1] if tiers else cfg.other_dex_fee_pct
    for start, pct in tiers:
        if mcap_sol >= start:
            fee = pct
    return fee


def venue_fee_pct(cfg: Config, dex: str | None, mcap_usd: float, sol_usd: float) -> float:
    """The pool's own fee, which DexScreener's price doesn't include."""
    d = (dex or "").lower()
    if d in BONDING_DEXES:
        return cfg.pumpfun_curve_fee_pct
    if d == "pumpswap":
        return pumpswap_fee_pct(cfg, mcap_usd / sol_usd if sol_usd else 0.0)
    return cfg.other_dex_fee_pct


def network_fee_usd(cfg: Config, sol_usd: float) -> float:
    """Solana costs of one transaction: base fee + priority fee + Jito tip."""
    return (cfg.network_fee_sol + cfg.priority_fee_sol + cfg.bribe_sol) * sol_usd


def breakeven_price(cfg: Config, pos: "Position", liquidity_usd: float, venue_pct: float,
                    net_fee_usd: float) -> float:
    """Price at which selling all of `pos` brings back what's left of its cost after
    slippage, Axiom and pool fees and the sell's network fee (the same math as sell())."""
    owed = pos.cost_usd - pos.realized_usd
    if pos.tokens <= 0 or owed <= 0:
        return 0.0
    keep = 1 - (cfg.platform_fee_pct + venue_pct) / 100
    gross = owed + net_fee_usd
    for _ in range(20):  # slippage depends on how much is sold: settle it by iteration
        gross = (owed + net_fee_usd) / (keep * (1 - Portfolio._slippage(cfg, gross, liquidity_usd)))
    return gross / pos.tokens


@dataclass
class Position:
    id: str
    address: str
    symbol: str
    setup: str
    opened_at: float
    entry_price: float  # effective fill price incl. slippage
    tokens: float
    cost_usd: float  # total USD spent incl. fees
    entry_mcap: float
    entry_liquidity: float
    peak_price: float
    initials_taken: bool = False
    realized_usd: float = 0.0  # proceeds from partial sells
    last_price: float = 0.0
    exit_plan: dict = field(default_factory=dict)
    thesis: str = ""
    entry_holders: dict = field(default_factory=dict)  # holder stats at entry, to spot a bundle exit
    stop_reviews: int = 0  # times the brain chose to hold through the stop
    dex: str = ""
    venue_fee_pct: float = 0.0  # pool fee paid on entry
    network_fee_usd: float = 0.0  # per-transaction network cost at entry
    fees_usd: float = 0.0  # all fees paid on this position, both ways
    slippage_usd: float = 0.0  # value lost to slippage, both ways

    def value(self, price: float | None = None) -> float:
        return self.tokens * (price if price is not None else self.last_price or self.entry_price)


@dataclass
class Portfolio:
    cash_usd: float
    positions: dict[str, Position] = field(default_factory=dict)
    day: str = ""
    day_start_equity: float = 0.0
    realized_pnl_usd: float = 0.0
    fees_paid_usd: float = 0.0
    fees_by_kind: dict = field(default_factory=dict)  # axiom / pool / network → USD
    slippage_paid_usd: float = 0.0
    trades_closed: int = 0
    wins: int = 0
    started_at: float = field(default_factory=time.time)

    # ---------------------------------------------------------------- state
    @classmethod
    def load(cls, cfg: Config) -> "Portfolio":
        path = cfg.memory_dir / "state.json"
        if not path.exists():
            p = cls(cash_usd=cfg.starting_cash_usd)
            p.day_start_equity = cfg.starting_cash_usd
            return p
        raw = json.loads(path.read_text())
        raw["positions"] = {k: Position(**v) for k, v in raw.get("positions", {}).items()}
        return cls(**raw)

    def save(self, cfg: Config) -> None:
        path: Path = cfg.memory_dir / "state.json"
        tmp = path.with_suffix(".tmp")
        data = asdict(self)
        tmp.write_text(json.dumps(data, indent=2))
        os.replace(tmp, path)

    # ---------------------------------------------------------------- views
    def equity(self) -> float:
        return self.cash_usd + sum(p.value() for p in self.positions.values())

    def holds(self, address: str) -> bool:
        return any(p.address == address for p in self.positions.values())

    def roll_day(self) -> None:
        today = time.strftime("%Y-%m-%d", time.gmtime())
        if self.day != today:
            self.day = today
            self.day_start_equity = self.equity()

    def can_open(self, cfg: Config) -> tuple[bool, str]:
        eq = self.equity()
        if eq < cfg.broke_equity_usd:
            return False, f"equity ${eq:.2f} below ${cfg.broke_equity_usd} — Trencher is broke"
        if cfg.max_open_positions and len(self.positions) >= cfg.max_open_positions:
            return False, "max open positions"
        if self.day_start_equity and eq < self.day_start_equity * (1 - cfg.daily_loss_limit_pct / 100):
            return False, f"daily loss limit hit ({cfg.daily_loss_limit_pct}%)"
        if self.cash_usd < cfg.min_position_usd + 0.5:
            return False, "not enough cash"
        return True, ""

    # ---------------------------------------------------------------- fills
    @staticmethod
    def _slippage(cfg: Config, size_usd: float, liquidity_usd: float) -> float:
        """Fractional price impact: base spread + constant-product impact on the
        quote side (~half of the reported liquidity)."""
        quote_side = max(liquidity_usd / 2, 1.0)
        impact = size_usd / (quote_side + size_usd)
        return min(cfg.max_slippage_pct / 100, cfg.base_slippage_pct / 100 + impact)

    def _charge(self, pos: Position, axiom: float, pool: float, network: float, slippage: float) -> float:
        fees = axiom + pool + network
        for kind, usd in (("axiom", axiom), ("pool", pool), ("network", network)):
            self.fees_by_kind[kind] = round(self.fees_by_kind.get(kind, 0.0) + usd, 6)
        self.fees_paid_usd += fees
        self.slippage_paid_usd += slippage
        pos.fees_usd += fees
        pos.slippage_usd += slippage
        return fees

    def buy(self, cfg: Config, snap: dict, size_usd: float, sol_usd: float, setup: str,
            exit_plan: dict, thesis: str) -> Position:
        size_usd = min(size_usd, self.cash_usd)
        venue = venue_fee_pct(cfg, snap.get("dex"), snap["mcap_usd"], sol_usd)
        net_fee = network_fee_usd(cfg, sol_usd)
        axiom = size_usd * cfg.platform_fee_pct / 100
        pool = size_usd * venue / 100
        spend = size_usd - axiom - pool - net_fee
        if spend <= 0:
            raise ValueError(f"${size_usd:.2f} doesn't cover the ${axiom + pool + net_fee:.2f} in fees")
        slip = self._slippage(cfg, spend, snap["liquidity_usd"])
        fill = snap["price_usd"] * (1 + slip)
        pos = Position(
            id=uuid.uuid4().hex[:8],
            address=snap["address"],
            symbol=snap["symbol"] or "?",
            setup=setup,
            opened_at=time.time(),
            entry_price=fill,
            tokens=spend / fill,
            cost_usd=size_usd,
            entry_mcap=snap["mcap_usd"],
            entry_liquidity=snap["liquidity_usd"],
            peak_price=snap["price_usd"],
            last_price=snap["price_usd"],
            exit_plan=exit_plan,
            thesis=thesis,
            dex=snap.get("dex") or "",
            venue_fee_pct=venue,
            network_fee_usd=net_fee,
        )
        self.cash_usd -= size_usd
        self._charge(pos, axiom, pool, net_fee, spend - spend / (1 + slip))
        self.positions[pos.id] = pos
        return pos

    def sell(self, cfg: Config, pos: Position, fraction: float, price: float, liquidity_usd: float,
             sol_usd: float, rugged: bool = False, dex: str | None = None, mcap_usd: float | None = None) -> float:
        """Sell `fraction` of the position. Returns USD proceeds after costs. `dex` and
        `mcap_usd` are where the coin trades now (it may have migrated since entry)."""
        fraction = max(0.0, min(1.0, fraction))
        tokens = pos.tokens * fraction
        gross = tokens * price
        if rugged or liquidity_usd < 500:
            proceeds = 0.0
        else:
            slippage = gross * self._slippage(cfg, gross, liquidity_usd)
            gross -= slippage
            venue = (venue_fee_pct(cfg, dex, mcap_usd or 0.0, sol_usd) if dex is not None
                     else pos.venue_fee_pct or cfg.other_dex_fee_pct)
            axiom = gross * cfg.platform_fee_pct / 100
            pool = gross * venue / 100
            fees = self._charge(pos, axiom, pool, network_fee_usd(cfg, sol_usd), slippage)
            proceeds = max(0.0, gross - fees)
        pos.tokens -= tokens
        pos.realized_usd += proceeds
        self.cash_usd += proceeds
        return proceeds

    def costs_view(self) -> dict:
        return {"fees_paid_usd": round(self.fees_paid_usd, 2),
                "fees_by_kind_usd": {k: round(v, 2) for k, v in sorted(self.fees_by_kind.items())},
                "slippage_paid_usd": round(self.slippage_paid_usd, 2)}

    def close(self, pos: Position) -> float:
        """Remove a fully sold position, book the PnL, return it."""
        pnl = pos.realized_usd - pos.cost_usd
        self.realized_pnl_usd += pnl
        self.trades_closed += 1
        self.wins += pnl > 0
        self.positions.pop(pos.id, None)
        return pnl
