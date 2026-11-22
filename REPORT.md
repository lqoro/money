# Trencher live report

Updated 2026-11-22T00:24:32Z (paper trading, never real money)

- Equity: $74.23 (-25.8% vs $100 start)
- Closed trades: 22, 3 wins
- Fees paid: $14.78 (axiom $2.81, network $9.18, pool $2.66), plus $4.15 lost to slippage
- New trades: WATCH-ONLY (scans and decides, buys nothing)
- Brain: subscription, claude-haiku-5-5 for routine calls, claude-opus-5-5 for the daily review; 280 routine calls and 0 plan-limit hits in 48h
- Watch log: 84 coins being followed, 2471 filed, 0 would-buys (6h follow, sampled every 2 min)

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
- 00:23Z: 2 coins, 1 with pairs, 0 passed the market filters, 0 researched

## Coins it looked at, and why it passed
- 00:21Z STREETS (MIGRATED, $715,162 mcap, $584,733 5m vol): REJECT, Top 10 hold 29.8% ex-pool (>25%) (V13)  
  CA `GY23CdhszidJZpLyNQ9PB63HPXq8RXqhnLtUYUH7pump`
- 00:16Z RIZZMAS3 (MIGRATED, $43,211 mcap, $31,671 5m vol): REJECT, RugCheck danger: Creator history of rugged tokens  
  CA `BQcV4Ryfu9bZK8egAF89AhkojdJqAaDt4xTFwUQ2pump`
- 00:12Z SBS (MIGRATED, $166,359 mcap, $2,430 5m vol): PASS at conviction 2, PASS: flow below pace (0.96x hourly), 5m $2.4k, and the drawdown number is broken data. Not a DIP, not a buy. (V1, V6, V13)  
  CA `4mE8dPH1RTqQBT5EPim5Ubt2v2wXZ9zgEDDWmL1o1EYu`
- 00:11Z SHIT (MIGRATED, $637,094 mcap, $12,276 5m vol): PASS at conviction 2, PASS: blocker "dead story". Down 82% from a $3.6M peak, 5m flow at 0.61x the hourly pace, and the theme is at 0.3x pace with no outside catalyst. Clean holders don't fix that (V1, V6, V13).  
  CA `Fn95NtGXWPaJXc4N5y9rVkUq1NwZbjBNJzPVvNRLpump`
- 00:07Z time (MIGRATED, $69,282 mcap, $31,784 5m vol): PASS at conviction 2, PASS: chasing spike. Up 27% on 5m at 3.4x hourly pace, 12 minutes old, no printed higher low, and two bigger "time" copies split the crowd (V1, V6, V3).  
  CA `Ak8pAMMeiqbu3tyE2MU33o8W2RfhLk1hXYsscnFkpump`
- 00:04Z C@T (MIGRATED, $215,104 mcap, $82,044 5m vol): REJECT, Top 10 hold 49.3% ex-pool (>25%) (V13)  
  CA `8R7rompcCDEZKGjRRybZt1UrDrZTdmSXqFjDtvSCpump`
- 00:01Z MANEKI (DIP, $36,638 mcap, $2,233 5m vol): REJECT, Dip with fading attention is a falling knife, not a dip (5m at 0.39x the hour's pace, under 0.6x)  
  CA `G74SSWk4qF4BeWfyR53fVZYqdNWo9wH7UR55jF4uuxds`
- 23:59Z URANUS (MIGRATED, $60,772 mcap, $2,782 5m vol): PASS at conviction 3, PASS: no breakout, no higher low, and the theme is at 0.38x its hourly pace. Stop at 5% off the high and sit on the flow leader (V1, V6).  
  CA `DUvFjnaE3r46WLbz9rz6MNk2bq9xPFPUfMd8bDgmpump`
- 23:58Z CUNTS (FINAL_STRETCH, $23,358 mcap, $9,323 5m vol): PASS at conviction 3, PASS: chasing spike. CUNTS is up 78% on 5m, sitting at its high, with 5m volume under $10k and 25 copies in the field. Blocker: "chasing spike" (V1, V6).  
  CA `7CvW68FD9KjNYGByfykhaNps7VNPLN8dFwMRfmgQpump`
- 23:57Z Wow (FINAL_STRETCH, $19,980 mcap, $4,309 5m vol): PASS at conviction 3, PASS: blocker "no live narrative". Wow cat is a 8-copy cat/wow vamp field on a 10x spike that is already 20% off its high, with $4.3k 5m under the $10k bar and no radar story behind it. (V1, V6, V13)  
  CA `4jPVfKpDNzZ9WrVrPoDBAGPsVcu8zbkN2WUw5GiCpump`

## What its skips did next (last 48h)
A skip "ran" if the coin reached the first target (1.5x) from the skip price before a 20% drop, "dumped" if the drop came first. Sampled every 10 min, followed 6h.
- flow below pace: blocked 27, ran 5, dumped 18, flat 0, open 4 (saving losses: keep it)
  - ran: AI up to 1.51x  
    CA `8SacNb6sgiAcscRe4m915B6nL9XX55dk8FS7L532pump`
  - ran: SWRDXSTFF up to 1.77x  
    CA `Csoj9XHJfBAxsKswqKKBENnGeoRDHtACfyYi7HmJpump`
  - ran: Trader up to 2.04x  
    CA `BYKQkHKMWHidNBLQXgt7NX4PLUtJZRYGLWQYkJzPGenX`
- top 10 over 25%: blocked 26, ran 1, dumped 23, flat 1, open 1 (saving losses: keep it)
  - ran: :) up to 1.65x  
    CA `Dtx414D8jurspmB1jqJWsYU66pemoXRjQeXx7TC1pump`
