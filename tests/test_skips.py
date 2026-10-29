"""Bundle data, probe trades, and the skip review that lets rules loosen as well as tighten."""

import json
import time

import pytest

from agent import journal, skips
from agent.brain import Brain
from agent.checklist import holder_stats, run_checklist
from agent.sizing import fee_check, network_fee_usd

from test_agent import SOL, report, snap

REAL_SOL = 190.0  # where SOL trades: network fees are ~$0.38 a transaction


@pytest.fixture
def cfg(tmp_path, monkeypatch):
    from agent.config import Config
    monkeypatch.setenv("BRAIN", "rules")
    c = Config()
    c.memory_dir = tmp_path
    # Lenny's steering on Oct 29: survival first.
    c.stop_loss_pct, c.take_initials_multiple, c.trailing_stop_pct, c.max_total_risk_pct = 20, 1.5, 20, 15
    return c


def networks(*pcts, supply=10**15):
    return [{"id": f"n{i}", "size": 50, "type": "transfer", "currentHolding": int(supply * p / 100),
             "tokenAmount": int(supply * p / 100), "activeAccounts": 50} for i, p in enumerate(pcts)]


# --- Bundles: RugCheck already had them --------------------------------------

def test_bundle_share_comes_from_rugchecks_wallet_clusters(cfg):
    # HOUSEWORM on Oct 29: 465 flagged wallets in 10 clusters holding ~45% of supply.
    h = holder_stats(report(graphInsidersDetected=465, insiderNetworks=networks(10, 8.4, 7.9, 7.6, 2.4, 2.2, 2.1,
                                                                                    1.9, 1.6, 1.3)), snap())
    assert h["insider_wallets_flagged"] == 465 and h["bundle_networks"] == 10
    assert h["bundles_checked"] and 44 < h["bundle_pct"] < 46 and h["largest_bundle_pct"] == 10
    c = run_checklist(snap(), report(graphInsidersDetected=465, insiderNetworks=networks(10, 8.4, 7.9, 7.6, 2.4,
                                                                                         2.2, 2.1, 1.9, 1.6, 1.3)),
                      [], cfg, SOL)
    assert not c.passed and any("linked wallet cluster" in f for f in c.fails)


def test_no_clusters_is_a_clean_bundle_check_not_unverified(cfg):
    # DESSA on Oct 29: RugCheck found no insider networks at all, then it ran 5x.
    c = run_checklist(snap(), report(insiderNetworks=None), [], cfg, SOL)
    assert c.passed and c.holders["bundle_pct"] == 0
    assert any("no linked wallet clusters" in p for p in c.plusses)
    assert not any("unverified" in w.lower() for w in c.warns)


def test_one_big_cluster_warns_and_missing_data_says_unverified(cfg):
    c = run_checklist(snap(), report(insiderNetworks=networks(6.6, 4.5)), [], cfg, SOL)
    assert c.passed and any("one linked wallet cluster holds 6.6%" in w for w in c.warns)
    c = run_checklist(snap(), report(), [], cfg, SOL)  # no insiderNetworks field at all
    assert c.passed and any("Bundles unverified" in w for w in c.warns)


# --- Partial holder data: probe, don't skip -----------------------------------

def test_pumpfun_coin_without_rugcheck_is_a_partial_pass(cfg):
    c = run_checklist(snap(address="Coin111pump"), None, [], cfg, SOL)
    assert c.passed and c.partial
    c = run_checklist(snap(address="Coin111xyz", dex="raydium"), None, [], cfg, SOL)
    assert not c.passed and "unavailable" in c.fails[0]


def test_empty_holder_list_is_partial(cfg):
    c = run_checklist(snap(), report(topHolders=[]), [], cfg, SOL)
    assert c.passed and c.partial


# --- Probes: conviction 5-6 trades small instead of never -----------------------

def _research(cfg, monkeypatch, conviction, partial=False, sol=REAL_SOL):
    from agent.main import Agent
    agent = Agent(cfg)
    check = run_checklist(snap(), report(insiderNetworks=None), [], cfg, SOL)
    check.partial = partial
    monkeypatch.setattr(agent, "build_dossier", lambda s, sol_, always_crawl=False: check)
    monkeypatch.setattr(agent.brain, "has_budget", lambda: True)
    monkeypatch.setattr(agent.brain, "decide", lambda *a, **k: {
        "action": "BUY", "verdict": "BUY", "conviction": conviction, "thesis": "",
        "exit_plan": {"take_initials_multiple": 1.5, "stop_loss_pct": 20, "trailing_stop_pct": 20,
                      "time_stop_minutes": 45, "target_mcap_usd": 0}})
    agent.research(snap(), sol)
    return agent


