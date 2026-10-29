"""All tunable numbers in one place.

Defaults come from the Trenches Bootcamp guide (knowledge/memecoin-study-guide.txt).
Every field can be overridden with an env var of the same name in upper case,
e.g. STARTING_CASH_USD=250 or MAX_POSITION_PCT=5.
"""

from __future__ import annotations

import json
import os
from dataclasses import dataclass, field, fields
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent


@dataclass
class Config:
    # --- Wallet ------------------------------------------------------------
    starting_cash_usd: float = 100.0
    # Sizing: conviction (1-10) sets how much of equity you're willing to LOSE if the
    # stop is hit; the stop distance then sets the position size. "conviction:risk%".
    conviction_risk_pct: str = "1:0,2:0,3:0,4:0,5:1,6:1.5,7:2.5,8:4,9:6,10:8"
    max_position_pct: float = 25.0  # hard cap per position: a rug skips the stop (V8)
    max_total_risk_pct: float = 25.0  # combined at-stop risk across all open positions (evolvable)
    min_position_usd: float = 2.0
    max_open_positions: int = 0  # 0 = no limit: a bot has more eyes; the risk budget is the limit
    daily_loss_limit_pct: float = 25.0  # stop opening trades for the day past this drawdown
    broke_equity_usd: float = 5.0  # below this the agent stops trading entirely

    # --- Paper execution model ---------------------------------------------
    # Every paper fill pays what the same trade on Axiom (Lenny's terminal) would:
    # the terminal fee, the pool's own fee, Solana network fees and slippage.
    platform_fee_pct: float = 1.0  # Axiom's fee per swap (its small cashback isn't counted)
    pumpfun_curve_fee_pct: float = 1.25  # pump.fun bonding curve: 0.95% protocol + 0.30% creator
    # PumpSwap fee by market cap in SOL, "tier start:fee%". From pump.fun's fee docs
    # (Sep 2026); inside tiers the docs list but these don't, the higher fee applies.
    pumpswap_fee_tiers: str = "0:1.25,420:1.2,1470:1.15,2460:1.1,9820:0.95,34380:0.7,63860:0.475,98240:0.3"
    other_dex_fee_pct: float = 0.25  # Raydium/Orca/Meteora pool fee (varies by pool)
    network_fee_sol: float = 0.000005  # Solana base fee per signature
    priority_fee_sol: float = 0.001  # priority fee per tx (V2)
    bribe_sol: float = 0.001  # Jito tip / bribe per tx (V2)
    base_slippage_pct: float = 1.5  # spread/latency cost on top of price impact
    max_slippage_pct: float = 20.0  # sell slippage cap (V17)

    # --- Discovery / market filters (guide Part 1 §3 and §5) ---------------
    bond_mcap_sol: float = 410.0  # pump.fun graduation market cap in SOL (~$41k at $100 SOL)
    final_stretch_min_bond_pct: float = 50.0
    final_stretch_max_bond_pct: float = 97.0
    migrated_max_age_hours: float = 12.0  # Dex tab: age max 12h (V1)
    migrated_min_mcap_usd: float = 30_000.0  # Dex tab min (V1)
    recon_min_mcap_usd: float = 70_000.0  # Dex Screener recon min (V6)
    recon_max_mcap_usd: float = 11_000_000.0  # V6
    min_vol_5m_usd: float = 2_000.0  # "fine but not optimal"; below is dead (V1)
    good_vol_5m_usd: float = 10_000.0  # what you actually want (V1, V6, V13)
    min_liquidity_usd: float = 5_000.0
    suspicious_boosts: int = 3_500  # ~$20k of boosts is suspicious (V6)

    # --- Holder checklist (guide Part 1 §4) --------------------------------
    max_top10_pct: float = 25.0  # V13 hard line
    warn_top10_pct: float = 15.0  # V6 preferred
    max_dev_pct: float = 1.0  # V13, V17
    max_insider_pct: float = 10.0  # V13
    min_lp_locked_pct: float = 90.0  # "burned 99-100% or locked" (V2, V3, V6)

    # --- Exits --------------------------------------------------------------
    take_initials_multiple: float = 2.0  # sell initials at 2x (V2, V11)
    stop_loss_pct: float = 30.0
    trailing_stop_pct: float = 35.0  # from peak, after initials are out
    time_stop_minutes: float = 45.0  # nothing happened → thesis wrong
    time_stop_min_gain_pct: float = 10.0
    max_hold_hours: float = 12.0  # "hold hours, maybe overnight" (V8)
    rug_liquidity_drop_pct: float = 70.0
    hard_stop_pct: float = 60.0  # floor no stop review can ever hold past
    max_stop_reviews: int = 1  # times a position may be held through its stop
    # Break-even stop: once a coin has run, a winner can't turn into a loss. The stop
    # is the price where selling everything gets the cost back after the sell's fees
    # and slippage (about 1.1-1.3x for $3-10 positions; flat network fees make small
    # ones need more), plus a buffer for price moving between 15s checks.
    breakeven_arm_multiple: float = 1.3  # arm once the peak reaches this...
    breakeven_arm_room_pct: float = 10.0  # ...and sits this far above the stop, so noise doesn't sell at cost
    breakeven_buffer_pct: float = 3.0
    # Fading volume: the crowd is leaving while we're green, so bank some (once per position).
    fade_volume_ratio: float = 0.5  # 5m volume under this x the last hour's average 5m volume
    fade_confirm_sec: float = 60.0  # the fade has to last this long, so one quiet tick doesn't sell
    fade_sell_fraction: float = 0.5
    fade_min_partial_usd: float = 4.0  # a smaller piece sells it all: one more tx (~$0.20) would be >5% of it

    # --- Narrative / attention trading -------------------------------------
    dip_min_drawdown_pct: float = 40.0  # a normal pullback is ~40-50%
    dip_max_drawdown_pct: float = 75.0  # ~70% is deep; past this it's usually dead
    dip_min_peak_mcap_usd: float = 70_000.0  # only dips of coins that proved themselves (V6)
    reentry_window_hours: float = 3.0  # stopped-out coins stay on the watchlist this long

    # --- Loop timing --------------------------------------------------------
    scan_interval_sec: float = 60.0
    monitor_interval_sec: float = 15.0
    reject_cooldown_min: float = 45.0  # don't re-research a rejected token for this long
    max_candidates_per_scan: int = 6

    # --- Brain (Claude) -----------------------------------------------------
    model: str = "claude-opus-5-5"
    effort: str = "medium"  # low | medium | high | xhigh | max
    # Pacing, not a bill: on a Claude plan every call draws on the same usage window
    # you use yourself. 0 = no hourly cap (it runs until the plan's limit, then waits
    # for the reset). Evolvable: Trencher sets its own pace from how its usage goes.
    max_brain_calls_per_hour: int = 0
    claude_cli: str = "claude"  # Claude Code CLI used for BRAIN=subscription
    claude_cli_timeout_sec: float = 300.0
    usage_limit_pause_min: float = 30.0  # stand down this long when the plan limit hits and no reset time is given
    web_research: bool = True  # let Claude search the web/X for scam accusations (V13)
    web_search_max_uses: int = 3
    guide_mode: str = "full"  # full = whole guide in the prompt, cheatsheet = Part 1 only
    lessons_in_prompt: int = 20
    reflect_every_n_trades: int = 5  # how often Claude reviews results and evolves the strategy

    # --- Web crawler: meta radar + project crawler --------------------------
    radar_interval_min: float = 10.0
    meta_summary_interval_min: float = 60.0  # Claude summarizes "what's the meta right now"
    news_feeds: str = (
        "https://news.google.com/rss/search?q=memecoin&hl=en-US&gl=US&ceid=US:en,"
        "https://news.google.com/rss/search?q=solana+meme+coin&hl=en-US&gl=US&ceid=US:en,"
        "https://news.google.com/rss/search?q=pump.fun&hl=en-US&gl=US&ceid=US:en,"
        "https://cointelegraph.com/rss,https://decrypt.co/feed,https://www.coindesk.com/arc/outboundfeeds/rss/"
    )
    telegram_channels: str = ""  # public channel usernames to read via t.me/s/<name>, comma-separated
    reddit_subs: str = "memecoins,solana,CryptoMoonShots"
    crawl_websites: bool = True
    github_token: str = ""  # optional, raises GitHub's 60 req/h anonymous limit

    # --- Read-only JSON API (for other bots, e.g. a chat agent) ---------------
    api_port: int = 0  # 0 = off
    api_host: str = "127.0.0.1"
    api_token: str = ""  # if set, requests need "Authorization: Bearer <token>"

    # --- Claude Duet bridge (see agent/bridge.py) ----------------------------
    duet_sync_dir: str = ""  # git checkout of the shared branch; empty = off
    duet_sync_branch: str = "trencher-live"
    duet_sync_interval_min: float = 15.0
    auto_update: bool = False  # restart on new commits to auto_update_branch
    auto_update_branch: str = "main"
    # Set at runtime by Duet's steer.json, not from the environment.
    pause_new_trades: bool = False
    owner_note: str = ""
    steer_pinned: dict = field(default_factory=dict, repr=False)  # name → value before steering

    # --- Notifications ------------------------------------------------------
    notify_webhook_url: str = ""  # Discord/Slack/any JSON webhook
    telegram_bot_token: str = ""
    telegram_chat_id: str = ""

    # --- Paths --------------------------------------------------------------
    memory_dir: Path = field(default_factory=lambda: ROOT / "memory")
    soul_path: Path = field(default_factory=lambda: ROOT / "SOUL.md")
    guide_path: Path = field(default_factory=lambda: ROOT / "knowledge" / "memecoin-study-guide.txt")

    @classmethod
    def from_env(cls) -> "Config":
        cfg = cls()
        for f in fields(cls):
            raw = os.environ.get(f.name.upper())
            if raw is None or raw == "":
                continue
            current = getattr(cfg, f.name)
            if isinstance(current, dict):
                continue
            if isinstance(current, bool):
                value = raw.strip().lower() in ("1", "true", "yes", "on")
            elif isinstance(current, int):
                value = int(raw)
            elif isinstance(current, float):
                value = float(raw)
            elif isinstance(current, Path):
                value = Path(raw)
            else:
                value = raw
            setattr(cfg, f.name, value)
        cfg.memory_dir.mkdir(parents=True, exist_ok=True)
        cfg.apply_strategy()
        return cfg

    # --- Evolving strategy --------------------------------------------------
    def apply_strategy(self) -> dict:
        """Load the parameters Trencher has evolved for itself (memory/strategy.json).
        Values you set explicitly in the environment always win."""
        path = self.memory_dir / "strategy.json"
        if not path.exists():
            return {}
        applied = {}
        for name, value in json.loads(path.read_text()).items():
            if name in EVOLVABLE and not os.environ.get(name.upper()) and name not in self.steer_pinned:
                lo, hi = EVOLVABLE[name]
                setattr(self, name, min(hi, max(lo, float(value))))
                applied[name] = getattr(self, name)
        return applied

    def strategy_view(self) -> dict:
        return {name: getattr(self, name) for name in EVOLVABLE}