- too new / sniping: blocked 21, ran 3, dumped 17, flat 1, open 0 (saving losses: keep it)
  - ran: AudaCity up to 1.96x  
    CA `3rtTUCpe1BBgCTNWQ9jK3xkAz1E7SPqMt4uYHx1Bpump`
  - ran: TA up to 1.77x  
    CA `DKUM8qywmi8X9RYK2wUgnTw8QKjh1nYDThZR1GXPpump`
  - ran: time up to 1.65x  
    CA `Ak8pAMMeiqbu3tyE2MU33o8W2RfhLk1hXYsscnFkpump`
- near the high / chasing: blocked 20, ran 5, dumped 15, flat 0, open 0 (saving losses: keep it)
  - ran: BEAR up to 2.32x  
    CA `DCPm44cT9i39HjR13QHYgxkR7wEx9TDeniGuayB5pump`
  - ran: ZOL up to 1.55x  
    CA `UQLWvkwiSsnViuVBy7oArMtzb5RAZyrdJ79amQFrzoL`
  - ran: STICK up to 2.08x  
    CA `532iaQrhFCD3QKFHsAtFAQ1mQZMjMdNrPXLeCS6cpump`
- RugCheck danger: blocked 17, ran 2, dumped 13, flat 0, open 2 (saving losses: keep it)
  - ran: TOP up to 1.67x  
    CA `hT9xKkj6dPMz97zcxEEE5T5fFdm6x31P6FodwT8pump`
  - ran: CAP up to 2.6x  
    CA `CxGYpWoTun4J3xD4cNwXFRn2W3RzJozTxyU9nbJ4pump`
- falling knife (code): blocked 14, ran 1, dumped 12, flat 1, open 0 (saving losses: keep it)
  - ran: MANEKI up to 2.06x  
    CA `G74SSWk4qF4BeWfyR53fVZYqdNWo9wH7UR55jF4uuxds`
- thin 5m volume: blocked 11, ran 1, dumped 8, flat 1, open 1 (saving losses: keep it)
  - ran: chud up to 1.55x  
    CA `EV7J2QaPXPytSkM1LD9GPRkgAbmSEr9R3kYiXBzbpump`
- bundles over the line: blocked 8, ran 0, dumped 5, flat 1, open 2 (saving losses: keep it)
- falling knife / no higher low: blocked 8, ran 3, dumped 3, flat 0, open 2 (mixed)
  - ran: pCAT up to 1.58x  
    CA `BLdC7hwRijHudKYDmtEkx1SHUdBWm8XbjBCSvwa6pump`
  - ran: MACCA up to 1.71x  
    CA `C5eGEXJZYvXEbKdyvPtasksjGNV4xvMowpKM92bVv47f`
  - ran: UrAnus up to 2.97x  
    CA `27u3diWofnXGUkddjLGhcy1nRssFKHW3RtNbpWzUpump`
- dev share over 1%: blocked 7, ran 2, dumped 3, flat 1, open 1 (mixed)
  - ran: SANTINU up to 1.56x  
    CA `BCTwG3LDhNcthcK374aWQfAzLYGRXDu1apmrqw3Tpump`
  - ran: Mfer up to 1.55x  
    CA `9tX1UpBGeNqMb1VqqzVumwzW71ybsNZFyWKYiL8Ppump`

