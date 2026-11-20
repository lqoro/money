# Trencher live report

Updated 2026-11-20T20:10:13Z (paper trading, never real money)

- Equity: $74.23 (-25.8% vs $100 start)
- Closed trades: 22, 3 wins
- Fees paid: $14.78 (axiom $2.81, network $9.18, pool $2.66), plus $4.15 lost to slippage
- New trades: WATCH-ONLY (scans and decides, buys nothing)
- Brain: subscription, claude-haiku-5-5 for routine calls, claude-opus-5-5 for the daily review; 344 routine calls and 152 plan-limit hits in 48h
- Watch log: 85 coins being followed, 2423 filed, 0 would-buys (6h follow, sampled every 2 min)

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
- 20:09Z: 5 coins, 5 with pairs, 0 passed the market filters, 0 researched

## Coins it looked at, and why it passed
- 19:59Z GTA (MIGRATED, $203,465 mcap, $17,461 5m vol): REJECT, Top 10 hold 42.3% ex-pool (>25%) (V13)  
  CA `3fWhdo8bQCamw5ed6yNGdvaru1qS5UVwB6dYp9znpump`
- 19:50Z GATO (MIGRATED, $3,431,414 mcap, $4,365 5m vol): REJECT, Dev holds 2.7% (>1%) (V13, V17)  
  CA `HsprHxBRgiVaQdRf3TnKNuZZtaX9JUSPgMFdAkk6pump`
- 19:37Z MATHISOVER (MIGRATED, $78,391 mcap, $3,052 5m vol): PASS at conviction 2, PASS: chasing, flow below pace, no higher low, and the story lives on the coin's own site. Blockers: chasing / flow below pace / no higher low. (V1, V6, V13)  
  CA `3JgkhGnN5ggpE14Ykb2sgcsF1LTBUFyVZBPa3VrDpump`
- 19:37Z PAY (FINAL_STRETCH, $22,276 mcap, $30,806 5m vol): PASS at conviction 2, PASS: four-minute-old pump.fun coin up 1075% in 5m with no story and no X. That's a spike, not a setup (V1, V6).  
  CA `GdqJ3D4BF6ZKtpXajVqZTP39vrwD8wDXZGgw7tBA8PAY`
- 19:36Z jingyu (DIP, $72,284 mcap, $4,067 5m vol): REJECT, Bundles: 1 linked wallet cluster(s) hold 100.0% of supply (>20%) (V17)  
  CA `DUZrwdjEthcJ99ZiRXr31UuqTohoTg7VjTEyfGdBpump`
- 19:34Z DYSON (MIGRATED, $382,014 mcap, $9,907 5m vol): PASS at conviction 2, PASS — 5m flow at 0.31x its hourly pace, under an hour old and still bleeding off a +1010% spike, no printed higher low. The site says "CA TBA" and the dog theme is fading. (V1, V6, V13)  
  CA `C2As2w55q3V3snKVCyA3nZvmQJSx2NApM5SLK5krpump`
- 19:33Z runner (FINAL_STRETCH, $16,946 mcap, $3,210 5m vol): REJECT, RugCheck danger: Creator history of rugged tokens  
  CA `RUnnEr6YskBKYibKeUZRHaDQAAfdgYZPoikkmv4NnLx`
- 19:25Z OGTA (MIGRATED, $133,000 mcap, $3,618 5m vol): PASS at conviction 2, PASS — OGTA is 94% off its $2.07M high in a fading GTA theme, with 12 copies and $3.6k of 5m flow. Blocker: too deep, no catch. (V1, V6, V13)  
  CA `7bCiddGLe5aM8HE2pigT9jsqkmC1HSPxyXN6GkHEpump`
- 19:24Z LOOSY (MIGRATED, $278,851 mcap, $2,622 5m vol): PASS at conviction 2, PASS. Down 91% from a $3.03M peak, 5m flow at half pace, no higher low, and the site doesn't show this CA. Blocker: "flow below pace" plus "theme volume below pace". (V1, V6, V13)  
  CA `HF2RBPrfNBk9TxggL2cYZFEKSgirzh5HKCngLENTpump`
