# Nate Herk study notes - batch 01 (videos 1-9)

Paraphrased notes. Source captions were machine-translated into several languages, so tool names are sometimes spelled inconsistently; where a name is uncertain it is flagged. Earnings or result statements are labelled "(Nate's claim)".

## 1. /roast-room: How I Use Claude to Think Like the Top 1%
- **Link:** https://www.youtube.com/watch?v=DSS1Yqb6-qE | **Length:** 15 min | **AI-relevant:** yes
- **What it teaches:**
  - A Claude Code skill ("Roast Room") that runs a decision debate between "advisor" sub-agents. Each advisor is modeled on a well-known business figure and owns one guiding question (e.g. Buffett: effect on cash, risk, long-term value; Hormozi: will people pay, how much, how to close; Wickman: can the business run without the founder).
  - Each advisor is a short markdown agent file in `.claude/agents/`, which points to a larger "brain" folder in the skills directory (rules sheet, books, frameworks, positions, principles, sources, stories, voice). Brains were built from public talks, interviews, posts and books (one example cited: roughly 48 sources / ~500k words).
  - Flow: you give a decision plus 2-3 options and context; the skill picks the best seats; round 1 = written positions and scores; round 2 = advisors rebut each other, with the chair (Claude Code) forcing a devil's-advocate if everyone agrees; round 3 = final votes and a verdict exported as a PDF.
  - Uses sub-agents, not agent teams: Nate says teams cost more and added little in testing.
  - A "new roaster" skill creates additional advisors (demoed with Elon Musk) including agent file, brain files and a cartoon portrait. 7 default seats plus 4 extra (Naval, Cody Sanchez, Sara Blakely, Leila Hormozi) = 11.
  - Main idea: extract proven experts' thinking into reusable agents, treat the output as input to your judgment, not an oracle. A local visual UI is optional; the skill works without it.
- **Tools / prices / numbers:**
  - Claude Code with sub-agents, markdown agent files, a localhost visual layer; Glydo (sponsored desktop tool, coordinates chats across coding agents) offered with 1 month free via his link; Fish Audio "Drama 3" voice model mid-roll sponsor (emotion tags, word-level timestamps, MCP server, n8n node; no price given).
  - Demo scored the winning option 7.9/10; he says he picked Salt Lake City for a 2027 live event based on the council.
- **Skills it demonstrates:** sub-agent orchestration, persona/agent design, context engineering (brain files), skill authoring, decision frameworks.
- **Money angle:** Package "AI advisory board" agents for founders or small teams as a paid decision-support/consulting deliverable (PDF verdict per decision). Build niche councils (marketing, legal, security) for a client's industry. No prices stated.
- **Sponsor / affiliate / upsell:** Glydo (affiliate-style link, 1 month free), Fish Audio (sponsored segment); the repo is free inside his free School community.

## 2. I Tried 100+ AI Tools. These 7 Are the Best
- **Link:** https://www.youtube.com/watch?v=hgLI491ajG0 | **Length:** 10 min | **AI-relevant:** yes
- **What it teaches:**
  - His 7 daily tools: (1) Claude Code and Codex as the "operating system" of his business (second brain, projects, skills, meeting transcripts); he pays for both and rotates by usage limits. Codex judged stronger for computer/browser use, Claude Code better for ideation. Setup should let you switch easily between them.
  - (2) OpenRouter: one account for 500+ models from 80+ providers; fallbacks if a model fails, a separate API key per automation to track cost per automation, cheap fast model for classification plus smarter model for replies.
  - (3) A VPS (Hostinger) for always-on agents (Hermes, OpenClaw, Claude Code experiments); one-click templates.
  - (4) Grok Bot: cloud computer with browser, file system, terminal, connectors, scheduled routines and webhooks; phone app. Examples: auto-post call transcripts to his community, post new videos to communities, AI-news digests. Compared to a lower-setup "OpenClaw in your pocket".
  - (5) Glydo: voice dictation plus a "command mode" that can search, summarize and drive custom MCP servers; stored locally.
  - (6) key.ai: pay-per-use gateway to image/video models (Veo, Kling, Nano Banana, GPT image and others) for carousels, thumbnails, reels.
  - (7) trigger.dev: runs TypeScript code on schedule/webhook without managing a server; Claude Code writes, deploys and tests the script. Use for deterministic jobs (document processing, syncing two tools).
  - Insight: building small custom apps with Claude Code can replace monthly SaaS (he cites replacing Gamma, Poppy and building a Loom-like tool).