@pytest.mark.parametrize("conviction", [5, 6])
def test_conviction_five_and_six_buy_a_probe(cfg, monkeypatch, conviction):
    # Before: a conviction 5-6 position was so small its network fees failed the fee check,
    # so only 7+ could ever trade.
    agent = _research(cfg, monkeypatch, conviction)
    buy = [t for t in journal.read_trades(cfg) if t["event"] == "BUY"]
    assert len(buy) == 1, agent.recent_looks[-1]
    size = buy[0]["size_usd"]
    assert fee_check(size, 1.5, cfg, REAL_SOL, liquidity_usd=40_000).ok
    assert buy[0]["risk_usd"] <= 100 * cfg.probe_max_risk_pct / 100
    assert size < 15  # small: the smallest size whose fees work


def test_partial_holder_data_caps_a_high_conviction_buy_to_a_probe(cfg, monkeypatch):
    full = _research(cfg, monkeypatch, 8)
    full_size = [t for t in journal.read_trades(cfg) if t["event"] == "BUY"][0]["size_usd"]
    (cfg.memory_dir / "trades.jsonl").unlink()
    (cfg.memory_dir / "state.json").unlink(missing_ok=True)
    _research(cfg, monkeypatch, 8, partial=True)
    probe_size = [t for t in journal.read_trades(cfg) if t["event"] == "BUY"][0]["size_usd"]
    assert probe_size < full_size and full is not None


def test_conviction_four_still_risks_nothing(cfg, monkeypatch):
    agent = _research(cfg, monkeypatch, 4)
    assert not agent.pf.positions and agent.recent_looks[-1]["outcome"] == "TOO_SMALL"


def test_sizing_guide_offers_the_probe(cfg):
    from agent.portfolio import Portfolio
    from agent.sizing import sizing_guide
    text = sizing_guide(Portfolio.load(cfg), cfg, sol_usd=REAL_SOL, liquidity_usd=40_000)
    assert "PROBE of ~$" in text and "buys the probe below" in text
    assert network_fee_usd(cfg, REAL_SOL) > 0.3


# --- Skip review --------------------------------------------------------------

def test_gates_name_the_reason():
    assert skips.gate_for("PASS: 11.6% off a peak set 12 minutes ago, bundles unverified. "
                          "That's the CATCULUS setup again.") == "near the high / chasing"
    assert skips.gate_for("Dip with fading attention is a falling knife, not a dip") == "falling knife (code)"
    assert skips.gate_for("Dev holds 3.3% (>1%) (V13, V17)") == "dev share over 1%"
    assert skips.gate_for("PASS: KATT is 3.5 minutes old, sniping") == "too new / sniping"
    assert skips.gate_for("PASS — down 35% in 5 min with no higher low") == "falling knife / no higher low"


def _pair(price):
    return {"priceUsd": str(price)}


def test_skips_settle_as_ran_dumped_or_flat(cfg, monkeypatch):
    from agent import data
    book = {}
    t0 = 1_000_000.0
    monkeypatch.setattr(time, "time", lambda: t0)
    for ca, sym in (("RunA", "DESSA"), ("DumpB", "CATBOT"), ("FlatC", "MEH")):
        skips.record(cfg, book, snap(address=ca, symbol=sym, price_usd=1.0), "PASS",
                     "PASS: 6% under the high, that's the CATCULUS trade again")
    # Skipped again later at a higher price for another reason: keeps the first price, adds the gate.
    skips.record(cfg, book, snap(address="RunA", symbol="DESSA", price_usd=1.3), "REJECT",
                 "Dip with fading attention is a falling knife, not a dip")
    assert book["RunA"]["price"] == 1.0 and len(book["RunA"]["gates"]) == 2

    prices = {"RunA": 1.6, "DumpB": 0.7, "FlatC": 1.1}
    monkeypatch.setattr(data, "get_pairs", lambda cas: {c: _pair(prices[c]) for c in cas})
    assert skips.update(cfg, book, now=t0 + 600) == 2
    assert book["RunA"]["result"] == "ran" and book["DumpB"]["result"] == "dumped"
    assert book["FlatC"]["result"] is None
    assert skips.update(cfg, book, now=t0 + 7 * 3600) == 1 and book["FlatC"]["result"] == "flat"

    st = skips.stats(book, now=t0 + 7 * 3600)
    chase = st["near the high / chasing"]
    assert chase["blocked"] == 3 and chase["ran"] == 1 and chase["dumped"] == 1 and chase["flat"] == 1
    assert chase["ran_examples"][0]["ca"] == "RunA"
    assert st["falling knife (code)"]["ran"] == 1
    assert "ran: DESSA" in skips.prompt_text(book)


def test_verdict_reads_both_ways():
    assert "loosen" in skips.verdict({"ran": 4, "dumped": 1, "flat": 0})
    assert "keep" in skips.verdict({"ran": 1, "dumped": 5, "flat": 0})
    assert "too few" in skips.verdict({"ran": 1, "dumped": 0, "flat": 9})


