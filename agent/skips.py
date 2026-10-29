"""Skip review: what the coins Trencher passed on did next.

Lessons only come from trades it took, so on their own its rules can only tighten:
every loss adds a ban, and a coin it skipped that went 5x never teaches it anything.
This closes that loop. Every PASS/REJECT is filed under the reason it gave (the gate),
then followed with DexScreener prices for skip_review_hours:

    ran     reached the first profit target (take_initials_multiple) from the skip
            price before falling stop_loss_pct: the skip cost a winner
    dumped  fell stop_loss_pct first: the skip saved a loss
    flat    neither within the window

Prices are sampled every skip_review_interval_min, so a spike between samples can be
missed: the tally is evidence, not a backtest. Evolution reads it per gate and loosens
rules whose skips keep running, and keeps the ones whose skips keep dumping.
"""

from __future__ import annotations

import json
import logging
import re
import time

from . import data
from .config import Config

log = logging.getLogger(__name__)

# First match names the gate. Code hard lines first, then the brain's own reasons.
GATES = (
    ("bundles over the line", r"linked wallet cluster|bundles:"),
    ("dev share over 1%", r"dev holds"),
    ("top 10 over 25%", r"top 10 hold .*>25%|top 10 .*hard line"),
    ("insiders over 10%", r"insiders hold"),
    ("RugCheck danger", r"rugcheck danger|rugged|mint authority|freeze authority|transfer tax|lp only"),
    ("RugCheck didn't load", r"rugcheck report unavailable|didn't load"),
    ("falling knife (code)", r"dip with fading attention"),
    ("fees or size", r"fee|too small|minimum|no probe fits"),
    ("brain paced", r"paced or paused|brain unavailable"),
    ("political figure", r"politic"),
    ("too new / sniping", r"snip|seconds old|minutes? old|\bmin old\b|new pair|brand.new|too (new|young|fresh)"),
    ("near the high / chasing", r"chas|near (its|the) (high|top)|off (a|the|its) (\d+-minute-old )?(high|peak|top)"
                                r"|under (its|the) high|at (its|the) (all-time )?high|local high|catculus|entry location"),
    ("falling knife / no higher low", r"falling knife|higher low|knife"),
    ("crowd leaving / fading volume", r"fading|leaving|left|collaps|hourly pace|hour's pace|0\.\d+x"),
    ("thin 5m volume", r"5m (volume )?(is |of )?\$?\d|dead|thin|under (my )?\$10k|below \$10k|weak flow"),
    ("sellers in control", r"seller"),
    ("vamp / copycat", r"vamp|copycat|same.ticker|share (the|this) ticker|original|twin|duplicate"),
    ("LARP / no product", r"larp|no github|no product|dead website|site"),
    ("holders or bundles unverified", r"bundl|unverified|insider|holder"),
)


def gate_for(reason: str) -> str:
    text = (reason or "").lower()
    for name, pattern in GATES:
        if re.search(pattern, text):
            return name
    return "other"


def _path(cfg: Config):
    return cfg.memory_dir / "skips.json"


def load(cfg: Config) -> dict:
    try:
        return json.loads(_path(cfg).read_text()) if _path(cfg).exists() else {}
    except ValueError:
        return {}


def save(cfg: Config, skips: dict) -> None:
    cutoff = time.time() - 72 * 3600
    _path(cfg).write_text(json.dumps({k: v for k, v in skips.items() if v.get("at", 0) > cutoff}))


