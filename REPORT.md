# Trencher live report

Updated 2026-11-03T18:43:58Z (paper trading, never real money)

- Equity: $74.23 (-25.8% vs $100 start)
- Closed trades: 22, 3 wins
- Fees paid: $14.78 (axiom $2.81, network $9.18, pool $2.66), plus $4.15 lost to slippage
- New trades: WATCH-ONLY (scans and decides, buys nothing)
- Brain: subscription, claude-haiku-5-5 for routine calls, claude-opus-5-5 for the daily review; 458 routine calls and 1 plan-limit hits in 48h
- Watch log: 124 coins being followed, 100 filed, 0 would-buys (6h follow, sampled every 2 min)

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
- 18:43Z: 9 coins, 7 with pairs, 0 passed the market filters, 0 researched

## Coins it looked at, and why it passed
- 18:42Z ANONVOYAGE (MIGRATED, $1,664,336 mcap, $8,055 5m vol): REJECT, Bundles: 10 linked wallet cluster(s) hold 50.3% of supply (>20%) (V17)  
  CA `8muc9DdhqWfAPcvmEebNQCG89bLiwi12T2KtBtzVpump`
- 18:40Z MEOWNERO (MIGRATED, $188,288 mcap, $2,190 5m vol): REJECT, Top 10 hold 25.2% ex-pool (>25%) (V13)  
  CA `6gnB2H2hbTVvKUWCzNuqjWY8Rod6EVBmfHi7YxZpTWa7`
- 18:40Z CBUCKS (MIGRATED, $1,623,026 mcap, $2,329 5m vol): REJECT, Top 10 hold 26.1% ex-pool (>25%) (V13)  
  CA `DtcicPCKTKeAh7TDEzTym3hXeoHAoMiBdYJhMYxZpump`
- 18:39Z SPHERE (MIGRATED, $155,311 mcap, $2,518 5m vol): PASS at conviction 2, PASS: 90.6% off a $1.65M high is a corpse, not a dip, and the only story is 19 copies of "project sphere" with a day-old website. Blocker "dead story" (V1, V3, V6).  
  CA `31SYoqWFhx3i9UsfnoXTjFp4ZwJA8F8UPrMxymfDpump`
- 18:34Z WASTED (DIP, $897,047 mcap, $4,383 5m vol): REJECT, Dev holds 3.5% (>1%) (V13, V17)  
  CA `GexThZHgaswpAQ7Fi8QrHFubjPimUNSYhJiAA7XZpump`
- 18:29Z WOOP (DIP, $159,321 mcap, $4,784 5m vol): REJECT, Top 10 hold 27.6% ex-pool (>25%) (V13)  
  CA `2724239D1JhWQGV5WZ7tdBTN5Jz4FZ3pdmvj3iD4LsVE`
- 18:27Z DESSA (MIGRATED, $8,765,383 mcap, $2,757 5m vol): PASS at conviction 3, PASS: DESSA, $8.8M mcap, 5m flow is 5 buys vs 10 sells and no catalyst on the radar. A bottom buy with no story and no higher low is a farm to me. (V1, V6, V13)  
  CA `npz2FhoufQ7pKqhGpaipYWacrAkidyW2yDpVWSvpump`
