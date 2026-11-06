# Trencher live report

Updated 2026-11-06T00:35:23Z (paper trading, never real money)

- Equity: $74.23 (-25.8% vs $100 start)
- Closed trades: 22, 3 wins
- Fees paid: $14.78 (axiom $2.81, network $9.18, pool $2.66), plus $4.15 lost to slippage
- New trades: WATCH-ONLY (scans and decides, buys nothing)
- Brain: subscription, claude-haiku-5-5 for routine calls, claude-opus-5-5 for the daily review; 489 routine calls and 0 plan-limit hits in 48h
- Watch log: 96 coins being followed, 1079 filed, 0 would-buys (6h follow, sampled every 2 min)

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
- 00:34Z: 2 coins, 1 with pairs, 0 passed the market filters, 0 researched

## Coins it looked at, and why it passed
- 00:28Z GLITCH (MIGRATED, $3,132,457 mcap, $943 5m vol): REJECT, 5m volume $943 is dead (<$2,000) (V1)  
  CA `8Xg89xT8Ve34sKiYqYuMs46mycREsCA2F362UscRpump`
- 00:28Z BFN (FINAL_STRETCH, $20,956 mcap, $7,973 5m vol): REJECT, Top 10 hold 25.6% ex-pool (>25%) (V13)  
  CA `2WBx8bdnKC2PrY1hvbCjDSkYy2JLhPMda5UemmuBWDEW`
- 00:14Z Bear (no setup, $17,756 mcap, $17,365 5m vol): REJECT, No setup fits: not Final Stretch, not a migrated runner, not a healthy dip  
  CA `AX56XAixNhncCoqW3AdKmE6KsZuiuNTqPvNYTa5Ypump`
