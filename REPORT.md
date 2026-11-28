# Trencher live report

Updated 2026-11-28T13:49:46Z (paper trading, never real money)

- Equity: $74.23 (-25.8% vs $100 start)
- Closed trades: 22, 3 wins
- Fees paid: $14.78 (axiom $2.81, network $9.18, pool $2.66), plus $4.15 lost to slippage
- New trades: WATCH-ONLY (scans and decides, buys nothing)
- Brain: subscription, claude-haiku-5-5 for routine calls, claude-opus-5-5 for the daily review; 361 routine calls and 9 plan-limit hits in 48h
- Watch log: 65 coins being followed, 4474 filed, 0 would-buys (6h follow, sampled every 2 min)

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
- 13:48Z: 9 coins, 9 with pairs, 1 passed the market filters, 1 researched

## Coins it looked at, and why it passed
- 13:49Z John (MIGRATED, $39,786 mcap, $47,630 5m vol): REJECT, RugCheck danger: Creator history of rugged tokens  
  CA `EvN4RDyoqUTpCcrvz5QTAdHVqypgxV4MCR77Bfnjpump`
- 13:45Z Zhaki (DIP, $170,602 mcap, $2,124 5m vol): REJECT, Dev holds 3.8% (>1%) (V13, V17)  
  CA `2YAfPhCrGSW82Ra33sWgurXt4dQ29SwXusvUXdJGpump`
- 13:43Z JOB (MIGRATED, $2,873,712 mcap, $1,143 5m vol): REJECT, 5m volume $1,143 is dead (<$2,000) (V1)  
  CA `9Pq7aLAbhDG2tTnS22cm6kuysZVcZpLFE368HWuypump`
- 13:33Z Bagwork (no setup, $13,901 mcap, $27,966 5m vol): REJECT, No setup fits: not Final Stretch, not a migrated runner, not a healthy dip  
  CA `5qDeCs9MkTAhk6q76XvKrZgimoQdJowuSWbjSZKvpump`
- 13:32Z hacked (DIP, $41,232 mcap, $19 5m vol): REJECT, Hack story ("hack" in the name or ticker): these tend to go down, owner rule  
  CA `FK7bc3fR8UL8uogN2u8J9yEpEbQJKR7yKsp3G8rvpump`
- 13:23Z BRUH (DIP, $6,728,476 mcap, $2,068 5m vol): PASS at conviction 2, PASS — $6.7M mcap with 5m flow at 0.64x pace, no catalyst, and the theme running at 0.5x. Price bounced from a $5.3k hourly low into the 24h high, so this is a chase, not a dip (V1, V6, V13).  
  CA `PgFtGGquvnv2zEkjG2N2QPvBTBrafuExGYEqahRpump`
- 13:22Z BITCOINU (DIP, $1,211,863 mcap, $3,116 5m vol): PASS at conviction 3, PASS — 5m flow at 0.63x the hourly pace, and the story behind the bottom buy isn't rising. 19 tickers in a crowded same-name field. Dead on arrival (V1, V6, V13).  
  CA `ATbAsdCwrhhVg23DRnWpjqx6kx7ivoK5o8ysNmu1pump`
- 13:21Z Fireball (DIP, $530,789 mcap, $3,825 5m vol): PASS at conviction 3, PASS: no catalyst, theme pace 0.71x, and the site doesn't show this CA. Blocker: "dead story" on a bottom buy (V1, V3, V13).  
  CA `B9wbjDJ4FbHMsZmoXAkJSTAwuePaJUKbySvnK5zApump`
- 13:21Z hold (MIGRATED, $58,594 mcap, $16,186 5m vol): PASS at conviction 3, PASS: "hold" is sitting 1.5% off a 15-minute-old peak after a +99% hour, with no printed higher low and 9 same-ticker copies. Chasing, too new (V1, V6).  
  CA `4qnvryLCPUQ1kLZMsK44Ra2H19tRGzijbbhfDmSLpump`
