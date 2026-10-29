"""Strategy evolution: Claude studies its closed trades, rewrites its learned rules
and retunes its own strategy parameters (within hard bounds). Changes persist in
memory/strategy.json and are logged to memory/strategy_log.md."""

from __future__ import annotations

import json
import logging
import time

from . import journal, skips
from .brain import Brain
from .config import EVOLVABLE, Config

log = logging.getLogger(__name__)


def evolve(cfg: Config, brain: Brain) -> str | None:
    """Run one evolution step. Returns a human-readable summary, or None if nothing ran."""
    closes = [t for t in journal.read_trades(cfg) if t.get("event") == "CLOSE"]
    skip_review = skips.prompt_text(skips.load(cfg), top=20)
    if not closes and not skips.stats(skips.load(cfg)):
        return None
    out = brain.evolve(closes, skip_review)
    if not out:
        return None
    rule_changes = [r for r in out.get("rule_changes") or [] if r.get("change") != "kept"]
    if rule_changes:
        with (cfg.memory_dir / "rule_changes.jsonl").open("a") as f:
            for r in rule_changes:
                f.write(json.dumps({"t": round(time.time()), **r}) + "\n")

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
    rule_lines = [f"- {r['change']}: {r['rule']} ({r['evidence']})" for r in rule_changes]
    if changed or rule_lines:
        with (cfg.memory_dir / "strategy_log.md").open("a") as f:
            f.write(f"\n## {time.strftime('%Y-%m-%d %H:%M UTC', time.gmtime())} — after {len(closes)} trades "
                    f"and the skip review\n")
            f.write("\n".join(changed + rule_lines) + "\n")

    summary = f"📚 Trencher studied {len(closes)} trades and what its skips did.\n"
    summary += ("Strategy changes:\n" + "\n".join(changed) + "\n") if changed else "No parameter changes.\n"
    if rule_lines:
        summary += "Rule changes:\n" + "\n".join(rule_lines) + "\n"
    summary += "Learned rules:\n" + (out.get("rules_markdown") or "(unchanged)")
    return summary
