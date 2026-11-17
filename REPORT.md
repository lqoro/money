# Trencher live report

Updated 2026-11-17T01:02:05Z (paper trading, never real money)

- Equity: $74.23 (-25.8% vs $100 start)
- Closed trades: 22, 3 wins
- Fees paid: $14.78 (axiom $2.81, network $9.18, pool $2.66), plus $4.15 lost to slippage
- New trades: WATCH-ONLY (scans and decides, buys nothing)
- Brain: subscription, claude-haiku-5-5 for routine calls, claude-opus-5-5 for the daily review; 422 routine calls and 1 plan-limit hits in 48h
- Watch log: 131 coins being followed, 1890 filed, 0 would-buys (6h follow, sampled every 2 min)

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
- 01:00Z: 9 coins, 7 with pairs, 1 passed the market filters, 1 researched

## Coins it looked at, and why it passed
- 01:01Z IFRUIT (FINAL_STRETCH, $20,384 mcap, $24,317 5m vol): REJECT, Dev holds 2.2% (>1%) (V13, V17)  
  CA `EykPg5B2c5Gd7VTsiGJRGtx3A3W44sD9ATmiGziDpump`
- 00:59Z DIGS (MIGRATED, $196,498 mcap, $1,962 5m vol): REJECT, 5m volume $1,962 is dead (<$2,000) (V1)  
  CA `9QT8K685Hrae4k11dhGXirdtpfAaimExtyfwt8cPpump`
- 00:57Z JOB (MIGRATED, $2,047,661 mcap, $2,242 5m vol): PASS at conviction 2, PASS: JOB is a 23-copy ticker field with a 17.2% linked bundle cluster, flow at 0.66x pace, and the last 15m close under the hourly low. Old coin, no catalyst. (V1, V3, V13)  
  CA `9Pq7aLAbhDG2tTnS22cm6kuysZVcZpLFE368HWuypump`
- 00:56Z LUCIA (MIGRATED, $97,562 mcap, $4,109 5m vol): PASS at conviction 2, PASS — this is a copy of the LUCIA leader, and its own 5m flow is 0.24x its hourly pace with no printed higher low. Blocker: flow below pace / split crowd (V1, V3, V6).  
  CA `HgDyiDQ2hfcPiYoSgzfu7848Aw4iFyPt6sWpmXnSpump`
- 00:51Z AGI (DIP, $50,259 mcap, $6,380 5m vol): REJECT, RugCheck danger: Mint Authority still enabled  
  CA `CUmQsPuWxK97tYYWV44qhHXEu69oM4nj3CpYBTw796ea`
- 00:49Z BINDER (MIGRATED, $32,801 mcap, $9,600 5m vol): REJECT, Top 10 hold 25.8% ex-pool (>25%) (V13)  
  CA `Q9kYktMbrdEt7oXwC4AqK9Jqyqjqax2VE6j5wwjpump`
- 00:48Z LUCIA (MIGRATED, $422,745 mcap, $88,092 5m vol): REJECT, Top 10 hold 43.0% ex-pool (>25%) (V13)  
  CA `27Ggmg2ZmaehHX7L5vZqCeTRoQmPaBtR5vqvaRLbpump`
- 00:45Z ETF (MIGRATED, $255,182 mcap, $4,413 5m vol): PASS at conviction 3, PASS: flow below pace, 21-copy same-ticker field, and a 27% bottom buy with no catalyst. Blockers: "flow below pace", "split crowd", "no catalyst" (V1, V13).  
  CA `Gg5aWvfucyMwihDzyfCEaLgyeeNE2dkob2LTwWfHpump`
- 00:43Z LEOSTAR (MIGRATED, $1,073,414 mcap, $6,160 5m vol): PASS at conviction 2, PASS: flow below pace (5m at 0.54x hourly, sells ahead of buys), theme at 0.43x, and 13 same-ticker copies. The prior high is only 1.36x away. Name is a field, not a story. (V1, V6, V13)  
  CA `2cMcMEX3Eqo86tUrVe5dgHp5GZNwqQ6crqm22UeZpump`
