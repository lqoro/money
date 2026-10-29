"""Claude Duet bridge: how Trencher talks to Lenny's Claude Duet channel while it
runs nonstop on his own machine.

Trencher and Duet share one git branch (DUET_SYNC_BRANCH, default trencher-live)
in this repo, checked out at DUET_SYNC_DIR:

    status.json  written by Trencher: wallet, positions, trades, lessons, brain usage
    REPORT.md    the same, readable on GitHub or a phone
    steer.json   written by Duet:  {"pause_new_trades": bool,
                                    "settings": {"stop_loss_pct": 25, "bribe_sol": 0.002, ...},
                                    "owner_note": "short guidance for the brain",
                                    "goal": {"equity_usd": 1000, "deadline": "2026-11-05T05:00:00Z"}}

Every DUET_SYNC_INTERVAL_MIN minutes Trencher pulls the branch, applies steer.json,
writes its status and pushes. Steering is data, never code: only a pause flag,
settings Trencher could evolve anyway, the paper fee and slippage settings
(STEERABLE, which Trencher can't change itself), all clamped to their bounds, and
a note.

With AUTO_UPDATE=true it also checks origin/main and, when a merged change is
waiting, stops cleanly so the launcher restarts it on the new code.
"""

from __future__ import annotations

import json
import logging
import os
import subprocess
import time
from pathlib import Path

from . import journal, radar
from .config import EVOLVABLE, ROOT, STEERABLE, Config

log = logging.getLogger(__name__)

STEER_FILE = "steer.json"
MAX_NOTE_CHARS = 600


def git(repo: Path, *args: str, timeout: float = 60) -> subprocess.CompletedProcess:
    return subprocess.run(["git", "-C", str(repo), *args], capture_output=True, text=True, timeout=timeout)


def apply_steering(cfg: Config, steer: dict) -> dict:
    """Apply a steer.json payload to cfg. Returns what was applied. Unknown keys and
    settings outside EVOLVABLE and STEERABLE are ignored; values are clamped to their bounds."""
    applied: dict = {}
    pause = bool(steer.get("pause_new_trades", False))
    if pause != cfg.pause_new_trades:
        log.info("Duet steering: new trades %s", "paused" if pause else "resumed")
    cfg.pause_new_trades = applied["pause_new_trades"] = pause

    settings = steer.get("settings") or {}
    if isinstance(settings, dict):
        for name, value in settings.items():
            bounds = EVOLVABLE.get(name) or STEERABLE.get(name)
            if not bounds:
                log.warning("Duet steering: ignoring %r (not a steerable setting)", name)
                continue
            try:
                lo, hi = bounds
                value = min(hi, max(lo, float(value)))
            except (TypeError, ValueError):
                continue
            if getattr(cfg, name) != value:
                log.info("Duet steering: %s %g → %g", name, getattr(cfg, name), value)
            cfg.steer_pinned.setdefault(name, getattr(cfg, name))
            setattr(cfg, name, value)
            applied[name] = value
    # Settings dropped from steer.json go back to what they were (then to anything
    # Trencher has evolved for itself since).
    for name in [n for n in cfg.steer_pinned if n not in applied]:
        setattr(cfg, name, cfg.steer_pinned.pop(name))
        log.info("Duet steering: %s back to %g", name, getattr(cfg, name))
    cfg.apply_strategy()

    goal = steer.get("goal")
    cfg.goal_equity_usd, cfg.goal_deadline = 0.0, ""
    if isinstance(goal, dict):
        try:
            target = float(goal.get("equity_usd") or 0)
            deadline = str(goal.get("deadline") or "")
            time.strptime(deadline, "%Y-%m-%dT%H:%M:%SZ")
        except (TypeError, ValueError):
            log.warning("Duet steering: ignoring goal %r (needs equity_usd and a deadline like 2026-11-05T05:00:00Z)", goal)
        else:
            if target > 0:
                cfg.goal_equity_usd, cfg.goal_deadline = target, deadline
                applied["goal"] = {"equity_usd": target, "deadline": deadline}

    note = steer.get("owner_note")
    cfg.owner_note = str(note).strip()[:MAX_NOTE_CHARS] if note else ""
    if cfg.owner_note:
        applied["owner_note"] = cfg.owner_note
    return applied


