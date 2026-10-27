"""Trencher's 24/7 loop: scan → checklist → brain → paper buy, and monitor open
positions for exits. Run with `python -m agent run`."""

from __future__ import annotations

import argparse
import logging
import signal
import sys
import time

from . import data, journal
from .brain import Brain
from .checklist import market_prefilter, run_checklist
from .config import Config
from .notify import notify
from .portfolio import Portfolio, Position
from .risk import check_exit, sanitize_exit_plan
from .sizing import position_size, sizing_guide

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
        if not ok:
            log.info("Not opening new trades: %s", why)
            return
        sol = data.sol_price_usd()
        now = time.time()
        tokens = [t for t in data.discover_solana_tokens()
                  if self.cooldown.get(t, 0) < now and not self.pf.holds(t)]
        pairs = data.get_pairs(tokens)
        candidates = []
        for addr, pair in pairs.items():
            snap = data.pair_snapshot(pair)
            setup = market_prefilter(snap, self.cfg, sol)
            if setup:
                candidates.append(snap)
            else:
                self.cooldown[addr] = now + 10 * 60
        candidates.sort(key=lambda s: s["vol_5m"], reverse=True)
        log.info("Scan: %d tokens discovered, %d pairs, %d pass market filters (SOL $%.2f)",
                 len(tokens), len(pairs), len(candidates), sol)

        for snap in candidates[: self.cfg.max_candidates_per_scan]:
            if not self.running or not self.pf.can_open(self.cfg)[0]:
                break
            self.research(snap, sol)

    def research(self, snap: dict, sol: float) -> None:
        cfg = self.cfg
        addr = snap["address"]
        self.cooldown[addr] = time.time() + cfg.reject_cooldown_min * 60
        report = data.rugcheck_report(addr)
        same = data.search_same_name(snap["symbol"]) if snap["symbol"] else []
        check = run_checklist(snap, report, same, cfg, sol)
        if not check.passed:
            log.info("  ✗ %-10s %s", snap["symbol"], check.fails[0] if check.fails else "no setup")
            journal.log_decision(cfg, {"token": addr, "symbol": snap["symbol"], "action": "REJECT",
                                       "fails": check.fails, "warns": check.warns})
            return
        if not self.brain.has_budget():
            log.info("  … %-10s passed checklist but brain budget for this hour is used up", snap["symbol"])
            self.cooldown[addr] = time.time() + 5 * 60
            return

        decision = self.brain.decide(snap, check, self.portfolio_view(), sizing_guide(self.pf, cfg))
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
            if signal_:
                self.execute_exit(pos, snap, signal_.fraction, signal_.reason, signal_.rugged, sol)
        self.pf.save(self.cfg)

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
                "thesis": pos.thesis, "exit_plan": pos.exit_plan,
            }
            lesson = self.brain.reflect(trade)
            journal.add_lesson(cfg, lesson)
            journal.log_trade(cfg, {"event": "CLOSE", **trade, "lesson": lesson})
            emoji = "✅" if pnl > 0 else "🔴"
            notify(cfg, f"{emoji} CLOSED {pos.symbol} {trade['pnl_pct']:+.0f}% (${pnl:+.2f}) — {reason}\n"
                        f"Equity ${self.pf.equity():.2f}\nLesson: {lesson}")
            log.info("  ■ CLOSED %s %+.2f USD. Equity $%.2f. Lesson: %s", pos.symbol, pnl, self.pf.equity(), lesson)
            if self.pf.trades_closed % cfg.reflect_every_n_trades == 0:
                closes = [t for t in journal.read_trades(cfg) if t.get("event") == "CLOSE"]
                rules = self.brain.condense_rules(closes)
                if rules:
                    journal.save_learned_rules(cfg, rules)
                    log.info("Updated learned rules:\n%s", rules)
                    notify(cfg, f"📚 Trencher updated its learned rules after {len(closes)} trades:\n{rules}")

    # ---------------------------------------------------------------- loop
    def run(self, once: bool = False) -> None:
        log.info("Trencher online. Equity $%.2f, %d open position(s).", self.pf.equity(), len(self.pf.positions))
        notify(self.cfg, f"🪖 Trencher online. Paper equity ${self.pf.equity():.2f}.")
        last_scan = 0.0
        while self.running:
            try:
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
    rs = sub.add_parser("reset", help="wipe the wallet back to the starting cash (keeps lessons)")
    rs.add_argument("--all", action="store_true", help="also wipe lessons, learned rules and logs")
    ap.add_argument("-v", "--verbose", action="store_true")
    args = ap.parse_args(argv)

    cfg = Config.from_env()
    handlers = [logging.StreamHandler(sys.stdout), logging.FileHandler(cfg.memory_dir / "agent.log")]
    logging.basicConfig(level=logging.DEBUG if args.verbose else logging.INFO,
                        format="%(asctime)s %(levelname).1s %(message)s", datefmt="%m-%d %H:%M:%S", handlers=handlers)
    for noisy in ("urllib3", "httpx", "httpcore", "anthropic"):
        logging.getLogger(noisy).setLevel(logging.WARNING)

    if args.cmd == "status":
        print_status(cfg)
    elif args.cmd == "reset":
        names = ["state.json"] + (["trades.jsonl", "decisions.jsonl", "lessons.md", "learned_rules.md"] if args.all else [])
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
