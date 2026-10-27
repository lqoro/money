import time

import pytest

from agent.brain import Brain
from agent.checklist import holder_stats, run_checklist
from agent.config import Config
from agent.portfolio import Portfolio
from agent.risk import check_exit, sanitize_exit_plan

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


def test_rules_brain_respects_max_size(cfg):
    b = Brain(cfg)
    c = run_checklist(snap(), report(), [], cfg, SOL)
    d = b.decide(snap(), c, {}, max_size=7.0)
    assert d["action"] == "BUY" and d["size_usd"] <= 7.0


def test_state_round_trip(cfg):
    pf = Portfolio(cash_usd=100.0)
    pf.buy(cfg, snap(), 10.0, SOL, "MIGRATED", {"stop_loss_pct": 30}, "thesis")
    pf.save(cfg)
    again = Portfolio.load(cfg)
    assert again.cash_usd == pytest.approx(90.0)
    assert list(again.positions.values())[0].thesis == "thesis"
