# Trencher live report

Updated 2026-11-24T19:59:30Z (paper trading, never real money)

- Equity: $74.23 (-25.8% vs $100 start)
- Closed trades: 22, 3 wins
- Fees paid: $14.78 (axiom $2.81, network $9.18, pool $2.66), plus $4.15 lost to slippage
- New trades: WATCH-ONLY (scans and decides, buys nothing)
- Brain: subscription, claude-haiku-5-5 for routine calls, claude-opus-5-5 for the daily review; 515 routine calls and 0 plan-limit hits in 48h
- Watch log: 77 coins being followed, 3352 filed, 0 would-buys (6h follow, sampled every 2 min)

## Scorecard (after fees)
- 22 closed, 3 won (14%), net $-25.79
- Per trade (expectancy) $-1.17; avg win $+1.43, avg loss $-1.58
- Gross $-6.96; costs $18.83 (fees $14.66 + slippage $4.17), on top of a gross loss
- Give-back: peaked 1.36x on average, banked 0.86x
- Hit 1.5x+ and still closed red: 2
  - CPU peaked 1.63x, $-0.43  
    CA `5JbRYEz844bwnKbGx4dRHhrJ6zjrJ194CKdDXtzwgaXo`
  - FLOAT peaked 1.64x, $-0.76  
    CA `Bv1a7cEj5aRnJQhMw4kRQqAFesMSd5LwcDnUzq52BMmr`
- By exit:
  - time stop: 10, 1 won, net $-8.24, fees+slip $8.34, peak 1.22x → 0.87x
  - stop loss: 9, 0 won, net $-21.73, fees+slip $7.78, peak 1.08x → 0.65x
  - trailing stop: 2, 2 won, net $+4.21, fees+slip $2.04, peak 3.32x → 1.72x
  - other: 1, 0 won, net $-0.03, fees+slip $0.67, peak 1.4x → 0.99x

## Open positions
- none

## Recent trades
- 06:19Z CLOSE AAPLCAT -31% ($-3.14), fees $0.73  
  CA `GYKnd6jGUSQoBUnj6LdGCBtCWYDgr2Zd6QwNPcy5pump`
- 07:37Z BUY ANAKIN $10.01, fees $0.36  
  CA `8s4bNqEztH1JP7mkU747uMr7AckCQdiV47FDqYnDpump`
- 08:22Z SELL ANAKIN for $8.58, fees $0.34  
  CA `8s4bNqEztH1JP7mkU747uMr7AckCQdiV47FDqYnDpump`
- 08:22Z CLOSE ANAKIN -14% ($-1.43), fees $0.70  
  CA `8s4bNqEztH1JP7mkU747uMr7AckCQdiV47FDqYnDpump`
- 10:10Z BUY ANAKIN $10.00, fees $0.36  
  CA `8s4bNqEztH1JP7mkU747uMr7AckCQdiV47FDqYnDpump`
- 10:55Z SELL ANAKIN for $7.98, fees $0.33  
  CA `8s4bNqEztH1JP7mkU747uMr7AckCQdiV47FDqYnDpump`
- 10:56Z CLOSE ANAKIN -20% ($-2.02), fees $0.69  
  CA `8s4bNqEztH1JP7mkU747uMr7AckCQdiV47FDqYnDpump`
- 20:22Z BUY Slingoor $10.00, fees $0.39  
  CA `H4gHnZ3NCU7Z9XQwGX6YYJNyieGEW8pqwGRUcdSxpump`
- 20:24Z SELL Slingoor for $7.14, fees $0.34  
  CA `H4gHnZ3NCU7Z9XQwGX6YYJNyieGEW8pqwGRUcdSxpump`
- 20:25Z CLOSE Slingoor -29% ($-2.86), fees $0.74  
  CA `H4gHnZ3NCU7Z9XQwGX6YYJNyieGEW8pqwGRUcdSxpump`

## Last closes
- HYPERCHAN: -5% ($-0.49), time stop: 45 min and only 1.05x  
  CA `3ApVr1xphYMpi9dn3rpqU4hwvpmCQDVwxET1rdCDpump`
- PILLSEY: -31% ($-3.59), stop loss -20% hit (0.78x)  
  CA `J5jxG3PFaWpj6BLEQExyC6FSqSvaTKNdQ9G3sZwBpump`
