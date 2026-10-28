import time

import pytest

from agent.brain import Brain
from agent.checklist import holder_stats, run_checklist
from agent.config import Config
from agent.portfolio import Portfolio
from agent.risk import check_exit, sanitize_exit_plan
from agent.sizing import open_risk_usd, position_size

SOL = 100.0


@pytest.fixture
def cfg(tmp_path, monkeypatch):
    monkeypatch.setenv("BRAIN", "rules")
    c = Config()
    c.memory_dir = tmp_path
    return c


def snap(**kw):
    s = {
        "address": "TokenMint1111", "name": "Turtle", "symbol": "TURTLE", "pair_address": "Pool111",
        "dex": "pumpswap", "url": "https://dexscreener.com/x", "price_usd": 0.001, "mcap_usd": 120_000,
        "liquidity_usd": 40_000, "vol_5m": 15_000, "vol_1h": 90_000, "vol_24h": 200_000,
        "buys_5m": 80, "sells_5m": 60, "buys_1h": 700, "sells_1h": 500, "change_5m": 3, "change_1h": 20,
        "change_24h": 50, "age_hours": 3.0, "boosts": 300, "has_paid_profile": True,
        "socials": ["twitter"], "social_links": [], "websites": [],
    }
    s.update(kw)
    return s


def report(**kw):
    r = {
        "mintAuthority": None, "freezeAuthority": None, "rugged": False, "risks": [],
        "creator": "Dev111", "creatorBalance": 0, "token": {"supply": 10**15},
        "tokenMeta": {"mutable": False}, "totalHolders": 2000, "graphInsidersDetected": 0,
        "knownAccounts": {"Pool111": {"type": "AMM"}},
        "markets": [{"pubkey": "Pool111", "liquidityA": "VaultA", "liquidityB": "VaultB", "lp": {"lpLockedPct": 100}}],
        "topHolders": [
            {"address": "VaultA", "owner": "Pool111", "pct": 30.0, "insider": False},
            *({"address": f"H{i}", "owner": f"O{i}", "pct": 1.0, "insider": False} for i in range(12)),
        ],
    }
    r.update(kw)
    return r


def test_pool_is_excluded_from_top10():
    h = holder_stats(report(), snap())
    assert h["top10_pct_ex_pool"] == 10.0


def test_clean_token_passes(cfg):
    c = run_checklist(snap(), report(), [], cfg, SOL)
    assert c.passed, c.fails
    assert c.setup == "MIGRATED"


@pytest.mark.parametrize("bad, expect", [
    ({"mintAuthority": "X"}, "Mint authority"),
    ({"freezeAuthority": "X"}, "Freeze authority"),
    ({"markets": [{"pubkey": "Pool111", "lp": {"lpLockedPct": 10}}]}, "LP only"),
    ({"topHolders": [{"address": f"W{i}", "owner": f"W{i}", "pct": 4.0} for i in range(10)]}, "Top 10"),
    ({"topHolders": [{"address": "D", "owner": "Dev111", "pct": 5.0}]}, "Dev holds"),
])
def test_hard_lines_fail(cfg, bad, expect):
    c = run_checklist(snap(), report(**bad), [], cfg, SOL)
    assert not c.passed
    assert any(expect in f for f in c.fails), c.fails


def test_final_stretch_classification(cfg):
    # Bond ≈ 410 SOL * $100 = $41k; $30k is ~73% of the way.
    c = run_checklist(snap(dex="pumpfun", mcap_usd=30_000), report(), [], cfg, SOL)
    assert c.setup == "FINAL_STRETCH"
    c = run_checklist(snap(dex="pumpfun", mcap_usd=8_000), report(), [], cfg, SOL)
    assert c.setup is None


def test_buy_and_sell_costs_money(cfg):
    pf = Portfolio(cash_usd=100.0)
    pos = pf.buy(cfg, snap(), 10.0, SOL, "MIGRATED", sanitize_exit_plan({}, cfg), "")
    assert pf.cash_usd == pytest.approx(90.0)
    assert pos.entry_price > 0.001  # paid slippage
    proceeds = pf.sell(cfg, pos, 1.0, 0.001, 40_000, SOL)
    assert proceeds < 10.0  # round trip at the same price loses fees + slippage
    assert pf.close(pos) < 0
    assert pf.trades_closed == 1 and pf.wins == 0


def test_rugged_sell_returns_zero(cfg):
    pf = Portfolio(cash_usd=100.0)
    pos = pf.buy(cfg, snap(), 10.0, SOL, "MIGRATED", {}, "")
    assert pf.sell(cfg, pos, 1.0, 0.0005, 100, SOL) == 0.0


