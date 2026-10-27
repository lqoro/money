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
every 15s  monitor open positions ──► exits: initials at 2x, trail, time stop, rug
           stop hit ──► Claude reviews: bundle exit + narrative alive? hold once : sell
on close   Claude writes a lesson; stopped-out coins go on a re-entry watchlist
every 5    Claude studies its results ──► rewrites learned rules + retunes its strategy
```

1. **Discover**: tokens getting attention right now: DexScreener boosts and
   fresh paid profiles, plus RugCheck trending.
2. **Market filter**: does it fit one of the guide's setups?
   - `FINAL_STRETCH` (V1 strategy 2): pump.fun token still on the curve, 50–97% of
     the way to bond.
   - `MIGRATED` (V1 strategy 3 + V6 recon): graduated, ≤12h old with ≥$30k mcap, or
     $70k–$11M mcap.
   - `DIP` (narrative/attention): a coin that peaked at ≥$70k, now 40–75% off its
     recent high (24h candles from GeckoTerminal plus its own price tracking),
     with attention still alive. A dip with fading volume fails as a falling knife.
   - At least $2k of 5-minute volume (the guide wants $10k).
   - Every dossier carries attention numbers: 5-minute volume vs the hour's
     average (crowd arriving or leaving) and the 5-minute buy ratio.
3. **Checklist** (`agent/checklist.py`): the guide's pre-trade due diligence as
   code. Hard fails: mint/freeze authority live, LP not burned, dev >1%, top 10
   >25% (with the pool excluded), insiders >10%, transfer tax, RugCheck "danger",
   ~$20k of boosts. Warnings: possible vamp (bigger token with the same ticker),
   no X account, top 10 >15%, insider networks, thin liquidity, sellers in control.
4. **Brain** (`agent/brain.py`): Claude gets `SOUL.md` + the full guide (cached),
   its learned rules and recent lessons, the wallet, and the token dossier. It
   can search the web for scam accusations, the project's X and the current meta
   (V13), then answers BUY or PASS with a conviction score, thesis and exit plan as JSON.
5. **Sizing** (`agent/sizing.py`): no fixed bet size. Only risk what you're
   willing to lose (V8): Claude's conviction (1–10, from its due diligence) sets
   how much of equity it's willing to lose if the stop hits, and the stop
   distance sets the size:

   | Conviction | Risk if stopped | Position at a 30% stop, $100 wallet |
   |---|---|---|
   | 1–4 | 0% (pass) | — |
   | 5 | 1% | ~$2.90 |
   | 6 | 1.5% | ~$4.30 |
   | 7 | 2.5% | ~$7.10 |
   | 8 | 4% | ~$11.40 |
   | 9 | 6% | ~$17.10 |
   | 10 | 8% | ~$22.90 |

   A tighter stop means a bigger position for the same risk. Caps: 25% of
   equity in any one position (a rug skips the stop), 15% total at-stop risk
   across open positions. Tune with `CONVICTION_RISK_PCT`, `MAX_POSITION_PCT`,
   `MAX_TOTAL_RISK_PCT`.
6. **Paper fills** (`agent/portfolio.py`): 1% platform fee, 0.001 SOL priority
   fee, and constant-product price impact, so the results aren't fantasy numbers.
   Max 4 open positions; stops opening trades after a 25% day.
7. **Exits** (`agent/risk.py`): sell initials at ~2x, then trail the rest; time
   stop if nothing happens in 45 min; rug detection on liquidity collapse; 12h
   max hold. **A stop is a decision point**: when the −30% stop hits, Claude
   compares holders now vs at entry and checks the narrative. If a bundle came
   out (top 10 / insider share dropped) and attention is still alive, it can
   hold once with a deeper stop and a deadline to reclaim; otherwise it sells.
   The −60% hard floor and rug exits never wait for a review, and a hold must
   still fit the total risk budget (otherwise it trims half).
8. **Re-entry**: coins it got stopped out of (not rugged) stay on a watchlist
   for 3h and get re-scanned; Claude sees why it left and can buy back if the
   narrative held.
9. **Learning and evolving**: after every closed trade Claude writes a lesson to
   `memory/lessons.md`. Every 5 trades (or `python -m agent evolve`) it studies
   its stats by setup, rewrites `memory/learned_rules.md`, and **retunes its own
   strategy parameters** (stop size, dip range, time stops, initials multiple,
   volume bars…) within hard bounds. Changes go to `memory/strategy.json` and are
   logged with reasons in `memory/strategy_log.md`. The checklist hard lines and
   your conviction→risk table can't be evolved, and anything you set in `.env`
   overrides what it learned.

## Run it

```bash
python3 -m venv .venv && .venv/bin/pip install -r requirements.txt
cp .env.example .env          # put your ANTHROPIC_API_KEY in it
set -a; . ./.env; set +a

.venv/bin/python -m agent run --once --dry-run   # one research pass, no trades
.venv/bin/python -m agent run                    # the 24/7 loop
.venv/bin/python -m agent status                 # wallet, positions, lessons, evolved strategy
.venv/bin/python -m agent evolve                 # study results and evolve the strategy now
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
`CONVICTION_RISK_PCT=5:0.5,6:1,7:2,8:3,9:4,10:5`, `EFFORT=high`, `GUIDE_MODE=cheatsheet`).

## What it costs to run

Market data is free (DexScreener, RugCheck, GeckoTerminal, Jupiter). Claude is not. A decision
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