# Parameters Trencher may retune from its own results, with hard bounds. The
# checklist hard lines and the conviction→risk table are deliberately NOT here.
EVOLVABLE: dict[str, tuple[float, float]] = {
    "stop_loss_pct": (15, 50),
    "max_total_risk_pct": (10, 40),
    "trailing_stop_pct": (20, 55),
    "take_initials_multiple": (1.5, 4),
    "time_stop_minutes": (15, 240),
    "max_hold_hours": (2, 48),
    "dip_min_drawdown_pct": (25, 60),
    "dip_max_drawdown_pct": (50, 80),
    "dip_min_peak_mcap_usd": (40_000, 500_000),
    "good_vol_5m_usd": (3_000, 30_000),
    "min_vol_5m_usd": (1_000, 10_000),
    "final_stretch_min_bond_pct": (30, 90),
    "migrated_max_age_hours": (2, 48),
    "reentry_window_hours": (0.5, 12),
    "max_brain_calls_per_hour": (0, 300),  # 0 = no cap
}

# Settings only the owner may change (through Duet's steer.json), never Trencher
# itself: it shouldn't be able to make its own trades cheaper.
STEERABLE: dict[str, tuple[float, float]] = {
    "platform_fee_pct": (0, 2),
    "pumpfun_curve_fee_pct": (0, 3),
    "other_dex_fee_pct": (0, 3),
    "priority_fee_sol": (0, 0.05),
    "bribe_sol": (0, 0.05),
    "base_slippage_pct": (0, 10),
    "max_slippage_pct": (5, 50),
}
