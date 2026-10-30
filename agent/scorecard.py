"""After-fees scorecard: what Trencher's closed trades actually made once Axiom,
pool and network fees and slippage are paid, and which exits are working.

Computed from the CLOSE records in trades.jsonl, so it covers every closed trade,
not just the last few in the report. All money figures are after costs unless
labelled gross (gross = what the trade would have made with no fees or slippage).
"""

from __future__ import annotations

# Order matters: the first keyword found in a trade's final exit reason names it.
EXIT_KINDS = (
    ("rug", "rug"),
    ("hard stop", "hard stop"),
    ("held through the stop", "stop review ran out"),
    ("trailing", "trailing stop"),
    ("stop loss", "stop loss"),
    ("time stop", "time stop"),
    ("target", "target"),
    ("max hold", "max hold"),
    ("initials", "initials"),
)
RED_AFTER_PEAK_X = 1.5  # a trade that got this far and still closed red should have been a win


def exit_kind(close: dict) -> str:
    reason = ((close.get("exit_reasons") or ["?"])[-1] or "?").lower()
    return next((kind for key, kind in EXIT_KINDS if key in reason), "other")


def _f(t: dict, key: str) -> float:
    try:
        return float(t.get(key) or 0)
    except (TypeError, ValueError):
        return 0.0


def _group(closes: list[dict]) -> dict:
    pnls = [_f(t, "pnl_usd") for t in closes]
    wins = [p for p in pnls if p > 0]
    losses = [p for p in pnls if p <= 0]
    fees = sum(_f(t, "fees_usd") for t in closes)
    slip = sum(_f(t, "slippage_usd") for t in closes)
    net = sum(pnls)
    peaks = [_f(t, "peak_multiple") for t in closes if _f(t, "peak_multiple") > 0]
    banked = [_f(t, "proceeds_usd") / _f(t, "cost_usd") for t in closes if _f(t, "cost_usd") > 0]
    n = len(closes)
    return {
        "trades": n,
        "wins": len(wins),
        "win_rate_pct": round(100 * len(wins) / n) if n else 0,
        "net_usd": round(net, 2),
        "avg_net_usd": round(net / n, 2) if n else 0.0,
        "avg_win_usd": round(sum(wins) / len(wins), 2) if wins else None,
        "avg_loss_usd": round(sum(losses) / len(losses), 2) if losses else None,
        "fees_usd": round(fees, 2),
        "slippage_usd": round(slip, 2),
        "gross_usd": round(net + fees + slip, 2),
        "avg_peak_x": round(sum(peaks) / len(peaks), 2) if peaks else None,
        "avg_banked_x": round(sum(banked) / len(banked), 2) if banked else None,
    }


def build(trades: list[dict], equity_usd: float, goal: dict | None = None) -> dict:
    """The scorecard as data (for status.json and the hourly PnL post)."""
    closes = [t for t in trades if t.get("event") == "CLOSE"]
    card = _group(closes)
    gross = card["gross_usd"]
    costs = card["fees_usd"] + card["slippage_usd"]
    card["costs_pct_of_gross"] = round(100 * costs / gross) if gross > 0 else None
    card["red_after_peak"] = [
        {"symbol": t.get("symbol"), "ca": t.get("ca") or t.get("token"),
         "peak_x": _f(t, "peak_multiple"), "pnl_usd": _f(t, "pnl_usd")}
        for t in closes if _f(t, "peak_multiple") >= RED_AFTER_PEAK_X and _f(t, "pnl_usd") <= 0
    ]
    kinds: dict[str, list[dict]] = {}
    for t in closes:
        kinds.setdefault(exit_kind(t), []).append(t)
    card["by_exit"] = {k: _group(v) for k, v in sorted(kinds.items(), key=lambda kv: (-len(kv[1]), kv[0]))}
    if goal:
        to_go = max(0.0, goal["target_usd"] - equity_usd)
        avg = card["avg_net_usd"]
        card["goal"] = {"target_usd": goal["target_usd"], "to_go_usd": round(to_go, 2),
                        "trades_needed_at_this_pace": (int(-(-to_go // avg)) if avg > 0 and to_go else None)}
    return card


def _usd(x: float | None) -> str:
    return "n/a" if x is None else f"${x:+.2f}"


def lines(card: dict) -> list[str]:
    """The scorecard as short Markdown lines that read on a phone."""
    out = ["## Scorecard (after fees)"]
    if not card["trades"]:
        return out + ["- no closed trades yet"]
    out.append(f"- {card['trades']} closed, {card['wins']} won ({card['win_rate_pct']}%), net {_usd(card['net_usd'])}")
    out.append(f"- Per trade (expectancy) {_usd(card['avg_net_usd'])}; avg win {_usd(card['avg_win_usd'])}, "
               f"avg loss {_usd(card['avg_loss_usd'])}")
    costs = card["fees_usd"] + card["slippage_usd"]
    share = (f", {card['costs_pct_of_gross']}% of it" if card["costs_pct_of_gross"] is not None
             else ", on top of a gross loss")
    out.append(f"- Gross {_usd(card['gross_usd'])}; costs ${costs:.2f} (fees ${card['fees_usd']:.2f}"
               f" + slippage ${card['slippage_usd']:.2f}){share}")
    if card["avg_peak_x"] is not None:
        out.append(f"- Give-back: peaked {card['avg_peak_x']:g}x on average, banked {card['avg_banked_x']:g}x")
    red = card["red_after_peak"]
    if red:
        out.append(f"- Hit {RED_AFTER_PEAK_X:g}x+ and still closed red: {len(red)}")
        out += [f"  - {r['symbol']} peaked {r['peak_x']:g}x, {_usd(r['pnl_usd'])}  \n    CA `{r['ca']}`" for r in red]
    out.append("- By exit:")
    for kind, g in card["by_exit"].items():
        out.append(f"  - {kind}: {g['trades']}, {g['wins']} won, net {_usd(g['net_usd'])}, "
                   f"fees+slip ${g['fees_usd'] + g['slippage_usd']:.2f}"
                   + (f", peak {g['avg_peak_x']:g}x → {g['avg_banked_x']:g}x" if g["avg_peak_x"] is not None else ""))
    goal = card.get("goal")
    if goal:
        need = goal["trades_needed_at_this_pace"]
        out.append(f"- To ${goal['target_usd']:,.0f}: ${goal['to_go_usd']:,.2f} to go; "
                   + (f"about {need} more trades at {_usd(card['avg_net_usd'])} each" if need
                      else f"at {_usd(card['avg_net_usd'])} a trade this pace doesn't get there"
                      if goal["to_go_usd"] else "reached"))
    return out
