"""Meta radar: a small web crawler that reads where attention is going.

Every few minutes it reads crypto news feeds, CoinGecko trending, DexScreener
boost blurbs and community takeovers, Reddit and public Telegram channels, then
works out which narratives, tickers and contract addresses keep coming up.
"Be early to the meta, not late" (V1, V5) and "trade the narrative, trade the
attention" need to know what the meta *is*.

Everything here is attention data, not a buy signal: callers farm followers as
exit liquidity (V7).
"""

from __future__ import annotations

import html
import json
import logging
import re
import time
import xml.etree.ElementTree as ET
from collections import Counter
from html.parser import HTMLParser
from pathlib import Path

import requests

from .config import Config

log = logging.getLogger(__name__)

UA = "Mozilla/5.0 (compatible; trencher-paper-agent/1.0; research crawler)"
SOLANA_ADDR = re.compile(r"\b[1-9A-HJ-NP-Za-km-z]{32,44}\b")
TICKER = re.compile(r"\$([A-Za-z][A-Za-z0-9]{1,11})\b")
WORD = re.compile(r"[A-Za-z][A-Za-z0-9'\-]{2,}")
STOP = set("""
the and for with that this from are was were has have had not but you your our its it's they their them his her
will just about into over more than been what when where which while who why how all any can could would should
may might new now out off one two get got after before amid says said say also very much most some such only
crypto coin coins token tokens price prices market markets trading trader traders today week day year news update
https http www com amp via report reports here there make makes made back down still even like bitcoin btc
first every nearly million billion world business finance sent cap launch launches launched know need first
going top best big huge high low rise rises falls fell drop drops gains gain surge surges soars soared crash
crashes crashed hit hits next latest live users says amid could worth buy sell investors analyst analysts
""".split())
# Words that are always present in memecoin chatter: they say nothing about the current meta.
STOP |= set("solana sol meme memes memecoin memecoins pump fun pumpfun dex dexscreener ca contract holders "
            "community takeover cto chart moon gem launchpad".split())


class _Text(HTMLParser):
    def __init__(self):
        super().__init__()
        self.parts: list[str] = []
        self._skip = 0

    def handle_starttag(self, tag, attrs):
        if tag in ("script", "style", "noscript"):
            self._skip += 1

    def handle_endtag(self, tag):
        if tag in ("script", "style", "noscript") and self._skip:
            self._skip -= 1

    def handle_data(self, data):
        if not self._skip and data.strip():
            self.parts.append(data.strip())


def html_to_text(raw: str) -> str:
    p = _Text()
    try:
        p.feed(raw)
    except Exception:  # malformed HTML from random sites
        pass
    return " ".join(p.parts)


def _fetch(url: str, timeout: float = 12, max_bytes: int = 1_500_000) -> str | None:
    try:
        r = requests.get(url, headers={"User-Agent": UA}, timeout=timeout, stream=True)
        if r.status_code != 200:
            return None
        body = r.raw.read(max_bytes, decode_content=True)
        return body.decode(r.encoding or "utf-8", errors="replace")
    except (requests.RequestException, ValueError) as e:
        log.debug("fetch %s failed: %s", url, e)
        return None


# --- Sources -----------------------------------------------------------------

def read_rss(url: str, max_age_h: float = 12) -> list[dict]:
    raw = _fetch(url)
    if not raw:
        return []
    try:
        root = ET.fromstring(raw)
    except ET.ParseError:
        return []
    items = []
    source = re.sub(r"^https?://(www\.)?", "", url).split("/")[0]
    for it in root.iter("item"):
        title = html.unescape((it.findtext("title") or "").strip())
        if "news.google." in url:
            title = re.sub(r"\s+-\s+[^-]{2,60}$", "", title)  # drop the " - Publisher" suffix
        if not title:
            continue
        items.append({"title": title, "source": source, "link": it.findtext("link"),
                      "published": it.findtext("pubDate")})
    return items[:40]


def read_coingecko_trending() -> dict:
    raw = _fetch("https://api.coingecko.com/api/v3/search/trending")
    if not raw:
        return {}
    try:
        d = json.loads(raw)
    except ValueError:
        return {}
    return {
        "coins": [c["item"].get("symbol") for c in d.get("coins", []) if c.get("item")],
        "categories": [c.get("name") for c in d.get("categories", []) if c.get("name")],
    }


