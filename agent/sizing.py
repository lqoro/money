"""Conviction-based position sizing.

Only risk what you're willing to lose (V8): conviction decides how much of the
wallet you're willing to lose on this idea, and the stop decides how big the
position can be for that loss to be the most you lose.

    risk_usd = equity × risk%(conviction)
    size     = (risk_usd − 2 × network fee) ÷ (stop distance + round-trip % costs)

Network fees are a flat amount per transaction, so on a small position they eat
a big share of the risk: when they'd eat all of it, the trade isn't worth taking.

So a high-conviction coin with a tight stop gets a big position, and a coin
you're unsure about with a wide stop gets a small one. Caps keep any one rug
(which skips the stop) and the total open risk survivable.
"""

from __future__ import annotations

from dataclasses import dataclass

from .config import Config
from .portfolio import Portfolio, network_fee_usd


def risk_table(cfg: Config) -> dict[int, float]:
    table = {}
    for pair in cfg.conviction_risk_pct.split(","):
        k, v = pair.split(":")
        table[int(k)] = float(v)
    return table


def risk_pct_for(conviction: int, cfg: Config) -> float:
    conviction = max(1, min(10, int(conviction)))
    return risk_table(cfg).get(conviction, 0.0)


def loss_at_stop_frac(stop_loss_pct: float, cfg: Config, venue_pct: float | None = None) -> float:
    """Fraction of the position lost if the stop is hit, incl. % fees and slippage both
    ways. Flat network fees come on top (see position_size)."""
    venue = cfg.other_dex_fee_pct if venue_pct is None else venue_pct
    costs = 2 * (cfg.platform_fee_pct + venue + cfg.base_slippage_pct)
    return (stop_loss_pct + costs) / 100


def open_risk_usd(pf: Portfolio, cfg: Config) -> float:
    """At-stop risk still on the table. Positions with initials out are free rides."""
    total = 0.0
    for p in pf.positions.values():
        if p.initials_taken:
            continue
        stop = (p.exit_plan or {}).get("stop_loss_pct", cfg.stop_loss_pct)
        total += p.cost_usd * loss_at_stop_frac(stop, cfg, p.venue_fee_pct or None) + 2 * p.network_fee_usd
    return total


@dataclass
class Sizing:
    size_usd: float
    risk_usd: float
    risk_pct: float
    note: str


def position_size(conviction: int, stop_loss_pct: float, pf: Portfolio, cfg: Config,
                  sol_usd: float = 0.0, venue_pct: float | None = None) -> Sizing:
    equity = pf.equity()
    risk_pct = risk_pct_for(conviction, cfg)
    if risk_pct <= 0:
        return Sizing(0.0, 0.0, 0.0, f"conviction {conviction}/10 is not worth risking money on")

    per_dollar_loss = loss_at_stop_frac(stop_loss_pct, cfg, venue_pct)
    fixed = 2 * network_fee_usd(cfg, sol_usd)  # buy + sell transactions
    risk_usd = equity * risk_pct / 100
    note = f"conviction {conviction}/10 → risk {risk_pct:g}% (${risk_usd:.2f}) with a {stop_loss_pct:.0f}% stop"
    if risk_usd <= fixed:
        return Sizing(0.0, 0.0, risk_pct, note + f", but ${fixed:.2f} of network fees would eat all of it")
    size = (risk_usd - fixed) / per_dollar_loss

    caps = {
        "max position": equity * cfg.max_position_pct / 100,
        "cash": pf.cash_usd - 0.25,
        "total risk budget": max(0.0, equity * cfg.max_total_risk_pct / 100 - open_risk_usd(pf, cfg) - fixed)
        / per_dollar_loss,
    }
    binding = min(caps, key=caps.get)
    if caps[binding] < size:
        size = max(0.0, caps[binding])
        note += f", capped by {binding}"
    return Sizing(round(size, 2), round(size * per_dollar_loss + (fixed if size else 0), 2), risk_pct, note)


def cost_note(cfg: Config, sol_usd: float, venue_pct: float | None = None) -> str:
    """What one round trip costs, in words, for the brain's prompt."""
    venue = cfg.other_dex_fee_pct if venue_pct is None else venue_pct
    net = network_fee_usd(cfg, sol_usd)
    return (f"Every trade pays real costs (as on Axiom): {cfg.platform_fee_pct:g}% Axiom fee + {venue:g}% pool fee "
            f"each way, ${net:.2f} of network fees per transaction (priority + tip), and slippage "
            f"({cfg.base_slippage_pct:g}% + price impact). A $5 round trip at an unchanged price loses about "
            f"${5 * 2 * (cfg.platform_fee_pct + venue + cfg.base_slippage_pct) / 100 + 2 * net:.2f}. "
            f"So a round trip always costs at least {2 * (cfg.platform_fee_pct + venue + cfg.base_slippage_pct):g}% "
            f"+ ${2 * net:.2f} at any size: that's the price of a trade, so judge whether the upside beats it, "
            f"don't pass just because it exists.")


def sizing_guide(pf: Portfolio, cfg: Config, stop_loss_pct: float | None = None,
                 sol_usd: float = 0.0, venue_pct: float | None = None) -> str:
    """Human-readable table for the brain's prompt."""
    stop = stop_loss_pct or cfg.stop_loss_pct
    rows = [cost_note(cfg, sol_usd, venue_pct)] if sol_usd else []
    for c, r in sorted(risk_table(cfg).items()):
        if r <= 0:
            continue
        s = position_size(c, stop, pf, cfg, sol_usd, venue_pct)
        rows.append(f"  conviction {c:>2}: risk {r:g}% of equity → ~${s.size_usd:.2f} position at a {stop:.0f}% stop"
                    + ("" if s.size_usd else " (not worth it after fees)"))
    return "\n".join(rows)