- 19:22Z FIENA (MIGRATED, $99,280 mcap, $6,230 5m vol): PASS at conviction 3, PASS: flow below pace. FIENA is at 0.63x its hourly 5m pace, and a shallow-band MIGRATED entry needs at least pace. The holders are clean, but clean holders don't make up for thin flow. (V1, V6)  
  CA `FqjZnuzRv3QYQQQrRRxt6fAGtrnaXnPXFabExM7Ppump`

## What its skips did next (last 48h)
A skip "ran" if the coin reached the first target (1.5x) from the skip price before a 20% drop, "dumped" if the drop came first. Sampled every 10 min, followed 6h.
- top 10 over 25%: blocked 61, ran 4, dumped 52, flat 4, open 1 (saving losses: keep it)
  - ran: DAKITTY up to 1.51x  
    CA `3YyNSd5dAe5hbKu83syLCjZKWYD9d94EGYCfEWNkpump`
  - ran: AudaCity up to 1.66x  
    CA `ERDrmaqsoeLdsCMMpBKkRM4LV1mzTA2KHrVxKLpqpump`
  - ran: Audacity up to 2.7x  
    CA `5oYuJG44HdkSSj2pabAKzKk7p2p3b1LbqUC5n82ppump`
- falling knife (code): blocked 40, ran 3, dumped 35, flat 1, open 1 (saving losses: keep it)
  - ran: DCTC up to 2.59x  
    CA `47f8bEDWs6VDpnnmxegyL4A3GbBVVcssrMQeBjPvpump`
  - ran: BUNC up to 1.91x  
    CA `43Z5f8GboUfc6M6wtaGGtFciEhLXixJEwQKv8wBUpump`
  - ran: PIPI up to 1.65x  
    CA `6MKD1NkLvWRqdbFtqmgACBwUV5o6GJpZry8HkNgzpump`
- RugCheck danger: blocked 28, ran 5, dumped 22, flat 0, open 1 (saving losses: keep it)
  - ran: CATCOIN up to 2.06x  
    CA `9JngoeaZHbV4f5EyRR3oDLNPH7VUGw1PYQC4s6j2pump`
  - ran: Leonida up to 1.51x  
    CA `9rbKkz2BDQBVgZmrHY6d7PTq2ge91gkpEyE4y9PPpump`
  - ran: PIPI up to 1.63x  
    CA `J51xgomTx21VHY62Q7uv2otWRUSq71WeaApLfsAnpump`
- flow below pace: blocked 18, ran 3, dumped 12, flat 1, open 2 (saving losses: keep it)
  - ran: SI up to 1.53x  
    CA `4s38cgZJN4J39S2BQwCkcsJJ9ZGeJSjw8vK9wVtupump`
  - ran: AI up to 1.51x  
    CA `8SacNb6sgiAcscRe4m915B6nL9XX55dk8FS7L532pump`
  - ran: SWRDXSTFF up to 1.77x  
    CA `Csoj9XHJfBAxsKswqKKBENnGeoRDHtACfyYi7HmJpump`
- thin 5m volume: blocked 16, ran 1, dumped 11, flat 4, open 0 (saving losses: keep it)
  - ran: Snapmatic up to 1.68x  
    CA `4S8pUKWKUAtQKfE5qokSjszWDp1RqQWnom8jNYSWpump`
- too new / sniping: blocked 16, ran 1, dumped 15, flat 0, open 0 (saving losses: keep it)
  - ran: AudaCity up to 1.96x  
    CA `3rtTUCpe1BBgCTNWQ9jK3xkAz1E7SPqMt4uYHx1Bpump`