- 18:20Z HIGH (DIP, $112,642 mcap, $3,295 5m vol): REJECT, Dip with fading attention is a falling knife, not a dip (5m at 0.15x the hour's pace, under 0.6x)  
  CA `7ymF66Z6VhgNiwadtVhjTtT6U7iQRpSxeiRrhfufhigh`
- 18:19Z Ahsoka (DIP, $761,600 mcap, $7,126 5m vol): PASS at conviction 3, PASS — DIP with no story behind it: no radar mention, no catalyst, and the project's own site doesn't show this CA. Blocker: no catalyst / narrative not rising (V1, V13).  
  CA `4nuj5NLHMtQSezfmz6CwBpCRJisFie6F6MxNNz1dpump`
- 18:18Z Dacity (MIGRATED, $6,848,868 mcap, $5,376 5m vol): REJECT, Bundles: 10 linked wallet cluster(s) hold 24.0% of supply (>20%) (V17)  
  CA `nxPqZ4F7ux8Vph5NFu25rEP6Kx9Gr1U6Fmj36Rjpump`

## What its skips did next (last 48h)
A skip "ran" if the coin reached the first target (1.5x) from the skip price before a 20% drop, "dumped" if the drop came first. Sampled every 10 min, followed 6h.
- too new / sniping: blocked 59, ran 11, dumped 46, flat 0, open 2 (saving losses: keep it)
  - ran: VETOTRUMP up to 1.66x  
    CA `6g16UK4wHoFhC7PCmw8LYYCdt9q8m99fyoAwxeCrpump`
  - ran: Anakinius up to 1.93x  
    CA `2pKpMwUQXNZeAf93LoomnZSworH3ezFzweCiuvrppump`
  - ran: CLIPPED up to 1.65x  
    CA `Bxyp4L6EbDys4fo51qxMEQTx41sj6McnsbPZTdvipump`
- top 10 over 25%: blocked 54, ran 8, dumped 41, flat 1, open 4 (saving losses: keep it)
  - ran: GODHOUSE up to 3.19x  
    CA `CSGTuLtWhCfGZ5S5TvASQ6a5su91NCfRpNqfPczfpump`
  - ran: KYBER up to 1.83x  
    CA `BasL6j1MNkjFyuvRRFsmbm3bKqFPr6Yg3UhShii6pump`
  - ran: WIF up to 1.67x  
    CA `E7ayy5Se6gjwCNtw9NP629AucnTgqab4SSmSxDpUpump`
- flow below pace: blocked 40, ran 7, dumped 28, flat 2, open 3 (saving losses: keep it)
  - ran: KOROSUKE up to 1.54x  
    CA `7ha4HFgdvkXaDcR2biCsuBpoCZzoLSRjb5we34Gbpump`
  - ran: CAPY up to 1.51x  
    CA `DBPTU2oKLDHXQjAEJ3rZi8bUGmt2uxUbipgg6xmXoMqr`
  - ran: ZERO up to 1.61x  
    CA `Aes6XNH9BboLZuchD5PnDwaX6Zj1nU79TU3gNtPEpump`
- near the high / chasing: blocked 33, ran 2, dumped 25, flat 4, open 2 (saving losses: keep it)
  - ran: underdog up to 1.64x  
    CA `BZXh2LcnNNyypxsdfVeFzXawqmoGoSShC5i4NEQQpump`
  - ran: LUCIA up to 1.83x  
    CA `Cbtnpg6SL9jvZxtZTYYFPtVQXkuuqSUxCU5aXeTkpump`
- falling knife (code): blocked 30, ran 5, dumped 23, flat 1, open 1 (saving losses: keep it)
  - ran: VETOTRUMP up to 1.66x  
    CA `6g16UK4wHoFhC7PCmw8LYYCdt9q8m99fyoAwxeCrpump`
  - ran: STEALTH up to 1.77x  
    CA `GoDSW31bTxfkoup9yA1qcGGx9RMXdTEWgApv3xzBmoA`
  - ran: PEACE up to 1.75x  
    CA `BngAfLZxaWN2QvpFhRbUHydYGr8zA7YTSA178G8Epump`
- RugCheck danger: blocked 26, ran 3, dumped 20, flat 1, open 2 (saving losses: keep it)
  - ran: COLLECTOR up to 1.62x  
    CA `6kKETm8xPeZ2z1DBYjXmxMTFAJudvGHJvRHu5Wt8uGtf`
  - ran: GTA up to 1.74x  
    CA `G6F6SYSUAUxsnKLyeRW29hE5A4BGCbw91x7HMPySpump`
  - ran: Wanted up to 1.53x  
    CA `8oUGdPdyxVaCSJSZpcVZuxqoyiZAmc2Z22FsDRZ3pump`
- bundles over the line: blocked 21, ran 3, dumped 15, flat 0, open 3 (saving losses: keep it)
  - ran: Nuts up to 1.53x  
    CA `APH9FRoKst66E4a7uZXcEfE8NjtwybUC8Jq7ue8upump`
  - ran: NA up to 1.97x  
    CA `9ZmdP8q22ebRhEkcwd5EDkitu7ypeDFXTQXpv2kUpump`
  - ran: MAMESUKE up to 1.95x  
    CA `SCGBBnSwnekytGFHgyeHHxPMiN7xDxsWFGg9JgFSTNK`
- thin 5m volume: blocked 14, ran 3, dumped 6, flat 3, open 2 (saving losses: keep it)
  - ran: CUMFACE up to 1.55x  
    CA `J1D3X8znX4AzUPMHVWyBLNHqBBqWDPNSjX4KwK3Qpump`
  - ran: KIDS up to 1.73x  
    CA `7uwr9Zoz8WW9UyRVC22nmmAXRbPoFTUpVjsN8q7kids`
  - ran: 404 up to 1.89x  
    CA `9gKArqT6qp3goHfuwAnfG7LioqwUtJ8TFu7P1Bhbpump`
- falling knife / no higher low: blocked 14, ran 1, dumped 10, flat 2, open 1 (saving losses: keep it)
  - ran: HEDGE up to 1.77x  
    CA `wDSAqt4tEZpDAwB9XY6ejkZvMFuT1zUMjUh67txeYhf`
- dev share over 1%: blocked 11, ran 2, dumped 4, flat 2, open 3 (saving losses: keep it)
  - ran: Firecube up to 1.88x  
    CA `Ebih1KdijjpQBaM83gUfGhRtTCpHzDkBZhCZedZwpump`
  - ran: HUND  up to 1.63x  
    CA `HAjc6B1MfdjnYPiB2xcETPb25kb85Pxg9nq9i4D5pump`

## Daily review (2026-11-03, claude-opus-5-5)
There's no positive after-cost edge yet. The 13 settled coins averaged -6.7% net under the simple plan, which is about +3.6% gross minus a 10.3% round-trip cost. The best bucket, MIGRATED, is break-even at -0.4% (n=8). With a 1.5x target, a -20% stop and about 10% cost, a winner nets about +40% and a loser about -30%, so a coin has to hit the target first about 43% of the time just to break even. Nothing big enough to trust gets there: the whole set is at 31% and MIGRATED at 37.5%. With n=13 the confidence intervals run roughly ±25 points, and the simulator flatters losses (see data issues), so the real numbers are probably worse. The routine model logged zero would-buys, so there's nothing to compare against the coins it passed on. Its PASSes did worse (-20.5% net, n=7) than the coins the checklist rejected (+9.4%, n=6). So passing was mostly right, but that gap rests on 2–3 coins (3/6 vs 1/7 ran, Fisher p≈0.3). It also passed on the day's two best runners, LIFEVAL at 4.2x and XDG at 2.7x.
- finding: Costs are the whole story. Overall: n=13, ran 30.8%, dumped 61.5%, average net -6.7% against 10.3% cost, so gross price action was slightly positive (+3.6%). The one real trade in the window (Slingoor) cost $1.00 on $10, the same 10%. That matches the pre-pause record, where fees and slippage were $18.83 of the $25.79 lost.
- finding: Break-even maths: at a 1.5x target, -20% stop and 10% cost, a strategy needs about 43% of trades to hit the target first. No sample of 6 or more reaches that. By setup: MIGRATED 37.5%, FINAL_STRETCH 33.3%, DIP 0%.
- finding: MIGRATED, n=8: ran 37.5%, dumped 50%, median peak 1.6x, hit 2x 25%, net -0.4%. It's the only setup near zero, and it's still not positive.
- finding: DIP, n=2: both dumped, net -30.7% each. That is exactly -20% plus 10.7% cost, which shows the simulator fills every stop at exactly -20%. Two coins is not evidence about the setup.
- finding: FINAL_STRETCH, n=3: one ran (Firecube, 2.09x high 13.6 min after logging, rejected by the checklist for dev share over 1%), net -7.5%.
- idea to test: Cost gate. Hypothesis: low-cost pools are the only place an edge can survive. Test: on all logged coins, bucket by estimated round-trip cost (<5%, 5–8%, >8%) and compare simple-plan net. Also re-price at $25 and $50 notional if the cost model splits fixed fees from slippage, to see where fixed fees stop dominating.
- idea to test: Older, larger migrated coins. Hypothesis: the RICO/MAMESUKE pattern. Test setup=MIGRATED AND age_hours 6–48 AND mcap $300k–$3M AND 5m volume ≥ $10k AND flow ratio ≥ 0.8 AND drawdown from high 20–50%, with no time stop or a 6h one. Compare its hit rate with the 43% break-even.
- idea to test: Very young migrated coins. Hypothesis: the LIFEVAL/XDG pattern. Test setup=MIGRATED AND age_hours < 0.5 AND mcap $100k–$250k AND 5m volume ≥ $15k AND buy ratio ≥ 0.6 AND checklist pass, against the same age band that 'too new' blocks (15% ran). Keep it only if an mcap or volume floor clearly separates the runners.
- idea to test: Time-stop comparison. On every settled coin, run the simple plan three ways: no time stop, a 45-minute time stop (current live plans), and a 6h time stop. Several runners peaked after 150–360 minutes, so the 45-minute stop may be cutting the only gains there are.
- idea to test: Stop/target geometry. Compare -20%/1.5x, -30%/2x and -25%/1.5x with the 2x initials from the soul file. At least one 2x coin dropped through -20% before it ran. Stops must fill at the first sample at or below the level, not at the level itself.

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
The movers say the trenches are running launch bursts: fresh coins, under about 1h old, with 1h volume several times market cap (Kotanosuke, ElunMesk, STONKS, and Dacity 9iFR at $252k cap with $285k 1h volume). Two other themes show up across several coins: name fights (two Dacity tokens, one +316% and one -34%, plus the Elon-style ElunMesk at a 95% buy ratio) and the GTA theme, which is dying in the scan. GTAVI ARC is down -98.8% to a $2.2k cap with zero 5m volume, and QUESTLY is down -95%; the crawler's $104k GTAVI figure is stale, so I'm using the scan. Setups to research, not buys: 9iFR "$DCYC" first (48k 5m, 76% buys, the strongest organic-looking volume), then whichever Dacity is the original versus the vamp, and STONKS only if its 5m volume holds with a clean holder check. ElunMesk is an impersonation risk, so it needs a similar-token and holder check before anything else. Fading: GATO (34% buys, flat, 12M), HIGH, and the GTA names. Not quiet; the movers are loud, and the burst is the story until the holder and bundle checks say otherwise.

## Moving most in its scans, last 30 min (1h volume)
- GTAVI: $418,895 1h vol, $2,200 mcap, -99% 1h  
  CA `HekahVohmeokPUhscg5taNme3Qs2fcSQoNgEeUPMpump`
- DCYC: $310,006 1h vol, $29,618 mcap, -34% 1h  
  CA `EJPWoVgMrkZrqZAtRkGvA4jppbo15rMF2hhe1EPzpump`
- $DCYC : $285,495 1h vol, $251,892 mcap, +316% 1h  
  CA `9iFR4DuinJ96rUHdf7uRutJYbdAPZKrFbkRzVzSepump`
- HIGH: $272,365 1h vol, $111,695 mcap, -33% 1h  
  CA `7ymF66Z6VhgNiwadtVhjTtT6U7iQRpSxeiRrhfufhigh`
- 1WIN: $194,260 1h vol, $15,712,763 mcap, -1% 1h  
  CA `FjPKUGnF5zBpdEv18gT8FJCtxh3MKrFkoeYekgYr1win`
