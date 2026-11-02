"""The replay of Trencher's first 19 closed trades (Oct 28 - Nov 2 2026), pinned so the
diagnosis in PR 17 stays checkable: the picks lost before costs, stop losses did most of
the damage, and costs ate ~13% of every dollar that went in."""

from pathlib import Path

import pytest

from agent import replay

DATA = Path(__file__).parent / "data" / "closes_2026-11-02.json"


@pytest.fixture
def logged():
    return replay.load_closes(DATA)


def test_the_picks_lost_before_costs(logged):
    a = replay.analyse(*logged)
    assert a["trades"] == 19
    assert a["net_usd"] == pytest.approx(-19.48, abs=0.01)
    assert a["gross_usd"] == pytest.approx(-3.59, abs=0.01)  # red even with zero fees
    assert a["costs_usd"] == pytest.approx(15.89, abs=0.01)


def test_stop_losses_did_most_of_the_damage(logged):
    a = replay.analyse(*logged)
    stop = a["by_exit"]["stop loss"]
    assert stop["n"] == 8 and stop["net_usd"] == pytest.approx(-18.87, abs=0.01)
    assert stop["never_green"] == 5
    s = a["stop_losses"]
    # The stop fired a few points past its level; fees and slippage did twice that.
    assert 3 < s["avg_points_past_the_stop_when_it_fired"] < 6
    assert -12 < s["avg_points_lost_to_costs"] < -9
    assert s["reviewed"] == 8


def test_what_ifs_scale_costs_the_right_way(logged):
    closes, meta = logged
    a = replay.analyse(closes, meta)
    w = a["what_if"]
    assert w["as_logged"] == pytest.approx(a["net_usd"], abs=0.02)
    assert w["no_costs_at_all"] == pytest.approx(a["gross_usd"], abs=0.01)
    assert w["as_logged"] < w["priority_0.0002_sol_no_tip"] < w["no_costs_at_all"]
    # Bigger positions don't fix picks that lose before costs.
    assert w["every_trade_25usd"] < w["as_logged"]


def test_render_names_the_numbers(logged):
    text = replay.render(replay.analyse(*logged))
    assert "gross $-3.59" in text and "Stop losses: 8" in text


def test_replay_cli_reads_the_trade_log(tmp_path, monkeypatch, capsys):
    from agent import journal
    from agent.config import Config
    monkeypatch.setenv("MEMORY_DIR", str(tmp_path))
    cfg = Config.from_env()
    closes, _ = replay.load_closes(DATA)
    for c in closes[:3]:
        journal.log_trade(cfg, c)
    replay.main(None, cfg)
    assert "3 closed trades" in capsys.readouterr().out
