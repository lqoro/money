"""All tunable numbers in one place.

Defaults come from the Trenches Bootcamp guide (knowledge/memecoin-study-guide.txt).
Every field can be overridden with an env var of the same name in upper case,
e.g. STARTING_CASH_USD=250 or MAX_POSITION_PCT=5.
"""

from __future__ import annotations

import os
from dataclasses import dataclass, field, fields
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent


@dataclass
class Config:
    # --- Wallet ------------------------------------------------------------
    starting_cash_usd: float = 100.0
    max_position_pct: float = 10.0  # % of equity per trade ("size for survival", V8)
    min_position_usd: float = 3.0
    max_open_positions: int = 4
    daily_loss_limit_pct: float = 25.0  # stop opening trades for the day past this drawdown
    broke_equity_usd: float = 5.0  # below this the agent stops trading entirely

    # --- Paper execution model ---------------------------------------------
    platform_fee_pct: float = 1.0  # terminal fee per swap (Axiom/Padre class)
    priority_fee_sol: float = 0.001  # priority + bribe per tx (V2)
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

    # --- Loop timing --------------------------------------------------------
    scan_interval_sec: float = 60.0
    monitor_interval_sec: float = 15.0
    reject_cooldown_min: float = 45.0  # don't re-research a rejected token for this long
    max_candidates_per_scan: int = 6

    # --- Brain (Claude) -----------------------------------------------------
    model: str = "claude-opus-5-5"
    effort: str = "medium"  # low | medium | high | xhigh | max
    max_brain_calls_per_hour: int = 10  # cost cap: ~$0.05-0.15 per decision
    web_research: bool = True  # let Claude search the web/X for scam accusations (V13)
    web_search_max_uses: int = 3
    guide_mode: str = "full"  # full = whole guide in the prompt, cheatsheet = Part 1 only
    lessons_in_prompt: int = 20
    reflect_every_n_trades: int = 10

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
        return cfg
