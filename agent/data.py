"""Free public market data: DexScreener (pairs, boosts, profiles), GeckoTerminal
(candles), RugCheck (authorities, holders, LP), Jupiter (SOL price). No API keys
needed."""

from __future__ import annotations

import logging
import time
from typing import Any

import requests

log = logging.getLogger(__name__)

DEX = "https://api.dexscreener.com"
RUGCHECK = "https://api.rugcheck.xyz/v1"
JUP_PRICE = "https://lite-api.jup.ag/price/v3"
GECKO = "https://api.geckoterminal.com/api/v2"
SOL_MINT = "So11111111111111111111111111111111111111112"

_session = requests.Session()
_session.headers["User-Agent"] = "trencher-paper-agent/1.0"


def _get(url: str, params: dict | None = None, retries: int = 3) -> Any:
    delay = 1.0
    for attempt in range(retries):
        try:
            r = _session.get(url, params=params, timeout=15)
            if r.status_code == 429:
                time.sleep(delay * 3)
                delay *= 2
                continue
            r.raise_for_status()
            return r.json()
        except (requests.RequestException, ValueError) as e:
            if attempt == retries - 1:
                log.warning("GET %s failed: %s", url, e)
                return None
            time.sleep(delay)
            delay *= 2
    return None


# --- Discovery --------------------------------------------------------------

def discover_solana_tokens() -> list[str]:
    """Token addresses that are getting attention right now: fresh DexScreener
    profiles (paid = team is active, V13), latest and top boosts, and tokens
    RugCheck flags as trending."""
    seen: dict[str, None] = {}
    for path in ("/token-boosts/top/v1", "/token-boosts/latest/v1", "/token-profiles/latest/v1"):
        for item in _get(DEX + path) or []:
            if item.get("chainId") == "solana" and item.get("tokenAddress"):
                seen.setdefault(item["tokenAddress"], None)
    for item in _get(RUGCHECK + "/stats/trending") or []:
        mint = item.get("mint")
        if mint:
            seen.setdefault(mint, None)
    return list(seen)


def get_pairs(token_addresses: list[str]) -> dict[str, dict]:
    """Best (most liquid) Solana pair per token, batched 30 at a time."""
    best: dict[str, dict] = {}
    for i in range(0, len(token_addresses), 30):
        chunk = token_addresses[i : i + 30]
        for pair in _get(f"{DEX}/tokens/v1/solana/{','.join(chunk)}") or []:
            addr = pair.get("baseToken", {}).get("address")
            if not addr or addr not in chunk:
                continue
            liq = (pair.get("liquidity") or {}).get("usd") or 0
            cur = best.get(addr)
            if cur is None or liq > ((cur.get("liquidity") or {}).get("usd") or 0):
                best[addr] = pair
    return best


def search_same_name(symbol: str) -> list[dict]:
    """Other Solana pairs with the same ticker, to spot vamps/copycats (V1, V3)."""
    data = _get(f"{DEX}/latest/dex/search", {"q": symbol}) or {}
    return [
        p for p in data.get("pairs") or []
        if p.get("chainId") == "solana"
        and (p.get("baseToken", {}).get("symbol") or "").lower() == symbol.lower()
    ]


def rugcheck_report(mint: str) -> dict | None:
    return _get(f"{RUGCHECK}/tokens/{mint}/report")


_ohlcv_cache: dict[str, tuple[float, list]] = {}


def recent_candles(pool: str, minutes: int = 15, limit: int = 96) -> list[list[float]]:
    """[ts, open, high, low, close, volume] candles (newest first) from GeckoTerminal.
    Cached 5 min per pool: the free tier allows ~30 calls/min."""
    key = f"{pool}:{minutes}:{limit}"
    hit = _ohlcv_cache.get(key)
    if hit and time.time() - hit[0] < 300:
        return hit[1]
    data = _get(f"{GECKO}/networks/solana/pools/{pool}/ohlcv/minute",
                {"aggregate": minutes, "limit": limit}, retries=2) or {}
    candles = ((data.get("data") or {}).get("attributes") or {}).get("ohlcv_list") or []
    _ohlcv_cache[key] = (time.time(), candles)
    return candles


