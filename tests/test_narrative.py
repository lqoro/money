"""Narrative and catalyst gate for bottom buys (owner rule, Nov 2)."""
import pytest

from agent import narrative
from agent.bridge import apply_steering
from agent.config import EVOLVABLE, Config

from test_agent import SOL, _agent_with_decision, _plan, snap


@pytest.fixture
def cfg(tmp_path, monkeypatch):
    monkeypatch.setenv("BRAIN", "rules")
    c = Config()
    c.memory_dir = tmp_path
    return c


def coin(symbol, name=None, vol_5m=10_000, vol_1h=120_000, **kw):
    return snap(address=f"{symbol}-{name}-mint", symbol=symbol, name=name or symbol,
                vol_5m=vol_5m, vol_1h=vol_1h, **kw)


def buy(trend="rising", strength=8, catalyst="Robinhood announced tokenized stocks on Solana this morning (CoinDesk)"):
    return {"action": "BUY", "narrative_trend": trend, "narrative_strength": strength, "catalyst": catalyst}


def dip(theme_pace=1.3, **kw):
    s = snap(drawdown_pct=45, **kw)
    s["theme"] = {"words": ["turtle"], "copies": 3, "pace": theme_pace, "leader": "TURTLE", "this_is_leader": True}
    return s


# --- Measuring the theme across its copies ---------------------------------------

def test_theme_sums_volume_across_copies_by_shared_word_and_ticker():
    me = coin("ANAKIN", "Anakin Coin", vol_5m=10_000, vol_1h=150_000)
    others = [
        coin("ANAKIN", "Anakin Skywalker", vol_5m=500, vol_1h=40_000),  # same ticker
        coin("SKY", "Anakin Skywalker Fan", vol_5m=300, vol_1h=10_000),  # shares "anakin"
        coin("MANDO", "Mandalorian", vol_5m=8_000, vol_1h=30_000),  # another theme
    ]
    t = narrative.theme_flow(me, others)
    assert t["copies"] == 3 and t["vol_5m"] == 10_800 and t["vol_1h"] == 200_000
    assert t["pace"] == pytest.approx(10_800 / (200_000 / 12), abs=0.01)  # 0.65x: the theme is cooling
    assert t["leader"] == "ANAKIN" and t["this_is_leader"]


def test_generic_words_dont_make_a_theme():
    me = coin("FLOAT", "Float Coin")
    t = narrative.theme_flow(me, [coin("BONK", "Bonk Coin"), coin("WIF", "The Official Wif")])
    assert t["copies"] == 1


def test_counts_each_coin_once():
    me = coin("CAT", "Cat Bot")
    twin = coin("CAT", "Cat Bot")  # same address as me
    assert narrative.theme_flow(me, [twin, twin])["copies"] == 1


# --- Which buys the gate covers -------------------------------------------------

@pytest.mark.parametrize("setup,drawdown,covered", [
    ("DIP", 45, True), ("MIGRATED", 34, True), ("MIGRATED", 20, True),
    ("MIGRATED", 13, False), ("FINAL_STRETCH", 30, False),
])
def test_bottom_buys_are_dips_and_pullbacks(cfg, setup, drawdown, covered):
    assert narrative.is_bottom_buy(setup, snap(drawdown_pct=drawdown), cfg) is covered


def test_a_buy_near_the_high_is_not_gated(cfg):
    assert narrative.gate(buy(trend="none", strength=1, catalyst="none"), "MIGRATED", snap(drawdown_pct=3), cfg) is None


def test_a_pass_stays_a_pass(cfg):
    assert narrative.gate({"action": "PASS"}, "DIP", dip(), cfg) is None


# --- The three checks -----------------------------------------------------------

def test_rising_strong_narrative_with_a_catalyst_and_a_live_theme_passes(cfg):
    assert narrative.gate(buy(), "DIP", dip(), cfg) is None


@pytest.mark.parametrize("trend,strength", [("holding", 8), ("fading", 9), ("none", 0), ("rising", 6)])
def test_a_narrative_that_isnt_rising_and_strong_is_blocked(cfg, trend, strength):
    reason = narrative.gate(buy(trend=trend, strength=strength), "DIP", dip(), cfg)
    assert reason and "narrative gate" in reason and "rising" in reason


@pytest.mark.parametrize("catalyst", ["none", "", "None found", "N/A", "momentum", "buyers stepping in",
                                      "higher low", "hype"])
def test_no_catalyst_or_a_chart_reason_is_blocked(cfg, catalyst):
    reason = narrative.gate(buy(catalyst=catalyst), "DIP", dip(), cfg)
    assert reason and "catalyst" in reason


