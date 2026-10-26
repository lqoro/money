# MEMORY

## Owner and business (fill in every FILL_ME)
- owner_name: FILL_ME
- business_name: LeadDrop
- domain: FILL_ME
- sending_inbox: FILL_ME (e.g. hello@yourdomain.com)
- physical_address: FILL_ME (required in every cold email)
- timezone: FILL_ME (e.g. America/New_York)
- approval_channel: WhatsApp to FILL_ME
- payment_link: FILL_ME (Stripe Payment Link, $400/mo)
- drive_folder: FILL_ME
- pipeline_sheet: FILL_ME

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

## Limits
- daily_send_cap: 20 (weeks 1–2), then 40, max 60. The owner raises it.
- follow_ups: at most 2, spaced 3 and 7 days after the first email
- auto_client_replies: off
- suppression_list: []  (opt-outs, bounces, "not interested"; never contact these again)

## STATE (update at the end of every run)
```
week_of: FILL_ME
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
