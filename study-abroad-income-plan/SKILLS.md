# Skills worth learning (from Nate Herk's 368 videos)

Ranked by **payoff for earning money while studying abroad**: remote, flexible hours, low startup cost. `Vnnn` = video number in [nate-herk/video-index.md](nate-herk/video-index.md); each has a condensed note in `nate-herk/notes/`.

**Honesty notes.** Time-to-competence figures are my rough estimates, not Nate's. Nate sells communities and courses (free "school" community, paid "Plus", courses), so treat "learn this to make money" as a pitch to check against real buyers. Income numbers are labelled *(Nate's claim)* in the notes and are not evidence.

## Tier 1: learn first (direct line to paid work)

### 1. Building automations that actually run in production
- **What:** triggers, API calls, webhooks, scheduled jobs, error handling, retries, logging. Nate's tools: **n8n** (no-code; V190 "Is n8n dead?" argues about its future), **Claude Code** for building them, and **trigger.dev / Modal** for plain code-based automations. He repeatedly says boring deterministic workflows beat agents for reliability (V127, V205, V304).
- **Learn from:** V214 (17 essential nodes), V295 (error handling), V264 (parallelization), V28 (automations that don't eat usage limits), V115 (deploying Claude automations, 3 methods), V141 and V183 (hosting always-on agents), V338 (APIs for beginners), V356 (n8n masterclass), V281 (8+ hour course).
- **Prove it:** a workflow that handles a real input end to end (form -> enrich -> draft -> approval -> send) with error alerts and a run log. Estimate: 3-6 weeks part-time.

### 2. Claude Code (and skills) as your build engine
- **What:** project setup and context files, plan mode, sub-agents, slash commands, hooks, scheduled tasks, MCP connections, **writing reusable skills**, keeping context lean to save tokens.
- **Learn from:** V76 (Claude Code for non-coders, 6 h), V167 (build and sell with Claude Code, 10+ h), V91, V129 (32 tricks), V179 and V25 (skills), V175, V143, V196, V182 (first agentic workflow), V152, V154, V111 and V122 (token and session-limit savings), V12 and V103 (mods and features).
- **Prove it:** three skills you reuse across projects (for example a "grill me" interview skill, a branded report skill, a scraping skill). Estimate: 2-4 weeks.

### 3. Client discovery, scoping and delivery
- **What:** run a discovery call, map the client's process before building, write scope and "done" criteria, price, take staged payments, hand over cleanly, then run a maintenance retainer.
- **Learn from:** V102 (extracting requirements), V312 (wireframe before quoting), V204 (delivery, hosting, handover; client owns accounts and pays API costs), V219 (client holds billing), V213 and V68 (pricing), V242 (live $6,000 sales call), V23 and V52 (value-based pricing: about 10% of first-year value, "10x" test), V236 (sell solutions, not agents), V3 (turn agents into repeatable processes).
- **Prove it:** one written scope-of-work template and one case study with a before/after number. Estimate: ongoing; first usable version in 1-2 weeks.

### 4. Finding and signing your first clients
- **What:** warm network first (list 50 contacts, V218), free or discounted pilot to get a testimonial (V185, V189), building in public so inbound leads find you (V245, V248, V252), cold outreach done carefully (V75, V186, V350), partnering with agencies and consultants who already have clients (V185).
- **Prove it:** 10 conversations booked; one paid pilot. Estimate: 4-8 weeks; this is the real bottleneck, not tool skill.

## Tier 2: strong add-ons clients ask for

### 5. RAG: chat over a business's own documents
- **What:** chunking, metadata, embeddings, vector databases (Pinecone, Supabase/Postgres), reranking, citations, keeping the knowledge base updated.
- **Learn from:** V203, V228, V260 (beginner course), V238 (no-code), V259 (metadata), V268 (reranking), V311 (agentic RAG), V316 (Supabase + memory), V339 (strong RAG system), V357 (100+ files to Pinecone), V366 (RAG chatbot), V215 (Gemini file search, cheaper), V168 (RAG with Google's new model).
- **Prove it:** a Q&A bot over a real policy or manual that cites its sources, tested on 20 questions. Estimate: 3-4 weeks.

### 6. Voice agents (receptionists, lead-qualification calls)
- **What:** Vapi or ElevenLabs agents wired to n8n for booking, FAQs and follow-up; cost guardrails (domain lock, call length cap, rate limit); compliance (call recording, health data).
- **Learn from:** V222 (beginner's guide), V210 (receptionist + template), V201 (calls every new lead), V239 (Vapi + n8n voice agent, "won $5,000 in 21 days" *(Nate's claim)*), V125, V158, V256, V319, V333, V334.
- **Prove it:** a receptionist demo for one fictional local business you can show on a call. Estimate: 2-3 weeks.

### 7. Agent design: memory, human approval, guardrails, evals
- **What:** when an agent beats a workflow (usually it does not, V205, V304), human-in-the-loop approvals (V288, V317, V322), memory (V262), guardrails and PII redaction (V220), sub-agent teams (V258, V277, V315), evaluating output quality (V244), model comparison (V131).
- **Prove it:** an agent with an approval step and a small test set that scores its answers. Estimate: 3-5 weeks.

### 8. Cost control and model routing
- **What:** use the cheapest model that passes your test, track tokens and cost, avoid usage-limit burn, run cheap/local models for routine work.
- **Learn from:** V90 (GLM in Claude Code), V145, V151 (Ollama), V291 (agent picks its own model), V290 (token tracking), V325 and V328 (DeepSeek), V54 and V56, V111, V152, V16 and V37 (cost per task comparisons).
- **Why it pays:** lower delivery cost lets you price against client value with better margin; also sellable as an audit (V90).

### 9. Security and safe access
- **What:** webhook authentication (V261), read-only defaults, separate accounts for bots, secrets in `.env`, keeping API keys out of workflows, approval gates, action logs (V18, V191, V192, V193).
- **Why it pays:** every client automation touches email, calendar or CRM; a clean permission story is a selling point.

## Tier 3: useful, but lower or less certain payoff

### 10. Always-on personal agents and "AI operating systems"
- **What:** persistent assistants (Grok Bot, Hermes, OpenClaw/Clawdbot, Claude Code remote/channels) with identity and memory files, a heartbeat, routines, connectors. A personal "AIOS" of your goals and business context.
- **Learn from:** V47, V48, V59, V64 (Grok Bot), V119 and V50 (Hermes), V191-V193 (Clawdbot), V159, V162, V180 (Claude Code on phone), V71, V97, V110, V127 (AI OS setups), V36, V81, V92 (second brain). See [CLAUDE-DUET-READY.md](CLAUDE-DUET-READY.md).

### 11. Creative production with AI (video, ads, sites)
- **What:** website design skills (V44, V55, V134, V144, V177), AI video editing and avatar video (V19, V132, V136, V140), ad creative and UGC (V124, V223, V227, V243).
- **Caution:** buyers pay for results, not tools; prices are not stated in the videos. Good for portfolios and local-business offers.

### 12. Data collection and lead generation
- **What:** scraping and enrichment (Firecrawl V187/V297, Playwright V130, Clay V75, Apify), prospect lists (V347, V350, V355, V362).
- **Caution:** scraping and cold email carry terms-of-service and spam-law risk (see [RISKS-AND-LIMITS.md](RISKS-AND-LIMITS.md)).

### 13. Consulting and in-house AI roles
- **What:** diagnose a workflow, pilot one fix, show measured results; or become the in-house AI person (V72, V74, V88, V96, V114).
- **Why later:** best once you have 1-2 case studies.

## What I would not prioritise
- Automated faceless video channels (V271, V286, V300, V310): platform-policy and low-quality-content risk, little client demand evidenced.
- AI trading bots (V17, V35, V138, V146): experiments, no product, and not financial advice in the videos themselves.
- Learning every new model release: pick one build tool and one test set, then compare models only when a project needs it (V16, V37, V77).

## Suggested 12-week path (my plan, adjust as needed)
1. **Weeks 1-2:** Claude Code basics and 3 skills (V76, V179); build one n8n workflow with error handling (V214, V295).
2. **Weeks 3-4:** deploy it somewhere that stays on (V115, V183); write a scope template and price sheet (V204, V213).
3. **Weeks 5-6:** build one demo per offer: inbox triage, RAG over documents, voice receptionist.
4. **Weeks 7-9:** 50 warm-contact messages and 2 free pilots (V185, V189, V218); collect a testimonial and a before/after number.
5. **Weeks 10-12:** convert a pilot to a paid build; propose a maintenance retainer; check work-rights rules before charging anyone (see risks file).