def test_a_cooling_theme_is_blocked_even_when_the_brain_likes_it(cfg):
    reason = narrative.gate(buy(), "MIGRATED", dip(theme_pace=0.6), cfg)
    assert reason and "theme is cooling" in reason and "0.60x" in reason


def test_no_theme_data_leaves_it_to_the_brain(cfg):
    s = snap(drawdown_pct=45)  # theme not measured (e.g. the scan cache is empty)
    assert narrative.gate(buy(), "DIP", s, cfg) is None


# --- Trencher's own losing dips, as its brain read them before buying ------------

@pytest.mark.parametrize("name,decision,theme_pace", [
    # Nov 2: its meta read didn't mention Star Wars; flow had moved to young coins.
    ("ANAKIN #1", buy(trend="holding", strength=6, catalyst="none"), 0.8),
    # Nov 2: "Star Wars is holding"; the thesis was a range breakout, no outside driver.
    ("ANAKIN #2", buy(trend="holding", strength=7, catalyst="pushing through the range high"), 0.9),
    # Nov 1: its own meta read said AAPLCAT was cooling at ~0.5x pace.
    ("AAPLCAT", buy(trend="fading", strength=5, catalyst="none"), 0.5),
    # Nov 1: "AI names are split".
    ("SIS", buy(trend="holding", strength=6, catalyst="higher low"), 1.0),
])
def test_past_losing_dips_would_have_been_blocked(cfg, name, decision, theme_pace):
    assert narrative.gate(decision, "DIP", dip(theme_pace=theme_pace), cfg), name


def test_the_tokenized_stock_buys_would_still_go_through(cfg):
    # Oct 29: tokenized stocks rising on the Robinhood headlines; FLOATER, CPU and FLOAT all ran past 1.6x.
    decision = buy(trend="rising", strength=8,
                   catalyst="Robinhood Chain and tokenized-stock headlines today are pulling money into the theme")
    assert narrative.gate(decision, "MIGRATED", dip(theme_pace=1.4), cfg) is None


# --- The owner's setting, not Trencher's -----------------------------------------

def test_only_the_owner_can_change_the_gate(cfg):
    for name in ("narrative_min_strength", "theme_min_pace", "pullback_min_drawdown_pct"):
        assert name not in EVOLVABLE
    apply_steering(cfg, {"settings": {"narrative_min_strength": 0}})
    assert narrative.gate(buy(trend="fading", strength=1, catalyst="none"), "DIP", dip(), cfg) is None
    apply_steering(cfg, {"settings": {}})
    assert cfg.narrative_min_strength == 7


def test_theme_check_can_be_turned_off_alone(cfg):
    apply_steering(cfg, {"settings": {"theme_min_pace": 0}})
    assert narrative.gate(buy(), "DIP", dip(theme_pace=0.2), cfg) is None


# --- Wired into research ---------------------------------------------------------

def test_research_turns_a_gated_buy_into_a_pass(cfg, monkeypatch):
    agent, _ = _agent_with_decision(cfg, monkeypatch, {
        "action": "BUY", "verdict": "BUY the dip", "conviction": 7, "thesis": "", "exit_plan": _plan(1.5),
        "narrative_trend": "holding", "narrative_strength": 6, "catalyst": "none"})
    monkeypatch.setattr(agent, "fresh_snapshot", lambda addr: snap(drawdown_pct=30))
    agent.research(snap(drawdown_pct=30), SOL)
    assert not agent.pf.positions
    look = agent.recent_looks[-1]
    assert look["outcome"] == "PASS" and "narrative gate (owner rule)" in look["reason"]
    from agent import skips
    assert skips.gate_for(look["reason"]) == "narrative gate (owner rule)"


def test_research_still_buys_a_qualifying_dip(cfg, monkeypatch):
    agent, _ = _agent_with_decision(cfg, monkeypatch, {
        "action": "BUY", "verdict": "BUY", "conviction": 7, "thesis": "", "exit_plan": _plan(1.5), **buy()})
    monkeypatch.setattr(agent, "fresh_snapshot", lambda addr: snap(drawdown_pct=30))
    agent.research(snap(drawdown_pct=30), SOL)
    assert agent.pf.positions


def test_the_brain_is_told_the_rule_and_the_theme_numbers(cfg):
    from agent.brain import DECISION_SCHEMA, Brain
    text = Brain(cfg)._narrative_rule(dip(theme_pace=0.7))
    assert "catalyst" in text and "rising" in text and "0.7x" in text
    for field in ("narrative_trend", "narrative_strength", "catalyst"):
        assert field in DECISION_SCHEMA["required"]
    cfg.narrative_min_strength = 0
    assert Brain(cfg)._narrative_rule(dip()) == ""
