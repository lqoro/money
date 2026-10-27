"""Project crawler: visits a token's own website and linked GitHub to run the
guide's web checks automatically.

- Does the site show THIS contract address, or a different one? (vamps, V1/V3)
- How old is the domain? (V3)
- Tech/AI claims with no live GitHub work are probably a LARP (V1).

It never runs JavaScript, never connects a wallet, respects robots.txt, caps
download size, and treats everything it reads as untrusted data.
"""

from __future__ import annotations

import ipaddress
import json
import logging
import re
import socket
import time
from datetime import datetime, timezone
from urllib import robotparser
from urllib.parse import urljoin, urlparse

import requests

from .config import Config
from .radar import SOLANA_ADDR, UA, _fetch, html_to_text

log = logging.getLogger(__name__)

TECH_WORDS = re.compile(r"\b(ai|agent|agents|protocol|platform|dashboard|sdk|api|infrastructure|layer|"
                        r"launchpad|bot|framework|dapp|utility)\b", re.I)
GITHUB_REPO = re.compile(r"https?://(?:www\.)?github\.com/([\w.-]+)/([\w.-]+)", re.I)
SKIP_HOSTS = ("x.com", "twitter.com", "t.me", "telegram.me", "discord.gg", "discord.com", "dexscreener.com",
              "pump.fun", "tiktok.com", "instagram.com", "youtube.com")

_cache: dict[str, tuple[float, dict]] = {}


def is_public_url(url: str) -> bool:
    """Token websites are attacker-controlled: never let one point the crawler at
    localhost, the LAN or a cloud metadata endpoint."""
    parts = urlparse(url)
    if parts.scheme not in ("http", "https") or not parts.hostname:
        return False
    try:
        infos = socket.getaddrinfo(parts.hostname, parts.port or (443 if parts.scheme == "https" else 80))
    except (socket.gaierror, UnicodeError):
        return False
    return all(ipaddress.ip_address(info[4][0]).is_global for info in infos)


def safe_fetch(url: str, timeout: float = 12, max_bytes: int = 1_000_000) -> str | None:
    """GET with every redirect hop checked against is_public_url."""
    for _ in range(4):
        if not is_public_url(url):
            return None
        try:
            r = requests.get(url, headers={"User-Agent": UA}, timeout=timeout, stream=True, allow_redirects=False)
        except requests.RequestException:
            return None
        if r.is_redirect or r.status_code in (301, 302, 303, 307, 308):
            url = urljoin(url, r.headers.get("location", ""))
            continue
        if r.status_code != 200:
            return None
        try:
            return r.raw.read(max_bytes, decode_content=True).decode(r.encoding or "utf-8", errors="replace")
        except Exception:
            return None
    return None


def _allowed(url: str) -> bool:
    parts = urlparse(url)
    rp = robotparser.RobotFileParser()
    try:
        robots = f"{parts.scheme}://{parts.netloc}/robots.txt"
        if not is_public_url(robots):
            return False
        r = requests.get(robots, headers={"User-Agent": UA}, timeout=6, allow_redirects=False)
        if r.status_code != 200:
            return True
        rp.parse(r.text.splitlines())
        return rp.can_fetch(UA, url)
    except requests.RequestException:
        return True


def domain_age_days(host: str) -> float | None:
    """Registration age from RDAP (the free successor to WHOIS)."""
    labels = host.lower().split(".")
    domain = ".".join(labels[-2:]) if len(labels) >= 2 else host
    raw = _fetch(f"https://rdap.org/domain/{domain}", timeout=10, max_bytes=300_000)
    try:
        for ev in json.loads(raw or "{}").get("events", []):
            if ev.get("eventAction") == "registration":
                reg = datetime.fromisoformat(ev["eventDate"].replace("Z", "+00:00"))
                return round((datetime.now(timezone.utc) - reg).total_seconds() / 86400, 1)
    except (ValueError, KeyError):
        pass
    return None


