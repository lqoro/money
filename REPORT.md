# Trencher live report

Updated 2026-11-26T06:33:22Z (paper trading, never real money)

- Equity: $74.23 (-25.8% vs $100 start)
- Closed trades: 22, 3 wins
- Fees paid: $14.78 (axiom $2.81, network $9.18, pool $2.66), plus $4.15 lost to slippage
- New trades: WATCH-ONLY (scans and decides, buys nothing)
- Brain: subscription, claude-haiku-5-5 for routine calls, claude-opus-5-5 for the daily review; 406 routine calls and 0 plan-limit hits in 48h
- Watch log: 103 coins being followed, 3760 filed, 0 would-buys (6h follow, sampled every 2 min)

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
- 06:32Z: 5 coins, 4 with pairs, 0 passed the market filters, 0 researched

## Coins it looked at, and why it passed
- 06:29Z NORFEATH (DIP, $454,580 mcap, $2,809 5m vol): REJECT, Dip with fading attention is a falling knife, not a dip (5m at 0.54x the hour's pace, under 0.6x)  
  CA `3gmFG4sFDJErDV8pacFrL2uUPXeGJTYLjfRy4hFypump`
- 06:26Z DIGS (MIGRATED, $262,891 mcap, $2,497 5m vol): REJECT, Bundles: 10 linked wallet cluster(s) hold 100.0% of supply (>20%) (V17)  
  CA `9QT8K685Hrae4k11dhGXirdtpfAaimExtyfwt8cPpump`
- 06:22Z Elonmas (DIP, $70,101 mcap, $17,537 5m vol): REJECT, Dip with fading attention is a falling knife, not a dip (5m at 0.58x the hour's pace, under 0.6x)  
  CA `DMXm1gSmAZn1RV4fGXGG8Y1cXfKWXMDYaiKF4B6Cpump`
- 06:17Z FIONA (DIP, $1,968,669 mcap, $3,036 5m vol): REJECT, Bundles: 10 linked wallet cluster(s) hold 30.2% of supply (>20%) (V17)  
  CA `B34nXKzCgsJb9ChLuSHPRpXLE3WFSWyeT8Cqkzzmpump`
- 06:12Z Grodia (DIP, $832,221 mcap, $5,834 5m vol): PASS at conviction 3, PASS — DIP with no catalyst, no printed higher low, and a story the radar never names. The site doesn't show this CA. Wait. (V1, V13)  
  CA `6HS1aeSk7osT5B1CzLp1HTRTAweFr5wurfMHS4vppump`
- 06:09Z UHI (MIGRATED, $962,432 mcap, $5,132 5m vol): PASS at conviction 3, PASS — flow below pace, no printed higher low, and the site doesn't show a CA. A vamp field of 21 copies, and the Elon correction meme has already printed. (V1, V3, V13)  
  CA `Bnw5JRPek5JvJhzUiB9yrs2cmzt4bLeFqSRzDzSppump`
- 06:04Z ccat (MIGRATED, $34,353 mcap, $2,881 5m vol): PASS at conviction 3, PASS: chasing a 5.8x volume spike on a 15-copy clan-cat field, no narrative on the radar, no printed higher low, top 10 at 23%. Wait. (V1, V6, V13)  
  CA `3jAB5ksB13Kgm2Q39NU6d2USUxBy2f9LaTvyay6Gpump`
- 06:02Z TEEETHY (DIP, $62,176 mcap, $7,650 5m vol): PASS at conviction 4, PASS: bottom buy with no catalyst, theme pace 0.79x, 5m flow $7.6k under the $10k bar and buys 50%. Named story, clean holders, still no entry. (blocker: dead story / no catalyst)  
  CA `BbC8hVHJ2bo6xFcGh2X6zcMiv1T1rznQd3qWoxXApump`
- 06:02Z Elonmas (MIGRATED, $111,545 mcap, $24,440 5m vol): PASS at conviction 3, PASS: too new, flow below pace, and a bigger Elonmas copy is taking the crowd. Blocker: "too new" and "flow below pace". (V1, V3, V6)  
  CA `6B5X3keXJ4J8LLvswa2mbqMhrRDbt85Jo88sbB6apump`
- 05:44Z NORFEATH (MIGRATED, $535,784 mcap, $3,307 5m vol): PASS at conviction 3, PASS: flow at 0.67x pace on $3.3k 5m, first resistance only ~1.2x away, theme pace 0.64x. Parade date is a catalyst, not a buy. (V1, V6)  
  CA `3gmFG4sFDJErDV8pacFrL2uUPXeGJTYLjfRy4hFypump`

## What its skips did next (last 48h)
A skip "ran" if the coin reached the first target (1.5x) from the skip price before a 20% drop, "dumped" if the drop came first. Sampled every 10 min, followed 6h.
- top 10 over 25%: blocked 37, ran 6, dumped 28, flat 1, open 2 (saving losses: keep it)
  - ran: SCF up to 2.01x  
    CA `Az7dYDicMc4G9hwnkeQYwHi6Fop1711C7hABcrWzpump`
  - ran: MARS up to 2.06x  
    CA `816BuXnCFQqt6KXbBTcFgHWD29Ckpaqt8HMKSN4Vpump`
  - ran: 4CHAN up to 1.87x  
    CA `DVdWuNK8ncn79B6z8nCiwcNAiwyFcmBPfChgxJGTpump`
- flow below pace: blocked 35, ran 3, dumped 27, flat 2, open 3 (saving losses: keep it)
  - ran: BOOBS up to 1.51x  
    CA `E35iEA2yLLHc1tjm6et1Z3YuH8DhxJYWtWezPHgSpump`
  - ran: BASKET up to 1.55x  
    CA `3Tg6YnNrfPdFfsY14MaNsDMWLseAyrUDS3myJtbaJN6f`
  - ran: BIAO up to 1.51x  
    CA `As3XtYSstuVdrVyb6sJZZ77Tu8JvjTBg6S6hgPv4pump`
- brain paced: blocked 35, ran 10, dumped 24, flat 1, open 0 (saving losses: keep it)
  - ran: Scamsem up to 1.56x  
    CA `5JWeGmA9z6yHd5F9P6B23A8wthho8BpZuDmQv5DfLoat`
  - ran: RUGSEM up to 1.5x  
    CA `9cDnmLRDWeJzcpyw8tSFAT7HS4Aunx6MmZWjMfrzpump`
  - ran: SHHFT up to 1.61x  
    CA `GqMg4TRt5U5HRK6oeZYwCF1Jz7Ym9MSzWSoFCtFsbzf6`
- RugCheck danger: blocked 29, ran 3, dumped 25, flat 0, open 1 (saving losses: keep it)
  - ran: TROLL up to 1.94x  
    CA `7ykeHoEnjnGkY6tqteXn47fdGtd7kfXWghiyZ7YKpump`
  - ran: Snowball up to 3.52x  
    CA `9TKbd3VFaMSXsEAicD9JVQWpWwAoLi4fSgWmZL2cpump`
  - ran: Bababoi up to 2.17x  
    CA `28B9kDm6XtQNqAkzuiKH3Zu1L8cVM6SLW4iRamFspump`
- near the high / chasing: blocked 26, ran 5, dumped 17, flat 1, open 3 (saving losses: keep it)
  - ran: BRUH up to 1.51x  
    CA `PgFtGGquvnv2zEkjG2N2QPvBTBrafuExGYEqahRpump`
  - ran: SNOWCUMBRR up to 2.36x  
    CA `Gf9wm93TTDpbPC467Eio5Vc42Kr6MAomUD172drWpump`
  - ran: HEYOS up to 1.91x  
    CA `A88p1LcHisrx3TuTwUGVrLtc1LBTUPZUfVgaCGutAFaK`
- too new / sniping: blocked 24, ran 7, dumped 16, flat 0, open 1 (saving losses: keep it)
  - ran: BABYANSEM up to 2.77x  
    CA `F3VctV9FqDgiyqaztN6z78bgWy27eH7DBBHW1vjpump`
  - ran: Merged up to 2.18x  
    CA `AMYpNGi5aGrKr1ZDsotUdWh7k1mMi569ygtaHJmErGEd`
  - ran: Boor up to 1.56x  
    CA `GHFpSSw2ZMjmKCyc1wrHUjJiqnJeP18mekY9GL1Xpump`
- falling knife (code): blocked 19, ran 3, dumped 12, flat 1, open 3 (saving losses: keep it)
  - ran: Jimmies up to 1.53x  
    CA `GisWWjhwrSud4aFGSHvTMt85Ky14sY7LeBFCpfoFpump`
  - ran: Investor up to 1.58x  
    CA `J9eBkCb4UtquAMQqB6duwBmR99fFSMoTnDcaMB9Wpump`
  - ran: MONEY up to 1.58x  
    CA `DeACAbp2GMzapB6Z2K8qdkTZupmNbKc6EZx9bnbCpump`
- bundles over the line: blocked 13, ran 2, dumped 8, flat 0, open 3 (saving losses: keep it)
  - ran: jingyu up to 1.58x  
    CA `DUZrwdjEthcJ99ZiRXr31UuqTohoTg7VjTEyfGdBpump`
  - ran: DUMBMONEY up to 1.74x  
    CA `GEHehS5Rr4rNCjvrHLjjV1avD4bjMsn53ywDGv1spump`
- other: blocked 13, ran 1, dumped 12, flat 0, open 0 (saving losses: keep it)
  - ran: SXI up to 2.34x  
    CA `BFWNbSwRodXPTQqrMSCfhznhJwEzY6ERd6MHjWUEpump`
- dev share over 1%: blocked 11, ran 2, dumped 8, flat 1, open 0 (saving losses: keep it)
  - ran: PI up to 1.77x  
    CA `D2AK5DvBj8AxN5VX1t6bjv7muJVPUx4hFPowVRWYpump`
  - ran: Grinch up to 1.94x  
    CA `J1b5HnRzmXsYK5akPTFtBR7B4E74JG8eyULodd7ypump`

## Daily review (2026-11-25, claude-opus-5-5)
Nothing has a positive edge after costs. All 213 settled coins came out at -12.2% net under the simple plan, and every setup and stage is negative: MIGRATED -10.0%, FINAL_STRETCH -15.3%, DIP -19.8%. The cost estimate, about 9.8% round trip on a $10 buy, is what kills it. Before costs, MIGRATED (about -0.3%) and the coins the brain reviewed (about +0.8%) are close to break-even. With a 1.5x target, a -20% stop and about 10% cost, a coin set needs roughly 42% of its coins to hit the target before the stop just to break even. The best group here gets 28.6%. With n=213, repeat entries for the same coin and coins from the same meme moving together, the before-cost numbers are within noise of zero. The after-cost loss is not noise. I can't say whether the routine model's would-buys beat its passes: it logged 0 would-buys in 24h. Every coin that reached it was passed, so the only split we can measure is the checklist. Checklist-passed coins ran 28.6% of the time vs 15.8% for checklist failures, and netted -9.0% vs -15.6%.
- finding: Overall (n=213): 22.5% ran, 66.2% dumped, median peak 1.27x, 20.7% hit 2x, net -12.2% after an average 9.8% cost. Before costs that is about -2.4%. Fees, not picks, are most of the loss, the same as in the 22 real trades ($18.83 of the $25.79 was fees).
- finding: Break-even math for the simple plan: a win nets about +40% (50 - 9.8) and a stop nets about -30% (-20 - 9.8), so about 42% of coins must hit 1.5x first. With zero costs the bar falls to about 29%. Brain-reviewed coins sit right at that zero-cost bar (28.6% ran) and still lose 9% after costs.
- finding: MIGRATED (n=147) is the least bad setup: 25.2% ran, median peak 1.33x, net -10.0% (gross about -0.3%). It is the only setup worth testing further.
- finding: FINAL_STRETCH (n=43): 20.9% ran, but 79.1% dumped (the highest), net -15.3%. Two of the top five runners came from here (Memeployed 15.2x, FUCKCANCER 7.6x, both around $18k mcap), but the average still loses. One-in-twenty tails don't save a fixed 1.5x/-20% plan.
- finding: DIP (n=23): 8.7% ran, 13.0% hit 2x, net -19.8% (gross about -10%). It is the worst setup on every measure, though the sample is small.
- idea to test: Cost gate: only count coins whose logged est_cost_pct at the intended size is ≤4%. Re-run net on that subset. If no subset with costs that low exists, this strategy has no edge at $10 sizing, whatever the picks.
- idea to test: Setup filter: setup == MIGRATED AND checklist == pass. Measure net and the run rate in which 1.5x is hit before the stop. This is the only group close to gross break-even, so check whether it holds across the full week.
- idea to test: Drop DIP, or allow it only when drawdown is 40-55% from the high AND flow ratio (5m/hourly pace) ≥1.0 AND buy ratio ≥0.55. Compare the result against dropping DIP entirely.
- idea to test: FINAL_STRETCH only if 5m volume ≥ $10k AND buy ratio ≥0.55 AND mcap ≥ $15k. Otherwise exclude it. Check whether the 79% dump rate falls below about 60%.
- idea to test: Young MIGRATED test: setup == MIGRATED AND age_hours ≤1 AND mcap between $100k and $300k AND checklist pass. Expect survivorship to shrink the edge. Only accept it if n ≥ 40 for the week and net > 0 after costs.

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
Not quiet, but thin: the volume sits in coins under about 2h old, while the older big caps are dead on the 5m (Fiona at $2M with $2.1k, UHI and Grodia under $6k). Two themes are rising across several movers. Celebrity-name pulls: Elonmas on two CAs ($112k and $72k, $24k and $23k 5m, +290% and +138% 1h, buyers 56-58%) and MuskGiving (+300% 1h on $8.6k, but only $2.6k 5m). Early holiday names: Rizzclaus (6 min old, $13.7k 5m on a $4.4k cap, a turnover that looks wash or bundled until proven otherwise) against Chillmas (-70% 1h, zero 5m). Animal mascots are mixed: the hippo cluster looks alive on the web but Fiona is dead on the 5m, clancat holds $3.2k at +22%, and Squidtard and Jamtis are dead. Fading: news-named Block0 (-43%) and the sub-hour joke launches. Trump, ANSEM and the Block0 fee headlines are in the web text but not in the movers, so the news is not what is moving money right now. Setups: Elonmas CA 6B5X... ($112k, $24k 5m, 58% buys, under 12h, pumpswap) is the only mover that clears the MIGRATED bars on paper. It is a duplicate name, though, so I research it only after I know which CA is the original and the other is the vamp; conviction 4 until then, becoming a 5 probe at most if it is the original and the holder and bundle checks come back clean. Stop at -30%, and out if the 5m falls under $10k. The FRITZ setup from the web summary is dropped: no CA in the scan, its 5m and buy figures don't match the scan, and its $71k and +138% match Elonmas CA2, so it may be a mislabel. Fiona, Norfeather and TEEETHY (under $9k 5m) are not buys until the 5m clears $10k. Rizzclaus is a new pair, which we don't snipe. This is a research read from scan data, and the holder, dev and bundle checks are still unrun on each coin, so none of this is a buy. Paper only, nothing here is financial advice.

## Moving most in its scans, last 30 min (1h volume)
- Elonmas: $367,568 1h vol, $71,828 mcap, +138% 1h  
  CA `DMXm1gSmAZn1RV4fGXGG8Y1cXfKWXMDYaiKF4B6Cpump`
- FRITZ: $126,316 1h vol, $1,435 mcap, -98% 1h  
  CA `4VMwK3shXxsaMbiJ4qtBMMEgi63riezBSWFHfA6Vpump`
- hoss: $75,704 1h vol, $6,635 mcap, +196% 1h  
  CA `EvTaKHSWxhvqfdLNLJnuX8DMZyQA8Kg9nTNmhQhYpump`
- UHI: $66,261 1h vol, $977,824 mcap, -10% 1h  
  CA `Bnw5JRPek5JvJhzUiB9yrs2cmzt4bLeFqSRzDzSppump`
- Grodia: $63,919 1h vol, $836,666 mcap, -16% 1h  
  CA `6HS1aeSk7osT5B1CzLp1HTRTAweFr5wurfMHS4vppump`
