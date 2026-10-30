"""Exit rules: take initials, stop loss, break-even stop, sell on fading volume,
trailing stop, time stop, target, rug detection. The brain proposes an exit plan; this code enforces it with the
config's limits as the floor ("plan the exit before the entry", V1, V11)."""

from __future__ import annotations

import time
from dataclasses import dataclass

from .config import Config
from .portfolio import Position, breakeven_price, network_fee_usd, venue_fee_pct


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


def breakeven_stop(pos: Position, snap: dict, cfg: Config, sol_usd: float = 0.0) -> float:
    """The price the break-even stop sells at: selling everything there gets back what's
    left of the cost after the sell's fees, plus a buffer. Never below the entry fill."""
    if sol_usd:
        venue = venue_fee_pct(cfg, snap.get("dex"), snap["mcap_usd"], sol_usd)
        net = network_fee_usd(cfg, sol_usd)
    else:  # no SOL price this tick: use what the entry paid
        venue, net = pos.venue_fee_pct or cfg.other_dex_fee_pct, pos.network_fee_usd
    be = breakeven_price(cfg, pos, snap["liquidity_usd"], venue, net)
    return max(pos.entry_price, be * (1 + cfg.breakeven_buffer_pct / 100))


def volume_pace(snap: dict) -> float | None:
    """5m volume vs the last hour's average 5m volume (1.0 = keeping pace)."""
    hour = snap.get("vol_1h") or 0
    return (snap.get("vol_5m") or 0) / (hour / 12) if hour else None


def check_exit(pos: Position, snap: dict, cfg: Config, now: float | None = None,
               sol_usd: float = 0.0) -> ExitSignal | None:
    now = now or time.time()
    price = snap["price_usd"]
    if not pos.exit_plan:
        pos.exit_plan = default_exit_plan(cfg)
    plan = pos.exit_plan
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

    # Break-even stop: once it has run far enough, a winner can't turn into a loss.
    # It sells outright (no review), and before the % stop so a gap down still sells here.
    be_stop = 0.0
    if not pos.initials_taken:
        be_stop = breakeven_stop(pos, snap, cfg, sol_usd)
        arm = max(cfg.breakeven_arm_multiple * pos.entry_price, be_stop * (1 + cfg.breakeven_arm_room_pct / 100))
        if pos.peak_price >= arm:
            plan["_be_armed"] = True
        if plan.get("_be_armed") and price <= be_stop:
            return ExitSignal(1.0, f"break-even stop: peaked {pos.peak_price / pos.entry_price:.2f}x, "
                                   f"back to {multiple:.2f}x")

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

    # Fading volume while green and initials still in: the crowd is leaving, so bank some
    # before it round-trips. A free runner is left to the trailing stop.
    pace = volume_pace(snap)
    green = ((pos.initials_taken and cfg.fade_trims_runner)
             or (not pos.initials_taken and plan.get("_be_armed") and price > be_stop))
    if green and not plan.get("_fade_sold") and pace is not None and pace < cfg.fade_volume_ratio:
        since = plan.setdefault("_fade_since", now)
        if now - since >= cfg.fade_confirm_sec:
            plan["_fade_sold"] = True
            plan.pop("_fade_since", None)
            piece = pos.tokens * price * cfg.fade_sell_fraction
            frac = cfg.fade_sell_fraction if piece >= cfg.fade_min_partial_usd else 1.0
            return ExitSignal(frac, f"5m volume faded to {pace:.2f}x its hourly pace at {multiple:.2f}x")
    else:
        plan.pop("_fade_since", None)

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
