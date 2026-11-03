"""Narrative and catalyst gate for bottom buys (owner rule, Nov 2).

The owner's rule: when Trencher buys a coin on its way back up from a pullback, the
narrative has to be alive and strong, and something should be coming that makes more
people buy it. Its record backed this: 11 dip and pullback buys on themes its own meta
read called fading, holding or didn't name went 0 for 11 (-$15.67), while the three
buys on a theme with real outside news behind it (tokenized stocks) all ran past 1.6x.

A bottom buy is a DIP, or a MIGRATED buy at least `pullback_min_drawdown_pct` off its
high. It goes through only if all three hold:

1. The brain rates the narrative rising and at least `narrative_min_strength` of 10.
2. The brain names a specific catalyst it found: fresh news, a listing, an event on a
   date, a big account posting about it. "Momentum" or "buyers stepping in" isn't one.
3. Code measures the theme, not only the coin: every coin scanned in the last 30 min
   (plus same-ticker pairs) that shares a theme word with this one, summed. The theme's
   5m volume has to keep at least `theme_min_pace` x its own hourly average 5m. A theme
   whose copies are all bleeding volume is fading, even when one coin still looks fine.

These settings are the owner's (steer.json), not evolvable: Trencher can't loosen them.
`narrative_min_strength` 0 turns the whole gate off; `theme_min_pace` 0 turns off check 3.
"""

from __future__ import annotations

import re

# Words that say nothing about which story a coin rides.
STOPWORDS = {
    "coin", "coins", "token", "the", "and", "for", "official", "real", "original", "solana", "sol",
    "pump", "pumpfun", "meme", "memes", "community", "dao", "fun", "new", "first", "only", "just",
}
NO_CATALYST = re.compile(r"^\s*(none|n/?a|no(ne)?\s+(found|named|known|catalyst)|nothing|unknown|-)?\s*\.?\s*$", re.I)
VAGUE_CATALYST = re.compile(
    r"^\s*(momentum|volume|buyers?( stepping in| returning)?|higher low|bounce|the (chart|dip)|"
    r"attention|hype|community|narrative|meta)\s*\.?\s*$", re.I)


def theme_words(snap: dict) -> set[str]:
    text = f"{snap.get('name') or ''} {snap.get('symbol') or ''}".lower()
    return {w for w in re.split(r"[^a-z0-9]+", text) if len(w) >= 3 and w not in STOPWORDS}


def theme_flow(snap: dict, others: list[dict]) -> dict:
    """This coin's theme, measured across its copies: summed 5m and 1h volume, and the
    theme's pace (5m volume vs the hour's average 5m). `others` are snapshots of other
    coins (recent scans, same-ticker pairs); duplicates by address are counted once."""
    words = theme_words(snap)
    sym = (snap.get("symbol") or "").lower()
    seen, copies = set(), []
    for s in [snap, *others]:
        addr = s.get("address") or s.get("pair_address")
        if not addr or addr in seen:
            continue
        same_ticker = sym and (s.get("symbol") or "").lower() == sym
        if s is snap or same_ticker or (words and words & theme_words(s)):
            seen.add(addr)
            copies.append(s)
    vol_5m = sum(float(c.get("vol_5m") or 0) for c in copies)
    vol_1h = sum(float(c.get("vol_1h") or 0) for c in copies)
    pace = round(vol_5m / (vol_1h / 12), 2) if vol_1h else None
    leader = max(copies, key=lambda c: float(c.get("vol_5m") or 0))
    return {
        "words": sorted(words) or [sym],
        "copies": len(copies),
        "vol_5m": round(vol_5m),
        "vol_1h": round(vol_1h),
        "pace": pace,
        "leader": leader.get("symbol"),
        "this_is_leader": leader is snap,
    }


def is_bottom_buy(setup: str | None, snap: dict, cfg) -> bool:
    if setup == "DIP":
        return True
    return setup == "MIGRATED" and (snap.get("drawdown_pct") or 0) >= cfg.pullback_min_drawdown_pct


def gate(decision: dict, setup: str | None, snap: dict, cfg) -> str | None:
    """None if this buy may go ahead; otherwise the reason it's blocked."""
    if cfg.narrative_min_strength <= 0 or decision.get("action") != "BUY" or not is_bottom_buy(setup, snap, cfg):
        return None
    what = "dip" if setup == "DIP" else f"pullback ({snap.get('drawdown_pct') or 0:.0f}% off the high)"
    trend = str(decision.get("narrative_trend") or "").lower()
    strength = int(decision.get("narrative_strength") or 0)
    if trend != "rising" or strength < cfg.narrative_min_strength:
        return (f"narrative gate (owner rule): a {what} needs a rising, strong narrative; "
                f"read it as {trend or 'unrated'} at {strength}/10 (needs rising and {cfg.narrative_min_strength:g}+)")
    catalyst = str(decision.get("catalyst") or "").strip()
    if NO_CATALYST.match(catalyst) or VAGUE_CATALYST.match(catalyst) or len(catalyst) < 12:
        return f"narrative gate (owner rule): a {what} needs a named catalyst, and none was found ({catalyst or 'none'})"
    theme = snap.get("theme") or {}
    pace = theme.get("pace")
    if cfg.theme_min_pace > 0 and pace is not None and pace < cfg.theme_min_pace:
        return (f"narrative gate (owner rule): the {'/'.join(theme.get('words') or [])} theme is cooling: "
                f"{theme.get('copies')} coin(s), 5m volume at {pace:.2f}x the theme's hourly pace "
                f"(needs {cfg.theme_min_pace:g}x)")
    return None
