# Trencher live report

Updated 2026-11-04T22:46:53Z (paper trading, never real money)

- Equity: $74.23 (-25.8% vs $100 start)
- Closed trades: 22, 3 wins
- Fees paid: $14.78 (axiom $2.81, network $9.18, pool $2.66), plus $4.15 lost to slippage
- New trades: WATCH-ONLY (scans and decides, buys nothing)
- Brain: subscription, claude-haiku-5-5 for routine calls, claude-opus-5-5 for the daily review; 496 routine calls and 1 plan-limit hits in 48h
- Watch log: 120 coins being followed, 625 filed, 0 would-buys (6h follow, sampled every 2 min)

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
- 22:45Z: 6 coins, 6 with pairs, 2 passed the market filters, 2 researched

## Coins it looked at, and why it passed
- 22:46Z GHOST (MIGRATED, $235,507 mcap, $6,317 5m vol): PASS at conviction 3, PASS: target too close. The first resistance (the $306k peak) is only about 1.3x away, and 5m sells are running ahead of buys. Vamp field, no printed higher low. (V1, V6)  
  CA `42qKoGmEPTRJsa5jWrYwpydL8RkBwMvg2ykYVoerpump`
- 22:46Z SLOP (MIGRATED, $119,452 mcap, $31,267 5m vol): PASS at conviction 3, PASS: flow below pace (5m at 0.2x the hour, theme at 0.18x), drawdown 72% is past the 70% DIP max, and 13 same-ticker copies split the crowd. Blocker: "flow below pace". (V1, V6)  
  CA `6z3cf9nDuxdA9xyccx8m8SonWdZGH5s9kbqAeaV5gajt`
- 22:39Z GATO (MIGRATED, $10,279,524 mcap, $7,155 5m vol): REJECT, Dev holds 3.3% (>1%) (V13, V17)  
  CA `HsprHxBRgiVaQdRf3TnKNuZZtaX9JUSPgMFdAkk6pump`
- 22:31Z VI (DIP, $349,660 mcap, $5,781 5m vol): PASS at conviction 4, PASS — Vice Inu is a 69% dip with a real catalyst 15 days out, but the story is fading on the radar, the 5m is under $10k, the domain is under a day old, and the bottom-buy gate needs a rising narrative. Blocker: "narrative not rising" (V1, V13).  
  CA `FpWWSqLNrjTTMDM41EXkvBmHBDkNdWrf9RwHL57xpump`
- 22:29Z GDA (FINAL_STRETCH, $28,554 mcap, $36,621 5m vol): REJECT, Top 10 hold 25.7% ex-pool (>25%) (V13)  
  CA `F1FiJdqfUzEx8BtfdSCRwGwrKBAZHJs6JkNEfVYYpump`
- 22:28Z JOB (MIGRATED, $3,593,465 mcap, $5,518 5m vol): PASS at conviction 3, PASS: flow below pace, no printed higher low, and a bottom buy on a theme the radar doesn't name. It's a copy in an 8-coin vamp field. (V1, V6, V13)  
  CA `9Pq7aLAbhDG2tTnS22cm6kuysZVcZpLFE368HWuypump`
- 22:26Z nuLL (DIP, $134,710 mcap, $11,128 5m vol): REJECT, Dev holds 5.2% (>1%) (V13, V17)  
  CA `A72sK9mPWTvU4f5RQFy7upBCeJi9HZx3Q2Wgr7QBnuLL`
- 22:26Z MSFT (MIGRATED, $35,931 mcap, $12,335 5m vol): PASS at conviction 2, PASS: "Microsoft" (MSFT) is down 47% from a $68k peak in 11 minutes, with no printed higher low and no story on the radar. Too new, falling knife (V1, V6).  
  CA `CggrqcmnVyppSAgyaVMDPrESybPHhq9dZgVV788Vpump`
- 22:19Z RICO (DIP, $227,828 mcap, $2,388 5m vol): PASS, PASS — brain unavailable, not trading blind.  
  CA `8kuQg3WivDtL85VEdw2jEmSXjYt6EEeYBATJ4DtQpump`
