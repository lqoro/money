"""Watch-only mode: Trencher keeps scanning, researching and deciding, but buys nothing.

Owner's call on Nov 3: pause trading for a week and collect the data to test rule sets
against real costs before any more paper money goes in. Every coin that passes the
market filters becomes an observation: the numbers it had at that moment, what the
checklist and the brain said about it, and whether Trencher would have bought it. Each
one is then followed for `watch_follow_hours`, sampled every `watch_sample_min`
minutes, so a rule set can be replayed offline against the real price path:

    x_at       price multiple at fixed checkpoints (5, 15, 30 ... 360 min)
    up_at      minutes until the price first reached 1.3x, 1.5x, 2x, 3x, 5x
    down_at    minutes until it first fell to 0.9x, 0.8x, 0.7x, 0.5x
    max_x/min_x and when the high came

Coins that just graduated from a launchpad's bonding curve (pump.fun and bonk.fun on Solana,
four.meme on BNB Chain; config migration_feeds) are logged at that moment even when they
don't pass the market filters (setup AT_MIGRATION unless another setup fits), with a
`migration` block: launchpad, chain, pool, minutes since the pool opened, and on Solana a
RugCheck holder snapshot. Off-Solana coins are only logged and followed, with no paper
costs modeled (avg_net_pct counts Solana coins only).

Live observations are kept in memory_dir/watch_live.json; settled ones are appended to
memory_dir/observations/YYYY-MM-DD.jsonl (UTC day they started), which the Duet bridge
copies to the trencher-live branch.
"""

from __future__ import annotations

import json
import time
from pathlib import Path

from . import data
from .config import Config

CHECKPOINTS_MIN = (5, 15, 30, 45, 60, 90, 120, 180, 240, 360)
UP_X = (1.3, 1.5, 2.0, 3.0, 5.0)
DOWN_X = (0.9, 0.8, 0.7, 0.5)

FEATURES = ("symbol", "name", "dex", "pair_address", "price_usd", "mcap_usd", "liquidity_usd", "vol_5m", "vol_1h",
            "vol_24h", "buys_5m", "sells_5m", "buys_1h", "sells_1h", "change_5m", "change_1h", "change_24h",
            "age_hours", "vol_5m_vs_hour_avg", "buy_ratio_5m", "boosts", "has_paid_profile", "peak_mcap_usd",
            "drawdown_pct", "bond_pct")


def _live_path(cfg: Config) -> Path:
    return cfg.memory_dir / "watch_live.json"


def obs_dir(cfg: Config) -> Path:
    return cfg.memory_dir / "observations"


def load(cfg: Config) -> dict:
    try:
        return json.loads(_live_path(cfg).read_text()) if _live_path(cfg).exists() else {}
    except ValueError:
        return {}


def save(cfg: Config, book: dict) -> None:
    _live_path(cfg).write_text(json.dumps(book))


def _key(ca: str, at: float) -> str:
    return f"{ca}:{int(at)}"


def current(book: dict, ca: str, now: float, cfg: Config) -> dict | None:
    """The newest observation of this coin still inside its re-observe window, if any."""
    best = None
    for rec in book.values():
        if rec["ca"] == ca and now - rec["at"] < cfg.watch_reobserve_min * 60:
            if best is None or rec["at"] > best["at"]:
                best = rec
    return best


def observe(cfg: Config, book: dict, snap: dict, setup: str | None, sol_usd: float = 0.0,
            now: float | None = None, chain: str = "solana") -> dict | None:
    """Open an observation for a coin that passed the market filters, unless it was
    observed within the last `watch_reobserve_min` minutes (then return that one)."""
    now = now or time.time()
    ca, price = snap.get("address"), float(snap.get("price_usd") or 0)
    if not ca or price <= 0:
        return None
    rec = current(book, ca, now, cfg)
    if rec is not None:
        return rec
    if sum(1 for r in book.values() if r.get("result") is None) >= cfg.watch_max_live:
        return None
    rec = {
        "ca": ca, "at": now, "ts": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime(now)),
        "setup": setup, "chain": chain, "sol_usd": round(sol_usd, 2),
        "features": {k: snap.get(k) for k in FEATURES if snap.get(k) is not None},
        "price": price, "stage": "candidate",
        "checklist": None, "brain": None, "would_buy": None,
        "max_x": 1.0, "min_x": 1.0, "max_at_min": 0.0, "last_x": 1.0,
        "x_at": {}, "up_at": {}, "down_at": {}, "samples": 0, "checked_at": now, "result": None,
    }
    book[_key(ca, now)] = rec
    return rec


def annotate(book: dict, ca: str, cfg: Config, now: float | None = None, **fields) -> None:
    """Add what research found (checklist, brain, would-buy) to the coin's current observation."""
    rec = current(book, ca, now or time.time(), cfg)
    if rec is None:
        return
    for k, v in fields.items():
        if v is not None:
            rec[k] = v
    rec["stage"] = ("would_buy" if rec.get("would_buy") else "brain" if rec.get("brain") is not None
                    else "checklist" if rec.get("checklist") is not None else "candidate")


