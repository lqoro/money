# Trencher live report

Updated 2026-11-03T10:25:14Z (paper trading, never real money)

- Equity: $74.23 (-25.8% vs $100 start)
- Closed trades: 22, 3 wins
- Fees paid: $14.78 (axiom $2.81, network $9.18, pool $2.66), plus $4.15 lost to slippage
- New trades: WATCH-ONLY (scans and decides, buys nothing)
- Brain: subscription, claude-haiku-5-5 for routine calls, claude-opus-5-5 for the daily review; 444 routine calls and 1 plan-limit hits in 48h
- Watch log: 68 coins being followed, 0 filed, 0 would-buys (6h follow, sampled every 2 min)

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
- 10:24Z: 5 coins, 5 with pairs, 0 passed the market filters, 0 researched

## Coins it looked at, and why it passed
- 10:18Z Slingoor (MIGRATED, $118,265 mcap, $6,321 5m vol): REJECT, Top 10 hold 26.4% ex-pool (>25%) (V13)  
  CA `9rZR9nCQbaiBvotWVpifN8z1vckVFshnsATuAJrXpump`
- 10:13Z UNPOOLED (MIGRATED, $70,385 mcap, $5,132 5m vol): PASS at conviction 3, PASS: no printed higher low, 47% buy share, and a theme that's dumping with no catalyst. The site is 7 hours old and doesn't show this CA. (V1, V6, V13)  
  CA `FxQ5GbqCBxNHDpFTpiL9RDVHiP58ar5nMkR3eMwepump`
- 10:09Z SPHERE (DIP, $711,116 mcap, $3,825 5m vol): PASS at conviction 3, PASS: SPHERE is a 17-copy "Project Sphere" field with 5m flow at 0.62x pace, no catalyst and a 0.5-day-old site that doesn't show this CA. Blocker: flow below pace (V1, V6, V13).  
  CA `31SYoqWFhx3i9UsfnoXTjFp4ZwJA8F8UPrMxymfDpump`
- 10:08Z 김여정 (MIGRATED, $75,574 mcap, $60,164 5m vol): PASS at conviction 2, PASS: chasing spike. 5m volume is 7.2x the hourly pace, the coin is 10 minutes old, and no higher low has printed. It's also one of 9 same-ticker copies with no catalyst. Wait (V1, V6).  
  CA `3imKAhTuUakBCGK1aXxihc13Qe5prGzQb7eWMn1gpump`
- 10:03Z MAMESUKE (DIP, $1,124,930 mcap, $3,394 5m vol): REJECT, Bundles: 5 linked wallet cluster(s) hold 66.3% of supply (>20%) (V17)  
  CA `SCGBBnSwnekytGFHgyeHHxPMiN7xDxsWFGg9JgFSTNK`
- 09:48Z GENESIS (MIGRATED, $56,222 mcap, $21,982 5m vol): PASS at conviction 3, PASS: chasing spike, too new, target too close. GENESIS is one of 12 copies of a generic word with no radar mention, and its first resistance is only 1.14x away. (V1, V6, V13)  
  CA `9W7Dyv9CV9UhwKfW9gCuYoPncAY8M3EScLiD8ZHemDAr`
- 09:47Z OMBRO (MIGRATED, $224,629 mcap, $25,233 5m vol): PASS at conviction 3, PASS: OMBRO is the cleanest holder table I've seen this hour, but its 5m flow is 0.67x pace and nothing is bottoming. Blocker: "flow below pace," plus "bottom buy, no catalyst." (V1, V6)  
  CA `8DB8Fw5UiC1AzugQAfRyw3qL8omw772LJbdehNWhpump`
- 09:42Z LIFEVAL (MIGRATED, $95,522 mcap, $18,627 5m vol): REJECT, Bundles: 10 linked wallet cluster(s) hold 100.0% of supply (>20%) (V17)  
  CA `Bmn5qFwQHxteaoM1et9FLdHsi52DmuXZyzWinih8pump`
- 09:42Z ABDUL (MIGRATED, $141,894 mcap, $22,735 5m vol): PASS at conviction 3, PASS: chasing spike. ABDUL is up 37% on its last 5m candle, 10.8% off a peak printed 12 minutes ago, with no higher low yet. Wait for the retrace (V1, V6).  
  CA `94exwLui2KfAzYnbATkX8iKh4tcjMDW6YwckkSJVpump`
