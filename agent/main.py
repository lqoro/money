"""Trencher's 24/7 loop: scan → checklist → brain → paper buy, and monitor open
positions for exits. Run with `python -m agent run`."""

from __future__ import annotations

import argparse
import json
import logging
import signal
import sys
import time

from . import data, journal, radar
from .api import start_api
from .brain import Brain
from .bridge import DuetBridge
from .checklist import holder_stats, market_prefilter, run_checklist
from .config import Config
from .evolve import evolve
from .notify import notify
from .portfolio import Portfolio, Position
from .risk import check_exit, sanitize_exit_plan
from .site import project_report
from .sizing import open_risk_usd, position_size, sizing_guide

log = logging.getLogger("trencher")


class Agent:
    def __init__(self, cfg: Config, dry_run: bool = False):
        self.cfg = cfg
        self.dry_run = dry_run
        self.pf = Portfolio.load(cfg)
        self.brain = Brain(cfg)
        self.cooldown: dict[str, float] = {}  # token → time we may look at it again
        self.exit_log: dict[str, list[str]] = {}
        self.running = True
        # peaks: token → [highest mcap seen, last seen]; watchlist: coins we were stopped out of
        watch_path = cfg.memory_dir / "watch.json"
        watch = json.loads(watch_path.read_text()) if watch_path.exists() else {}
        self.peaks: dict[str, list[float]] = watch.get("peaks", {})
        self.watchlist: dict[str, dict] = watch.get("watchlist", {})
        self.meta: dict = radar.load_radar(cfg)  # the web crawler's view of the meta
        self.bridge = DuetBridge(cfg, self)

    # ---------------------------------------------------------------- web crawler
    def refresh_radar(self, force: bool = False) -> None:
        cfg = self.cfg
        if not force and time.time() - self.meta.get("updated_at", 0) < cfg.radar_interval_min * 60:
            return
        self.meta = radar.build_radar(cfg, previous=self.meta)
        if (time.time() - self.meta.get("meta_summary_at", 0) >= cfg.meta_summary_interval_min * 60
                and self.brain.use_claude):
            summary = self.brain.summarize_meta(radar.public_view(self.meta))
            if summary:
                self.meta["meta_summary"], self.meta["meta_summary_at"] = summary, time.time()
                log.info("Meta: %s", summary)
        radar.save_radar(cfg, self.meta)
        top = ", ".join(n["term"] for n in self.meta.get("top_narratives", [])[:8])
        log.info("Radar: %s | hot: %s", self.meta.get("sources"), top or "(quiet)")

    def save_watch(self) -> None:
        now = time.time()
        self.peaks = {k: v for k, v in self.peaks.items() if now - v[1] < 48 * 3600}
        self.watchlist = {k: v for k, v in self.watchlist.items() if v.get("until", 0) > now}
        (self.cfg.memory_dir / "watch.json").write_text(json.dumps({"peaks": self.peaks, "watchlist": self.watchlist}))

    def track_peak(self, snap: dict) -> None:
        """Remember the highest market cap we've seen, so we can tell a dip from a dud."""
        addr, mcap = snap["address"], snap["mcap_usd"]
        prev = self.peaks.get(addr, [0.0, 0.0])
        # A big negative 1h/24h change means it was at least that much higher before.
        worst = min((c for c in (snap.get("change_1h"), snap.get("change_24h")) if c is not None), default=0)
        implied = mcap / (1 + worst / 100) if -99 < worst < 0 else 0.0
        self.peaks[addr] = [max(prev[0], mcap, implied), time.time()]
        peak = self.peaks[addr][0]
        snap["peak_mcap_usd"] = peak
        snap["drawdown_pct"] = round(100 * (1 - mcap / peak), 1) if peak else 0.0

    # ---------------------------------------------------------------- views
    def portfolio_view(self) -> dict:
        pf = self.pf
        return {
            "equity_usd": round(pf.equity(), 2),
            "cash_usd": round(pf.cash_usd, 2),
            "started_with_usd": self.cfg.starting_cash_usd,
            "realized_pnl_usd": round(pf.realized_pnl_usd, 2),
            "fees_paid_usd": round(pf.fees_paid_usd, 2),
            "closed_trades": pf.trades_closed,
            "win_rate": round(pf.wins / pf.trades_closed, 2) if pf.trades_closed else None,
            "open_positions": [
                {"symbol": p.symbol, "setup": p.setup, "cost_usd": round(p.cost_usd, 2),
                 "value_usd": round(p.value(), 2), "multiple": round((p.last_price or p.entry_price) / p.entry_price, 2),
                 "initials_taken": p.initials_taken}
                for p in pf.positions.values()
            ],
        }

    # ---------------------------------------------------------------- scan
    def scan(self) -> None:
        self.pf.roll_day()
        ok, why = self.pf.can_open(self.cfg)
        if ok and self.cfg.pause_new_trades:
            ok, why = False, "paused from Claude Duet"
        if not ok:
            log.info("Not opening new trades: %s", why)
            return
        sol = data.sol_price_usd()
        now = time.time()
        discovered = data.discover_solana_tokens()
        # Contract addresses the crawler saw called on Telegram/Reddit in the last 2h.
        discovered += [a for a, v in self.meta.get("called_cas", {}).items()
                       if now - v.get("last_seen", 0) < 7200 and a not in discovered]
        watched = [t for t, w in self.watchlist.items() if w.get("until", 0) > now and t not in discovered]
        tokens = [t for t in discovered + watched
                  if self.cooldown.get(t, 0) < now and not self.pf.holds(t)]
        pairs = data.get_pairs(tokens)
        candidates = []
        for addr, pair in pairs.items():
            snap = data.pair_snapshot(pair)
            self.track_peak(snap)
            setup = market_prefilter(snap, self.cfg, sol)
            if setup:
                candidates.append(snap)
            else:
                self.cooldown[addr] = now + 10 * 60
        candidates.sort(key=lambda s: s["vol_5m"], reverse=True)
        log.info("Scan: %d tokens (%d on watchlist), %d pairs, %d pass market filters (SOL $%.2f)",
                 len(tokens), len(watched), len(pairs), len(candidates), sol)
        self.save_watch()

        for snap in candidates[: self.cfg.max_candidates_per_scan]:
            if not self.running or not self.pf.can_open(self.cfg)[0]:
                break
            self.research(snap, sol)

    def build_dossier(self, snap: dict, sol: float, always_crawl: bool = False):
        """Everything we can learn about a token without asking Claude."""
        cfg = self.cfg
        # Price path: how far off the recent high is it? (dip vs. dud)
        hist = data.price_history(snap)
        if hist:
            snap.update(hist)
            peak = max(snap.get("peak_mcap_usd") or 0, hist["peak_mcap_24h"])
            snap["peak_mcap_usd"] = round(peak)
            snap["drawdown_pct"] = round(100 * (1 - snap["mcap_usd"] / peak), 1) if peak else 0.0
        snap["buzz"] = radar.token_buzz(snap, self.meta)
        report = data.rugcheck_report(snap["address"])
        same = data.search_same_name(snap["symbol"]) if snap["symbol"] else []
        check = run_checklist(snap, report, same, cfg, sol)
        # Only crawl the project's site once it clears the hard lines (it's slow).
        if check.passed or always_crawl:
            snap["web"] = project_report(snap, cfg)
            check = run_checklist(snap, report, same, cfg, sol)
        return check

    def inspect_token(self, address: str) -> dict | None:
        """Full crawl + checklist on any token, for the CLI and the API. No Claude call."""
        pair = data.get_pairs([address]).get(address)
        if not pair:
            return None
        snap = data.pair_snapshot(pair)
        self.track_peak(snap)
        check = self.build_dossier(snap, data.sol_price_usd(), always_crawl=True)
        return {"token": snap, "checklist": check.as_dict()}

    def status(self) -> dict:
        return {**self.portfolio_view(), "strategy": self.cfg.strategy_view(),
                "watchlist": list(self.watchlist.values()), "meta": radar.public_view(self.meta, headlines=5)}

    def research(self, snap: dict, sol: float) -> None:
        cfg = self.cfg
        addr = snap["address"]
        self.cooldown[addr] = time.time() + cfg.reject_cooldown_min * 60
        check = self.build_dossier(snap, sol)
        if not check.passed:
            log.info("  ✗ %-10s %s", snap["symbol"], check.fails[0] if check.fails else "no setup")
            journal.log_decision(cfg, {"token": addr, "symbol": snap["symbol"], "action": "REJECT",
                                       "fails": check.fails, "warns": check.warns})
            return
        if not self.brain.has_budget():
            log.info("  … %-10s passed checklist but the brain is paced or paused right now", snap["symbol"])
            self.brain.note("skipped")
            self.cooldown[addr] = time.time() + 5 * 60
            return

        decision = self.brain.decide(snap, check, self.portfolio_view(), sizing_guide(self.pf, cfg),
                                     history=self.watchlist.get(addr), radar_view=radar.public_view(self.meta))
        log.info("  ◆ %-10s %s", snap["symbol"], decision.get("verdict"))
        plan = sanitize_exit_plan(decision.get("exit_plan"), cfg)
        sizing = position_size(int(decision.get("conviction") or 0), plan["stop_loss_pct"], self.pf, cfg)
        journal.log_decision(cfg, {"token": addr, "symbol": snap["symbol"], "snapshot": snap,
                                   "checklist": check.as_dict(), "decision": decision,
                                   "sizing": sizing.__dict__})
        if decision.get("action") != "BUY":
            return
        size = sizing.size_usd
        log.info("    sizing: %s → $%.2f (loses ~$%.2f at the stop)", sizing.note, size, sizing.risk_usd)
        if size < cfg.min_position_usd:
            log.info("    size $%.2f below minimum, skipping", size)
            return
        if self.dry_run:
            log.info("    [dry run] would buy $%.2f", size)
            return
        pos = self.pf.buy(cfg, snap, size, sol, check.setup, plan, decision.get("thesis", ""))
        pos.entry_holders = check.holders
        self.watchlist.pop(addr, None)
        self.pf.save(cfg)
        journal.log_trade(cfg, {"event": "BUY", "id": pos.id, "token": addr, "symbol": pos.symbol,
                                "setup": pos.setup, "size_usd": size, "conviction": decision.get("conviction"),
                                "risk_usd": sizing.risk_usd, "price": pos.entry_price,
                                "mcap": snap["mcap_usd"], "exit_plan": plan, "thesis": pos.thesis})
        notify(cfg, f"🟢 BUY ${size:.2f} {pos.symbol} ({pos.setup}, conviction {decision.get('conviction')}/10, "
                    f"risking ${sizing.risk_usd:.2f}) @ ${snap['mcap_usd']:,.0f} mcap\n"
                    f"{decision.get('verdict')}\n{snap['url']}")

    # ---------------------------------------------------------------- monitor
    def monitor(self) -> None:
        if not self.pf.positions:
            return
        sol = data.sol_price_usd()
        pairs = data.get_pairs(list({p.address for p in self.pf.positions.values()}))
        for pos in list(self.pf.positions.values()):
            pair = pairs.get(pos.address)
            if pair is None:
                log.warning("No market data for %s this tick", pos.symbol)
                continue
            snap = data.pair_snapshot(pair)
            pos.last_price = snap["price_usd"]
            pos.peak_price = max(pos.peak_price, snap["price_usd"])
            signal_ = check_exit(pos, snap, self.cfg)
            if signal_ and signal_.review:
                self.review_stop(pos, snap, signal_.reason, sol)
            elif signal_:
                self.execute_exit(pos, snap, signal_.fraction, signal_.reason, signal_.rugged, sol)
        self.pf.save(self.cfg)

    def review_stop(self, pos: Position, snap: dict, reason: str, sol: float) -> None:
        """The stop hit. A stop is a decision point: was it a bundle exit / shakeout with
        the narrative intact (hold once, to the hard floor, with a deadline), or is the
        coin dead (sell)?"""
        cfg = self.cfg
        pos.stop_reviews += 1
        report = data.rugcheck_report(pos.address)
        holders_now = holder_stats(report, snap) if report else {}
        pos_view = {
            "symbol": pos.symbol, "setup": pos.setup, "thesis": pos.thesis,
            "entry_mcap": pos.entry_mcap, "mcap_now": snap["mcap_usd"],
            "multiple": round(snap["price_usd"] / pos.entry_price, 2),
            "minutes_held": round((time.time() - pos.opened_at) / 60),
            "planned_stop_pct": pos.exit_plan.get("stop_loss_pct"), "entry_holders": pos.entry_holders,
        }
        rv = self.brain.review_stop(pos_view, snap, holders_now)
        action = rv.get("action", "SELL")
        new_stop = min(cfg.hard_stop_pct, max(float(rv.get("new_stop_loss_pct") or 0),
                                              pos.exit_plan.get("stop_loss_pct", cfg.stop_loss_pct)))
        # Holding to a deeper stop puts more at risk; it must still fit the total risk budget.
        if action == "HOLD":
            extra = pos.cost_usd * (new_stop - pos.exit_plan.get("stop_loss_pct", cfg.stop_loss_pct)) / 100
            if open_risk_usd(self.pf, cfg) + extra > self.pf.equity() * cfg.max_total_risk_pct / 100:
                action = "SELL_HALF"
                rv["verdict"] = (rv.get("verdict") or "") + " (trimmed: holding all would break the risk budget)"
        journal.log_decision(cfg, {"token": pos.address, "symbol": pos.symbol, "action": "STOP_REVIEW",
                                   "review": rv, "final_action": action, "holders_now": holders_now})
        log.info("  ⚖ %-10s stop review: %s", pos.symbol, rv.get("verdict"))
        notify(cfg, f"⚖️ {pos.symbol} hit its stop — {rv.get('verdict')}")
        self.exit_log.setdefault(pos.id, []).append(f"stop review: {action} ({rv.get('cause')})")
        if action == "SELL":
            self.execute_exit(pos, snap, 1.0, reason, False, sol)
            return
        if action == "SELL_HALF":
            self.execute_exit(pos, snap, 0.5, f"{reason}; trimmed half on review", False, sol)
            if pos.id not in self.pf.positions:
                return
        plan = pos.exit_plan
        plan.setdefault("_orig_stop", plan.get("stop_loss_pct", cfg.stop_loss_pct))
        plan["stop_loss_pct"] = new_stop
        plan["hold_until"] = time.time() + 60 * min(240.0, max(10.0, float(rv.get("recheck_minutes") or 30)))

    def execute_exit(self, pos: Position, snap: dict, fraction: float, reason: str, rugged: bool, sol: float) -> None:
        cfg = self.cfg
        proceeds = self.pf.sell(cfg, pos, fraction, snap["price_usd"], snap["liquidity_usd"], sol, rugged)
        self.exit_log.setdefault(pos.id, []).append(reason)
        if "initials" in reason:
            pos.initials_taken = True
        journal.log_trade(cfg, {"event": "SELL", "id": pos.id, "token": pos.address, "symbol": pos.symbol,
                                "fraction": round(fraction, 3), "proceeds_usd": round(proceeds, 2),
                                "price": snap["price_usd"], "mcap": snap["mcap_usd"], "reason": reason})
        log.info("  ↘ SELL %.0f%% %s for $%.2f — %s", fraction * 100, pos.symbol, proceeds, reason)

        if pos.tokens * snap["price_usd"] < 0.05 or fraction >= 0.999:
            pnl = self.pf.close(pos)
            trade = {
                "id": pos.id, "symbol": pos.symbol, "token": pos.address, "setup": pos.setup,
                "cost_usd": round(pos.cost_usd, 2), "proceeds_usd": round(pos.realized_usd, 2),
                "pnl_usd": round(pnl, 2), "pnl_pct": round(100 * pnl / pos.cost_usd, 1),
                "held_minutes": round((time.time() - pos.opened_at) / 60),
                "entry_mcap": pos.entry_mcap, "exit_mcap": snap["mcap_usd"],
                "peak_multiple": round(pos.peak_price / pos.entry_price, 2),
                "exit_reasons": self.exit_log.pop(pos.id, [reason]),
                "stop_reviews": pos.stop_reviews,
                "thesis": pos.thesis, "exit_plan": pos.exit_plan,
            }
            lesson = self.brain.reflect(trade)
            journal.add_lesson(cfg, lesson)
            journal.log_trade(cfg, {"event": "CLOSE", **trade, "lesson": lesson})
            if "stop" in reason and not rugged:
                # Stopped out, not rugged: keep watching in case the narrative holds and it reclaims.
                self.watchlist[pos.address] = {
                    "symbol": pos.symbol, "stopped_out_at_mcap": round(snap["mcap_usd"]),
                    "entry_mcap": round(pos.entry_mcap), "pnl_pct": trade["pnl_pct"], "why": reason,
                    "lesson": lesson, "until": time.time() + cfg.reentry_window_hours * 3600,
                }
                self.cooldown[pos.address] = time.time() + 15 * 60
                self.save_watch()
            emoji = "✅" if pnl > 0 else "🔴"
            notify(cfg, f"{emoji} CLOSED {pos.symbol} {trade['pnl_pct']:+.0f}% (${pnl:+.2f}) — {reason}\n"
                        f"Equity ${self.pf.equity():.2f}\nLesson: {lesson}")
            log.info("  ■ CLOSED %s %+.2f USD. Equity $%.2f. Lesson: %s", pos.symbol, pnl, self.pf.equity(), lesson)
            if self.pf.trades_closed % cfg.reflect_every_n_trades == 0:
                summary = evolve(cfg, self.brain)
                if summary:
                    log.info(summary)
                    notify(cfg, summary)

    # ---------------------------------------------------------------- loop
    def run(self, once: bool = False) -> None:
        log.info("Trencher online. Equity $%.2f, %d open position(s).", self.pf.equity(), len(self.pf.positions))
        notify(self.cfg, f"🪖 Trencher online. Paper equity ${self.pf.equity():.2f}.")
        last_scan = 0.0
        start_api(self.cfg, self.status, self.inspect_token)
        self.bridge.tick(force=True)
        while self.running:
            try:
                self.bridge.tick()
                self.refresh_radar()
                self.monitor()
                if time.time() - last_scan >= self.cfg.scan_interval_sec:
                    last_scan = time.time()
                    self.scan()
            except Exception:  # keep the 24/7 loop alive no matter what one tick does
                log.exception("tick failed")
            if once:
                break
            time.sleep(self.cfg.monitor_interval_sec)
        self.pf.save(self.cfg)
        if self.bridge.dir:
            try:
                self.bridge.sync()  # last report before going offline
            except Exception:
                log.exception("final Duet sync failed")
        log.info("Trencher offline. Equity $%.2f.", self.pf.equity())

    def stop(self, *_):
        self.running = False