def read_dexscreener_blurbs() -> list[str]:
    texts = []
    for path in ("/token-boosts/latest/v1", "/token-profiles/latest/v1", "/community-takeovers/latest/v1"):
        raw = _fetch("https://api.dexscreener.com" + path)
        try:
            for item in json.loads(raw or "[]"):
                if item.get("chainId") == "solana" and item.get("description"):
                    texts.append(item["description"][:400])
        except ValueError:
            continue
    return texts


def read_reddit(sub: str) -> list[dict]:
    raw = _fetch(f"https://www.reddit.com/r/{sub}/new.json?limit=40")
    try:
        posts = json.loads(raw or "{}").get("data", {}).get("children", [])
    except ValueError:
        return []
    return [{"title": p["data"].get("title", ""), "text": (p["data"].get("selftext") or "")[:500],
             "source": f"r/{sub}"} for p in posts if p.get("data")]


def read_telegram(channel: str) -> list[dict]:
    """Public channel preview page (no login, no bot): t.me/s/<channel>."""
    raw = _fetch(f"https://t.me/s/{channel}")
    if not raw:
        return []
    msgs = re.findall(r'class="tgme_widget_message_text[^"]*"[^>]*>(.*?)</div>', raw, re.S)
    return [{"text": html_to_text(m)[:600], "source": f"t.me/{channel}"} for m in msgs[-30:]]


# --- Radar -------------------------------------------------------------------

def _terms(text: str) -> list[str]:
    words = [w.lower().strip("'-") for w in WORD.findall(text)]
    words = [w for w in words if w not in STOP and not w.isdigit() and len(w) > 2]
    words = [w for w in words if not (w.endswith("s") and w[:-1] in STOP)]
    bigrams = [f"{a} {b}" for a, b in zip(words, words[1:])]
    return words + bigrams


def build_radar(cfg: Config, previous: dict | None = None) -> dict:
    """Crawl every source once and score narratives with time decay, so a term
    that keeps coming up across refreshes outranks a one-off."""
    headlines: list[dict] = []
    for url in filter(None, (u.strip() for u in cfg.news_feeds.split(","))):
        headlines += read_rss(url)
    social: list[dict] = []
    for sub in filter(None, (s.strip() for s in cfg.reddit_subs.split(","))):
        social += read_reddit(sub)
    tg: list[dict] = []
    for ch in filter(None, (c.strip().lstrip("@") for c in cfg.telegram_channels.split(","))):
        tg += read_telegram(ch)
    blurbs = read_dexscreener_blurbs()
    trending = read_coingecko_trending()

    texts = ([h["title"] for h in headlines] + [p["title"] + " " + p["text"] for p in social]
             + [m["text"] for m in tg] + blurbs)
    counts = Counter()
    tickers = Counter()
    for t in texts:
        counts.update(set(_terms(t)))
        tickers.update({m.upper() for m in TICKER.findall(t)})

    # Time-decayed scores: half-life of ~1 hour of refreshes.
    prev_scores = (previous or {}).get("_scores", {})
    elapsed_h = (time.time() - (previous or {}).get("updated_at", time.time())) / 3600
    decay = 0.5 ** max(0.0, elapsed_h)
    scores = {k: v * decay for k, v in prev_scores.items() if v * decay > 0.3}
    for term, n in counts.items():
        if n >= 2:  # mentioned by at least two different texts
            scores[term] = scores.get(term, 0) + n

    called: dict[str, dict] = dict((previous or {}).get("called_cas", {}))
    for m in tg + social:
        for addr in set(SOLANA_ADDR.findall(m["text"])):
            entry = called.setdefault(addr, {"count": 0, "sources": [], "first_seen": time.time()})
            entry["count"] += 1
            entry["last_seen"] = time.time()
            if m["source"] not in entry["sources"]:
                entry["sources"].append(m["source"])
    called = {a: v for a, v in called.items() if time.time() - v.get("last_seen", 0) < 6 * 3600}

    top = sorted(scores.items(), key=lambda kv: kv[1], reverse=True)
    return {
        "updated_at": time.time(),
        "sources": {"headlines": len(headlines), "reddit_posts": len(social), "telegram_msgs": len(tg),
                    "dexscreener_blurbs": len(blurbs)},
        "trending_coins": trending.get("coins", []),
        "trending_categories": trending.get("categories", []),
        "top_narratives": [{"term": k, "score": round(v, 1)} for k, v in top[:30]],
        "hot_tickers": [{"ticker": f"${k}", "mentions": v} for k, v in tickers.most_common(20)],
        "called_cas": called,
        "headlines": [{"title": h["title"], "source": h["source"]} for h in headlines[:25]],
        "meta_summary": (previous or {}).get("meta_summary", ""),
        "meta_summary_at": (previous or {}).get("meta_summary_at", 0),
        "scan_movers": (previous or {}).get("scan_movers", []),  # filled in by the agent's own scans
        "scan_movers_at": (previous or {}).get("scan_movers_at", 0),
        "_scores": dict(top[:300]),
        "_texts": texts[:400],  # kept for per-token buzz lookups; not shown to the brain
    }


