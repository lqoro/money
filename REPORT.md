# Trencher live report

Updated 2026-11-26T10:35:41Z (paper trading, never real money)

- Equity: $74.23 (-25.8% vs $100 start)
- Closed trades: 22, 3 wins
- Fees paid: $14.78 (axiom $2.81, network $9.18, pool $2.66), plus $4.15 lost to slippage
- New trades: WATCH-ONLY (scans and decides, buys nothing)
- Brain: subscription, claude-haiku-5-5 for routine calls, claude-opus-5-5 for the daily review; 408 routine calls and 0 plan-limit hits in 48h
- Watch log: 83 coins being followed, 3836 filed, 0 would-buys (6h follow, sampled every 2 min)

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
- 10:34Z: 1 coins, 1 with pairs, 0 passed the market filters, 0 researched

## Coins it looked at, and why it passed
- 10:25Z PUMPCHAN (MIGRATED, $6,336,866 mcap, $67,826 5m vol): PASS at conviction 3, PASS — big cap, no room. $6.3M mcap, 5m flow at 0.9x pace, first resistance (the $9.1M high) only 1.44x away. Vamp field of 11 same-ticker coins, no catalyst. (V1, V6, V13)  
  CA `Fo2HAwr7ZAUM2bSZ7MWSi16e3aWGpbw5MsUDYCttpump`
- 10:23Z duk (MIGRATED, $37,846 mcap, $4,263 5m vol): REJECT, Top 10 hold 25.9% ex-pool (>25%) (V13)  
  CA `DG2EJSEtPBge5F7zBCTZG78p27LTCiq8tUkJ39qupump`
- 10:21Z konnichiwa (FINAL_STRETCH, $22,642 mcap, $39,209 5m vol): PASS at conviction 3, PASS: up 842% in 5 minutes, one of 18 same-name copies, a bundle cluster sitting inside that crowd, and no X or site to check. That's a split-crowd spike, not a leader (V1, V3, V13).  
  CA `HdRPR3nqkNCt98DWQqDdfkRHDc1NFsgCJVbfXRnppump`
- 10:17Z CGBJ (FINAL_STRETCH, $22,693 mcap, $1,964 5m vol): REJECT, 5m volume $1,964 is dead (<$2,000) (V1)  
  CA `Hnv5e4c8amHREbBDgzxGtaYPVSt7nhrW5AUNS6Q7pump`
- 10:17Z NORFEATH (DIP, $456,375 mcap, $4,887 5m vol): PASS at conviction 3, PASS: no live catalyst, 9 same-ticker copies, 5m flow $4.9k under $10k, and the first resistance is only ~1.16x away. Blocker: "dead story" plus "target too close" (V1, V6, V13).  
  CA `3gmFG4sFDJErDV8pacFrL2uUPXeGJTYLjfRy4hFypump`
- 10:16Z STRUCK (MIGRATED, $66,052 mcap, $105,499 5m vol): REJECT, Bundles: 2 linked wallet cluster(s) hold 42.4% of supply (>20%) (V17)  
  CA `HN9jRRCKuLNL3oSgNV1MBvd3Krg6TingFntJp1PSpump`
- 10:14Z DIGS (MIGRATED, $249,840 mcap, $3,327 5m vol): REJECT, Bundles: 10 linked wallet cluster(s) hold 100.0% of supply (>20%) (V17)  
  CA `9QT8K685Hrae4k11dhGXirdtpfAaimExtyfwt8cPpump`
- 10:12Z TRUMP (FINAL_STRETCH, $14,592 mcap, $19,009 5m vol): PASS at conviction 2, PASS: one of seven "Trump" copies at a 10-minute-old pump.fun coin, top 10 at 22.7%, no X or socials, and 5m volume 6.3x pace after a +32% candle. Vamp field, chasing a spike (V1, V3, V6, V13).  
  CA `3PfQEuGvK97bSPthf1gMkejeAQKEfSPisciU96JRpump`
- 10:11Z CBUCKS (MIGRATED, $6,185,490 mcap, $5,692 5m vol): REJECT, Top 10 hold 25.7% ex-pool (>25%) (V13)  
  CA `DtcicPCKTKeAh7TDEzTym3hXeoHAoMiBdYJhMYxZpump`
- 10:08Z YEE (MIGRATED, $70,658 mcap, $29,544 5m vol): REJECT, Bundles: 3 linked wallet cluster(s) hold 68.5% of supply (>20%) (V17)  
  CA `BKGidSAf6RkUUymQYYoN8ifm3VMsLkeFTocvza3Spump`

## What its skips did next (last 48h)
A skip "ran" if the coin reached the first target (1.5x) from the skip price before a 20% drop, "dumped" if the drop came first. Sampled every 10 min, followed 6h.
- top 10 over 25%: blocked 41, ran 6, dumped 33, flat 0, open 2 (saving losses: keep it)
  - ran: SCF up to 2.01x  
    CA `Az7dYDicMc4G9hwnkeQYwHi6Fop1711C7hABcrWzpump`
  - ran: MARS up to 2.06x  
    CA `816BuXnCFQqt6KXbBTcFgHWD29Ckpaqt8HMKSN4Vpump`
  - ran: 4CHAN up to 1.87x  
    CA `DVdWuNK8ncn79B6z8nCiwcNAiwyFcmBPfChgxJGTpump`
