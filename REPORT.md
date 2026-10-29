# Trencher live report

Updated 2026-10-29T13:21:06Z (paper trading, never real money)

- Equity: $99.93 (-0.1% vs $100 start)
- Goal: $1,000 by 2026-11-05 05:03Z (a stretch, survival first): at 10% of it, 6.7 days left, needs +41.4% a day from here
- Closed trades: 7, 2 wins
- Fees paid: $4.16 (axiom $0.43, network $3.26, pool $0.35), plus $0.62 lost to slippage
- New trades: on
- Brain: subscription, 350 calls and 0 plan-limit hits in 48h

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
- 13:20Z: 6 coins, 3 with pairs, 0 passed the market filters, 0 researched

## Coins it looked at, and why it passed
- 13:15Z CHLOE (DIP, $50,615 mcap, $29,115 5m vol): PASS at conviction 3, PASS: 16 minutes old, back under $70k after an $89k peak, still falling (-17% on the 5m), top 10 holding 22.7%, 25 insider networks, and a bigger coin already uses the ticker. That's a new pair, not a dip (V1, V6).  
  CA `J92Gw8j5nwkhAKgM1UsTD9GxegeLWXDht4RNx8YTpump`
- 13:12Z GATO (MIGRATED, $5,195,499 mcap, $2,737 5m vol): REJECT, Dev holds 3.3% (>1%) (V13, V17)  
  CA `HsprHxBRgiVaQdRf3TnKNuZZtaX9JUSPgMFdAkk6pump`
- 13:11Z DUBBLE (MIGRATED, $982,069 mcap, $7,026 5m vol): PASS at conviction 3, PASS — 80% off the peak, 5m volume $7k and fading at 0.72x the hourly pace, and a launchpad story with no GitHub on a 1-day-old site that doesn't show the CA. LARP smell, crowd leaving (V1, V6).  
  CA `FEXGegqeVm5vZurqyC7qsmkLqWspVV1ACb9bbLvcpump`
- 13:10Z CATBOT (DIP, $2,636,424 mcap, $11,977 5m vol): PASS at conviction 4, PASS: CATBOT is 58% off its high, but 5m volume is only 0.59x the hourly pace and there's no confirmed higher low. That's a dip with the crowd thinning, and my own rules say wait (V1).  
  CA `dyw5fDNv91eknniMG4tGCU1ZrzjuxbpsLiEzih6pump`
- 13:03Z REMUS (MIGRATED, $457,571 mcap, $4,036 5m vol): PASS at conviction 2, PASS: 20 buys against 261 sells on the 5m, and 180 against 3,727 on the hour. That's a crowd leaving, not arriving. 48 insider networks finish it off. (V1, V13)  
  CA `CA8q2mkYWZnUNqYmf6pxyxAPZsmSe2EG9P7hHMW5pump`
- 12:58Z STONKDILE (DIP, $235,501 mcap, $29,237 5m vol): PASS at conviction 3, PASS — 35-minute-old coin, still red −19.5% on the 5m, volume fading at 0.53x the hourly pace, 405 insider networks flagged. Falling knife, not a dip (V1, V13).  
  CA `WkHcrrgrXHkdMC5csTAKo4YJCVbpH3zkTCBnNQ8pump`
- 12:53Z jeff (DIP, $950,893 mcap, $5,773 5m vol): REJECT, Top 10 hold 33.7% ex-pool (>25%) (V13)  
  CA `HAsTKXYvv65zM7J6Cu5o5PcZsiKMQYo5oz4WPjgqwP6k`
- 12:52Z OREN (DIP, $140,930 mcap, $93,751 5m vol): PASS at conviction 4, PASS: OREN is down 29% in the last 5 minutes on a coin that's 57 minutes old. No higher low yet, so this is a falling knife, not a dip (V1, learned DIP rule).  
  CA `57vAaMsnAJXkvULtAz7fsi6gRn3bHRJFJsJV1okNpump`
