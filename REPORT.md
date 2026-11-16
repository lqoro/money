# Trencher live report

Updated 2026-11-16T03:03:57Z (paper trading, never real money)

- Equity: $74.23 (-25.8% vs $100 start)
- Closed trades: 22, 3 wins
- Fees paid: $14.78 (axiom $2.81, network $9.18, pool $2.66), plus $4.15 lost to slippage
- New trades: WATCH-ONLY (scans and decides, buys nothing)
- Brain: subscription, claude-haiku-5-5 for routine calls, claude-opus-5-5 for the daily review; 219 routine calls and 0 plan-limit hits in 48h
- Watch log: 128 coins being followed, 1547 filed, 0 would-buys (6h follow, sampled every 2 min)

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
- 03:03Z: 8 coins, 8 with pairs, 0 passed the market filters, 0 researched

## Coins it looked at, and why it passed
- 02:52Z FiveM (MIGRATED, $353,617 mcap, $6,016 5m vol): PASS at conviction 3, PASS: flow below pace and no higher low. A 23-copy GTA field with a 0.88x theme pace and no catalyst is not a bottom buy. (V1, V6)  
  CA `2YxbK7V6ZTKSxcavk3V4kFzdtZ4uywhhoyuSxapjpump`
- 02:52Z Neil (MIGRATED, $201,345 mcap, $11,805 5m vol): PASS at conviction 3, PASS. Not the lemur leader: the Cxf4 CA is doing $54k on 5m to this one's $11.8k, and this coin's flow is 0.45x its own hourly pace. The 15m closes are a saw-tooth with no printed higher low. Top 10 at 20.2% and a 5.4% bundle cluster add to it (V3, V6, V13).  
  CA `9iG6qBMgzzuYyq2kfXcAD49bkTFrpGp5gr1QHJiZMwoi`
- 02:50Z WISHMAS (DIP, $167,857 mcap, $2,104 5m vol): PASS at conviction 3, PASS: no higher low, flow only 1.34x pace on $2.1k 5m, and the story is fading. Blockers: "no higher low", "no catalyst", "dead story" (V1, V6).  
  CA `9cmXfuC26anZtH9AUWVzpUxU1UJ7PPogYxftYTepump`
