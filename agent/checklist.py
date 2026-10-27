"""The guide's pre-trade due diligence checklist (Part 1 §4), as code.

`classify_setup` decides which strategy a pair fits (or none).
`run_checklist` returns hard failures (never trade), warnings (weigh them) and
plusses, each tagged with the video it comes from.
"""

from __future__ import annotations

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
        }


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
    if setup == "MIGRATED" and snap["liquidity_usd"] < cfg.min_liquidity_usd:
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
        "insider_networks_detected": report.get("graphInsidersDetected") or 0,
    }


def run_checklist(snap: dict, report: dict | None, same_name: list[dict], cfg: Config, sol_usd: float) -> Checklist:
    c = Checklist(setup=classify_setup(snap, cfg, sol_usd))
    if c.setup is None:
        c.fails.append("No setup fits: not in Final Stretch range and not a migrated runner")
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
    if c.setup == "MIGRATED" and snap["mcap_usd"] and snap["liquidity_usd"] / snap["mcap_usd"] < 0.05:
        c.warns.append("Thin liquidity vs market cap: exits will slip hard")

    # --- Attention / community ---
    if snap["boosts"] >= cfg.suspicious_boosts:
        c.fails.append(f"{snap['boosts']} boosts (~$20k spent) is suspicious (V6)")
    elif 200 <= snap["boosts"] <= 1000:
        c.plusses.append(f"{snap['boosts']} boosts: sweet spot (V6)")
    if "twitter" not in snap["socials"] and "x" not in snap["socials"]:
        c.warns.append("No X account linked: can't check the community or the CA on X (V1, V3, V13)")
    if snap["has_paid_profile"]:
        c.plusses.append("DexScreener profile paid/updated (V13)")

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
    if c.setup == "MIGRATED":
        lp = max((((m.get("lp") or {}).get("lpLockedPct") or 0) for m in report.get("markets") or []), default=0)
        if lp < cfg.min_lp_locked_pct:
            c.fails.append(f"LP only {lp:.0f}% burned/locked (V2, V3, V6)")
    if (report.get("tokenMeta") or {}).get("mutable"):
        c.warns.append("Token metadata is mutable")

    h = holder_stats(report, snap)
    c.holders = h
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
    if h["insider_networks_detected"]:
        c.warns.append(f"{h['insider_networks_detected']} insider wallet network(s) detected (V13, V17)")
    if h["largest_holder_pct"] > 5:
        c.warns.append(f"Largest non-pool wallet holds {h['largest_holder_pct']:.1f}%")
    if (h["total_holders"] or 0) and h["total_holders"] < 150:
        c.warns.append(f"Only {h['total_holders']} holders")
    return c
