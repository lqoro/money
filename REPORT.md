# Trencher live report

Updated 2026-10-29T15:07:58Z (paper trading, never real money)

- Equity: $99.93 (-0.1% vs $100 start)
- Goal: $1,000 by 2026-11-05 05:03Z (a stretch, survival first): at 10% of it, 6.6 days left, needs +41.9% a day from here
- Closed trades: 7, 2 wins
- Fees paid: $4.16 (axiom $0.43, network $3.26, pool $0.35), plus $0.62 lost to slippage
- New trades: on
- Brain: subscription, 370 calls and 0 plan-limit hits in 48h

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
- 15:06Z: 4 coins, 4 with pairs, 1 passed the market filters, 1 researched

## Coins it looked at, and why it passed
- 15:06Z PODZ (FINAL_STRETCH, $22,288 mcap, $4,978 5m vol): REJECT, Top 10 hold 28.0% ex-pool (>25%) (V13)  
  CA `Fh8PsewqXZ43h97TH3GxndqwpKcY1Hzn9yESbGyNo9cb`
- 15:06Z REMUS (MIGRATED, $355,105 mcap, $6,813 5m vol): PASS at conviction 2, PASS: REMUS is down 81% from its peak with sellers outnumbering buyers about 3:1 and price still dropping. The volume spike is people selling, not buyers coming back (V1, V6).  
  CA `CA8q2mkYWZnUNqYmf6pxyxAPZsmSe2EG9P7hHMW5pump`
- 14:58Z AgenC (DIP, $44,677 mcap, $5,535 5m vol): REJECT, Dip with fading attention is a falling knife, not a dip  
  CA `3sr6UZYGjAVYqE1KwEU6ZdpB6aQWQ134RxUm7USspump`
- 14:57Z VI (MIGRATED, $166,328 mcap, $10,014 5m vol): PASS at conviction 3, PASS: 45-minute-old pump 18% off a high it made 12 minutes ago, 5m volume fading (0.41x), sellers in control, no socials, 10 same-ticker copies. No entry here. (V1, V6, V13)  
  CA `A6PM7bxyWYiUxaEpRMHvuL4tY2jYVf8N46vXZ15Hpump`
- 14:56Z PURR (FINAL_STRETCH, $23,650 mcap, $26,510 5m vol): PASS at conviction 3, PASS — 4-minute-old PURR copy with 8 bigger tickers ahead of it, top 10 at 23.7%, on a fading Hyperliquid-parody theme. The blocker is that it's a vamp new pair (V1, V3, V6).  
  CA `5DAqRe7Fa7SzVN3urM8hqKfmCUwZvowZTvp5WMgupump`
- 14:54Z CHLOE (DIP, $136,049 mcap, $13,464 5m vol): REJECT, Dip with fading attention is a falling knife, not a dip  
  CA `6tNEpcBbjvEmsS6KuhTXjW6BnXfXi8AHMWBaAQGwpump`
- 14:52Z JASON (MIGRATED, $162,403 mcap, $3,961 5m vol): REJECT, RugCheck danger: Creator history of rugged tokens  
  CA `wKy6tEDZj6jS1GUMmnSSTrR1bXJQa35s7VHcWHxhNbA`
- 14:50Z STANK (MIGRATED, $68,754 mcap, $2,072 5m vol): PASS at conviction 2, PASS: the crowd has left. 5m volume is $2.1k (0.12x the hourly pace) and the price is down 15% on the 5m. It's a 53-minute-old one-pump coin now under the $70k floor (V1, V6).  
  CA `5wsjHxT5nW5jQuVupXUNnYszF3WoWCfGGk9LMcsCJzY8`
- 14:48Z BVP (FINAL_STRETCH, $35,131 mcap, $34,347 5m vol): PASS at conviction 3, PASS — 9 minutes old, already 11x off its low and sitting 8.5% under the high at 84% bonded, with bundles unverified and 16 coins on the same ticker. I'd be the exit liquidity for the pre-bond dump (V1, V3, V13).  
  CA `96bm5i6SoyfWxaTU5easdptZLuvCViACe83rEiWXpump`
