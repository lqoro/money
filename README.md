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

   | Conviction | Risk if stopped | Position at a 30% stop, $100 wallet, SOL $100 |
   |---|---|---|
   | 1–4 | 0% (pass) | — |
   | 5 | 1% | ~$1.60 (under the $2 minimum after fees, so skipped) |
   | 6 | 1.5% | ~$3.00 |
   | 7 | 2.5% | ~$5.70 |
   | 8 | 4% | ~$9.70 |
   | 9 | 6% | ~$15.10 |
   | 10 | 8% | ~$20.50 |

   A tighter stop means a bigger position for the same risk. Caps: 25% of
   equity in any one position (a rug skips the stop), 25% total at-stop risk
   across open positions. Tune with `CONVICTION_RISK_PCT`, `MAX_POSITION_PCT`,
   `MAX_TOTAL_RISK_PCT`.
6. **Paper fills** (`agent/portfolio.py`): prices come from DexScreener; no real
   venue is touched. Every buy and sell pays what the same trade on Axiom would:
   Axiom's 1% fee, the pool's own fee (pump.fun bonding curve 1.25%; PumpSwap
   1.25% down to 0.30% as market cap grows, per pump.fun's fee docs; 0.25% on
   Raydium-style pools), Solana network fees per transaction (0.001 SOL priority +
   0.001 SOL Jito tip + base fee), and slippage (1.5% plus constant-product price
   impact from the pool's liquidity). Sizing counts the flat network fees too, so
   a trade too small to beat its own fees isn't taken. The report breaks fees down
   by kind. The owner can change these through Duet's `steer.json`; Trencher can't.
   **Fee check** (`sizing.fee_check`): after the brain says BUY, code works out
   that trade's real round trip (both fees, network fees and slippage at an
   unchanged price) and only buys if the first profit target pays at least 3x it
   and the round trip costs no more than 20% of the position. A round trip can't
   cost less than ~5.5-7.5% plus ~$0.48, so there's no flat friction cap: at 1.5x
   initials a ~$5 trade on a curve coin is about the smallest that passes, a $2
   one never does. Only the owner can change the two numbers. Fee caps and
   minimum sizes Trencher wrote into its own lessons before this existed are
   marked retired in its prompts, and it's told not to write new ones.
   No limit on how many positions it holds (it has more eyes than a human);
   what limits it is the total at-stop risk budget (25%, which it can evolve
   between 10% and 40%) and cash. It stops
   opening trades after a 25% day.
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
   volume bars, its own Claude call pace…) within hard bounds. Changes go to `memory/strategy.json` and are
   logged with reasons in `memory/strategy_log.md`. The checklist hard lines and
   your conviction→risk table can't be evolved, and anything you set in `.env`
   overrides what it learned.

## Run it

```bash
python3 -m venv .venv && .venv/bin/pip install -r requirements.txt
npm install -g @anthropic-ai/claude-code   # the brain runs on your Claude plan through it
claude setup-token            # once; put the token in .env as CLAUDE_CODE_OAUTH_TOKEN
cp .env.example .env
set -a; . ./.env; set +a

.venv/bin/python -m agent brain                  # check the Claude brain answers

.venv/bin/python -m agent run --once --dry-run   # one research pass, no trades
.venv/bin/python -m agent run                    # the 24/7 loop
.venv/bin/python -m agent status                 # wallet, positions, lessons, evolved strategy
.venv/bin/python -m agent evolve                 # study results and evolve the strategy now
.venv/bin/python -m agent meta                   # crawl the web now, show the meta radar
.venv/bin/python -m agent crawl <address>        # crawl + checklist one token
.venv/bin/python -m agent reset                  # back to $100 (keeps lessons)
```

Without the Claude Code CLI (or an `ANTHROPIC_API_KEY`) it still runs, on a
rules-only brain (checklist score decides). That's useful for testing, but the
point is the Claude brain.

### 24/7 on a Mac mini, steered from Claude Duet

This is the main setup. Trencher runs nonstop on your Mac mini; Claude on your
Max plan makes every call; your Claude Duet channel reads its reports and steers it.

```bash
git clone https://github.com/lqoro/money ~/money && cd ~/money
bash deploy/mac/setup.sh
```

The script makes the Python environment, checks Claude Code is installed and
logged in, sets up the `trencher-live` branch next to the repo, and installs a
launchd job that starts Trencher at login and restarts it if it stops. Keep the
Mac awake (System Settings > Energy).

How it talks to Duet (`agent/bridge.py`): every 15 minutes Trencher pulls the
`trencher-live` branch, applies `steer.json`, and pushes `status.json` and
`REPORT.md`. Duet reads those and writes `steer.json`:

- `pause_new_trades`: stop new buys; open positions are still managed
- `settings`: any setting Trencher could evolve (stop size, dip range, call pace…),
  plus the paper costs (`platform_fee_pct`, `pumpfun_curve_fee_pct`,
  `other_dex_fee_pct`, `priority_fee_sol`, `bribe_sol`, `base_slippage_pct`,
  `max_slippage_pct`) and the fee check (`min_target_cost_multiple`,
  `max_round_trip_cost_pct`), clamped to their bounds. Removing one puts it back.
