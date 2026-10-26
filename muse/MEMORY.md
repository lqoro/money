# MEMORY

## Owner and business (fill in every FILL_ME)
- owner_name: Lenny Ramirez (confirm, or change to the name you sign emails with)
- business_name: LeadDrop
- domain: FILL_ME
- sending_inbox: FILL_ME (e.g. hello@yourdomain.com)
- physical_address: FILL_ME (required in every cold email)
- timezone: FILL_ME (e.g. America/New_York)
- approval_channel: WhatsApp to FILL_ME
- payment_link: FILL_ME (Stripe Payment Link, $400/mo)
- drive_folder: FILL_ME
- virtual_card: FILL_ME (a virtual card with a spending limit, used only for approved purchases. Do not paste the number here)
- pipeline_sheet: FILL_ME
- claude_channel: the open pull request in lqoro/money from branch `claude/nice-noether-qxk1sn` (currently #3; see playbooks/08-claude-channel.md)

## Offer
- Product: **Weekly Lead List**, 25 researched prospects every Monday by 9am client time, delivered as a Google Sheet.
  Each row: business, website, decision-maker's name/role (if public), public contact route, the trigger ("why now"), and a personalized opener.
- Price: **$400/month**, cancel anytime. No setup fee.
- Free sample: 10 leads for their exact niche and city, delivered within 24h of a "yes". No card needed.
- Guarantee: if fewer than 20 of the 25 weekly leads are a fit, we replace them that week.
- Add-on (offer only after 4 weeks as a client): **Outreach drafts** (a 3-email sequence per lead): +$200/month.

## Ideal customers (ICP): work them in this order, one niche at a time
1. Small marketing / web design agencies (2–15 people) that sell to local businesses
2. Commercial cleaning companies
3. Bookkeepers and fractional CFOs serving small businesses
4. IT support / managed service providers (MSPs)
5. Commercial solar and HVAC installers (B2B side)
Region: US only to start. City sizes 100k–1M people.
Find the prospects on their own websites, Google Maps, Clutch, chamber-of-commerce directories, and industry associations.

## Triggers that make a lead good ("why now")
New business filing, hiring for sales or marketing, a new location, a website that's broken / not mobile / very old,
few or bad Google reviews, a recent funding or press mention, an expired promotion, a competitor that just closed.

## Money you may spend (each purchase needs the owner's yes first, see SOUL)
- spend_cap_setup: $100 total before the first client pays
- spend_cap_monthly: $60 until MRR is over $400, then ask
- approved_purchases: domain (about $15/yr, up to 3 more later for extra inboxes), Google Workspace Business Starter (one user per sending inbox), Stripe (free, the owner finishes ID checks), Netlify free plan. Anything else: ask.

## Prospects are strangers only
Never contact anyone the owner knows. Don't ask the owner for contacts. Every prospect comes from public research (playbook 01).

## Limits
- send_ramp (total emails per day, spread across inboxes, per-inbox max in brackets). Move up a step only when the previous step ran clean
  (bounces under 3%, opt-outs under 1%, no spam-folder warnings), and never faster than listed:
  days 1–7: 20 total [10 per inbox]
  days 8–14: 40 total [20]
  days 15–21: 80 total [30], needs 2 inboxes
  days 22–28: 150 total [40], needs 4 inboxes
  after day 28: up to 200 total [50], and ask the owner before going higher
  (about 1,000 emails a week by week 4. Sending 1,000 on day one from a new domain gets it blocked and the replies go to zero.)
- inboxes: 1 now; add one per step above when the ramp calls for it (new domain + new Workspace user, each approved as a purchase)
- follow_ups: at most 2, spaced 3 and 7 days after the first email
- auto_client_replies: off
- suppression_list: []  (opt-outs, bounces, "not interested"; never contact these again)

## STATE (update at the end of every run)
```
week_of: 2026-10-26
current_niche: marketing agencies
current_cities: []
mrr: 0
clients: []          # {name, niche, city, ICP notes, start_date, sheet_url, status}
pipeline_counts: {prospects: 0, emailed: 0, replied: 0, sample_sent: 0, won: 0, lost: 0}
awaiting_approval: []
todo: []
lessons: []          # what's working / not working: subject lines, niches, cities
```

## HANDOFF (overwritten nightly by the Night Handoff routine)
```
date:
done_today:
open_threads:
next_up:
blockers_for_owner:
```