def record(cfg: Config, skips: dict, snap: dict, outcome: str, reason: str) -> None:
    """File a skip. A coin skipped again while it's still being followed keeps its first
    price (that's the trade it didn't take) and adds the new gate, once."""
    ca, price = snap.get("address"), float(snap.get("price_usd") or 0)
    if not ca or price <= 0:
        return
    gate = gate_for(reason)
    rec = skips.get(ca)
    if rec and rec.get("result") is None:
        if gate not in rec["gates"]:
            rec["gates"].append(gate)
        return
    skips[ca] = {
        "symbol": snap.get("symbol"), "at": time.time(), "outcome": outcome, "gates": [gate],
        "reason": str(reason)[:200], "price": price, "mcap": round(snap.get("mcap_usd") or 0),
        "up_x": cfg.take_initials_multiple, "down_pct": cfg.stop_loss_pct,
        "max_x": 1.0, "min_x": 1.0, "result": None, "checked_at": 0.0,
    }


def update(cfg: Config, skips: dict, now: float | None = None) -> int:
    """Price every skip still being followed and settle the ones that played out.
    Returns how many settled."""
    now = now or time.time()
    window = cfg.skip_review_hours * 3600
    live = {ca: r for ca, r in skips.items() if r.get("result") is None}
    if not live:
        return 0
    pairs = data.get_pairs(list(live))
    settled = 0
    for ca, rec in live.items():
        pair = pairs.get(ca)
        if pair is not None:
            price = float(pair.get("priceUsd") or 0)
            if price > 0:
                x = price / rec["price"]
                rec["max_x"], rec["min_x"] = max(rec["max_x"], x), min(rec["min_x"], x)
                rec["last_x"], rec["checked_at"] = round(x, 3), now
                # Whichever threshold a sample crosses first decides it.
                if x >= rec["up_x"]:
                    rec["result"] = "ran"
                elif x <= 1 - rec["down_pct"] / 100:
                    rec["result"] = "dumped"
        if rec["result"] is None and now - rec["at"] >= window:
            rec["result"] = "flat"
        if rec["result"]:
            rec["settled_at"] = now
            settled += 1
    return settled


def stats(skips: dict, hours: float = 48, now: float | None = None) -> dict:
    """Per gate: how many coins it blocked, and what they did."""
    now = now or time.time()
    out: dict[str, dict] = {}
    for ca, rec in skips.items():
        if now - rec.get("at", 0) > hours * 3600:
            continue
        for gate in rec.get("gates") or ["other"]:
            g = out.setdefault(gate, {"blocked": 0, "ran": 0, "dumped": 0, "flat": 0, "pending": 0,
                                      "ran_examples": [], "dumped_examples": []})
            g["blocked"] += 1
            res = rec.get("result") or "pending"
            g[res] += 1
            if res in ("ran", "dumped") and len(g[f"{res}_examples"]) < 3:
                g[f"{res}_examples"].append({"symbol": rec.get("symbol"), "ca": ca,
                                             "best_x": round(rec.get("max_x", 1), 2),
                                             "worst_x": round(rec.get("min_x", 1), 2)})
    return dict(sorted(out.items(), key=lambda kv: -kv[1]["blocked"]))


def resolved_since(skips: dict, since: float) -> int:
    return sum(1 for r in skips.values() if r.get("result") and r.get("settled_at", 0) >= since)


def verdict(g: dict) -> str:
    """Plain-words read of one gate's tally."""
    done = g["ran"] + g["dumped"]
    if done < 3:
        return "too few played out to judge"
    if g["ran"] > g["dumped"]:
        return "cost more winners than it saved: loosen it"
    if g["dumped"] >= 2 * max(1, g["ran"]):
        return "saving losses: keep it"
    return "mixed"


def prompt_text(skips: dict, hours: float = 48, top: int = 8) -> str:
    """Compact tally for the brain's prompts."""
    st = stats(skips, hours)
    if not st:
        return "(no skips followed yet)"
    lines = []
    for gate, g in list(st.items())[:top]:
        ran = ", ".join(e["symbol"] or "?" for e in g["ran_examples"])
        lines.append(f"- {gate}: blocked {g['blocked']}, ran {g['ran']}, dumped {g['dumped']}, flat {g['flat']}, "
                     f"still open {g['pending']} ({verdict(g)})" + (f"; ran: {ran}" if ran else ""))
    return "\n".join(lines)
