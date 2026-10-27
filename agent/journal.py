"""Append-only logs plus the agent's lessons and learned rules (its memory)."""

from __future__ import annotations

import json
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