## Daily review (2026-11-21, claude-opus-5-5)
Nothing has a positive after-cost edge. All 98 settled coins average -15.7% net under the simple plan, and every setup and stage is negative: MIGRATED -13.6% (n=70), FINAL_STRETCH -20.0% (n=14), DIP -21.7% (n=14). The main reason is the 9.5% average round-trip cost on a $10 buy. With a +50%/-20% bracket and that cost, a coin nets about +40% when it runs and about -30% when it dumps, so the plan breaks even only if roughly 42% of coins run. The observed rate is 16.3% (95% CI about 9–24%), so the overall verdict is solid even at n=98. The per-setup splits are not: n=14 gives about ±19 points, and coins from the same day and meta move together. I can't answer whether the routine model's would-buys beat its passes because it made zero would-buys. It declined all 49 coins it reviewed, including all 5 of the day's 4.5–5.5x runners. Even so, declining was right on average, since that reviewed group nets -16.2% under the simple plan.
- finding: Costs are bigger than the price edge. Average cost is 9.5% per round trip, and the gross result before costs is only about -6%. At this size, even a coin-flip entry would bleed about 10% a trade. This matches the paper trades: $18.83 of the $25.79 loss was fees and slippage.
- finding: MIGRATED is the least bad setup: n=70, 18.6% ran, 20.0% hit 2x, net -13.6%. It still needs about 2.3x its current run rate to break even.
- finding: DIP is the worst setup: n=14, 7.1% ran (1 coin), 0% hit 2x, 78.6% dumped, net -21.7%. Not one dip buy produced a 2x in 24h. That fits 'a dip with fading volume is a falling knife', but n=14 is small.
- finding: FINAL_STRETCH: n=14, 28.6% hit 2x (4 coins) but only 14.3% ran (2 coins), net -20.0%. Half the coins that eventually doubled hit -20% before +50%. That looks like the V1 pre-bond dump shaking out a tight stop. Too few samples to act on alone.
- finding: Overall, 18.4% of coins hit 2x but only 16.3% ran under the bracket. Some later winners dipped through -20% first, so the -20% stop is clipping part of the right tail.
- idea to test: Cost gate: skip when the estimated round-trip cost is above about 5%. Also re-run the whole week at $25 and $50 sizes to see how much of the 9.5% is fixed (priority fee, bribe) versus slippage. If the fixed part dominates, size is the biggest lever and no entry rule fixes it.
- idea to test: Exit variant: re-score every setup with stop -35% instead of -20%, sell initials at 2x, trail the rest by 30% from peak, and a 60-minute time stop. Test it first on brain-reviewed coins (n=49 today, 28.6% hit 2x) to see whether the right tail pays for the wider stop after costs.
- idea to test: Young small-cap bucket: setup in {FINAL_STRETCH, MIGRATED}, age ≤ 1h, mcap $14k–$60k, checklist passed. Report n, ran %, 2x % and net for the whole bucket, not just the winners. Only consider it if net beats 0 with n ≥ 50 across at least 4 different days.
- idea to test: Turn DIP off for evaluation unless a narrower version proves itself: DIP with 5m volume ≥ 1h pace, buy ratio ≥ 0.55 and drawdown 40–60%. It needs net > 0 on at least 30 week samples. Otherwise drop DIP.
- idea to test: FINAL_STRETCH stop test: bracket +100%/-35% against +50%/-20%, to check whether the pre-bond dump is what's stopping out the eventual 2x coins.

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
Meta: fresh pump.fun launches with crude-joke, cult-slang and animal names are getting the volume and the buyers. "time" ($72k cap, 66% buys, +143% 1h), C@T ($215k, +511% 1h, $82k 5m, 86% buys), KAREN ($32k, 55% buys) and CUNTS ($22k, $9.5k 5m) are the active ones. Older dog and animal coins are fading or thin: MAYA ($719k, -26% 1h, only $2.5k 5m) and GATO (2,123h old, 33% buys, $503 5m). Trump and news-name coins aren't on the movers list, so the headlines aren't the trade (V1). Setups to research, no entries yet: "time" and KAREN fit the MIGRATED screen (pumpswap, under 12h, cap above $30k, 5m above $10k), so holder, bundle and dev checks come before any size (V1, V6). C@T is the strongest tape, but +511% in an hour is a chase, so it only qualifies on a pullback where buyers hold. SHIT is a DIP candidate: -63% in 1h with 89% buys on $13k 5m, and it only qualifies if its prior peak was above $70k (V1). The crawler's tapcash, Mfer and PUNANI figures don't match scan_movers, so I'm ignoring them. The tape is active, not quiet, and spike-and-dump, so every size stays small and conviction-based.

## Moving most in its scans, last 30 min (1h volume)
- BIGFOOT: $1,239,780 1h vol, $1,381 mcap, -99% 1h  
  CA `EMjVCbyVHVZ88zvmQPVZffB6Nk2eksS6aCACGVGnpump`
- STREETS: $751,699 1h vol, $629,500 mcap, +451% 1h  
  CA `GY23CdhszidJZpLyNQ9PB63HPXq8RXqhnLtUYUH7pump`
- Inu: $377,429 1h vol, $2,706 mcap, -92% 1h  
  CA `7htmi1ohL8vgAxmdLtvyXR2Z4As6bj6dXEx5wRh78VJG`
- SHIT: $243,179 1h vol, $653,481 mcap, -63% 1h  
  CA `Fn95NtGXWPaJXc4N5y9rVkUq1NwZbjBNJzPVvNRLpump`
- time: $113,852 1h vol, $71,771 mcap, +143% 1h  
  CA `Ak8pAMMeiqbu3tyE2MU33o8W2RfhLk1hXYsscnFkpump`