- 22:17Z AMD (MIGRATED, $899,041 mcap, $5,344 5m vol): PASS at conviction 3, PASS — bottom buy on a theme running at 0.82x its hourly pace, no catalyst, no printed higher low, and it's one of 10 same-ticker copies. Blocker: "theme volume below pace." (V1, V6, V13)  
  CA `5tdWkbqhTqVyPmksqX8WVKrHbjjqmvQfrMGwZoZPpump`

## What its skips did next (last 48h)
A skip "ran" if the coin reached the first target (1.5x) from the skip price before a 20% drop, "dumped" if the drop came first. Sampled every 10 min, followed 6h.
- top 10 over 25%: blocked 68, ran 13, dumped 53, flat 1, open 1 (saving losses: keep it)
  - ran: KYBER up to 1.83x  
    CA `BasL6j1MNkjFyuvRRFsmbm3bKqFPr6Yg3UhShii6pump`
  - ran: WIF up to 1.67x  
    CA `E7ayy5Se6gjwCNtw9NP629AucnTgqab4SSmSxDpUpump`
  - ran: j*b up to 1.97x  
    CA `7uHBhrdN1UNf1vggnvoZMHVA6Du4NQe2USP2oMnYpump`
- too new / sniping: blocked 64, ran 9, dumped 54, flat 1, open 0 (saving losses: keep it)
  - ran: SNOWMEI up to 1.76x  
    CA `ETVD787UcTkJqrhZMt15bVet7CQ4SDzCga7DfBm8pump`
  - ran: GTAVI up to 2.31x  
    CA `HekahVohmeokPUhscg5taNme3Qs2fcSQoNgEeUPMpump`
  - ran: PEPTDOG up to 1.88x  
    CA `GExwMYa2tnJwGfKTmzR4ERiQKptfNceN9GTXc82Lpump`
- flow below pace: blocked 55, ran 10, dumped 37, flat 4, open 4 (saving losses: keep it)
  - ran: Wanted up to 1.53x  
    CA `8oUGdPdyxVaCSJSZpcVZuxqoyiZAmc2Z22FsDRZ3pump`
  - ran: METEORITE up to 1.58x  
    CA `67RBmGztx8ciVyWr8yi6R8fwrc3EG86XejYT7mespump`
  - ran: OMBRO up to 1.54x  
    CA `8DB8Fw5UiC1AzugQAfRyw3qL8omw772LJbdehNWhpump`
- near the high / chasing: blocked 39, ran 7, dumped 27, flat 3, open 2 (saving losses: keep it)
  - ran: underdog up to 1.64x  
    CA `BZXh2LcnNNyypxsdfVeFzXawqmoGoSShC5i4NEQQpump`
  - ran: LUCIA up to 1.83x  
    CA `Cbtnpg6SL9jvZxtZTYYFPtVQXkuuqSUxCU5aXeTkpump`
  - ran: AMD up to 2.02x  
    CA `3MfZ4URVxmB4mfPuy4AxUxpcC5U7aXe7TDA7XVoGpump`
- RugCheck danger: blocked 26, ran 5, dumped 18, flat 2, open 1 (saving losses: keep it)
  - ran: Wanted up to 1.53x  
    CA `8oUGdPdyxVaCSJSZpcVZuxqoyiZAmc2Z22FsDRZ3pump`
  - ran: RAM up to 1.63x  
    CA `72QNkZqiTBsq5dvn4DEwaC5qBPDkc7SZJ38xXy4jpump`
  - ran: $LIBCOIN up to 1.54x  
    CA `2UxjHoidyefQxJrCS8qT23JsbqKFcpPCa8ywBYZupump`
- falling knife (code): blocked 22, ran 3, dumped 19, flat 0, open 0 (saving losses: keep it)
  - ran: DESSA up to 1.54x  
    CA `npz2FhoufQ7pKqhGpaipYWacrAkidyW2yDpVWSvpump`
  - ran: RATIO up to 1.51x  
    CA `3JdeP1VBHgRPunmjTj1D6w6ZZePwGAwjUr2tCufwpump`
  - ran: ORBIE up to 1.83x  
    CA `HEb2dwDNbBhnrCusoNXXvba9MymYTTmMQcHKaptxmfun`
