# Income ideas for the study abroad plan (AI and agents)

Built from my notes on all 368 of Nate Herk's videos. `Vnnn` = video number in [nate-herk/video-index.md](nate-herk/video-index.md).

> **Read first: work rights.** Many student visas limit paid work, and some countries treat freelancing or self-employment (even for clients abroad) as work. Check with your school's international office or the immigration authority **before you charge anyone**. See [RISKS-AND-LIMITS.md](RISKS-AND-LIMITS.md). Until then, everything below (building demos, learning, free portfolio projects) is the safe part.

> **How to read the numbers.** Dollar figures are what Nate or his guests *claim* in the videos (marked *claim*) or my inferences (marked *inference*). Nate funnels viewers to his free school community, a paid "Plus" community (about $89/month per V232) and courses, so income stories are marketing, not evidence. Plan with your own numbers.

## Ranking (for: remote, flexible hours, low startup cost)

| Rank | Idea | Typical buyer | Price signals in the videos | Hours per week once running | Main risk |
|---|---|---|---|---|---|
| 1 | Done-for-you workflow for one small-business pain (inbox, lead follow-up, document intake, onboarding) | Local and small service businesses, agencies | $1,200-$2,600 first builds, $6,000 for a team assistant *(claims)* | 5-15 | Needs work rights; finding clients |
| 2 | Monthly maintenance and monitoring retainer on builds you delivered | Same clients | Separate from the build fee (V204, V213); $5K-$20K/month retainers are *claims* | 2-5 per client | Scope creep; keep "no new features" in the contract |
| 3 | Document Q&A (RAG) assistants | Firms with manuals, policies, product docs | not stated | 5-10 | Data privacy; keeping content updated |
| 4 | Voice receptionist / lead-call agent | Local service businesses (HVAC, detailing, clinics) | $5,000 in 21 days *(claim, V239)* | 5-10 | Call-recording and health-data rules |
| 5 | Personal assistant / inbox-manager setups | Founders, busy operators | $1,650 (V202) and $6,000 (V242) *(claims)* | 5-10 | Security of connected accounts |
| 6 | Agent QA, evals and guardrail audits | Agencies that deploy support bots | $499/month reports *(claim, V26)* | 3-6 | New market, unproven demand |
| 7 | Cost-and-model optimization audit | Teams already spending on AI | not stated (V90, V145, V291) | 2-5 | Hard to prove savings |
| 8 | Creative production with AI (sites, video, ads) | Small brands, creators | not stated; "$10k websites" in V144 is a title, not a price | 5-15 | Crowded; clients pay for taste |
| 9 | Lead lists and outreach as a service | B2B sales teams, agencies | about $24 spend per 100 leads (V75, Nate's estimate) | 5-10 | Spam law and scraping terms |
| 10 | Teaching and templates (workshops, team training) | Companies, other students | "few thousand to tens of thousands" per project for consulting (V224) | variable | Needs credibility first |
| 11 | Small SaaS product | Agency owners, niche users | $19 per approved response concept (V79, not built); about $30/year app example (V163) | 10+ | Highest effort; subscriptions are hard to sell cold (V66) |
| 12 | In-house AI role | Your employer | $200K-type job headlines (V74) | n/a | Later-career path |

Rank 1-3 together form the simplest ladder: **one pain -> one build -> one retainer**.

## How Nate and guests price and sell (consistent across videos)
- **Service ladder:** free work or audit -> small paid session ($100-200 in V65, about $100/hour trial in V48) -> paid audit ($1K-$10K in V48) -> build -> retainer.
- **Price on value, not hours:** about 10% of first-year value, and the "10x" test (V23, V52, V206, V242). Use the client's own numbers for hours or money saved (V156, V236, V240).
- **Structure:** fixed build fee, staged payments (two payments in V242; 30-day milestones with objective acceptance criteria in V23), separate maintenance retainer that excludes new features (V204), written scope and done criteria.
- **Clients pay API costs directly and own their accounts** (V23, V167, V204, V219): less risk for you.
- **First clients:** warm contacts (list 50, V218), free or discounted pilot for a testimonial (V185, V189), build in public and post demos with contact info (V245, V248, V252, V202), partner with consultants and agencies that already have clients (V185), cold outreach with proof (V75, V186).
- **Sell the outcome, not the agent:** "sell the booked call, not the voice agent" (V125); "sell solutions, not agents" (V236).

## Idea details (first 30 days)

### 1. Done-for-you workflow for a single pain
- **What to offer:** the five most common automations in V58 and V156: document processing, lead routing and follow-up, missed-call recovery, inbox triage, onboarding. Start with the one your first contact already complains about.
- **Days 1-10:** build a demo with fake data; record a 2-minute walkthrough. Tools: n8n or Claude Code (V167, V281).
- **Days 11-20:** message 50 warm contacts (V218); offer one free pilot to the first 1-2 who say yes; write the scope on one page.
- **Days 21-30:** measure before and after (hours saved, replies faster); ask for a testimonial; propose a paid next step or retainer.
- **Watch for:** do not sell a generic email product, big providers are adding AI (V202).

### 2. Maintenance and monitoring retainer
- Include monitoring, error alerts and small fixes; exclude new features (V204). Self-healing monitors are discussed in V195. Set the price after the first month of results (V52).

### 3. Document Q&A (RAG) assistant
- Pick one business with manuals or policies (V316 uses a body shop example; V357 internal knowledge for menus and SOPs). Build ingestion once, then charge for updates. Test on the client's own documents first (V238). Always show source citations (V259).

### 4. Voice receptionist
- Build one demo for a fictional local business (V210, V222), then try one real business with a free first month (V73 suggests free first service to win trust). Put guardrails in (call length cap, domain lock, rate limit; V125). If health data is involved, get compliance advice first (V239 flags HIPAA).

### 5. Personal assistant / inbox setups
- Slack or Telegram assistant that searches mail, looks up contacts and drafts replies (V202, V242, V358, V360, V363). Use read-only access first and approval before sending (V317, V288). Phase the rollout (Slack first, then other sources) as in V242.

### 6. Agent QA, evals and governance audits
- V26 describes weekly QA reports on support bots for agencies, at $499/month *(claim)*, starting with refunds and billing disputes. V244 shows evals in n8n; V46 argues governance is what businesses will pay for. Unproven demand, so test with 5 conversations before building.

### 7. Cost and model optimization
- Show a client what they spend per task and where a cheaper model passes the same test (V90, V145, V291, V290). A good low-risk first offer because it needs no integration, only logs and a test set.

### 8. Creative production
- Websites (V44, V55, V134, V144, V177), video (V19, V132, V136, V140), ads and UGC (V124, V223, V227, V243). Build one demo per niche, pitch with the pain/person/promise brief (V39, V44, V57). Prices are not stated, so use your own market check.

### 9. Lead lists and outreach
- Prospect lists and personalized drafts (V75, V251, V347, V350, V355, V362, V364). Terms of service for scraping (Google Maps in V347) and cold-email law apply. Offer lists you collected from allowed sources and require your client to handle consent.

### 10-12. Teaching, SaaS, in-house role
- Teaching: V224 (education and team training), V227 (teach marketers prompting). A skills marketplace is mentioned in V179 with a warning not to rely on it.
- SaaS: V66 (proposal-deck SaaS; free deck first, moat is proof and prompts). Keep for after you have client revenue and data.
- In-house role: V72, V74, V88, V96 (propose a measured pilot, ask for budget and title).

## What not to chase
- Anything promising passive income from faceless channels, or "AI trading bots" (V17, V35, V138, V146): the videos present them as experiments, not products.
- "$20K/month retainer" and "$100M agency" stories (V23, V52, V68, V109): useful for how they price, not as a forecast of your income.

## Next steps
1. Confirm work rights (see risks file).
2. Pick one niche and one pain; list 50 contacts.
3. Build the demo and the one-page scope.
4. Run 1-2 free pilots; collect a number and a testimonial.
5. Decide whether to continue to a paid build; check taxes and payments first.