def _mark(rec: dict, x: float, minutes: float) -> None:
    if x > rec["max_x"]:
        rec["max_x"], rec["max_at_min"] = round(x, 4), round(minutes, 1)
    rec["min_x"] = round(min(rec["min_x"], x), 4)
    rec["last_x"] = round(x, 4)
    for up in UP_X:
        if x >= up and str(up) not in rec["up_at"]:
            rec["up_at"][str(up)] = round(minutes, 1)
    for down in DOWN_X:
        if x <= down and str(down) not in rec["down_at"]:
            rec["down_at"][str(down)] = round(minutes, 1)
    for cp in CHECKPOINTS_MIN:
        # The first sample at or after each checkpoint stands in for it.
        if minutes >= cp and str(cp) not in rec["x_at"]:
            rec["x_at"][str(cp)] = round(x, 4)


def sample(cfg: Config, book: dict, now: float | None = None, prices: dict[str, float] | None = None) -> int:
    """Price every live observation and settle the ones whose follow window is over.
    Settled observations are appended to the day file. Returns how many settled."""
    now = now or time.time()
    live = [r for r in book.values() if r.get("result") is None]
    if not live:
        return 0
    if prices is None:
        prices = {}
        for chain in {r.get("chain", "solana") for r in live}:
            cas = sorted({r["ca"] for r in live if r.get("chain", "solana") == chain})
            pairs = data.get_pairs(cas, chain)
            prices.update({ca: float(p.get("priceUsd") or 0) for ca, p in pairs.items()})
    window = cfg.watch_follow_hours * 3600
    settled = []
    for rec in live:
        minutes = (now - rec["at"]) / 60
        price = prices.get(rec["ca"]) or 0
        if price > 0:
            _mark(rec, price / rec["price"], minutes)
            rec["samples"] += 1
            rec["checked_at"] = now
        elif now - rec.get("checked_at", rec["at"]) > 3600:
            rec["result"] = "no_price"  # delisted or rugged out of DexScreener for an hour
        if rec["result"] is None and now - rec["at"] >= window:
            rec["result"] = "done"
        if rec["result"]:
            rec["settled_at"] = now
            settled.append(rec)
    if settled:
        out = obs_dir(cfg)
        out.mkdir(parents=True, exist_ok=True)
        for rec in settled:
            day = time.strftime("%Y-%m-%d", time.gmtime(rec["at"]))
            with (out / f"{day}.jsonl").open("a") as f:
                f.write(json.dumps(rec, default=str) + "\n")
            book.pop(_key(rec["ca"], rec["at"]), None)
    return len(settled)


def prune_files(cfg: Config, now: float | None = None) -> None:
    """Drop day files older than watch_keep_days."""
    out = obs_dir(cfg)
    if not out.exists():
        return
    cutoff = time.strftime("%Y-%m-%d", time.gmtime((now or time.time()) - cfg.watch_keep_days * 86400))
    for path in out.glob("*.jsonl"):
        if path.stem < cutoff:
            path.unlink()


def summary(cfg: Config, book: dict) -> dict:
    """Counts for the Duet report."""
    files = sorted(obs_dir(cfg).glob("*.jsonl")) if obs_dir(cfg).exists() else []
    settled = would = brain = 0
    migs: dict[str, int] = {}
    for path in files:
        for line in path.read_text().splitlines():
            try:
                rec = json.loads(line)
            except ValueError:
                continue
            settled += 1
            would += bool(rec.get("would_buy"))
            brain += rec.get("brain") is not None
            if rec.get("migration"):
                pad = rec["migration"].get("launchpad") or "pump.fun"
                migs[pad] = migs.get(pad, 0) + 1
    live = [r for r in book.values() if r.get("result") is None]
    for r in live:
        if r.get("migration"):
            pad = r["migration"].get("launchpad") or "pump.fun"
            migs[pad] = migs.get(pad, 0) + 1
    return {"on": cfg.watch_only, "live": len(live), "settled": settled, "brain_reads": brain,
            "at_migration": sum(migs.values()), "at_migration_by_launchpad": migs,
            "would_buys": would + sum(1 for r in live if r.get("would_buy")),
            "days": [p.stem for p in files], "follow_hours": cfg.watch_follow_hours,
            "sample_min": cfg.watch_sample_min}


# ---------------------------------------------------------------- daily digest
def simple_plan_x(rec: dict, take: float = 1.5, stop: float = 0.8) -> float:
    """Price multiple a plain take-profit/stop would have sold at. When both lines were
    crossed between the same two samples, count the stop (the cautious read)."""
    up, down = rec["up_at"].get(str(take)), rec["down_at"].get(str(stop))
    if up is not None and (down is None or up < down):
        return take
    if down is not None:
        return stop
    return rec.get("last_x") or 1.0