- bundles over the line: blocked 19, ran 1, dumped 15, flat 3, open 0 (saving losses: keep it)
  - ran: MAMESUKE up to 1.95x  
    CA `SCGBBnSwnekytGFHgyeHHxPMiN7xDxsWFGg9JgFSTNK`
- falling knife / no higher low: blocked 16, ran 3, dumped 9, flat 2, open 2 (saving losses: keep it)
  - ran: DESSA up to 1.54x  
    CA `npz2FhoufQ7pKqhGpaipYWacrAkidyW2yDpVWSvpump`
  - ran: HEDGE up to 1.77x  
    CA `wDSAqt4tEZpDAwB9XY6ejkZvMFuT1zUMjUh67txeYhf`
  - ran: MEOWNERO up to 1.76x  
    CA `6gnB2H2hbTVvKUWCzNuqjWY8Rod6EVBmfHi7YxZpTWa7`
- thin 5m volume: blocked 15, ran 4, dumped 9, flat 1, open 1 (saving losses: keep it)
  - ran: DESSA up to 1.54x  
    CA `npz2FhoufQ7pKqhGpaipYWacrAkidyW2yDpVWSvpump`
  - ran: 404 up to 1.89x  
    CA `9gKArqT6qp3goHfuwAnfG7LioqwUtJ8TFu7P1Bhbpump`
  - ran: MEOWNERO up to 1.76x  
    CA `6gnB2H2hbTVvKUWCzNuqjWY8Rod6EVBmfHi7YxZpTWa7`
- other: blocked 14, ran 4, dumped 8, flat 1, open 1 (saving losses: keep it)
  - ran: DESSA up to 1.54x  
    CA `npz2FhoufQ7pKqhGpaipYWacrAkidyW2yDpVWSvpump`
  - ran: FEAR up to 125.22x  
    CA `CHtXwJ3qa2ozS9vQkxhR3MmNwkoUqkh3icGXgZPepump`
  - ran: MACHKA up to 1.52x  
    CA `CG1DmSiMXw9WjQXCzP5JDnma5BDY3Cks9bRTdXNLpump`

