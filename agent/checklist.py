"""The guide's pre-trade due diligence checklist (Part 1 §4), as code.

`classify_setup` decides which strategy a pair fits (or none).
`run_checklist` returns hard failures (never trade), warnings (weigh them) and
plusses, each tagged with the video it comes from.
"""

from __future__ import annotations

import re
from dataclasses import dataclass, field

from .config import Config

BONDING_DEXES = {"pumpfun", "pump.fun", "pumpdotfun"}


@dataclass
class Checklist:
    setup: str | None
    fails: list[str] = field(default_factory=list)
    warns: list[str] = field(default_factory=list)
    plusses: list[str] = field(default_factory=list)
    holders: dict = field(default_factory=dict)
    # Holder data didn't load (or came back empty): tradable only as a probe, because
    # concentration, dev share and bundles are unknown.
    partial: bool = False

    @property
    def passed(self) -> bool:
        return self.setup is not None and not self.fails

    @property
    def score(self) -> int:
        """Crude 0-100 quality score for the rule-only brain."""
        return max(0, min(100, 60 + 8 * len(self.plusses) - 10 * len(self.warns)))

    def as_dict(self) -> dict:
        return {
            "setup": self.setup,
            "passed": self.passed,
            "score": self.score,
            "fails": self.fails,
            "warns": self.warns,
            "plusses": self.plusses,
            "holders": self.holders,
            "partial_holder_data": self.partial,
        }


def is_dip(snap: dict, cfg: Config) -> bool:
    """A proven coin pulling back 40-75% off its recent high: a possible buy if the
    narrative and attention are still there. `peak_mcap_usd`/`drawdown_pct` are
    filled in by the agent from its own price tracking and recent candles."""
    dd = snap.get("drawdown_pct")
    return (
        dd is not None
        and cfg.dip_min_drawdown_pct <= dd <= cfg.dip_max_drawdown_pct
        and (snap.get("peak_mcap_usd") or 0) >= cfg.dip_min_peak_mcap_usd
        and snap["mcap_usd"] >= cfg.migrated_min_mcap_usd
    )


def classify_setup(snap: dict, cfg: Config, sol_usd: float) -> str | None:
    mcap = snap["mcap_usd"]
    age = snap["age_hours"]
    if snap["dex"] in BONDING_DEXES:
        bond_usd = cfg.bond_mcap_sol * sol_usd
        pct = 100 * mcap / bond_usd if bond_usd else 0
        snap["bond_pct"] = round(pct, 1)
        if cfg.final_stretch_min_bond_pct <= pct <= cfg.final_stretch_max_bond_pct:
            return "FINAL_STRETCH"
        return None
    if is_dip(snap, cfg):
        return "DIP"
    if cfg.recon_min_mcap_usd <= mcap <= cfg.recon_max_mcap_usd:
        return "MIGRATED"
    if age is not None and age <= cfg.migrated_max_age_hours and mcap >= cfg.migrated_min_mcap_usd:
        return "MIGRATED"
    return None


def market_prefilter(snap: dict, cfg: Config, sol_usd: float) -> str | None:
    """Cheap filter on DexScreener data alone, before spending a RugCheck call."""
    setup = classify_setup(snap, cfg, sol_usd)
    if setup is None:
        return None
    if snap["vol_5m"] < cfg.min_vol_5m_usd:
        return None
    if setup != "FINAL_STRETCH" and snap["liquidity_usd"] < cfg.min_liquidity_usd:
        return None
    return setup


def holder_stats(report: dict, snap: dict) -> dict:
    """Top-10 / insider / dev concentration, with pool and locker accounts removed
    (the bonding curve or AMM vault always shows up as the biggest 'holder')."""
    known = report.get("knownAccounts") or {}
    excluded = {a for a, v in known.items() if (v or {}).get("type") in ("AMM", "LOCKER")}
    for m in report.get("markets") or []:
        excluded.update(filter(None, [m.get("pubkey"), m.get("liquidityA"), m.get("liquidityB")]))
    if snap.get("pair_address"):
        excluded.add(snap["pair_address"])

    holders = [
        h for h in report.get("topHolders") or []
        if h.get("owner") not in excluded and h.get("address") not in excluded
    ]
    holders.sort(key=lambda h: h.get("pct") or 0, reverse=True)
    top10 = sum(h.get("pct") or 0 for h in holders[:10])
    insider = sum(h.get("pct") or 0 for h in holders if h.get("insider"))
    creator = report.get("creator")
    dev_pct = sum(h.get("pct") or 0 for h in holders if creator and h.get("owner") == creator)
    supply = (report.get("token") or {}).get("supply") or 0
    if not dev_pct and supply and report.get("creatorBalance"):
        dev_pct = 100 * report["creatorBalance"] / supply
    return {
        "top10_pct_ex_pool": round(top10, 2),
        "insider_pct": round(insider, 2),
        "dev_pct": round(dev_pct, 2),
        "largest_holder_pct": round(holders[0].get("pct") or 0, 2) if holders else 0,
        "total_holders": report.get("totalHolders"),
        # graphInsidersDetected counts wallets, not networks: 465 wallets can be 10 clusters.
        "insider_wallets_flagged": report.get("graphInsidersDetected") or 0,
        **bundle_stats(report),
    }