- Leverhedge: -3% ($-0.32), time stop: 76 min and only 1.06x  
  CA `FWatMYieKhRuJ1yuTcmVG1njRhZWwqHwjR11pBympump`
- PAWCAT: +1% ($+0.07), time stop: 45 min and only 1.10x  
  CA `762ZqBCd5m2q3QJ5UPkFL5rqdEUeygNkfTZrpGEZpump`
- BLUE: -30% ($-2.98), stop loss -20% hit (0.78x)  
  CA `CPoGSmcjprCvzA2MFYLJMpQkGjmgVzKg4RVwMdrzpump`
- SIS: -31% ($-3.31), stop loss -20% hit (0.76x)  
  CA `FdKdpz11GsTofLaNiddrhxrsE4APZYSSfLFqQ9YKpump`
- AAPLCAT: -31% ($-3.14), stop loss -20% hit (0.76x)  
  CA `GYKnd6jGUSQoBUnj6LdGCBtCWYDgr2Zd6QwNPcy5pump`
- ANAKIN: -14% ($-1.43), time stop: 45 min and only 0.94x  
  CA `8s4bNqEztH1JP7mkU747uMr7AckCQdiV47FDqYnDpump`
- ANAKIN: -20% ($-2.02), time stop: 45 min and only 0.88x  
  CA `8s4bNqEztH1JP7mkU747uMr7AckCQdiV47FDqYnDpump`
- Slingoor: -29% ($-2.86), stop loss -20% hit (0.79x)  
  CA `H4gHnZ3NCU7Z9XQwGX6YYJNyieGEW8pqwGRUcdSxpump`

## Last scan
- 19:58Z: 6 coins, 6 with pairs, 0 passed the market filters, 0 researched

## Coins it looked at, and why it passed
- 19:57Z Slingoor (MIGRATED, $39,600 mcap, $2,109 5m vol): REJECT, Top 10 hold 28.4% ex-pool (>25%) (V13)  
  CA `ANvsL4A6tJKAXJsPg7XVSHQA7KYmFcpW42jPuhVtpump`
- 19:56Z PumpBull (MIGRATED, $219,925 mcap, $3,591 5m vol): REJECT, RugCheck danger: Creator history of rugged tokens  
  CA `GzDqH7FnMqtuMupdc2ZQF6KX2yk9A4CbUBzs2Kaspump`
- 19:38Z Slingoor (DIP, $148,882 mcap, $13,989 5m vol): PASS, PASS — brain unavailable, not trading blind.  
  CA `6GLetugFEmy7P7SmLtg3zyZdz6rWCQ8gHPbPYZs9pump`
- 19:32Z ANSEM (MIGRATED, $30,660 mcap, $7,178 5m vol): PASS, PASS — brain unavailable, not trading blind.  
  CA `7R7ouhA2Wt1QQZGaJAT3PPnQbRTbZWrFhYzBCwSTpump`
- 19:29Z wizardcat (FINAL_STRETCH, $22,683 mcap, $2,595 5m vol): REJECT, Top 10 hold 25.1% ex-pool (>25%) (V13)  
  CA `6W3H5nEzuLUpTbcMrhRfMiDPCZ4QuBmZPBkeAMzypump`
- 19:29Z DONJENSEN (MIGRATED, $1,962,587 mcap, $3,095 5m vol): PASS, PASS — brain unavailable, not trading blind.  
  CA `5LDowscYVD3a6ZS4m8gCqG5nU16eLTwRXhciFi1bpump`
- 19:21Z Z3RO (FINAL_STRETCH, $14,624 mcap, $4,797 5m vol): PASS, PASS — brain unavailable, not trading blind.  
  CA `94ygGubtS2jZewsuPd13Gqfj4Wi3mh8iGGDpDSYzero`
- 19:20Z Holders (DIP, $157,501 mcap, $54,549 5m vol): PASS, PASS — brain unavailable, not trading blind.  
  CA `55RwtHpoNB81SgfiNvogeZTMfik2SfMGa5FaxKcXpump`
- 19:18Z FREEDOM (FINAL_STRETCH, $17,305 mcap, $49,658 5m vol): PASS, PASS — brain unavailable, not trading blind.  
  CA `FDNc812jkHdhkdeRNaLMVwyihHMLR6ztTmRfxG7opump`