## Daily review (2026-11-04, claude-opus-5-5)
No. After costs, every bucket loses money. Across 355 settled coins the simple plan (sell at 1.5x or -20%) averaged -10.1%, and before costs it was only about +0.4%. So the 10.5% round-trip cost on a $10 buy is the whole loss, and no group gets close to clearing it. The best group is MIGRATED at -8.1% net (about +2.3% before costs). With ~355 samples the all-coin result is clearly below zero, about -10% ± 3%. But the samples overlap: the same coin gets logged more than once, a few metas cluster, and it's all one market day. So the real uncertainty is wider, and a single day can't show any subgroup edge. The question about would-buys can't be answered: the routine model made zero BUY calls (would_buy n=0) and said PASS on all 181 coins it reviewed. Those passed coins ran more often than the checklist rejects (30.4% vs 16.1%) and lost less (-7.2% vs -13.1% net). That says the checklist filters somewhat, but nothing here is buyable.
- finding: Costs are the whole story. All coins (n=355): 23.4% ran, 59.2% dumped, median peak 1.25x, 18.0% hit 2x. Before costs about +0.4%; after the 10.5% cost, -10.1%. A typical coin that peaks at 1.25x can't pay a 10.5% round trip.
- finding: MIGRATED is the least bad setup (n=250): 24.8% ran, 53.6% dumped, -8.1% net (about +2.3% before costs). It's the only setup positive before costs, and the margin is small enough to be noise.
- finding: DIP is clearly the worst (n=51): only 11.8% ran (6 coins), 72.5% dumped, 5.9% hit 2x, -18.4% net and about -8% even before costs. Its run rate is roughly half of MIGRATED's 24.8% on 250. With this gap it's unlikely to be just noise, though it's still only one day of data. Dip-buying as currently defined catches falling knives.
- finding: FINAL_STRETCH (n=54) has the biggest upside and still loses: median peak 1.45x, 27.8% hit 2x, but 72.2% dumped and -11.5% net. Ran plus dumped is exactly 100% and 'ran' equals 'hit 2x' exactly (27.8%), which looks like an artifact, not a real pattern (see data issues).
- finding: The checklist separates a little. Rejects (n=174): 16.1% ran, -13.1% net, about -2.8% before costs. Coins it let through to the model (n=181, all declined): 30.4% ran, -7.2% net, about +3.4% before costs. Dump rates are about the same (57.5% vs 60.8%), so the checklist finds more runners but doesn't avoid dumps.
- idea to test: Cost gate: add the condition est_round_trip_cost_pct ≤ 5 and re-run every setup on the week's data. With costs at ~10.5%, a cost filter is the only lever big enough to matter. If the low-cost subset is still negative, the setups have no edge.
- idea to test: Drop or rebuild DIP: test setup=DIP only when drawdown_from_high is between 40% and 55%, 5m volume ≥ the 1h average pace (flow ratio ≥ 1.0), buy ratio ≥ 0.55, and the previous high was ≥ $150k mcap. If that subset doesn't beat -5% net on n≥40, turn DIP off.
- idea to test: MIGRATED focus: test setup=MIGRATED AND checklist passed AND mcap between $40k and $300k AND age between 0.5h and 6h AND 5m volume ≥ $10k AND buy ratio ≥ 0.55. Also split by mcap band to see whether the small positive before costs is concentrated anywhere.
- idea to test: FINAL_STRETCH exit variant: once the bonding-curve price switch is confirmed not to cause fake 2x hits, test selling half at 2x and trailing the rest (or a -30% stop), against the current all-out at 1.5x / -20%. 27.8% hit 2x, but the 1.5x target caps them while 72% eat the full stop.
- idea to test: Agreement signal: test whether coins where the checklist passed AND the model's conviction was ≥ 6 (even when it said PASS) beat the other checklist passes. To do this the model must log a conviction score on every PASS, not just a verdict.

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
Meta right now is cat coins plus Bitcoin/satoshi names, mostly launched in the last one to two hours. The cat cluster is Sasha "Bitcoin cat" ($126k cap, $61k 5m, 56% buys, +217% 1h), FED Fedora Cat, GG Golden Goose and GATO GTA6CAT, with the satoshi-name cluster (satoshi/Len Sassaman, Central Intelligence) riding alongside. Joke and event-hook launches like AMC "Another Meme Coin" ($28k cap, $55k 5m, 61% buys, +481% in six minutes) are the other fresh flow. Rising with buyers: Sasha, AMC, and GTA "Grab That Ass" ($2.65M cap, $14k 5m, 73% buys) as the bigger, cleaner-flow name. Fading: older $1M+ coins (JOB at 194h, VI at 21h, GATO at 1,713h) doing a few thousand 5m, Sisyphean Leopard down 80% in the hour, and MortgageCoin with zero buys in 5m. Setups to research, no entry: Sasha and AMC first, conviction about 4/10 until holder, dev and bundle checks come back; GTA only if its buyers hold. The crawler's ABTC, Ourcoin and tism figures don't match scan_movers, so I ignored them. $LAPTOP is out: it's tied to a political figure (Hunter Biden). Paper trading only, not financial advice.

## Moving most in its scans, last 30 min (1h volume)
- SLOP: $1,936,328 1h vol, $146,412 mcap, +279% 1h  
  CA `6z3cf9nDuxdA9xyccx8m8SonWdZGH5s9kbqAeaV5gajt`
- Democat: $780,206 1h vol, $548,624 mcap, +954% 1h  
  CA `9Y1F6dZ6HpjZDYZdYuUGwMbkUiPsyU7WPTqTQU4Tpump`
- PHIL: $127,842 1h vol, $12,573 mcap, +19% 1h  
  CA `6X6E4frRadiUEcVqUKTyUVS2FhGmwN359TocEaHXtBX5`
- JOB: $103,431 1h vol, $3,593,465 mcap, -18% 1h  
  CA `9Pq7aLAbhDG2tTnS22cm6kuysZVcZpLFE368HWuypump`
- PI: $102,592 1h vol, $6,179 mcap, -86% 1h  
  CA `G4bjr2e9BwqkPxfjUfpsk3B8ySvNYq4rBu2RrQMJpump`