def build_report(agent) -> tuple[dict, str]:
    cfg = agent.cfg
    view = agent.portfolio_view()
    trades = journal.read_trades(cfg)
    closes = [t for t in trades if t.get("event") == "CLOSE"]
    status = {
        "updated_at": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()),
        "paused_new_trades": cfg.pause_new_trades,
        "brain": {"mode": agent.brain.backend or "rules", "paused_until": agent.brain.paused_until or None,
                  "usage_48h": agent.brain.usage_view()},
        **view,
        "strategy": cfg.strategy_view(),
        "paper_costs": {name: getattr(cfg, name) for name in STEERABLE},
        "recent_trades": [{"ca": t.get("token"), **t} for t in trades[-20:]],
        "recent_lessons": journal.recent_lessons(cfg, 10),
        "learned_rules": journal.learned_rules(cfg),
        "meta": radar.public_view(agent.meta, headlines=5),
        "goal": cfg.goal_progress(view.get("equity_usd", agent.pf.equity())),
        "last_scan": getattr(agent, "last_scan", {}),
        "recent_looks": list(getattr(agent, "recent_looks", []))[-15:],
    }

    eq = view.get("equity_usd", agent.pf.equity())
    wins = sum(1 for t in closes if t.get("pnl_usd", 0) > 0)
    lines = [
        "# Trencher live report",
        "",
        f"Updated {status['updated_at']} (paper trading, never real money)",
        "",
        f"- Equity: ${eq:,.2f} ({100 * (eq / cfg.starting_cash_usd - 1):+.1f}% vs ${cfg.starting_cash_usd:.0f} start)",
        *([f"- Goal: ${g['target_usd']:,.0f} by {g['deadline'][:16].replace('T', ' ')}Z (a stretch, survival first): "
           f"at {g['progress_pct']:g}% of it, {g['days_left']:g} days left"
           + (f", needs {g['needed_daily_growth_pct']:+g}% a day from here" if g["needed_daily_growth_pct"] is not None else "")]
          if (g := status["goal"]) else []),
        f"- Closed trades: {len(closes)}" + (f", {wins} wins" if closes else ""),
        f"- Fees paid: ${view.get('fees_paid_usd', 0):.2f}"
        + (" (" + ", ".join(f"{k} ${v:.2f}" for k, v in (view.get("fees_by_kind_usd") or {}).items()) + ")"
           if view.get("fees_by_kind_usd") else "")
        + f", plus ${view.get('slippage_paid_usd', 0):.2f} lost to slippage",
        f"- New trades: {'PAUSED by Duet' if cfg.pause_new_trades else 'on'}",
        f"- Brain: {status['brain']['mode']}, {status['brain']['usage_48h']['brain_calls']} calls and "
        f"{status['brain']['usage_48h']['plan_limit_hits']} plan-limit hits in 48h",
        "",
        "## Open positions",
    ]
    positions = view.get("open_positions") or []
    lines += [f"- {p.get('symbol')} ({p.get('setup')}): cost ${p.get('cost_usd')}, {p.get('multiple', '?')}x, "
              f"fees ${p.get('fees_usd', 0):.2f}  \n  CA `{p.get('ca')}`"
              for p in positions] or ["- none"]
    lines += ["", "## Recent trades"]
    lines += [f"- {t.get('ts', '')[11:16]}Z {t.get('event')} {t.get('symbol')}"
              + (f" ${t.get('size_usd', 0):.2f}" if t.get("event") == "BUY" else "")
              + (f" for ${t.get('proceeds_usd', 0):.2f}" if t.get("event") == "SELL" else "")
              + (f" {t.get('pnl_pct', 0):+.0f}% (${t.get('pnl_usd', 0):+.2f})" if t.get("event") == "CLOSE" else "")
              + (f", fees ${t['fees_usd']:.2f}" if t.get("fees_usd") is not None else "")
              + f"  \n  CA `{t.get('ca') or t.get('token')}`" for t in trades[-10:]] or ["- none yet"]
    lines += ["", "## Last closes"]
    lines += [f"- {t.get('symbol')}: {t.get('pnl_pct', 0):+.0f}% (${t.get('pnl_usd', 0):+.2f}), "
              f"{(t.get('exit_reasons') or ['?'])[-1]}  \n  CA `{t.get('ca') or t.get('token')}`"
              for t in closes[-10:]] or ["- none yet"]
    lines += ["", "## Last scan"]
    scan = status["last_scan"]
    if scan.get("blocked"):
        lines.append(f"- Not opening trades: {scan['blocked']}")
    elif scan:
        lines.append(f"- {time.strftime('%H:%MZ', time.gmtime(scan['at']))}: {scan['tokens']} coins, "
                     f"{scan['pairs']} with pairs, {scan['passed_market_filters']} passed the market filters, "
                     f"{scan['researched']} researched")
    else:
        lines.append("- no scan yet since the last restart")
    lines += ["", "## Coins it looked at, and why it passed"]
    lines += [f"- {look.get('ts', '')[11:16]}Z {look.get('symbol')} ({look.get('setup') or 'no setup'}, "
              f"${look.get('mcap_usd', 0):,} mcap, ${look.get('vol_5m', 0):,} 5m vol): {look.get('outcome')}"
              + (f" at conviction {look['conviction']}" if look.get("conviction") else "")
              + f", {look.get('reason')}  \n  CA `{look.get('ca')}`"
              for look in reversed(status["recent_looks"][-10:])] or ["- none since the last restart"]
    lines += ["", "## Recent lessons", *(status["recent_lessons"] or ["- none yet"])]
    if agent.meta.get("meta_summary"):
        lines += ["", "## Meta right now", agent.meta["meta_summary"]]
    movers = (agent.meta.get("scan_movers") or [])[:5]
    if movers:
        lines += ["", "## Moving most in its scan (1h volume)"]
        lines += [f"- {m.get('symbol')}: ${m.get('vol_1h', 0):,} 1h vol, ${m.get('mcap_usd', 0):,} mcap"
                  + (f", {m['change_1h']:+.0f}% 1h" if isinstance(m.get("change_1h"), (int, float)) else "")
                  + f"  \n  CA `{m.get('ca')}`" for m in movers]
    return status, "\n".join(lines) + "\n"


