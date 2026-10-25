# Claude duet: preparing before release

You described "Claude duet" as Claude's version of Meta's Muse and xAI's Grok Bot, an always-on personal agent, not yet released. **I don't know its real features**; this file prepares for that kind of product using what Nate's videos show about the current ones. Anything marked *assumption* must be checked against the real release.

Sources: V15 (Dots vs Muse), V47, V48, V59, V64, V8, V29 (Grok Bot), V50, V119 (Hermes), V146, V191-V193 (OpenClaw/Clawdbot), V159, V162, V180, V103 (Claude Code on phone, channels, dispatch, routines), V147 (Claude managed agents). See [nate-herk/video-index.md](nate-herk/video-index.md).

## 1. What this product category does (from the videos)
- **A persistent agent with its own cloud computer**, running when your devices are off (V15, V47, V64). Reachable from phone and desktop and often through Slack, WhatsApp or Telegram.
- **Identity and memory you can edit:** soul/persona and memory files (V15 Muse shows them in a panel; V119 Hermes keeps user, memory and soul files; V191 uses soul.md and user.md).
- **Routines:** actions on a schedule or event, such as a weekday 6-7 a.m. brief, a form webhook, a Slack message (V47, V64, V28). Muse shows a Schedule page with a 30-minute **heartbeat** that checks docs and email (V15); Clawdbot uses a heartbeat about every 30 minutes (V191).
- **Connectors:** Gmail, Calendar, Slack, GitHub, ClickUp, Google Docs, accounts connected once and shared across agents (V64, V47).
- **Approvals, notifications and logs** so you see what it did (V47, V15 Approvals tab).
- **Skills from demos:** record a task and the bot turns it into a reusable skill (V47, V59, V64).
- **Chief-of-staff + specialists**, with shared vs private memory (V59).
- **Model routing:** Grok Bot picks the model per task with no user control (V8).
- **Own inbox for the bot:** an AgentMail inbox that wakes the bot via webhook (V29).

## 2. Costs and limits seen today (numbers are from the videos; check current prices)
- Grok Bot: subscription tiers about $20, $100 or $200 a month with weekly usage caps; group chats and multi-agent delegation use the cap faster (V47). 
- Muse: a free tier of up to 100 million tokens per week *(Nate's figure)*; Dots needs a paid ChatGPT subscription (V15).
- Hermes: managed from about $6/month; a VPS plan roughly $100/year *(his figures)* (V50, V119).
- Claude Code remote control needs Pro (about $20) or Max ($100-$200); the computer must stay on and the terminal open (V180).
- Claude managed agents: about 8 cents per live session hour plus tokens; no native cron at the time; $5 API credit to start (V147).
- Clawdbot-style bots: Nate estimated about $50/month then said the real cost was higher; about a quarter billion tokens in three days (about $223) *(his claim)*; about $80 in a day of heavy testing (V191, V192).

## 3. Risks learned the hard way
- **Security:** Clawdbot defaults were unsafe when exposed online; Nate cites about 900 exposed servers with no password (V192, citing a tweet). Treat webhook URLs and keys like passwords (V29, V261).
- **Blast radius:** give the bot its **own accounts**, start **read-only**, lock the Telegram bot to your own user ID, keep keys in `.env` (V191, V193, V119).
- **Too much auto-ingested context can cause harm** (V92).
- **Subscription terms:** Nate says Anthropic has been banning accounts for using a Max plan with a third-party bot like Clawdbot, so he used API keys instead (V191, *his claim*, not verified here). Check the real terms for Claude duet and for any third-party tool before connecting a subscription.
- **Always-on = always spending:** heartbeats, group chats and many agents burn usage fast (V47, V191).

## 4. Income plays this unlocks (inference; test each with real buyers)
1. **Personal assistant setup for busy operators:** configure persona, memory, connectors, routines and approvals. Price signals: $1,650 inbox assistant (V202) and $6,000 Slack-based team assistant (V242), both *claims*; V48 mentions about $5,000 to set up a team and about $100/hour trials *(claims)*.
2. **Role packs:** a chief-of-staff and 2-3 specialist agents pre-built for one profession (real estate, recruiting, coaching, local services).
3. **Routine and skill libraries per niche** (morning brief, inbox sweep, weekly report, follow-up reminders). Sell setup plus tuning, not only the files (V179 warns against relying on a skills marketplace).
4. **Safety and permission reviews** for people who want assistants on their email and calendar (V192, V261).
5. **Knowledge-base ("second brain") builds** that the assistant draws on (V36, V81, V92, V97).
6. **Training and handover sessions** for founders and small teams (V48, V224).
7. **Cost caps and monitoring** for people who run assistants all day (V290, V8).

## 5. What to build and learn now so you can move on day one
- [ ] **Write the four context files** an always-on assistant needs: who you are, your business, your rules/approvals, your tools (the "AIOS" in V71, V97, V110, V127).
- [ ] **Build a "grill me" interview skill** that extracts a client's context (V59, V50, V3).
- [ ] **Practice routines today** with Claude Code scheduled tasks and remote control (V103, V162, V180) or a small VPS/Telegram bot (V50, V119).
- [ ] **Build 3 demo assistants:** morning brief, inbox triage with approval, meeting-notes-to-tasks. Record 2-minute demos.
- [ ] **Learn the permission model:** read-only first, separate accounts, approval gates, action logs (V191-V193, V18).
- [ ] **Track cost per task** so you can price a monthly plan (V290).
- [ ] **Write a client setup checklist** (discovery, accounts, connectors, rules, test week, handover) using [AGENT-INCOME-PLAYBOOK.md](AGENT-INCOME-PLAYBOOK.md).

## 6. Fill in on release day (assumption checklist)
| Question | Answer |
|---|---|
| Is it a cloud agent with its own computer, or tied to your device? | |
| Channels supported (Slack, WhatsApp, Telegram, iMessage, email)? | |
| Memory model: editable persona and memory files? shared vs per-agent? | |
| Routines: schedule, events, webhooks? heartbeat? | |
| Connectors and API/MCP access? can you add your own? | |
| Approvals, notifications and logs? | |
| Multi-user or team use? | |
| Pricing, weekly limits, overage? | |
| Terms of service for client work and resale? | |
| Data and privacy (where data lives, retention)? | |
| Can it call other agents / be driven by Claude Code? | |

## 7. Caveat
These are notes from videos about other products. Treat them as a design pattern, not as promises about Claude duet.
