"""Replay closed trades to see where the money went: picks, the stop, or the costs.

    python -m agent replay                 # this machine's memory/trades.jsonl
    python -m agent replay --file x.json   # a saved list of CLOSE records

It answers three questions from the log alone (no market data needed):

1. Did the picks make money before costs? gross = net + fees + slippage.
2. How far past the stop did stop-loss exits land, and how much of that was the price
   moving between checks versus the round trip's fees and slippage?
3. What would the same price moves have netted at another size, or with a lower
   priority fee and tip? Percentage costs scale with size; the network fee per
   transaction doesn't, so small positions pay more of it.

These are what-ifs on the logged moves, not a backtest: a different size or fee would
not have changed what the coin did, but it can't show trades that weren't taken.
"""

from __future__ import annotations

import json
import re
from pathlib import Path

STOP_TRIGGER = re.compile(r"stop loss -(\d+(?:\.\d+)?)% hit \((\d+(?:\.\d+)?)x\)")


def load_closes(path: str | Path | None, cfg=None) -> tuple[list[dict], dict]:
    """CLOSE records and, when the file has them, its fee totals and paper costs."""
    if path is None:
        from . import journal
        return [t for t in journal.read_trades(cfg) if t.get("event") == "CLOSE"], {}
    p = Path(path)
    if p.suffix == ".jsonl":
        rows = [json.loads(line) for line in p.read_text().splitlines() if line.strip()]
        return [r for r in rows if r.get("event") == "CLOSE"], {}
    raw = json.loads(p.read_text())
    if isinstance(raw, list):
        return [r for r in raw if r.get("event", "CLOSE") == "CLOSE"], {}
    return raw.get("closes", []), {k: v for k, v in raw.items() if k != "closes"}


def exit_kind(trade: dict) -> str:
    last = (trade.get("exit_reasons") or [""])[-1]
    for kind in ("break-even stop", "stop loss", "trailing stop", "time stop", "hard stop"):
        if kind in last:
            return kind
    return "other"


def sells(trade: dict) -> int:
    """Sell transactions: every exit reason except the stop-review notes."""
    return max(1, sum(1 for r in trade.get("exit_reasons") or [] if not r.startswith("stop review")))


def gross(trade: dict) -> float:
    return trade["pnl_usd"] + trade["fees_usd"] + trade["slippage_usd"]


def network_per_tx(closes: list[dict], fees_by_kind: dict | None) -> float:
    """Average network cost of one transaction, from the wallet's fee totals."""
    txs = sum(1 + sells(t) for t in closes)
    net = (fees_by_kind or {}).get("network")
    return net / txs if net and txs else 0.0


def what_if(closes: list[dict], size_usd: float | None = None, network_scale: float = 1.0,
            net_per_tx: float = 0.0) -> float:
    """Net PnL of the logged moves at another size and/or another network fee.

    A trade's percentage costs (platform, pool, slippage) scale with its size; its network
    fees (net_per_tx per transaction) are fixed per transaction and scale by network_scale."""
    total = 0.0
    for t in closes:
        cost = t["cost_usd"] or 1.0
        network = net_per_tx * (1 + sells(t))
        pct_costs = t["fees_usd"] + t["slippage_usd"] - network
        scale = (size_usd / cost) if size_usd else 1.0
        total += gross(t) * scale - pct_costs * scale - network * network_scale
    return total


