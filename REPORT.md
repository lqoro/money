# Trencher live report

Updated 2026-10-29T16:23:56Z (paper trading, never real money)

- Equity: $99.93 (-0.1% vs $100 start)
- Goal: $1,000 by 2026-11-05 05:03Z (a stretch, survival first): at 10% of it, 6.5 days left, needs +42.3% a day from here
- Closed trades: 7, 2 wins
- Fees paid: $4.16 (axiom $0.43, network $3.26, pool $0.35), plus $0.62 lost to slippage
- New trades: on
- Brain: subscription, 382 calls and 0 plan-limit hits in 48h

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
- 16:23Z: 7 coins, 6 with pairs, 0 passed the market filters, 0 researched

## Coins it looked at, and why it passed
- 16:16Z GTA (MIGRATED, $52,077 mcap, $4,235 5m vol): PASS at conviction 2, PASS: down 83% off a $304k peak in 30 minutes, and its 993 buys moved only $4.2k. That's bot dust, not a crowd. Vamp of a bigger GTA ticker. (V3, V6, V13)  
  CA `FViKbzdiHbBYXnVGfkdHAzJD6PcSPDGQHRQ4GY8zpump`
- 16:12Z CATBOT (DIP, $2,317,092 mcap, $24,527 5m vol): REJECT, Dip with fading attention is a falling knife, not a dip  
  CA `dyw5fDNv91eknniMG4tGCU1ZrzjuxbpsLiEzih6pump`
- 16:12Z DESSA (MIGRATED, $7,111,693 mcap, $133,002 5m vol): PASS at conviction 4, PASS: DESSA is 11.6% off a peak set 12 minutes ago, after a 280% hour, and I can't see the bundles. That's the CATCULUS setup again. I'll wait for the 0.618 retest near $4.2M (my rule, V1, V3, V5).  
  CA `npz2FhoufQ7pKqhGpaipYWacrAkidyW2yDpVWSvpump`
- 16:08Z ELOOONG (MIGRATED, $90,467 mcap, $39,669 5m vol): PASS at conviction 2, PASS — 85% off the $600k peak, -45% on the 5m, volume at 0.21x the hourly pace, and a copy with the same ticker is taking the flow. Falling knife in a field of copies. (V1, V6)  
  CA `3zoyoJwywuALj49wi9ffsz49hJaToJ29f9JBSCGNpump`
- 15:58Z SENSE (MIGRATED, $1,356,810 mcap, $21,897 5m vol): REJECT, Top 10 hold 34.3% ex-pool (>25%) (V13)  
  CA `GydpvgKppv8a4gGQqAQsyQJxtQN4S6Ym9gKxjnN3mfun`
- 15:57Z HYPE (MIGRATED, $272,131 mcap, $15,698 5m vol): REJECT, Top 10 hold 42.9% ex-pool (>25%) (V13)  
  CA `8FDW22Dov1Q2hrmb64uPKqyuFKfpGJRQvm9JGsuLpump`
- 15:55Z ELOOONG (MIGRATED, $199,800 mcap, $23,376 5m vol): PASS at conviction 3, PASS: 16 minutes old, 4% off the high, 5 insider networks and bundles unverified, on an Elon-tweet vamp field of 16 copies. That's sniping the top (V1, V5, learned rule).  
  CA `2YZdszj9XpTrKZ3FsVJH5sqGXppCgfW5E5pCVR9Apump`
- 15:54Z offgrid (DIP, $54,083 mcap, $119,609 5m vol): REJECT, Dev holds 5.3% (>1%) (V13, V17)  
  CA `7x8FSbwgJGrXXbk6BgSpXjiW25rzzzNu2wBhsDJbAjUi`
- 15:44Z SARA (MIGRATED, $43,569 mcap, $39,835 5m vol): REJECT, Dev holds 1.7% (>1%) (V13, V17)  
  CA `3j2RebsuBjNoV5DPz1xSztasqWhjStpQarisDpcLpump`
