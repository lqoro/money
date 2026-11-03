"""Watch-only week (owner, Nov 3): scan and decide, buy nothing, log what every coin did
next. Haiku for routine calls, Opus once a day at the head of the chain."""

import json

import pytest

from agent import watch
from agent.bridge import apply_steering, build_report, copy_observations

from test_agent import SOL, _agent_with_decision, _plan, snap


@pytest.fixture
def cfg(tmp_path, monkeypatch):
    from agent.config import Config
    monkeypatch.setenv("BRAIN", "rules")
    c = Config()
    c.memory_dir = tmp_path
    c.watch_only = True
    return c


T0 = 1_800_000_000.0


def test_an_observation_follows_the_price_and_files_when_done(cfg):
    book = {}
    rec = watch.observe(cfg, book, snap(price_usd=1.0), "MIGRATED", SOL, now=T0)
    assert rec and rec["stage"] == "candidate" and rec["features"]["mcap_usd"]
    # The same coin again inside 30 minutes is the same observation.
    assert watch.observe(cfg, book, snap(price_usd=1.2), "MIGRATED", SOL, now=T0 + 600) is rec
    ca = rec["ca"]
    path = [(5, 1.1), (16, 1.6), (31, 0.75), (61, 2.1), (130, 1.0)]
    for minute, x in path:
        assert watch.sample(cfg, book, now=T0 + minute * 60, prices={ca: x}) == 0
    assert rec["up_at"] == {"1.3": 16.0, "1.5": 16.0, "2.0": 61.0}
    assert rec["down_at"] == {"0.9": 31.0, "0.8": 31.0}
    assert rec["x_at"]["5"] == 1.1 and rec["x_at"]["15"] == 1.6 and rec["x_at"]["60"] == 2.1
    assert rec["max_x"] == 2.1 and rec["max_at_min"] == 61.0 and rec["min_x"] == 0.75
    # 1.5x came before -20%, so the plain plan sells at 1.5x.
    assert watch.simple_plan_x(rec) == 1.5
    assert watch.sample(cfg, book, now=T0 + 6 * 3600 + 1, prices={ca: 1.0}) == 1
    assert not book
    filed = watch.read_settled(cfg)
    assert len(filed) == 1 and filed[0]["result"] == "done" and filed[0]["ca"] == ca
    # Past the re-observe window a new observation opens.
    assert watch.observe(cfg, book, snap(price_usd=1.0), "MIGRATED", SOL, now=T0 + 3600)["at"] == T0 + 3600


def test_stop_counts_when_both_lines_cross_between_samples(cfg):
    book = {}
    rec = watch.observe(cfg, book, snap(price_usd=1.0), "DIP", SOL, now=T0)
    rec["up_at"], rec["down_at"] = {"1.5": 10.0}, {"0.8": 10.0}
    assert watch.simple_plan_x(rec) == 0.8


def test_a_coin_with_no_price_for_an_hour_is_filed(cfg):
    book = {}
    watch.observe(cfg, book, snap(price_usd=1.0), "DIP", SOL, now=T0)
    assert watch.sample(cfg, book, now=T0 + 3700, prices={}) == 1
    assert watch.read_settled(cfg)[0]["result"] == "no_price"


def test_watch_only_research_logs_the_buy_it_would_make_and_buys_nothing(cfg, monkeypatch):
    agent, _ = _agent_with_decision(cfg, monkeypatch, {
        "action": "BUY", "verdict": "BUY", "conviction": 7, "thesis": "story", "exit_plan": _plan(1.5),
        "narrative_trend": "rising", "narrative_strength": 8, "catalyst": "listing"})
    s = snap()
    watch.observe(cfg, agent.watch, s, "MIGRATED", SOL)
    agent.research(s, SOL)
    assert not agent.pf.positions and agent.pf.cash_usd == cfg.starting_cash_usd
    rec = next(iter(agent.watch.values()))
    assert rec["stage"] == "would_buy" and rec["would_buy"]["size_usd"] > 0
    assert rec["checklist"]["passed"] and rec["brain"]["action"] == "BUY" and rec["brain"]["catalyst"] == "listing"
    assert agent.recent_looks[-1]["outcome"] == "WATCH_BUY"


def test_a_plain_pause_still_never_buys(cfg, monkeypatch):
    cfg.watch_only, cfg.pause_new_trades = False, True
    agent, _ = _agent_with_decision(cfg, monkeypatch, {
        "action": "BUY", "verdict": "BUY", "conviction": 7, "thesis": "", "exit_plan": _plan(1.5)})
    agent.research(snap(), SOL)
    assert not agent.pf.positions


