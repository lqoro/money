"""Break-even stop and sell-on-fading-volume exits."""

import time

import pytest

from agent.config import Config
from agent.portfolio import Portfolio, breakeven_price
from agent.risk import breakeven_stop, check_exit, sanitize_exit_plan

SOL = 100.0


@pytest.fixture
def cfg(tmp_path, monkeypatch):
    monkeypatch.setenv("BRAIN", "rules")
    c = Config()
    c.memory_dir = tmp_path
    return c


def snap(**kw):
    s = {"address": "TokenMint1111", "symbol": "FLOAT", "dex": "pumpswap", "price_usd": 0.001,
         "mcap_usd": 120_000, "liquidity_usd": 40_000, "vol_5m": 15_000, "vol_1h": 90_000}
    s.update(kw)
    return s


def opened(cfg, size=10.0, **kw):
    pf = Portfolio(cash_usd=100.0)
    pos = pf.buy(cfg, snap(**kw), size, SOL, "MIGRATED", sanitize_exit_plan({}, cfg), "")
    return pf, pos


def tick(pos, cfg, mult, now=None, **kw):
    """One monitor tick at `mult` x the entry fill."""
    price = pos.entry_price * mult
    pos.last_price, pos.peak_price = price, max(pos.peak_price, price)
    return check_exit(pos, snap(price_usd=price, **kw), cfg, now=now, sol_usd=SOL)


def test_breakeven_price_matches_a_real_sell(cfg):
    pf, pos = opened(cfg, 5.0)
    be = breakeven_price(cfg, pos, 40_000, pos.venue_fee_pct, pos.network_fee_usd)
    proceeds = pf.sell(cfg, pos, 1.0, be, 40_000, SOL, dex="pumpswap", mcap_usd=120_000)
    assert proceeds == pytest.approx(5.0, abs=1e-6)


def test_small_positions_need_more_to_break_even(cfg):
    """Network fees are flat, so a $3 position has to run further than a $10 one."""
    _, small = opened(cfg, 3.0)
    _, big = opened(cfg, 10.0)
    s = breakeven_stop(small, snap(), cfg, SOL) / small.entry_price
    b = breakeven_stop(big, snap(), cfg, SOL) / big.entry_price
    assert 1.1 < b < s < 1.35


def test_cheaper_pool_means_a_lower_stop(cfg):
    _, pos = opened(cfg, 5.0)
    assert breakeven_stop(pos, snap(dex="raydium"), cfg, SOL) < breakeven_stop(pos, snap(), cfg, SOL)


def test_float_replay_closes_green_not_red(cfg):
    """FLOAT ran to 1.64x, faded and got time-stopped at 0.92x for -24%. Now the stop
    arms on the way up and sells above cost on the way down."""
    pf, pos = opened(cfg, 5.0)
    for m in (1.1, 1.3, 1.5, 1.64, 1.4):
        assert tick(pos, cfg, m) is None
    stop = breakeven_stop(pos, snap(), cfg, SOL)
    sig = tick(pos, cfg, stop / pos.entry_price * 0.999)
    assert sig and "break-even stop" in sig.reason and sig.fraction == 1.0 and not sig.review
    pf.sell(cfg, pos, 1.0, stop * 0.999, 40_000, SOL, dex="pumpswap", mcap_usd=120_000)
    assert pf.close(pos) > 0


def test_not_armed_until_it_has_run(cfg):
    """CATCULUS peaked at 1.24x: too little room to arm, the normal stop still applies."""
    _, pos = opened(cfg, 5.0)
    assert tick(pos, cfg, 1.24) is None
    assert tick(pos, cfg, 1.02) is None
    sig = tick(pos, cfg, 0.65)
    assert "stop loss" in sig.reason and sig.review


def test_gap_through_an_armed_stop_sells_without_review(cfg):
    _, pos = opened(cfg, 10.0)
    tick(pos, cfg, 1.6)
    sig = tick(pos, cfg, 0.6)
    assert "break-even stop" in sig.reason and not sig.review


def test_breakeven_stop_is_off_once_initials_are_out(cfg):
    _, pos = opened(cfg, 10.0)
    tick(pos, cfg, 1.6)
    pos.initials_taken = True
    assert tick(pos, cfg, 1.15) is None  # the trailing stop's job now


def test_fading_volume_sells_half_once(cfg):
    _, pos = opened(cfg, 10.0)
    t = time.time()
    tick(pos, cfg, 1.6, now=t)
    quiet = {"vol_5m": 3_000, "vol_1h": 90_000}  # 0.4x the hourly pace
    assert tick(pos, cfg, 1.45, now=t + 10, **quiet) is None  # first sight: wait for it to hold
    assert tick(pos, cfg, 1.45, now=t + 40, **quiet) is None
    sig = tick(pos, cfg, 1.45, now=t + 75, **quiet)
    assert sig and "faded" in sig.reason and sig.fraction == 0.5
    assert tick(pos, cfg, 1.45, now=t + 200, **quiet) is None  # once per position


def test_one_quiet_tick_does_not_sell(cfg):
    _, pos = opened(cfg, 10.0)
    t = time.time()
    tick(pos, cfg, 1.6, now=t)
    quiet = {"vol_5m": 3_000, "vol_1h": 90_000}
    assert tick(pos, cfg, 1.45, now=t + 10, **quiet) is None
    assert tick(pos, cfg, 1.45, now=t + 40) is None  # volume came back: the clock resets
    assert tick(pos, cfg, 1.45, now=t + 80, **quiet) is None


def test_small_position_sells_all_on_a_fade(cfg):
    """Half of a ~$7 position is under $4: one more sell's network fee isn't worth it."""
    _, pos = opened(cfg, 5.0)
    t = time.time()
    tick(pos, cfg, 1.5, now=t)
    quiet = {"vol_5m": 2_000, "vol_1h": 90_000}
    tick(pos, cfg, 1.4, now=t + 1, **quiet)
    sig = tick(pos, cfg, 1.4, now=t + 70, **quiet)
    assert sig and sig.fraction == 1.0


def test_no_fade_sell_before_it_is_green(cfg):
    _, pos = opened(cfg, 10.0)
    t = time.time()
    quiet = {"vol_5m": 1_000, "vol_1h": 90_000}
    for dt in (0, 30, 90, 200):
        assert tick(pos, cfg, 1.1, now=t + dt, **quiet) is None


def test_fade_trims_the_runner_after_initials(cfg):
    _, pos = opened(cfg, 10.0)
    pos.initials_taken, t = True, time.time()
    quiet = {"vol_5m": 2_000, "vol_1h": 90_000}
    tick(pos, cfg, 2.5, now=t, **quiet)
    sig = tick(pos, cfg, 2.5, now=t + 70, **quiet)
    assert sig and "faded" in sig.reason


def test_empty_exit_plan_keeps_its_state(cfg):
    pf = Portfolio(cash_usd=100.0)
    pos = pf.buy(cfg, snap(), 10.0, SOL, "MIGRATED", {}, "")
    tick(pos, cfg, 1.6)
    assert pos.exit_plan.get("_be_armed")
    assert "break-even stop" in tick(pos, cfg, 1.05).reason