def test_exit_rules(cfg):
    pf = Portfolio(cash_usd=100.0)
    pos = pf.buy(cfg, snap(), 10.0, SOL, "MIGRATED", sanitize_exit_plan({}, cfg), "")
    e = pos.entry_price
    assert check_exit(pos, snap(price_usd=e * 1.2), cfg) is None
    sig = check_exit(pos, snap(price_usd=e * 2.1), cfg)
    assert sig and "initials" in sig.reason and 0.4 < sig.fraction < 0.7
    assert "stop loss" in check_exit(pos, snap(price_usd=e * 0.6), cfg).reason
    assert "rug" in check_exit(pos, snap(liquidity_usd=1_000), cfg).reason
    later = time.time() + 60 * 60
    assert "time stop" in check_exit(pos, snap(price_usd=e), cfg, now=later).reason
    pos.initials_taken, pos.peak_price = True, e * 5
    assert "trailing" in check_exit(pos, snap(price_usd=e * 3), cfg).reason


def test_exit_plan_is_clamped(cfg):
    p = sanitize_exit_plan({"stop_loss_pct": 95, "take_initials_multiple": 50, "target_mcap_usd": 0}, cfg)
    assert p["stop_loss_pct"] <= cfg.stop_loss_pct * 1.5
    assert p["take_initials_multiple"] <= 5
    assert p["target_mcap_usd"] is None


def test_rules_brain_gives_conviction(cfg):
    b = Brain(cfg)
    c = run_checklist(snap(), report(), [], cfg, SOL)
    d = b.decide(snap(), c, {}, "")
    assert d["action"] == "BUY" and 5 <= d["conviction"] <= 8


def test_size_scales_with_conviction(cfg):
    pf = Portfolio(cash_usd=100.0)
    sizes = [position_size(c, 30, pf, cfg).size_usd for c in range(1, 11)]
    assert sizes[:4] == [0, 0, 0, 0]  # below 5/10: pass
    assert all(a < b for a, b in zip(sizes[4:], sizes[5:]))  # strictly more conviction, more size
    # Getting stopped out loses about the risk budget: 2.5% of $100 at conviction 7.
    s7 = position_size(7, 30, pf, cfg)
    assert s7.risk_usd == pytest.approx(2.5, abs=0.02)


def test_tighter_stop_means_bigger_size(cfg):
    pf = Portfolio(cash_usd=100.0)
    assert position_size(7, 15, pf, cfg).size_usd > position_size(7, 40, pf, cfg).size_usd


def test_size_caps(cfg):
    pf = Portfolio(cash_usd=100.0)
    s = position_size(10, 10, pf, cfg)  # $8 risk / 16% ≈ $50 → capped at 25% of equity
    assert s.size_usd == pytest.approx(25.0) and "max position" in s.note
    # Open risk eats the total risk budget.
    cfg.max_total_risk_pct = 18
    for _ in range(2):
        pf.buy(cfg, snap(), 20.0, SOL, "MIGRATED", {"stop_loss_pct": 30}, "")
    s = position_size(9, 30, pf, cfg)
    assert "total risk budget" in s.note
    assert open_risk_usd(pf, cfg) + s.risk_usd <= pf.equity() * cfg.max_total_risk_pct / 100 + 0.05


def test_state_round_trip(cfg):
    pf = Portfolio(cash_usd=100.0)
    pf.buy(cfg, snap(), 10.0, SOL, "MIGRATED", {"stop_loss_pct": 30}, "thesis")
    pf.save(cfg)
    again = Portfolio.load(cfg)
    assert again.cash_usd == pytest.approx(90.0)
    assert list(again.positions.values())[0].thesis == "thesis"


# --- Narrative trading: dips, stop reviews, re-entry, evolving strategy ------

def test_dip_setup(cfg):
    dip = snap(mcap_usd=100_000, peak_mcap_usd=220_000, drawdown_pct=55.0, vol_5m_vs_hour_avg=1.2,
               buy_ratio_5m=0.6, change_5m=4)
    c = run_checklist(dip, report(), [], cfg, SOL)
    assert c.setup == "DIP" and c.passed, c.fails
    assert any("Buyers stepping in" in x for x in c.plusses)


def test_dip_with_fading_attention_is_a_falling_knife(cfg):
    knife = snap(mcap_usd=100_000, peak_mcap_usd=220_000, drawdown_pct=55.0, vol_5m_vs_hour_avg=0.3)
    c = run_checklist(knife, report(), [], cfg, SOL)
    assert not c.passed and any("falling knife" in f for f in c.fails)


def test_dip_too_deep_is_not_a_dip(cfg):
    dead = snap(mcap_usd=40_000, peak_mcap_usd=400_000, drawdown_pct=90.0, age_hours=30)
    assert run_checklist(dead, report(), [], cfg, SOL).setup is None


