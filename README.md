# money

A business that Muse (Meta's always-on agent) runs around the clock. You spend about 10 minutes a day approving what it sends.

**Goal:** $10/hr around the clock = **$240/day ≈ $7,200/month**. Then scale.

## The business: "LeadDrop"

A done-for-you weekly lead list for small B2B service sellers (marketing agencies, web designers,
commercial cleaners, bookkeepers, IT/MSPs, solar installers). Every Monday each client gets a
spreadsheet of researched prospects that fit their target customer. Each row has a verified public
contact route, a reason this prospect needs the client *now*, and a ready-to-send personalized
opening line.

Why this one (from [the Nate Herk recap](research/nate-herk-all-videos-recap.md)):

| Recap lesson | How LeadDrop uses it |
|---|---|
| "One small-business pain, one automation, one retainer" | Pain = "I don't have enough leads". One recurring deliverable, billed monthly. |
| Sell the outcome, not the AI (#296, #304: "get more customers" bucket) | We sell booked conversations, not "an AI tool". |
| Lead gen + personalized outreach, priced per batch (#118, #294, #362) | This is the product. |
| Free first build, then paid (#145, #297, #304) | Every prospect gets a free sample of 10 leads before we ask for money. |
| Human approval for money, publishing and sending (#81, #351) | Muse drafts. You approve every outbound message and every invoice. |
| Stateless runs need handoff notes (#334, #352) | Each routine reads and writes `STATE` in memory, plus a nightly handoff. |
| Not recommended: trading bots, faceless channels, scraping without checking the rules (summary #7) | Public business info only. No logins, no LinkedIn scraping, CAN-SPAM-compliant email. |

Muse does all of the work on its own computer and browser. It needs no API to the client's systems,
no phone line and no hosting, so it can actually run hands-free.

## The math

| | |
|---|---|
| Price | **$400/month** per client (a 25-lead weekly list, ~100 leads/month) |
| Target | **18 clients = $7,200/mo ≈ $10/hr** |
| Muse workload per client | ~1–2 hours of agent time a week |
| Your time | ~10 min/day approving sends and invoices, plus the occasional sales call |
| Costs | Muse plan, a domain + Google Workspace inbox (~$8/mo), Stripe fees (~3%) |

**Honest expectation:** this is not passive on day one. Cold outreach usually converts at about 1%
or less (the recap's own estimate in #294). So 18 clients means roughly 1,500–2,000 well-targeted
prospects and 6–12 weeks of Muse running the sales loop. Treat these milestones as the real plan:

1. First reply → 2. First free sample delivered → 3. First paying client ($0.55/hr)
4. 5 clients ($2.75/hr) → 5. 18 clients ($10/hr) → 6. Scale ([SCALING.md](SCALING.md))

## What's in here

| File | What it is | Where it goes in Muse |
|---|---|---|
| [`muse/SOUL.md`](muse/SOUL.md) | Identity, mission, hard rules | Muse's **soul / persona** file |
| [`muse/MEMORY.md`](muse/MEMORY.md) | Offer, pricing, ICPs, and the live `STATE` block | Muse's **memory** file |
| [`muse/ROUTINES.md`](muse/ROUTINES.md) | 7 scheduled tasks with paste-ready prompts | Muse **scheduled tasks** |
| [`muse/playbooks/`](muse/playbooks) | Step-by-step for each job | Upload as files, or paste into memory |
| [`muse/templates/`](muse/templates) | Emails, the lead sheet schema, the pipeline tracker | Same |
| [`muse/skills/humanizer/`](muse/skills/humanizer) | The owner's humanizer skill plus voice profile. Playbook 07 runs it on every outbound message, with a ZeroGPT check | Upload as files (SETUP step 6) |
| [`SETUP.md`](SETUP.md) | One-time setup checklist (≈2 hours) | You |
| [`muse/SESSION-1.md`](muse/SESSION-1.md) | Messages to paste into Muse, with Claude checking each reply | You ↔ Muse ↔ Claude |
| [`build/`](build) + [`scripts/build.py`](scripts/build.py) | Paste pack, website and Pipeline.xlsx with your details filled in | Muse, Netlify, Google Sheets |
| [`site/`](site) | Source of the one-page website | Netlify |
| [`SCALING.md`](SCALING.md) | What to do after $10/hr | You + Muse |
| [`research/`](research) | The full video recap Muse can reference | Upload as a file |

Start with **[SETUP.md](SETUP.md)**.