def bundle_stats(report: dict) -> dict:
    """What RugCheck's linked-wallet clusters (insiderNetworks: wallets funded from the
    same source, i.e. bundles) hold right now, as % of supply. A report without the
    field can't say; an empty or null one means no clusters were found."""
    if "insiderNetworks" not in report:
        return {"bundles_checked": False, "bundle_networks": 0, "bundle_pct": None, "largest_bundle_pct": None}
    supply = float((report.get("token") or {}).get("supply") or 0)
    nets = report.get("insiderNetworks") or []
    shares = []
    for n in nets:
        held = float((n or {}).get("currentHolding") or (n or {}).get("tokenAmount") or 0)
        shares.append(100 * held / supply if supply else 0.0)
    if nets and not supply:
        return {"bundles_checked": False, "bundle_networks": len(nets), "bundle_pct": None, "largest_bundle_pct": None}
    return {"bundles_checked": True, "bundle_networks": len(nets), "bundle_pct": round(min(100.0, sum(shares)), 2),
            "largest_bundle_pct": round(max(shares, default=0.0), 2)}


def pumpfun_launch(snap: dict) -> bool:
    """A pump.fun coin (bonding curve or PumpSwap): the launchpad revokes mint and
    freeze at creation and burns the LP at migration, so those checks hold even when
    RugCheck doesn't answer. Holders, dev share and bundles still don't."""
    return (snap.get("address") or "").endswith("pump") and snap.get("dex") in BONDING_DEXES | {"pumpswap"}


def hack_story(snap: dict, cfg: Config) -> str | None:
    """The word that ties this coin to a hack story, or None. Owner rule: hacked
    projects and coins riding a hack headline tend to go down."""
    text = f"{snap.get('name') or ''} {snap.get('symbol') or ''}".lower()
    for term in cfg.avoid_terms:
        term = str(term).strip()
        # A contract address matches that coin only; a word or ticker matches it whole
        # (so "cop" doesn't block "Copper").
        if term and (term == snap.get("address") or re.search(rf"\b{re.escape(term.lower())}\b", text)):
            return snap.get("symbol") or term if term == snap.get("address") else term
    m = re.search(cfg.hack_story_pattern, text) if cfg.hack_story_pattern else None
    return m.group(0) if m else None