def test_stop_is_a_review_once_then_final(cfg):
    pf = Portfolio(cash_usd=100.0)
    pos = pf.buy(cfg, snap(), 10.0, SOL, "MIGRATED", sanitize_exit_plan({}, cfg), "")
    e = pos.entry_price
    sig = check_exit(pos, snap(price_usd=e * 0.65), cfg)
    assert sig.review
    pos.stop_reviews = 1
    assert not check_exit(pos, snap(price_usd=e * 0.65), cfg).review
    pos.stop_reviews = 0
    hard = check_exit(pos, snap(price_usd=e * 0.35), cfg)
    assert "hard stop" in hard.reason and not hard.review


def test_hold_deadline(cfg):
    pf = Portfolio(cash_usd=100.0)
    pos = pf.buy(cfg, snap(), 10.0, SOL, "MIGRATED", sanitize_exit_plan({}, cfg), "")
    e = pos.entry_price
    pos.exit_plan.update({"_orig_stop": 30, "stop_loss_pct": 50, "hold_until": time.time() - 1})
    assert "no recovery" in check_exit(pos, snap(price_usd=e * 0.6), cfg).reason
    pos.exit_plan.update({"stop_loss_pct": 50, "hold_until": time.time() - 1})
    assert check_exit(pos, snap(price_usd=e * 0.9), cfg) is None
    assert pos.exit_plan["stop_loss_pct"] == 30  # recovered: normal stop again


def _agent(cfg, monkeypatch, holders_now_top10):
    from agent import main as m
    rep = report(topHolders=[{"address": f"H{i}", "owner": f"O{i}", "pct": holders_now_top10 / 10} for i in range(10)])
    monkeypatch.setattr(m.data, "rugcheck_report", lambda addr: rep)
    monkeypatch.setattr(m, "notify", lambda *a, **k: None)
    agent = m.Agent(cfg)
    pos = agent.pf.buy(cfg, snap(), 10.0, SOL, "MIGRATED", sanitize_exit_plan({}, cfg), "")
    pos.entry_holders = {"top10_pct_ex_pool": 20.0, "insider_pct": 0}
    return agent, pos


def test_bundle_exit_with_live_attention_holds(cfg, monkeypatch):
    agent, pos = _agent(cfg, monkeypatch, holders_now_top10=8.0)  # top 10 went 20% → 8%: bundle sold
    now = snap(price_usd=pos.entry_price * 0.65, vol_5m_vs_hour_avg=1.1, buy_ratio_5m=0.6)
    agent.review_stop(pos, now, "stop loss -30% hit", SOL)
    assert pos.id in agent.pf.positions
    assert pos.exit_plan["stop_loss_pct"] == cfg.hard_stop_pct - 10
    assert pos.exit_plan["hold_until"] > time.time()


def test_no_shakeout_sells_and_watches_for_reentry(cfg, monkeypatch):
    agent, pos = _agent(cfg, monkeypatch, holders_now_top10=20.0)  # holders unchanged: no bundle exit
    now = snap(price_usd=pos.entry_price * 0.65, vol_5m_vs_hour_avg=1.1, buy_ratio_5m=0.6)
    agent.review_stop(pos, now, "stop loss -30% hit", SOL)
    assert pos.id not in agent.pf.positions
    assert pos.address in agent.watchlist


def test_evolve_applies_bounded_changes(cfg, monkeypatch):
    import json as _json
    from agent import evolve as ev, journal
    journal.log_trade(cfg, {"event": "CLOSE", "symbol": "X", "setup": "DIP", "pnl_usd": -2})
    b = Brain(cfg)
    monkeypatch.setattr(b, "evolve", lambda trades: {
        "rules_markdown": "- wider stops on DIP",
        "param_changes": [{"param": "stop_loss_pct", "value": 40, "reason": "bundle exits"},
                          {"param": "dip_max_drawdown_pct", "value": 99, "reason": "too greedy"},
                          {"param": "max_top10_pct", "value": 90, "reason": "not evolvable"}],
    })
    summary = ev.evolve(cfg, b)
    assert cfg.stop_loss_pct == 40
    assert cfg.dip_max_drawdown_pct == 80  # clamped to its bound
    assert cfg.max_top10_pct == 25  # hard lines can't evolve
    assert "stop_loss_pct" in _json.loads((cfg.memory_dir / "strategy.json").read_text())
    assert "wider stops" in summary
    monkeypatch.setenv("STOP_LOSS_PCT", "25")
    cfg.stop_loss_pct = 25
    cfg.apply_strategy()
    assert cfg.stop_loss_pct == 25  # an explicit env setting beats the learned one


def test_no_cap_on_number_of_positions(cfg):
    pf = Portfolio(cash_usd=100.0)
    for _ in range(8):
        pf.buy(cfg, snap(), 2.5, SOL, "MIGRATED", {"stop_loss_pct": 30}, "")
    assert pf.can_open(cfg) == (True, "")
    cfg.max_open_positions = 8
    assert pf.can_open(cfg) == (False, "max open positions")


# --- Web crawler ---------------------------------------------------------------