- `owner_note`: a short note the brain reads before every decision and every
  meta summary
- `goal`: `{"equity_usd": 1000, "deadline": "2026-11-05T05:00:00Z"}`, a stretch
  target the brain sees with its progress; REPORT.md shows how far along it is
  and the daily growth it would take. It never changes sizing or stops.

`REPORT.md` also shows the last scan (how many coins, how many passed the market
filters), the last coins it looked at with why it passed on each (checklist
fail, the brain's verdict, or a size under the minimum) and their CAs, and the
coins moving most in its own scan.

Steering is data, never code, and can't move the hard lines. With
`AUTO_UPDATE=true` (the setup turns it on), Trencher restarts itself on new
code whenever a change is merged to `main`, so fixes made through Duet land
without touching the Mac.

### Other hosting

Any machine that stays on works.

- **Docker**: `docker compose up -d --build` (restarts automatically; state is in `./memory`).
- **systemd**: see `deploy/trencher.service`.

Everything it learns lives in `memory/` (state, trade log, decisions, lessons,
learned rules, log file). Back that folder up and it survives restarts.

### Notifications

Set `NOTIFY_WEBHOOK_URL` (Discord, Slack or any JSON webhook) and/or
`TELEGRAM_BOT_TOKEN` + `TELEGRAM_CHAT_ID` to get every buy, sell, lesson and
rule update pushed to you. This is also the hook for wiring Trencher into a
chat bot.

### Web crawler

Two parts, both free and keyless (`agent/radar.py`, `agent/site.py`):

- **Meta radar**, every 10 min: crypto news RSS (Google News queries for
  memecoin / Solana meme coin / pump.fun, CoinTelegraph, Decrypt, CoinDesk),
  CoinGecko trending coins and categories, DexScreener boost/profile/takeover
  blurbs, Reddit (`REDDIT_SUBS`, where reachable) and public Telegram channels
  you list in `TELEGRAM_CHANNELS` (read from `t.me/s/<channel>`, no bot needed).
  It scores narratives with time decay, counts `$TICKER` mentions, and collects
  contract addresses called in channels; those get scanned too. Every scan
  also keeps the coins trading the most volume right now (`scan_movers`), so the
  meta comes from what the trenches are trading, not only from the news. About
  hourly, Claude writes a one-paragraph "what's the meta right now" summary,
  starting from those movers. All of it goes into every decision. `python -m agent meta` shows it.
- **Project crawler**, per candidate that clears the hard lines: visits the
  token's website(s) and linked GitHub. It flags a site that shows a **different
  contract address** (vamp), a dead site, and **tech/AI claims with no GitHub
  pushed in 30 days** (LARP, V1), and reports domain age from RDAP.
  `python -m agent crawl <address>` runs it on any token.

Safety: it never runs JavaScript or touches a wallet, respects robots.txt, caps
downloads, refuses private/loopback/metadata addresses on every redirect hop,
and passes website text to Claude as clearly marked untrusted data.

### JSON API (for other bots)

Set `API_PORT=8787` and Trencher serves read-only JSON so a chat agent or
dashboard can ask what it's doing: `/status`, `/meta`, `/trades`, `/lessons`,
and `/token/<address>` (crawl + checklist on any token, no Claude call). It binds
to `127.0.0.1` by default; set `API_TOKEN` (sent as `Authorization: Bearer …`)
before exposing it with `API_HOST=0.0.0.0`.

## Settings

Every number is in `agent/config.py`, with the guide video it comes from, and
can be overridden by an env var with the same name in upper case (for example
`CONVICTION_RISK_PCT=5:0.5,6:1,7:2,8:3,9:4,10:5`, `EFFORT=high`, `GUIDE_MODE=cheatsheet`).

## Running on your Claude plan

Market data and the crawler are free (DexScreener, RugCheck, GeckoTerminal,
Jupiter, CoinGecko, RSS). The brain runs on your Claude Pro/Max plan through the
Claude Code CLI (`claude -p`), so there's no per-call bill; what matters is the
plan's usage window, which Trencher shares with your own Claude use.

- **Pacing.** No hourly cap by default. Trencher logs its brain usage
  (`memory/brain_usage.jsonl`: calls, plan-limit hits, coins skipped, stop
  reviews done without the brain) and sets its own `MAX_BRAIN_CALLS_PER_HOUR`
  when it evolves, between 0 (no cap) and 300. Set it in `.env` to pin it.
- **When the limit hits**, the brain stands down until the window resets (or 30
  minutes if Claude doesn't say when) and passes on every coin meanwhile. It never
  buys blind. Open positions are still managed by its rules.
- **What it can do in a call:** web search only. No shell, no files, no fetching
  arbitrary pages, so a malicious coin website has nothing to hijack.
- Each decision reads ~52k tokens of soul + guide from the prompt cache. To make
  each call lighter on your plan: `GUIDE_MODE=cheatsheet`, `WEB_RESEARCH=false`,
  or `MODEL=claude-sonnet-5-5`.
- **API instead:** `BRAIN=api` with `ANTHROPIC_API_KEY` uses the Anthropic API,
  billed per token (about $0.05–0.15 per decision on Opus).

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
