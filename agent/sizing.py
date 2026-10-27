"""Conviction-based position sizing.

Only risk what you're willing to lose (V8): conviction decides how much of the
wallet you're willing to lose on this idea, and the stop decides how big the
position can be for that loss to be the most you lose.

    risk_usd = equity × risk%(conviction)
    size     = risk_usd ÷ (stop distance + round-trip costs)

So a high-conviction coin with a tight stop gets a big position, and a coin
you're unsure about with a wide stop gets a small one. Caps keep any one rug
(which skips the stop) and the total open risk survivable.
"""

from __future__ import annotations

from dataclasses import dataclass

from .config import Config
from .portfolio import Portfolio


def risk_table(cfg: Config) -> dict[int, float]:
    table = {}
    for pair in cfg.conviction_risk_pct.split(","):
        k, v = pair.split(":")
        table[int(k)] = float(v)
    return table


def risk_pct_for(conviction: int, cfg: Config) -> float:
    conviction = max(1, min(10, int(conviction)))
    return risk_table(cfg).get(conviction, 0.0)


def loss_at_stop_frac(stop_loss_pct: float, cfg: Config) -> float:
    """Fraction of the position lost if the stop is hit, incl. fees and slippage both ways."""
    costs = 2 * (cfg.platform_fee_pct + cfg.base_slippage_pct)
    return (stop_loss_pct + costs) / 100


def open_risk_usd(pf: Portfolio, cfg: Config) -> float:
    """At-stop risk still on the table. Positions with initials out are free rides."""
    total = 0.0
    for p in pf.positions.values():
        if p.initials_taken:
            continue
        stop = (p.exit_plan or {}).get("stop_loss_pct", cfg.stop_loss_pct)
        total += p.cost_usd * loss_at_stop_frac(stop, cfg)
    return total


@dataclass
class Sizing:
    size_usd: float
    risk_usd: float
    risk_pct: float
    note: str


def position_size(conviction: int, stop_loss_pct: float, pf: Portfolio, cfg: Config) -> Sizing:
    equity = pf.equity()
    risk_pct = risk_pct_for(conviction, cfg)
    if risk_pct <= 0:
        return Sizing(0.0, 0.0, 0.0, f"conviction {conviction}/10 is not worth risking money on")

    per_dollar_loss = loss_at_stop_frac(stop_loss_pct, cfg)
    risk_usd = equity * risk_pct / 100
    size = risk_usd / per_dollar_loss
    note = f"conviction {conviction}/10 → risk {risk_pct:g}% (${risk_usd:.2f}) with a {stop_loss_pct:.0f}% stop"

    caps = {
        "max position": equity * cfg.max_position_pct / 100,
        "cash": pf.cash_usd - 0.25,
        "total risk budget": max(0.0, equity * cfg.max_total_risk_pct / 100 - open_risk_usd(pf, cfg)) / per_dollar_loss,
    }
    binding = min(caps, key=caps.get)
    if caps[binding] < size:
        size = max(0.0, caps[binding])
        note += f", capped by {binding}"
    return Sizing(round(size, 2), round(size * per_dollar_loss, 2), risk_pct, note)


def sizing_guide(pf: Portfolio, cfg: Config, stop_loss_pct: float | None = None) -> str:
    """Human-readable table for the brain's prompt."""
    stop = stop_loss_pct or cfg.stop_loss_pct
    rows = []
    for c, r in sorted(risk_table(cfg).items()):
        if r <= 0:
            continue
        s = position_size(c, stop, pf, cfg)
        rows.append(f"  conviction {c:>2}: risk {r:g}% of equity → ~${s.size_usd:.2f} position at a {stop:.0f}% stop")
    return "\n".join(rows)