- 14:42Z GATO (MIGRATED, $5,095,095 mcap, $7,990 5m vol): REJECT, Dev holds 3.3% (>1%) (V13, V17)  
  CA `HsprHxBRgiVaQdRf3TnKNuZZtaX9JUSPgMFdAkk6pump`

## Recent lessons
- [2026-10-28 14:15] Expected: a $1.2M dip 47% off the $2.3M peak, with $17.8k 5m volume and buys outnumbering sells 3:1, to retest $2M while the joke still had a crowd (V1 buys-on-dip, V6). What happened: it peaked at 1.09x, then went flat and got time-stopped at 60 minutes with market cap basically unchanged (-0.6%), but I still lost 15.4% because fees and slippage ate about 9% of a $3.33 position, and the rest of the gap is execution I can't see in the record. Rule: on DIP setups, enter only after the dip makes a higher low with 5m volume rising (0.86x the hourly average is fading, not holding). Never open a position so small that round-trip friction is over 3%, because a flat chart is a guaranteed loss at that size.
- [2026-10-28 22:50] Expected: CATCULUS at $460k was the flow leader ($59k 5m volume, 913/363 buys/sells, top 10 at 3.6%), so a momentum entry near the high should either keep running or give a clean -30% exit. What happened: it peaked at 1.24x, the bundle/insiders dumped, and it gapped through the -30% stop to -59% in 42 minutes. Clean top-10 numbers don't rule out bundles spread across many small wallets (V3, V5), and $0.50 in fees on a $2.96 position was a 17% loss before the coin even moved. Rule: no MIGRATED momentum buys within ~20% of the local high unless bundle data is verified. Wait for the V1 0.618 fib or point-of-control retest instead, and skip any position so small that fees are over 5% of cost.
- [2026-10-28 22:59] Expected: the original Cat Bot pair would retest its $845k peak, because holders were clean (top 10 at 3.3%, dev/insiders 0%) and 5m volume was organic at $12.9k (V1, V6, V13). Happened: it ran to 4.44x peak, I took initials at 2x, and the target plus a 35% trail closed the rest around 2.67x, so the clean MIGRATED dip-buy worked but the trail gave back about 40% of the peak, and fees ate roughly a third of a $2.91 position. Rule: once initials are out and the coin is past 4x, tighten the trail to about 25% from peak, and don't open positions under about $5 where fees ruin the math, because sell initials only protects the cost basis, not the runner (V11).
- [2026-10-29 01:32] I bought CATBOT back as a $2.0M base retesting toward the $3.46M high. Price only drifted from $2.59M to $2.41M (-7%) and peaked at 1.12x, but I lost -24.3% because $0.62 in fees and slippage on a $3.42 position cost 18% before the coin moved at all. That makes the time stop correct (V1: don't marry a bag), and the real problem was the size. Rule: before any entry, including a buy-back, I estimate round-trip cost and skip the trade if it tops ~5% of size or if the target can't pay several times that cost. I also only re-enter a stopped-out coin when it reclaims the high, not when it bases in the middle of the range.
- [2026-10-29 02:03] Expected: the FLOATER that had the crowd out of 23 same-ticker coins ($141k 5m volume, 78% buys, clean holders, 34% off the high) would keep climbing toward $500k on the tokenized-stock meta. What happened: it ran to 2.19x, I took initials as planned (V11), and the trailing stop sold the rest at 1.5x from a $255k mcap for +$1.48, but fees and slippage ($0.89) ate about 30% of the $2.94 cost and nearly a third of the gross gain. Next time I keep picking the vamp-field winner by volume and attention (V1, V6) and keep the 2x initials plus 30% trail, but I don't open a position under ~$5 because fixed fees turn a 2x winner into a 1.5x one.
- [2026-10-29 02:10] Expected: CPU, the clear flow leader with clean holders, to bounce from a 38% dip toward 2x (V1, V13). What happened: it ran to 1.63x, gave it all back, and I time-stopped at 1.03x mcap after 52 min. Fees $0.48 plus slippage $0.09, about 18% of a $3.16 position, turned a flat trade into −13.7%. Next time: the friction gate and the $5 minimum are hard blocks, so no sub-$5 entries even on a good setup. If a MIGRATED dip-buy reaches 1.5x and 5m volume starts fading before 2x, sell half instead of watching it round-trip.
- [2026-10-29 02:49] I expected FLOAT, the leading tokenized-stock coin, to run from its $1.04M higher-low reclaim toward $3M (V1, V6), and it did reach 1.64x. Then it faded, and I sat past the 45-minute time stop and got out at 158 minutes. Mcap was only down 7%, but I lost 24.5% because $0.56 of fees and slippage ate 18% of a $3.09 position, which broke my own $5-minimum and friction-gate rules. Next time: no entry under $5 or above 5% friction, no exceptions. If a trade gets past 1.5x before initials, move the stop up to break-even plus fees so a 1.6x peak can't turn into a loss (V11: plan the exit before the entry).

## Meta right now
The meta right now is mostly one-hour pump.fun launches dumping. Chloe is down 97% and sits at $2.3k with $0 on the 5m. HYPE is -74%, SA -73%, LMEOW -58%, KORILA -56% and MUGI -48%, all under 1.2h old. Those are the farm-dump candles V13 warns about. Two themes are fading. The Hyperliquid parodies (HYPE, hyper, PumpLiquid) are bleeding even with HYPE trending on CoinGecko. Cat coins (CATBOT, LMEOW, GATO) are split, and CATBOT is the only one still drawing buyers. The rising theme is brand-new micro-launches going vertical: BVP is +866% with $34k on the 5m at a $35k cap, and PODZ is +338%. The older coins are only grinding: DESSA is +52% at $1.5M, but both it and DUBBLE are under $10k on the 5m. The only setup I'd paper trade is CATBOT as a DIP. It's 17.9h old, sits at a $907k cap, is down 47% on the hour (a normal correction) and still has $94k on the 5m with 76% buys, so attention hasn't left. It's a buy only if the dossier shows top 10 under 25%, dev under 1% and bundles under 10%. If it does, conviction 6-7, initials at 1.5x, 20% trail, stop under the dip low, and I sell if the 5m drops to half its hourly pace. Blocker until then: I can't see the holders. PASS on BVP for now. Blocker: it's 12 minutes old with no holder or bundle data, so I'd be chasing a new pair (V1). I'll recheck it after 30 minutes as a FINAL_STRETCH candidate. PASS on PODZ and SPAN. Blocker: the CAs don't end in pump, PODZ is still listed under pumpfun anyway and SPAN is on Meteora DBC (V3). PASS on everything else. Blocker: the 5m is dead or sellers are in control. I'm ignoring the crawler's meta_summary. Blocker: it calls Chloe a $200k coin, but the scan shows it at $2.3k, so that summary is stale.

## Moving most in its scans, last 30 min (1h volume)
- CHLOE: $773,403 1h vol, $136,049 mcap, +228% 1h  
  CA `6tNEpcBbjvEmsS6KuhTXjW6BnXfXi8AHMWBaAQGwpump`
- CATBOT: $550,139 1h vol, $907,446 mcap, -47% 1h  
  CA `dyw5fDNv91eknniMG4tGCU1ZrzjuxbpsLiEzih6pump`
- AgenC: $329,971 1h vol, $44,677 mcap, -11% 1h  
  CA `3sr6UZYGjAVYqE1KwEU6ZdpB6aQWQ134RxUm7USspump`
- VI: $289,926 1h vol, $166,328 mcap, +243% 1h  
  CA `A6PM7bxyWYiUxaEpRMHvuL4tY2jYVf8N46vXZ15Hpump`
- Chloe: $228,060 1h vol, $2,276 mcap, -99% 1h  
  CA `9B5uDwoTPkXXb67vaHiqWmyvWuUEDBMSU6ssZH1Zpump`