def test_rules_stay_frozen_during_the_watch_week(cfg, monkeypatch):
    from agent import main
    agent, _ = _agent_with_decision(cfg, monkeypatch, {"action": "PASS", "verdict": "PASS", "conviction": 3})
    called = []
    monkeypatch.setattr(main, "evolve", lambda *a: called.append(1))
    (cfg.memory_dir / "skip_evolve_at").write_text("0")
    agent.review_skips(now=T0)
    assert not called


def test_steering_turns_watch_mode_on_and_picks_models(cfg):
    cfg.watch_only = False
    cfg.model, cfg.head_model = "claude-opus-5-5", "claude-opus-5-5"  # what an old .env sets
    applied = apply_steering(cfg, {"pause_new_trades": True, "watch_only": True,
                                   "brain_model": "claude-haiku-5-5", "head_model": "claude-opus-5-5"})
    assert cfg.watch_only and cfg.model == "claude-haiku-5-5" and cfg.head_model == "claude-opus-5-5"
    assert applied["watch_only"] and applied["brain_model"] == "claude-haiku-5-5"
    apply_steering(cfg, {"brain_model": "gpt-9"})  # not allowed: back to the .env model
    assert cfg.model == "claude-opus-5-5" and not cfg.watch_only


def test_report_and_branch_carry_the_watch_log(cfg, monkeypatch, tmp_path):
    from agent.main import Agent
    agent = Agent(cfg)
    rec = watch.observe(cfg, agent.watch, snap(price_usd=1.0), "MIGRATED", SOL, now=T0)
    watch.sample(cfg, agent.watch, now=T0 + 7 * 3600, prices={rec["ca"]: 1.4})
    status, report = build_report(agent)
    assert status["watch_only"] and status["watch"]["settled"] == 1
    assert "WATCH-ONLY" in report and "Watch log:" in report
    dest = tmp_path / "sync"
    dest.mkdir()
    assert copy_observations(cfg, dest) and not copy_observations(cfg, dest)
    assert len((dest / "watch").glob("*.jsonl").__iter__().__next__().read_text().splitlines()) == 1


def test_daily_review_runs_once_a_day_on_the_head_model(cfg, monkeypatch):
    from agent.main import Agent
    agent = Agent(cfg)
    rec = watch.observe(cfg, agent.watch, snap(price_usd=1.0), "MIGRATED", SOL, now=T0)
    watch.sample(cfg, agent.watch, now=T0 + 7 * 3600, prices={rec["ca"]: 1.6})
    asked = []

    def ask(prompt, schema, effort, web, model=None):
        asked.append(model)
        return {"summary": "No edge yet.", "findings": [], "rule_ideas": [], "data_issues": []}

    agent.brain.use_claude = True
    monkeypatch.setattr(agent.brain, "has_budget", lambda: True)
    monkeypatch.setattr(agent.brain, "_ask", ask)
    morning = T0 - T0 % 86400 + 14 * 3600  # 14:00 UTC
    agent.daily_review(now=morning - 2 * 3600)  # before the hour: nothing
    assert not asked
    agent.daily_review(now=morning)
    agent.daily_review(now=morning + 3600)  # same day: once
    assert asked == ["claude-opus-5-5"]
    saved = [json.loads(x) for x in (cfg.memory_dir / "daily_reviews.jsonl").read_text().splitlines()]
    assert saved[0]["summary"] == "No edge yet." and saved[0]["model"] == "claude-opus-5-5"


def test_digest_counts_after_costs(cfg):
    book = {}
    for i, x in enumerate((1.6, 0.7, 1.0)):
        s = snap(price_usd=1.0)
        s["address"] = f"coin{i}"
        rec = watch.observe(cfg, book, s, "MIGRATED", SOL, now=T0)
        watch.sample(cfg, book, now=T0 + 600, prices={rec["ca"]: x})
    watch.sample(cfg, book, now=T0 + 7 * 3600, prices={f"coin{i}": 1.0 for i in range(3)})
    d = watch.digest(cfg, book, hours=24, now=T0 + 7 * 3600)
    g = d["all"]
    assert d["settled"] == 3 and g["ran_pct"] == pytest.approx(33.3) and g["dumped_pct"] == pytest.approx(33.3)
    # (+50 - 20 + 0)/3 = +10% before costs; costs come off.
    assert g["avg_net_pct"] == pytest.approx(10 - g["avg_cost_pct"], abs=0.1)


# --- Graduation feed (owner, Nov 3: "ideally should be as the migrate/graduate") ------