def analyse(closes: list[dict], meta: dict | None = None) -> dict:
    meta = meta or {}
    n = len(closes)
    net = sum(t["pnl_usd"] for t in closes)
    costs = sum(t["fees_usd"] + t["slippage_usd"] for t in closes)
    out: dict = {"trades": n, "net_usd": round(net, 2), "gross_usd": round(net + costs, 2),
                 "costs_usd": round(costs, 2),
                 "avg_cost_pct_of_position": round(100 * costs / max(1e-9, sum(t["cost_usd"] for t in closes)), 1)}

    kinds: dict[str, dict] = {}
    for t in closes:
        k = kinds.setdefault(exit_kind(t), {"n": 0, "net_usd": 0.0, "gross_usd": 0.0, "never_green": 0})
        k["n"] += 1
        k["net_usd"] = round(k["net_usd"] + t["pnl_usd"], 2)
        k["gross_usd"] = round(k["gross_usd"] + gross(t), 2)
        k["never_green"] += (t.get("peak_multiple") or 0) <= 1.02
    out["by_exit"] = kinds
    out["never_green"] = sum(1 for t in closes if (t.get("peak_multiple") or 0) <= 1.02)
    plan_x = [(t.get("exit_plan") or {}).get("take_initials_multiple") or 2.0 for t in closes]
    out["reached_initials"] = sum(1 for t, x in zip(closes, plan_x) if (t.get("peak_multiple") or 0) >= x)

    # Stop-loss exits: where the stop fired vs where it was set, and the costs on top.
    stops = []
    for t in closes:
        for r in t.get("exit_reasons") or []:
            m = STOP_TRIGGER.search(r)
            if m:
                stops.append({"symbol": t["symbol"], "stop_pct": float(m.group(1)), "fired_x": float(m.group(2)),
                              "pnl_pct": t["pnl_pct"], "reviewed": bool(t.get("stop_reviews"))})
                break
    if stops:
        gap = [100 * ((1 - s["stop_pct"] / 100) - s["fired_x"]) for s in stops]
        moved = [100 * (s["fired_x"] - 1) for s in stops]
        out["stop_losses"] = {
            "n": len(stops),
            "avg_closed_pct": round(sum(s["pnl_pct"] for s in stops) / len(stops), 1),
            "avg_points_past_the_stop_when_it_fired": round(sum(gap) / len(gap), 1),
            "avg_points_lost_to_costs": round(sum(s["pnl_pct"] - m for s, m in zip(stops, moved)) / len(stops), 1),
            "reviewed": sum(s["reviewed"] for s in stops),
        }

    npt = network_per_tx(closes, meta.get("fees_by_kind_usd"))
    out["network_per_tx_usd"] = round(npt, 3)
    if npt:
        costs_cfg = meta.get("paper_costs") or {}
        sol_per_tx = (costs_cfg.get("priority_fee_sol", 0.001) + costs_cfg.get("bribe_sol", 0.001) + 0.000005)
        lean = (0.0002 + 0.000005) / sol_per_tx  # 0.0002 SOL priority, no tip
        out["what_if"] = {
            "as_logged": round(what_if(closes, net_per_tx=npt), 2),
            "every_trade_25usd": round(what_if(closes, 25.0, net_per_tx=npt), 2),
            "every_trade_10usd": round(what_if(closes, 10.0, net_per_tx=npt), 2),
            "no_costs_at_all": round(sum(gross(t) for t in closes), 2),
            "priority_0.0002_sol_no_tip": round(what_if(closes, network_scale=lean, net_per_tx=npt), 2),
        }
    return out


def render(a: dict) -> str:
    lines = [f"{a['trades']} closed trades: net ${a['net_usd']:+.2f} = gross ${a['gross_usd']:+.2f} "
             f"minus costs ${a['costs_usd']:.2f} ({a['avg_cost_pct_of_position']}% of what went in)",
             f"Never went green (peak <= 1.02x): {a['never_green']}. Reached the initials target: {a['reached_initials']}.",
             "By exit:"]
    for k, v in sorted(a["by_exit"].items(), key=lambda kv: kv[1]["net_usd"]):
        lines.append(f"  {k}: {v['n']} trades, net ${v['net_usd']:+.2f}, gross ${v['gross_usd']:+.2f}, "
                     f"never green {v['never_green']}")
    s = a.get("stop_losses")
    if s:
        lines.append(f"Stop losses: {s['n']}, closed {s['avg_closed_pct']}% on average. The stop fired "
                     f"{s['avg_points_past_the_stop_when_it_fired']} points past its level (price moved between "
                     f"checks); costs took another {-s['avg_points_lost_to_costs']} points. Reviewed first: {s['reviewed']}.")
    w = a.get("what_if")
    if w:
        lines.append(f"Network cost per transaction: ${a['network_per_tx_usd']:.3f}")
        lines.append("Same price moves, other settings:")
        for k, v in w.items():
            lines.append(f"  {k}: ${v:+.2f}")
    return "\n".join(lines)


def main(path: str | None = None, cfg=None) -> None:
    closes, meta = load_closes(path, cfg)
    if not closes:
        print("No closed trades to replay.")
        return
    print(render(analyse(closes, meta)))
