"""Strategy evolution: Claude studies its closed trades, rewrites its learned rules
and retunes its own strategy parameters (within hard bounds). Changes persist in
memory/strategy.json and are logged to memory/strategy_log.md."""

from __future__ import annotations

import json
import logging
import time

from . import journal
from .brain import Brain
from .config import EVOLVABLE, Config

log = logging.getLogger(__name__)


def evolve(cfg: Config, brain: Brain) -> str | None:
    """Run one evolution step. Returns a human-readable summary, or None if nothing ran."""
    closes = [t for t in journal.read_trades(cfg) if t.get("event") == "CLOSE"]
    if not closes:
        return None
    out = brain.evolve(closes)
    if not out:
        return None

    if out.get("rules_markdown"):
        journal.save_learned_rules(cfg, out["rules_markdown"])

    path = cfg.memory_dir / "strategy.json"
    current = json.loads(path.read_text()) if path.exists() else {}
    changed = []
    for ch in out.get("param_changes") or []:
        name = ch.get("param")
        if name not in EVOLVABLE:
            continue
        lo, hi = EVOLVABLE[name]
        value = min(hi, max(lo, float(ch["value"])))
        old = getattr(cfg, name)
        if abs(value - old) < 1e-9:
            continue
        current[name] = value
        changed.append(f"- `{name}`: {old:g} → {value:g} — {ch.get('reason', '')}")
    if changed:
        path.write_text(json.dumps(current, indent=2))
        applied = cfg.apply_strategy()
        log.info("Strategy evolved: %s", applied)
        with (cfg.memory_dir / "strategy_log.md").open("a") as f:
            f.write(f"\n## {time.strftime('%Y-%m-%d %H:%M UTC', time.gmtime())} — after {len(closes)} trades\n")
            f.write("\n".join(changed) + "\n")

    summary = f"📚 Trencher studied {len(closes)} trades.\n"
    summary += ("Strategy changes:\n" + "\n".join(changed) + "\n") if changed else "No parameter changes.\n"
    summary += "Learned rules:\n" + (out.get("rules_markdown") or "(unchanged)")
    return summary