- 09:34Z DESSA (DIP, $14,049,001 mcap, $2,682 5m vol): REJECT, Dip with fading attention is a falling knife, not a dip (5m at 0.46x the hour's pace, under 0.6x)  
  CA `npz2FhoufQ7pKqhGpaipYWacrAkidyW2yDpVWSvpump`

## What its skips did next (last 48h)
A skip "ran" if the coin reached the first target (1.5x) from the skip price before a 20% drop, "dumped" if the drop came first. Sampled every 10 min, followed 6h.
- top 10 over 25%: blocked 55, ran 10, dumped 40, flat 3, open 2 (saving losses: keep it)
  - ran: TIPPER up to 1.55x  
    CA `3DEcz7AnmJiGSnDHYvUeX5uPMMHVcDwqrWRSGdHEpump`
  - ran: Capri up to 1.84x  
    CA `6qhnbvdJuWVUQ7EQpgz5GNraV7pty7cqc8MmfQTEpump`
  - ran: PEAKY up to 1.53x  
    CA `2EQxezWgXPRU6V3UD7DKr5m12mxqeFGPWNRx9wbqy9fC`
- too new / sniping: blocked 51, ran 8, dumped 42, flat 0, open 1 (saving losses: keep it)
  - ran: VETOTRUMP up to 1.66x  
    CA `6g16UK4wHoFhC7PCmw8LYYCdt9q8m99fyoAwxeCrpump`
  - ran: Anakinius up to 1.93x  
    CA `2pKpMwUQXNZeAf93LoomnZSworH3ezFzweCiuvrppump`
  - ran: CLIPPED up to 1.65x  
    CA `Bxyp4L6EbDys4fo51qxMEQTx41sj6McnsbPZTdvipump`
- near the high / chasing: blocked 38, ran 2, dumped 32, flat 3, open 1 (saving losses: keep it)
  - ran: BLUE up to 1.53x  
    CA `CPoGSmcjprCvzA2MFYLJMpQkGjmgVzKg4RVwMdrzpump`
  - ran: PIRATE up to 2.27x  
    CA `gzQXRwGRzfKLHfaV1f84QT7e5mt4vevu7MgacEfpump`
- flow below pace: blocked 31, ran 7, dumped 19, flat 1, open 4 (saving losses: keep it)
  - ran: Ahsoka up to 1.54x  
    CA `4nuj5NLHMtQSezfmz6CwBpCRJisFie6F6MxNNz1dpump`
  - ran: KOROSUKE up to 1.54x  
    CA `7ha4HFgdvkXaDcR2biCsuBpoCZzoLSRjb5we34Gbpump`
  - ran: RICO up to 1.78x  
    CA `8kuQg3WivDtL85VEdw2jEmSXjYt6EEeYBATJ4DtQpump`
- RugCheck danger: blocked 30, ran 6, dumped 23, flat 0, open 1 (saving losses: keep it)
  - ran: AIC up to 1.6x  
    CA `2T9WZjVC6L3BvusUtjKDT6HcZeEYgU9T5xhfJQxFpump`
  - ran: ZECRET up to 1.62x  
    CA `ChCi2x2bpevrNyeRoPHLXHzmaCdGQPuU15CNqxY1pump`
  - ran: Bitboy up to 1.6x  
    CA `GvXhSHnWrkAasjAUZeRzRfUBV2BJiiduaHarCWAEpump`
- falling knife (code): blocked 28, ran 7, dumped 19, flat 1, open 1 (saving losses: keep it)
  - ran: BLUE up to 1.53x  
    CA `CPoGSmcjprCvzA2MFYLJMpQkGjmgVzKg4RVwMdrzpump`
  - ran: VETOTRUMP up to 1.66x  
    CA `6g16UK4wHoFhC7PCmw8LYYCdt9q8m99fyoAwxeCrpump`
  - ran: STEALTH up to 1.77x  
    CA `GoDSW31bTxfkoup9yA1qcGGx9RMXdTEWgApv3xzBmoA`
- bundles over the line: blocked 19, ran 2, dumped 14, flat 2, open 1 (saving losses: keep it)
  - ran: Nuts up to 1.53x  
    CA `APH9FRoKst66E4a7uZXcEfE8NjtwybUC8Jq7ue8upump`
  - ran: NA up to 1.97x  
    CA `9ZmdP8q22ebRhEkcwd5EDkitu7ypeDFXTQXpv2kUpump`
- falling knife / no higher low: blocked 15, ran 1, dumped 10, flat 2, open 2 (saving losses: keep it)
  - ran: HEDGE up to 1.77x  
    CA `wDSAqt4tEZpDAwB9XY6ejkZvMFuT1zUMjUh67txeYhf`
- thin 5m volume: blocked 14, ran 3, dumped 5, flat 5, open 1 (mixed)
  - ran: CUMFACE up to 1.55x  
    CA `J1D3X8znX4AzUPMHVWyBLNHqBBqWDPNSjX4KwK3Qpump`
  - ran: RICO up to 1.78x  
    CA `8kuQg3WivDtL85VEdw2jEmSXjYt6EEeYBATJ4DtQpump`
  - ran: KIDS up to 1.73x  
    CA `7uwr9Zoz8WW9UyRVC22nmmAXRbPoFTUpVjsN8q7kids`
- dev share over 1%: blocked 12, ran 3, dumped 5, flat 3, open 1 (mixed)
  - ran: MINTED up to 1.61x  
    CA `9yEKBwczdqoox7Red6GGPTrJ2dUbMvFUagdjxFqHpump`
  - ran: DOJAK up to 2.62x  
    CA `E5aeDjgq6ZSzAmihKoh9JPEhwK2bMCbZLJf6LYT9pump`
  - ran: Firecube up to 1.88x  
    CA `Ebih1KdijjpQBaM83gUfGhRtTCpHzDkBZhCZedZwpump`

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
Meta: the volume is in pump.fun launches under an hour old with joke and meta-commentary names (MENTIONS +379% at $17.8k cap, Stonkero.fun, Terminal of Truths, Nori, Cooked), but most sit under the $10k 5m bar, so they're New Pairs and out of scope for me. The second theme is fresh coins already past migration with real flow: 김여정 "Crypto Final Boss" ($75.6k cap, $60k 5m, 0.67 buy ratio, +97% 1h, pumpswap, 0.2h old). Fading: old names on thin 5m volume (GATO/GTA6CAT at 1,678h, WASTED, MAMESUKE, DESSA). Politics dominates the headlines (LAPTOP crash, Trump, Hunter Biden), but none of it is in the movers, so I treat it as background, not a setup. Only setup to research: Crypto Final Boss under MIGRATED rules (V1, V6). Its name is a real politician's name (Kim Yo-jong), so check for political pushing before anything else, and don't chase the +97% spike; wait for a pullback that holds buy ratio above 0.5, check similar tokens for an original, and check holders and bundles. Conviction is 4 for now, so this is a research-only pass, not a buy. Not in this scan, so ignored: OMBRO, PUPER, peach, PRESSURE, and Donkey. Also, the crawler's UNPOOLED -55% doesn't match the scan (+13% 1h), so I'm not using it.

## Moving most in its scans, last 30 min (1h volume)
- 1WIN: $112,499 1h vol, $16,487,635 mcap, +0% 1h  
  CA `FjPKUGnF5zBpdEv18gT8FJCtxh3MKrFkoeYekgYr1win`
- 김여정: $100,772 1h vol, $75,574 mcap, +97% 1h  
  CA `3imKAhTuUakBCGK1aXxihc13Qe5prGzQb7eWMn1gpump`
- SPHERE: $73,680 1h vol, $721,236 mcap, +0% 1h  
  CA `31SYoqWFhx3i9UsfnoXTjFp4ZwJA8F8UPrMxymfDpump`
- Slingoor: $72,886 1h vol, $116,584 mcap, +2% 1h  
  CA `9rZR9nCQbaiBvotWVpifN8z1vckVFshnsATuAJrXpump`
- GATO: $68,636 1h vol, $13,299,523 mcap, +3% 1h  
  CA `HsprHxBRgiVaQdRf3TnKNuZZtaX9JUSPgMFdAkk6pump`
