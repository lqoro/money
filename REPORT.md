# Trencher live report

Updated 2026-10-29T01:59:24Z (paper trading, never real money)

- Equity: $103.00 (+3.0% vs $100 start)
- Closed trades: 4, 1 wins
- Fees paid: $3.46 (axiom $0.35, network $2.66, pool $0.31), plus $0.51 lost to slippage
- New trades: on
- Brain: subscription, 223 calls and 0 plan-limit hits in 48h

## Open positions
- FLOAT (MIGRATED): cost $3.09, 1.36x, fees $0.24  
  CA `Bv1a7cEj5aRnJQhMw4kRQqAFesMSd5LwcDnUzq52BMmr`
- FLOATER (MIGRATED): cost $2.94, 1.58x, fees $0.53  
  CA `J7cqsaTuXUavwA3sp238tSpartUfYwDrJAaHuDvypump`
- CPU (MIGRATED): cost $3.16, 1.35x, fees $0.24  
  CA `5JbRYEz844bwnKbGx4dRHhrJ6zjrJ194CKdDXtzwgaXo`

## Recent trades
- 22:55Z SELL CATBOT for $1.65, fees $0.24  
  CA `dyw5fDNv91eknniMG4tGCU1ZrzjuxbpsLiEzih6pump`
- 22:59Z SELL CATBOT for $1.22, fees $0.23  
  CA `dyw5fDNv91eknniMG4tGCU1ZrzjuxbpsLiEzih6pump`
- 22:59Z CLOSE CATBOT +94% ($+2.73), fees $1.01  
  CA `dyw5fDNv91eknniMG4tGCU1ZrzjuxbpsLiEzih6pump`
- 00:10Z BUY FLOAT $3.09, fees $0.24  
  CA `Bv1a7cEj5aRnJQhMw4kRQqAFesMSd5LwcDnUzq52BMmr`
- 00:43Z BUY FLOATER $2.94, fees $0.27  
  CA `J7cqsaTuXUavwA3sp238tSpartUfYwDrJAaHuDvypump`
- 00:46Z BUY CATBOT $3.42, fees $0.27  
  CA `dyw5fDNv91eknniMG4tGCU1ZrzjuxbpsLiEzih6pump`
- 01:18Z BUY CPU $3.16, fees $0.24  
  CA `5JbRYEz844bwnKbGx4dRHhrJ6zjrJ194CKdDXtzwgaXo`
- 01:31Z SELL CATBOT for $2.59, fees $0.26  
  CA `dyw5fDNv91eknniMG4tGCU1ZrzjuxbpsLiEzih6pump`
- 01:32Z CLOSE CATBOT -24% ($-0.83), fees $0.53  
  CA `dyw5fDNv91eknniMG4tGCU1ZrzjuxbpsLiEzih6pump`
- 01:39Z SELL FLOATER for $2.80, fees $0.27  
  CA `J7cqsaTuXUavwA3sp238tSpartUfYwDrJAaHuDvypump`

## Last closes
- Something: -15% ($-0.51), time stop: 60 min and only 0.98x  
  CA `AZdhikmyj6ibsejv7EjML9SfNmuiMvwDrKXTEU2zpump`
- CATCULUS: -59% ($-1.75), stop loss -30% hit (0.55x)  
  CA `AfPhjrZx3oyh38G28ZVViP4p7h53N5kTxEeg5tzhpump`
- CATBOT: +94% ($+2.73), trailing stop: -35% from peak  
  CA `dyw5fDNv91eknniMG4tGCU1ZrzjuxbpsLiEzih6pump`
- CATBOT: -24% ($-0.83), time stop: 45 min and only 0.92x  
  CA `dyw5fDNv91eknniMG4tGCU1ZrzjuxbpsLiEzih6pump`

## Recent lessons
- [2026-10-28 14:15] Expected: a $1.2M dip 47% off the $2.3M peak, with $17.8k 5m volume and buys outnumbering sells 3:1, to retest $2M while the joke still had a crowd (V1 buys-on-dip, V6). What happened: it peaked at 1.09x, then went flat and got time-stopped at 60 minutes with market cap basically unchanged (-0.6%), but I still lost 15.4% because fees and slippage ate about 9% of a $3.33 position, and the rest of the gap is execution I can't see in the record. Rule: on DIP setups, enter only after the dip makes a higher low with 5m volume rising (0.86x the hourly average is fading, not holding). Never open a position so small that round-trip friction is over 3%, because a flat chart is a guaranteed loss at that size.
- [2026-10-28 22:50] Expected: CATCULUS at $460k was the flow leader ($59k 5m volume, 913/363 buys/sells, top 10 at 3.6%), so a momentum entry near the high should either keep running or give a clean -30% exit. What happened: it peaked at 1.24x, the bundle/insiders dumped, and it gapped through the -30% stop to -59% in 42 minutes. Clean top-10 numbers don't rule out bundles spread across many small wallets (V3, V5), and $0.50 in fees on a $2.96 position was a 17% loss before the coin even moved. Rule: no MIGRATED momentum buys within ~20% of the local high unless bundle data is verified. Wait for the V1 0.618 fib or point-of-control retest instead, and skip any position so small that fees are over 5% of cost.
- [2026-10-28 22:59] Expected: the original Cat Bot pair would retest its $845k peak, because holders were clean (top 10 at 3.3%, dev/insiders 0%) and 5m volume was organic at $12.9k (V1, V6, V13). Happened: it ran to 4.44x peak, I took initials at 2x, and the target plus a 35% trail closed the rest around 2.67x, so the clean MIGRATED dip-buy worked but the trail gave back about 40% of the peak, and fees ate roughly a third of a $2.91 position. Rule: once initials are out and the coin is past 4x, tighten the trail to about 25% from peak, and don't open positions under about $5 where fees ruin the math, because sell initials only protects the cost basis, not the runner (V11).
- [2026-10-29 01:32] I bought CATBOT back as a $2.0M base retesting toward the $3.46M high. Price only drifted from $2.59M to $2.41M (-7%) and peaked at 1.12x, but I lost -24.3% because $0.62 in fees and slippage on a $3.42 position cost 18% before the coin moved at all. That makes the time stop correct (V1: don't marry a bag), and the real problem was the size. Rule: before any entry, including a buy-back, I estimate round-trip cost and skip the trade if it tops ~5% of size or if the target can't pay several times that cost. I also only re-enter a stopped-out coin when it reclaims the high, not when it bases in the middle of the range.

## Meta right now
It's quiet. Nothing is running in the trenches right now. The loudest Solana story is Hunter Biden's $LAPTOP, which fell about 98% on day one and is fading. A political figure pushed that CA, so it's a hard no, and so is any vamp or "revival" of it (V13). The Robinhood/Circle hype is fading too. The money that's rising is bucket-2 money, not trench money: tokenized stocks and Robinhood Chain, stablecoins and RWA, PEPE and PENGU on CoinGecko trending, the Frog-Themed and Boy's Club categories, and BTC above $81k ahead of the Fed (V8). $MT (3 mentions), $LICK and $POKERFACE (1 each) are a few scattered mentions with no crowd behind them, so I'm not chasing them (V7). The one meta I can see coming is Halloween, three days out, and holiday metas get front-run, so it could start any hour now (V5). The coin that rides it will be an original, funny spooky idea, like a pumpkin or a frog in a costume that catches the PEPE/frog flow, not a knockoff (V1). It also has to be bonded, do $10k+ in 5-minute volume and have clean holders before I touch it (V1, V6). Nothing like that has shown up yet. PASS for now; watching for pumpkins.