- flow below pace: blocked 36, ran 3, dumped 27, flat 3, open 3 (saving losses: keep it)
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
- near the high / chasing: blocked 27, ran 6, dumped 18, flat 1, open 2 (saving losses: keep it)
  - ran: BRUH up to 1.51x  
    CA `PgFtGGquvnv2zEkjG2N2QPvBTBrafuExGYEqahRpump`
  - ran: SNOWCUMBRR up to 2.36x  
    CA `Gf9wm93TTDpbPC467Eio5Vc42Kr6MAomUD172drWpump`
  - ran: HEYOS up to 1.91x  
    CA `A88p1LcHisrx3TuTwUGVrLtc1LBTUPZUfVgaCGutAFaK`
- RugCheck danger: blocked 27, ran 3, dumped 23, flat 1, open 0 (saving losses: keep it)
  - ran: TROLL up to 1.94x  
    CA `7ykeHoEnjnGkY6tqteXn47fdGtd7kfXWghiyZ7YKpump`
  - ran: Snowball up to 3.52x  
    CA `9TKbd3VFaMSXsEAicD9JVQWpWwAoLi4fSgWmZL2cpump`
  - ran: Bababoi up to 2.17x  
    CA `28B9kDm6XtQNqAkzuiKH3Zu1L8cVM6SLW4iRamFspump`
- too new / sniping: blocked 25, ran 7, dumped 18, flat 0, open 0 (saving losses: keep it)
  - ran: BABYANSEM up to 2.77x  
    CA `F3VctV9FqDgiyqaztN6z78bgWy27eH7DBBHW1vjpump`
  - ran: Merged up to 2.18x  
    CA `AMYpNGi5aGrKr1ZDsotUdWh7k1mMi569ygtaHJmErGEd`
  - ran: Boor up to 1.56x  
    CA `GHFpSSw2ZMjmKCyc1wrHUjJiqnJeP18mekY9GL1Xpump`
- falling knife (code): blocked 18, ran 3, dumped 13, flat 1, open 1 (saving losses: keep it)
  - ran: Jimmies up to 1.53x  
    CA `GisWWjhwrSud4aFGSHvTMt85Ky14sY7LeBFCpfoFpump`
  - ran: Investor up to 1.58x  
    CA `J9eBkCb4UtquAMQqB6duwBmR99fFSMoTnDcaMB9Wpump`
  - ran: MONEY up to 1.58x  
    CA `DeACAbp2GMzapB6Z2K8qdkTZupmNbKc6EZx9bnbCpump`
- bundles over the line: blocked 17, ran 3, dumped 10, flat 1, open 3 (saving losses: keep it)
  - ran: jingyu up to 1.58x  
    CA `DUZrwdjEthcJ99ZiRXr31UuqTohoTg7VjTEyfGdBpump`
  - ran: DUMBMONEY up to 1.74x  
    CA `GEHehS5Rr4rNCjvrHLjjV1avD4bjMsn53ywDGv1spump`
  - ran: WIENER up to 1.59x  
    CA `8BDkDfj3ZUvcG9caGzF2XnHfwg7K6fjfKKDvX6SCpump`
- other: blocked 13, ran 1, dumped 12, flat 0, open 0 (saving losses: keep it)
  - ran: SXI up to 2.34x  
    CA `BFWNbSwRodXPTQqrMSCfhznhJwEzY6ERd6MHjWUEpump`
- dev share over 1%: blocked 12, ran 2, dumped 8, flat 1, open 1 (saving losses: keep it)
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
Trencher, scan_movers read (scan numbers only, web figures conflict and were ignored). Three themes are moving. (1) Cute/greeting and joke names: konnichiwa ($22.6k cap, $39k 5m, 62% buys, ~6 min old) and YEE ($70k cap, $29.5k 5m, 66% buys) are rising, while WIENER ($0 5m, -98% 1h) and Ponzi are dead. (2) Pump-platform and product riffs: STRUCK/SpaceTruck ($66k cap, $105k 5m, 56% buys, ~6 min old), PumpChan ($6.3M cap, $74k 5m, 61% buys) and PELAGO carry the most flow, while PPV/Pay Per View is down 90% in an hour. (3) Trump-named coins: "I Am Not Corrupt" (TRUMP, $14.6k cap, $19k 5m, +267% 1h) is hot, but it names a political figure, so it's a pass under the political-figure rule, and the web's Trump token headlines (down 99%, gala demand collapsing) say the big-name version is fading. Fading: old tickers CBUCKS and DIGS (600-1200h old, thin 5m) and the dumpers. Setups to research, not buys: STRUCK and konnichiwa (conviction 4-5, bundle, dev and holder checks first, stop at -30%, out if 5m volume drops under $10k), and YEE as a migrated-range check. Nothing named for a hack appears in the movers. Paper only, not financial advice.

## Moving most in its scans, last 30 min (1h volume)
- PUMPCHAN: $911,068 1h vol, $6,316,547 mcap, +17% 1h  
  CA `Fo2HAwr7ZAUM2bSZ7MWSi16e3aWGpbw5MsUDYCttpump`
- STRUCK: $132,605 1h vol, $66,052 mcap, +125% 1h  
  CA `HN9jRRCKuLNL3oSgNV1MBvd3Krg6TingFntJp1PSpump`
- PPV: $83,502 1h vol, $2,665 mcap, -90% 1h  
  CA `CbGrZ3Q2XxSV2oiZsLkDWW1GFjrqUDAzTH9XwVr1pump`
- YEE: $80,245 1h vol, $70,658 mcap, +139% 1h  
  CA `BKGidSAf6RkUUymQYYoN8ifm3VMsLkeFTocvza3Spump`
- Saxon: $62,532 1h vol, $2,262 mcap, +13% 1h  
  CA `F4JRm4qE6UJesCPc4NPwJwosYqNGsFWoFGfZJe6zpump`
