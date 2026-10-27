"""Paper wallet. Starts with $100 cash and simulates fills with fees, priority
fees and price impact so paper results aren't fantasy numbers."""

from __future__ import annotations

import json
import os
import time
import uuid
from dataclasses import asdict, dataclass, field
from pathlib import Path

from .config import Config


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
        if len(self.positions) >= cfg.max_open_positions:
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

    def buy(self, cfg: Config, snap: dict, size_usd: float, sol_usd: float, setup: str,
            exit_plan: dict, thesis: str) -> Position:
        size_usd = min(size_usd, self.cash_usd)
        fees = size_usd * cfg.platform_fee_pct / 100 + cfg.priority_fee_sol * sol_usd
        spend = size_usd - fees
        fill = snap["price_usd"] * (1 + self._slippage(cfg, spend, snap["liquidity_usd"]))
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
        )
        self.cash_usd -= size_usd
        self.fees_paid_usd += fees
        self.positions[pos.id] = pos
        return pos

    def sell(self, cfg: Config, pos: Position, fraction: float, price: float, liquidity_usd: float,
             sol_usd: float, rugged: bool = False) -> float:
        """Sell `fraction` of the position. Returns USD proceeds after costs."""
        fraction = max(0.0, min(1.0, fraction))
        tokens = pos.tokens * fraction
        gross = tokens * price
        if rugged or liquidity_usd < 500:
            proceeds = 0.0
            fees = 0.0
        else:
            gross *= 1 - self._slippage(cfg, gross, liquidity_usd)
            fees = gross * cfg.platform_fee_pct / 100 + cfg.priority_fee_sol * sol_usd
            proceeds = max(0.0, gross - fees)
        pos.tokens -= tokens
        pos.realized_usd += proceeds
        self.cash_usd += proceeds
        self.fees_paid_usd += fees
        return proceeds

    def close(self, pos: Position) -> float:
        """Remove a fully sold position, book the PnL, return it."""
        pnl = pos.realized_usd - pos.cost_usd
        self.realized_pnl_usd += pnl
        self.trades_closed += 1
        self.wins += pnl > 0
        self.positions.pop(pos.id, None)
        return pnl