- 00:39Z BLACKOUT (MIGRATED, $56,475 mcap, $1,649 5m vol): REJECT, 5m volume $1,649 is dead (<$2,000) (V1)  
  CA `Cza8qQwR659D6j9rHdxJvHmuwEJg81QZGMCQz43Kpump`

## What its skips did next (last 48h)
A skip "ran" if the coin reached the first target (1.5x) from the skip price before a 20% drop, "dumped" if the drop came first. Sampled every 10 min, followed 6h.
- flow below pace: blocked 54, ran 9, dumped 40, flat 2, open 3 (saving losses: keep it)
  - ran: PASSED up to 1.73x  
    CA `3XaH8VPUaUegqmnkYA8PXCWqQqD8doqdsGGfZyoYpump`
  - ran: ANT up to 1.52x  
    CA `BDPm9gPHCRyo2qjcRrYPsXexmbRwuuHQZo2qhhYXpump`
  - ran: ANT up to 1.58x  
    CA `7H2sHeLHyHR8jxENGmsqn7RxTkYZa4KwXvKYcoxBpump`
- top 10 over 25%: blocked 50, ran 10, dumped 33, flat 3, open 4 (saving losses: keep it)
  - ran: rockstar up to 1.95x  
    CA `9HFUEab7sompLDPTAaTGkryMNGbtBaFMhHMVpJEBpump`
  - ran: VI up to 1.71x  
    CA `4Dj8m9vWqu779F1KDBUttvXM8YFm7U92SDpvjBNKtEiB`
  - ran: ANT up to 1.52x  
    CA `BDPm9gPHCRyo2qjcRrYPsXexmbRwuuHQZo2qhhYXpump`
- too new / sniping: blocked 45, ran 8, dumped 37, flat 0, open 0 (saving losses: keep it)
  - ran: Chick up to 1.66x  
    CA `Dueav76X9spnoLomhM2jMkkWorVggbeWucLs3YLupump`
  - ran: TOOLS up to 1.83x  
    CA `9Ei1d97U7M8m4t3fof7c8MUECtmzgqbQCo81cGGzpump`
  - ran: twert up to 1.81x  
    CA `8WvWwttzaLfW1nbjx6wmYL5jozWpvy95WktAg5cipump`
- near the high / chasing: blocked 43, ran 8, dumped 33, flat 0, open 2 (saving losses: keep it)
  - ran: penny up to 1.6x  
    CA `5gmCPpuktJ7Svjgr4PPJBTosAFKB8K6Z45EGfSUmpump`
  - ran: WIGGLES up to 1.69x  
    CA `2kWx47CUrcXtzptFNnbSXKq3vo1ebqyLBhRytKRGpump`
  - ran: Bustas up to 1.75x  
    CA `9rTgs58B3p11vXekTTgVYtv8vKxQ6oSoZFXPy4onpump`
- RugCheck danger: blocked 34, ran 8, dumped 24, flat 1, open 1 (saving losses: keep it)
  - ran: Ivy up to 1.88x  
    CA `DxNF3Qxd8XeUBdz7ReRdoiFzRmNDKbSz4c2oA7aRpump`
  - ran: SI up to 1.93x  
    CA `AiQUqe4zjiDssth2FsCoeQVaGtCtHYyKGX8U52rWpump`
  - ran: FUTA up to 2.77x  
    CA `FxoXV4C8DTSYeg5dSXrEsr45zzr8tpNbsrpoiZ8Kpump`
- falling knife / no higher low: blocked 18, ran 3, dumped 11, flat 3, open 1 (saving losses: keep it)
  - ran: CateGiving up to 1.57x  
    CA `5XasjCnMPTczL9VZTDHgbK5sQzwkjnu41oLeHf5Wpump`
  - ran: Nyajira up to 1.52x  
    CA `8cWGfiHyKqxgLrLtkPt2NnLkSUV2JbcLBf4RN6Fapump`
  - ran: GOAT up to 1.61x  
    CA `D7iafdwzzpB7tisqQqT5T9aRrYPtHLqzwxhnLoWJgoat`