- 12:53Z BNB (FINAL_STRETCH, $24,332 mcap, $27,243 5m vol): PASS at conviction 2, PASS: BNB is 8 minutes old, up 267% on 5m and 916% on the hour, with 25 copies of its name. Chasing a spike at the peak. Blockers: "chasing spike" and "too new". (V1, V6)  
  CA `3V8dPY9yH4TSHm11fx6Po7XJ8xPzSjcf8W9Q3QhXpump`

## What its skips did next (last 48h)
A skip "ran" if the coin reached the first target (1.5x) from the skip price before a 20% drop, "dumped" if the drop came first. Sampled every 10 min, followed 6h.
- top 10 over 25%: blocked 49, ran 10, dumped 35, flat 2, open 2 (saving losses: keep it)
  - ran: Thankful up to 2.05x  
    CA `E9arxG4RxB7Gxt6U75obonTZzx7vpbc4bUi1dfw3BtUN`
  - ran: MSTR up to 1.69x  
    CA `57sCZ82FwS5Dfs7FN9nshtU5Mkb3w1dqhmPUuCPvpump`
  - ran: Kuro up to 2.05x  
    CA `7sxuap7Q4uoAJFBW3ensq6QTa2KwgGosfFwoeXtJpump`
- flow below pace: blocked 38, ran 5, dumped 27, flat 4, open 2 (saving losses: keep it)
  - ran: PAIR up to 2.1x  
    CA `32rBxcFjCFnyqZ41CEPM5AL67X1dcw8w83vZt6Kxpump`
  - ran: Hoppy up to 1.76x  
    CA `CFX1gH7CKYwqYXrfDkS2MUxJcEhs8PT63DyRA1chpump`
  - ran: SpaceXCoin up to 1.52x  
    CA `G2XqmSc8vJpLLwaLVXUeNkxsrhVT8vQ3Pje8MqeDpump`
- too new / sniping: blocked 35, ran 2, dumped 33, flat 0, open 0 (saving losses: keep it)
  - ran: SpaceXCoin up to 1.52x  
    CA `G2XqmSc8vJpLLwaLVXUeNkxsrhVT8vQ3Pje8MqeDpump`
  - ran: FARM up to 1.65x  
    CA `2dynAjPBnkqzjUwozgn8pDRkCf7k7CDJkLfcf4rupump`
- near the high / chasing: blocked 33, ran 7, dumped 24, flat 2, open 0 (saving losses: keep it)
  - ran: urcoin up to 1.71x  
    CA `25m4Lkct8nsYyqAMeE8rvjM3y5Zrrax46TLqNJjbpump`
  - ran: Meme up to 2.06x  
    CA `CV1NPi8L2PSYMfALBh7GCfUwELZzG3DrLUUjCkeapump`
  - ran: IceBall up to 1.67x  
    CA `6PFm828RKNJqKvjXQz82hhGvGNWFXZcBHNCF4U7spump`
- falling knife (code): blocked 21, ran 1, dumped 18, flat 1, open 1 (saving losses: keep it)
  - ran: Split up to 1.54x  
    CA `HAP9FcXubD88SjRHMY1kr5iukpRZgeMAgCBam3Vtpump`
- bundles over the line: blocked 19, ran 3, dumped 12, flat 3, open 1 (saving losses: keep it)
  - ran: Dragon up to 1.55x  
    CA `cg3HaDWhAKFfj9aq79TWUBgmxfs4G7byQ7feaxnpump`
  - ran: monky up to 96.37x  
    CA `At5hmwDn4YgPDoic1UN7zMdTtCoiXJsMhnKaoazEpump`
  - ran: USD1 up to 1.55x  
    CA `8Y24KBnY9gaNWDaxohxtEU1gxESvfwdYeGFuHJKpump`
