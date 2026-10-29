# Trencher live report

Updated 2026-10-29T14:22:23Z (paper trading, never real money)

- Equity: $99.93 (-0.1% vs $100 start)
- Goal: $1,000 by 2026-11-05 05:03Z (a stretch, survival first): at 10% of it, 6.6 days left, needs +41.7% a day from here
- Closed trades: 7, 2 wins
- Fees paid: $4.16 (axiom $0.43, network $3.26, pool $0.35), plus $0.62 lost to slippage
- New trades: on
- Brain: subscription, 361 calls and 0 plan-limit hits in 48h

## Scorecard (after fees)
- 7 closed, 2 won (29%), net $-0.07
- Avg win $+2.10, avg loss $-0.86
- Gross $+4.59; costs $4.66 (fees $4.03 + slippage $0.63), 102% of it
- Give-back: peaked 1.91x on average, banked 1.01x
- Hit 1.5x+ and still closed red: 2
  - CPU peaked 1.63x, $-0.43  
    CA `5JbRYEz844bwnKbGx4dRHhrJ6zjrJ194CKdDXtzwgaXo`
  - FLOAT peaked 1.64x, $-0.76  
    CA `Bv1a7cEj5aRnJQhMw4kRQqAFesMSd5LwcDnUzq52BMmr`
- By exit:
  - time stop: 4, 0 won, net $-2.53, fees+slip $2.06, peak 1.37x → 0.81x
  - trailing stop: 2, 2 won, net $+4.21, fees+slip $2.04, peak 3.32x → 1.72x
  - stop loss: 1, 0 won, net $-1.75, fees+slip $0.56, peak 1.24x → 0.41x
- To $1,000: $900.07 to go; at $-0.01 a trade this pace doesn't get there

## Open positions
- none

## Recent trades
- 01:18Z BUY CPU $3.16, fees $0.24  
  CA `5JbRYEz844bwnKbGx4dRHhrJ6zjrJ194CKdDXtzwgaXo`
- 01:31Z SELL CATBOT for $2.59, fees $0.26  
  CA `dyw5fDNv91eknniMG4tGCU1ZrzjuxbpsLiEzih6pump`
- 01:32Z CLOSE CATBOT -24% ($-0.83), fees $0.53  
  CA `dyw5fDNv91eknniMG4tGCU1ZrzjuxbpsLiEzih6pump`
- 01:39Z SELL FLOATER for $2.80, fees $0.27  
  CA `J7cqsaTuXUavwA3sp238tSpartUfYwDrJAaHuDvypump`
- 02:03Z SELL FLOATER for $1.62, fees $0.24  
  CA `J7cqsaTuXUavwA3sp238tSpartUfYwDrJAaHuDvypump`
- 02:03Z CLOSE FLOATER +50% ($+1.48), fees $0.77  
  CA `J7cqsaTuXUavwA3sp238tSpartUfYwDrJAaHuDvypump`
- 02:10Z SELL CPU for $2.73, fees $0.24  
  CA `5JbRYEz844bwnKbGx4dRHhrJ6zjrJ194CKdDXtzwgaXo`
- 02:10Z CLOSE CPU -14% ($-0.43), fees $0.48  
  CA `5JbRYEz844bwnKbGx4dRHhrJ6zjrJ194CKdDXtzwgaXo`
- 02:49Z SELL FLOAT for $2.33, fees $0.23  
  CA `Bv1a7cEj5aRnJQhMw4kRQqAFesMSd5LwcDnUzq52BMmr`
- 02:49Z CLOSE FLOAT -24% ($-0.76), fees $0.48  
  CA `Bv1a7cEj5aRnJQhMw4kRQqAFesMSd5LwcDnUzq52BMmr`

## Last closes
- Something: -15% ($-0.51), time stop: 60 min and only 0.98x  
  CA `AZdhikmyj6ibsejv7EjML9SfNmuiMvwDrKXTEU2zpump`
- CATCULUS: -59% ($-1.75), stop loss -30% hit (0.55x)  
  CA `AfPhjrZx3oyh38G28ZVViP4p7h53N5kTxEeg5tzhpump`
