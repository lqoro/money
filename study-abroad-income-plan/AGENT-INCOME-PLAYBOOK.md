# Agent income playbook

Ways to earn with agents, and the build and delivery patterns behind them. Source: my notes on Nate Herk's 368 videos (`Vnnn` = video number, see [nate-herk/video-index.md](nate-herk/video-index.md)). Pricing and results are *claims* from the videos unless I say *inference*. For the always-on personal bot angle, see [CLAUDE-DUET-READY.md](CLAUDE-DUET-READY.md). Work-rights and legal limits: [RISKS-AND-LIMITS.md](RISKS-AND-LIMITS.md).

## 1. First decision: agent or workflow?
- Nate's repeated advice: **default to a deterministic workflow**; use an agent only where judgement or language handling is needed (V205 "AI agents are overused", V304 what beginners get wrong, V31 what to build instead of agents, V127 boring automations on trigger.dev or Modal).
- A client pays for the **outcome** (hours saved, leads answered), not the architecture (V125, V236, V229).
- Cheaper and more reliable builds make better margins and easier handover (V204).

## 2. Offers you can sell (agent-flavoured)
| Offer | What the client gets | Evidence in videos |
|---|---|---|
| **Inbox triage / assistant** | Labels, drafts and summaries; phone ping | V202 ($1,650 *claim*), V358, V360, V363, V313, V337, V29 |
| **Lead response and follow-up** | Reply and tag new leads; human sign-off before sending | V322, V354, V251, V364 |
| **Document Q&A (RAG)** | Chat over manuals and policies with citations | V366, V238, V260, V357, V316 |
| **Voice receptionist / lead-call agent** | Answers calls, books, qualifies | V222, V210, V201, V239 |
| **Team assistant (Slack-based)** | Answers from Notion, Drive, Gmail, Slack | V242 ($6,000 *claim*), V273, V291 |
| **Content pipelines** | Newsletters, social posts, UGC variants, summaries | V247, V250, V330, V223, V243 |
| **Research and monitoring** | Scheduled competitor, news and price reports | V266, V279, V278, V196 |
| **Browser automation for tools with no API** | Scripted clicks via Playwright or Airtop | V130, V278, V162 |
| **Always-on assistant setup** | Telegram or Slack assistant with memory and routines | V48, V191-V193, V119, V50 |
| **QA, evals and guardrail audits** | Weekly scorecards on a client's bot; safety layer | V26 ($499/month *claim*), V244, V220 |
| **Cost and model-routing audit** | Cheaper model per task without losing quality | V90, V145, V291, V290 |
| **Agent maintenance retainer** | Monitoring, fixes, small improvements | V204, V195, V213 |

## 3. Reusable architecture patterns
1. **Trigger -> gather -> decide -> act -> log.** Webhook/schedule/inbox event, fetch context, one model call or a small agent, action (draft, update, send), write a log row (V295 error handling, V290 token tracking).
2. **Human in the loop for anything outward-facing.** Draft first; the owner approves by tap or reply; then send (V288, V317, V322).
3. **Memory:** short-term chat memory for conversations (V262), per-user memory keyed by email or phone (V260), shared vs private memory across bots (V47, V59).
4. **Retrieval:** ingest once, keep add/update/delete flows, use metadata and reranking, always show sources (V259, V268, V311).
5. **Guardrails:** redact personal data before model calls, check outputs, rate limits, domain lock on public bots (V220, V125, V261).
6. **Model routing:** small steps on cheap models, hard reasoning on strong ones; split big skills into smaller ones (V8, V291, V90).
7. **Skills as the reusable unit:** a markdown skill per repeatable task (interview-the-client, branded report, scrape, QA check); teach a task by recording it where the tool supports that (V59, V179, V25).
8. **Chief-of-staff pattern:** one front-door agent delegates to specialists; give each agent one job and a clear description so routing works (V47, V59, V64).
9. **Safety defaults:** read-only first, separate accounts for bots, secrets in `.env`, approvals and action logs (V18, V191, V192, V193).

## 4. Delivery checklist (from V204, V219, V312, V102)
- [ ] Discovery call: process, volume, who approves, what a "win" looks like (V102).
- [ ] Wireframe the flow before quoting; list integrations and who owns each account (V312).
- [ ] One-page scope: inputs, outputs, done criteria, exclusions.
- [ ] Client creates and owns accounts (n8n hosting, API keys, billing); you work as adviser and builder (V219, V204).
- [ ] Staged payments; milestones with objective acceptance (V23, V242).
- [ ] Test on the client's real examples before launch (V238).
- [ ] Handover doc: how it works, where it runs, how to pause it, who to call.
- [ ] Maintenance retainer excluding new features (V204); monthly report with the metric you agreed (V67).

## 5. Pricing guide (Nate and guests; claims)
- Free pilot or audit first, then paid session ($100-$200, V65), paid audit ($1K-$10K, V48), build, retainer.
- First builds quoted around $1,200-$2,600 (V218, V240, V248, V202, V206), 4 agents for $23,000 in total (V245), a $6,000 team assistant (V242).
- Value rule: about 10% of first-year value, and the "10x" test (V23, V52). Convert your own examples (hours saved x hourly cost x 12) before quoting.
- Retainers of $5K-$20K/month are claims from his agency years (V48, V52, V68); treat them as upside, not a plan.

## 6. Agent-as-a-service ideas to test (inference)
- A **"morning brief" assistant** for a small business owner: calendar + inbox + task list into one daily message (pattern in V28, V173, V191).
- **Role-specific chief-of-staff packs** (real estate, recruiting, coaching, agencies): a few specialist agents, connectors and approval rules pre-configured, customised per client (pattern in V59, V64).
- **Agent safety review**: permissions, secrets handling, webhook security and cost caps for people who set up their own bots (V261, V192, V193).
- **Skill packs** per niche (inference from V179, which warns not to rely on a skills marketplace as a business).

## 7. Stack I would start with (inference, from what the videos use most)
Claude Code for building (V76, V167), n8n for hosted workflows (V356) or trigger.dev/Modal for code workflows (V127), Supabase or Pinecone for retrieval (V316, V357), Vapi or ElevenLabs for voice (V222, V333), a small VPS or managed host for always-on jobs (V183, V193; about $6/month in V50), and a Google Sheet as the client-facing control panel (V250, V364).