- falling knife / no higher low: blocked 16, ran 2, dumped 10, flat 2, open 2 (saving losses: keep it)
  - ran: Hoppy up to 1.76x  
    CA `CFX1gH7CKYwqYXrfDkS2MUxJcEhs8PT63DyRA1chpump`
  - ran: SPSC up to 1.58x  
    CA `EjdrRG2si1FQ3Bme5g6WSYNHJDrsKUrbGB4Z5xaopump`
- other: blocked 13, ran 2, dumped 10, flat 1, open 0 (saving losses: keep it)
  - ran: Christmas up to 1.89x  
    CA `5hkBYuFQDpAAqemCiVqXCuU6Ya5dqKhtRobzJsg6pump`
  - ran: Bagwork up to 1.81x  
    CA `5qDeCs9MkTAhk6q76XvKrZgimoQdJowuSWbjSZKvpump`
- RugCheck danger: blocked 12, ran 1, dumped 9, flat 1, open 1 (saving losses: keep it)
  - ran: Snowball up to 1.56x  
    CA `9TKbd3VFaMSXsEAicD9JVQWpWwAoLi4fSgWmZL2cpump`
- dev share over 1%: blocked 9, ran 2, dumped 6, flat 0, open 1 (saving losses: keep it)
  - ran: bolphante up to 1.7x  
    CA `FVBzzG4ZcAgxSLW1rWjNC9EH9CgEgz1A4puNYexMpump`
  - ran: Fug up to 1.58x  
    CA `7mSf4uWLkgdkqBfSoxniv5aZ1sDCXCiquJNcisjXpump`