- 02:49Z XRL (DIP, $59,369 mcap, $2,543 5m vol): REJECT, Dip with fading attention is a falling knife, not a dip (5m at 0.24x the hour's pace, under 0.6x)  
  CA `Fww6zaNKcjpJaB33JayvUzsofBUobX5JaHiuQBN1Jf9g`
- 02:47Z POKE (FINAL_STRETCH, $21,950 mcap, $5,097 5m vol): PASS at conviction 3, PASS: POKE is one of 13 copies of the ticker and not the leader, its 5m volume is $5.1k (under the $10k bar), and it sits 8% off a +966% hour with no catalyst. Blocker: split crowd. (V1, V6, V13)  
  CA `6ZadZuzJ752xcUyWKnniwDyajYVJiKRhT4iyeUCvpump`
- 02:44Z BAWSAQ (DIP, $577,553 mcap, $3,499 5m vol): PASS at conviction 3, PASS: not the Vice City leader, no catalyst, and the GTA-name story is fading. The bottom-buy rule blocks it. Wait for VICE to set the pace. (V1, V13)  
  CA `DTJbHA1ntTzsp6FXKRhwwD4E3CLcd5trkWhSV8ivpump`
- 02:40Z PSYOP (FINAL_STRETCH, $26,491 mcap, $2,468 5m vol): REJECT, Top 10 hold 27.9% ex-pool (>25%) (V13)  
  CA `AaBt5bHNvrM5aLR8gfDEHwBTtTHZiPbre251UVGwpump`
- 02:39Z Anthropig (MIGRATED, $1,043,755 mcap, $4,943 5m vol): PASS at conviction 3, PASS: Anthropig is 17% off a $1.26M peak with 5m flow at $4.9k, under the $10k bar, and it isn't pushing into the high. Blocker "no breakout." It's a parody coin in a 19-copy field. (V1, V6, V13)  
  CA `2NUaS6Gfrm5rBuPBn7svHka8t33SrSkpXGQiUvZLpump`
- 02:37Z NEON (MIGRATED, $62,050 mcap, $1,097 5m vol): REJECT, 5m volume $1,097 is dead (<$2,000) (V1)  
  CA `A5xsAQhwGeKsNTKPiyB3jYydffWxPyzyWVodSA4hpump`
- 02:27Z Nеil (MIGRATED, $150,297 mcap, $54,412 5m vol): REJECT, Bundles: 7 linked wallet cluster(s) hold 95.2% of supply (>20%) (V17)  
  CA `Cxf4sN6MT7o3rMgS86JwFEnh6Fiisk5GDzxWHr4Ppump`

## What its skips did next (last 48h)
A skip "ran" if the coin reached the first target (1.5x) from the skip price before a 20% drop, "dumped" if the drop came first. Sampled every 10 min, followed 6h.
- flow below pace: blocked 32, ran 3, dumped 24, flat 3, open 2 (saving losses: keep it)
  - ran: PASSED up to 1.73x  
    CA `3XaH8VPUaUegqmnkYA8PXCWqQqD8doqdsGGfZyoYpump`
  - ran: ANT up to 1.52x  
    CA `BDPm9gPHCRyo2qjcRrYPsXexmbRwuuHQZo2qhhYXpump`
  - ran: ANT up to 1.58x  
    CA `7H2sHeLHyHR8jxENGmsqn7RxTkYZa4KwXvKYcoxBpump`
- top 10 over 25%: blocked 29, ran 6, dumped 17, flat 3, open 3 (saving losses: keep it)
  - ran: rockstar up to 1.95x  
    CA `9HFUEab7sompLDPTAaTGkryMNGbtBaFMhHMVpJEBpump`
  - ran: VI up to 1.71x  
    CA `4Dj8m9vWqu779F1KDBUttvXM8YFm7U92SDpvjBNKtEiB`
  - ran: ANT up to 1.52x  
    CA `BDPm9gPHCRyo2qjcRrYPsXexmbRwuuHQZo2qhhYXpump`
- too new / sniping: blocked 25, ran 5, dumped 20, flat 0, open 0 (saving losses: keep it)
  - ran: Chick up to 1.66x  
    CA `Dueav76X9spnoLomhM2jMkkWorVggbeWucLs3YLupump`
  - ran: TOOLS up to 1.83x  
    CA `9Ei1d97U7M8m4t3fof7c8MUECtmzgqbQCo81cGGzpump`
  - ran: twert up to 1.81x  
    CA `8WvWwttzaLfW1nbjx6wmYL5jozWpvy95WktAg5cipump`
- RugCheck danger: blocked 23, ran 7, dumped 14, flat 2, open 0 (saving losses: keep it)
  - ran: Ivy up to 1.88x  
    CA `DxNF3Qxd8XeUBdz7ReRdoiFzRmNDKbSz4c2oA7aRpump`
  - ran: SI up to 1.93x  
    CA `AiQUqe4zjiDssth2FsCoeQVaGtCtHYyKGX8U52rWpump`
  - ran: FUTA up to 2.77x  
    CA `FxoXV4C8DTSYeg5dSXrEsr45zzr8tpNbsrpoiZ8Kpump`
- near the high / chasing: blocked 19, ran 3, dumped 15, flat 0, open 1 (saving losses: keep it)
  - ran: penny up to 1.6x  
    CA `5gmCPpuktJ7Svjgr4PPJBTosAFKB8K6Z45EGfSUmpump`
  - ran: WIGGLES up to 1.69x  
    CA `2kWx47CUrcXtzptFNnbSXKq3vo1ebqyLBhRytKRGpump`
  - ran: Bustas up to 1.75x  
    CA `9rTgs58B3p11vXekTTgVYtv8vKxQ6oSoZFXPy4onpump`
- falling knife (code): blocked 11, ran 2, dumped 9, flat 0, open 0 (saving losses: keep it)
  - ran: BigP up to 1.57x  
    CA `CY254o6VPaJnTiY5uuKUB8xDjSgykC6xtoLoC3kpump`
  - ran: SAME up to 1.89x  
    CA `5qRxJ9W45zUrUtGGDneysiRBKZaceNriEqVUei1Rpump`
- falling knife / no higher low: blocked 11, ran 3, dumped 4, flat 3, open 1 (mixed)
  - ran: CateGiving up to 1.57x  
    CA `5XasjCnMPTczL9VZTDHgbK5sQzwkjnu41oLeHf5Wpump`
  - ran: Nyajira up to 1.52x  
    CA `8cWGfiHyKqxgLrLtkPt2NnLkSUV2JbcLBf4RN6Fapump`
  - ran: GOAT up to 1.61x  
    CA `D7iafdwzzpB7tisqQqT5T9aRrYPtHLqzwxhnLoWJgoat`
- other: blocked 10, ran 2, dumped 6, flat 0, open 2 (saving losses: keep it)
  - ran: TaoTao up to 1.53x  
    CA `G1KuEMuLrxWynFddQVnpdkQAhYFBwNJiuz1Lv7d9pump`
  - ran: SI up to 1.94x  
    CA `H2irVtPLfKoBJ69itZmhsedSPwBUTaubmUavc6Uapump`
- thin 5m volume: blocked 9, ran 2, dumped 5, flat 1, open 1 (saving losses: keep it)
  - ran: SENDER up to 1.58x  
    CA `5peJLZQnBkXtydYYMunbT4QutSyd9eA474MqxcmEpump`
  - ran: UNITY up to 1.66x  
    CA `GD6MboptxbHBspASr5PWozgNDrZxmxJ8JpBBD8Vpump`
- crowd leaving / fading volume: blocked 7, ran 1, dumped 6, flat 0, open 0 (saving losses: keep it)
  - ran: NUREMBERG up to 1.62x  
    CA `7R3RnGmpV9mZXwSyHyKN5LEddiZRmGsYrAZPgDJqpump`

## Daily review (2026-11-15, claude-opus-5-5)
Nothing shows a positive after-cost edge. Across all 93 settled coins the simple plan nets -5.5%: about +4.3% before costs, wiped out by an estimated 9.8% round-trip cost on a $10 buy. With a 1.5x target, a -20% stop and 10% cost, a setup needs about 43% of coins to run just to break even. FINAL_STRETCH (n=20) sits at 45% and nets +1.5%, but its 95% range on that share is roughly 23-67%, and one winner turning into a loser moves the average by about 3 points. That result is probably optimistic anyway: the simulator appears to fill every stop at exactly -20%, while several coins in the logs went to about zero. The routine model logged zero would-buys in 24h (39 brain calls, all PASS), so there is nothing to compare against what it passed on. Its PASSed coins did better than the checklist failures (-3.3% vs -7.1% net), but both groups lose money. Honest answer: no edge yet, and one day of correlated samples can't show one.
- finding: Costs are the whole story. All coins: n=93, 30.1% ran, 52.7% dumped, -5.5% net, 9.8% average cost, so about +4.3% before costs. The real trades say the same thing: $18.83 of the $25.79 lost over 22 trades was fees and slippage.
- finding: Breakeven math for the simple plan at about 10% cost and no flats: win share p must satisfy p*50 - (1-p)*20 = 10, so p = 42.9%. Only FINAL_STRETCH (45%) clears it. MIGRATED (28.3%) and DIP (15.4%) are nowhere close.
- finding: MIGRATED is the biggest bucket and among the worst: n=60, 28.3% ran, 60.0% dumped, -7.5% net. 23.3% of them hit 2x at some point, but the -20% stop usually triggers before the run.
- finding: DIP mostly does nothing: n=13, 15.4% ran, 15.4% dumped, so about 69% flat. Net is -7.4%, roughly the cost. Over a 6h window the dips neither recover nor die; they just pay fees.
- finding: FINAL_STRETCH: n=20, 45% ran, 55% dumped, 0% flat, +1.5% net, median peak 1.94x. The +1.5% is less than one winner's worth (one winner is about +40 net, or 2 points of the average). Four of the five top runners are FINAL_STRETCH entries, including a pump.fun token named USDC (13.6x) and Chick, entered 2 minutes after launch. If the USDC entry was one of the 1.5x winners and is removed as an impersonator, FINAL_STRETCH drops to about -0.5%.
- idea to test: Before any rule comparison, rerun the simulation with stops that can gap: fill at the first sampled price below -20%, plus extra sell slippage on a falling pool. Every rule idea below should be scored that way.
- idea to test: FINAL_STRETCH timing: setup == FINAL_STRETCH and age_hours >= 0.25 and 15k <= mcap <= 35k and 5m volume >= $10k. Report the share that ran, net %, and net with the single best coin removed. Compare against FINAL_STRETCH with age_hours < 0.25 (snipes, which SOUL already rules out).
- idea to test: FINAL_STRETCH exit variant: same entries, target 2x (or sell half at 2x and trail the rest), -20% stop, with the order of target vs stop resolved from the price samples. Reason: hit-2x share = ran share = 45% in this sample.
- idea to test: MIGRATED filter: setup == MIGRATED and 5m volume >= $10k and buy ratio >= 0.55 and flow ratio >= 1.0 and drawdown from high <= 30%. Keep MIGRATED only if some subset clears 43% ran after costs on the full week; otherwise stop trading MIGRATED.
- idea to test: DIP rework: setup == DIP and 40% <= drawdown <= 70% and 5m volume >= 0.5x the hourly pace and buy ratio >= 0.55, with a time stop of 60-90 minutes instead of 6h, since most DIPs were flat and simply paid fees. If no version clears costs, drop DIP.

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
The trenches are trading animal-and-character name plays right now, led by the Neil the Lemur tokens: CA Cxf4sN6MT7o3rMgS86JwFEnh6Fiisk5GDzxWHr4Ppump ($99.6k cap, $61.6k 5m, 66% buys, +230% 1h, 12 min old) and CA 9iG6qBMgzzuYyq2kfXcAD49bkTFrpGp5gr1QHJiZMwoi ($115k cap, $16.3k 5m, 58% buys, +312% 1h), while the older-looking Neil at $66k is already -57% on $3.3k 5m and is the one to avoid. AI-lab name plays are a second theme (Anthropic Inu at 88% buys, Anthropig at $1.1M with 71% buys), but their 5m volume is thin and nema is -35% on 36% buys, which contradicts the crawler's +38% claim, so I'm trusting the scan. GTA-name coins have real volume but are flat or fading (GRAND THEFT CRYPTO $398k with $5.5k 5m, GTAVI -56%), and crude joke coins are dying (ELONBUTT -87%, Butthole $641 5m). The crawler's "no coin clears $10k 5m" is wrong: both Neil CAs and Say No to Crack ($13k 5m, but $21.7k cap and -50% 1h, so it fails the migrated mcap floor) show it, so this is not a quiet tape. Setup to research now: the $99.6k Neil lemur CA as a MIGRATED-lane probe at conviction 5, pending holder, dev and bundle checks, and first sort out which Neil is the original versus the vamp; initials at 2x, stop at -30%, out if 5m volume falls below half its hourly pace. Not a buy until those checks come back clean."

## Moving most in its scans, last 30 min (1h volume)
- Neil: $318,037 1h vol, $201,345 mcap, +81% 1h  
  CA `9iG6qBMgzzuYyq2kfXcAD49bkTFrpGp5gr1QHJiZMwoi`
- Nеil: $125,917 1h vol, $37,885 mcap, -47% 1h  
  CA `FwVsiYsWBDCs4QifGcDRGGxQ3xh6CYLnWWFLUDiupump`
- XRL: $124,880 1h vol, $62,446 mcap, +113% 1h  
  CA `Fww6zaNKcjpJaB33JayvUzsofBUobX5JaHiuQBN1Jf9g`
- MMM: $102,288 1h vol, $12,188 mcap, -55% 1h  
  CA `HnwmCecgrfkEeFCVKtnRs195Mq5ydnaQcM7ZxqzV14yE`
- FiveM: $76,354 1h vol, $360,696 mcap, -4% 1h  
  CA `2YxbK7V6ZTKSxcavk3V4kFzdtZ4uywhhoyuSxapjpump`