def test_site_showing_another_ca_is_flagged(cfg):
    web = {"websites": [{"host": "spx6900.com", "reachable": True, "shows_this_ca": False,
                         "other_addresses": ["J3NKxxXZcnNiMjKw9hYb2K4LUxgwB6t1FtPtQVsv3KFr"], "tech_claims": []}],
           "github": []}
    c = run_checklist(snap(web=web), report(), [], cfg, SOL)
    assert any("different contract address" in w for w in c.warns)


def test_tech_claims_without_github_is_a_larp_warning(cfg):
    web = {"websites": [{"host": "aiagent.xyz", "reachable": True, "shows_this_ca": True, "other_addresses": [],
                         "tech_claims": ["ai", "agent"]}], "github": [{"repo": "x/y", "days_since_push": 200}]}
    c = run_checklist(snap(web=web), report(), [], cfg, SOL)
    assert any("LARP" in w for w in c.warns)
    web["github"] = [{"repo": "x/y", "days_since_push": 2}]
    c = run_checklist(snap(web=web), report(), [], cfg, SOL)
    assert any("real recent work" in p for p in c.plusses)


def test_crawler_refuses_private_addresses():
    from agent.site import crawl_site, is_public_url
    assert not is_public_url("http://127.0.0.1:8080/")
    assert not is_public_url("http://169.254.169.254/latest/meta-data")
    assert not is_public_url("file:///etc/passwd")
    assert crawl_site("http://localhost/", "X")["skipped"]


def test_token_buzz_and_radar_terms():
    from agent import radar
    rad = {"_texts": ["GTA trailer drops, $GTA memes everywhere", "gta trailer hype", "kimchi coin"],
           "top_narratives": [{"term": "gta trailer", "score": 5}, {"term": "kimchi", "score": 3}],
           "trending_coins": ["GTA"], "called_cas": {"TokenMint1111": {"count": 2, "sources": ["t.me/alpha"]}}}
    b = radar.token_buzz(snap(symbol="GTA", name="GTA trailer"), rad)
    assert b["ticker_mentions"] == 2 and b["on_coingecko_trending"]
    assert "gta trailer" in b["fits_hot_narratives"]
    assert b["ca_call_count"] == 2
    assert "memecoin" not in radar._terms("Solana memecoin pump fun launch")


def test_api_serves_status_and_meta(cfg, monkeypatch):
    import json as _json
    import urllib.request
    from agent import api, radar
    cfg.api_port, cfg.api_token = 18765, "secret"
    radar.save_radar(cfg, {"updated_at": time.time(), "top_narratives": [{"term": "kimchi", "score": 3}]})
    server = api.start_api(cfg, lambda: {"equity_usd": 100}, lambda a: None)
    try:
        def get(path, token="secret"):
            req = urllib.request.Request(f"http://127.0.0.1:18765{path}", headers={"Authorization": f"Bearer {token}"})
            try:
                with urllib.request.urlopen(req) as r:
                    return r.status, _json.loads(r.read())
            except urllib.error.HTTPError as e:
                return e.code, None
        assert get("/status") == (200, {"equity_usd": 100})
        assert get("/meta")[1]["top_narratives"] == ["kimchi"]
        assert get("/status", token="wrong")[0] == 401
        assert get("/token/abc")[0] == 404
    finally:
        server.shutdown()


# --- Claude plan brain (Claude Code CLI) -------------------------------------

FAKE_CLI = r'''#!/usr/bin/env python3
import json, os, sys
args = sys.argv[1:]
prompt = sys.stdin.read()
with open(os.environ["FAKE_CLI_LOG"], "a") as f:
    f.write(json.dumps({"args": args, "prompt": prompt,
                        "api_key_leaked": "ANTHROPIC_API_KEY" in os.environ}) + "\n")
mode = os.environ.get("FAKE_CLI_MODE", "ok")
if mode == "limit":
    print(json.dumps({"type": "result", "is_error": True, "result": "Claude AI usage limit reached|4102444800"}))
    sys.exit(1)
if mode == "auth":
    print(json.dumps({"type": "result", "is_error": True, "result": "Not logged in · Please run /login"}))
    sys.exit(1)
schema = json.loads(args[args.index("--json-schema") + 1])
answer = {"summary": "Online."} if "summary" in schema["properties"] else {"lesson": "Size down."}
print(json.dumps({"type": "result", "is_error": False, "result": json.dumps(answer), "structured_output": answer}))
'''


@pytest.fixture
def plan_brain(cfg, tmp_path, monkeypatch):
    import json as _json
    cli = tmp_path / "fake-claude"
    cli.write_text(FAKE_CLI)
    cli.chmod(0o755)
    log_path = tmp_path / "cli.log"
    monkeypatch.setenv("BRAIN", "subscription")
    monkeypatch.setenv("ANTHROPIC_API_KEY", "sk-should-not-be-used")
    monkeypatch.setenv("FAKE_CLI_LOG", str(log_path))
    cfg.claude_cli = str(cli)
    b = Brain(cfg)
    b.calls_log = lambda: [_json.loads(x) for x in log_path.read_text().splitlines()]
    return b