- near the high / chasing: blocked 15, ran 3, dumped 12, flat 0, open 0 (saving losses: keep it)
  - ran: BEAR up to 2.32x  
    CA `DCPm44cT9i39HjR13QHYgxkR7wEx9TDeniGuayB5pump`
  - ran: ZOL up to 1.55x  
    CA `UQLWvkwiSsnViuVBy7oArMtzb5RAZyrdJ79amQFrzoL`
  - ran: STICK up to 2.08x  
    CA `532iaQrhFCD3QKFHsAtFAQ1mQZMjMdNrPXLeCS6cpump`
- dev share over 1%: blocked 13, ran 2, dumped 9, flat 1, open 1 (saving losses: keep it)
  - ran: LOOSY up to 1.71x  
    CA `FtSWWxVmKNXz8ksJxzJJ7BdDWXbQb3vC94J99oyypump`
  - ran: MANDY up to 1.54x  
    CA `GQngHP8P6s45MxWnU7JsocfV2HjPQdJZmCEAYKpBpump`
- bundles over the line: blocked 13, ran 1, dumped 9, flat 2, open 1 (saving losses: keep it)
  - ran: PAPA up to 1.66x  
    CA `3hdXmQqZHmm7gWWweFKGdkjnxyWQZ2SWVNt1Jty5pump`
- other: blocked 13, ran 3, dumped 10, flat 0, open 0 (saving losses: keep it)
  - ran: After up to 2.36x  
    CA `Db2s6iVvenVhJkj96P4UbZWEAYX4nUhgXhSVbQrwpump`
  - ran: Ant up to 2.32x  
    CA `HKGtUPPKvXkMPyNX4QeMubENuiimFQ8W1Veg4y52pump`
  - ran: PAY up to 3.67x  
    CA `GdqJ3D4BF6ZKtpXajVqZTP39vrwD8wDXZGgw7tBA8PAY`

