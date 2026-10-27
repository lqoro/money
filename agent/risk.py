"""Exit rules: take initials, stop loss, trailing stop, time stop, target,
rug detection. The brain proposes an exit plan; this code enforces it with the
config's limits as the floor ("plan the exit before the entry", V1, V11)."""

from __future__ import annotations

import time
from dataclasses import dataclass

from .config import Config
from .portfolio import Position


@dataclass
class ExitSignal:
    fraction: float  # of the remaining tokens
    reason: str
    rugged: bool = False
    review: bool = False  # stop hit: ask the brain whether this is a shakeout before selling


def default_exit_plan(cfg: Config) -> dict:
    return {
        "take_initials_multiple": cfg.take_initials_multiple,
        "stop_loss_pct": cfg.stop_loss_pct,
        "trailing_stop_pct": cfg.trailing_stop_pct,
        "time_stop_minutes": cfg.time_stop_minutes,
        "target_mcap_usd": None,
    }


def sanitize_exit_plan(plan: dict | None, cfg: Config) -> dict:
    """Merge the brain's plan over the defaults and clamp it to sane bounds, so
    a bad answer can't remove the stop."""
    out = default_exit_plan(cfg)
    for k, v in (plan or {}).items():
        if k in out and v is not None:
            out[k] = v
    out["take_initials_multiple"] = min(5.0, max(1.3, float(out["take_initials_multiple"])))
    out["stop_loss_pct"] = min(cfg.stop_loss_pct * 1.5, max(10.0, float(out["stop_loss_pct"])))
    out["trailing_stop_pct"] = min(60.0, max(15.0, float(out["trailing_stop_pct"])))
    out["time_stop_minutes"] = min(cfg.max_hold_hours * 60, max(10.0, float(out["time_stop_minutes"])))
    if out["target_mcap_usd"] is not None:
        out["target_mcap_usd"] = float(out["target_mcap_usd"]) or None
    return out


def check_exit(pos: Position, snap: dict, cfg: Config, now: float | None = None) -> ExitSignal | None:
    now = now or time.time()
    price = snap["price_usd"]
    plan = pos.exit_plan or default_exit_plan(cfg)
    held_min = (now - pos.opened_at) / 60

    # Rug: liquidity pulled or price nuked.
    if pos.entry_liquidity and snap["liquidity_usd"] < pos.entry_liquidity * (1 - cfg.rug_liquidity_drop_pct / 100):
        return ExitSignal(1.0, f"liquidity collapsed ${pos.entry_liquidity:,.0f} → ${snap['liquidity_usd']:,.0f} (rug)",
                          rugged=snap["liquidity_usd"] < 500)
    if price <= 0:
        return ExitSignal(1.0, "no price — treating as rugged", rugged=True)

    multiple = price / pos.entry_price

    # The floor no review can hold past.
    if multiple <= 1 - cfg.hard_stop_pct / 100:
        return ExitSignal(1.0, f"hard stop -{cfg.hard_stop_pct:.0f}% hit ({multiple:.2f}x)")

    # Held through the stop on a shakeout read: it had until the deadline to reclaim.
    hold_until = plan.get("hold_until")
    if hold_until and now >= hold_until:
        reclaim = 1 - plan.get("_orig_stop", plan["stop_loss_pct"]) / 100
        plan.pop("hold_until")
        if multiple < reclaim:
            return ExitSignal(1.0, f"held through the stop but no recovery by the deadline ({multiple:.2f}x)")
        plan["stop_loss_pct"] = plan.get("_orig_stop", plan["stop_loss_pct"])  # recovered: normal stop again

    # Stop loss. A stop is a decision point: if reviews are left, the brain looks at
    # why it hit (bundle dump with the narrative intact vs. a dead coin) first.
    if not pos.initials_taken and multiple <= 1 - plan["stop_loss_pct"] / 100:
        return ExitSignal(1.0, f"stop loss -{plan['stop_loss_pct']:.0f}% hit ({multiple:.2f}x)",
                          review=pos.stop_reviews < cfg.max_stop_reviews)

    # Take initials: sell enough to recover cost, ride the rest free (V2, V11).
    if not pos.initials_taken and multiple >= plan["take_initials_multiple"]:
        value = pos.tokens * price
        # Over-sell a little to cover fees/slippage on the way out.
        frac = min(0.9, (pos.cost_usd - pos.realized_usd) * 1.06 / value) if value else 1.0
        return ExitSignal(max(0.1, frac), f"took initials at {multiple:.2f}x")

    # Target market cap from the thesis: sell half of what's left.
    target = plan.get("target_mcap_usd")
    if target and snap["mcap_usd"] >= target and not plan.get("_target_hit"):
        plan["_target_hit"] = True
        return ExitSignal(0.5, f"target mcap ${target:,.0f} reached")

    # Trailing stop on the free ride.
    if pos.initials_taken and price <= pos.peak_price * (1 - plan["trailing_stop_pct"] / 100):
        return ExitSignal(1.0, f"trailing stop: -{plan['trailing_stop_pct']:.0f}% from peak")

    # Time stop: nothing happened, thesis was wrong.
    if (not pos.initials_taken and not plan.get("hold_until") and held_min >= plan["time_stop_minutes"]
            and multiple < 1 + cfg.time_stop_min_gain_pct / 100):
        return ExitSignal(1.0, f"time stop: {held_min:.0f} min and only {multiple:.2f}x")

    if held_min >= cfg.max_hold_hours * 60:
        return ExitSignal(1.0, f"max hold {cfg.max_hold_hours:.0f}h reached")
    return None
