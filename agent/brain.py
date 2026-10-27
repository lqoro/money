"""The brain: Claude with SOUL.md + the full study guide in its (cached) system
prompt. It researches each candidate that survives the checklist, decides BUY or
PASS with a written exit plan, and writes a lesson after every closed trade.

Without an Anthropic credential the agent falls back to a rules-only brain so
paper trading still runs.
"""

from __future__ import annotations

import json
import logging
import os
import re
import time
from collections import deque

from .checklist import Checklist
from .config import Config
from . import journal
from .risk import default_exit_plan

log = logging.getLogger(__name__)

EXIT_PLAN_SCHEMA = {
    "type": "object",
    "properties": {
        "take_initials_multiple": {"type": "number", "description": "Price multiple at which to sell initials, e.g. 2.0"},
        "stop_loss_pct": {"type": "number", "description": "Exit everything if down this % from entry"},
        "trailing_stop_pct": {"type": "number", "description": "After initials, exit if down this % from the peak"},
        "time_stop_minutes": {"type": "number", "description": "Exit if no progress after this many minutes"},
        "target_mcap_usd": {"type": "number", "description": "Market cap where you sell half the rest; 0 for none"},
    },
    "required": ["take_initials_multiple", "stop_loss_pct", "trailing_stop_pct", "time_stop_minutes", "target_mcap_usd"],
    "additionalProperties": False,
}

DECISION_SCHEMA = {
    "type": "object",
    "properties": {
        "action": {"type": "string", "enum": ["BUY", "PASS"]},
        "verdict": {"type": "string", "description": "One line in Trencher's voice, e.g. 'PASS — top 10 hold 31%. Farm. (V6)'"},
        "conviction": {"type": "integer", "description": "1-10 from your due diligence; this sets the position size"},
        "conviction_reason": {"type": "string", "description": "Why this conviction level and not one higher or lower"},
        "setup": {"type": "string"},
        "meta": {"type": "string", "description": "The narrative/meta this token rides, or 'none'"},
        "thesis": {"type": "string", "description": "Why this trade, in 2-4 sentences, citing V-numbers"},
        "red_flags": {"type": "array", "items": {"type": "string"}},
        "unverified": {"type": "array", "items": {"type": "string"}, "description": "Checklist items you could not verify"},
        "exit_plan": EXIT_PLAN_SCHEMA,
    },
    "required": ["action", "verdict", "conviction", "conviction_reason", "setup", "meta", "thesis", "red_flags", "unverified", "exit_plan"],
    "additionalProperties": False,
}

LESSON_SCHEMA = {
    "type": "object",
    "properties": {"lesson": {"type": "string", "description": "Expected / happened / rule for next time, max 3 sentences"}},
    "required": ["lesson"],
    "additionalProperties": False,
}

RULES_SCHEMA = {
    "type": "object",
    "properties": {"rules_markdown": {"type": "string", "description": "Markdown bullet list, at most 15 rules"}},
    "required": ["rules_markdown"],
    "additionalProperties": False,
}


def _cheatsheet(guide: str) -> str:
    start = guide.find("Part 1: Master Cheat Sheet", 1000)
    end = guide.find("Part 2: Glossary", start)
    return guide[start:end] if start != -1 and end != -1 else guide[:40_000]


