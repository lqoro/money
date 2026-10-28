"""Optional push notifications: any JSON webhook (Discord, Slack, a bot bridge)
and/or Telegram. Silent when nothing is configured."""

from __future__ import annotations

import logging

import requests

from .config import Config

log = logging.getLogger(__name__)


def notify(cfg: Config, text: str) -> None:
    if cfg.notify_webhook_url:
        try:
            # "content" for Discord, "text" for Slack and most bridges.
            requests.post(cfg.notify_webhook_url, json={"content": text[:1900], "text": text}, timeout=10)
        except requests.RequestException as e:
            log.warning("webhook notify failed: %s", e)
    if cfg.telegram_bot_token and cfg.telegram_chat_id:
        try:
            requests.post(
                f"https://api.telegram.org/bot{cfg.telegram_bot_token}/sendMessage",
                json={"chat_id": cfg.telegram_chat_id, "text": text[:4000], "disable_web_page_preview": True},
                timeout=10,
            )
        except requests.RequestException as e:
            log.warning("telegram notify failed: %s", e)