def print_status(cfg: Config) -> None:
    pf = Portfolio.load(cfg)
    if pf.positions:
        pairs = data.get_pairs([p.address for p in pf.positions.values()])
        for p in pf.positions.values():
            if p.address in pairs:
                p.last_price = data.pair_snapshot(pairs[p.address])["price_usd"]
    eq = pf.equity()
    print(f"Equity      ${eq:,.2f}  ({100 * (eq / cfg.starting_cash_usd - 1):+.1f}% vs ${cfg.starting_cash_usd:.0f} start)")
    print(f"Cash        ${pf.cash_usd:,.2f}")
    print(f"Realized    ${pf.realized_pnl_usd:+,.2f} over {pf.trades_closed} trades"
          + (f", win rate {100 * pf.wins / pf.trades_closed:.0f}%" if pf.trades_closed else ""))
    print(f"Fees paid   ${pf.fees_paid_usd:,.2f}")
    for p in pf.positions.values():
        m = (p.last_price or p.entry_price) / p.entry_price
        print(f"  {p.symbol:<10} {p.setup:<13} cost ${p.cost_usd:6.2f}  value ${p.value():6.2f}  {m:5.2f}x"
              f"{'  (initials out)' if p.initials_taken else ''}")
    strategy = cfg.memory_dir / "strategy.json"
    if strategy.exists():
        print("\nEvolved strategy: " + strategy.read_text().replace("\n", " "))
    rules = journal.learned_rules(cfg)
    if rules:
        print("\nLearned rules:\n" + rules)
    lessons = journal.recent_lessons(cfg, 5)
    if lessons:
        print("Recent lessons:\n" + "\n".join(lessons))


