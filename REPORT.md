# Trencher live report

Updated 2026-11-22T20:20:50Z (paper trading, never real money)

- Equity: $74.23 (-25.8% vs $100 start)
- Closed trades: 22, 3 wins
- Fees paid: $14.78 (axiom $2.81, network $9.18, pool $2.66), plus $4.15 lost to slippage
- New trades: WATCH-ONLY (scans and decides, buys nothing)
- Brain: subscription, claude-haiku-5-5 for routine calls, claude-opus-5-5 for the daily review; 252 routine calls and 0 plan-limit hits in 48h
- Watch log: 51 coins being followed, 2690 filed, 0 would-buys (6h follow, sampled every 2 min)

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
- 19:25Z: 43 coins, 43 with pairs, 5 passed the market filters, 5 researched

## Coins it looked at, and why it passed
- 20:19Z DIGS (DIP, $254,414 mcap, $2,980 5m vol): PASS, PASS — brain unavailable, not trading blind.  
  CA `9QT8K685Hrae4k11dhGXirdtpfAaimExtyfwt8cPpump`
- 20:08Z IF (DIP, $36,979 mcap, $2,628 5m vol): REJECT, Top 10 hold 25.8% ex-pool (>25%) (V13)  
  CA `3hi7qBus11Xg9Pmj7xuuK9pjmKF7UUhT5uh7SXQbhsQt`
- 20:04Z earball (MIGRATED, $73,532 mcap, $2,209 5m vol): PASS, PASS — brain unavailable, not trading blind.  
  CA `FryQiSLqU7NfPvpQJRiYrVuvRRW66uB4FLorrKmjpump`
- 19:54Z OpenIndex (MIGRATED, $359,076 mcap, $24,790 5m vol): PASS, PASS — brain unavailable, not trading blind.  
  CA `FuKY3dk7QmpbDdQRjzbjB3G6PiCuqKNvN4dAWDpwpump`
- 19:42Z SINGULARTY (DIP, $67,475 mcap, $53,845 5m vol): PASS, PASS — brain unavailable, not trading blind.  
  CA `DJcHva2UJnRUPxzVfczcYyqxRtpwDTPcok6irtNmpump`
- 19:02Z PushCoin (MIGRATED, $1,587,415 mcap, $2,968 5m vol): PASS, PASS — brain unavailable, not trading blind.  
  CA `3N6Mp8YQuVDfEtyuyJS72s4MRrgQuKY34gvYZD5Kpump`
- 18:48Z DELULU (FINAL_STRETCH, $15,745 mcap, $3,200 5m vol): PASS, PASS — brain unavailable, not trading blind.  
  CA `A37ozuu1D1pP1cM27y1HYkSArVQbgsZNN7Va74yNpump`
- 18:37Z MCAT (MIGRATED, $187,650 mcap, $15,385 5m vol): PASS, PASS — brain unavailable, not trading blind.  
  CA `v4GK8f24ZJJa5qLoTJ4mJ5d6jsNUXHScwGaRHdfpump`
- 18:14Z DIGS (DIP, $278,669 mcap, $3,001 5m vol): REJECT, Bundles: 10 linked wallet cluster(s) hold 100.0% of supply (>20%) (V17)  
  CA `9QT8K685Hrae4k11dhGXirdtpfAaimExtyfwt8cPpump`
- 18:11Z FOAM (MIGRATED, $104,513 mcap, $14,073 5m vol): PASS, PASS — brain unavailable, not trading blind.  
  CA `2MdCPWNFufmJSZhajSvi1yqBFTB24GQ4ipjNcB8Vpump`

## What its skips did next (last 48h)
A skip "ran" if the coin reached the first target (1.5x) from the skip price before a 20% drop, "dumped" if the drop came first. Sampled every 10 min, followed 6h.
- flow below pace: blocked 26, ran 4, dumped 19, flat 0, open 3 (saving losses: keep it)
  - ran: Trader up to 2.04x  
    CA `BYKQkHKMWHidNBLQXgt7NX4PLUtJZRYGLWQYkJzPGenX`
  - ran: Bust up to 1.55x  
    CA `EoV9JQYi57tqjyQbWLdXVarYpEu82FsP8SDnkbFmpump`
  - ran: Mandy up to 1.53x  
    CA `HmJRWZ8tFfuCY9A4MrSftnrvEFCApw1hyqHtb9Rzpump`