- 19:15Z FIONA (MIGRATED, $2,959,907 mcap, $3,278 5m vol): REJECT, Bundles: 9 linked wallet cluster(s) hold 28.8% of supply (>20%) (V17)  
  CA `B34nXKzCgsJb9ChLuSHPRpXLE3WFSWyeT8Cqkzzmpump`

## What its skips did next (last 48h)
A skip "ran" if the coin reached the first target (1.5x) from the skip price before a 20% drop, "dumped" if the drop came first. Sampled every 10 min, followed 6h.
- too new / sniping: blocked 37, ran 6, dumped 30, flat 1, open 0 (saving losses: keep it)
  - ran: Wojak up to 4.29x  
    CA `5eiLc9r79PkJquiFvYWdXJYtGNRjTpzot8MR7Z4Ppump`
  - ran: Hold up to 1.62x  
    CA `8J7yeYsBzozSQ67Ji4kpun2gdfTFp8o9g6rNkYR3pump`
  - ran: VEST up to 2.65x  
    CA `5ajKDjnprQhAZb7psoUbDSdqocaQJgnWySLTmH8ppump`
- top 10 over 25%: blocked 33, ran 5, dumped 24, flat 2, open 2 (saving losses: keep it)
  - ran: SNP6900 up to 2.76x  
    CA `DnbQKi146NDmwwji3f3q5i68HQnYyBEhoDyj2q3Npump`
  - ran: JENSEN up to 2.62x  
    CA `GaNJeASYBM9k3TvEeUC2Pdyu1TjcpzTmPpoom92fpump`
  - ran: GOAT up to 1.53x  
    CA `5Ze97VEpX3EdRF4vbsxUXTdwGKF2qHGregrxToWEpump`
- near the high / chasing: blocked 33, ran 7, dumped 24, flat 2, open 0 (saving losses: keep it)
  - ran: Bertcoin up to 1.8x  
    CA `xEK58Qa2xZ7C36Z2g3Jjq1WHY561CvvnJkLpgJspump`
  - ran: WOFL up to 2.62x  
    CA `AdXjXfumPSSKk7PrfgDHcAsPvuxnKv7Zo9WZEWKbiDkh`
  - ran: Phil up to 2.05x  
    CA `GMLSyjZCKGtFwztp2mtT8PDeNUA6WEk7oQoe3QkFpump`
- flow below pace: blocked 32, ran 7, dumped 25, flat 0, open 0 (saving losses: keep it)
  - ran: OpenIndex up to 1.63x  
    CA `FuKY3dk7QmpbDdQRjzbjB3G6PiCuqKNvN4dAWDpwpump`
  - ran: hCAT up to 1.52x  
    CA `2FYs4vApfj4ErsggpFDfzMv1WvxnyiLtzNEj84mS6TLh`
  - ran: WALLSTFLY up to 1.52x  
    CA `2DQbV7hsqxKVWmFakXGGhBbNyY28tDJ9YuJkojYrpump`
- brain paced: blocked 26, ran 8, dumped 13, flat 0, open 5 (mixed)
  - ran: Scamsem up to 1.56x  
    CA `5JWeGmA9z6yHd5F9P6B23A8wthho8BpZuDmQv5DfLoat`
  - ran: RUGSEM up to 1.5x  
    CA `9cDnmLRDWeJzcpyw8tSFAT7HS4Aunx6MmZWjMfrzpump`
  - ran: SHHFT up to 1.61x  
    CA `GqMg4TRt5U5HRK6oeZYwCF1Jz7Ym9MSzWSoFCtFsbzf6`
- RugCheck danger: blocked 22, ran 5, dumped 16, flat 0, open 1 (saving losses: keep it)
  - ran: Holdsgiving up to 2.96x  
    CA `A2jLaCC7v3VjXP8gEgCQNbTWEvizYuQ82jFEYfzipump`
  - ran: JENSEN up to 1.7x  
    CA `CjPoozfB2Vub8pHFvdKuKUGJDLWuYC2U32yRTxMhpump`
  - ran: FUCK! up to 2.22x  
    CA `CSjwLiCLyaJqXQm9XCV3LdYWMYswbZ7JQ71JKX77pump`