def main(argv: list[str] | None = None) -> None:
    ap = argparse.ArgumentParser(prog="python -m agent", description="Trencher: 24/7 paper memecoin agent")
    sub = ap.add_subparsers(dest="cmd", required=True)
    r = sub.add_parser("run", help="run the 24/7 loop")
    r.add_argument("--once", action="store_true", help="one scan + monitor tick, then exit")
    r.add_argument("--dry-run", action="store_true", help="research and decide, but don't place paper trades")
    sub.add_parser("status", help="show the paper wallet")
    sub.add_parser("evolve", help="study closed trades now and evolve the strategy")
    sub.add_parser("meta", help="crawl the web now and show the meta radar")
    sub.add_parser("brain", help="check that the Claude brain answers (one small call)")
    cr = sub.add_parser("crawl", help="crawl + checklist one token (no trade, no Claude)")
    cr.add_argument("address")
    rs = sub.add_parser("reset", help="wipe the wallet back to the starting cash (keeps lessons)")
    rs.add_argument("--all", action="store_true", help="also wipe lessons, learned rules and logs")
    ap.add_argument("-v", "--verbose", action="store_true")
    args = ap.parse_args(argv)

    cfg = Config.from_env()
    handlers = [logging.StreamHandler(sys.stderr), logging.FileHandler(cfg.memory_dir / "agent.log")]
    logging.basicConfig(level=logging.DEBUG if args.verbose else logging.INFO,
                        format="%(asctime)s %(levelname).1s %(message)s", datefmt="%m-%d %H:%M:%S", handlers=handlers)
    for noisy in ("urllib3", "httpx", "httpcore", "anthropic"):
        logging.getLogger(noisy).setLevel(logging.WARNING)

    if args.cmd == "status":
        print_status(cfg)
    elif args.cmd == "meta":
        agent = Agent(cfg)
        agent.refresh_radar(force=True)
        print(json.dumps(radar.public_view(agent.meta, headlines=15), indent=1))
    elif args.cmd == "crawl":
        result = Agent(cfg).inspect_token(args.address)
        print(json.dumps(result, indent=1, default=str) if result else "No Solana pair found for that address.")
    elif args.cmd == "brain":
        b = Brain(cfg)
        if not b.use_claude:
            print("Rules-only brain: no Claude Code CLI on PATH and no ANTHROPIC_API_KEY.")
            sys.exit(1)
        out = b._ask("Brain check. In one short sentence as Trencher, say you're online.",
                     {"type": "object", "properties": {"summary": {"type": "string"}},
                      "required": ["summary"], "additionalProperties": False}, "low", web=False)
        print(f"{b.backend}: {out['summary']}" if out else f"{b.backend}: no answer, see the log above.")
        sys.exit(0 if out else 1)
    elif args.cmd == "evolve":
        print(evolve(cfg, Brain(cfg)) or "Nothing to evolve yet (needs closed trades and the Claude brain).")
    elif args.cmd == "reset":
        names = ["state.json", "watch.json", "narratives.json"] + (["trades.jsonl", "decisions.jsonl", "lessons.md", "learned_rules.md",
                                                  "strategy.json", "strategy_log.md"] if args.all else [])
        for name in names:
            (cfg.memory_dir / name).unlink(missing_ok=True)
        print(f"Reset. Trencher starts again with ${cfg.starting_cash_usd:.2f}.")
    else:
        agent = Agent(cfg, dry_run=args.dry_run)
        signal.signal(signal.SIGTERM, agent.stop)
        signal.signal(signal.SIGINT, agent.stop)
        agent.run(once=args.once)


if __name__ == "__main__":
    main()