## Daily review (2026-11-20, claude-opus-5-5)
No edge yet. All 322 settled coins lost money after costs on the simple plan, and so did every setup: the average was -13.8%, of which about 9.9% was round-trip cost, so the price moves alone already lost about 4%. With a +50% target, a -20% stop and about 10% cost, a winner nets about +40% and a loser about -30%, so a setup has to reach 1.5x before the stop roughly 43% of the time just to break even. The best bucket, FINAL_STRETCH, did it 27.7% of the time (n=47). The overall average is clearly negative: about ±3.6 points of noise at n=322. Even FINAL_STRETCH's -10.6% has a 95% range of roughly ±9 points that stays below zero, and the real sample is smaller than it looks because of meta clustering (GTA and FIONA copies) and at least one coin logged twice. The routine model made zero would-buys, so there is nothing to compare against what it passed on. The 79 coins it reviewed and passed did -14.4%, the same as the 168 the checklist failed (-14.0%). On this data neither the checklist nor the model separates winners from losers.
- finding: Overall (n=322): 19.3% reached 1.5x before the -20% stop, 68.6% hit the stop, the median coin peaked at only 1.24x, average net -13.8% with 9.9% average cost. The typical coin's best move barely covers costs twice over.
- finding: The simple plan's result is roughly ran% × +40 − dumped% × 30. For all coins that gives 0.193×40 − 0.686×30 ≈ -12.9%, close to the measured -13.8%. The losses come from the hit rate, not from a few bad outliers.
- finding: FINAL_STRETCH (n=47) is the least bad: 27.7% ran, 25.5% hit 2x, median peak 1.38x, net -10.6%. That is still well short of the ~43% ran rate needed to break even. MIGRATED (n=222): 20.7% ran, net -13.1%.
- finding: DIP is the worst setup (n=53): 5.7% ran, median peak 1.14x, net -19.9%. More DIP coins hit 2x at some point (9.4%) than hit 1.5x before the -20% stop (5.7%), so the stop often fired before a later run. Even so, nothing here justifies buying dips: they mostly did not bounce.
- finding: Checklist failures (n=168): 17.3% ran, 64.9% dumped, net -14.0%. Coins the model reviewed and passed (n=79): 21.5% ran, 74.7% dumped, 24.1% hit 2x, net -14.4%. Passing the checklist gave a wider spread of outcomes (more 2x, more dumps) but no better average.
- idea to test: Set every rule's thresholds before looking at the week's data, then score them on a holdout of days the rule wasn't tuned on. For any rule to be worth testing live, its subset needs n ≥ 40 and an average net whose 95% lower bound is above 0. Anything else counts as noise.
- idea to test: Cost gate: only count coins whose estimated round-trip cost is ≤ 5% (if per-coin cost isn't logged, use mcap ≥ $100k as a stand-in). Compare net % with the ≤5% and >5% cost groups side by side. The idea: with a 1.24x median peak, a coin only has room for profit if its pool is deep.
- idea to test: FINAL_STRETCH-only test: setup = FINAL_STRETCH AND checklist = pass AND 5m volume ≥ $10k AND buy ratio ≥ 0.55 AND flow ratio ≥ 1.0. Score it on both the simple plan and a 2x target / -35% stop / 60-minute time stop.
- idea to test: Exit-shape test on all setups: compare +50%/-20% with 2x/-35% and 2x/-50% (all with a 6h time exit). The DIP numbers (more coins hit 2x than 1.5x-before-stop) suggest the -20% stop sits inside normal noise; 68.6% of all coins hit it.
- idea to test: DIP suspension test: drop DIP entirely, or allow it only when drawdown is 40-55% AND 5m volume ≥ its 1h average pace (flow ratio ≥ 1.0) AND buy ratio ≥ 0.55. Check whether any DIP subset gets above a 25% ran rate. If none does, retire the setup.

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
The meta is brand-name and cryptid tickers with live 5m flow. The cat/animal wave is a 1-hour spike that has gone thin: BTC and CATPOOP are at $0 to $3k 5m and MAYA is at $0, so I'm trusting the scan over the crawler's cat numbers. Three themes are live: (1) brand and domain names, with Singularity.com on two CAs at $279k and $95k 5m, 54% and 83% buys, only about 6 minutes old, which is a vamp fight, so find the original before anything else; (2) cryptids, with BIGFOOT IS REAL at $18.8k 5m, 54% buys, $34k cap, while The Bigfoot Files has zero buys, so it's split; (3) MIC, a country-name coin at $96k 5m with 52% buys. Fading: Trump and GTA (OFFICIALGTA at $3.6k 5m, 25h old, and the Trump dinner news is down 98%), dog/doge names (HOGE and LOOSY under $7k 5m), and holiday names (RUDY at 44% buys). Setups to research, not buy: BIGFOOT IS REAL, and the Singularity original once identified, only on a pullback that holds 5m above $10k with buys above half; MIC and both Singularity pairs are up 140-500% in an hour, so that is chase territory. Holder, dev and bundle checks are pending on all of these, so this is a read, not an entry.

## Moving most in its scans, last 30 min (1h volume)
- Singularity: $244,286 1h vol, $1,291 mcap, -97% 1h  
  CA `7KUg78hyohckj8i728YuCu6CweTArxhwRrVrFyvHpump`
- Singularity: $125,987 1h vol, $17,655 mcap, -49% 1h  
  CA `FBKkoVcXaHzpLHheCRnPk3zvLgiqhugbwGcegc9Ykvxx`
- BIGFOOT: $110,485 1h vol, $10,396 mcap, -34% 1h  
  CA `Aykavwa4Z1Z2pW3CRuRpXBXrNZAtuhzAskgBFXFgpump`
- MIC: $82,723 1h vol, $15,065 mcap, -69% 1h  
  CA `G6H8DjYRPomfmG5KrEAMpxoUU2uRLxdeTrkxnSiXpump`
- FIENA: $71,557 1h vol, $1,272 mcap, -98% 1h  
  CA `FqjZnuzRv3QYQQQrRRxt6fAGtrnaXnPXFabExM7Ppump`