FEEDS = (("pump.fun", "solana", "solana", "pump", ("pumpswap",)),
         ("bonk.fun", "solana", "solana", "bonk", ("raydium",)),
         ("four.meme", "bsc", "bsc", "4444", ("pancakeswap",)))
BONDING = ("launch", "pump-fun")


def _pool(mint, dex, ago_min, network="solana"):
    import time as _time
    created = _time.strftime("%Y-%m-%dT%H:%M:%SZ", _time.gmtime(_time.time() - ago_min * 60))
    return {"attributes": {"address": f"pool-{mint}", "pool_created_at": created},
            "relationships": {"dex": {"data": {"id": dex}}, "base_token": {"data": {"id": f"{network}_{mint}"}}}}


def test_graduation_feed_matches_each_launchpad_on_its_own_chain(monkeypatch):
    from agent import data
    pools = {
        "solana": [_pool("Aaapump", "pumpswap", 2), _pool("Bbbpump", "raydium", 2), _pool("Ccc111", "pumpswap", 2),
                   _pool("Dddpump", "pumpswap", 45), _pool("Eeebonk", "raydium-launchlab", 1),
                   _pool("Fffbonk", "raydium-cpmm", 3)],
        "bsc": [_pool("0xABC4444", "pancakeswap_v2", 4, "bsc"), _pool("0xABC1234", "pancakeswap_v2", 4, "bsc")],
    }

    def get(url, params=None, retries=3):
        net = url.split("/networks/")[1].split("/")[0]
        return {"data": pools[net] if params["page"] == 1 else []}

    monkeypatch.setattr(data, "_get", get)
    got = data.new_migrations(FEEDS, 20, bonding_words=BONDING)
    assert [(m["mint"], m["launchpad"], m["chain"]) for m in got["migrations"]] == [
        ("Aaapump", "pump.fun", "solana"), ("Fffbonk", "bonk.fun", "solana"), ("0xABC4444", "four.meme", "bsc")]
    assert got["answered"] == {"solana": True, "bsc": True}
    assert got["dex_seen"]["solana"]["pumpswap"] == 3 and got["dex_seen"]["bsc"] == {"pancakeswap_v2": 2}
    monkeypatch.setattr(data, "_get", lambda *a, **k: None)
    got = data.new_migrations(FEEDS)
    assert got["answered"] == {"solana": False, "bsc": False} and not got["migrations"]  # no answer, not "none"


def _migs(*rows):
    import time as _time
    return lambda *a, **k: {
        "migrations": [{"mint": m, "pool": f"P{m}", "dex": d, "chain": c, "network": c, "launchpad": pad,
                        "created_at": _time.time() - 180} for m, d, c, pad in rows],
        "answered": {"solana": True, "bsc": True}, "dex_seen": {"solana": {"pumpswap": 4}}}


def test_a_coin_is_logged_at_graduation_even_when_it_fails_the_filters(cfg, monkeypatch):
    from agent import data
    from agent.bridge import build_report
    from agent.main import Agent
    from test_agent import _scan_with

    agent = Agent(cfg)
    fresh = snap(address="Grad1pump", symbol="GRAD", mcap_usd=45_000, vol_5m=900, age_hours=0.05)
    monkeypatch.setattr(data, "new_migrations", _migs(("Grad1pump", "pumpswap", "solana", "pump.fun")))
    _scan_with(agent, monkeypatch, {"Grad1pump": fresh}, {"action": "PASS", "verdict": "PASS", "conviction": 3})
    rec = next(iter(agent.watch.values()))
    assert rec["setup"] == "AT_MIGRATION" and rec["chain"] == "solana" and rec["features"]["mcap_usd"] == 45_000
    assert 2.5 <= rec["migration"]["minutes_since"] <= 3.5 and rec["migration"]["launchpad"] == "pump.fun"
    assert rec["migration"]["holders"]["top10_pct_ex_pool"] is not None
    assert agent.migration_feed["ok"] and agent.migration_feed["logged"] == 1
    status, text = build_report(agent)
    assert status["watch"]["at_migration"] == 1 and "1 coins logged at migration (pump.fun 1)" in text
    assert "solana answered, bsc answered" in text and "solana pools by venue: pumpswap 4" in text