- 00:12Z sssdfg (DIP, $183,903 mcap, $56,690 5m vol): REJECT, Dip with fading attention is a falling knife, not a dip (5m at 0.56x the hour's pace, under 0.6x)  
  CA `BQjiYCutv9LVtbgj7pKCN2Ce6k2eUM5RSKs6kDAzpump`
- 00:09Z COGE (MIGRATED, $2,883,411 mcap, $4,124 5m vol): PASS at conviction 3, PASS. Chasing 9% off the high, the first resistance is only 1.10x away, 5m flow is under $10k in a crowded copy field, and the project's own site doesn't show this CA. (V1, V6, V13)  
  CA `8UQdy5sHMVWUWSHeA5B3ZuuAVNumjSLPXdf19MXcpump`
- 23:54Z LEAP (FINAL_STRETCH, $26,877 mcap, $3,272 5m vol): REJECT, Top 10 hold 29.6% ex-pool (>25%) (V13)  
  CA `Ex4sJY2KjgQhgwFTfyfPzPUbpUu5g53W9FxfvRVGpump`
- 23:54Z Bubbles (MIGRATED, $162,819 mcap, $3,954 5m vol): PASS at conviction 3, PASS — 5m flow is $3.9k, under the $10k bar, and the coin sits 12% off its high with no breakout printing. It's one of 16 same-ticker copies with no narrative on the radar. Blocker: "no breakout" (V1, V6, V13).  
  CA `DNerJKigs1xZ5rCBDtU9a2ACxvskScMnSihWY9yYpump`
- 23:45Z TOYS4KIDS (MIGRATED, $73,556 mcap, $9,561 5m vol): PASS at conviction 3, PASS: TOYS4KIDS is the leader of a 9-copy same-name field running at 0.04x its theme's hourly pace, with 5m flow at 0.6x its own pace and $9.6k on the 5m. Blocker: flow below pace. (V1, V6)  
  CA `FqJu1nmcNP8fCJfAW7Y4dGmp6fF9iF2RxrqMSFAcpump`
- 23:44Z COPE (MIGRATED, $396,179 mcap, $91,079 5m vol): PASS at conviction 3, PASS: chasing. COPE is 7.8% off a $430k high after +708% in an hour, with no printed higher low and a 1.08x first target. A farm-shaped spike, not a pullback (V1, V6).  
  CA `g8FFFJHQnd84dcbHGjvTRMLzRPaE7FVV2bmNs2wpump`
- 23:37Z BD (FINAL_STRETCH, $22,836 mcap, $21,569 5m vol): REJECT, Top 10 hold 25.4% ex-pool (>25%) (V13)  
  CA `HiC6kWaZ19h3YDZcCQT455ECJZ9qpnSfVYRZJ2ktpump`

## What its skips did next (last 48h)
A skip "ran" if the coin reached the first target (1.5x) from the skip price before a 20% drop, "dumped" if the drop came first. Sampled every 10 min, followed 6h.
- top 10 over 25%: blocked 73, ran 12, dumped 56, flat 2, open 3 (saving losses: keep it)
  - ran: NEMO up to 1.6x  
    CA `5ja9qQuE5V9g5TVAFZVdtVQQqoThkAWxEKUaPcC5jN3F`
  - ran: Aren up to 1.75x  
    CA `HkyNkVXpJWg1H7hAWjnSW58J22Cx7gnWwUHhFtf5pump`
  - ran: SUPERBOWL up to 1.61x  
    CA `92j5cWKjdVKDC7skBw1HjvYtrTU8nMM1zKjC4dqmpump`
- too new / sniping: blocked 49, ran 5, dumped 41, flat 3, open 0 (saving losses: keep it)
  - ran: AMD up to 1.61x  
    CA `GCEEdGYx17shhJyudBTAHYAgcTEpKzntyiiqysmUpump`
  - ran: POLY up to 1.65x  
    CA `DMgry6A9C6U6jopS7bAawukAvAcgpUvWfJULcbnfpump`
  - ran: Doge up to 1.72x  
    CA `9CRbVZxQshb9dMkh3yGvyARJRAHMGVuxiQRGhUsppump`
- flow below pace: blocked 44, ran 9, dumped 28, flat 6, open 1 (saving losses: keep it)
  - ran: Link up to 1.57x  
    CA `7kqWni27vRVCKjcuBAmAbs8t7PxXgxdEjUSyRfeFpump`
  - ran: CHICKPOT up to 1.55x  
    CA `8B6ZZAC2FQ7AJrZPz7veXJrod5t2MG1C5MZBLNbUpump`
  - ran: Donkey up to 1.57x  
    CA `G8Lf8uthQp5YHoswQZDRdeRxaWiUqnNFNoZ45y68pump`
- near the high / chasing: blocked 38, ran 5, dumped 30, flat 1, open 2 (saving losses: keep it)
  - ran: PayIF up to 1.56x  
    CA `FfuBMS3rh9M61apXJDs14yAngVnYLWR7xkcX5FxMpump`
  - ran: SAN up to 1.63x  
    CA `8kfp8MzuFuj3vrnmG3KBcYVctYmu2JYerdFhPnX4pump`
  - ran: SOLUNA up to 2.13x  
    CA `3brY153eRNKLxUY3zfBYW9LvarfHUFhgSW66tbQupump`
- RugCheck danger: blocked 28, ran 8, dumped 19, flat 1, open 0 (saving losses: keep it)
  - ran: RAM up to 1.63x  
    CA `72QNkZqiTBsq5dvn4DEwaC5qBPDkc7SZJ38xXy4jpump`
  - ran: $LIBCOIN up to 1.54x  
    CA `2UxjHoidyefQxJrCS8qT23JsbqKFcpPCa8ywBYZupump`
  - ran: ORBIE up to 1.83x  
    CA `HEb2dwDNbBhnrCusoNXXvba9MymYTTmMQcHKaptxmfun`
- other: blocked 19, ran 6, dumped 10, flat 0, open 3 (mixed)
  - ran: DESSA up to 1.54x  
    CA `npz2FhoufQ7pKqhGpaipYWacrAkidyW2yDpVWSvpump`
  - ran: MACHKA up to 1.52x  
    CA `CG1DmSiMXw9WjQXCzP5JDnma5BDY3Cks9bRTdXNLpump`
  - ran: BLOOM up to 1.74x  
    CA `ExdQxJcXzNzhW6CC9phvoEVpKvJQJyg98CE228Uxpump`
- falling knife (code): blocked 18, ran 4, dumped 12, flat 1, open 1 (saving losses: keep it)
  - ran: DESSA up to 1.54x  
    CA `npz2FhoufQ7pKqhGpaipYWacrAkidyW2yDpVWSvpump`
  - ran: ORBIE up to 1.83x  
    CA `HEb2dwDNbBhnrCusoNXXvba9MymYTTmMQcHKaptxmfun`
  - ran: inu up to 1.5x  
    CA `Bid8i1ocWssjRmKh2kcUfHxD1K6Sk7E5pV2PSVdepump`
- thin 5m volume: blocked 18, ran 3, dumped 9, flat 5, open 1 (saving losses: keep it)
  - ran: DESSA up to 1.54x  
    CA `npz2FhoufQ7pKqhGpaipYWacrAkidyW2yDpVWSvpump`
  - ran: MEOWNERO up to 1.76x  
    CA `6gnB2H2hbTVvKUWCzNuqjWY8Rod6EVBmfHi7YxZpTWa7`
  - ran: TTPRO up to 1.71x  
    CA `FrSrp9P3bgiFHwr6h5PQHVh55iC8Dae4eZCKPUo9pump`
- bundles over the line: blocked 17, ran 1, dumped 13, flat 2, open 1 (saving losses: keep it)
  - ran: dump up to 1.72x  
    CA `Bu3h78FY2fsWVZ1MdyQVpFTvv5XsRotWX6VjszQTpump`
- dev share over 1%: blocked 15, ran 1, dumped 10, flat 3, open 1 (saving losses: keep it)
  - ran: Leonida up to 2.03x  
    CA `BWJfBNeXpapG7uoqByp5KSwWgCQba8QcDmA2DQiEpump`

## Daily review (2026-11-05, claude-opus-5-5)
Nothing has a positive edge after costs yet. All 359 settled coins averaged -10.2% net on the simple plan. Before costs that is about +0.4%, so the round-trip cost on a $10 buy (10.6% on average) accounts for the entire loss, the same story as the 22 real trades. FINAL_STRETCH comes closest: about +5.9% before costs, -5.1% after (n=46). At this sample size that is roughly one standard error from zero, from a single day's market, so it is noise until the full week says otherwise. I can't say whether the routine model's would-buys beat its passes, because it made zero would-buys out of 217 decisions. The coins it passed on averaged -11.2% net, the coins that failed the checklist -8.7%, and that gap is also noise.
- finding: Costs decide everything. Average round-trip cost is 10.6% at $10 size. Before costs: all coins +0.4%, MIGRATED about -1.9%, DIP about +5.3%, FINAL_STRETCH about +5.9%. With the 1.5x / -20% plan, ignoring flat outcomes, a coin needs to hit 1.5x first about 44% of the time just to break even after 10.6% cost. No setup gets there (best is 37%).
- finding: FINAL_STRETCH (n=46): 37.0% hit 1.5x first, 63.0% hit the stop, median peak 1.54x, 39.1% touched 2x, net -5.1%. Over half of these coins peaked at 1.54x or more, yet only 37% reached 1.5x before -20%. Most of them shake out hard before moving, which fits the pre-bond dump in V1. Before costs: 0.37×50 − 0.63×20 = +5.9%, which matches the logged net once 11% cost is taken off.
- finding: MIGRATED (n=252, 70% of the sample) is the worst bucket: 20.2% ran, 61.1% dumped, median peak 1.22x, 13.5% touched 2x, net -12.4%. It loses even before costs (about -1.9%), so most of the day's sample is negative-expectancy coins.
- finding: DIP (n=61): 24.6% ran, 50.8% dumped (the lowest dump rate), net -5.2%. Only 4.9% touched 2x. Dips drift and rarely run, so on this data the 'let the runner run' idea has almost no tail to ride here. About +5.3% before costs, with a lot of it from coins that ended flat rather than from 1.5x exits.
- finding: Checklist vs model: coins that failed the checklist (n=142) ran 25.4% and netted -8.7%. Coins the model passed on (n=217) ran 21.7% and netted -11.2%. The soft parts of the filter are not separating winners from losers on this data.
- idea to test: Cost gate: only consider coins whose estimated round-trip cost is at most 5%. First break net% down by cost bucket (<5%, 5-10%, >10%) and by buy size ($10 / $25 / $50). If most of the cost is fixed (priority fee, account rent), size matters more than coin selection. Any bigger size still has to fit the conviction risk budget.
- idea to test: FINAL_STRETCH with a clean checklist (no hard-line or soft fails) and 5m volume ≥ $10k (V1). Report n, share that ran, before-cost and after-cost net. Only adopt it if after-cost net is above zero with n ≥ 150 over the week.
- idea to test: FINAL_STRETCH with mcap ≥ 85% of the bond estimate vs below that. Tests whether the edge is concentrated right at bond. Beware: the runners were picked after the fact.
- idea to test: Exit variant for FINAL_STRETCH only: stop at -30% vs -20%, with the target at 1.5x and also tried at 2x. Check that the gain shows up in both halves of the week (Nov 3-6 vs Nov 7-10) before trusting it. Don't tune on a single day.
- idea to test: MIGRATED limited to the V6 range (mcap $70k-$11M) AND 5m volume ≥ $10k AND buy ratio ≥ 0.55 AND flow ratio (5m vs hourly pace) ≥ 1.0. If no subset beats costs on the week's data, turn MIGRATED off rather than tuning it.

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
Not quiet. Nine of fifteen movers print at least $1.5k of 5-minute volume, and most of it sits in pump.fun launches under about 6 hours old and pumpswap copies. Two themes repeat across several coins: animal mascots (COGE cougar x2, BD Business Dog, Democat, CAT) and joke or reaction names (sssdfg, LIFE, Bubbles, Horny). Rising: BD ($23k cap, $22.8k 5m, 57% buys, on the curve) and MuseX402 ($22k cap, $14.6k 5m, 58% buys). Fading: Democat -98%, CAT -83%, Horny -81%, LIFE -86% in 1h, so copies die fast. Research only, not buys: BD and MuseX402 after +431% and +167% in an hour are chase risks, so I want a clean chart plus holder, dev and bundle checks first; COPE ($396k, $91k 5m, 78% buys, +708% in 1h) is a lottery ticket at best; COGE ($373k, $8.8k 5m) sits just under the $10k bar, so it's a watch. The crawler's NEARFUN and Gavel Drop aren't in the scan, and its CAT row ($18k cap, $13.1k 5m) contradicts the scan row ($2.6k, $0 5m), so I'm using the scan rows and treating the summary's numbers as unverified. The political headlines (Trump, Melania, $LAPTOP) aren't showing up in the trenches right now, so they stay news. Paper only, not financial advice.

## Moving most in its scans, last 30 min (1h volume)
- sssdfg: $1,220,231 1h vol, $185,101 mcap, +420% 1h  
  CA `BQjiYCutv9LVtbgj7pKCN2Ce6k2eUM5RSKs6kDAzpump`
- COPE: $742,548 1h vol, $1,689 mcap, -99% 1h  
  CA `g8FFFJHQnd84dcbHGjvTRMLzRPaE7FVV2bmNs2wpump`
- GATO: $153,311 1h vol, $13,082,918 mcap, +18% 1h  
  CA `HsprHxBRgiVaQdRf3TnKNuZZtaX9JUSPgMFdAkk6pump`
- TOYS4KIDS: $93,318 1h vol, $21,154 mcap, -68% 1h  
  CA `FqJu1nmcNP8fCJfAW7Y4dGmp6fF9iF2RxrqMSFAcpump`
- BongoCat: $73,565 1h vol, $22,929 mcap, -38% 1h  
  CA `GyPoNrioGXzY6d7uNHnFnW614Cw3XC1KQv9MVNS5pump`
