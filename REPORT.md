# Trencher live report

Updated 2026-11-28T11:03:07Z (paper trading, never real money)

- Equity: $74.23 (-25.8% vs $100 start)
- Closed trades: 22, 3 wins
- Fees paid: $14.78 (axiom $2.81, network $9.18, pool $2.66), plus $4.15 lost to slippage
- New trades: WATCH-ONLY (scans and decides, buys nothing)
- Brain: subscription, claude-haiku-5-5 for routine calls, claude-opus-5-5 for the daily review; 375 routine calls and 9 plan-limit hits in 48h
- Watch log: 70 coins being followed, 4444 filed, 0 would-buys (6h follow, sampled every 2 min)

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
- 11:02Z: 5 coins, 5 with pairs, 1 passed the market filters, 1 researched

## Coins it looked at, and why it passed
- 11:02Z Mojave (MIGRATED, $35,058 mcap, $2,077 5m vol): PASS at conviction 2, PASS: flow at 0.18x pace on a coin 54 min off its bond spike, and the theme is at 0.81x. Blocker "flow below pace," with "too new" right behind it (V1, V6).  
  CA `4newt1R5fGEoCKdf9XBgiR6B43iacmnVAR2d4Wt8pump`
- 10:46Z Snowball (MIGRATED, $213,954 mcap, $3,455 5m vol): REJECT, RugCheck danger: Creator history of rugged tokens  
  CA `9TKbd3VFaMSXsEAicD9JVQWpWwAoLi4fSgWmZL2cpump`
- 10:43Z COMM (DIP, $36,365 mcap, $2,332 5m vol): PASS at conviction 2, PASS, dead story: COMM is a 2-hour-old commodity-themed copy with $2.3k 5m flow, a saw-tooth chart and a theme at 0.1x its hourly pace. Blocker: "dead story" (V1, V6, V13).  
  CA `8i2ssMZBaS3HShu5hoDEV4tVLf5RGXeNJnK3LNTHTH9e`
- 10:34Z cheng (FINAL_STRETCH, $15,830 mcap, $2,793 5m vol): PASS at conviction 3, PASS - $2.8k 5m flow on a 5-copy ticker with no story behind it, and the theme is at 0.05x its pace. Blocker: flow below pace / no narrative. Fresh and thin (V1, V6, V13).  
  CA `5zhdK5tA8Fz4L74YgYeSAVjjZ2NGTfSmWNYAiWN2pump`
- 10:33Z SPSC (DIP, $153,968 mcap, $2,148 5m vol): PASS at conviction 3, PASS: SPSC is a DIP with no catalyst, 5m flow at 0.66x pace, and 16 copies of the same joke ticker. Blocked by the bottom-buy owner rule (V1, V13).  
  CA `EjdrRG2si1FQ3Bme5g6WSYNHJDrsKUrbGB4Z5xaopump`
- 10:30Z hacked (no setup, $45,175 mcap, $266 5m vol): REJECT, Hack story ("hack" in the name or ticker): these tend to go down, owner rule  
  CA `FK7bc3fR8UL8uogN2u8J9yEpEbQJKR7yKsp3G8rvpump`
- 10:24Z JOB (MIGRATED, $3,049,752 mcap, $2,565 5m vol): REJECT, Bundles: 1 linked wallet cluster(s) hold 22.5% of supply (>20%) (V17)  
  CA `9Pq7aLAbhDG2tTnS22cm6kuysZVcZpLFE368HWuypump`
- 10:18Z Fireball (DIP, $512,057 mcap, $3,968 5m vol): PASS at conviction 3, PASS. Fireball is a 57%-off DIP with no story behind it. The ticker is shared by 27 copies, the site is 0.9 days old and doesn't show this CA, and the flow is under $10k. Blocker: no catalyst, narrative not rising. (V1, V6, V13)  
  CA `B9wbjDJ4FbHMsZmoXAkJSTAwuePaJUKbySvnK5zApump`
- 10:18Z BITCOINU (DIP, $1,259,106 mcap, $4,987 5m vol): PASS at conviction 3, PASS: bottom-buy gate failed. Theme is at 0.89x its hourly pace, no catalyst, and 5m flow is only $4,987 on a 17-copy ticker. The original may be real, but nothing is pulling the crowd back in (V1, V6, V13).  
  CA `ATbAsdCwrhhVg23DRnWpjqx6kx7ivoK5o8ysNmu1pump`
- 10:16Z Mojave (MIGRATED, $35,953 mcap, $30,715 5m vol): PASS at conviction 3, PASS. Blocker: chasing spike. 5m flow is 6.7x hourly pace, no printed higher low, and it's a 23-copy Mojave field with no project X behind it. Farm risk. (V1, V3, V6)  
  CA `4newt1R5fGEoCKdf9XBgiR6B43iacmnVAR2d4Wt8pump`