def run_checklist(snap: dict, report: dict | None, same_name: list[dict], cfg: Config, sol_usd: float) -> Checklist:
    c = Checklist(setup=classify_setup(snap, cfg, sol_usd))
    hack = hack_story(snap, cfg)
    if hack:
        c.fails.append(f"Hack story (\"{hack}\" in the name or ticker): these tend to go down, owner rule")
        return c
    if c.setup is None:
        c.fails.append("No setup fits: not Final Stretch, not a migrated runner, not a healthy dip")
        return c

    # --- Flow ---
    if snap["vol_5m"] < cfg.min_vol_5m_usd:
        c.fails.append(f"5m volume ${snap['vol_5m']:,.0f} is dead (<${cfg.min_vol_5m_usd:,.0f}) (V1)")
    elif snap["vol_5m"] < cfg.good_vol_5m_usd:
        c.warns.append(f"5m volume ${snap['vol_5m']:,.0f} is 'fine, not optimal' (<$10k) (V1)")
    else:
        c.plusses.append(f"5m volume ${snap['vol_5m']:,.0f} ≥ $10k (V1, V6, V13)")
    tx5 = snap["buys_5m"] + snap["sells_5m"]
    if tx5 and snap["vol_5m"] / tx5 > 1500:
        c.warns.append("Few, large trades in 5m: volume may be a few whales or a farm (V13)")
    if snap["sells_1h"] and snap["buys_1h"] / max(1, snap["sells_1h"]) < 0.6:
        c.warns.append("Sellers dominate the last hour")
    if c.setup != "FINAL_STRETCH" and snap["mcap_usd"] and snap["liquidity_usd"] / snap["mcap_usd"] < 0.05:
        c.warns.append("Thin liquidity vs market cap: exits will slip hard")

    # --- Attention: trade the narrative and the attention ---
    accel = snap.get("vol_5m_vs_hour_avg")
    buy_ratio = snap.get("buy_ratio_5m")
    if accel is not None and accel >= 1.5:
        c.plusses.append(f"Attention rising: 5m volume is {accel:.1f}x the hour's average")
    elif accel is not None and accel < 0.5:
        c.warns.append(f"Attention fading: 5m volume is only {accel:.1f}x the hour's average")

    # --- Dip-specific: a correction is only a buy if the crowd is still here ---
    if c.setup == "DIP":
        dd = snap["drawdown_pct"]
        if dd > 65:
            c.warns.append(f"Deep correction ({dd:.0f}% off the high): only with a very strong narrative")
        if accel is not None and accel < cfg.dip_min_attention_ratio:
            c.fails.append(f"Dip with fading attention is a falling knife, not a dip (5m at {accel:.2f}x "
                           f"the hour's pace, under {cfg.dip_min_attention_ratio:g}x)")
        if buy_ratio is not None and buy_ratio < 0.45:
            c.warns.append(f"Sellers still in control on the dip ({buy_ratio:.0%} buys in 5m)")
        elif buy_ratio is not None and buy_ratio >= 0.55 and (snap.get("change_5m") or 0) > 0:
            c.plusses.append("Buyers stepping in on the dip (V1: big buys on a dip are bullish)")

    # --- Attention / community ---
    if snap["boosts"] >= cfg.suspicious_boosts:
        c.fails.append(f"{snap['boosts']} boosts (~$20k spent) is suspicious (V6)")
    elif 200 <= snap["boosts"] <= 1000:
        c.plusses.append(f"{snap['boosts']} boosts: sweet spot (V6)")
    if "twitter" not in snap["socials"] and "x" not in snap["socials"]:
        c.warns.append("No X account linked: can't check the community or the CA on X (V1, V3, V13)")
    if snap["has_paid_profile"]:
        c.plusses.append("DexScreener profile paid/updated (V13)")

    # --- Web crawl: buzz and the project's own site ---
    buzz = snap.get("buzz") or {}
    if buzz.get("fits_hot_narratives"):
        c.plusses.append(f"Fits what the web is talking about now: {', '.join(buzz['fits_hot_narratives'][:3])} (V1, V5)")
    if buzz.get("on_coingecko_trending"):
        c.plusses.append("Ticker is on CoinGecko trending")
    if buzz.get("ca_call_count"):
        c.warns.append(f"CA called in {len(buzz['ca_called_in'])} channel(s): attention, but callers farm exit liquidity (V7)")
    web = snap.get("web") or {}
    sites = [x for x in web.get("websites", []) if not x.get("skipped")]
    for site in sites:
        if site.get("reachable") is False:
            c.warns.append(f"Project website {site['host']} is down")
        elif site.get("other_addresses") and not site.get("shows_this_ca"):
            c.warns.append(f"{site['host']} shows a different contract address: this may be a vamp (V1, V3)")
        elif site.get("shows_this_ca"):
            c.plusses.append(f"{site['host']} shows this exact contract address")
    claims = {w for x in sites for w in x.get("tech_claims", [])}
    live_repo = any((g.get("days_since_push") or 1e9) <= 30 for g in web.get("github", []))
    if claims & {"ai", "agent", "agents", "protocol", "platform", "sdk", "api", "framework", "infrastructure"} and not live_repo:
        c.warns.append("Tech/AI claims with no GitHub pushed in the last 30 days: probably a LARP (V1)")
    elif live_repo:
        c.plusses.append("Linked GitHub has real recent work (V1)")

    # --- Right token or vamp? ---
    bigger = [
        p for p in same_name
        if p.get("baseToken", {}).get("address") != snap["address"]
        and float(p.get("marketCap") or p.get("fdv") or 0) > snap["mcap_usd"] * 1.5
    ]
    if bigger:
        c.warns.append(f"{len(bigger)} bigger token(s) share this ticker: may be a vamp/copycat (V1, V3)")
    elif len(same_name) > 3:
        c.warns.append(f"{len(same_name)} tokens share this ticker: crowded meta, pick the original (V13)")

    # --- On-chain safety (RugCheck) ---
    if report is None:
        if pumpfun_launch(snap):
            c.partial = True
            c.warns.append("RugCheck didn't load: holders, dev share and bundles are unverified (mint, freeze "
                           "and LP are handled by the pump.fun launchpad). Probe size only.")
        else:
            c.fails.append("RugCheck report unavailable: can't verify mint/freeze/holders, skip")
        return c
    if report.get("rugged"):
        c.fails.append("RugCheck marks this token as rugged")
    if report.get("mintAuthority"):
        c.fails.append("Mint authority NOT revoked (V2, V3, V6)")
    if report.get("freezeAuthority"):
        c.fails.append("Freeze authority NOT revoked: honeypot risk (V6, V10)")
    fee = (report.get("transferFee") or {}).get("pct") or 0
    if fee:
        c.fails.append(f"Token has a {fee}% transfer tax")
    for r in report.get("risks") or []:
        if (r.get("level") or "").lower() == "danger":
            c.fails.append(f"RugCheck danger: {r.get('name')} {r.get('value') or ''}".strip())
        elif (r.get("level") or "").lower() == "warn":
            c.warns.append(f"RugCheck warn: {r.get('name')}")
    if c.setup != "FINAL_STRETCH":
        lp = max((((m.get("lp") or {}).get("lpLockedPct") or 0) for m in report.get("markets") or []), default=0)
        if lp < cfg.min_lp_locked_pct:
            c.fails.append(f"LP only {lp:.0f}% burned/locked (V2, V3, V6)")
    if (report.get("tokenMeta") or {}).get("mutable"):
        c.warns.append("Token metadata is mutable")

    h = holder_stats(report, snap)
    c.holders = h
    if not report.get("topHolders"):
        c.partial = True
        c.warns.append("RugCheck returned no holder list: top 10 and dev share are unverified. Probe size only.")
    if h["dev_pct"] > cfg.max_dev_pct:
        c.fails.append(f"Dev holds {h['dev_pct']:.1f}% (>1%) (V13, V17)")
    if h["top10_pct_ex_pool"] > cfg.max_top10_pct:
        c.fails.append(f"Top 10 hold {h['top10_pct_ex_pool']:.1f}% ex-pool (>25%) (V13)")
    elif h["top10_pct_ex_pool"] > cfg.warn_top10_pct:
        c.warns.append(f"Top 10 hold {h['top10_pct_ex_pool']:.1f}% ex-pool (>15%) (V6)")
    else:
        c.plusses.append(f"Top 10 hold only {h['top10_pct_ex_pool']:.1f}% ex-pool (V6)")
    if h["insider_pct"] > cfg.max_insider_pct:
        c.fails.append(f"Insiders hold {h['insider_pct']:.1f}% (>10%) (V13)")
    if h["bundles_checked"]:
        if h["bundle_pct"] > cfg.max_bundle_pct:
            c.fails.append(f"Bundles: {h['bundle_networks']} linked wallet cluster(s) hold {h['bundle_pct']:.1f}% "
                           f"of supply (>{cfg.max_bundle_pct:g}%) (V17)")
        elif h["largest_bundle_pct"] > cfg.warn_bundle_pct:
            c.warns.append(f"Bundles: one linked wallet cluster holds {h['largest_bundle_pct']:.1f}% "
                           f"({h['bundle_pct']:.1f}% across {h['bundle_networks']}) (V3, V17)")
        elif h["bundle_networks"]:
            c.plusses.append(f"Bundle check: {h['bundle_networks']} small linked cluster(s), "
                             f"{h['bundle_pct']:.1f}% of supply combined (V3, V17)")
        else:
            c.plusses.append("Bundle check: no linked wallet clusters found (V3, V17)")
    else:
        c.warns.append("Bundles unverified: RugCheck gave no wallet-cluster data for this coin")
    if h["largest_holder_pct"] > 5:
        c.warns.append(f"Largest non-pool wallet holds {h['largest_holder_pct']:.1f}%")
    if (h["total_holders"] or 0) and h["total_holders"] < 150:
        c.warns.append(f"Only {h['total_holders']} holders")
    return c