- near the high / chasing: blocked 18, ran 3, dumped 14, flat 0, open 1 (saving losses: keep it)
  - ran: Trader up to 2.04x  
    CA `BYKQkHKMWHidNBLQXgt7NX4PLUtJZRYGLWQYkJzPGenX`
  - ran: CUNTS up to 1.61x  
    CA `7CvW68FD9KjNYGByfykhaNps7VNPLN8dFwMRfmgQpump`
  - ran: SANTA up to 1.85x  
    CA `tZsjFu2CH1R23wEpbfXAYGc2KUaVrUbwofCNNNqpump`
- too new / sniping: blocked 18, ran 3, dumped 14, flat 1, open 0 (saving losses: keep it)
  - ran: TA up to 1.77x  
    CA `DKUM8qywmi8X9RYK2wUgnTw8QKjh1nYDThZR1GXPpump`
  - ran: SANTAHAT up to 3x  
    CA `5fWLSMA5HoK9W4VoTMi4c3qjyu3N2LsKRSM8Ffpgpump`
  - ran: KYC up to 2.37x  
    CA `47YCrfUmSQUF9vnPsPGSzrmTcxttdRAWejCMkhrrpump`
- brain paced: blocked 17, ran 2, dumped 6, flat 1, open 8 (saving losses: keep it)
  - ran: STREETS up to 1.73x  
    CA `82mseLFauphc2yutbaDGgViahquJ1jGVLpyof99xpump`
  - ran: FOAM up to 1.98x  
    CA `2MdCPWNFufmJSZhajSvi1yqBFTB24GQ4ipjNcB8Vpump`
- top 10 over 25%: blocked 17, ran 2, dumped 14, flat 0, open 1 (saving losses: keep it)
  - ran: :) up to 1.65x  
    CA `Dtx414D8jurspmB1jqJWsYU66pemoXRjQeXx7TC1pump`
  - ran: GIF up to 2.16x  
    CA `B6wM98qkQKP71mhPA48S7No6TxM4KaXdFojDTZeUpump`
- RugCheck danger: blocked 12, ran 2, dumped 10, flat 0, open 0 (saving losses: keep it)
  - ran: CAP up to 2.6x  
    CA `CxGYpWoTun4J3xD4cNwXFRn2W3RzJozTxyU9nbJ4pump`
  - ran: MIHAOMAS up to 1.62x  
    CA `3XsFunPdji9U1EgJXokZysw8SB3t74un89b6KLEVpump`
- falling knife / no higher low: blocked 8, ran 2, dumped 2, flat 4, open 0 (mixed)
  - ran: UrAnus up to 2.97x  
    CA `27u3diWofnXGUkddjLGhcy1nRssFKHW3RtNbpWzUpump`
  - ran: STREETS up to 1.73x  
    CA `82mseLFauphc2yutbaDGgViahquJ1jGVLpyof99xpump`
- falling knife (code): blocked 8, ran 2, dumped 5, flat 1, open 0 (saving losses: keep it)
  - ran: RIZZMAS3 up to 1.84x  
    CA `BQcV4Ryfu9bZK8egAF89AhkojdJqAaDt4xTFwUQ2pump`
  - ran: STREETS up to 1.73x  
    CA `82mseLFauphc2yutbaDGgViahquJ1jGVLpyof99xpump`
- dev share over 1%: blocked 5, ran 2, dumped 2, flat 1, open 0 (mixed)
  - ran: SANTINU up to 1.56x  
    CA `BCTwG3LDhNcthcK374aWQfAzLYGRXDu1apmrqw3Tpump`
  - ran: Mfer up to 1.55x  
    CA `9tX1UpBGeNqMb1VqqzVumwzW71ybsNZFyWKYiL8Ppump`
- bundles over the line: blocked 5, ran 0, dumped 2, flat 2, open 1 (too few played out to judge)