class DuetBridge:
    def __init__(self, cfg: Config, agent):
        self.cfg = cfg
        self.agent = agent
        self.dir = Path(cfg.duet_sync_dir).expanduser() if cfg.duet_sync_dir else None
        self.last = 0.0
        self.restart_requested = False

    @property
    def enabled(self) -> bool:
        return bool(self.dir) or self.cfg.auto_update

    def tick(self, force: bool = False) -> None:
        if not self.enabled or (not force and time.time() - self.last < self.cfg.duet_sync_interval_min * 60):
            return
        self.last = time.time()
        if self.dir:
            try:
                self.sync()
            except Exception:
                log.exception("Duet sync failed; will retry next interval")
        if self.cfg.auto_update:
            self.check_update()

    def sync(self) -> None:
        branch = self.cfg.duet_sync_branch
        pulled = git(self.dir, "pull", "--rebase", "--autostash", "-q", "origin", branch)
        if pulled.returncode != 0:
            log.warning("Duet sync: pull failed: %s", pulled.stderr.strip()[:200])
        steer_path = self.dir / STEER_FILE
        if steer_path.exists():
            try:
                apply_steering(self.cfg, json.loads(steer_path.read_text() or "{}"))
            except json.JSONDecodeError as e:
                log.warning("Duet sync: steer.json is not valid JSON (%s); keeping current steering", e)

        status, report = build_report(self.agent)
        (self.dir / "status.json").write_text(json.dumps(status, indent=1, default=str))
        (self.dir / "REPORT.md").write_text(report)
        git(self.dir, "add", "status.json", "REPORT.md")
        if git(self.dir, "diff", "--cached", "--quiet").returncode == 0:
            return
        git(self.dir, "-c", "user.name=Trencher", "-c", "user.email=trencher@localhost",
            "commit", "-q", "-m", f"Trencher status {status['updated_at']}")
        pushed = git(self.dir, "push", "-q", "origin", f"HEAD:{branch}")
        if pushed.returncode != 0:
            log.warning("Duet sync: push failed: %s", pushed.stderr.strip()[:200])

    def check_update(self) -> None:
        """If a newer main is waiting, stop so the launcher restarts on it."""
        if os.environ.get("TRENCHER_UPDATE_FAILED"):
            return  # the launcher couldn't apply the last update; don't restart-loop on it
        branch = self.cfg.auto_update_branch
        if git(ROOT, "fetch", "-q", "origin", branch).returncode != 0:
            return
        head = git(ROOT, "rev-parse", "HEAD").stdout.strip()
        remote = git(ROOT, "rev-parse", f"origin/{branch}").stdout.strip()
        if head and remote and head != remote and git(ROOT, "merge-base", "--is-ancestor", head, remote).returncode == 0:
            log.info("Update waiting on %s (%s → %s); restarting on the new code", branch, head[:7], remote[:7])
            self.restart_requested = True
            self.agent.stop()
