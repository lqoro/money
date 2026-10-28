# Trencher live branch

Shared between Trencher (running on the Mac mini) and Claude Duet. Paper trading only.

- `status.json` and `REPORT.md`: written by Trencher every 15 minutes.
- `steer.json`: written by Claude Duet. Trencher applies it on its next sync:
  - `pause_new_trades`: true stops new buys (open positions are still managed)
  - `settings`: any setting Trencher can evolve, e.g. `{"stop_loss_pct": 25}`, clamped to its bounds
  - `owner_note`: a short note the brain reads before every decision

Never put keys or secrets here.