def price_history(snap: dict) -> dict:
    """Peak in the last ~24h and how far price is off it: the dip/correction view."""
    candles = recent_candles(snap["pair_address"]) if snap.get("pair_address") else []
    price = snap["price_usd"]
    if not candles or not price:
        return {}
    high = max(c[2] for c in candles)
    hours_since_high = (time.time() - max(c[0] for c in candles if c[2] == high)) / 3600
    last_hour = candles[:4]
    return {
        "peak_price_24h": high,
        "peak_mcap_24h": snap["mcap_usd"] * high / price,
        "drawdown_from_peak_pct": round(100 * (1 - price / high), 1) if high else 0,
        "hours_since_peak": round(hours_since_high, 1),
        "low_last_hour": min(c[3] for c in last_hour) if last_hour else None,
        "candles_15m_close_newest_first": [c[4] for c in candles[:16]],
    }


_sol_cache: tuple[float, float] = (0.0, 0.0)


def sol_price_usd() -> float:
    global _sol_cache
    if time.time() - _sol_cache[1] < 60 and _sol_cache[0]:
        return _sol_cache[0]
    data = _get(JUP_PRICE, {"ids": SOL_MINT}) or {}
    price = float((data.get(SOL_MINT) or {}).get("usdPrice") or 0)
    if price:
        _sol_cache = (price, time.time())
        return price
    return _sol_cache[0] or 150.0


# --- Normalized view of a pair ---------------------------------------------

def pair_snapshot(pair: dict) -> dict:
    """Flatten a DexScreener pair into the numbers the agent cares about."""
    info = pair.get("info") or {}
    created = pair.get("pairCreatedAt") or 0
    txns = pair.get("txns") or {}
    vol = pair.get("volume") or {}
    m5 = txns.get("m5") or {}
    hour_avg_5m = float(vol.get("h1") or 0) / 12
    return {
        "address": pair["baseToken"]["address"],
        "name": pair["baseToken"].get("name"),
        "symbol": pair["baseToken"].get("symbol"),
        "pair_address": pair.get("pairAddress"),
        "dex": pair.get("dexId"),
        "url": pair.get("url"),
        "price_usd": float(pair.get("priceUsd") or 0),
        "mcap_usd": float(pair.get("marketCap") or pair.get("fdv") or 0),
        "liquidity_usd": float((pair.get("liquidity") or {}).get("usd") or 0),
        "vol_5m": float(vol.get("m5") or 0),
        "vol_1h": float(vol.get("h1") or 0),
        "vol_24h": float(vol.get("h24") or 0),
        "buys_5m": (txns.get("m5") or {}).get("buys", 0),
        "sells_5m": (txns.get("m5") or {}).get("sells", 0),
        "buys_1h": (txns.get("h1") or {}).get("buys", 0),
        "sells_1h": (txns.get("h1") or {}).get("sells", 0),
        "change_5m": (pair.get("priceChange") or {}).get("m5"),
        "change_1h": (pair.get("priceChange") or {}).get("h1"),
        "change_24h": (pair.get("priceChange") or {}).get("h24"),
        "age_hours": (time.time() * 1000 - created) / 3_600_000 if created else None,
        # Attention: is the crowd arriving or leaving right now?
        "vol_5m_vs_hour_avg": round(float(vol.get("m5") or 0) / hour_avg_5m, 2) if hour_avg_5m else None,
        "buy_ratio_5m": round(m5.get("buys", 0) / (m5.get("buys", 0) + m5.get("sells", 0)), 2)
        if (m5.get("buys", 0) + m5.get("sells", 0)) else None,
        "boosts": (pair.get("boosts") or {}).get("active", 0),
        "has_paid_profile": bool(info.get("header") or info.get("imageUrl")),
        "socials": [s.get("type") or s.get("platform") for s in info.get("socials") or []],
        "social_links": [s.get("url") for s in info.get("socials") or []],
        "websites": [w.get("url") for w in info.get("websites") or []],
    }
