"""Read-only JSON API so other bots (a chat agent, a dashboard) can ask Trencher
what it's doing. Off unless API_PORT is set. Binds to localhost by default; set
API_TOKEN before exposing it anywhere else.

    GET /status            wallet, open positions, evolved strategy
    GET /meta              the meta radar (what the web is talking about)
    GET /trades?limit=50   recent buys, sells and closes
    GET /lessons           lessons and learned rules
    GET /token/<address>   crawl + checklist on any Solana token (no Claude call)
"""

from __future__ import annotations

import json
import logging
import threading
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from urllib.parse import parse_qs, urlparse

from . import journal, radar
from .config import Config

log = logging.getLogger(__name__)


def start_api(cfg: Config, status_fn, token_fn) -> ThreadingHTTPServer | None:
    if not cfg.api_port:
        return None

    class Handler(BaseHTTPRequestHandler):
        def log_message(self, fmt, *args):  # keep the agent log clean
            log.debug("api: " + fmt, *args)

        def _send(self, code: int, body) -> None:
            data = json.dumps(body, default=str, indent=1).encode()
            self.send_response(code)
            self.send_header("Content-Type", "application/json")
            self.send_header("Content-Length", str(len(data)))
            self.end_headers()
            self.wfile.write(data)

        def do_GET(self):
            if cfg.api_token and self.headers.get("Authorization") != f"Bearer {cfg.api_token}":
                return self._send(401, {"error": "unauthorized"})
            url = urlparse(self.path)
            parts = [p for p in url.path.split("/") if p]
            try:
                if parts == ["status"] or not parts:
                    return self._send(200, status_fn())
                if parts == ["meta"]:
                    return self._send(200, radar.public_view(radar.load_radar(cfg), headlines=25))
                if parts == ["trades"]:
                    limit = int(parse_qs(url.query).get("limit", ["50"])[0])
                    return self._send(200, journal.read_trades(cfg)[-limit:])
                if parts == ["lessons"]:
                    return self._send(200, {"learned_rules": journal.learned_rules(cfg),
                                            "lessons": journal.recent_lessons(cfg, 50)})
                if len(parts) == 2 and parts[0] == "token":
                    result = token_fn(parts[1])
                    return self._send(200 if result else 404, result or {"error": "no Solana pair found"})
                return self._send(404, {"error": "unknown endpoint",
                                        "endpoints": ["/status", "/meta", "/trades", "/lessons", "/token/<address>"]})
            except Exception as e:  # never let a bad request kill the agent
                log.exception("api error")
                return self._send(500, {"error": str(e)})

    server = ThreadingHTTPServer((cfg.api_host, cfg.api_port), Handler)
    threading.Thread(target=server.serve_forever, daemon=True, name="trencher-api").start()
    log.info("JSON API on http://%s:%d (%s)", cfg.api_host, cfg.api_port,
             "token required" if cfg.api_token else "no token")
    return server