def test_auto_prefers_the_claude_plan_over_the_api(monkeypatch, tmp_path):
    from agent.brain import resolve_backend
    cli = tmp_path / "claude"
    cli.write_text("#!/bin/sh\n")
    cli.chmod(0o755)
    monkeypatch.setenv("ANTHROPIC_API_KEY", "sk-x")
    assert resolve_backend("auto", str(cli)) == "subscription"
    assert resolve_backend("auto", str(tmp_path / "missing")) == "api"
    monkeypatch.delenv("ANTHROPIC_API_KEY")
    assert resolve_backend("auto", str(tmp_path / "missing")) is None
    assert resolve_backend("api", str(cli)) == "api"
    assert resolve_backend("rules", str(cli)) is None


def test_plan_brain_calls_cli_with_schema_and_only_web_search(plan_brain):
    out = plan_brain._ask("What's the meta?", {"type": "object", "properties": {"summary": {"type": "string"}},
                                                "required": ["summary"]}, "low", web=True)
    assert out == {"summary": "Online."}
    call = plan_brain.calls_log()[-1]
    args = call["args"]
    assert args[:2] == ["-p", "--output-format"] and "--json-schema" in args
    assert args[args.index("--tools") + 1] == "WebSearch"
    assert "--system-prompt-file" in args and "What's the meta?" in call["prompt"]
    # The API key is stripped so the CLI bills the plan, not the API.
    assert call["api_key_leaked"] is False
    plan_brain._ask("x", {"type": "object", "properties": {"summary": {"type": "string"}}}, "low", web=False)
    args = plan_brain.calls_log()[-1]["args"]
    assert args[args.index("--tools") + 1] == ""


def test_plan_usage_limit_pauses_the_brain(plan_brain, monkeypatch):
    monkeypatch.setenv("FAKE_CLI_MODE", "limit")
    assert plan_brain._ask("x", {"type": "object", "properties": {"summary": {"type": "string"}}}, "low", False) is None
    assert plan_brain.paused_until > time.time() and not plan_brain.has_budget()


def test_plan_not_logged_in_fails_safe(plan_brain, monkeypatch):
    monkeypatch.setenv("FAKE_CLI_MODE", "auth")
    assert plan_brain._ask("x", {"type": "object", "properties": {"summary": {"type": "string"}}}, "low", False) is None
    assert plan_brain.has_budget()  # not a usage limit: no pause
    assert not plan_brain.use_claude  # falls back to the rules-only brain


def test_zero_hourly_cap_means_unlimited(plan_brain):
    plan_brain.cfg.max_brain_calls_per_hour = 0
    plan_brain.calls.extend([time.time()] * 500)
    assert plan_brain.has_budget()
    plan_brain.cfg.max_brain_calls_per_hour = 30
    assert not plan_brain.has_budget()


def test_call_pace_is_evolvable_and_usage_is_logged(plan_brain, monkeypatch):
    from agent.config import EVOLVABLE
    assert EVOLVABLE["max_brain_calls_per_hour"][0] == 0
    plan_brain._ask("x", {"type": "object", "properties": {"summary": {"type": "string"}}}, "low", False)
    monkeypatch.setenv("FAKE_CLI_MODE", "limit")
    plan_brain._ask("x", {"type": "object", "properties": {"summary": {"type": "string"}}}, "low", False)
    plan_brain.note("skipped")
    u = plan_brain.usage_view()
    assert u["brain_calls"] == 2 and u["plan_limit_hits"] == 1 and u["candidates_skipped_no_brain"] == 1


def test_default_has_no_call_cap():
    from agent.config import Config
    assert Config().max_brain_calls_per_hour == 0


# --- Claude Duet bridge --------------------------------------------------------

def _git(*args, cwd=None):
    import subprocess
    subprocess.run(["git", "-c", "user.name=t", "-c", "user.email=t@t", "-c", "init.defaultBranch=main", *args],
                   cwd=cwd, check=True, capture_output=True)


@pytest.fixture
def live_repo(tmp_path):
    """A bare 'GitHub' repo with a trencher-live branch, and a checkout of it."""
    import json as _json
    origin, seed, live = tmp_path / "origin.git", tmp_path / "seed", tmp_path / "live"
    _git("init", "-q", "--bare", str(origin))
    _git("init", "-q", str(seed))
    _git("checkout", "-q", "--orphan", "trencher-live", cwd=seed)

    def steer(payload):
        (seed / "steer.json").write_text(_json.dumps(payload))
        _git("add", "steer.json", cwd=seed)
        _git("commit", "-q", "-m", "steer", cwd=seed)
        _git("pull", "-q", "--rebase", str(origin), "trencher-live", cwd=seed) if (origin / "refs/heads/trencher-live").exists() else None
        _git("push", "-q", str(origin), "HEAD:trencher-live", cwd=seed)

    steer({"pause_new_trades": False})
    _git("clone", "-q", "-b", "trencher-live", str(origin), str(live))
    return origin, live, steer