## What its skips did next (last 48h)
A skip "ran" if the coin reached the first target (1.5x) from the skip price before a 20% drop, "dumped" if the drop came first. Sampled every 10 min, followed 6h.
- top 10 over 25%: blocked 52, ran 11, dumped 37, flat 3, open 1 (saving losses: keep it)
  - ran: Legatum up to 2.21x  
    CA `HkPSDYRcw4uqgRzZMDd5sRnMpE4ungR1K8MRNXnBVtQ2`
  - ran: Thankful up to 2.05x  
    CA `E9arxG4RxB7Gxt6U75obonTZzx7vpbc4bUi1dfw3BtUN`
  - ran: MSTR up to 1.69x  
    CA `57sCZ82FwS5Dfs7FN9nshtU5Mkb3w1dqhmPUuCPvpump`
- flow below pace: blocked 42, ran 4, dumped 29, flat 5, open 4 (saving losses: keep it)
  - ran: PAIR up to 2.1x  
    CA `32rBxcFjCFnyqZ41CEPM5AL67X1dcw8w83vZt6Kxpump`
  - ran: Hoppy up to 1.76x  
    CA `CFX1gH7CKYwqYXrfDkS2MUxJcEhs8PT63DyRA1chpump`
  - ran: SpaceXCoin up to 1.52x  
    CA `G2XqmSc8vJpLLwaLVXUeNkxsrhVT8vQ3Pje8MqeDpump`
- near the high / chasing: blocked 36, ran 7, dumped 27, flat 2, open 0 (saving losses: keep it)
  - ran: urcoin up to 1.71x  
    CA `25m4Lkct8nsYyqAMeE8rvjM3y5Zrrax46TLqNJjbpump`
  - ran: Meme up to 2.06x  
    CA `CV1NPi8L2PSYMfALBh7GCfUwELZzG3DrLUUjCkeapump`
  - ran: IceBall up to 1.67x  
    CA `6PFm828RKNJqKvjXQz82hhGvGNWFXZcBHNCF4U7spump`
- too new / sniping: blocked 36, ran 3, dumped 32, flat 0, open 1 (saving losses: keep it)
  - ran: Pair up to 1.76x  
    CA `EWCfhnj8YjPEbvQXEtwkxMT54WhBpZBLQDFncRoypump`
  - ran: SpaceXCoin up to 1.52x  
    CA `G2XqmSc8vJpLLwaLVXUeNkxsrhVT8vQ3Pje8MqeDpump`
  - ran: FARM up to 1.65x  
    CA `2dynAjPBnkqzjUwozgn8pDRkCf7k7CDJkLfcf4rupump`
- falling knife (code): blocked 22, ran 1, dumped 20, flat 0, open 1 (saving losses: keep it)
  - ran: Split up to 1.54x  
    CA `HAP9FcXubD88SjRHMY1kr5iukpRZgeMAgCBam3Vtpump`
- bundles over the line: blocked 21, ran 3, dumped 14, flat 3, open 1 (saving losses: keep it)
  - ran: Dragon up to 1.55x  
    CA `cg3HaDWhAKFfj9aq79TWUBgmxfs4G7byQ7feaxnpump`
  - ran: monky up to 96.37x  
    CA `At5hmwDn4YgPDoic1UN7zMdTtCoiXJsMhnKaoazEpump`
  - ran: USD1 up to 1.55x  
    CA `8Y24KBnY9gaNWDaxohxtEU1gxESvfwdYeGFuHJKpump`
- falling knife / no higher low: blocked 17, ran 2, dumped 11, flat 2, open 2 (saving losses: keep it)
  - ran: Maru up to 1.88x  
    CA `FokVFH6mDsazoKbtnUaA2FRMsRbDSwZhNfn17Fdvpump`
  - ran: Hoppy up to 1.76x  
    CA `CFX1gH7CKYwqYXrfDkS2MUxJcEhs8PT63DyRA1chpump`
- RugCheck danger: blocked 11, ran 0, dumped 9, flat 1, open 1 (saving losses: keep it)
- other: blocked 11, ran 1, dumped 9, flat 0, open 1 (saving losses: keep it)
  - ran: Christmas up to 1.89x  
    CA `5hkBYuFQDpAAqemCiVqXCuU6Ya5dqKhtRobzJsg6pump`
- dev share over 1%: blocked 9, ran 2, dumped 7, flat 0, open 0 (saving losses: keep it)
  - ran: bolphante up to 1.7x  
    CA `FVBzzG4ZcAgxSLW1rWjNC9EH9CgEgz1A4puNYexMpump`
  - ran: Fug up to 1.58x  
    CA `7mSf4uWLkgdkqBfSoxniv5aZ1sDCXCiquJNcisjXpump`