- 15:43Z Stanley (MIGRATED, $45,320 mcap, $9,918 5m vol): REJECT, Top 10 hold 27.6% ex-pool (>25%) (V13)  
  CA `83MRySsDw9nuyV2e7iowXBxPJgSNFphvsytvnBWjop6d`

## Recent lessons
- [2026-10-28 14:15] Expected: a $1.2M dip 47% off the $2.3M peak, with $17.8k 5m volume and buys outnumbering sells 3:1, to retest $2M while the joke still had a crowd (V1 buys-on-dip, V6). What happened: it peaked at 1.09x, then went flat and got time-stopped at 60 minutes with market cap basically unchanged (-0.6%), but I still lost 15.4% because fees and slippage ate about 9% of a $3.33 position, and the rest of the gap is execution I can't see in the record. Rule: on DIP setups, enter only after the dip makes a higher low with 5m volume rising (0.86x the hourly average is fading, not holding). Never open a position so small that round-trip friction is over 3%, because a flat chart is a guaranteed loss at that size.
- [2026-10-28 22:50] Expected: CATCULUS at $460k was the flow leader ($59k 5m volume, 913/363 buys/sells, top 10 at 3.6%), so a momentum entry near the high should either keep running or give a clean -30% exit. What happened: it peaked at 1.24x, the bundle/insiders dumped, and it gapped through the -30% stop to -59% in 42 minutes. Clean top-10 numbers don't rule out bundles spread across many small wallets (V3, V5), and $0.50 in fees on a $2.96 position was a 17% loss before the coin even moved. Rule: no MIGRATED momentum buys within ~20% of the local high unless bundle data is verified. Wait for the V1 0.618 fib or point-of-control retest instead, and skip any position so small that fees are over 5% of cost.
- [2026-10-28 22:59] Expected: the original Cat Bot pair would retest its $845k peak, because holders were clean (top 10 at 3.3%, dev/insiders 0%) and 5m volume was organic at $12.9k (V1, V6, V13). Happened: it ran to 4.44x peak, I took initials at 2x, and the target plus a 35% trail closed the rest around 2.67x, so the clean MIGRATED dip-buy worked but the trail gave back about 40% of the peak, and fees ate roughly a third of a $2.91 position. Rule: once initials are out and the coin is past 4x, tighten the trail to about 25% from peak, and don't open positions under about $5 where fees ruin the math, because sell initials only protects the cost basis, not the runner (V11).
- [2026-10-29 01:32] I bought CATBOT back as a $2.0M base retesting toward the $3.46M high. Price only drifted from $2.59M to $2.41M (-7%) and peaked at 1.12x, but I lost -24.3% because $0.62 in fees and slippage on a $3.42 position cost 18% before the coin moved at all. That makes the time stop correct (V1: don't marry a bag), and the real problem was the size. Rule: before any entry, including a buy-back, I estimate round-trip cost and skip the trade if it tops ~5% of size or if the target can't pay several times that cost. I also only re-enter a stopped-out coin when it reclaims the high, not when it bases in the middle of the range.
- [2026-10-29 02:03] Expected: the FLOATER that had the crowd out of 23 same-ticker coins ($141k 5m volume, 78% buys, clean holders, 34% off the high) would keep climbing toward $500k on the tokenized-stock meta. What happened: it ran to 2.19x, I took initials as planned (V11), and the trailing stop sold the rest at 1.5x from a $255k mcap for +$1.48, but fees and slippage ($0.89) ate about 30% of the $2.94 cost and nearly a third of the gross gain. Next time I keep picking the vamp-field winner by volume and attention (V1, V6) and keep the 2x initials plus 30% trail, but I don't open a position under ~$5 because fixed fees turn a 2x winner into a 1.5x one.
- [2026-10-29 02:10] Expected: CPU, the clear flow leader with clean holders, to bounce from a 38% dip toward 2x (V1, V13). What happened: it ran to 1.63x, gave it all back, and I time-stopped at 1.03x mcap after 52 min. Fees $0.48 plus slippage $0.09, about 18% of a $3.16 position, turned a flat trade into −13.7%. Next time: the friction gate and the $5 minimum are hard blocks, so no sub-$5 entries even on a good setup. If a MIGRATED dip-buy reaches 1.5x and 5m volume starts fading before 2x, sell half instead of watching it round-trip.
- [2026-10-29 02:49] I expected FLOAT, the leading tokenized-stock coin, to run from its $1.04M higher-low reclaim toward $3M (V1, V6), and it did reach 1.64x. Then it faded, and I sat past the 45-minute time stop and got out at 158 minutes. Mcap was only down 7%, but I lost 24.5% because $0.56 of fees and slippage ate 18% of a $3.09 position, which broke my own $5-minimum and friction-gate rules. Next time: no entry under $5 or above 5% friction, no exceptions. If a trade gets past 1.5x before initials, move the stop up to break-even plus fees so a 1.6x peak can't turn into a loss (V11: plan the exit before the entry).

## Meta right now
The meta is fresh pump.fun launches riding the Hyperliquid joke: PURR (Hypurr), Stanley (The Hyperliquid Bull), XLIQUID and Pumperps are all under an hour old and getting buyers, so that theme is rising. The GTA6/Vice City theme is mixed: VI is up 192% but only 30% of its 5m flow is buys, and GATO and Vicecity are bleeding. Cats are fading. CATBOT is up 130% on the hour but its 5m volume ($14.5k) is about a fifth of its hourly pace, with 44% buys. LMEOW is dead at a $2.9k cap with $0 traded in the last 5 minutes, and BVP and SA are farm dumps. The crawler's own summary is stale (it has BVP at +866%; the scan shows -75%), so I'm ignoring it. Hunter Biden's $LAPTOP is a political figure's coin, so it's a hard PASS (V13). The setups I'd paper trade right now: DESSA, a 74h-old migrated coin at $3.4M, up 164%, with $88k on the 5m and buys and sells roughly even. It's inside the V6 range and the volume is real, but I can't see the holders yet; if top 10 < 25%, dev < 1% and bundles < 10% check out, it's conviction 7, initials at 1.5x, 20% trail, and I sell half when the 5m drops to half its hourly pace. Watchlist: XLIQUID ($108k cap, $64k on the 5m, 69% buys) and ELOOONG ($273k cap, $484k on the 5m). Blocker on both: they're 6–12 minutes old with no holder or bundle data, so buying now is sniping a new pair (V1, V5); I'll recheck them at ~30–60 min. PASS on CATBOT (blocker: the 5m dropped to a fifth of its hourly pace and sellers lead, and a DIP needs attention still there), PASS on PURR (blocker: its 5m is down to half its hourly pace), and PASS on Stanley and Pumperps (blocker: their CAs don't end in pump, so I can't confirm the launchpad protections, V3).

## Moving most in its scans, last 30 min (1h volume)
- ELOOONG: $2,279,348 1h vol, $90,467 mcap, +104% 1h  
  CA `3zoyoJwywuALj49wi9ffsz49hJaToJ29f9JBSCGNpump`
- DESSA: $1,615,360 1h vol, $7,111,693 mcap, +280% 1h  
  CA `npz2FhoufQ7pKqhGpaipYWacrAkidyW2yDpVWSvpump`
- CATBOT: $978,902 1h vol, $2,317,092 mcap, -31% 1h  
  CA `dyw5fDNv91eknniMG4tGCU1ZrzjuxbpsLiEzih6pump`
- SENSE: $546,342 1h vol, $1,356,810 mcap, -22% 1h  
  CA `GydpvgKppv8a4gGQqAQsyQJxtQN4S6Ym9gKxjnN3mfun`
- GTA: $342,956 1h vol, $52,077 mcap, +9% 1h  
  CA `FViKbzdiHbBYXnVGfkdHAzJD6PcSPDGQHRQ4GY8zpump`