def test_bridge_publishes_status_and_applies_steering(cfg, live_repo):
    import json as _json
    import subprocess
    from agent.main import Agent
    origin, live, steer = live_repo
    steer({"pause_new_trades": True, "settings": {"stop_loss_pct": 99, "max_top10_pct": 90, "bogus": 1},
           "owner_note": "x" * 1000})
    cfg.duet_sync_dir = str(live)
    agent = Agent(cfg)
    agent.bridge.sync()

    assert cfg.pause_new_trades is True
    assert cfg.stop_loss_pct == 50  # clamped to its evolvable bound
    assert cfg.max_top10_pct == 25  # hard lines can't be steered
    assert len(cfg.owner_note) == 600
    assert "note from your owner" in agent.brain._owner_note()
    pushed = subprocess.run(["git", "-C", str(origin), "show", "trencher-live:status.json"],
                            capture_output=True, text=True, check=True).stdout
    status = _json.loads(pushed)
    assert status["paused_new_trades"] is True and status["equity_usd"] == 100
    assert "PAUSED" in (live / "REPORT.md").read_text()

    # Dropping a setting from steer.json puts it back.
    steer({"pause_new_trades": False, "settings": {}})
    agent.bridge.sync()
    assert cfg.pause_new_trades is False and cfg.stop_loss_pct == 30 and cfg.owner_note == ""


def test_paused_agent_opens_nothing(cfg, monkeypatch):
    from agent import data
    from agent.main import Agent
    agent = Agent(cfg)
    cfg.pause_new_trades = True
    monkeypatch.setattr(data, "sol_price_usd", lambda: (_ for _ in ()).throw(AssertionError("scanned while paused")))
    agent.scan()


def test_auto_update_restarts_when_main_moves(cfg, tmp_path, monkeypatch):
    from agent import bridge as br
    from agent.main import Agent
    origin, here, other = tmp_path / "o.git", tmp_path / "here", tmp_path / "other"
    _git("init", "-q", "--bare", str(origin))
    _git("clone", "-q", str(origin), str(here))
    (here / "a").write_text("1")
    _git("add", "a", cwd=here)
    _git("commit", "-q", "-m", "one", cwd=here)
    _git("push", "-q", "origin", "HEAD:main", cwd=here)
    monkeypatch.setattr(br, "ROOT", here)
    cfg.auto_update = True
    agent = Agent(cfg)
    agent.bridge.check_update()
    assert not agent.bridge.restart_requested  # nothing new yet

    _git("clone", "-q", "-b", "main", str(origin), str(other))
    (other / "a").write_text("2")
    _git("commit", "-q", "-am", "two", cwd=other)
    _git("push", "-q", "origin", "HEAD:main", cwd=other)
    agent.bridge.check_update()
    assert agent.bridge.restart_requested and not agent.running


def test_auto_update_does_not_loop_when_the_launcher_could_not_update(cfg, monkeypatch):
    from agent.main import Agent
    monkeypatch.setenv("TRENCHER_UPDATE_FAILED", "1")
    cfg.auto_update = True
    agent = Agent(cfg)
    agent.bridge.check_update()
    assert not agent.bridge.restart_requested and agent.running


# --- Realistic paper costs (Axiom + pool + network) and contract addresses -----

def test_pool_fee_follows_the_venue(cfg):
    from agent.portfolio import venue_fee_pct
    assert venue_fee_pct(cfg, "pumpfun", 30_000, SOL) == 1.25  # bonding curve
    assert venue_fee_pct(cfg, "pumpswap", 10_000, SOL) == 1.25  # 100 SOL mcap
    assert venue_fee_pct(cfg, "pumpswap", 120_000, SOL) == 1.2  # 1,200 SOL
    assert venue_fee_pct(cfg, "pumpswap", 1_200_000, SOL) == 0.95  # 12,000 SOL
    assert venue_fee_pct(cfg, "pumpswap", 50_000_000, SOL) == 0.3  # floor
    assert venue_fee_pct(cfg, "raydium", 1_000_000, SOL) == 0.25


def test_buy_charges_axiom_pool_and_network_fees(cfg):
    pf = Portfolio(cash_usd=100.0)
    pos = pf.buy(cfg, snap(), 10.0, SOL, "MIGRATED", {}, "")  # PumpSwap at 1,200 SOL mcap: 1.2% pool fee
    assert pf.fees_by_kind["axiom"] == pytest.approx(0.10)
    assert pf.fees_by_kind["pool"] == pytest.approx(0.12)
    assert pf.fees_by_kind["network"] == pytest.approx(0.002005 * SOL)  # base + priority + Jito tip
    assert pf.fees_paid_usd == pytest.approx(pos.fees_usd) == pytest.approx(0.4205)
    spend = 10.0 - 0.4205
    assert pos.tokens * 0.001 == pytest.approx(spend - pos.slippage_usd)  # slippage costs value, not cash
    assert pos.slippage_usd > spend * cfg.base_slippage_pct / 100 * 0.9
    assert pos.cost_usd == 10.0 and pf.cash_usd == pytest.approx(90.0)


