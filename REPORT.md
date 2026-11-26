# Trencher live report

Updated 2026-11-26T18:40:13Z (paper trading, never real money)

- Equity: $74.23 (-25.8% vs $100 start)
- Closed trades: 22, 3 wins
- Fees paid: $14.78 (axiom $2.81, network $9.18, pool $2.66), plus $4.15 lost to slippage
- New trades: WATCH-ONLY (scans and decides, buys nothing)
- Brain: subscription, claude-haiku-5-5 for routine calls, claude-opus-5-5 for the daily review; 396 routine calls and 0 plan-limit hits in 48h
- Watch log: 99 coins being followed, 3949 filed, 0 would-buys (6h follow, sampled every 2 min)

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
- 18:39Z: 3 coins, 3 with pairs, 0 passed the market filters, 0 researched

## Coins it looked at, and why it passed
- 18:38Z JIMMY (DIP, $751,938 mcap, $2,176 5m vol): REJECT, Dip with fading attention is a falling knife, not a dip (5m at 0.43x the hour's pace, under 0.6x)  
  CA `38M2z4UCfZEkUHFzD48vhKQhFhNyRGto8pZbLjNipump`
- 18:38Z WOOPY (MIGRATED, $191,554 mcap, $3,266 5m vol): PASS at conviction 2, PASS. Chasing a spike at the top of a dog meta that's fading, on $3k of 5m flow. Blocker: "chasing" (V1, V6).  
  CA `2va3NUJtEcPemDYg2N1RgA79rPKGTGGJKo3gTY5zpump`
- 18:36Z NORFEATH (MIGRATED, $260,730 mcap, $2,725 5m vol): PASS at conviction 2, PASS. Norfeather is a 75%-down bottom with 5m flow at 0.58x pace, $2.7k of 5m volume, a theme at 0.39x pace and 27 copies of the ticker. Nothing is printing. (DIP, V1, V6, V13)  
  CA `3gmFG4sFDJErDV8pacFrL2uUPXeGJTYLjfRy4hFypump`
- 18:34Z DIGS (MIGRATED, $250,519 mcap, $2,506 5m vol): REJECT, Bundles: 10 linked wallet cluster(s) hold 100.0% of supply (>20%) (V17)  
  CA `9QT8K685Hrae4k11dhGXirdtpfAaimExtyfwt8cPpump`
- 18:30Z JANTA (DIP, $153,003 mcap, $7,009 5m vol): REJECT, Dip with fading attention is a falling knife, not a dip (5m at 0.43x the hour's pace, under 0.6x)  
  CA `9tERTsZZj19ZHAqg7URtfkfPdaCiVeR4JkuPVoHrpump`
- 18:27Z KURO (MIGRATED, $101,406 mcap, $44,815 5m vol): PASS at conviction 2, PASS. Down 96.7% from a $3.07M peak in about 70 minutes, the theme at 0.4x pace, and 22 tickers on the same name. That's a collapse with a crowd leaving, not a dip (V1, V13).  
  CA `AaY6XtQZYYaxQ4fV8R8acConnMsgjg9zrZs341HUpump`
- 18:22Z PICKLES (FINAL_STRETCH, $25,794 mcap, $10,380 5m vol): PASS at conviction 2, PASS: chasing spike, +171% on 5m and +1080% on the hour, into 14 same-ticker copies. The story is a real animal's death, and I won't trade that. (V1, V6, V13)  
  CA `133CMybtis6bg987aB1TxZXekai1wYnwtUj1tfiApump`
- 18:21Z PEDALFIN (MIGRATED, $50,849 mcap, $107,914 5m vol): REJECT, Dev holds 5.3% (>1%) (V13, V17)  
  CA `CD3AHwDcZziU85JpxxMLW2xhXHJUgDyjUxJVjmUZpump`
- 18:15Z bolphante (MIGRATED, $56,911 mcap, $2,468 5m vol): REJECT, Dev holds 2.1% (>1%) (V13, V17)  
  CA `FVBzzG4ZcAgxSLW1rWjNC9EH9CgEgz1A4puNYexMpump`
- 18:11Z UHI (MIGRATED, $1,757,200 mcap, $9,616 5m vol): PASS at conviction 3, PASS: 8% off the $1.92M high, sellers 2:1 on the 5m, no printed higher low, and the site says "Contract TBA." Chasing a meme copied 20 times (V1, V3, V6, V13).  
  CA `Bnw5JRPek5JvJhzUiB9yrs2cmzt4bLeFqSRzDzSppump`

## What its skips did next (last 48h)
A skip "ran" if the coin reached the first target (1.5x) from the skip price before a 20% drop, "dumped" if the drop came first. Sampled every 10 min, followed 6h.
- top 10 over 25%: blocked 46, ran 9, dumped 36, flat 0, open 1 (saving losses: keep it)
  - ran: MARS up to 2.06x  
    CA `816BuXnCFQqt6KXbBTcFgHWD29Ckpaqt8HMKSN4Vpump`
  - ran: 4CHAN up to 1.87x  
    CA `DVdWuNK8ncn79B6z8nCiwcNAiwyFcmBPfChgxJGTpump`
  - ran: SWARM up to 1.57x  
    CA `2Rw6rLRRZXQLNreForjeVvDjnpYUaW6rmMFXmRP9pump`
- flow below pace: blocked 40, ran 4, dumped 28, flat 4, open 4 (saving losses: keep it)
  - ran: BOOBS up to 1.51x  
    CA `E35iEA2yLLHc1tjm6et1Z3YuH8DhxJYWtWezPHgSpump`
  - ran: BASKET up to 1.55x  
    CA `3Tg6YnNrfPdFfsY14MaNsDMWLseAyrUDS3myJtbaJN6f`
  - ran: BIAO up to 1.51x  
    CA `As3XtYSstuVdrVyb6sJZZ77Tu8JvjTBg6S6hgPv4pump`
- near the high / chasing: blocked 36, ran 5, dumped 26, flat 2, open 3 (saving losses: keep it)
  - ran: SNOWCUMBRR up to 2.36x  
    CA `Gf9wm93TTDpbPC467Eio5Vc42Kr6MAomUD172drWpump`
  - ran: HEYOS up to 1.91x  
    CA `A88p1LcHisrx3TuTwUGVrLtc1LBTUPZUfVgaCGutAFaK`
  - ran: Nala up to 1.64x  
    CA `FeBG8AEG4j7LT7xQF38gPXQFBRBtXBTNzhZjSa3bpump`
- too new / sniping: blocked 34, ran 8, dumped 26, flat 0, open 0 (saving losses: keep it)
  - ran: BABYANSEM up to 2.77x  
    CA `F3VctV9FqDgiyqaztN6z78bgWy27eH7DBBHW1vjpump`
  - ran: Merged up to 2.18x  
    CA `AMYpNGi5aGrKr1ZDsotUdWh7k1mMi569ygtaHJmErGEd`
  - ran: Boor up to 1.56x  
    CA `GHFpSSw2ZMjmKCyc1wrHUjJiqnJeP18mekY9GL1Xpump`
- RugCheck danger: blocked 27, ran 3, dumped 23, flat 1, open 0 (saving losses: keep it)
  - ran: TROLL up to 1.94x  
    CA `7ykeHoEnjnGkY6tqteXn47fdGtd7kfXWghiyZ7YKpump`
  - ran: Snowball up to 3.52x  
    CA `9TKbd3VFaMSXsEAicD9JVQWpWwAoLi4fSgWmZL2cpump`
  - ran: Bababoi up to 2.17x  
    CA `28B9kDm6XtQNqAkzuiKH3Zu1L8cVM6SLW4iRamFspump`
- brain paced: blocked 20, ran 5, dumped 15, flat 0, open 0 (saving losses: keep it)
  - ran: SANTIA up to 1.76x  
    CA `2YKce3apGESoWhqt4N7MGg5t4UEKgPPL4ArheEvPpump`
  - ran: Slingoor up to 1.73x  
    CA `6GLetugFEmy7P7SmLtg3zyZdz6rWCQ8gHPbPYZs9pump`
  - ran: FREEDOM up to 4.48x  
    CA `FDNc812jkHdhkdeRNaLMVwyihHMLR6ztTmRfxG7opump`
- falling knife (code): blocked 19, ran 3, dumped 12, flat 1, open 3 (saving losses: keep it)
  - ran: Jimmies up to 1.53x  
    CA `GisWWjhwrSud4aFGSHvTMt85Ky14sY7LeBFCpfoFpump`
  - ran: Investor up to 1.58x  
    CA `J9eBkCb4UtquAMQqB6duwBmR99fFSMoTnDcaMB9Wpump`
  - ran: MONEY up to 1.58x  
    CA `DeACAbp2GMzapB6Z2K8qdkTZupmNbKc6EZx9bnbCpump`
- bundles over the line: blocked 18, ran 3, dumped 12, flat 2, open 1 (saving losses: keep it)
  - ran: jingyu up to 1.58x  
    CA `DUZrwdjEthcJ99ZiRXr31UuqTohoTg7VjTEyfGdBpump`
  - ran: DUMBMONEY up to 1.74x  
    CA `GEHehS5Rr4rNCjvrHLjjV1avD4bjMsn53ywDGv1spump`
  - ran: WIENER up to 1.59x  
    CA `8BDkDfj3ZUvcG9caGzF2XnHfwg7K6fjfKKDvX6SCpump`
- dev share over 1%: blocked 12, ran 2, dumped 8, flat 2, open 0 (saving losses: keep it)
  - ran: Grinch up to 1.94x  
    CA `J1b5HnRzmXsYK5akPTFtBR7B4E74JG8eyULodd7ypump`
  - ran: bolphante up to 1.7x  
    CA `FVBzzG4ZcAgxSLW1rWjNC9EH9CgEgz1A4puNYexMpump`
- falling knife / no higher low: blocked 12, ran 3, dumped 5, flat 3, open 1 (mixed)
  - ran: Jimmies up to 1.53x  
    CA `GisWWjhwrSud4aFGSHvTMt85Ky14sY7LeBFCpfoFpump`
  - ran: Zero up to 2.07x  
    CA `DTSkmo3sCCKLCh91dJLiWCpwcKtK3yDBZMqZGSV1pump`
  - ran: Maru up to 1.88x  
    CA `FokVFH6mDsazoKbtnUaA2FRMsRbDSwZhNfn17Fdvpump`

## Daily review (2026-11-26, claude-opus-5-5)
No edge yet. All 276 settled coins lost money after costs under the simple plan: -6.4% average net. Every setup was negative: FINAL_STRETCH -3.6% (n=45), MIGRATED -5.1% (n=193), DIP -16.1% (n=38). Before costs the simple plan made roughly +3% overall and about +6% on FINAL_STRETCH. The ~9.7% round-trip cost on a $10 buy wipes that out, which is the same thing the 22 real trades showed: $18.83 of the $25.79 loss was fees and slippage. The sample is far too small to trust a 3–6% gross edge. Payoffs swing from +50% to -20%, so the error bar on 45 FINAL_STRETCH coins is about ±9 points. Repeat logs of the same coin also make the overall n look bigger than it is. Only the negative after-cost result is solid. The brain logged zero would-buys, so nobody can say yet whether it picks better than it passes. That missing data is the main thing to fix before Nov 10.
- finding: Costs decide the result. Average round-trip cost is 9.7% of a $10 buy (FINAL_STRETCH 10.0, MIGRATED 9.6, DIP 9.6). Before costs: all coins about +3.3%, FINAL_STRETCH about +6.4%, MIGRATED about +4.5%, DIP about -6.5%. After costs every group is negative. At this size, fees are a bigger problem than coin picking.
- finding: DIP is clearly the worst setup: n=38, 10.5% ran, 2.6% hit 2x, median peak 1.10x, net -16.1%, and still negative before costs. The other setups ran 29–38% of the time. Four runners out of 38 is a small number, but the gap is large and DIP is the one setup that looks broken on this sample.
- finding: FINAL_STRETCH did best: n=45, 37.8% ran, 26.7% hit 2x, median peak 1.37x, net -3.6%. It still loses after costs, and with n=45 the gross number can't be told apart from zero.
- finding: MIGRATED is most of the sample: n=193, 29.5% ran, 20.7% hit 2x, net -5.1%. That is close to the overall average, so nothing stands out yet.
- finding: The checklist and the brain don't separate winners from losers on this metric. Checklist-failed coins (n=138): 28.3% ran, 22.5% hit 2x, net -6.2%. Coins that cleared the checklist and reached the brain (n=138): 28.3% ran, 15.9% hit 2x, net -6.5%, and they dumped more often (60.1% vs 52.2%). The rejected coins did no worse. Hard lines still stay where they are, because the -20% simulated stop probably hides the rug losses they exist to avoid (see data_issues).
- idea to test: Turn DIP off: setup == DIP → no entry. Alternatively allow it only if 5m volume ≥ 1h average pace and buy ratio ≥ 0.55. Test whether the filtered DIP subset gets above zero before costs. If it doesn't, drop DIP for good.
- idea to test: Cost gate: enter only if estimated round-trip cost_pct ≤ 5%. Re-run the simple plan by cost bucket (<5%, 5–10%, >10%) and at larger notional sizes ($25 and $50 against pool liquidity). This shows whether the gross edge survives once fixed fees are a smaller share.
- idea to test: FINAL_STRETCH with mcap < $25k and 5m volume ≥ $10k against FINAL_STRETCH with mcap ≥ $25k. Report n, the share that hit 2x, and net after costs. Pnut and Fug are what prompted this split, not proof of it.
- idea to test: MIGRATED, V6 recon band: mcap $70k–$11M, age ≤ 12h, 5m volume ≥ $10k, flow ratio (5m volume ÷ (1h volume / 12)) ≥ 1.0, buy ratio ≥ 0.5. Compare against the rest of MIGRATED.
- idea to test: Exit-plan test on the same entries, order-aware: (a) sell all at 1.5x or -20%; (b) sell initials at 2x, trail the rest by 30% off the high, hard stop -30%; (c) break-even stop after 1.3x. Only worth doing if the logs keep the full sample path.

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
The meta is fresh pump.fun launches under 3h old with real buying: PEDALFIN ($51k cap, $87k 5m, 53% buys), Criminul ($45k cap, $32k 5m, 57% buys) and PICKLES ($26k cap, $10k 5m, 57% buys, +1080% in 1h) are rising, while the dog/animal jokes are fading (KURO -97% in 1h, Kuro -81%) and the stock-parody cluster is dead (MSTR -99%, $1.4k cap, no 5m flow). JANTA ($145k cap, 78% buys, $8.5k 5m, +60%) is the only Santa-named mover, so a holiday theme may be starting early, but it is one coin, not a confirmed meta. Setups to research, not buy: PEDALFIN and Criminul clear the $10k 5m bar but are about 6 minutes old, so bundle and chart-start checks decide everything before any entry (V3, V13); JANTA only if 5m holds above $10k with buyers still in. Not setups: bolphante's $3.6k 5m is under the $10k floor (V1, V6), and the crawler's XSEmu, PVE, SCENARIO, TRUMP and MEMESTOCK/DUO/X figures do not appear in the raw scan, so I'm treating them as unverified; the Trump-dinner and Ansem headlines are news, not flow, and nothing on the list is hack-named.

## Moving most in its scans, last 30 min (1h volume)
- KURO: $438,506 1h vol, $92,233 mcap, -97% 1h  
  CA `AaY6XtQZYYaxQ4fV8R8acConnMsgjg9zrZs341HUpump`
- JANTA: $196,440 1h vol, $144,830 mcap, +60% 1h  
  CA `9tERTsZZj19ZHAqg7URtfkfPdaCiVeR4JkuPVoHrpump`
- PEDALFIN: $146,938 1h vol, $50,849 mcap, +74% 1h  
  CA `CD3AHwDcZziU85JpxxMLW2xhXHJUgDyjUxJVjmUZpump`
- bolphante: $113,828 1h vol, $51,682 mcap, +39% 1h  
  CA `FVBzzG4ZcAgxSLW1rWjNC9EH9CgEgz1A4puNYexMpump`
- JAZZ: $101,829 1h vol, $20,001 mcap, -34% 1h  
  CA `CErq2oGNSJWVovVMjx8k1wuL6qR75q1teSxJNqrCpump`