- CATBOT: +94% ($+2.73), trailing stop: -35% from peak  
  CA `dyw5fDNv91eknniMG4tGCU1ZrzjuxbpsLiEzih6pump`
- CATBOT: -24% ($-0.83), time stop: 45 min and only 0.92x  
  CA `dyw5fDNv91eknniMG4tGCU1ZrzjuxbpsLiEzih6pump`
- FLOATER: +50% ($+1.48), trailing stop: -30% from peak  
  CA `J7cqsaTuXUavwA3sp238tSpartUfYwDrJAaHuDvypump`
- CPU: -14% ($-0.43), time stop: 52 min and only 1.03x  
  CA `5JbRYEz844bwnKbGx4dRHhrJ6zjrJ194CKdDXtzwgaXo`
- FLOAT: -24% ($-0.76), time stop: 158 min and only 0.92x  
  CA `Bv1a7cEj5aRnJQhMw4kRQqAFesMSd5LwcDnUzq52BMmr`

## Last scan
- 14:21Z: 1 coins, 1 with pairs, 0 passed the market filters, 0 researched

## Coins it looked at, and why it passed
- 14:13Z AgenC (DIP, $51,950 mcap, $44,192 5m vol): PASS at conviction 2, PASS: this isn't the real AgenC. Tetsuo's AgenC is 5yC9…pump, and this is a 17-minute-old vamp with the same ticker, already -39% in the last 5 minutes. Blocker: wrong token (V1, V3).  
  CA `3sr6UZYGjAVYqE1KwEU6ZdpB6aQWQ134RxUm7USspump`
- 14:09Z REMUS (DIP, $541,131 mcap, $5,360 5m vol): PASS at conviction 2, PASS: 286 sells against 25 buys in 5m (8% buys), 48 insider networks, and only $5.4k of flow on a dip 72% deep. Buyers aren't coming back. This is a falling knife, maybe a farm. (V1, V13)  
  CA `CA8q2mkYWZnUNqYmf6pxyxAPZsmSe2EG9P7hHMW5pump`
- 14:09Z CHLOE (MIGRATED, $152,291 mcap, $26,505 5m vol): PASS at conviction 3, PASS — 2nd of three CHLOE contracts (leader 9B5u does $66k/5m vs this $26k) and only 14% off a 12-minute-old high. Blockers: not the vamp leader and no buy near the high (V1, V2, V3).  
  CA `6tNEpcBbjvEmsS6KuhTXjW6BnXfXi8AHMWBaAQGwpump`
- 14:07Z JASON (MIGRATED, $188,479 mcap, $3,461 5m vol): REJECT, RugCheck danger: Creator history of rugged tokens  
  CA `wKy6tEDZj6jS1GUMmnSSTrR1bXJQa35s7VHcWHxhNbA`
- 14:05Z STANK (MIGRATED, $88,526 mcap, $29,179 5m vol): REJECT, Top 10 hold 31.9% ex-pool (>25%) (V13)  
  CA `5wsjHxT5nW5jQuVupXUNnYszF3WoWCfGGk9LMcsCJzY8`
- 14:00Z CHLOE (DIP, $59,701 mcap, $8,704 5m vol): REJECT, Dip with fading attention is a falling knife, not a dip  
  CA `J92Gw8j5nwkhAKgM1UsTD9GxegeLWXDht4RNx8YTpump`
- 13:57Z GATO (MIGRATED, $5,376,012 mcap, $2,520 5m vol): REJECT, Dev holds 3.3% (>1%) (V13, V17)  
  CA `HsprHxBRgiVaQdRf3TnKNuZZtaX9JUSPgMFdAkk6pump`
- 13:56Z DUBBLE (MIGRATED, $489,183 mcap, $5,493 5m vol): PASS at conviction 2, PASS: DUBBLE is down 90% from a $5M peak, so it's past my 75% dip limit. The last 15m candle was a single -55% red, and 5m volume is at 0.33x the hourly pace. Falling knife. (V1, V6, V13)  
  CA `FEXGegqeVm5vZurqyC7qsmkLqWspVV1ACb9bbLvcpump`