## Daily review (2026-11-22, claude-opus-5-5)
Nothing has a positive edge after costs. All 166 settled coins averaged -11.3% net under the simple plan, and no setup or stage was positive. The closest were FINAL_STRETCH at -3.3% (n=21) and DIP at -5.9% (n=20). Both look slightly positive before costs (about +6.7% and +3.6%), but with ~20 samples the error bar is roughly ±13 points, and some coins are logged more than once, so both are noise for now. The biggest loss is the 9.8% average round-trip cost on a $10 buy: at that cost, the simple plan only breaks even if about 43% of coins hit 1.5x before -20%. Overall only 23.5% did, and the best setup (FINAL_STRETCH) managed 38.1%. I can't answer whether the routine model's would-buys beat its passes, because it logged zero would-buys in 24h out of 99 coins it reviewed. The coins it passed on did lose more than the coins the checklist rejected (-15.2% vs -5.7%). That suggests passing them was correct, but also that clearing the checklist didn't pick better coins this day.
- finding: Costs decide everything. The 'ran' and 'dumped' shares reproduce avg_net almost exactly: 0.235×50 − 0.669×20 − 9.8 ≈ -11.3. So the plan is effectively a race between +50% and -20%. Breakeven needs ~42.6% ran at 9.8% cost, but only ~35.7% at 5% cost and ~31% at 3%.
- finding: MIGRATED is the bulk and the worst: n=125, 20.8% ran, 71.2% dumped, net -13.5%. Before costs it is still about -3.7%, so this setup has no raw edge as currently filtered.
- finding: FINAL_STRETCH has the highest hit rate: n=21, 38.1% ran, net -3.3%. But only 14.3% reached 2x, so most of its runners stalled between 1.5x and 2x. That fits the guide's pre-bond dump and stall pattern (V1) and supports taking profit early on this setup. At a ~5% cost it would be about +1.4%, which still isn't significant at n=21.
- finding: DIP: n=20, 25% ran, but only 45% dumped (lowest of any setup). Net -5.9%, about +3.6% before costs. Losses were less frequent, not wins more frequent.
- finding: MIGRATED runners mostly kept going: 17.6% of coins hit 2x against 20.8% that hit 1.5x, so ~85% of those reaching 1.5x also reached 2x. For this setup the 1.5x exit may cut winners short. Small sample, but worth testing an exit at 2x for initials (V2, V11).
- idea to test: Cost gate, to apply before any other rule: skip if est_round_trip_cost_pct > 5% at the intended size. Also re-run every bucket at $25, $50 and $100 sizes to see whether any setup turns positive once costs drop. The current $10 'probe' is not a size where fees work.
- idea to test: FINAL_STRETCH, checklist passed, 5m volume ≥ $10k, buy ratio ≥ 0.55. Exit at 1.5x or -20%, plus a time stop if it stalls under bond. Success bar: ran% ≥ breakeven at the actual logged cost, with n ≥ 50 unique coins.
- idea to test: MIGRATED exit variant: sell initials at 2x, trail the rest at -30% from the peak, hard stop -20%. Compare net% against the 1.5x simple plan on the same coins.
- idea to test: MIGRATED, age 0.5–3h, mcap $40k–$150k, 5m volume ≥ $10k, flow ratio ≥ 1 (5m volume at or above its hourly pace). Versus MIGRATED with age over 3h. Tests whether this day's young runners are a pattern or a few outliers.
- idea to test: Exclude MIGRATED where age > 12h and mcap is under $70k (outside both guide windows, V1 and V6). Report them separately so old revived coins like HODL don't mix with fresh migrations.

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
Not quiet, but the movers are split. The hot money is in pump.fun name-plays and pop-culture jokes under about an hour old: MIKEDYSON is +1098% in 1h on $4k of 5m volume, Plurality has $49k of 5m on a $24.5k cap at 58% buys, and Justice For MengLan has $16.7k of 5m, with Jupiter Incident also in the mix. That is momentum, and most of it is a rug or a chase until proven otherwise (V1, V6). Brand and internet-slang launches are fading: KYC is -62% in 1h, Betty -41%, and GIF is only holding because it is already up 62%. Old one-word jokes are dead air: greg, Max and DIGS each do under $1k of 5m volume, and BLOB has $8k of 5m on a $16.5M cap, above the V6 $11M ceiling, so it is outside the recon range. Setups to research now: Plurality as a FINAL_STRETCH candidate (check its distance to bond and whether the $49k of 5m is organic or bundled), and MIKEDYSON only if it pulls back and holds, since +1098% in an hour is exit-liquidity territory. PushCoin, DESSA and Tesla FSD appear only in the web text, not the scan, so I am not weighing them.

## Moving most in its scans, last 30 min (1h volume)
- OpenIndex: $1,030,687 1h vol, $458,061 mcap, +95% 1h  
  CA `FuKY3dk7QmpbDdQRjzbjB3G6PiCuqKNvN4dAWDpwpump`
- SINGULARTY: $511,467 1h vol, $71,930 mcap, +163% 1h  
  CA `DJcHva2UJnRUPxzVfczcYyqxRtpwDTPcok6irtNmpump`
- OMGAI: $102,564 1h vol, $27,359 mcap, -44% 1h  
  CA `AHDP4wVa73GQYSP6AhrC2f5eE5CfkpCyyzwLg5WQpump`
- IF: $83,071 1h vol, $32,566 mcap, -5% 1h  
  CA `3hi7qBus11Xg9Pmj7xuuK9pjmKF7UUhT5uh7SXQbhsQt`
- earball: $76,835 1h vol, $97,265 mcap, +90% 1h  
  CA `FryQiSLqU7NfPvpQJRiYrVuvRRW66uB4FLorrKmjpump`
