"""Conviction-based position sizing.

Only risk what you're willing to lose (V8): conviction decides how much of the
wallet you're willing to lose on this idea, and the stop decides how big the
position can be for that loss to be the most you lose.

    risk_usd = equity × risk%(conviction)
    size     = (risk_usd − 2 × network fee) ÷ (stop distance + round-trip % costs)

Network fees are a flat amount per transaction, so on a small position they eat
a big share of the risk: when they'd eat all of it, the trade isn't worth taking.

So a high-conviction coin with a tight stop gets a big position, and a coin
you're unsure about with a wide stop gets a small one. Caps keep any one rug
(which skips the stop) and the total open risk survivable.
"""

from __future__ import annotations

import re
from dataclasses import dataclass

from .config import Config
from .portfolio import Portfolio, network_fee_usd


def round_trip_cost_pct(size_usd: float, cfg: Config, sol_usd: float, venue_pct: float | None = None,
                        liquidity_usd: float = 0.0) -> float:
    """What buying `size_usd` and selling it all back at an unchanged price costs, as a
    % of size, with the same fees and slippage the paper wallet charges. Without a
    liquidity figure only the base slippage is counted."""
    if size_usd <= 0:
        return 100.0
    venue = cfg.other_dex_fee_pct if venue_pct is None else venue_pct
    pct_fee = (cfg.platform_fee_pct + venue) / 100
    net = network_fee_usd(cfg, sol_usd)

    def slip(usd: float) -> float:
        return Portfolio._slippage(cfg, usd, liquidity_usd) if liquidity_usd else cfg.base_slippage_pct / 100

    spend = size_usd * (1 - pct_fee) - net
    if spend <= 0:
        return 100.0
    held = spend / (1 + slip(spend))  # value of the tokens at the unchanged price
    gross = held * (1 - slip(held))
    proceeds = max(0.0, gross * (1 - pct_fee) - net)
    return 100 * (size_usd - proceeds) / size_usd


@dataclass
class FeeCheck:
    ok: bool
    cost_pct: float  # round trip at an unchanged price
    target_pct: float  # gain at the first profit target
    note: str


def fee_check(size_usd: float, first_target_multiple: float, cfg: Config, sol_usd: float,
              venue_pct: float | None = None, liquidity_usd: float = 0.0) -> FeeCheck:
    """Is this trade worth its fees? Its first profit target has to pay the round trip
    several times over (min_target_cost_multiple), and the round trip itself can't eat
    more than max_round_trip_cost_pct of the position (fee-eaten micro trades).

    This replaces any flat friction cap: a round trip always costs at least the % fees
    and base slippage both ways, so a cap below that floor would block every trade."""
    cost = round_trip_cost_pct(size_usd, cfg, sol_usd, venue_pct, liquidity_usd)
    target = (first_target_multiple - 1) * 100
    need = cfg.min_target_cost_multiple * cost
    if cost > cfg.max_round_trip_cost_pct:
        return FeeCheck(False, round(cost, 1), round(target, 1),
                        f"a ${size_usd:.2f} round trip costs {cost:.1f}%, over the {cfg.max_round_trip_cost_pct:g}% "
                        f"ceiling: fees would eat the trade")
    if target < need:
        return FeeCheck(False, round(cost, 1), round(target, 1),
                        f"first target +{target:.0f}% doesn't pay {cfg.min_target_cost_multiple:g}x the "
                        f"{cost:.1f}% round trip (needs +{need:.0f}%)")
    return FeeCheck(True, round(cost, 1), round(target, 1),
                    f"round trip {cost:.1f}%, first target +{target:.0f}% pays it "
                    f"{target / cost if cost else 0:.1f}x")


_CITES_FEES = re.compile(r"friction|fees?\b|round.?trip|too small|minimum|under \$\d", re.I)


def cites_fees(verdict: str) -> bool:
    """Does a PASS verdict blame fees or position size rather than the coin?"""
    return bool(_CITES_FEES.search(verdict))


def first_target_multiple(plan: dict, entry_mcap_usd: float) -> float:
    """The first price multiple where the exit plan takes profit: initials, or the
    target market cap if that comes sooner."""
    first = float(plan.get("take_initials_multiple") or 0) or 2.0
    target = plan.get("target_mcap_usd")
    if target and entry_mcap_usd and target > entry_mcap_usd:
        first = min(first, target / entry_mcap_usd)
    return first


def risk_table(cfg: Config) -> dict[int, float]:
    table = {}
    for pair in cfg.conviction_risk_pct.split(","):
        k, v = pair.split(":")
        table[int(k)] = float(v)
    return table


def risk_pct_for(conviction: int, cfg: Config) -> float:
    conviction = max(1, min(10, int(conviction)))
    return risk_table(cfg).get(conviction, 0.0)


def loss_at_stop_frac(stop_loss_pct: float, cfg: Config, venue_pct: float | None = None) -> float:
    """Fraction of the position lost if the stop is hit, incl. % fees and slippage both
    ways. Flat network fees come on top (see position_size)."""
    venue = cfg.other_dex_fee_pct if venue_pct is None else venue_pct
    costs = 2 * (cfg.platform_fee_pct + venue + cfg.base_slippage_pct)
    return (stop_loss_pct + costs) / 100