- thin 5m volume: blocked 15, ran 1, dumped 11, flat 3, open 0 (saving losses: keep it)
  - ran: NINO up to 1.55x  
    CA `BqekG1RSPUthaKfStu7Uvyvr1eR6TchrQMp1M5r5pump`
- dev share over 1%: blocked 13, ran 2, dumped 8, flat 3, open 0 (saving losses: keep it)
  - ran: BLOOM up to 2.09x  
    CA `FyRXnHLBSeHHoigrgHR1hvcXiPbPCa5bxhVhEDampump`
  - ran: PI up to 1.77x  
    CA `D2AK5DvBj8AxN5VX1t6bjv7muJVPUx4hFPowVRWYpump`
- bundles over the line: blocked 11, ran 1, dumped 6, flat 4, open 0 (saving losses: keep it)
  - ran: RNV up to 2.35x  
    CA `A2nbXtQvvRMvWtifCkV8cYepwcC4M7iA1jVMwAh6pump`
- falling knife (code): blocked 11, ran 2, dumped 8, flat 1, open 0 (saving losses: keep it)
  - ran: OpenIndex up to 1.63x  
    CA `FuKY3dk7QmpbDdQRjzbjB3G6PiCuqKNvN4dAWDpwpump`
  - ran: Fly up to 1.52x  
    CA `84tAcSK5L9kuQEVM8C8vMHXnfdA83nGBT2nYfSbPUcAc`

## Daily review (2026-11-23, claude-opus-5-5)
Nothing has a positive after-cost edge yet. All 229 settled coins average -8.7% net on the simple plan. Before costs they average about +0.9%, so the 9.6% average round-trip cost on a $10 buy accounts for the whole loss. That is the same story as the 22 paper trades, where fees and slippage were $18.83 of the $25.79 lost. The best setup is FINAL_STRETCH: n=39, 35.9% hit 1.5x, -4.9% net. With a 1.5x target, a -20% stop and about 10% costs, a setup needs roughly 43% hitting the target to break even. At n=39 the hit rate's 95% range is about 21–51%, so this sample can't separate it from MIGRATED, from coin-flip noise or from breakeven. I can't say whether the routine model's would-buys beat its passes, because it made zero would-buys in 24h. The coins it passed on (n=157, -8.4%) did slightly better than the coins the checklist failed (n=70, -9.8%), but both lost money. Passing everything was the right call on average. One process note: the watch-only review was set for about Nov 10 and today is Nov 23, so the owner should decide whether this is still the plan.
- finding: All coins (n=229): 25.8% ran, 59.4% dumped, median peak 1.25x, 11.8% hit 2x, -8.7% net after 9.6% cost. Before costs that is about +0.9%: no edge, just a cost drag.
- finding: MIGRATED (n=162) is the weakest setup and 71% of the sample: 23.5% ran, 62.3% dumped, -10.0% net (about +0.5% before costs). The simple plan has nothing to work with here.
- finding: FINAL_STRETCH (n=39) is the least bad: 35.9% ran, 20.5% hit 2x, median peak 1.44x, -4.9% net (about +5.1% before costs). That gap is about 1 standard error (roughly 5 points). Ran plus dumped is 100%, so every one of these coins resolved within 6h; it is a coin-flip-style distribution.
- finding: DIP (n=28) dumps least (35.7%) but barely moves: median peak 1.08x, 3.6% hit 2x, 39% flat, -6.8% net. Dips mostly go sideways and then pay the fee.
- finding: The routine model's rejections (brain_passed n=157, -8.4%) and checklist failures (n=70, -9.8%) differ by 1.4 points. That is noise. Neither the checklist nor the routine model splits winners from losers on this metric, though both correctly kept money out of a losing pool.
- idea to test: Cost gate: only count coins whose logged round-trip cost is at most 5% at the intended size. Then check whether the before-cost return of the deeper-pool coins survives. If costs are mostly fixed fees, rerun the whole week at $25 and $50 buys. Costs are the single biggest lever in this data.
- idea to test: FINAL_STRETCH, checklist passed, 5m volume of at least $10k, buy ratio of at least 0.55 (V1). Test whether at least 43% hit 1.5x before -20% on deduplicated coins. Below about 40% on the week's sample, drop it.
- idea to test: FINAL_STRETCH exit variant: sell enough at 2x to get the cost back, trail the rest, stop at -30% to survive the pre-bond dump (V1). Compare with the 1.5x/-20% plan on the same coins. 20.5% hit 2x, and the 1.5x cap cuts off exactly the tail the strategy depends on.
- idea to test: MIGRATED split by age (under 1h vs 1–12h) and mcap ($30–70k vs $70k–$11M, V6), with 5m volume of at least $10k and flow ratio (5m volume over hourly pace) of at least 1.0. Keep MIGRATED only if one cell is positive after costs with n of at least 40. Otherwise drop the setup.
- idea to test: DIP split by drawdown (40–55% vs 55–75%) with flow ratio of at least 1.0 and buy ratio of at least 0.55. Check whether the deeper or the shallower dips are the flat, fee-paying ones.