def github_repo(owner: str, repo: str, token: str = "") -> dict:
    headers = {"User-Agent": UA, "Accept": "application/vnd.github+json"}
    if token:
        headers["Authorization"] = f"Bearer {token}"
    try:
        r = requests.get(f"https://api.github.com/repos/{owner}/{repo.removesuffix('.git')}", headers=headers, timeout=10)
        if r.status_code != 200:
            return {"repo": f"{owner}/{repo}", "error": f"HTTP {r.status_code}"}
        d = r.json()
        pushed = datetime.fromisoformat(d["pushed_at"].replace("Z", "+00:00"))
        created = datetime.fromisoformat(d["created_at"].replace("Z", "+00:00"))
        now = datetime.now(timezone.utc)
        return {
            "repo": d.get("full_name"),
            "stars": d.get("stargazers_count"),
            "forks": d.get("forks_count"),
            "days_since_push": round((now - pushed).total_seconds() / 86400, 1),
            "repo_age_days": round((now - created).total_seconds() / 86400, 1),
            "is_fork": d.get("fork"),
        }
    except (requests.RequestException, ValueError, KeyError) as e:
        return {"repo": f"{owner}/{repo}", "error": str(e)[:80]}


def crawl_site(url: str, token_address: str) -> dict:
    host = urlparse(url).netloc.lower()
    out: dict = {"url": url, "host": host}
    if urlparse(url).scheme not in ("http", "https") or any(host.endswith(h) for h in SKIP_HOSTS):
        out["skipped"] = "not a project website"
        return out
    if not is_public_url(url):
        out["skipped"] = "not a public internet address"
        return out
    if not _allowed(url):
        out["skipped"] = "robots.txt disallows crawling"
        return out
    raw = safe_fetch(url)
    if raw is None:
        out["reachable"] = False
        return out
    text = html_to_text(raw)
    title = re.search(r"<title[^>]*>(.*?)</title>", raw, re.S | re.I)
    addrs = set(SOLANA_ADDR.findall(raw))
    links = {urljoin(url, h) for h in re.findall(r'href=["\']([^"\']+)["\']', raw)}
    out.update({
        "reachable": True,
        "title": (title.group(1).strip()[:120] if title else ""),
        "text_excerpt": text[:1200],
        "shows_this_ca": token_address in raw,
        # Base58 strings that look like other token addresses (skip SOL / common program ids).
        "other_addresses": sorted(a for a in addrs if a != token_address and not a.startswith("So111")
                                  and not a.startswith("Token") and not a.startswith("1111"))[:5],
        "github_links": sorted({f"{m.group(1)}/{m.group(2)}" for l in links if (m := GITHUB_REPO.match(l))})[:3],
        "tech_claims": sorted({w.lower() for w in TECH_WORDS.findall(text)})[:8],
        "domain_age_days": domain_age_days(host),
    })
    return out


def project_report(snap: dict, cfg: Config) -> dict:
    """Crawl the token's websites (max 2) and any GitHub repos they link."""
    if not cfg.crawl_websites:
        return {}
    addr = snap["address"]
    hit = _cache.get(addr)
    if hit and time.time() - hit[0] < 1800:
        return hit[1]
    links = [u for u in (snap.get("websites") or []) + (snap.get("social_links") or []) if u]
    repos = {f"{m.group(1)}/{m.group(2)}" for l in links if (m := GITHUB_REPO.match(l))}
    sites = [crawl_site(u, addr) for u in [u for u in (snap.get("websites") or []) if u and not GITHUB_REPO.match(u)][:2]]
    repos |= {r for s in sites for r in s.get("github_links", [])}
    github = [github_repo(*r.split("/", 1), token=cfg.github_token) for r in sorted(repos)[:2]]
    report = {"websites": sites, "github": github}
    _cache[addr] = (time.time(), report)
    return report
