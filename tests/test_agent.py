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