def scan_movers(snaps: list[dict], n: int = 15, skip=None) -> list[dict]:
    """The coins the market is trading hardest right now, from the agent's own scan:
    the live meta is whatever these have in common, whatever the news says."""
    def row(s: dict) -> dict:
        return {"symbol": s.get("symbol"), "name": s.get("name"), "ca": s.get("address"), "dex": s.get("dex"),
                "mcap_usd": round(s.get("mcap_usd") or 0), "vol_5m": round(s.get("vol_5m") or 0),
                "vol_1h": round(s.get("vol_1h") or 0), "change_1h": s.get("change_1h"),
                "buy_ratio_5m": s.get("buy_ratio_5m"),
                "age_hours": round(s["age_hours"], 1) if s.get("age_hours") is not None else None}
    live = [s for s in snaps if (s.get("vol_1h") or 0) > 0 and not (skip and skip(s))]
    return [row(s) for s in sorted(live, key=lambda s: s.get("vol_1h") or 0, reverse=True)[:n]]


def radar_path(cfg: Config) -> Path:
    return cfg.memory_dir / "narratives.json"


def load_radar(cfg: Config) -> dict:
    path = radar_path(cfg)
    try:
        return json.loads(path.read_text()) if path.exists() else {}
    except ValueError:
        return {}


def save_radar(cfg: Config, radar: dict) -> None:
    radar_path(cfg).write_text(json.dumps(radar))


def public_view(radar: dict, headlines: int = 12) -> dict:
    """What the brain (and the API) sees: no raw texts, no internal scores."""
    if not radar:
        return {}
    return {
        "age_minutes": round((time.time() - radar.get("updated_at", 0)) / 60),
        "meta_summary": radar.get("meta_summary") or "(not summarized yet)",
        "top_narratives": [n["term"] for n in radar.get("top_narratives", [])[:20]],
        "trending_categories": radar.get("trending_categories", [])[:8],
        "trending_coins": radar.get("trending_coins", [])[:15],
        "hot_tickers": radar.get("hot_tickers", [])[:12],
        "headlines": [h["title"] for h in radar.get("headlines", [])[:headlines]],
        "scan_movers": radar.get("scan_movers", [])[:15],
    }


def token_buzz(snap: dict, radar: dict) -> dict:
    """How much the crawled web is talking about this token right now."""
    if not radar:
        return {}
    sym = (snap.get("symbol") or "").lower()
    name = (snap.get("name") or "").lower()
    addr = snap.get("address") or ""
    texts = [t.lower() for t in radar.get("_texts", [])]
    sym_hits = sum(1 for t in texts if sym and (f"${sym}" in t or re.search(rf"\b{re.escape(sym)}\b", t)))
    name_hits = sum(1 for t in texts if len(name) > 3 and name in t)
    called = radar.get("called_cas", {}).get(addr)
    narratives = [n["term"] for n in radar.get("top_narratives", [])[:30]]
    story = f"{name} {sym} {snap.get('description') or ''}".lower()
    fits = [n for n in narratives if re.search(rf"\b{re.escape(n)}\b", story)]
    return {
        "ticker_mentions": sym_hits,
        "name_mentions": name_hits,
        "on_coingecko_trending": sym.upper() in [c.upper() for c in radar.get("trending_coins", []) if c],
        "ca_called_in": called["sources"] if called else [],
        "ca_call_count": called["count"] if called else 0,
        "fits_hot_narratives": fits[:5],
    }