def test_a_bsc_graduation_is_logged_and_followed_on_its_own_chain(cfg, monkeypatch):
    from agent import data
    from agent.main import Agent
    from test_agent import _scan_with

    agent = Agent(cfg)
    asked = []
    bsc = {"0xabc4444": snap(address="0xABC4444", symbol="FOUR", dex="pancakeswap", mcap_usd=30_000, priceUsd="0.0012")}
    monkeypatch.setattr(data, "new_migrations", _migs(("0xabc4444", "pancakeswap_v2", "bsc", "four.meme")))
    monkeypatch.setattr(data, "sol_price_usd", lambda: SOL)
    monkeypatch.setattr(data, "discover_solana_tokens", lambda: [])
    monkeypatch.setattr(data, "pair_snapshot", lambda pair: dict(pair))
    monkeypatch.setattr(data, "rugcheck_report", lambda a: pytest.fail("RugCheck is Solana's"))
    monkeypatch.setattr(data, "get_pairs", lambda tokens, chain="solana": asked.append(chain) or (
        {t: bsc[t] for t in tokens if t in bsc} if chain == "bsc" else {}))
    agent.scan()
    rec = next(iter(agent.watch.values()))
    assert "bsc" in asked and rec["chain"] == "bsc" and rec["setup"] == "AT_MIGRATION"
    assert rec["migration"]["launchpad"] == "four.meme" and rec["migration"]["holders"] is None  # RugCheck is Solana's
    assert rec["ca"] == "0xabc4444" and watch.cost_pct(cfg, rec) is None
    asked.clear()
    watch.sample(cfg, agent.watch, now=rec["at"] + 600)
    assert asked == ["bsc"] and rec["samples"] == 1


def test_steering_can_replace_the_launchpad_list(cfg):
    from agent.bridge import apply_steering
    default = cfg.migration_feeds
    apply_steering(cfg, {"migration_feeds": [{"name": "zora", "network": "base", "ending": "", "dexes": ["uniswap"]},
                                             {"name": "x", "network": "eth"}]})
    assert cfg.migration_feeds == default  # an empty ending would match everything: ignored, and a bad row too
    applied = apply_steering(cfg, {"migration_feeds": [
        {"name": "four.meme", "network": "bsc", "ending": "4444", "dexes": ["pancake"]}]})
    assert applied["migration_feeds"] == ["four.meme"] and cfg.migration_feeds == (("four.meme", "bsc", "bsc", "4444", ("pancake",)),)
    apply_steering(cfg, {})
    assert cfg.migration_feeds == default


def test_graduation_feed_is_off_outside_watch_mode(cfg, monkeypatch):
    from agent import data
    from agent.main import Agent
    from test_agent import _scan_with

    cfg.watch_only = False
    agent = Agent(cfg)
    called = []
    monkeypatch.setattr(data, "new_migrations", lambda *a, **k: called.append(1) or [])
    _scan_with(agent, monkeypatch, {"X1": snap(address="X1")}, {"action": "PASS", "verdict": "PASS", "conviction": 3})
    assert not called and not agent.watch


def test_digest_splits_graduation_logs_by_holder_concentration(cfg):
    book = {}
    for i, (top10, x) in enumerate(((12.0, 1.6), (48.0, 0.7))):
        s = snap(price_usd=1.0)
        s["address"] = f"grad{i}"
        rec = watch.observe(cfg, book, s, "AT_MIGRATION", SOL, now=T0)
        rec["migration"] = {"launchpad": "pump.fun", "minutes_since": 2.0, "holders": {"top10_pct_ex_pool": top10}}
        watch.sample(cfg, book, now=T0 + 600, prices={rec["ca"]: x})
    watch.sample(cfg, book, now=T0 + 7 * 3600, prices={f"grad{i}": 1.0 for i in range(2)})
    d = watch.digest(cfg, book, hours=24, now=T0 + 7 * 3600)
    assert d["at_migration"]["n"] == 2
    assert d["at_migration_by_holders"]["top10 under 20%"]["ran_pct"] == 100.0
    assert d["at_migration_by_holders"]["top10 over 35%"]["dumped_pct"] == 100.0
    assert d["at_migration_by_launchpad"]["pump.fun"]["n"] == 2


def test_off_solana_coins_count_in_gross_but_not_after_costs(cfg):
    book = {}
    for i, (chain, x) in enumerate((("solana", 1.6), ("bsc", 0.7))):
        s = snap(price_usd=1.0)
        s["address"] = f"c{i}"
        watch.observe(cfg, book, s, "AT_MIGRATION", SOL, now=T0, chain=chain)
        watch.sample(cfg, book, now=T0 + 600, prices={f"c{i}": x})
    watch.sample(cfg, book, now=T0 + 7 * 3600, prices={"c0": 1.0, "c1": 1.0})
    g = watch.digest(cfg, book, hours=24, now=T0 + 7 * 3600)["all"]
    assert g["n"] == 2 and g["costed"] == 1 and g["avg_gross_pct"] == 15.0
    assert g["avg_net_pct"] == pytest.approx(50 - g["avg_cost_pct"], abs=0.1)