def cost_pct(cfg: Config, rec: dict, size_usd: float = 10.0) -> float | None:
    """Round-trip paper cost of a $10 entry, from the Solana cost model. None off Solana:
    gas, venue fees and slippage there aren't modeled yet."""
    from .portfolio import venue_fee_pct
    from .sizing import round_trip_cost_pct

    if rec.get("chain", "solana") != "solana":
        return None

    f = rec.get("features") or {}
    sol = rec.get("sol_usd") or 0.0
    venue = venue_fee_pct(cfg, f.get("dex"), f.get("mcap_usd") or 0.0, sol) if sol else cfg.other_dex_fee_pct
    return round_trip_cost_pct(size_usd, cfg, sol or 150.0, venue, f.get("liquidity_usd") or 0.0)


def read_settled(cfg: Config, since: float = 0.0) -> list[dict]:
    out = []
    if not obs_dir(cfg).exists():
        return out
    for path in sorted(obs_dir(cfg).glob("*.jsonl")):
        for line in path.read_text().splitlines():
            try:
                rec = json.loads(line)
            except ValueError:
                continue
            if rec.get("at", 0) >= since:
                out.append(rec)
    return out


def _group(cfg: Config, recs: list[dict]) -> dict:
    if not recs:
        return {"n": 0}
    xs = sorted(simple_plan_x(r) for r in recs)
    costs = [(r, cost_pct(cfg, r)) for r in recs]
    costed = [(r, c) for r, c in costs if c is not None]
    nets = [100 * (simple_plan_x(r) - 1) - c for r, c in costed]
    peaks = sorted(r.get("max_x", 1.0) for r in recs)
    return {
        "n": len(recs),
        "ran_pct": round(100 * sum(1 for x in xs if x >= 1.5) / len(recs), 1),
        "dumped_pct": round(100 * sum(1 for x in xs if x <= 0.8) / len(recs), 1),
        "median_peak_x": round(peaks[len(peaks) // 2], 2),
        "hit_2x_pct": round(100 * sum(1 for r in recs if "2.0" in r["up_at"]) / len(recs), 1),
        "avg_gross_pct": round(sum(100 * (simple_plan_x(r) - 1) for r in recs) / len(recs), 1),
        # After costs only where costs are modeled (Solana); off-Solana coins count in gross.
        "avg_net_pct": round(sum(nets) / len(nets), 1) if nets else None,
        "avg_cost_pct": round(sum(c for _, c in costed) / len(costed), 1) if costed else None,
        "costed": len(costed),
    }


def digest(cfg: Config, book: dict, hours: float = 24.0, now: float | None = None) -> dict:
    """What the last day of observations shows, as numbers for the daily review."""
    now = now or time.time()
    recs = read_settled(cfg, now - hours * 3600)
    by_setup: dict[str, list] = {}
    by_launchpad: dict[str, list] = {}
    for r in recs:
        by_setup.setdefault(r.get("setup") or "?", []).append(r)
        if r.get("migration"):
            by_launchpad.setdefault(r["migration"].get("launchpad") or "pump.fun", []).append(r)
    stage = {
        "checklist_failed": [r for r in recs if (r.get("checklist") or {}).get("passed") is False],
        "brain_passed": [r for r in recs if (r.get("brain") or {}).get("action") == "PASS"],
        "would_buy": [r for r in recs if r.get("would_buy")],
        "not_researched": [r for r in recs if r.get("checklist") is None],
    }
    # Logged right at graduation (owner, Nov 3): split by how concentrated the holders were.
    at_mig = [r for r in recs if (r.get("migration") or {}).get("minutes_since") is not None
              and r["migration"]["minutes_since"] <= 10]
    by_top10: dict[str, list] = {}
    for r in at_mig:
        top10 = ((r["migration"].get("holders") or {}).get("top10_pct_ex_pool"))
        band = ("unknown" if top10 is None else "top10 under 20%" if top10 < 20
                else "top10 20-35%" if top10 <= 35 else "top10 over 35%")
        by_top10.setdefault(band, []).append(r)
    runners = sorted(recs, key=lambda r: r.get("max_x", 1.0), reverse=True)[:5]
    return {
        "hours": hours, "settled": len(recs),
        "still_followed": sum(1 for r in book.values() if r.get("result") is None),
        "all": _group(cfg, recs),
        "by_setup": {k: _group(cfg, v) for k, v in by_setup.items()},
        "by_stage": {k: _group(cfg, v) for k, v in stage.items()},
        "at_migration": _group(cfg, at_mig),
        "at_migration_by_holders": {k: _group(cfg, v) for k, v in by_top10.items()},
        "at_migration_by_launchpad": {k: _group(cfg, v) for k, v in by_launchpad.items()},
        "top_runners": [{"symbol": (r.get("features") or {}).get("symbol"), "ca": r["ca"], "chain": r.get("chain", "solana"),
                         "setup": r.get("setup"),
                         "max_x": r.get("max_x"), "minutes_to_high": r.get("max_at_min"),
                         "mcap": (r.get("features") or {}).get("mcap_usd"),
                         "age_hours": (r.get("features") or {}).get("age_hours"),
                         "stage": r.get("stage"), "brain": (r.get("brain") or {}).get("action")} for r in runners],
    }