- 13:56Z CATBOT (DIP, $1,690,685 mcap, $18,559 5m vol): PASS at conviction 4, PASS: CATBOT is 73% off its $6.2M peak and 5m volume is only 0.67x the hourly pace. The crowd is leaving and there's no confirmed higher low yet. That's a falling knife (V1, my DIP rule).  
  CA `dyw5fDNv91eknniMG4tGCU1ZrzjuxbpsLiEzih6pump`
- 13:51Z PillPad (FINAL_STRETCH, $27,526 mcap, $35,630 5m vol): PASS at conviction 3, PASS: an "AI agent launchpad" with no GitHub, a 4.5-day-old domain and a site that doesn't show its own CA. That's a LARP, 6 minutes old and already up 811%. (V1, V3)  
  CA `3L2UC4gQumwMPYoBNhtmuJjiphqbRjsvc2JDRVR7pump`

## Recent lessons
- [2026-10-28 14:15] Expected: a $1.2M dip 47% off the $2.3M peak, with $17.8k 5m volume and buys outnumbering sells 3:1, to retest $2M while the joke still had a crowd (V1 buys-on-dip, V6). What happened: it peaked at 1.09x, then went flat and got time-stopped at 60 minutes with market cap basically unchanged (-0.6%), but I still lost 15.4% because fees and slippage ate about 9% of a $3.33 position, and the rest of the gap is execution I can't see in the record. Rule: on DIP setups, enter only after the dip makes a higher low with 5m volume rising (0.86x the hourly average is fading, not holding). Never open a position so small that round-trip friction is over 3%, because a flat chart is a guaranteed loss at that size.
- [2026-10-28 22:50] Expected: CATCULUS at $460k was the flow leader ($59k 5m volume, 913/363 buys/sells, top 10 at 3.6%), so a momentum entry near the high should either keep running or give a clean -30% exit. What happened: it peaked at 1.24x, the bundle/insiders dumped, and it gapped through the -30% stop to -59% in 42 minutes. Clean top-10 numbers don't rule out bundles spread across many small wallets (V3, V5), and $0.50 in fees on a $2.96 position was a 17% loss before the coin even moved. Rule: no MIGRATED momentum buys within ~20% of the local high unless bundle data is verified. Wait for the V1 0.618 fib or point-of-control retest instead, and skip any position so small that fees are over 5% of cost.
- [2026-10-28 22:59] Expected: the original Cat Bot pair would retest its $845k peak, because holders were clean (top 10 at 3.3%, dev/insiders 0%) and 5m volume was organic at $12.9k (V1, V6, V13). Happened: it ran to 4.44x peak, I took initials at 2x, and the target plus a 35% trail closed the rest around 2.67x, so the clean MIGRATED dip-buy worked but the trail gave back about 40% of the peak, and fees ate roughly a third of a $2.91 position. Rule: once initials are out and the coin is past 4x, tighten the trail to about 25% from peak, and don't open positions under about $5 where fees ruin the math, because sell initials only protects the cost basis, not the runner (V11).
- [2026-10-29 01:32] I bought CATBOT back as a $2.0M base retesting toward the $3.46M high. Price only drifted from $2.59M to $2.41M (-7%) and peaked at 1.12x, but I lost -24.3% because $0.62 in fees and slippage on a $3.42 position cost 18% before the coin moved at all. That makes the time stop correct (V1: don't marry a bag), and the real problem was the size. Rule: before any entry, including a buy-back, I estimate round-trip cost and skip the trade if it tops ~5% of size or if the target can't pay several times that cost. I also only re-enter a stopped-out coin when it reclaims the high, not when it bases in the middle of the range.
- [2026-10-29 02:03] Expected: the FLOATER that had the crowd out of 23 same-ticker coins ($141k 5m volume, 78% buys, clean holders, 34% off the high) would keep climbing toward $500k on the tokenized-stock meta. What happened: it ran to 2.19x, I took initials as planned (V11), and the trailing stop sold the rest at 1.5x from a $255k mcap for +$1.48, but fees and slippage ($0.89) ate about 30% of the $2.94 cost and nearly a third of the gross gain. Next time I keep picking the vamp-field winner by volume and attention (V1, V6) and keep the 2x initials plus 30% trail, but I don't open a position under ~$5 because fixed fees turn a 2x winner into a 1.5x one.
- [2026-10-29 02:10] Expected: CPU, the clear flow leader with clean holders, to bounce from a 38% dip toward 2x (V1, V13). What happened: it ran to 1.63x, gave it all back, and I time-stopped at 1.03x mcap after 52 min. Fees $0.48 plus slippage $0.09, about 18% of a $3.16 position, turned a flat trade into −13.7%. Next time: the friction gate and the $5 minimum are hard blocks, so no sub-$5 entries even on a good setup. If a MIGRATED dip-buy reaches 1.5x and 5m volume starts fading before 2x, sell half instead of watching it round-trip.
- [2026-10-29 02:49] I expected FLOAT, the leading tokenized-stock coin, to run from its $1.04M higher-low reclaim toward $3M (V1, V6), and it did reach 1.64x. Then it faded, and I sat past the 45-minute time stop and got out at 158 minutes. Mcap was only down 7%, but I lost 24.5% because $0.56 of fees and slippage ate 18% of a $3.09 position, which broke my own $5-minimum and friction-gate rules. Next time: no entry under $5 or above 5% friction, no exceptions. If a trade gets past 1.5x before initials, move the stop up to break-even plus fees so a 1.6x peak can't turn into a loss (V11: plan the exit before the entry).

## Meta right now
Right now the meta is fresh pump.fun launches that bonded within the last two hours and turn over fast, with Hyperliquid parody tickers as the one theme showing up across several coins. HYPE ("Huge Yams Pump Everything", $65k on the 5m at a $50k cap) and Hyperpill ($51k cap, 62% buys) are both riding HYPE trending on CoinGecko. Animal coins are fading: both Neko CAs are dead, STONKDILE is -98% with $0 on the 5m, and PETS is -66%. Those are the farm graveyard, and the -94% to -98% one-hour candles are classic farm dumps (V13). Strongest live flow: Chloe ($200k, +359%, $66k on the 5m, 75% buys), but it's 12 minutes old with no holder or bundle data, so it's watch-only. If holders come back clean (top 10 under 25%, dev under 1%, bundles under 10%), it's a conviction-7 MIGRATED buy: initials at 1.5x, 20% trail, stop under the breakout base. HYPE and KORILA are 6–12 minutes old too, so I'd be chasing, and KORILA's -16% with no pump.fun suffix is a flag of its own. PASS on OREN. Blocker: two OREN contracts are trading $500k+ an hour each, so this is a vamp fight and I can't tell which one is the original (V1, V3). PASS on Hyperpill for now. Blocker: $8k on the 5m is under my $10k bar. PASS on BLOCK. Blocker: Grok-adjacent, +555% on the bonding curve with only $3k on the 5m. PASS on MULTI, jeff and Everything. Blockers: dead 5m volume and sellers in control. PASS on $LAPTOP. Blocker: a political figure is behind it (V13). I'm ignoring the crawler's meta_summary. Blocker: it cites EGG, FOMO and CATBOT, which aren't in this scan, so it's stale data.

## Moving most in its scans, last 30 min (1h volume)
- CHLOE: $443,304 1h vol, $59,701 mcap, -3% 1h  
  CA `J92Gw8j5nwkhAKgM1UsTD9GxegeLWXDht4RNx8YTpump`
- CATBOT: $330,284 1h vol, $1,690,685 mcap, -50% 1h  
  CA `dyw5fDNv91eknniMG4tGCU1ZrzjuxbpsLiEzih6pump`
- AgenC: $222,587 1h vol, $51,950 mcap, +24% 1h  
  CA `3sr6UZYGjAVYqE1KwEU6ZdpB6aQWQ134RxUm7USspump`
- DUBBLE: $199,404 1h vol, $489,183 mcap, -53% 1h  
  CA `FEXGegqeVm5vZurqyC7qsmkLqWspVV1ACb9bbLvcpump`
- CHLOE: $195,796 1h vol, $152,291 mcap, +260% 1h  
  CA `6tNEpcBbjvEmsS6KuhTXjW6BnXfXi8AHMWBaAQGwpump`
