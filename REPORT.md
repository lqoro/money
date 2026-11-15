# Trencher live report

Updated 2026-11-15T06:06:16Z (paper trading, never real money)

- Equity: $74.23 (-25.8% vs $100 start)
- Closed trades: 22, 3 wins
- Fees paid: $14.78 (axiom $2.81, network $9.18, pool $2.66), plus $4.15 lost to slippage
- New trades: WATCH-ONLY (scans and decides, buys nothing)
- Brain: subscription, claude-haiku-5-5 for routine calls, claude-opus-5-5 for the daily review; 39 routine calls and 0 plan-limit hits in 48h
- Watch log: 74 coins being followed, 1293 filed, 0 would-buys (6h follow, sampled every 2 min)

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
- 06:05Z: 1 coins, 1 with pairs, 0 passed the market filters, 0 researched

## Coins it looked at, and why it passed
- 06:03Z Chick (FINAL_STRETCH, $19,039 mcap, $20,227 5m vol): PASS at conviction 2, PASS: chasing spike, 3 minutes old, +695% on the 5m, in a 14-copy "optimistic" vamp field with no radar story behind it. Blocker: "chasing spike" (V1, V6, V13).  
  CA `Dueav76X9spnoLomhM2jMkkWorVggbeWucLs3YLupump`
- 05:58Z GATO (DIP, $6,710,136 mcap, $2,491 5m vol): REJECT, Dev holds 3.0% (>1%) (V13, V17)  
  CA `HsprHxBRgiVaQdRf3TnKNuZZtaX9JUSPgMFdAkk6pump`
- 05:58Z SNIFFER (FINAL_STRETCH, $18,303 mcap, $19,686 5m vol): REJECT, Top 10 hold 25.5% ex-pool (>25%) (V13)  
  CA `6CDiNXJTtcgdJs1uGuhK5REFDRYT2AS3RifyanQ7pump`
- 05:58Z FUTA (FINAL_STRETCH, $18,013 mcap, $24,437 5m vol): REJECT, RugCheck danger: Large Amount of LP Unlocked 100.00%  
  CA `FxoXV4C8DTSYeg5dSXrEsr45zzr8tpNbsrpoiZ8Kpump`
- 05:57Z penny (MIGRATED, $32,062 mcap, $2,341 5m vol): PASS at conviction 3, PASS: penny is 76% off its peak in a 12-copy "penny" vamp field, with a 9.5% single bundle and $2.3k of 5m flow. Blocker: "split crowd" and "thin 5m volume" (V1, V3, V6).  
  CA `5gmCPpuktJ7Svjgr4PPJBTosAFKB8K6Z45EGfSUmpump`
- 05:43Z afk (FINAL_STRETCH, $25,218 mcap, $22,595 5m vol): REJECT, RugCheck danger: Large Amount of LP Unlocked 100.00%  
  CA `FWPMa5Z4iwtLbGDLpviBRcBoQkeWSabHYYK4HWUCpump`
- 05:37Z HODL (MIGRATED, $35,268 mcap, $4,342 5m vol): REJECT, Top 10 hold 29.3% ex-pool (>25%) (V13)  
  CA `F63zJ8AM4RnHHxnHzGAPgM8Amv8KTSqG9knPd7yvpump`