def test_round_trip_pays_fees_both_ways(cfg):
    pf = Portfolio(cash_usd=100.0)
    pos = pf.buy(cfg, snap(), 10.0, SOL, "MIGRATED", {}, "")
    proceeds = pf.sell(cfg, pos, 1.0, 0.001, 40_000, SOL, dex="pumpswap", mcap_usd=120_000)
    assert pf.fees_by_kind["network"] == pytest.approx(2 * 0.002005 * SOL)
    assert proceeds == pytest.approx(10.0 - pos.fees_usd - pos.slippage_usd, abs=1e-6)
    assert pf.close(pos) == pytest.approx(-(pos.fees_usd + pos.slippage_usd), abs=1e-6)


def test_sell_uses_the_pool_the_coin_trades_on_now(cfg):
    pf = Portfolio(cash_usd=100.0)
    pos = pf.buy(cfg, snap(dex="pumpfun", mcap_usd=30_000), 10.0, SOL, "FINAL_STRETCH", {}, "")
    assert pos.venue_fee_pct == 1.25
    pool_before = pf.fees_by_kind["pool"]
    pf.sell(cfg, pos, 1.0, 0.001, 40_000, SOL, dex="raydium", mcap_usd=500_000)
    assert pf.fees_by_kind["pool"] - pool_before < 0.03  # 0.25% of ~$9.5, not 1.25%


def test_old_state_without_fee_fields_still_loads(cfg):
    import json as _json
    pf = Portfolio(cash_usd=100.0)
    pf.buy(cfg, snap(), 10.0, SOL, "MIGRATED", {}, "")
    raw = _json.loads(_json.dumps(__import__("dataclasses").asdict(pf)))
    for key in ("fees_by_kind", "slippage_paid_usd"):
        raw.pop(key)
    for p in raw["positions"].values():
        for key in ("dex", "venue_fee_pct", "network_fee_usd", "fees_usd", "slippage_usd"):
            p.pop(key)
    (cfg.memory_dir / "state.json").write_text(_json.dumps(raw))
    loaded = Portfolio.load(cfg)
    pos = next(iter(loaded.positions.values()))
    assert loaded.sell(cfg, pos, 1.0, 0.001, 40_000, SOL, dex="pumpswap", mcap_usd=120_000) > 0


def test_network_fees_count_in_sizing(cfg):
    pf = Portfolio(cash_usd=100.0)
    no_fees = position_size(7, 30, pf, cfg)
    with_fees = position_size(7, 30, pf, cfg, sol_usd=SOL, venue_pct=1.2)
    assert with_fees.size_usd < no_fees.size_usd
    assert with_fees.risk_usd == pytest.approx(2.5, abs=0.02)  # still loses ~the risk budget at the stop
    # When network fees alone would eat the whole risk, the trade isn't worth taking.
    cfg.priority_fee_sol = 0.006
    s = position_size(5, 30, pf, cfg, sol_usd=SOL)
    assert s.size_usd == 0 and "network fees" in s.note


def test_trencher_cannot_evolve_its_own_fees(cfg):
    from agent import evolve as ev

    class FakeBrain:
        def evolve(self, closes):
            return {"rules_markdown": "", "param_changes": [{"param": "platform_fee_pct", "value": 0, "reason": "x"},
                                                             {"param": "bribe_sol", "value": 0, "reason": "x"}]}

    from agent import journal
    journal.log_trade(cfg, {"event": "CLOSE", "pnl_usd": -1})
    ev.evolve(cfg, FakeBrain())
    cfg.apply_strategy()
    assert cfg.platform_fee_pct == 1.0 and cfg.bribe_sol == 0.001


def test_duet_can_steer_fee_settings(cfg):
    from agent.bridge import apply_steering
    apply_steering(cfg, {"settings": {"bribe_sol": 0.01, "platform_fee_pct": 9}})
    assert cfg.bribe_sol == 0.01 and cfg.platform_fee_pct == 2  # clamped
    apply_steering(cfg, {"settings": {}})
    assert cfg.bribe_sol == 0.001 and cfg.platform_fee_pct == 1.0