def open_risk_usd(pf: Portfolio, cfg: Config) -> float:
    """At-stop risk still on the table. Positions with initials out are free rides."""
    total = 0.0
    for p in pf.positions.values():
        if p.initials_taken:
            continue
        stop = (p.exit_plan or {}).get("stop_loss_pct", cfg.stop_loss_pct)
        total += p.cost_usd * loss_at_stop_frac(stop, cfg, p.venue_fee_pct or None) + 2 * p.network_fee_usd
    return total


@dataclass
class Sizing:
    size_usd: float
    risk_usd: float
    risk_pct: float
    note: str


def position_size(conviction: int, stop_loss_pct: float, pf: Portfolio, cfg: Config,
                  sol_usd: float = 0.0, venue_pct: float | None = None) -> Sizing:
    equity = pf.equity()
    risk_pct = risk_pct_for(conviction, cfg)
    if risk_pct <= 0:
        return Sizing(0.0, 0.0, 0.0, f"conviction {conviction}/10 is not worth risking money on")

    per_dollar_loss = loss_at_stop_frac(stop_loss_pct, cfg, venue_pct)
    fixed = 2 * network_fee_usd(cfg, sol_usd)  # buy + sell transactions
    risk_usd = equity * risk_pct / 100
    note = f"conviction {conviction}/10 → risk {risk_pct:g}% (${risk_usd:.2f}) with a {stop_loss_pct:.0f}% stop"
    if risk_usd <= fixed:
        return Sizing(0.0, 0.0, risk_pct, note + f", but ${fixed:.2f} of network fees would eat all of it")
    size = (risk_usd - fixed) / per_dollar_loss

    caps = {
        "max position": equity * cfg.max_position_pct / 100,
        "cash": pf.cash_usd - 0.25,
        "total risk budget": max(0.0, equity * cfg.max_total_risk_pct / 100 - open_risk_usd(pf, cfg) - fixed)
        / per_dollar_loss,
    }
    binding = min(caps, key=caps.get)
    if caps[binding] < size:
        size = max(0.0, caps[binding])
        note += f", capped by {binding}"
    return Sizing(round(size, 2), round(size * per_dollar_loss + (fixed if size else 0), 2), risk_pct, note)


def cost_note(cfg: Config, sol_usd: float, venue_pct: float | None = None) -> str:
    """What one round trip costs, in words, for the brain's prompt."""
    venue = cfg.other_dex_fee_pct if venue_pct is None else venue_pct
    net = network_fee_usd(cfg, sol_usd)
    return (f"Every trade pays real costs (as on Axiom): {cfg.platform_fee_pct:g}% Axiom fee + {venue:g}% pool fee "
            f"each way, ${net:.2f} of network fees per transaction (priority + tip), and slippage "
            f"({cfg.base_slippage_pct:g}% + price impact). A $5 round trip at an unchanged price loses about "
            f"${5 * 2 * (cfg.platform_fee_pct + venue + cfg.base_slippage_pct) / 100 + 2 * net:.2f}.")


def sizing_guide(pf: Portfolio, cfg: Config, stop_loss_pct: float | None = None,
                 sol_usd: float = 0.0, venue_pct: float | None = None, liquidity_usd: float = 0.0) -> str:
    """Human-readable table for the brain's prompt, with what each size's round trip
    costs and the fee check (at the default first target)."""
    stop = stop_loss_pct or cfg.stop_loss_pct
    rows = [cost_note(cfg, sol_usd, venue_pct)] if sol_usd else []
    for c, r in sorted(risk_table(cfg).items()):
        if r <= 0:
            continue
        s = position_size(c, stop, pf, cfg, sol_usd, venue_pct)
        row = f"  conviction {c:>2}: risk {r:g}% of equity → ~${s.size_usd:.2f} position at a {stop:.0f}% stop"
        if not s.size_usd:
            row += " (not worth it after fees)"
        elif sol_usd:
            fc = fee_check(s.size_usd, cfg.take_initials_multiple, cfg, sol_usd, venue_pct, liquidity_usd)
            row += (f", round trip ~{fc.cost_pct:g}%"
                    + (", passes the fee check" if fc.ok else f", fails the fee check at {cfg.take_initials_multiple:g}x"))
        rows.append(row)
    return "\n".join(rows)


def fee_rule_text(cfg: Config, sol_usd: float, venue_pct: float | None = None) -> str:
    """The fee rule as the brain should know it. Code enforces it after a BUY."""
    floor = 2 * (cfg.platform_fee_pct + (cfg.other_dex_fee_pct if venue_pct is None else venue_pct)
                 + cfg.base_slippage_pct)
    return (f"Fees and size are checked in code after you say BUY: the trade goes ahead only if its first "
            f"profit target pays at least {cfg.min_target_cost_multiple:g}x its real round-trip cost and the "
            f"round trip costs no more than {cfg.max_round_trip_cost_pct:g}% of the position. On this coin's pool "
            f"a round trip never costs less than about {floor:g}% plus ${2 * network_fee_usd(cfg, sol_usd):.2f} of "
            f"network fees, so any flat friction cap below that, or a minimum position size, in your lessons "
            f"or learned rules is retired: it would block every trade. Don't PASS a coin over fees or size, "
            f"and don't raise conviction or stretch the first target just to pass the check. Judge the coin.")