- falling knife (code): blocked 17, ran 1, dumped 13, flat 1, open 2 (saving losses: keep it)
  - ran: BigP up to 1.57x  
    CA `CY254o6VPaJnTiY5uuKUB8xDjSgykC6xtoLoC3kpump`
- thin 5m volume: blocked 14, ran 2, dumped 10, flat 0, open 2 (saving losses: keep it)
  - ran: SENDER up to 1.58x  
    CA `5peJLZQnBkXtydYYMunbT4QutSyd9eA474MqxcmEpump`
  - ran: UNITY up to 1.66x  
    CA `GD6MboptxbHBspASr5PWozgNDrZxmxJ8JpBBD8Vpump`
- dev share over 1%: blocked 11, ran 2, dumped 7, flat 0, open 2 (saving losses: keep it)
  - ran: PANICSELL up to 1.74x  
    CA `82Z6CcE5g3o1jW3vgtcqr95jP4XFx8jg1SJe8ikepump`
  - ran: WSB up to 1.52x  
    CA `B82PFKmT4aM38EUUqVoZs6sZdAfxDHHrB6DSXxCKpump`
- other: blocked 11, ran 4, dumped 7, flat 0, open 0 (mixed)
  - ran: TaoTao up to 1.53x  
    CA `G1KuEMuLrxWynFddQVnpdkQAhYFBwNJiuz1Lv7d9pump`
  - ran: SI up to 1.94x  
    CA `H2irVtPLfKoBJ69itZmhsedSPwBUTaubmUavc6Uapump`
  - ran: BLOB up to 1.66x  
    CA `8s11PkgQt4ZzdZ7oo84hK5t9HG1EvdgAjcg4W7Lpump`