## Rules it changed from results and skips
- 11-02 23:38Z tightened: DIP gate: flow at least 0.7x the hourly pace plus a printed higher low (DIPs 0 for 5 (-$6.70), every one bought before the higher low held (HEXN x2, SIS, Something, Leverhedge). The code line is now aligned to the owner's 0.7x.)
- 11-02 23:38Z dropped: Never-green cut at under 0.92x in the first 10 minutes (It works as a tighter stop than the owner's code-enforced 20%, which I was told not to set. Replaced by a thesis exit (sell when the printed higher low breaks) plus the existing time-based check at minute 10 (under 1.05x with flow under pace).)
- 11-02 23:38Z added: Thesis exit: sell when the printed higher low the entry rested on breaks (HEXN #2, SIS and AAPLCAT all broke the higher low first and then slid through the stop to -27% to -31%. This exit is set by structure, not by a percent.)
- 11-03 02:40Z tightened: Entries above ~$1M mcap (was capped at 7; now a probe at most, and only with a breakout printing) (10 trades above $1M: Something, CATBOT re-entry, FLOAT, HYPERCHAN x2, Leverhedge, PAWCAT, AAPLCAT, ANAKIN x2. Only one closed green, PAWCAT at +0.7%; the rest lost between -3% and -31%. Only FLOAT got past 1.3x, and it gave it all back. This goes below the owner's 7 floor for this band only. 10 samples with one scratch win is the strongest pattern in the book, and on a ~$74 wallet each of these was mostly fees. The floor still stands under $1M.)
- 11-03 02:40Z added: Buy close to the structure: entry within ~12% above the printed higher low, otherwise PASS 'mid-range' (The 20% stop is set by the owner, so I fix the entry instead. The 9 stop exits filled at -59, -38, -36, -27, -31, -30, -31, -31 and -29%, about -35% on average after fees and gaps. HEXN #2, with its invalidation 13% under entry, was the smallest of them. Entering near the level lets the thesis-break exit fire before the price gaps through the hard stop.)
- 11-03 02:40Z dropped: All retired fee/size/minimum-position fragments (The code fee check owns this now (target must pay 3x the round trip, round trip capped at 20% of the position), so per the owner's instruction these are no longer learned rules.)
- 11-03 05:41Z tightened: DIP flow gate set to ≥0.7x hourly pace (owner gate, also the code param) (DIPs 0 for 5, −$6.70. Falling-knife (code) skips: 30 blocked, 5 ran, 22 dumped. The owner's Oct 30 note sets 0.7x.)
- 11-03 05:41Z dropped: All retired fee/size/friction/minimum-position text (Code now enforces the fee check (target ≥3x round trip, round trip ≤20% of the position), so these notes are removed from the rules.)

## Recent lessons
- [2026-10-30 10:53] Expected: HYPERCHAN, the clean flow leader of the HYPE meta at about $2M, would break its 4-hour range and run toward $3M. What happened: it peaked at 1.18x, never broke out, and the 45-minute time stop sold it at 1.05x on market cap, which is still a 4.9% loss after fees. The shallow-band leader rule did its job (clean holders, real flow, no dump), so it stays. What failed was the clock: my written rule is to exit if still under 1.0x at 45 min, but this one closed green on market cap, and a 1.5x move on a $2M coin rarely happens in 45 minutes (V1 talks about small new pairs, V6 about $70k–$11M runners). Next time, for MIGRATED entries above about $1M that are holding their range, give the time stop more room (about 90 min) and still exit if price closes back under the range low. One flat scratch is a sample of one, not a reason to drop the setup.
- [2026-10-30 21:37] Expected PILLSEY, the flow leader in the pump.fun meta at $125k 5m, to break its $414k high toward 1.5x; it peaked at 1.32x, never reached initials, fell back through the -20% stop inside 18 minutes, and the half-hold on review only made the loss bigger (-31%). It sat about 20% under the high, so it passed my pullback rule, but I bought right after a +31% five-minute candle at 4.2x the hourly pace, which is chasing a spike, not buying a pullback (V1, V6), and it fits my "near-high skips mostly dump" data. Next time a coin that is up more than ~25% in the last 5 minutes counts as "chasing" even if it's 20% off the high: wait for that candle to retrace and a higher low to form. And once a trade has hit ~1.3x, an early-shakeout stop review sells all of it instead of trimming half.
- [2026-10-31 19:21] Expected: a clean DIP on the proven Leverhedge original (top 10 at 4.6%, a higher low holding, buys 0.73 of the 5m flow) would retest the $1.71M high, with initials at 1.5x (V1 big buys on a dip, V6/V13 clean holders). What happened: it peaked at 1.28x, just under my 1.3x break-even trigger, then faded, and I used the over-$1M extension to hold past 45 min. The time stop sold it at 76 min at 1.06x mcap, which came out -3.2% after fees. This confirms the time-stop rule and refines the extension: "green on mcap" now means at least 1.08x so the ~5.5% round trip is covered, otherwise exit at 45 min. One near-miss at 1.28x isn't enough data to lower the 1.3x break-even trigger.
- [2026-10-31 22:25] Expected: PAWCAT, the clean cat-meta flow leader 24% off its high, would break the $4.05M high toward ~$5M. What happened: it peaked at 1.11x, never got near the $4.05M break, and the 45-min time stop closed it flat (+$0.07). That fits my shallow-band cap and my "target at least 1.5x" rule: a $3M coin needing a high break plus extension was a slow 1.3–1.6x idea at best. So the rule stays and the stop worked as intended (V1). Next time, on $3M+ migrated coins, rate the trade on how far the first resistance is ($4.05M = 1.32x, under the 1.5x initials target), not on the extension past it, and PASS with blocker "target below initials" unless the break is already happening.
- [2026-11-01 03:30] Expected: BLUE, the flow leader in a 14-coin same-ticker field, would bounce off its 0.618 base 36.6% below the high. Instead it never went green (peak 0.99x), the stop review fired at 11 minutes, and I closed at −29.8%, worse than the −20% stop. That makes 6 of 6 stop reviews closing worse than the stop. This confirms two of my rules. "Confirm the entry": a fib touch with fading pace is a guess, not a printed higher low (V1, V6). "Stop review defaults to SELL": a probe that never went green should be sold at the stop with no review delay. A noted bundle cluster plus fading pace is a PASS, not a probe, because a 14-copy vamp field splits the crowd even for the leader (V1, V3).
- [2026-11-01 05:24] Expected: SIS, the original SpaceX "SI" rebrand coin, to bounce off a higher low at 0.000679 to 1.5x initials, with $42.5k on the 5m at 1.16x pace and clean holders. What happened: it peaked at 1.01x, broke the higher low within 11 minutes, and the stop review read narrative_dead and sold at −31% for −$3.31, which makes DIPs 0 for 5. This confirms my rules that a DIP needs a confirmed higher low and that stop reviews sell at once (V1). It also confirms that a story already half-priced at $760k after $3.2M of 24h volume is a crowd leaving, not arriving, so next time a DIP whose catalyst has already printed (a news rebrand) rates a probe at most until the reclaim above the pullback high prints (V1, V5).
- [2026-11-01 06:19] Expected AAPLCAT, 36% off its $1.8M high with a printed higher-low base, clean holders and $12.6k on the 5m, to retest the peak at about 1.57x. It peaked at 1.01x, broke the 0.000981 higher low, and the "unclear" stop review sold at −31% instead of −20%. That makes 7 of 7 stop reviews closing worse than the stop. This confirms my existing rules rather than adding a new one: the proven band needs 5m at or above the hourly pace and a meta with the crowd still arriving (V1, V6). I bought with pace under the hourly average and a cooling meta, so next time a band entry with flow below pace is a PASS (blocker "flow below pace"), not a probe, and a broken higher low sells right away.
- [2026-11-02 08:22] I expected ANAKIN, the clean 5m-volume leader 34% off its $6.05M high with a 63% buy share, to retest the high for about 1.5x. It never reached 1.05x, the time stop sold it at 0.95x on mcap, and fees plus slippage turned that into −14%. I took the buy share as the bounce and never saw a printed higher low, so the money shape was only half there. The lesson backs my existing rule, not a new ban: a buy share is not a higher low (V1 says big buys on a dip are bullish, but only once they hold a level). Next time a MIGRATED dip buy needs a printed higher low above the hourly low before entry, and the 45-minute time stop did its job by cutting it small.
- [2026-11-02 10:56] I re-entered ANAKIN at $4.49M expecting a breakout through the 0.0043 range high to carry toward a retest of the $6.05M peak. That target was only 1.35x away, so I sized it as a probe. It peaked at 1.08x, failed back into the range and hit the 45-minute time stop at 0.88x for −20%. This was my second loss on the same coin and it backs my existing re-entry rule rather than adding a new one: buying back a coin that already burned me needs it to reclaim its prior high (here the $6.05M peak) with flow at or above pace, and a range-high break 1.35x under that peak is a mid-range entry (V1 plan the exit, V6 only trade when everything lines up).
- [2026-11-02 20:25] I expected Slingoor, a clean MIGRATED leader with $25k of 5m flow at pace and a 0.77 buy share, to retest its $408k high from $304k. It never went green (0.98x peak) and hit the -20% stop in 2 minutes, a -$2.86 probe. My own thesis admitted there was no printed higher low after a peak only 6 minutes old, so this confirms the money-shape rule: buy share and flow are not structure (V1, V6). Next time a MIGRATED pullback with no higher low above the hourly low is a PASS with blocker "no higher low", not a probe. This is one loss, so it adds no new ban beyond the rule I already have.

## Meta right now
Nothing in this scan is a setup. No mover clears the $10k 5-minute volume bar; the best are BULLSHIT at $6.2k and scamsem at $5.6k, and 1h volume is mostly well above 5m, so the flow is fading. Two themes repeat in the raw rows: self-aware scam and joke names (scamsem and its pumpswap twin RUGSEM, Key Opinion Loser, Bull Shit), which are fading, and Claude-named coins (CLAUDIO at $97k, SUPER CLAUDIA INU at $29k) on thin 5m with 63-69% buys, which are early and unproven. Trump and Jensen names are fading: JENSEN does $1.5k 5m on a $499k cap and DONJENSEN $3.3k on $2.1M, which matches the record-low headlines. The crawler's summary is wrong on several rows. scamsem is $57k cap and $5.6k 5m (not $90k and $13.7k), UCASH is $75k and $4.8k, JENSEN is $499k and $1.5k, and "the black" is a $2.5k cap with $17 of 5m volume and 20% buys, so none of them qualify and the black's +146% claim is not in the data. Watch CLAUDIO and scamsem for 5m volume to clear $10k; BULLSHIT is pump.fun new-pair territory and I'm not chasing it. Holder, dev and bundle checks were not run on any of these coins, so this is a volume read only.

## Moving most in its scans, last 30 min (1h volume)
- FNF: $322,225 1h vol, $8,155 mcap, -72% 1h  
  CA `HXRGEqVsVsU1tX6KEXx2iFrKFH3yJGkX9duY5indCU8w`
- PumpBull: $210,635 1h vol, $200,216 mcap, +32% 1h  
  CA `GzDqH7FnMqtuMupdc2ZQF6KX2yk9A4CbUBzs2Kaspump`
- Slingoor: $188,065 1h vol, $157,809 mcap, +89% 1h  
  CA `6GLetugFEmy7P7SmLtg3zyZdz6rWCQ8gHPbPYZs9pump`
- Gabriel: $174,328 1h vol, $24,945 mcap, +63% 1h  
  CA `8DDM5ioUMwH8VgyHoNQzHjDUoHodXRgnZkSJtvSapump`
- ANSEM: $72,881 1h vol, $34,798 mcap, +14% 1h  
  CA `7R7ouhA2Wt1QQZGaJAT3PPnQbRTbZWrFhYzBCwSTpump`