def test_report_lists_contract_addresses(cfg):
    from agent import journal
    from agent.bridge import build_report
    from agent.main import Agent
    agent = Agent(cfg)
    pos = agent.pf.buy(cfg, snap(address="AZdhikmyj6ibsejv7EjML9SfNmuiMvwDrKXTEU2zpump", symbol="Something"),
                       5.0, SOL, "DIP", {}, "")
    journal.log_trade(cfg, {"event": "BUY", "id": pos.id, "token": pos.address, "symbol": pos.symbol,
                            "size_usd": 5.0, "fees_usd": pos.fees_usd})
    status, report = build_report(agent)
    assert status["open_positions"][0]["ca"] == pos.address
    assert status["recent_trades"][0]["ca"] == pos.address
    assert report.count(f"CA `{pos.address}`") == 2  # open position + recent trade
    assert "Fees paid: $" in report and "slippage" in report


# --- Live meta from its own scan, and why it passed ---------------------------

def _scan_with(agent, monkeypatch, pairs, decision):
    from agent import data
    monkeypatch.setattr(data, "sol_price_usd", lambda: SOL)
    monkeypatch.setattr(data, "discover_solana_tokens", lambda: list(pairs))
    monkeypatch.setattr(data, "get_pairs", lambda tokens: {t: pairs[t] for t in tokens if t in pairs})
    monkeypatch.setattr(data, "pair_snapshot", lambda pair: dict(pair))
    monkeypatch.setattr(data, "price_history", lambda s: None)
    monkeypatch.setattr(data, "rugcheck_report", lambda a: report())
    monkeypatch.setattr(data, "search_same_name", lambda sym: [])
    monkeypatch.setattr("agent.main.project_report", lambda s, c: {})
    monkeypatch.setattr(agent.brain, "decide", lambda *a, **k: decision)
    agent.scan()


def test_scan_keeps_movers_and_says_why_it_passed(cfg, monkeypatch):
    from agent.bridge import build_report
    from agent.main import Agent
    agent = Agent(cfg)
    pairs = {
        "HotCoin111": snap(address="HotCoin111", symbol="HOT", vol_1h=500_000),
        "DeadCoin111": snap(address="DeadCoin111", symbol="DEAD", vol_5m=10, vol_1h=900),
    }
    _scan_with(agent, monkeypatch, pairs, {"action": "PASS", "verdict": "PASS — buyers fading on the 5m",
                                           "conviction": 4, "exit_plan": {}})
    movers = agent.meta["scan_movers"]
    assert [m["symbol"] for m in movers] == ["HOT", "DEAD"]  # sorted by 1h volume, all coins not just candidates
    assert movers[0]["ca"] == "HotCoin111"
    assert agent.last_scan["pairs"] == 2 and agent.last_scan["passed_market_filters"] == 1
    look = agent.recent_looks[-1]
    assert look["symbol"] == "HOT" and look["outcome"] == "PASS" and "buyers fading" in look["reason"]

    status, rep = build_report(agent)
    assert status["recent_looks"][-1]["ca"] == "HotCoin111"
    assert "## Coins it looked at, and why it passed" in rep and "buyers fading" in rep
    assert "CA `HotCoin111`" in rep and "passed the market filters" in rep
    assert "## Moving most in its scan" in rep


def test_buy_that_sizes_under_the_minimum_says_so(cfg, monkeypatch):
    from agent.main import Agent
    agent = Agent(cfg)
    pairs = {"HotCoin111": snap(address="HotCoin111", symbol="HOT")}
    _scan_with(agent, monkeypatch, pairs, {"action": "BUY", "verdict": "BUY — tiny", "conviction": 5,
                                           "exit_plan": {"stop_loss_pct": 30}})
    look = agent.recent_looks[-1]
    assert look["outcome"] == "TOO_SMALL" and "minimum" in look["reason"]
    assert not agent.pf.positions


def test_scan_movers_survive_a_radar_refresh(cfg, monkeypatch):
    from agent import radar
    for fn in ("read_rss", "read_reddit", "read_telegram"):
        monkeypatch.setattr(radar, fn, lambda *a: [])
    monkeypatch.setattr(radar, "read_dexscreener_blurbs", lambda: [])
    monkeypatch.setattr(radar, "read_coingecko_trending", lambda: {})
    prev = {"scan_movers": [{"symbol": "HOT"}], "updated_at": time.time()}
    fresh = radar.build_radar(cfg, previous=prev)
    assert fresh["scan_movers"] == [{"symbol": "HOT"}]
    assert radar.public_view(fresh)["scan_movers"] == [{"symbol": "HOT"}]


def test_meta_summary_reads_the_scan_and_the_owner_note(plan_brain, monkeypatch):
    seen = {}
    monkeypatch.setattr(plan_brain, "_ask", lambda prompt, *a, **k: seen.setdefault("p", prompt) and {"summary": "ok"})
    plan_brain.cfg.owner_note = "trade what's moving"
    plan_brain.summarize_meta({"scan_movers": [{"symbol": "HOT"}]})
    assert "scan_movers" in seen["p"] and "trade what's moving" in seen["p"] and "HOT" in seen["p"]