## Daily review (2026-11-16, claude-opus-5-5)
Nothing shows a positive edge after costs. Over 309 settled coins, every setup lost money net: FINAL_STRETCH -7.2%, DIP -7.4%, MIGRATED -13.5%. Costs alone averaged 9.8% per round trip. Before costs, FINAL_STRETCH made about +2.9% and DIP about +1.8%, but at n=46 and n=54 the noise is roughly ±4–5 points, so neither is different from zero. With a 1.5x / -20% plan and ~10% costs, you need about 43% of coins to reach 1.5x before -20% just to break even. The best group (FINAL_STRETCH) managed 32.6%, and the error bar on that is about ±14 points. The routine model gave zero would-buys, so the "did its buys beat its passes" question can't be answered. It passed on all 164 coins it reviewed. Those coins averaged -11.7% net, about the same as the checklist rejects at -11.3%, so passing on everything was roughly right this day, even though it missed LMAO, Marvin and WIGGLES.
- finding: Costs are the main problem. Average round-trip cost was 9.8% on a $10 buy, and the average net was -11.5%, so the coins themselves lost only about 1.7% before costs. This matches the real trades before the pause, where fees and slippage ($18.83) were 2.7x the price loss ($6.96).
- finding: FINAL_STRETCH (n=46) was the best setup and still lost: 32.6% ran, 26.1% hit 2x, median peak 1.44x, net -7.2% on 10.1% cost. A 95% interval on the run share is about 19–46%, which doesn't reach the ~43% break-even.
- finding: DIP (n=54) dumped least (33.3%), but most of these coins just went flat (about 54% neither ran nor dumped). Only 13.0% ran and net was -7.4% on 9.2% cost. Before costs it roughly breaks even; costs make it a loser.
- finding: MIGRATED (n=209) is the bulk of the flow and the worst setup: 17.2% ran, 66.0% dumped, net -13.5%. Even so, 3 of the 5 top runners were MIGRATED coins under 0.3h old, so these young migrations swing both ways.
- finding: Brain vs checklist: coins the brain reviewed and passed on (n=164) ran more often than checklist rejects (23.8% vs 13.1%) but also dumped much more (70.7% vs 49.0%). Net was the same (-11.7% vs -11.3%). The checklist sends the brain more volatile coins, not better ones after costs.
- idea to test: Cost gate: skip any coin whose estimated round-trip cost_pct is above 5%, then re-run every setup on the coins that remain. If no setup's before-cost result is above the remaining cost, that setup is dead at $10 size. Also simulate $25 and $50 buys to see whether the cost drag is mostly fixed fees.
- idea to test: FINAL_STRETCH candidate: setup=FINAL_STRETCH AND checklist passed AND 5m volume >= $10k AND buy ratio >= 0.55 AND flow ratio (5m vs hourly pace) >= 1.0. Before trusting it, require n >= 40 settled and a net above 0 with costs included.
- idea to test: DIP candidate: setup=DIP AND drawdown from high 40–70% AND peak mcap >= $70k AND flow ratio >= 1.0 AND buy ratio >= 0.55. The aim is to test whether coins with the crowd still arriving escape the 54% flat bucket. Run deeper drawdowns (>70%) as a separate bucket, not mixed in.
- idea to test: Young MIGRATED split: setup=MIGRATED AND age_hours < 0.5 AND mcap 30k–150k AND 5m volume >= $10k, compared against MIGRATED with age 0.5–12h. The question is whether the fat right tail pays for the 66% dump rate after costs. Score each bucket by mean net, not by hit rate.
- idea to test: Exit-plan comparison on the same logged coins: 1.5x/-20% vs 2x/-30% vs Trencher's real plan (sell initials at 2x, break-even stop after 1.3x, trailing stop on the rest). For a 1.5x/-20% plan to be worth running, a subset needs a first-touch 1.5x rate of at least ~43% at 10% cost (~36% at 5% cost).

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
The meta in the scan is the Vice City/GTA cluster, plus a wave of sub-$20k pump.fun micro-caps running 150-300% in the hour. Both are real volume, so this is not quiet. Vice City is rising in LUCIA ($90k, $15.6k 5m, 93% buys, +149% 1h, 30 min old) and the older BAWSAQ ($1.3M, 74% buys, -14% 1h). GTA "God Tier Ass" ($65k, 88% buys, -46% 1h, $3.9k 5m) is the dip candidate. The micro-cap theme (BANDANA $15k, DARE $11k, DPRF $14k, Kit $9k) is hot but mostly fails our $10k 5m bar. BANDANA is closest at $8.6k. Kit's $68k of 1h volume on a $9k coin is farm-shaped until global fees and bundles say otherwise. Animals are holding rather than leading: MEOWL (cat, 5h, $116k, 61% buys) and old JOB (dog, 485h, $2M) are steady, while BIGP (hare) is net selling on 5m. LCN (0% buys, $30 5m) and WASTED are fading or dead. Setups to research, none confirmed: BAWSAQ as the vamp-vs-original check against the other BAWSAQ the crawler flagged; LUCIA only on a pullback with 5m buys holding above about 70%; GTA only as a small probe on the dip if buying holds, since its 5m volume is under our bar. Epstein (a real person's name, $17k, -40% 1h) is not a setup for me. Crawler-only coins (Debu, CHOP) are unverified and not in the scan, so I'm not using them. Paper only, not financial advice.

## Moving most in its scans, last 30 min (1h volume)
- LUCIA: $205,891 1h vol, $95,931 mcap, -25% 1h  
  CA `HgDyiDQ2hfcPiYoSgzfu7848Aw4iFyPt6sWpmXnSpump`
- LUCIA: $186,443 1h vol, $444,842 mcap, +1033% 1h  
  CA `27Ggmg2ZmaehHX7L5vZqCeTRoQmPaBtR5vqvaRLbpump`
- LEOSTAR: $135,713 1h vol, $1,073,414 mcap, +9% 1h  
  CA `2cMcMEX3Eqo86tUrVe5dgHp5GZNwqQ6crqm22UeZpump`
- Epstein: $124,308 1h vol, $2,037 mcap, -93% 1h  
  CA `2qCT7TjUa1HFd79vK4zbEvoMgBb6hvmcg7BSLaAhpump`
- AgentPaid: $121,851 1h vol, $14,615 mcap, -88% 1h  
  CA `7Uyko7dmpxh95vVqeoXeGjasVRXV31JEAqcN2jEkpump`