- **Tools / prices / numbers:** OpenRouter (500+ models, 80+ providers); trigger.dev free plan includes $5/month credit; key.ai and trigger.dev are usage-based; Hostinger Black Friday sale mentioned; Claude Code ~90% of his daily workflow (Nate's claim). No other prices given.
- **Skills it demonstrates:** tool selection, model routing/fallbacks, always-on agent hosting, scheduled automations, code-based automation, cost tracking per workflow.
- **Money angle:** Use OpenRouter-style routing with per-client keys so you can bill AI cost back to clients; sell deterministic trigger.dev-style automations (doc processing, data sync) to small businesses; offer SOP-aware Claude Code assistants so a team can query SOPs.
- **Sponsor / affiliate / upsell:** Hostinger (sponsored VPS segment, link hostinger.com/natehurtsvps per captions), Glydo (he states he is a partner), free "AI OS kit" (Herc loop: context, connections, capabilities, cadence; 6 skills), his free and paid ("Plus") communities.

## 3. Matt Pocock: The Most Valuable Skill to Learn in the Age of AI
- **Link:** https://www.youtube.com/watch?v=Z8lf5oWKfj0 | **Length:** 45 min | **AI-relevant:** yes
- **What it teaches:**
  - Interview with Matt Pocock (TypeScript educator, skills author). Central thesis: the top skill is communication; agents cannot know what you care about, so you must say it, repeatedly. A gap always remains however smart the model.
  - The environment the agent works in (clean codebase, good tests, checks) drives output quality ("garbage in, garbage out"). Imagine managing 100 human programmers and raise the floor: old software-engineering books on testing and feedback loops apply directly.
  - His "grill me" skill makes the agent interview you relentlessly to expose unknown unknowns (security, deployment, edge cases); "grill with docs" additionally builds a shared domain vocabulary (domain-driven design's ubiquitous language) so code, UI and client use the same terms.
  - His "teach" skill pulls high-quality primary sources with citations; he treats it as an intro, then reads the originals because hallucinations still occur.
  - He abandoned spec-driven development after months because code quality degraded; now treats code as the agent's environment and makes it easy to change safely.
  - Practical habits: use medium or even low effort with the latest Opus model (he thinks most people over-use high effort); improve the environment (e.g. letting the agent drive the app in a browser and take screenshots) rather than chasing models; "climb the trust ladder" - learn the brake before the accelerator, watch the agent closely, then add agents, skills and data connections.
  - Opportunity he sees: taking agents and defining/reusing processes for knowledge work inside organisations, plus teaching, since every org adopts differently and real-world work is harder to verify than code.
- **Tools / prices / numbers:** Claude Code with Opus 5.5 at medium effort; he says he runs about 4 agents in parallel and 200-300 commits/day vs ~20 before (Matt's claim); sponsor spot for Hostinger KVM 2 (2 vCPU, 8 GB RAM, 100 GB storage), Claude Code template, snapshots/weekly backups, extra 10% off annual plans with code nateherk (no base price stated).
- **Skills it demonstrates:** prompt/context engineering, spec and interview skills, agent supervision, domain modeling, evaluation habits, positioning as an AI consultant.
- **Money angle:** Consulting angle is documenting and agentifying a company's knowledge-work processes; advice for standing out: show you understand the client's business, ship working prototypes fast, and consider charging for the value rather than hours (Matt: if a job takes one day, "charge for five"). Teaching and training teams is flagged as a large opportunity. No price points.
- **Sponsor / affiliate / upsell:** Hostinger KVM 2 VPS (code nateherk, link in description); free AI OS kit (Herc loop); Matt's own newsletter and skills repo (mentioned as places to start).

## 4. AI Agents Just Became Multiplayer. Here's How to Build Them.
- **Link:** https://www.youtube.com/watch?v=KZiF2J83zaY | **Length:** 22 min | **AI-relevant:** yes
- **What it teaches:**
  - Concept of "multiplayer AI": instead of each team member running a private AI OS, a Slack-like workspace with channels where humans and agents (including each person's Claude Code and Codex subscriptions) share apps, automations, files and memory. The tool name is transcribed inconsistently in the captions (Kylan/Kylon/Kilon); treat the exact spelling as unverified.
  - Setup walk-through: create a workspace, invite teammates (billing is per workspace, not per member), onboard the first agent by feeding it a markdown brief of you and your company exported from your own AI OS, connect tools via OAuth (Gmail, Calendar, GitHub, Notion) or custom API keys.
  - Agent types: hosted agents on the vendor's cloud with intelligence tiers (fast / pro / max; max reportedly uses Opus 5.5 in the back end), or "local" agents that attach your own Claude Code or Codex via a pasted connect prompt. Local ones only respond while your computer is on, unless you host them on an always-on VPS or Mac mini.
  - Use cases: Instagram carousel pipeline running every 6 hours (research, ideation, creation, posting, analytics); Kanban app built in-channel; end-of-day check-in agent that reconciles ClickUp tasks the team forgot to mark done; stalled-handoff alerts.
  - Adoption advice: convert one business unit at a time, start with small immediate wins, explain your pain points to the agent rather than rebuilding every tool.
  - Nate's verdict: nothing here was impossible before, but it is far simpler than hand-building polling apps and GitHub deployments; feels like Grok Bot with teammates.
- **Tools / prices / numbers:** credit-based plan (monthly credits consumed by messages; usage visible per person and per room); connected Claude Code/Codex subscriptions do not consume credits; Gemini, Hermes and Grok-build agents said to be coming. No dollar prices stated. Nate says he initially had pricing objections.
- **Skills it demonstrates:** multi-agent collaboration design, AI OS onboarding, team adoption strategy, scheduled agent automations, connector setup.
- **Money angle:** Rolling out shared agent workspaces for small teams is a service: map one department's workflow, build the channel apps/automations, train the team. Productized "team AI onboarding" would be the offer; no prices stated.
- **Sponsor / affiliate / upsell:** Disclosed that the tool's company contacted Nate for this video (sponsored/outreach); mentions his AI Automation Society community and an upcoming show format.

## 5. I Tested the Viral Reverse Engineer Anything Skill. What You Need to Know.
- **Link:** https://www.youtube.com/watch?v=rL5tw6h78zo | **Length:** 15 min | **AI-relevant:** yes
- **What it teaches:**
  - "Reverse-engineer-anything" (REA) is a popular GitHub repo (Nate cites ~192k stars) giving coding agents a structured way to study an existing app/feature and rebuild the behavior. Nate's point: the idea is old - show the agent the finished output and let it work backwards, which acts like a very specific PRD.
  - Examples: a skill that edits Instagram reels in his style, built by having Claude analyze ~30 of his best reels frame by frame; a Loom-like local screen recorder (functionality cloned, not the UI); a tool inspired by an Instagram analytics app; an eval studio inspired by Langfuse.
  - The five-step process: pick one specific feature (not the whole app); route by build/tech stack; produce a short summary from a huge raw analysis (the Loom analysis was over 1 GB); tag every claim as seen, inferred, or unknown; rebuild and test with real test cases.
  - Rule: never copy exact code or assets, and never hack into servers or private codebases; only analyze what is already accessible locally or via public APIs.
  - Applies beyond software: for a Friday report skill, show five good examples; study someone who did it well and adapt it.
  - Observation: an agent using the repo finished slower but with better results than one without it. Rebuilding with a cheaper model (Sonnet 5.5) after Opus did the analysis can lower cost.
- **Tools / prices / numbers:** REA repo (~192k stars at recording); Claude Opus 5.5 and Sonnet 5.5; Scrollcraft (his free web-design skill). No prices.
- **Skills it demonstrates:** reverse engineering as prompting, skill creation from examples, spec-by-example, evidence tagging (seen/inferred/unknown), iterative build-test loops.
- **Money angle:** Build custom internal replacements for SaaS a small client overpays for (functionality, not copied UI); create style-matching skills (e.g. reel editing) for content clients. Mind legal limits on copying. No prices.
- **Sponsor / affiliate / upsell:** Free Scrollcraft skill and a guide document given away via his free School community; links in description.

## 6. This ONE Claude Skill Helps You Think Clearer Than 99% of People
- **Link:** https://www.youtube.com/watch?v=nRXHWckVxoM | **Length:** 15 min | **AI-relevant:** yes
- **What it teaches:**
  - A walk-through of the same Roast Room advisory-council skill as video 1, with a different demo (choosing between four options for a June 2027 in-person event) and more architecture detail.
  - Chair (Claude Code) plus 7 sub-agent advisors; three rounds (positions, cross-debate, votes), outputs a PDF verdict; sessions are saved to disk so you can replay them.
  - Each advisor "brain" is a set of markdown files (decision rules, frameworks, positions, stories, voice, sources) distilled from public content; example brain cited at ~124 sources and ~1.3M words. Swap in any new expert by asking Claude to build one the same way.
  - How to ask a good question: state the decision, give 2-3 options, include real numbers (revenue, team size), constraints (deadline, budget), what success looks like, and which option you lean toward and why (since models tend to agree with you).
  - Broader principle: outsource thinking but not understanding; build specialist agents (e.g. security + CTO) that debate and still review their recommendations yourself.
  - Council seats are chosen per question; some questions only need 2-4 advisors.
- **Tools / prices / numbers:** Claude Code sub-agents; verdict example gave a recommendation with tier price $3,000, capped at 120 seats and a commitment gate of 50 members paying $150,000 by Jan 15 (this is his event example, not a general benchmark). Sub-agents chosen over agent teams for cost and distinct voices.
- **Skills it demonstrates:** sub-agent design, persona/knowledge distillation, prompt structure for decisions, AI OS context integration.
- **Money angle:** Same as video 1: sell "decision council" deliverables or custom expert-panels per niche; also the free SOP he offers for landing first AI-automation clients (see below). No prices.
- **Sponsor / affiliate / upsell:** Free School community (repo under "AI skills"); free SOP for getting first AI automation clients (one-sentence offer, why the first client should cost money, a 5-minute proof video, what to do without case studies).

## 7. I Tried 100+ Github Repos for Claude. These 6 Are the Best
- **Link:** https://www.youtube.com/watch?v=HhZdNYI4pJs | **Length:** 11 min | **AI-relevant:** yes
- **What it teaches:** (Title says 6, the spoken video covers 10 repos plus a token-saver section.)
  - Hyperframes (HeyGen): describe a video in natural language, Claude writes HTML/animation and renders a real MP4 locally; open source, no render fee. Sell as monthly short-form clip packages.
  - Google Workspace CLI: lets Claude Code/Codex work across Drive, Gmail, Calendar, Docs, Sheets, Slides; 40+ skills; needs a Google Cloud project for login.
  - Apify MCP server: connects to thousands of cloud scrapers (Instagram, TikTok, Amazon...); example lead list of Chicago bakeries without websites. Mentions Firecrawl as an alternative.
  - Scrollcraft (Nate's own, free): scroll-driven website design rules plus a checker that screenshots and fixes layout.
  - Humanizer: edits text to remove "AI tells" using the Wikipedia AI-writing signs guide.
  - Agent Skills by Addy Osmani: /spec, /plan, /build commands that move planning into files so long sessions can restart; asks about edge cases (double booking, refunds, time zones). Matt Pocock's skills named as a bonus.
  - Expo official skills for mobile apps (needs Apple Developer account at $99/year for TestFlight/App Store; tip: call the skills by name).
  - Supabase and Stripe official skills (install only the "Stripe best practices" skill, use read-only Supabase connector, test as a normal user).
  - Playwright CLI (Microsoft) for real-browser testing, more token-efficient than an MCP; Claude Security plugin (Anthropic) for multi-agent vulnerability search.
  - Open SEO for keyword/ranking/backlink data (free credits run out quickly; data stored on their server by default).
  - Token-saver tests: JetBrains reportedly measured Caveman ~8.5% output-token savings vs 65% claimed, RTK ~none, Ponytail ~10% per task; Codeburn tracks token spend. He suggests postponing Claude Mem and Context Mode (privacy/usage bug reasons given).
- **Tools / prices / numbers:** Apify free tier $5 credit/month, pay per result; Apple Developer $99/year; others free/open source per Nate.
- **Skills it demonstrates:** tool/stack selection, web scraping for lead gen, SEO audits, video automation, secure app building, QA testing, token-cost auditing.
- **Money angle:** Nate states clients pay for solutions, not repos: examples include monthly short-form video packages (e.g. gym needing 20 captioned clips a month), automating Google-based reports/invoices, scraped lead lists, custom scroll-driven sites, mobile apps for small businesses, SEO audit retainers, and building sites for businesses without one then pitching them. No prices.
- **Sponsor / affiliate / upsell:** Says the video is not sponsored; promotes his own Scrollcraft and links in description.

## 8. Grok Bot Just Got 2 Massive Upgrades. Do These Things Now.
- **Link:** https://www.youtube.com/watch?v=MgvwZaDPCs4 | **Length:** 9 min | **AI-relevant:** yes
- **What it teaches:**
  - Upgrade 1: per Elon Musk's post as Nate relays it, Grok Bot will route each task to the best back-end model (named: Claude Opus 5.5, Midjourney for images, Suno for music, other APIs); simple tasks to a small fast model (a future "Grok 4.8"), complex ones to a big model. Nate noted there is no visibility yet into which model or effort level is used and some users want to opt out.
  - Upgrade 2: Grok Bot gained built-in search/read/monitor of X, free to the user. Nate moved his routines off the paid X developer API; a bot told him he has 1,000 free daily reads resetting about 7 pm Central. He estimated old API cost at roughly $5/week (Nate's estimate).
  - Design implication: split big multi-step skills so cheap steps can go to a fast model and reasoning/design steps to a stronger one; wants per-skill model control. Skills behave differently across models.
  - Hack: install Claude Code or Codex inside a Grok Bot's cloud computer terminal, authenticate with your own subscription, clone your AI OS repo and move the .env file. Result: an always-on Claude Code in your pocket usable by any of your bots. He prefers API keys over desktop plugins for portability.
  - Compares Grok Bot favorably to OpenAI's "Dots" and Meta's "Muse" (covered in video 15 of the playlist).
- **Tools / prices / numbers:** X API reads normally paid per tweet; free built-in X search with 1,000 reads/day; subscription routes mentioned (Cursor, SpaceX, Super Grok) for Grok Bot; models: Opus 5.5, Grok 4.8 (upcoming). No other prices.
- **Skills it demonstrates:** agent platform operations, model-routing awareness, cost reduction, multi-bot orchestration, remote agent environment setup.
- **Money angle:** Cheaper X monitoring/social listening bots for clients; managed always-on agent setup (cloud computer plus client's own subscription) as a service. No prices.
- **Sponsor / affiliate / upsell:** Free AI OS kit (Herc loop) promoted; otherwise none.

## 9. Anthropic Engineers Just 10x'd Everyone's Claude Code
- **Link:** https://www.youtube.com/watch?v=oz2CwrPV2Rg | **Length:** 12 min | **AI-relevant:** yes
- **What it teaches:**
  - Nate cites an Anthropic engineer's article on new context-engineering rules for the latest (5th-gen) Claude models: Anthropic removed over 80% of Claude Code's system prompt with no measured quality drop (Anthropic's claim as relayed). Boris Cherny's earlier advice: every ~6 months consider deleting your skills.
  - Principle: use the minimum context that gives the best result ("minimal" is not "short"); stale rules from older models become restrictive. Define the desired output, the reason, and constraints, then leave the model room.
  - Evidence he cites: a 2025 paper showing 13.9%-85% performance drop as input grows (older models); Anthropic's tool-search style lazy loading of MCP tool definitions cut token use by 85% and raised an MCP eval from 49% to 74% (Opus 4) and 79.5% to 88.1% (Opus 4.5).
  - His experiment: ran the same task with and without his skills/CLAUDE.md; the bare version structured the content better, the full version had better branding. Fix: keep context (voice, goals, audience, business), drop over-prescriptive procedure, load procedures only when needed.
  - Use `/doctor` in Claude Code to audit setup: lists skills with token cost and usage counts, flags 18 unused ones, finds duplicated instructions (~2,250 characters / ~563 tokens to trim), stray CLAUDE.md files in other folders (~2,000 tokens), and 2 broken skills (bad filename, metadata format error), then offers to fix.
  - Workflow audit prompt: ask Claude to inspect the repo and propose minimal changes using existing files, without editing yet. Repeat monthly or quarterly and after each model change; optionally schedule it as a desktop scheduled task.
- **Tools / prices / numbers:** Claude Code `/doctor`; numbers above (skill headers ~100 tokens each; 252 runs and 223 transcripts analyzed in his audit; 3 of 25 video folders had sources.md).
- **Skills it demonstrates:** context engineering, skill pruning/auditing, prompt design for new models, AI OS maintenance, cost/token awareness.
- **Money angle:** Offer "AI setup audits": review a client's CLAUDE.md, skills and prompts, cut waste, document it. Per-client isolated agent workspaces are mentioned via the sponsor. No prices.
- **Sponsor / affiliate / upsell:** HyperAgent (sponsored segment: per-client workspaces for agent agencies, role-based access); free School community; free AI OS kit.

## Batch takeaways
- Highest-value skill across the batch is context/communication engineering: interview-style prompting (grill-me), minimal-but-sufficient context, periodic `/doctor` and skill audits when models change, and defining success by example (reverse engineering a good output).
- Sub-agent "councils" built from distilled expert brains (markdown agent file + brain folder) are a cheap, repeatable pattern; sub-agents beat agent teams on cost and distinctness in Nate's tests. Sellable as an advisory deliverable.
- Money ideas stated or implied (no price points given): monthly short-form video packages (Hyperframes), scraped lead lists (Apify), custom sites and apps for businesses without them, Google-Workspace report/invoice automations, SEO audit retainers, AI setup audits, rolling out shared team agent workspaces. Nate repeatedly stresses selling the solution around free tools, and his first-client SOP says the first client should pay.
- Cost control matters for any production agent: per-automation API keys via OpenRouter, deterministic code (trigger.dev) for non-agentic jobs, route cheap vs reasoning steps to different models, track tokens (Codeburn), and beware token-saver repos whose claimed savings were much lower in JetBrains testing.
- For an always-on personal agent bot (Grok Bot / Meta Muse style) for Claude: the recipe in videos 2, 4 and 8 is a cloud computer or VPS with terminal, files, browser, schedules/webhooks and chat connectors, with Claude Code installed and authenticated on it, the AI OS repo cloned and secrets moved via .env.
- Design points for such a bot: scheduled routines and webhook triggers, multiple named bots that message each other, skills split so each step can use the right model, visibility of which model/effort ran, per-room or per-person cost tracking, and a rule to keep local-subscription agents available by hosting them on an always-on machine.
- Trust and safety habits to copy: climb the trust ladder, treat model teaching as an intro then read primary sources, tag claims seen/inferred/unknown, never copy proprietary code or hack servers, install only the narrow skills you need (e.g. Stripe best practices).
- Caveats: many numbers are Nate's or third-party claims as relayed, tool names in some captions are garbled, and several products referenced (model versions, Grok Bot features) change quickly, so verify before building a business on them.