## Daily review (2026-11-27, claude-opus-5-5)
No edge after costs, and I'm fairly sure of that. All 250 settled coins averaged -12.7% net under the simple plan, and every setup and stage lost money (-12.2% to -15.2%). Before costs the average is still about -3%, because the median coin peaked at only 1.2x. At n=250 the standard error is roughly 2 points, so 'negative' is solid. The gaps between buckets (2-3 points) are noise, especially since the same coin can be logged more than once. The routine model made zero would-buys out of 130 coins it researched, so I can't test whether its buys beat its passes. The coins it passed on (-13.9%) did no worse than the checklist rejects (-11.5%) beyond noise. Passing everything was right for these 24 hours, but a model that never says buy gives the Nov 10 rule test nothing to grade.
- finding: Costs decide the result. The average round trip is 9.8% on a $10 buy. With a +50%/-20% plan, a win nets about +40% and a loss about -30%, so you need roughly 43% winners to break even. The best bucket ran 24%. Even with zero costs you would need about 29%, and nothing reached that.
- finding: MIGRATED: n=164, 20.1% ran, 12.2% hit 2x, median peak 1.21x, net -12.2%. That is the baseline and it loses money.
- finding: FINAL_STRETCH: n=50, 24.0% ran, 20.0% hit 2x (the highest), but 74% dumped (the most), net -12.8%. Fat tails on both sides. The 1.5x cap in the simple plan throws away the upside that makes this setup worth looking at at all.
- finding: DIP: n=36, 5.6% ran, 0% hit 2x, median peak 1.16x, net -15.2%. The worst setup on every measure. Not one dip-buy doubled in 24h.
- finding: Stages: checklist_failed n=120, 20.0% ran, net -11.5%. brain_passed n=130, 17.7% ran, net -13.9%. would_buy n=0. The brain's passes were neither better nor worse than code rejects (difference ~2.4 points, standard error ~3.8).
- idea to test: Exit variant on the same entries: sell half at 2x, trail the rest by 30% from the peak, stop at -20%, time stop at 6h. Compare it with the 1.5x/-20% plan on FINAL_STRETCH and MIGRATED. hit_2x is 12-20%, and tail capture is the only plausible source of edge here.
- idea to test: Cost gate: keep only coins with estimated round-trip cost ≤ 5% at the intended size. Also re-run the whole week at $20-25 size, since fixed fees dominate at $10. If no bucket turns positive even with costs at 5%, there is no edge at any size.
- idea to test: Retire DIP or tighten it: setup=DIP AND flow ratio ≥ 1.0 AND buy ratio ≥ 0.55 AND drawdown from high 40-60%. Compare with all DIP. If the filtered set still has 0% hit 2x over the week, drop the setup.
- idea to test: Young-migration bucket: setup=MIGRATED AND age ≤ 0.5h AND 30k ≤ mcap ≤ 80k AND 5m volume ≥ 10k AND checklist passed. Compare its net and dump rate with MIGRATED overall. Expect survivorship to cancel the top-runner effect.
- idea to test: FINAL_STRETCH flow quality: setup=FINAL_STRETCH AND 5m volume ≥ 10k AND buy ratio ≥ 0.55 AND flow ratio ≥ 1.0. The question is whether it lowers the 74% dump rate without losing the 20% that hit 2x.

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
The meta in the trenches right now is brand-new pump.fun joke launches, not the Trump riffs. The volume leaders are under an hour old: Mojave the Tortoise (0.1h, $31k cap, $20.6k 5m, 58% buys), cheng (0.7h, +503% in 1h, 60% buys) and EDITOR (0.8h, +76%, 61% buys), with animal and non-English names in the mix. The Trump-family riffs are fading: USD1 is -98% in 1h with no 5m volume, WLFI is a $286k coin on $3.4k 5m, and TRUMP isn't in the movers despite the dinner headlines. Fresh spikes are fading fast: SMOOTH and HPD are both down 79-82% in 1h, and MEMEPAY is -70% with zero buys on 5m. Setup to research: Mojave, the only mover clearing the ~$10k 5m bar, as a MIGRATED probe at conviction 5, with holder and bundle checks deciding whether it's a buy and a stop well under entry. cheng and EDITOR are below the 5m bar, so watch only. Caveat: the crawler summary says HPD is +525% at $18.9k and cites SPSC and FINGART, but the scan data shows HPD at -82% and $6k, so I used the scan numbers and did not rely on the summary.

## Moving most in its scans, last 30 min (1h volume)
- Mojave: $135,023 1h vol, $35,058 mcap, +22% 1h  
  CA `4newt1R5fGEoCKdf9XBgiR6B43iacmnVAR2d4Wt8pump`
- SMOOTH: $62,227 1h vol, $11,600 mcap, -63% 1h  
  CA `2n5tTb5UXKABFXYRxDEjtDpWFh5ZFk7oRcNLDML5pump`
- WLFI: $62,125 1h vol, $305,822 mcap, +28% 1h  
  CA `HmGQsYJyeiWrV6jABUY2Cb3bEmVxwk6LzVxCchsCpump`
- EDITOR: $49,940 1h vol, $8,802 mcap, -46% 1h  
  CA `57uooyjwYX2kpSGN3QnBLWAwk4KMZYbkp5e8f7i7pump`
- Snowball: $49,262 1h vol, $213,701 mcap, -7% 1h  
  CA `9TKbd3VFaMSXsEAicD9JVQWpWwAoLi4fSgWmZL2cpump`
