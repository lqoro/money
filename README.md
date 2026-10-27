# money — Trencher, a 24/7 paper memecoin agent

Trencher is a Solana memecoin trading agent that runs around the clock with a
**$100 paper wallet**. Everything it knows comes from our **Trenches Bootcamp
study guide** (`knowledge/memecoin-study-guide.txt`), and its personality and
hard rules live in **[`SOUL.md`](SOUL.md)**. Claude is its brain.

No real money, wallet or keys are involved. It only simulates trades.

## How it works

```
every 60s  scan ──► market filter ──► checklist ──► Claude research ──► paper BUY
                     (DexScreener)     (RugCheck,      (soul + guide,      (fees +
                                        guide §4)       web search)         slippage)
every 15s  monitor open positions ──► exits: initials at 2x, stop, trail, time stop, rug
on close   Claude writes a lesson ──► every 10 trades: rewrites its learned rules
```

1. **Discover**: tokens getting attention right now: DexScreener boosts and
   fresh paid profiles, plus RugCheck trending.
2. **Market filter**: does it fit one of the guide's setups?
   - `FINAL_STRETCH` (V1 strategy 2): pump.fun token still on the curve, 50–97% of
     the way to bond.
   - `MIGRATED` (V1 strategy 3 + V6 recon): graduated, ≤12h old with ≥$30k mcap, or
     $70k–$11M mcap.
   - At least $2k of 5-minute volume (the guide wants $10k).
3. **Checklist** (`agent/checklist.py`): the guide's pre-trade due diligence as
   code. Hard fails: mint/freeze authority live, LP not burned, dev >1%, top 10
   >25% (with the pool excluded), insiders >10%, transfer tax, RugCheck "danger",
   ~$20k of boosts. Warnings: possible vamp (bigger token with the same ticker),
   no X account, top 10 >15%, insider networks, thin liquidity, sellers in control.
4. **Brain** (`agent/brain.py`): Claude gets `SOUL.md` + the full guide (cached),
   its learned rules and recent lessons, the wallet, and the token dossier. It
   can search the web for scam accusations, the project's X and the current meta
   (V13), then answers BUY or PASS with a size, thesis and exit plan as JSON.
5. **Paper fills** (`agent/portfolio.py`): 1% platform fee, 0.001 SOL priority
   fee, and constant-product price impact, so the results aren't fantasy numbers.
   Max 10% of equity per trade, 4 open positions, stops opening trades after a
   25% day.
6. **Exits** (`agent/risk.py`): sell initials at ~2x, then trail the rest; −30%
   stop; time stop if nothing happens in 45 min; rug detection on liquidity
   collapse; 12h max hold. Claude can tune these per trade within clamps, but it
   can't remove the stop.
7. **Learning**: after every closed trade Claude writes a lesson to
   `memory/lessons.md`. Every 10 trades it studies its stats by setup and
   rewrites `memory/learned_rules.md`. Both go into every future decision.

## Run it

```bash
python3 -m venv .venv && .venv/bin/pip install -r requirements.txt
cp .env.example .env          # put your ANTHROPIC_API_KEY in it
set -a; . ./.env; set +a

.venv/bin/python -m agent run --once --dry-run   # one research pass, no trades
.venv/bin/python -m agent run                    # the 24/7 loop
.venv/bin/python -m agent status                 # wallet, positions, lessons
.venv/bin/python -m agent reset                  # back to $100 (keeps lessons)
```

Without `ANTHROPIC_API_KEY` it still runs, on a rules-only brain (checklist
score decides). That's useful for testing, but the point is the Claude brain.

### 24/7 hosting

It needs a machine that stays on. Any small VPS works.

- **Docker**: `docker compose up -d --build` (restarts automatically; state is in `./memory`).
- **systemd**: see `deploy/trencher.service`.

Everything it learns lives in `memory/` (state, trade log, decisions, lessons,
learned rules, log file). Back that folder up and it survives restarts.

### Notifications

Set `NOTIFY_WEBHOOK_URL` (Discord, Slack or any JSON webhook) and/or
`TELEGRAM_BOT_TOKEN` + `TELEGRAM_CHAT_ID` to get every buy, sell, lesson and
rule update pushed to you. This is also the hook for wiring Trencher into a
chat bot.

## Settings

Every number is in `agent/config.py`, with the guide video it comes from, and
can be overridden by an env var with the same name in upper case (for example
`MAX_POSITION_PCT=5`, `EFFORT=high`, `GUIDE_MODE=cheatsheet`).

## What it costs to run

Market data is free (DexScreener, RugCheck, Jupiter). Claude is not. A decision
reads ~52k tokens of soul + guide from the prompt cache plus the dossier, and
may run a few web searches: about **$0.05–0.15 per decision** on Claude Opus
5.5. It's capped at `MAX_BRAIN_CALLS_PER_HOUR=10` (≈ $1.50/hour at most) and
only tokens that pass every hard line reach Claude. To spend less: lower the
cap, set `WEB_RESEARCH=false`, `GUIDE_MODE=cheatsheet`, or `MODEL=claude-sonnet-5-5`.

## Known limits

- Free APIs can't see some checklist items: bundler %, chart-start candles,
  trades-panel icons, global fees paid, pro-trader ratio, or who the X admin is.
  Claude is told these are unverified and treats them as risk.
- DexScreener data lags a pro terminal by seconds (V5, V6), so Trencher doesn't
  snipe new pairs.
- Paper fills are an estimate. Real fills in the trenches are usually worse.

## Tests

```bash
.venv/bin/pip install -r requirements-dev.txt
.venv/bin/python -m pytest -q
```

*Nothing here is financial advice. 99% of memecoins go to zero (V13).*