- 05:34Z DOGE (DIP, $86,950 mcap, $3,560 5m vol): REJECT, Dip with fading attention is a falling knife, not a dip (5m at 0.26x the hour's pace, under 0.6x)  
  CA `D1noy4QtZiWkH3A8QJGq31HGaAvfvA3bti4C6HLEpump`
- 05:15Z meme (FINAL_STRETCH, $19,001 mcap, $33,787 5m vol): PASS at conviction 3, PASS: "memecoin" is a generic word with 8 same-ticker copies, a chasing spike (+27% on 5m, 6.6x hourly pace) and no printed higher low. Blocker: "chasing spike". (V1, V6, V13)  
  CA `4ed5SsUJeXaDCyM7aGHoA5LBjQjEx3xzVGpYEcMvpump`
- 05:12Z GATO (DIP, $6,838,995 mcap, $2,128 5m vol): REJECT, Dev holds 3.0% (>1%) (V13, V17)  
  CA `HsprHxBRgiVaQdRf3TnKNuZZtaX9JUSPgMFdAkk6pump`

## What its skips did next (last 48h)
A skip "ran" if the coin reached the first target (1.5x) from the skip price before a 20% drop, "dumped" if the drop came first. Sampled every 10 min, followed 6h.
- RugCheck danger: blocked 12, ran 3, dumped 7, flat 1, open 1 (saving losses: keep it)
  - ran: Ivy up to 1.88x  
    CA `DxNF3Qxd8XeUBdz7ReRdoiFzRmNDKbSz4c2oA7aRpump`
  - ran: SI up to 1.93x  
    CA `AiQUqe4zjiDssth2FsCoeQVaGtCtHYyKGX8U52rWpump`
  - ran: FUTA up to 2.77x  
    CA `FxoXV4C8DTSYeg5dSXrEsr45zzr8tpNbsrpoiZ8Kpump`
- top 10 over 25%: blocked 8, ran 0, dumped 6, flat 1, open 1 (saving losses: keep it)
- flow below pace: blocked 4, ran 0, dumped 3, flat 0, open 1 (saving losses: keep it)
- falling knife (code): blocked 4, ran 0, dumped 4, flat 0, open 0 (saving losses: keep it)
- too new / sniping: blocked 4, ran 0, dumped 3, flat 0, open 1 (saving losses: keep it)
- near the high / chasing: blocked 4, ran 1, dumped 3, flat 0, open 0 (saving losses: keep it)
  - ran: penny up to 1.6x  
    CA `5gmCPpuktJ7Svjgr4PPJBTosAFKB8K6Z45EGfSUmpump`
- crowd leaving / fading volume: blocked 2, ran 1, dumped 1, flat 0, open 0 (too few played out to judge)
  - ran: NUREMBERG up to 1.62x  
    CA `7R3RnGmpV9mZXwSyHyKN5LEddiZRmGsYrAZPgDJqpump`
- thin 5m volume: blocked 2, ran 0, dumped 2, flat 0, open 0 (too few played out to judge)
- dev share over 1%: blocked 1, ran 0, dumped 0, flat 0, open 1 (too few played out to judge)
- falling knife / no higher low: blocked 1, ran 0, dumped 0, flat 0, open 1 (too few played out to judge)

## Daily review (2026-11-14, claude-opus-5-5)
This window has no evidence in it. In 24 hours zero coins were logged at any stage: none failed the checklist, none were passed by the brain, none were would-buys and none went unresearched. Nothing settled, nothing is still being followed, and the brain was called once in 48 hours. With n=0, nobody can say anything about an after-cost edge, and the question of whether the routine model's would-buys beat the coins it passed on has no data to answer. The only real finding is that the pipeline looks stalled. A scanner running around the clock should pass at least a handful of coins through the market filters every day. It's also Nov 14, four days after the planned Nov 10 test, so it's worth confirming the watch-only week was captured and archived before anyone talks about edge.
- finding: Every stage has n=0 in the last 24 hours: checklist_failed, brain_passed, would_buy and not_researched. There is no share that ran and no net % to report.
- finding: No coins settled and none are still being followed, so the 6-hour price tracking has nothing to grade.
- finding: skips_48h is empty and top_runners is empty, so there's no record of passed coins running either. You can't tell whether a rule cost us anything.
- finding: The brain made 1 call in 48 hours with 0 plan-limit hits, 0 candidates skipped for lack of a brain and 0 stop reviews without a brain. The usage cap isn't the bottleneck. Too few candidates are reaching the brain at all.
- finding: Cost context from before the pause: 22 trades lost $25.79, and fees plus slippage were $18.83 of that (73%). Fees alone, not bad picks, were most of the loss. Any rule tested later has to clear that cost first.
- idea to test: These come from the guide and from the cost math, not from this window, which has no data. Test them on the full archived Nov 3–10 week only, and require n≥30 per group before believing a net % number.
- idea to test: Cost gate: skip the coin if the estimated round-trip cost for a $10 buy on its pool is above about 4%. Test whether coins with lower costs have a positive net_pct under the simple plan while the rest don't. Fees were 73% of the past loss.
- idea to test: Volume floor: setup=MIGRATED or FINAL_STRETCH and 5m volume ≥ $10k (V1, V6, V13). Compare against $2k–$10k. A small difference in net % after costs means the bar isn't earning its keep.
- idea to test: Flow quality: buy ratio ≥ 0.55 and a flow ratio that shows 5m volume at or above its 1h pace. Check whether this separates coins that hit 1.5x from coins that hit -20% first.
- idea to test: DIP setup: drawdown from the recent high between 40% and 55%, versus 55% to 70%, both with 5m volume ≥ $10k. This tests the house rule that a 70% dip is still buyable against the falling-knife cases.

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
The meta is thin but not dead. The live shapes are animal jokes (COLE, TAIL, PELI, Begcat) and "just hold / go AFK" jokes (afk, HODL), while dollar and "useless" jokes (Stable Inu, Useless Market, MIL) are fading and the news backdrop is bearish. Rising: afk ("buy and go afk", $22.6k 5m, 58% buys, +1017% in the hour) and Trashed Panda (COLE, $9.8k cap, $4.3k 5m, 60% buys, +285%). Fading: MIL (-95%), Begcat and Pelicoin (almost no 5m flow), Stable Inu (-24%). afk is the only coin clearing the $10k 5m bar, but it is 0.3h old and parabolic, so it is research now, and at most a probe on a pullback that holds volume with the stop under that pullback low. COLE is the cleaner animal setup if its 5m reaches $10k with buys holding, and Diamond Hands (HODL, migrated, $35k cap, $4.3k 5m, 55% buys) is a DIP/MIGRATED research name. DOGE on pumpswap is a name-jack of the famous ticker, so verify the real token before anything else. The crawler summary conflicts with the scan (penny $85k vs $27.5k, "nothing reaches $10k" vs afk at $22.6k), so I trust the scan_movers numbers and ignore the unlisted names (Bowser Farts, marmot, Sonny Angel, UpCat). Paper only, not advice.

## Moving most in its scans, last 30 min (1h volume)
- HODL: $91,205 1h vol, $35,268 mcap, +22% 1h  
  CA `F63zJ8AM4RnHHxnHzGAPgM8Amv8KTSqG9knPd7yvpump`
- MIL: $67,376 1h vol, $2,971 mcap, -95% 1h  
  CA `8655LtfvozXLSJWrzcmwVeK13s5Gvn49UXFHYcYzpump`
- GTA: $64,728 1h vol, $90,229 mcap, +53% 1h  
  CA `G9ZMir6uh66Y7viPkXAy7myA9jjE4T1YgheVUmGDpump`
- meme: $58,942 1h vol, $2,608 mcap, -91% 1h  
  CA `4ed5SsUJeXaDCyM7aGHoA5LBjQjEx3xzVGpYEcMvpump`
- BackBid: $58,795 1h vol, $2,224 mcap, -92% 1h  
  CA `CGajmY1RdMWy1QDD9fyUdnoGsmVLDW1xm4yqXdyo3ecs`