class Brain:
    def __init__(self, cfg: Config):
        self.cfg = cfg
        self.calls: deque[float] = deque()
        self.web_ok = cfg.web_research
        mode = os.environ.get("BRAIN", "auto").lower()
        has_key = bool(os.environ.get("ANTHROPIC_API_KEY") or os.environ.get("ANTHROPIC_AUTH_TOKEN"))
        self.use_claude = mode == "claude" or (mode == "auto" and has_key)
        self.client = None
        if self.use_claude:
            import anthropic

            self.anthropic = anthropic
            self.client = anthropic.Anthropic(max_retries=3)
            guide = cfg.guide_path.read_text()
            if cfg.guide_mode == "cheatsheet":
                guide = _cheatsheet(guide)
            self.system = [{
                "type": "text",
                "text": cfg.soul_path.read_text()
                + "\n\n=====================================================\n"
                + "# YOUR EDUCATION: Trenches Bootcamp study guide (full text)\n"
                + "=====================================================\n\n"
                + guide,
                # Soul + guide never change between calls: cache them for an hour.
                "cache_control": {"type": "ephemeral", "ttl": "1h"},
            }]
        log.info("Brain mode: %s", f"Claude ({cfg.model})" if self.use_claude else "rules-only (no ANTHROPIC_API_KEY)")

    # ------------------------------------------------------------ budget
    def has_budget(self) -> bool:
        if not self.use_claude:
            return True
        now = time.time()
        while self.calls and now - self.calls[0] > 3600:
            self.calls.popleft()
        return len(self.calls) < self.cfg.max_brain_calls_per_hour

    # ------------------------------------------------------------ Claude call
    def _ask(self, prompt: str, schema: dict, effort: str, web: bool) -> dict | None:
        self.calls.append(time.time())
        messages: list[dict] = [{"role": "user", "content": prompt}]
        tools = []
        if web and self.web_ok:
            tools = [{"type": "web_search_20260209", "name": "web_search", "max_uses": self.cfg.web_search_max_uses}]
        kwargs = dict(
            model=self.cfg.model,
            max_tokens=16000,
            system=self.system,
            output_config={"effort": effort, "format": {"type": "json_schema", "schema": schema}},
            # On a safety decline, let the API re-run the request on its recommended fallback model.
            betas=["server-side-fallback-2026-07-01"],
            fallbacks="default",
        )
        if tools:
            kwargs["tools"] = tools
        a = self.anthropic
        try:
            so_far: list = []
            for _ in range(4):  # web search can pause a long turn; resume it
                resp = self.client.beta.messages.create(messages=messages, **kwargs)
                if resp.stop_reason != "pause_turn":
                    break
                so_far.extend(resp.content)
                messages = [messages[0], {"role": "assistant", "content": so_far}]
        except a.BadRequestError as e:
            if tools:
                log.warning("Request with web search rejected (%s); continuing without web research", e.message)
                self.web_ok = False
                return self._ask(prompt, schema, effort, web=False)
            log.error("Claude rejected the request: %s", e.message)
            return None
        except a.RateLimitError:
            log.warning("Claude rate limited; skipping this decision")
            return None
        except (a.APIStatusError, a.APIConnectionError) as e:
            log.warning("Claude call failed: %s", e)
            return None

        u = resp.usage
        log.debug("usage in=%s cache_read=%s cache_write=%s out=%s", u.input_tokens,
                  u.cache_read_input_tokens, u.cache_creation_input_tokens, u.output_tokens)
        if resp.stop_reason == "refusal":
            log.warning("Claude declined this request")
            return None
        if resp.stop_reason == "max_tokens":
            log.warning("Claude hit max_tokens; ignoring partial answer")
            return None
        text = next((b.text for b in reversed(resp.content) if b.type == "text"), "")
        try:
            return json.loads(text)
        except json.JSONDecodeError:
            m = re.search(r"\{.*\}", text, re.S)
            try:
                return json.loads(m.group(0)) if m else None
            except json.JSONDecodeError:
                log.warning("Could not parse Claude's answer: %.200s", text)
                return None

    # ------------------------------------------------------------ decisions
    def decide(self, snap: dict, check: Checklist, portfolio_view: dict, sizing_text: str) -> dict:
        if not self.use_claude:
            return self._rules_decide(snap, check)

        rules = journal.learned_rules(self.cfg) or "(none yet: you haven't closed enough trades)"
        lessons = "\n".join(journal.recent_lessons(self.cfg, self.cfg.lessons_in_prompt)) or "(none yet)"
        web_note = (
            "You may use web_search (a few queries at most) to check the token on X and the web: "
            "scam accusations against the dev or CA (V13), whether the CA appears on the project's own X, "
            "whether a political figure pushed it, and what the current meta is."
            if self.web_ok else "Web research is off for this run; work from the dossier."
        )
        prompt = f"""Time (UTC): {time.strftime('%Y-%m-%d %H:%M')}

## Your learned rules
{rules}

## Your recent lessons
{lessons}

## Your paper wallet
{json.dumps(portfolio_view, indent=1)}

## How your conviction becomes a position size
Only risk what you're willing to lose (V8). Your conviction sets how much of the wallet
you'd lose if the stop is hit; your stop distance then sets the size. Right now:
{sizing_text}
A tighter stop means a bigger position for the same risk, so put the stop where the
thesis is actually wrong, never just to size up. A rug skips the stop, so a single
position is also capped at {self.cfg.max_position_pct:g}% of equity.

Conviction scale:
  1-4  not enough edge → PASS (risks nothing)
  5-6  clears the hard lines, but key items are unverified, the idea is so-so, or the meta is crowded
  7-8  clean holders, organic $10k+ 5m flow, an original idea on a live meta, community checks out
  9-10 everything lines up (V6) and you can name why it runs from here; rare

## Candidate dossier
Market data (DexScreener):
{json.dumps(snap, indent=1, default=str)}

Automated checklist (guide Part 1 §4) — it already passed every hard line:
{json.dumps(check.as_dict(), indent=1)}

Not available to you from this data: bundler %, chart-start candles, trades-panel icons,
global fees paid, pro-trader ratio, X admin identity. Treat them as unverified risk.

## Task
{web_note}
Then decide BUY or PASS as Trencher. Passing is a position (V6). If BUY, rate your
conviction honestly (it sets the size) and write the exit plan before the entry (V1, V11)."""
        out = self._ask(prompt, DECISION_SCHEMA, self.cfg.effort, web=True)
        if out is None:
            return {"action": "PASS", "verdict": "PASS — brain unavailable, not trading blind.",
                    "exit_plan": default_exit_plan(self.cfg), "thesis": "", "red_flags": [], "conviction": 0}
        return out

    def _rules_decide(self, snap: dict, check: Checklist) -> dict:
        score = check.score
        buy = check.passed and score >= 68 and snap["vol_5m"] >= self.cfg.good_vol_5m_usd * 0.5
        # Map the checklist score to conviction; rules alone never reach 9-10.
        conviction = min(8, max(1, round((score - 20) / 8))) if buy else min(4, round(score / 20))
        return {
            "action": "BUY" if buy else "PASS",
            "verdict": (f"BUY — {check.setup}, checklist score {score}, conviction {conviction}/10" if buy
                        else f"PASS — checklist score {score} with {len(check.warns)} warning(s)"),
            "conviction": conviction,
            "conviction_reason": f"rules-only: checklist score {score}",
            "setup": check.setup,
            "meta": "unknown (rules-only mode)",
            "thesis": "; ".join(check.plusses) or "rules-only",
            "red_flags": check.warns,
            "unverified": [],
            "exit_plan": default_exit_plan(self.cfg),
        }

    # ------------------------------------------------------------ learning
    def reflect(self, trade: dict) -> str:
        if not self.use_claude or not self.has_budget():
            pnl = trade["pnl_usd"]
            return (f"{trade['symbol']} ({trade['setup']}): {'won' if pnl > 0 else 'lost'} ${abs(pnl):.2f} "
                    f"({trade['pnl_pct']:+.0f}%), exit: {trade['exit_reasons'][-1]}.")
        prompt = f"""A paper trade just closed. Write one lesson for your lessons file.

Trade record:
{json.dumps(trade, indent=1, default=str)}

Your learned rules so far:
{journal.learned_rules(self.cfg) or '(none yet)'}

Say what you expected, what happened, and the concrete rule you will follow next time.
Cite the guide (V-numbers) when the lesson confirms or contradicts it. Max 3 sentences."""
        out = self._ask(prompt, LESSON_SCHEMA, "low", web=False)
        return (out or {}).get("lesson") or f"{trade['symbol']}: {trade['pnl_pct']:+.0f}% — no reflection available."

    def condense_rules(self, trades: list[dict]) -> str | None:
        if not self.use_claude or not self.has_budget():
            return None
        lessons = "\n".join(journal.recent_lessons(self.cfg, 200))
        wins = sum(1 for t in trades if t.get("pnl_usd", 0) > 0)
        by_setup: dict[str, list[float]] = {}
        for t in trades:
            by_setup.setdefault(t.get("setup", "?"), []).append(t.get("pnl_usd", 0))
        stats = {k: {"trades": len(v), "pnl_usd": round(sum(v), 2), "win_rate": round(sum(x > 0 for x in v) / len(v), 2)}
                 for k, v in by_setup.items()}
        prompt = f"""Time to study your own results and update your learned rules.

Closed trades: {len(trades)}, wins: {wins}
By setup: {json.dumps(stats)}

All your lessons:
{lessons}

Current learned rules:
{journal.learned_rules(self.cfg) or '(none yet)'}

Rewrite your learned rules: at most 15 short, concrete bullets that change how you trade
(thresholds, setups to favor or avoid, timing, exits). Keep rules your data supports, drop
ones it doesn't. Never loosen the hard lines in your soul."""
        out = self._ask(prompt, RULES_SCHEMA, "high", web=False)
        return (out or {}).get("rules_markdown")