- 12:51Z Hyperpill (MIGRATED, $44,741 mcap, $15,075 5m vol): PASS at conviction 2, PASS. It's a 2-minute-old pair. Its own website says "CA coming soon" and doesn't show this address, 10 coins share the ticker, and it makes tech claims with no GitHub. Probable vamp or LARP, and I'd be sniping. (V1, V3, V13)  
  CA `B2Sr358fKA5TvmE6zWoVR8Ks5h3mZQBqDM22pA52pump`
- 12:38Z OREN (MIGRATED, $168,926 mcap, $10,190 5m vol): PASS at conviction 3, PASS: 14% off the high on an unverified-bundle, 17-minute-old coin with 5m volume fading to 0.48x. That's the CATCULUS setup again. Blocker: entry location (learned rule, V3/V5).  
  CA `AVCoELxSDqmT1yUHfzMu9FBpX1MmygBaYdaiLZvMpump`

## Recent lessons
- [2026-10-28 14:15] Expected: a $1.2M dip 47% off the $2.3M peak, with $17.8k 5m volume and buys outnumbering sells 3:1, to retest $2M while the joke still had a crowd (V1 buys-on-dip, V6). What happened: it peaked at 1.09x, then went flat and got time-stopped at 60 minutes with market cap basically unchanged (-0.6%), but I still lost 15.4% because fees and slippage ate about 9% of a $3.33 position, and the rest of the gap is execution I can't see in the record. Rule: on DIP setups, enter only after the dip makes a higher low with 5m volume rising (0.86x the hourly average is fading, not holding). Never open a position so small that round-trip friction is over 3%, because a flat chart is a guaranteed loss at that size.
- [2026-10-28 22:50] Expected: CATCULUS at $460k was the flow leader ($59k 5m volume, 913/363 buys/sells, top 10 at 3.6%), so a momentum entry near the high should either keep running or give a clean -30% exit. What happened: it peaked at 1.24x, the bundle/insiders dumped, and it gapped through the -30% stop to -59% in 42 minutes. Clean top-10 numbers don't rule out bundles spread across many small wallets (V3, V5), and $0.50 in fees on a $2.96 position was a 17% loss before the coin even moved. Rule: no MIGRATED momentum buys within ~20% of the local high unless bundle data is verified. Wait for the V1 0.618 fib or point-of-control retest instead, and skip any position so small that fees are over 5% of cost.
- [2026-10-28 22:59] Expected: the original Cat Bot pair would retest its $845k peak, because holders were clean (top 10 at 3.3%, dev/insiders 0%) and 5m volume was organic at $12.9k (V1, V6, V13). Happened: it ran to 4.44x peak, I took initials at 2x, and the target plus a 35% trail closed the rest around 2.67x, so the clean MIGRATED dip-buy worked but the trail gave back about 40% of the peak, and fees ate roughly a third of a $2.91 position. Rule: once initials are out and the coin is past 4x, tighten the trail to about 25% from peak, and don't open positions under about $5 where fees ruin the math, because sell initials only protects the cost basis, not the runner (V11).
- [2026-10-29 01:32] I bought CATBOT back as a $2.0M base retesting toward the $3.46M high. Price only drifted from $2.59M to $2.41M (-7%) and peaked at 1.12x, but I lost -24.3% because $0.62 in fees and slippage on a $3.42 position cost 18% before the coin moved at all. That makes the time stop correct (V1: don't marry a bag), and the real problem was the size. Rule: before any entry, including a buy-back, I estimate round-trip cost and skip the trade if it tops ~5% of size or if the target can't pay several times that cost. I also only re-enter a stopped-out coin when it reclaims the high, not when it bases in the middle of the range.
- [2026-10-29 02:03] Expected: the FLOATER that had the crowd out of 23 same-ticker coins ($141k 5m volume, 78% buys, clean holders, 34% off the high) would keep climbing toward $500k on the tokenized-stock meta. What happened: it ran to 2.19x, I took initials as planned (V11), and the trailing stop sold the rest at 1.5x from a $255k mcap for +$1.48, but fees and slippage ($0.89) ate about 30% of the $2.94 cost and nearly a third of the gross gain. Next time I keep picking the vamp-field winner by volume and attention (V1, V6) and keep the 2x initials plus 30% trail, but I don't open a position under ~$5 because fixed fees turn a 2x winner into a 1.5x one.
- [2026-10-29 02:10] Expected: CPU, the clear flow leader with clean holders, to bounce from a 38% dip toward 2x (V1, V13). What happened: it ran to 1.63x, gave it all back, and I time-stopped at 1.03x mcap after 52 min. Fees $0.48 plus slippage $0.09, about 18% of a $3.16 position, turned a flat trade into −13.7%. Next time: the friction gate and the $5 minimum are hard blocks, so no sub-$5 entries even on a good setup. If a MIGRATED dip-buy reaches 1.5x and 5m volume starts fading before 2x, sell half instead of watching it round-trip.
- [2026-10-29 02:49] I expected FLOAT, the leading tokenized-stock coin, to run from its $1.04M higher-low reclaim toward $3M (V1, V6), and it did reach 1.64x. Then it faded, and I sat past the 45-minute time stop and got out at 158 minutes. Mcap was only down 7%, but I lost 24.5% because $0.56 of fees and slippage ate 18% of a $3.09 position, which broke my own $5-minimum and friction-gate rules. Next time: no entry under $5 or above 5% friction, no exceptions. If a trade gets past 1.5x before initials, move the stop up to break-even plus fees so a 1.6x peak can't turn into a loss (V11: plan the exit before the entry).

## Meta right now
The meta right now is fresh-launch churn plus cats. Most first-two-hour coins already pulled their volume and died: EGG is -95% and FOMO -98%, each with over $250k of volume in the hour and about $0 in the last 5 minutes. ShuBao and MAS are down 50%+ with under $1k on the 5m. That theme is fading, and it looks like farms (V13). The one fresh coin still holding flow is OREN: 18 minutes old, +300% on the hour, $169k market cap, $10.2k on the 5m but only 52% buys. Cats are the steadier theme. CATBOT is the only one with real weight ($3.5M market cap, $12.2k 5m, 66% buys, -6% on the hour), and GATO and Vivi are weak (GATO 30% buys, Vivi $824 on the 5m). Day-old migrated coins are coasting lower: DUBBLE is -20% with 77% buys but only $6.6k on the 5m, which is under my bar. My trades: CATBOT is a conditional DIP/MIGRATED buy at conviction 6–7, only if holders come back clean (top 10 under 25%, dev under 1%, bundles under 10%), with initials at 1.5x, a 20% trail, half off when 5m volume fades, and a stop where the hour's low breaks. OREN goes on watch only. Blocker: it's 18 minutes old, I'd be chasing +300% into a 50/50 tape, and there's no holder or bundle data, so it qualifies on numbers but not on checks (V1, V6). PASS on MULTI. Blocker: it's on Raydium, not a pump.fun pool, and has no LP or holder data (V2, V6). PASS on $LAPTOP, whatever the headlines say. Blocker: a political figure is behind it and it's already -98% (V13). PASS on MAX. Blocker: $557 on the 5m and a $7.5k market cap, which is dead. One more thing: the crawler's own summary says MAX did $41k on the 5m and MULTI was 54 minutes old, and the scan shows neither, so I'm ignoring that summary and its built-in "BUY" call and trading only the scan data.

## Moving most in its scans, last 30 min (1h volume)
- OREN: $745,307 1h vol, $140,930 mcap, +243% 1h  
  CA `57vAaMsnAJXkvULtAz7fsi6gRn3bHRJFJsJV1okNpump`
- STONKDILE: $659,400 1h vol, $235,501 mcap, +262% 1h  
  CA `WkHcrrgrXHkdMC5csTAKo4YJCVbpH3zkTCBnNQ8pump`
- CHLOE: $256,194 1h vol, $50,615 mcap, +13% 1h  
  CA `J92Gw8j5nwkhAKgM1UsTD9GxegeLWXDht4RNx8YTpump`
- CATBOT: $242,671 1h vol, $2,636,424 mcap, -20% 1h  
  CA `dyw5fDNv91eknniMG4tGCU1ZrzjuxbpsLiEzih6pump`
- EGG: $200,572 1h vol, $2,005 mcap, -98% 1h  
  CA `57ouseDGe5XZ5y9Me4WEwrhgi2q2cogtUUTqkUTGpump`
