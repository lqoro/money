"""Append-only logs plus the agent's lessons and learned rules (its memory)."""

from __future__ import annotations

import json
import re
import time
from pathlib import Path

from .config import Config


def _append_jsonl(path: Path, record: dict) -> None:
    record = {"ts": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()), **record}
    with path.open("a") as f:
        f.write(json.dumps(record, default=str) + "\n")


def log_decision(cfg: Config, record: dict) -> None:
    _append_jsonl(cfg.memory_dir / "decisions.jsonl", record)


def log_trade(cfg: Config, record: dict) -> None:
    _append_jsonl(cfg.memory_dir / "trades.jsonl", record)


def read_trades(cfg: Config) -> list[dict]:
    path = cfg.memory_dir / "trades.jsonl"
    if not path.exists():
        return []
    return [json.loads(line) for line in path.read_text().splitlines() if line.strip()]


def add_lesson(cfg: Config, lesson: str) -> None:
    path = cfg.memory_dir / "lessons.md"
    if not path.exists():
        path.write_text("# Trencher's lessons (one per closed trade)\n\n")
    with path.open("a") as f:
        f.write(f"- [{time.strftime('%Y-%m-%d %H:%M', time.gmtime())}] {lesson.strip()}\n")


def recent_lessons(cfg: Config, n: int) -> list[str]:
    path = cfg.memory_dir / "lessons.md"
    if not path.exists():
        return []
    return [line for line in path.read_text().splitlines() if line.startswith("- ")][-n:]


def learned_rules(cfg: Config) -> str:
    path = cfg.memory_dir / "learned_rules.md"
    return path.read_text() if path.exists() else ""


def save_learned_rules(cfg: Config, text: str) -> None:
    (cfg.memory_dir / "learned_rules.md").write_text(text.strip() + "\n")


# Fee caps and minimum sizes Trencher wrote into its own memory before the code fee
# check (sizing.fee_check) existed: "skip if friction tops 5%", "no position under $5".
# A round trip can't cost less than the fee floor, so such a cap blocks every trade.
# The lines stay in its files (they're its history) but are marked retired wherever
# they reach a prompt, so a stale cap can't quietly block trading again.
_FEE_RULE = re.compile(r"friction|round.?trip cost|fees? (?:are |is )?(?:over|above|top)|"
                       r"minimum position|position (?:size )?minimum|under (?:about |~)?\$\d|\$\d+ minimum", re.I)
RETIRED_FEE_NOTE = " [Retired fee/size part: the code fee check owns this now, so don't apply it yourself.]"


def mark_retired_fee_rules(text: str) -> str:
    return "\n".join(line + RETIRED_FEE_NOTE if line.strip() and _FEE_RULE.search(line) else line
                     for line in text.splitlines())


def prompt_lessons(cfg: Config, n: int) -> list[str]:
    """Recent lessons as the brain should read them."""
    return [mark_retired_fee_rules(line) for line in recent_lessons(cfg, n)]


def prompt_rules(cfg: Config) -> str:
    """Learned rules as the brain should read them."""
    return mark_retired_fee_rules(learned_rules(cfg))