def test_agent_files_its_skips_and_evolves_from_them_with_no_closed_trades(cfg, monkeypatch):
    from agent import data
    from agent.bridge import build_report
    from agent.main import Agent
    agent = Agent(cfg)
    for i in range(12):
        agent.note_look(snap(address=f"Coin{i}", symbol=f"C{i}", price_usd=1.0), "MIGRATED", "PASS",
                        "PASS: 5% under its high, chasing", conviction=4)
    agent.note_look(snap(address="Bought", price_usd=1.0), "MIGRATED", "BUY", "BUY")
    assert len(agent.skips) == 12 and "Bought" not in agent.skips

    seen = {}

    def fake_evolve(trades, skip_review=""):
        seen["trades"], seen["skips"] = trades, skip_review
        return {"rules_markdown": "- near-high momentum buys allowed as probes when bundles check clean",
                "param_changes": [{"param": "dip_min_attention_ratio", "value": 0.35, "reason": "knives ran"}],
                "rule_changes": [{"change": "loosened", "rule": "no buys within 20% of the high",
                                  "evidence": "blocked 12, 9 ran, 1 dumped"},
                                 {"change": "kept", "rule": "dev under 1%", "evidence": "n/a"}]}

    monkeypatch.setattr(agent.brain, "evolve", fake_evolve)
    monkeypatch.setattr(data, "get_pairs", lambda cas: {c: _pair(1.6) for c in cas})
    now = time.time()
    agent.review_skips(now)  # first run settles the skips but waits before evolving
    assert all(r["result"] == "ran" for r in agent.skips.values())
    assert "trades" not in seen
    agent.review_skips(now + cfg.skip_evolve_every_hours * 3600 + 60)
    assert seen["trades"] == [] and "near the high / chasing: blocked 12, ran 12" in seen["skips"]
    assert cfg.dip_min_attention_ratio == 0.35
    assert "loosened" in (cfg.memory_dir / "strategy_log.md").read_text()
    assert "near-high momentum" in journal.learned_rules(cfg)

    status, rep = build_report(agent)
    assert status["skip_review"]["near the high / chasing"]["ran"] == 12
    assert "## What its skips did next" in rep and "cost more winners than it saved: loosen it" in rep
    assert "CA `Coin0`" in rep
    assert "## Rules it changed from results and skips" in rep and "no buys within 20% of the high" in rep
    assert "dev under 1%" not in rep  # "kept" isn't a change


def test_skips_survive_a_restart(cfg):
    from agent.main import Agent
    agent = Agent(cfg)
    agent.note_look(snap(address="Coin1", price_usd=1.0), "DIP", "REJECT", "Dip with fading attention")
    agent.review_skips(time.time())
    assert "Coin1" in Agent(cfg).skips


def test_dip_falling_knife_line_is_evolvable(cfg):
    from agent.config import EVOLVABLE
    dip = snap(mcap_usd=100_000, peak_mcap_usd=220_000, drawdown_pct=55.0, vol_5m_vs_hour_avg=0.4)
    assert not run_checklist(dip, report(), [], cfg, SOL).passed
    cfg.dip_min_attention_ratio = 0.35
    assert run_checklist(dip, report(), [], cfg, SOL).passed
    assert "dip_min_attention_ratio" in EVOLVABLE


# --- Prompts ------------------------------------------------------------------

def test_decide_prompt_has_the_skip_review_bundles_and_probe_scale(cfg, monkeypatch, tmp_path):
    from agent.checklist import Checklist
    monkeypatch.setenv("BRAIN", "subscription")
    cli = tmp_path / "claude"
    cli.write_text("#!/bin/sh\n")
    cli.chmod(0o755)
    cfg.claude_cli = str(cli)
    b = Brain(cfg)
    book = {}
    skips.record(cfg, book, snap(address="RunA", symbol="DESSA", price_usd=1.0), "PASS", "chasing near the high")
    book["RunA"]["result"] = "ran"
    skips.save(cfg, book)
    seen = {}
    monkeypatch.setattr(b, "_ask", lambda prompt, *a, **k: seen.setdefault("p", prompt) and None)
    b.decide(snap(), Checklist(setup="MIGRATED"), {"equity_usd": 100}, "sizing", radar_view={"meta_summary": "x"})
    p = seen["p"]
    assert "What the coins you passed on did next" in p and "near the high / chasing: blocked 1, ran 1" in p
    assert "Bundles ARE in this data" in p and "not a buy/no-buy rule" in p
    assert "BUY a small probe" in p and "not a PASS" in p

    monkeypatch.setattr(b, "_ask", lambda prompt, *a, **k: seen.__setitem__("m", prompt) or {"summary": "ok"})
    b.summarize_meta({"scan_movers": []})
    assert "never a reason to say \"no buys\"" in seen["m"]

    monkeypatch.setattr(b, "_ask", lambda prompt, *a, **k: seen.__setitem__("r", prompt) or {"lesson": "ok"})
    b.reflect({"symbol": "X", "pnl_usd": -1, "pnl_pct": -10, "exit_reasons": ["stop"]})
    assert "sample of one" in seen["r"]

    monkeypatch.setattr(b, "_ask", lambda prompt, *a, **k: seen.__setitem__("e", prompt) or None)
    b.evolve([], "- near the high / chasing: blocked 6, ran 4")
    assert "Rules work both ways" in seen["e"] and "blocked 6, ran 4" in seen["e"]