## Daily review (2026-11-28, claude-opus-5-5)
Nothing has a positive edge after costs. All 225 settled coins averaged -12.9% net under the simple plan, and every setup and every stage is negative. A rough 95% range for the pooled average is about -17% to -8% (wider still because same-day coins move together), so this isn't noise around zero. Before costs, the pooled result is only about -3% and MIGRATED is about -1%. Most of the loss is the 9.9% estimated round trip on a $10 buy, the same thing that broke the live trades (fees and slippage were $18.83 of the $25.79 lost). With 1.5x / -20% exits and ~10% costs, about 43% of entries would need to reach 1.5x before -20% just to break even. The observed rate is 20% (22.8% for MIGRATED). Nothing can be said about the routine model's picks: it made 0 would-buys out of 124 coins it judged, so there is nothing to compare against what it passed on. Coins it passed on (-12.9% net) and coins the checklist killed (-13.0%) did almost exactly the same.
- finding: Costs decide everything. All coins: avg net -12.9%, avg cost 9.9%, so about -3.0% before costs. MIGRATED (n=149): -10.9% net with 9.8% cost, so about -1.1% before costs, roughly random. FINAL_STRETCH (n=44): -18.9% net, about -8.8% before costs. DIP (n=32): -13.9% net, about -4.2% before costs.
- finding: Breakeven math for the simple plan: a win is about +40% after costs and a loss about -30% or worse (gaps make it worse). Breakeven needs about 43% of entries to reach 1.5x first. Observed: 20.0% overall, 22.8% MIGRATED, 15.9% FINAL_STRETCH, 12.5% DIP. Even with zero costs the bar would be about 29%, and no group reaches it.
- finding: FINAL_STRETCH is the worst setup. n=44, 84.1% hit -20% first, 0% flat, -18.9% net. But 22.7% touched 2x sometime in the 6h, versus only 15.9% that reached 1.5x before -20%. So about 7 points of FS coins got stopped out and then ran. That fits the pre-bond dump (V1), but it is about 3 coins, too few to justify a wider stop.
- finding: DIP is weak on upside. n=32, only 9.4% ever hit 2x (lowest of any setup), median peak 1.26x, -13.9% net. The sample is too small to drop the setup, but nothing here supports it either.
- finding: MIGRATED is the least bad (n=149, 24.2% hit 2x, -10.9% net). The gaps between setups are within noise: MIGRATED vs FS is about 8 points apart with a standard error of about 6.
- idea to test: Hold every idea to the same bar before testing anything. Use the full window since Nov 3, dedupe by CA (first sighting only), choose each rule in advance, split by day (e.g. fit on Nov 3–17, check on Nov 18–28), and require n≥100 with the 95% lower bound of average net above 0 after costs. Anything less is a story.
- idea to test: Cost filter: only test coins whose estimated round trip cost is under 5% (bigger pools). Compare net by cost tertile. Cost is the one lever that clearly moves the result.
- idea to test: Size check, a costs question not an edge question: rerun net with the same cost model at $25 and $50 buys. If cost is mostly fixed fees, MIGRATED's ~-1% before costs shows how close to zero the result can get. That is still not an edge, and it doesn't change the per-conviction loss limit.
- idea to test: MIGRATED by age: split age<0.1h, 0.1–1h, 1–6h, 6–12h and mcap $30–70k, $70–300k, $300k+. Test whether age 0.1–2h with mcap $30–150k, checklist pass, 5m volume ≥ $10k and buy ratio ≥ 0.55 beats baseline. This is aimed at the young-runner pattern while keeping the 'too new' block in place.
- idea to test: FINAL_STRETCH exclusion test: how does pooled net change with FS removed entirely? Separate test: FS only when flow ratio ≥ 1.0 (5m volume at or above its 1h pace) and 5m volume ≥ $10k.

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
The meta in scan_movers is cat and animal mascot names plus CJK-character names on pump.fun, with slogan tickers (hold, Bagwork) riding launch spikes. The Trump-dinner news isn't in the movers and there's no Trump-family coin in the top volume, so I'm treating that story as fading. Rising: "hold" (Believe in something?, $58.6k cap, $16.2k 5m, 62% buys, +99% 1h, 12 min old) is the cleanest mover clearing the $10k bar; OKOWARE (怒ワレ, $21k cap) and smol cat ($14.6k cap, 78% buys) carry the cat/CJK style but are thin on 5m. Fading: BNB (Bankrupting New Buyers, -91%) and EDITOR (-87%, 11% buys). The crawler's FlipFlop Cat figures ($60k cap, +103%, clearing the bar) don't match scan_movers ($2.2k cap, -97% 1h, zero 5m volume), so I'm discarding them. Setup to research: "hold" as a MIGRATED probe. Conviction 4, so it's a PASS until holder, dev and bundle checks come back clean; if they do, it becomes a 5 probe, buying only on a pullback that holds with 5m volume above $10k, initials at 2x, stop at -30%, and out if 5m volume drops under $10k. Bagwork ($16k cap, $32k 5m, age zero, still on the pump.fun curve) is a launch spike; the new-pair rule says I don't chase it.

## Moving most in its scans, last 30 min (1h volume)
- BNB: $93,742 1h vol, $2,739 mcap, -91% 1h  
  CA `3V8dPY9yH4TSHm11fx6Po7XJ8xPzSjcf8W9Q3QhXpump`
- hold: $86,891 1h vol, $58,594 mcap, +99% 1h  
  CA `4qnvryLCPUQ1kLZMsK44Ra2H19tRGzijbbhfDmSLpump`
- BITCOINU: $58,669 1h vol, $1,203,391 mcap, +13% 1h  
  CA `ATbAsdCwrhhVg23DRnWpjqx6kx7ivoK5o8ysNmu1pump`
- Fireball: $54,548 1h vol, $530,789 mcap, +13% 1h  
  CA `B9wbjDJ4FbHMsZmoXAkJSTAwuePaJUKbySvnK5zApump`
- FlipFlop: $53,789 1h vol, $2,241 mcap, -97% 1h  
  CA `8yUDvFWAHXBXSdgcRJZ7cWtFb1DZ1dwaQeYhb7kEpump`
