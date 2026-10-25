# Nate Herk: all 368 videos, oldest to newest, with what is viable for making money

One-file recap of every video on youtube.com/@nateherk, **oldest first**. The channel page shows no dates, so the order is the channel list reversed (YouTube lists newest first). `List #` is the video's number in [video-index.md](video-index.md) and in its note filename (1 = newest, 368 = oldest).

**Money line labels**
- **Viable offer (price signal):** the video describes something you could sell and gives a price, percentage, retainer or fee structure. Prices are *claims* from the video, not verified.
- **Possible angle:** a plausible way to earn, but no price (or no buyer) is given. Some of these are my inferences, as marked in the notes.
- **Skill-builder:** no direct money angle; learn it to build the other things better.

Limits: work-rights, tax and legal rules apply ([../RISKS-AND-LIMITS.md](../RISKS-AND-LIMITS.md)). Ranked ideas: [../INCOME-IDEAS.md](../INCOME-IDEAS.md).

Totals: Viable offer 38, Possible angle 159, Skill-builder 171 (of 368).

## The short version: what is viable across the channel
1. **One small-business pain, one automation, one retainer** (inbox triage, lead follow-up, document intake, onboarding), priced on value. Claimed first builds are about $1,200 to $2,600, a team assistant $6,000. Appears throughout Phases 1 and 2.
2. **Document Q&A (RAG) bots and voice receptionists** for local service businesses. Mostly Phase 1.
3. **Done-for-you assistants** (inbox, calendar, Slack or Telegram) with approval steps. Phases 1 to 3.
4. **Selling the setup of AI operating systems and always-on bots** to founders and teams (Grok Bot, Hermes, Claude Code OS). Mostly Phases 2 and 3.
5. **Agent QA and eval audits, and cost or model-routing audits.** Newer and unproven.
6. **Creative production** (websites, video, ad creative) as a portfolio-led offer; prices are rarely stated.
7. **Not recommended as income plans:** faceless AI channels, AI trading bots, and scraping or cold email without checking the rules.


## Phase 1: n8n and no-code agents (oldest)

### 1. How I Wish Someone Explained AI Agents To Me (as a beginner)
[Watch](https://www.youtube.com/watch?v=w4qtnXRd8nU) · 12 min · List #368 · [note](notes/368-w4qtnXRd8nU.md)
- **Recap:** Definition: an AI agent is an LLM "brain" that reasons, follows instructions, and uses the tools you give it (calendar, CRM, Drive, Slack, etc.) to complete a task. Difference from traditional automation: rule-based flows break on decisions that need judgment, while agents can reason over messy input.
- **Money use (Possible angle (no price given)):** He says agents can help people "make a ton of money" but gives no specific product. Practical angle: sell agent builds to businesses in the four areas he lists. No price points stated.

### 2. How to Create an AI Email Agent with n8n (No Code, Step-by-Step Tutorial)
[Watch](https://www.youtube.com/watch?v=YFrej2oSldo) · 29 min · List #367 · [note](notes/367-YFrej2oSldo.md)
- **Recap:** Workflow 1: load contacts from a Google Doc into a Pinecone index (insert mode, namespace "context", token splitter at 200 characters). Workflow 2: a Gmail "send a message" tool. An LLM step parses the agent's query into to, subject, and body; wrap the input in `JSON.stringify` so the fields arrive as strings;
- **Money use (Possible angle):** Email assistants for executives or small teams that look up a contact and send mail on request; price per seat or per setup not stated. He says future versions could add calendar and Drive tools.

### 3. How to Create an RAG Chatbot AI Agent with n8n (No Code, Step-by-Step Tutorial)
[Watch](https://www.youtube.com/watch?v=6w0MshwAqBQ) · 17 min · List #366 · [note](notes/366-6w0MshwAqBQ.md)
- **Recap:** Workflow 1 (ingest): manual trigger, Google Drive download of a PDF as binary, then insert into a Pinecone index under a namespace. Set the default data loader to binary; with the default JSON setting nothing reached Pinecone (his mistake, shown on screen). Use a recursive character text splitter with a large chunk size for a long PDF; overlap left at zero.
- **Money use (Possible angle (no price given)):** Document Q&A bots for businesses with manuals, policies, or product docs. Build the ingestion once, then sell the chat front end to the client. No price points stated.

### 4. Build your first NO CODE AI Agent in n8n (for beginners)
[Watch](https://www.youtube.com/watch?v=otUBuV1foLY) · 20 min · List #365 · [note](notes/365-otUBuV1foLY.md)
- **Recap:** Build a tool as its own workflow: a "when called by another workflow" trigger, a Set node with a city field, an OpenWeatherMap current-weather node, then an LLM node that turns the raw JSON… Finish each tool with a Set node named `response`, which is the field the agent reads back.
- **Money use (Possible angle (no price given)):** Beginner-level "tool plus agent" builds are the base for client work (a weather or data lookup inside a chatbot or assistant). He does not state a product or price. The lesson is a starting point for selling custom agents.

### 5. *LIVE BUILD* Personalized Outreach AI Agent in n8n (No Code)
[Watch](https://www.youtube.com/watch?v=fz1RduhHeks) · 24 min · List #364 · [note](notes/364-fz1RduhHeks.md)
- **Recap:** Lead qualification: read leads from a Google Sheet (filled by a Google Form), send each lead to an LLM with qualification rules, and get back "qualified" or "not qualified" plus reasoning. Rules are written as a system prompt and the model replies in JSON; wrap the output in `JSON.parse` so later nodes can read fields.
- **Money use (Possible angle (no price given)):** Sell lead qualification plus outreach drafting to B2B sales teams or agencies, with the Sheet as the interface. Could be packaged as a "sales pre-qualifier." He doesn't state a price.

### 6. *LIVE BUILD* Inbox Management AI Agent with n8n (NO CODE, Step-by-Step Tutorial)
[Watch](https://www.youtube.com/watch?v=x1tam0Fhymc) · 16 min · List #363 · [note](notes/363-x1tam0Fhymc.md)
- **Recap:** Gmail trigger ("message received") that fires on each new email while the workflow is active. A text classifier node sorts each email body into one of four categories, each defined by a plain-language description plus keywords (drafted with ChatGPT).
- **Money use (Possible angle):** Inbox triage setup for busy professionals, executives, or small businesses; price per setup or monthly upkeep. Nate frames it as a time-saver, not a sold product. No price points stated.

### 7. How to Build a Google Scraping AI Agent with n8n (Step By Step Tutorial)
[Watch](https://www.youtube.com/watch?v=R36bpNPPIMs) · 20 min · List #362 · [note](notes/362-R36bpNPPIMs.md)
- **Recap:** Build a tool workflow: a "when called by another workflow" trigger with parameters (job title, company, industry, location), an HTTP Request to a Google search URL filtered to… Add a `user-agent` header to the HTTP request, since Google may block requests without one; a chatbot helped write the header and parsing code.
- **Money use (Possible angle):** Prospect-list building for sales teams or recruiters, delivered as a sheet on request. He says the basic version returns only about 10 results per query, so scaling needs a paid search API. No price points stated.

### 8. How to Build a Client Onboarding AI Agent with n8n (Step-by-Step Tutorial, No Code)
[Watch](https://www.youtube.com/watch?v=Wpwbm3zCymk) · 21 min · List #361 · [note](notes/361-Wpwbm3zCymk.md)
- **Recap:** Start with an n8n form trigger that collects client details (name, email, industry, goal, notes); send the form link to new clients. Agent 1 (conversational, no tools) writes a personalized welcome email from the form data; its system prompt forbids template variables and fixes the sign-off.
- **Money use (Possible angle (no price given)):** Agencies and consultants can sell onboarding automation: the welcome email, the client summary and CRM entry, set up for each new client. Price points not stated.

### 9. I Built a Personal Assistant AI Agent with No Code in n8n
[Watch](https://www.youtube.com/watch?v=omw1MEvMCo0) · 24 min · List #360 · [note](notes/360-omw1MEvMCo0.md)
- **Recap:** A personal assistant agent that you message from Telegram; the agent picks a tool and replies with the result. Each tool is its own n8n workflow called by the agent (get emails, send email, get calendar, set calendar event, update database, summarize database), and each returns a `response` field so…
- **Money use (Possible angle (no price given)):** Build a personal or small-team assistant for busy professionals or operators (inbox summaries, calendar summaries, CRM updates) and sell it as a setup plus monthly service. No price points stated.

### 10. Build a No-Code AI Chatbot (Step-by-Step Tutorial)
[Watch](https://www.youtube.com/watch?v=B15e_9_fCyE) · 19 min · List #359 · [note](notes/359-B15e_9_fCyE.md)
- **Recap:** Build a website chatbot in a no-code builder: crawl a site URL and upload an FAQ PDF into the knowledge base. Chain blocks in a flow: send a message, capture a form (name, email) into variables, capture the visitor's question, generate an AI answer from the knowledge base.
- **Money use (Possible angle (no price given)):** Sell chatbot setup to small businesses for their websites to answer FAQs and capture leads; add a lead-capture form that writes to a sheet. The video says lead-gen bots can store contact details but gives no pricing.

### 11. I Built an AI Agent that Automated my Inbox with n8n (No Code)
[Watch](https://www.youtube.com/watch?v=JUx2ZfNfD64) · 20 min · List #358 · [note](notes/358-JUx2ZfNfD64.md)
- **Recap:** Gmail trigger, then a text classifier (LLM) sorts each email into one of four labels (e.g., high priority, customer support, promotional, finance/billing). Each label routes to its own branch: high priority creates a Gmail draft (not sent) plus a Telegram alert; customer support drafts and sends a reply in the thread;
- **Money use (Possible angle (no price given)):** Inbox triage and auto-reply setup for busy operators, executives, or small businesses. Sell as a done-for-you build with routing rules per business. No price points stated.

### 12. Step-By-Step: Add 100+ Files to Pinecone for RAG AI Agent with n8n
[Watch](https://www.youtube.com/watch?v=iT9xpiUwVbI) · 14 min · List #357 · [note](notes/357-iT9xpiUwVbI.md)
- **Recap:** Ingest many documents into a vector database without manual runs: list a Drive folder, then download each file's content. The folder search returns only IDs and names; a second node downloads the actual binary content by ID. Loop in batches of one file, embed each file into Pinecone, and loop back until every file is done.
- **Money use (Possible angle (no price given)):** Internal knowledge-base agents for small businesses (staff Q&A over menus, policies, SOPs). Set up the ingestion pipeline once, then charge for ongoing updates. No price points stated.

### 13. n8n Masterclass: Build AI Agents & Automate Workflows (Beginner to Pro)
[Watch](https://www.youtube.com/watch?v=ZHH3sr234zY) · 91 min · List #356 · [note](notes/356-ZHH3sr234zY.md)
- **Recap:** - n8n basics: workflows (recipes), nodes (steps), and executions (each run); triggers, action, data transformation, and logic nodes (If, Switch, Wait). Self-hosted vs. cloud n8n: self-hosting gives data control but needs server upkeep; cloud is managed and subscription-based.
- **Money use (Skill-builder):** No direct money angle in the video. He frames n8n skills as a way to automate work and says savings or income depend on the user; no product or price points given. Skill to build: workflow building, RAG pipeline, agent prompting, tool design, HTTP requests, error handling.

### 14. Scrape Google for LinkedIn Profiles in Seconds with n8n
[Watch](https://www.youtube.com/watch?v=gvldzucAoBo) · 15 min · List #355 · [note](notes/355-gvldzucAoBo.md)
- **Recap:** A Google search is just an HTTP request; the profile URLs are parsed out of the returned HTML by a code node. Pagination: add a `start` parameter (0, 10, 20, ...) and loop over a list of start values so each loop fetches the next page of results.
- **Money use (Possible angle (no price given)):** Lead generation for sales or recruiting teams: a workflow that pulls prospect lists (e.g., CEOs in a given city) on demand. Sell as a lead-gen build to agencies or recruiters. No price points stated.

### 15. Step By Step: Automating Lead Nurturing with No Code in n8n
[Watch](https://www.youtube.com/watch?v=fWtXJswvUcA) · 23 min · List #354 · [note](notes/354-fWtXJswvUcA.md)
- **Recap:** Trigger: a Google Sheets "row added" node (polls every minute). The sheet is fed by a Google Form lead capture. Wait node before sending, so the reply feels human. The demo uses 1 second, but Nate suggests minutes.
- **Money use (Possible angle (no price given)):** sell lead capture and automated follow-up to small businesses, for example a website form that replies and tags leads. No price is given. Nate's own consult form is the model he shows.

### 16. n8n AI Agent Masterclass / AI Nodes Made Simple
[Watch](https://www.youtube.com/watch?v=EzS2PIjyeQQ) · 51 min · List #353 · [note](notes/353-EzS2PIjyeQQ.md)
- **Recap:** Six n8n agent types: Tools (Nate's default), Conversational (adds chat memory), Plan and Execute, ReAct, SQL, and OpenAI Functions. Variables: drag fields from the schema panel as `$json.field`. Names are case-sensitive, and a red expression means it does not resolve.
- **Money use (Skill-builder):** No direct money angle in the video. Skill to build: n8n agent configuration, expression syntax, output parsing, memory and logs debugging.

### 17. AI Personal Assistant 2.0 / This Agent Calls Other Agents (No Code) in n8n
[Watch](https://www.youtube.com/watch?v=9G-5SiShBKM) · 27 min · List #352 · [note](notes/352-9G-5SiShBKM.md)
- **Recap:** Architecture: one Telegram-triggered main agent routes to four sub-agents (email, calendar, research, projects). Each sub-agent is its own n8n workflow, attached as a tool. Each sub-agent starts with an Execute Workflow trigger and returns its result in a field named `response`.
- **Money use (Skill-builder):** No direct money angle in the video. The demo points to service businesses (for example, an auto shop) using an assistant for staff or customer questions. No pricing is given. Skill to build: multi-agent orchestration, sub-workflow design, error routing, prompt design for tool routing,….

### 18. The Best Way to Give AI Agents Tools in n8n
[Watch](https://www.youtube.com/watch?v=l8NoMgd8lG4) · 19 min · List #351 · [note](notes/351-l8NoMgd8lG4.md)
- **Recap:** Old pattern: the agent passes a query to a sub-workflow, which uses an LLM or code node to split it into fixed fields (send-to, subject, body). Any renamed field breaks the flow.
- **Money use (Skill-builder):** No direct money angle in the video. for the tools. Nate announces a new paid community that offers modules, live calls, and "guaranteed" responses. No price is given. Skill to build: n8n tool design, `$fromAI` parameter mapping, agent prompt basics, live debugging.

### 19. I Scraped, Researched, and Created Outreach for 16,846 Leads using Godmode HQ
[Watch](https://www.youtube.com/watch?v=DiCjeWKgNj0) · 13 min · List #350 · [note](notes/350-DiCjeWKgNj0.md)
- **Recap:** Fill in a go-to-market profile (company, value propositions, booking link). The AI uses it to write outreach that sells your offer. Build a lead list from search criteria: job title, company size, country, and keywords. Preview the count, then enrich rows with email and tech stack.
- **Money use (Possible angle (no price given)):** B2B outbound as a service. Set up lead lists and personalized campaigns for companies that sell to businesses. No price is stated. Cold outreach carries spam-law and deliverability risk, which the video does not address.

### 20. AI Agent Prompting Masterclass: Beginner to Advanced
[Watch](https://www.youtube.com/watch?v=bwrAsnU2P88) · 41 min · List #349 · [note](notes/349-bwrAsnU2P88.md)
- **Recap:** Agent prompts run once with no back-and-forth, so they must be precise up front. The five core parts are background, context, instructions, tools, and examples. Structured frameworks: a long format (role, objective, context, instructions, examples, notes), a short format for simple tasks, and an agent format that adds an SOP and tool descriptions.
- **Money use (Skill-builder):** No direct money angle in the video. Skill to build: agent prompt design, tool descriptions, evaluation and iteration, token budgeting.

### 21. How to Build an AI Slack Assistant in 5 Minutes (Chatbase)
[Watch](https://www.youtube.com/watch?v=krHTtaud0CU) · 4 min · List #348 · [note](notes/348-krHTtaud0CU.md)
- **Recap:** Create a chatbot in Chatbase and add a knowledge source. Pasting a website URL and choosing "fetch links" scrapes the site. Files, text, Q&A pairs, and Notion are also supported. Set the system prompt so the bot acts as an internal assistant for employees, and adjust the temperature (lower is more reserved, higher more creative).
- **Money use (Possible angle (no price given)):** implied, not stated. Businesses could pay for a setup like this as an internal knowledge bot. No price is given.

### 22. Step by Step: Scrape UNLIMITED Emails for FREE with n8n
[Watch](https://www.youtube.com/watch?v=NzMNuuS5JbI) · 28 min · List #347 · [note](notes/347-NzMNuuS5JbI.md)
- **Recap:** Fetch Google Maps search result pages with a plain HTTP GET, using `+` in place of spaces in the query. Parse the returned HTML in a Code node, then filter out non-business domains with a regex exclude list. Pipes in the list must have no spaces.
- **Money use (Possible angle):** a lead list of local businesses (for example dentists by region) can feed outreach or sales services. No price is given. Caution: scraping Google Maps may breach Google's terms, and cold email is subject to anti-spam rules. The video does not address either.

### 23. Step by Step: RAG AI Agents Got Even Better
[Watch](https://www.youtube.com/watch?v=wEXrbtqNIqI) · 34 min · List #346 · [note](notes/346-wEXrbtqNIqI.md)
- **Recap:** Swap n8n's window buffer memory for Postgres chat memory so chat history survives restarts. Build a RAG agent that answers from a vector store (Supabase with pgvector) and cites what it retrieved.
- **Money use (Possible angle (no price given)):** implied, not stated. Businesses could pay to have a document-chat system like this built, which Nate offers through booking a call.

### 24. How to Build a Personal Assistant AI Agent in n8n (Step-by-Step, No Code)
[Watch](https://www.youtube.com/watch?v=ZP4fjVWKt2w) · 66 min · List #345 · [note](notes/345-ZP4fjVWKt2w.md)
- **Recap:** Build a main "personal assistant" agent in n8n, triggered by Telegram messages, with window buffer memory keyed to the Telegram chat ID so it remembers the conversation. Give the main agent a Google Sheet "contact database" tool and make it look up contacts before emailing or inviting anyone.
- **Money use (Skill-builder):** No direct money angle in the video. for this build. Nate invites viewers to book a call to have him build assistants or automations for their business. Skill to build: n8n agent and sub-workflow design, prompt and tool-description writing, Telegram and Google API….

### 25. Set up Google Credentials in n8n in 5 minutes (2025)
[Watch](https://www.youtube.com/watch?v=3Ai1EPznlAc) · 5 min · List #344 · [note](notes/344-3Ai1EPznlAc.md)
- **Recap:** Create a Google Cloud project, then configure the OAuth consent screen and add your own account as a test user. Create an OAuth client ID as a web application, paste n8n's redirect URI into it, then copy the client ID and secret into the n8n credential. Click "sign in with Google" in n8n and grant access.
- **Money use (Skill-builder):** No direct money angle in the video. Skill to build: OAuth setup, Google Cloud console, n8n credential setup, API enablement.

### 26. 5 n8n Tips You NEED to Know
[Watch](https://www.youtube.com/watch?v=Ctr89Q2Nei8) · 17 min · List #343 · [note](notes/343-Ctr89Q2Nei8.md)
- **Recap:** Continue on error: set a node to keep going when one item fails, so one bad URL does not stop a loop. Adding the error output lets you route failed items separately. Parent and child agents: a parent agent calls a child workflow and waits for a "response" field. A quality-check model can send the query back for a retry.
- **Money use (Skill-builder):** No direct money angle in the video. Skill to build: error handling, sub-workflow calls, expression syntax, tool-calling agents, node referencing.

### 27. Build this Multi AI Agent System for Research and Content Creation in n8n
[Watch](https://www.youtube.com/watch?v=u2Tuu02r7QI) · 11 min · List #342 · [note](notes/342-u2Tuu02r7QI.md)
- **Recap:** A content sheet holds a campaign name, subject, and target audience. A new row triggers the workflow. Research step: a Tavily news search on the subject returns recent articles (three in the demo), which are aggregated into one item. Three specialised agents (LinkedIn, X, blog) each take the article content and audience, then write their post.
- **Money use (Possible angle (no price given)):** Not stated. Inferred: small businesses might pay for a campaign-to-posts pipeline with a review step. Nate suggests adding a chat interface and visuals.

### 28. Vector Database Optimization with n8n: Metadata, Text Splitting, & Embeddings
[Watch](https://www.youtube.com/watch?v=VBw5PEV-zKw) · 19 min · List #341 · [note](notes/341-VBw5PEV-zKw.md)
- **Recap:** The embedding model used for ingestion must match the index. Using a larger embedding model than the index was built for left the embedding step stuck, so he stopped it. Loader choice changes the output: extracting text from a PDF and loading JSON produced eight noisy vectors, while loading the PDF as binary produced one clean vector with PDF metadata.
- **Money use (Skill-builder):** No direct money angle in the video. Skill to build: vector database setup, text splitting, metadata design, embedding debugging, retrieval filters.

### 29. This AI Agent Extracts Text From Images in n8n
[Watch](https://www.youtube.com/watch?v=skHe-qIRkM4) · 12 min · List #340 · [note](notes/340-skHe-qIRkM4.md)
- **Recap:** A Telegram bot receives an invoice image. The workflow takes the largest version of the file and downloads it as binary. The binary is sent to a third-party OCR API over HTTP, which returns parsed text. A Code node splits out fields (invoice number, date, total, billing address, due date, notes) and writes them to Google Sheets columns.
- **Money use (Possible angle (no price given)):** Not stated. Inferred: small businesses that process paper invoices might pay for an intake bot that logs them automatically.

### 30. The Best RAG System On YouTube (Steal This!)
[Watch](https://www.youtube.com/watch?v=Kvf-Pr1LRe4) · 19 min · List #339 · [note](notes/339-Kvf-Pr1LRe4.md)
- **Recap:** Three parts: a RAG chat agent; an ingestion workflow that watches a Google Drive folder for new files; and an update workflow that watches for edited files. Files are routed by type (Google Docs exported as text, PDFs extracted, Excel aggregated, Word converted), then embedded into Supabase with metadata: file ID, name, creator, created and…
- **Money use (Possible angle (no price given)):** Not stated. Inferred: companies with shared Drive folders might pay for chat over their documents. Nate says he will expand this in his paid community.

### 31. Understanding APIs in n8n (as a beginner)
[Watch](https://www.youtube.com/watch?v=ju9xk_QX990) · 17 min · List #338 · [note](notes/338-ju9xk_QX990.md)
- **Recap:** An API is a set of rules that lets software talk to other software. Nate uses a restaurant waiter as the analogy. REST methods: GET reads, POST creates or sends, PUT replaces, PATCH partially updates, DELETE removes. GET and POST cover most use.
- **Money use (Skill-builder):** No direct money angle in the video. Skill to build: HTTP requests, query parameters, API key auth, reading API docs, JSON output handling.

### 32. How I Built an AI Agent to Automate my Emails in n8n (Step by Step, No Code)
[Watch](https://www.youtube.com/watch?v=KIJHRq_Tg6o) · 23 min · List #337 · [note](notes/337-KIJHRq_Tg6o.md)
- **Recap:** Gmail trigger fires on each new email; an LLM classifies it as customer-support or not, returning JSON with a true/false field. A Switch node routes the two cases. The support branch runs a tools agent that searches a policy/FAQ vector store and calls a Gmail "create draft" tool to reply in the same thread.
- **Money use (Possible angle (no price given)):** Not stated by Nate. Inferred: small businesses with a busy support inbox might pay for a triage-and-draft setup with a human approval step.

### 33. Everything I Learned About AI Agents in 2024 in 19 Minutes
[Watch](https://www.youtube.com/watch?v=pYelCIqkm5Y) · 19 min · List #336 · [note](notes/336-pYelCIqkm5Y.md)
- **Recap:** An assistant is reactive and needs direction; an agent acts autonomously across multi-step processes. Core agent parts: the core (brain), memory, tools, and the prompt. Build order: first a clean, up-to-date data foundation (e.g. a vector database), then goal mapping, then the build in n8n, then testing and refining against edge cases.
- **Money use (Possible angle (no price given)):** Nate offers paid AI consulting to build agents for businesses. No price is stated in the video.

### 34. Build AI Agents for $0.014 with DeepSeek V3 in n8n
[Watch](https://www.youtube.com/watch?v=-uEDxBXsAnQ) · 10 min · List #335 · [note](notes/335--uEDxBXsAnQ.md)
- **Recap:** Two ways to use DeepSeek V3 in n8n: as the chat model behind an AI agent, or as a plain HTTP request node. For the agent route, point n8n's OpenAI Chat Model node at OpenRouter's base URL and select the DeepSeek model ID, so the OpenAI-style node talks to a different provider.
- **Money use (Skill-builder):** No direct money angle in the video. Cheap per-token access could lower the cost of running agents for clients, but Nate does not say this. Skill to build: HTTP Request node, cURL import, API key credentials, base-URL swap, system and user message setup.

### 35. Having an Actual Conversation with Data Using an ElevenLabs Voice Agent and n8n
[Watch](https://www.youtube.com/watch?v=pJYm7MOyMH0) · 14 min · List #334 · [note](notes/334-pJYm7MOyMH0.md)
- **Recap:** The n8n side is a RAG agent: a Google Doc is loaded into a Pinecone namespace, and a tools agent searches it with a vector store tool. The voice agent sends the spoken question to an n8n webhook as a POST body parameter. The n8n agent answers, and Respond to Webhook returns the text to the voice agent.
- **Money use (Skill-builder):** No direct money angle in the video. Skill to build: RAG pipeline setup, webhook integration, voice agent prompting, tool parameter design.

### 36. ElevenLabs Voice Agents Are So Easy to Build (No Code!)
[Watch](https://www.youtube.com/watch?v=Je4EAscnKK0) · 16 min · List #333 · [note](notes/333-Je4EAscnKK0.md)
- **Recap:** An ElevenLabs voice agent gathers the recipient and the email content in conversation, then POSTs them to an n8n webhook. The agent writes the subject and body itself. The voice agent's tool description tells it when to call and which fields to collect.
- **Money use (Skill-builder):** No direct money angle in the video. Skill to build: voice agent configuration, webhook integration, tool and parameter design, n8n agent workflows.

### 37. How I'd Teach a 10 Year Old to Build AI Agents (No Code, n8n)
[Watch](https://www.youtube.com/watch?v=6DLZK7XDOGo) · 20 min · List #332 · [note](notes/332-6DLZK7XDOGo.md)
- **Recap:** An AI agent is a brain (the LLM), memory, instructions (system prompt), and tools. The user message is the input and the agent's action or reply is the output. Build steps in n8n: chat trigger, AI agent, OpenAI chat model, Window Buffer Memory (last five messages, keyed by session ID), then a Gmail send tool.
- **Money use (Skill-builder):** No direct money angle in the video. He says outputs can go to Telegram, Slack or a phone, which is how you would extend it. Skill to build: agent architecture, n8n AI agent setup, prompt writing, tool wiring with from-AI fields, memory….

### 38. How I Built A Technical Analyst AI Agent in n8n With No Code
[Watch](https://www.youtube.com/watch?v=dooXxhGy5Ow) · 17 min · List #331 · [note](notes/331-dooXxhGy5Ow.md)
- **Recap:** Telegram trigger into an AI agent with one tool, "get chart". Send a ticker such as "Apple" and the agent calls the tool. Tool flow: an HTTP POST to a chart-image API returns a stored chart URL, an HTTP GET downloads the image as binary, a vision model writes a technical analysis, and the text goes back to the…
- **Money use (Skill-builder):** No direct money angle in the video. Nate notes the output is not financial advice. Skill to build: agent tool design, vision model analysis, API debugging (headers, binary vs JSON), Telegram….

### 39. I Built a Team of Research Agents for Newsletter Automation in n8n (No Code)
[Watch](https://www.youtube.com/watch?v=HUdm3NXwk-w) · 23 min · List #330 · [note](notes/330-HUdm3NXwk-w.md)
- **Recap:** Sequential multi-agent pipeline: form trigger, then a newsletter planner (table of contents via search), a project planner (splits into sections), six research agents running in parallel,… One agent per section gives better output than one agent writing the whole newsletter. Each research agent searches and cites its own section.
- **Money use (Possible angle):** implied, not priced: automated newsletters for businesses or teams (he suggests sending to employees or a team). He also suggests scheduling it from a database or Airtable. No prices stated.

### 40. The Ultimate n8n Starter Kit (2025) (Free)
[Watch](https://www.youtube.com/watch?v=4JR-UrEZHQQ) · 3 min · List #329 · [note](notes/329-4JR-UrEZHQQ.md)
- **Recap:** Announces a free n8n starter kit: a roadmap in five modules, from n8n basics to building AI agents and advanced AI integrations. Each lesson links to resources such as videos, documentation and case studies. Aimed at people learning n8n or thinking about moving from Make or Zapier.
- **Money use (Skill-builder):** No direct money angle in the video. The free kit is the lead-in to his paid community. Skill to build: n8n fundamentals, AI agent basics (curriculum overview).

### 41. Two Ways to Save 96% of Your Money Using DeepSeek R1 in n8n
[Watch](https://www.youtube.com/watch?v=o69yGTxB8EE) · 15 min · List #328 · [note](notes/328-o69yGTxB8EE.md)
- **Recap:** Cost comparison: he quotes o1 output at $60 per million tokens and R1 at $2.19, which he calls about 96% cheaper. Method 1, R1 through OpenRouter: create a key, paste OpenRouter's base URL into the OpenAI chat credential, then paste the R1 model ID as an expression.
- **Money use (Skill-builder):** No direct money angle in the video. Cost savings are the pitch for builders. Skill to build: API provider switching, HTTP Request configuration, cost analysis, debugging reasoning-model output.

### 42. How to Actually Build Agents with DeepSeek R1 in n8n (Without OpenRouter)
[Watch](https://www.youtube.com/watch?v=tjaD65OCoE8) · 11 min · List #327 · [note](notes/327-tjaD65OCoE8.md)
- **Recap:** The problem: R1 through OpenRouter was very slow and looped on tool calls. R1 through DeepSeek's own API answered fast but rejected function calling. The pattern: use R1 as a planner. It turns a request into step-by-step instructions, and a tools agent with no system prompt carries them out (calendar event, two emails).
- **Money use (Skill-builder):** No direct money angle in the video. Skill to build: planner/executor agent design, n8n tools agents, API credential setup, HTTP requests.

### 43. Best Model for RAG? GPT-4o vs Claude 3.5 vs Gemini Flash 2.0 (n8n Experiment Results)
[Watch](https://www.youtube.com/watch?v=_DbZjllXDv8) · 19 min · List #326 · [note](notes/326-_DbZjllXDv8.md)
- **Recap:** RAG basics: the agent retrieves from a vector store, augments the query with that content, then the LLM writes the answer. Build three n8n agents with the same system prompt and the same Pinecone store, changing only the model. This keeps the test fair.
- **Money use (Skill-builder):** No direct money angle in the video. Skill to build: RAG pipeline design, vector store querying, multi-model evaluation, n8n agent configuration.

### 44. How to Locally Host DeepSeek R1 for FREE in Under 10 Minutes in n8n
[Watch](https://www.youtube.com/watch?v=MGaR7i35KhA) · 9 min · List #325 · [note](notes/325-MGaR7i35KhA.md)
- **Recap:** Why host locally: no API fees, and data stays on your own machine. Nate reads DeepSeek's hosted privacy policy as storing data in China, so he avoids sending sensitive data to its API. Start the self-hosted n8n AI starter kit with Docker. It runs n8n, Postgres, Qdrant and Ollama as containers.
- **Money use (Skill-builder):** No direct money angle in the video. Implied use case: client work where data cannot go to a third-party API. Skill to build: Docker setup, local LLM hosting with Ollama, n8n AI agent configuration, model management.

### 45. OpenAI Fires Back at DeepSeek With a New Reasoning Model: o3-mini (n8n AI Agent)
[Watch](https://www.youtube.com/watch?v=IBaT-XQm_wE) · 11 min · List #324 · [note](notes/324-IBaT-XQm_wE.md)
- **Recap:** Connect a reasoning model to an n8n AI Agent, either through the OpenAI chat node or through OpenRouter's native node when a new model is not yet listed. Give the agent three Pinecone vector stores as separate namespaces (resorts, flights, activities) and one Gmail send tool.
- **Money use (Skill-builder):** No direct money angle in the video. He mentions a travel-agent demo but does not describe clients or pricing. Skill to build: n8n AI agent setup, reasoning-model integration, Pinecone namespaces, OpenRouter credentials and….

### 46. I Built the Ultimate Team of AI Agents in n8n With No Code (Free Template)
[Watch](https://www.youtube.com/watch?v=9FuNtfsnRNo) · 23 min · List #323 · [note](notes/323-9FuNtfsnRNo.md)
- **Recap:** Orchestrator with specialist agents: one "ultimate assistant" agent with a short prompt delegates to email, calendar, contact, and content agents, each built as its own n8n workflow. Calling sub-workflows as tools: the sub-workflow starts with an Execute Workflow trigger, and its last node returns the response to the orchestrator.
- **Money use (Skill-builder):** No direct money angle in the video. Nate suggests the content agent could feed social posting or a content database, but he does not discuss pricing or clients. Skill to build: multi-agent architecture in n8n, sub-workflow tools, prompt scoping, error branches, tool ID….

### 47. I Built a Human In The Loop Sales Team That Waits for Feedback and Approval in n8n
[Watch](https://www.youtube.com/watch?v=FcAAlOw6KZ8) · 19 min · List #322 · [note](notes/322-FcAAlOw6KZ8.md)
- **Recap:** Trigger on new Airtable lead rows, then have a sales agent draft a personalized email using a project database as a tool. Structured output parser: force the agent to return separate "subject" and "email" fields instead of one blob.
- **Money use (Possible angle (no price given)):** Nate presents an AI agency ("Dunder AI") that sells custom AI solutions. The workflow is a lead-response system: inbound form, drafted outreach, human sign-off, then send. He says the aim is to book a discovery call. No price points for the agency's services are stated.

### 48. 4 Agentic Frameworks for More Efficient Workflows in n8n
[Watch](https://www.youtube.com/watch?v=nSQnJoqK4DQ) · 17 min · List #321 · [note](notes/321-nSQnJoqK4DQ.md)
- **Recap:** Prompt chaining: pass each agent's output as the next agent's input (outline writer, then evaluator, then blog writer). Linear, easy to debug, and each step can use its own prompt and model. Routing: a classifier agent labels an incoming email (support, promotion, finance, high priority) and sends it down the matching branch with its own persona and actions.
- **Money use (Skill-builder):** No direct money angle in the video. The routing and drafting pattern could suit email triage for support or sales teams, but Nate does not name a buyer or price. Skill to build: n8n multi-agent workflow design, prompt chaining, classifier routing, parallel branches and merges,….

### 49. This Trick Helps me Build Agents 3x Faster (as a beginner)
[Watch](https://www.youtube.com/watch?v=tr5_S1FGoUI) · 13 min · List #320 · [note](notes/320-tr5_S1FGoUI.md)
- **Recap:** The "from AI" pattern: switch a tool parameter to an expression so the agent fills it from the user's request. Each parameter needs a key; description, type, and default value are optional. Build a first working tool in minutes: an Outlook send-email tool with subject and body keys, then a calendar tool with event title, start, and end keys.
- **Money use (Skill-builder):** No direct money angle in the video. The method speeds up building assistants; Nate does not discuss clients or pricing. Skill to build: n8n AI agent tools, expression syntax, HTTP request tools, system prompt design, tool-sequencing….

### 50. I Built an AI Voice Travel Agent with ElevenLabs and n8n (Free Template)
[Watch](https://www.youtube.com/watch?v=5zhTxuuPc3A) · 31 min · List #319 · [note](notes/319-5zhTxuuPc3A.md)
- **Recap:** Voice intake: an ElevenLabs conversational agent collects trip details (origin, destination, dates, travelers, activities, email) and calls one custom tool. Webhook pattern: the tool POSTs the details to an n8n webhook, n8n runs the searches, and the workflow returns a short reply the voice agent speaks.
- **Money use (Possible angle (no price given)):** Nate's demo is a voice travel-planning intake that emails an itinerary. A plausible offer is voice intake plus automated research for travel agencies or similar service businesses. He does not state a price, client type, or sales method.

### 51. Building AI Agents in n8n Somehow Got Easier (as a beginner)
[Watch](https://www.youtube.com/watch?v=TfqioNAP1W4) · 13 min · List #318 · [note](notes/318-TfqioNAP1W4.md)
- **Recap:** Build a first n8n AI Agent: add a chat trigger, attach a chat model, then add tools. Use "let the model define this parameter" on a tool field instead of hand-written from-AI expressions, and add a short description to each field so the model fills it correctly.
- **Money use (Skill-builder):** No direct money angle in the video. The demo implies a chat assistant that books meetings and sends email for a business; Nate does not discuss pricing or clients. Skill to build: n8n agent setup, tool wiring for email, calendar, CRM, and chat, prompt-level date handling,….

### 52. I Built a Human in the Loop Calendar Agent in n8n with No Code
[Watch](https://www.youtube.com/watch?v=z-gDDajSSNE) · 20 min · List #317 · [note](notes/317-z-gDDajSSNE.md)
- **Recap:** Human-in-the-loop pattern: an intent agent reads calendar and contacts, drafts an action, and sends it to the user in Telegram for approval before anything is changed. Feedback loop: a classifier labels the reply as approved or denied; denials go to a correction agent that merges the original intent with the feedback and re-asks.
- **Money use (Skill-builder):** No direct money angle in the video. The pattern could be sold as an approval-gated scheduling assistant for small teams; Nate does not name a price. The free template is offered through his free school community. Skill to build: n8n no-code agent building, human-in-the-loop design, intent classification, feedback loops,….

### 53. How to Set up Supabase and Postgres for RAG Agent with Memory in n8n (2025)
[Watch](https://www.youtube.com/watch?v=JjBofKJnYIU) · 10 min · List #316 · [note](notes/316-JjBofKJnYIU.md)
- **Recap:** Postgres as chat memory for an n8n agent: connect a Postgres Chat Memory node, which stores each conversation in a table keyed by the chat session ID. Supabase as a vector store: create a project, run the vector-store setup SQL from the docs, and get a "documents" table for embeddings.
- **Money use (Possible angle (no price given)):** Nate's demo is a RAG chatbot answering a body shop's service questions from its own document, so a plausible offer is document-grounded FAQ agents for small local businesses. Nate does not state a price or sales method.

### 54. Make Your Agents Communicate Better in n8n (Feedback, Specifying Inputs, Agent Logs)
[Watch](https://www.youtube.com/watch?v=vwlx-e8UYC8) · 17 min · List #315 · [note](notes/315-vwlx-e8UYC8.md)
- **Recap:** Parent/child agent pattern in n8n: the parent agent calls child agent workflows as tools, and the child returns its last node's output as the tool response. Typed inputs: switching a child workflow trigger from "accept all data" to defined fields (setting, main character, adventure) lets the parent agent fill named parameters.
- **Money use (Skill-builder):** No direct money angle in the video. The pattern could support reliable multi-agent client builds (feedback loops make paid automations less brittle), but Nate does not pitch a product. Skill to build: n8n agent workflows, sub-workflow tools, input schema design, conditional routing, error-output….

### 55. Your AI Agent Prompts Are Wrong - Here's The Fix
[Watch](https://www.youtube.com/watch?v=2vj2BF_dWeY) · 27 min · List #314 · [note](notes/314-2vj2BF_dWeY.md)
- **Recap:** Prompt reactively: start with no system prompt, add one tool, test, then add one line for each error you see. Change one thing at a time. Core sections: background (role and goal), tools (what each is for and when to use it), rules (if-then conditions, not a fixed order), examples (only for observed failures), and final notes…
- **Money use (Skill-builder):** No direct money angle in the video. Skill to build: prompt engineering, agent debugging, tool design, markdown prompt structure.

### 56. How to Build an Outlook Inbox Manager in n8n (Step-by-Step, No Code)
[Watch](https://www.youtube.com/watch?v=h7BLVKh7yzc) · 32 min · List #313 · [note](notes/313-h7BLVKh7yzc.md)
- **Recap:** Trigger on Outlook "message received", polling every minute, with Raw output so the full body comes through. Clean the HTML body with an LLM step, then route with a Text Classifier using category descriptions and example phrases.
- **Money use (Skill-builder):** No direct money angle in the video. Skill to build: email automation, text classification, routing logic, agent drafting, Telegram alerts.

### 57. 6 Months of Building AI Agents in 43 Minutes (without the hype)
[Watch](https://www.youtube.com/watch?v=QhujcQk8pyU) · 43 min · List #312 · [note](notes/312-QhujcQk8pyU.md)
- **Recap:** Separate AI workflows (fixed steps with AI inside) from agents (the model picks its own steps). Most problems only need a workflow, which is easier to debug. Wireframe before building: map the trigger, data flow, branches, AI decision points, and integrations. Use AI only where it adds value, such as classifying free text. LLM calls cost money.
- **Money use (Possible angle (no price given)):** Nate's claim: he scopes client work with wireframes before quoting, since underpricing and missing integrations are common. No price points are given.

### 58. Store All Data Types with Agentic RAG in n8n
[Watch](https://www.youtube.com/watch?v=BhGaGFH0jR4) · 19 min · List #311 · [note](notes/311-BhGaGFH0jR4.md)
- **Recap:** Traditional RAG chunks documents, embeds them, and returns the nearest chunks. It misses whole-document context and gets numeric questions wrong. Agentic RAG lets the agent choose a source: vector search for text, SQL for tabular data, or full file retrieval for a whole document.
- **Money use (Skill-builder):** No direct money angle in the video. Skill to build: RAG architecture, SQL, vector databases, agent tool routing, Supabase setup.

### 59. How I Automated Faceless Shorts with AI in n8n (free template)
[Watch](https://www.youtube.com/watch?v=Gc03J27xmBc) · 37 min · List #310 · [note](notes/310-Gc03J27xmBc.md)
- **Recap:** A Google Sheet of ideas drives the run. A row with status "to do" starts it, and a schedule trigger can run it several times a day. An agent writes one family-friendly image prompt per animal. Prompts are cleaned of newlines and quotes before use.
- **Money use (Possible angle):** implied by "grow a YouTube channel while you sleep". No revenue or pricing is stated.

### 60. How to Actually Scrape Twitter/X Data with n8n
[Watch](https://www.youtube.com/watch?v=lEo7IAgj0UY) · 20 min · List #309 · [note](notes/309-lEo7IAgj0UY.md)
- **Recap:** Build a loop: set a starting count, search tweets, extract fields, append rows to Google Sheets, then return to the search until the count hits a limit (three runs gave 58 tweets in the… Use the response's next-cursor value as the pagination input for the next request, and reference the most recent count and cursor so each loop updates them.
- **Money use (Possible angle (no price given)):** Nate suggests market analysis, competitor analysis, and lead lists from scraped data. He gives no price for selling any of it.

### 61. How MCPs Make Agents Smarter (for non-techies)
[Watch](https://www.youtube.com/watch?v=m0YrxLnFPzQ) · 16 min · List #308 · [note](notes/308-m0YrxLnFPzQ.md)
- **Recap:** An LLM becomes an agent when it can call tools, but hardcoded tools need one node per operation, which does not scale. An MCP server sits between the agent and a service and tells the agent what tools, schemas, and resources exist.
- **Money use (Skill-builder):** No direct money angle in the video. Skill to build: MCP concepts, agent tool design, debugging API parameters.

### 62. Ultimate No Code MCP Setup Guide (Self-Host, Installation, Common Issues)
[Watch](https://www.youtube.com/watch?v=OUPW4DJMAsA) · 25 min · List #307 · [note](notes/307-OUPW4DJMAsA.md)
- **Recap:** Deploy self-hosted n8n with a one-click template on Elestio, adding a payment method and credits first; larger plans help MCP servers run. Install the community node n8n-nodes-mcp from Settings, Community Nodes (self-hosted only).
- **Money use (Skill-builder):** No direct money angle in the video. Skill to build: self-hosting, MCP configuration, environment variables, agent tool design, troubleshooting.

### 63. How I Built JARVIS with No Code (Tutorial w/ Lovable, ElevenLabs, n8n)
[Watch](https://www.youtube.com/watch?v=KUvSzvFeZls) · 34 min · List #306 · [note](notes/306-KUvSzvFeZls.md)
- **Recap:** Architecture: an ElevenLabs voice agent sends each spoken request to one n8n webhook tool with a single "query" field. A main n8n agent (GPT-4o) picks one of four sub-agent workflows (email, calendar, contacts in Airtable, web content), and each sub-agent calls its own Gmail, Calendar, or Airtable tools.
- **Money use (Skill-builder):** No direct money angle in the video. He frames it as a personal assistant build and mentions a paid community, without pricing a client offer. Skill to build: voice agent design, webhook integration, multi-agent routing, prompt writing, no-code front-end….

### 64. Understand ANY Document with Mistral OCR in n8n (Step-by-Step)
[Watch](https://www.youtube.com/watch?v=85qo6qC4r-0) · 15 min · List #305 · [note](notes/305-85qo6qC4r-0.md)
- **Recap:** Three HTTP requests in order: upload the binary file to Mistral, request a signed URL for the uploaded file ID, then send that URL to the OCR endpoint. Get the file from a form trigger by pointing nodes at the binary field name, not the default "data". Import curl commands from API docs into HTTP Request nodes to fill them in fast.
- **Money use (Skill-builder):** No direct money angle in the video. The extracted fields are meant to feed Sheets or email, but no client or pricing model is given. Skill to build: API chaining, HTTP Request node, binary file handling, OCR, structured data extraction.

### 65. AI Agents: What 99% of Beginners Get Wrong
[Watch](https://www.youtube.com/watch?v=HuTyZiUDz2k) · 13 min · List #304 · [note](notes/304-HuTyZiUDz2k.md)
- **Recap:** Default to a fixed AI workflow (step 1, step 2, step 3) when the steps are known. Use an agent only when the path must be decided at run time. Four reasons he gives for workflows: reliability (no mis-passed data between agents and tools), cost (no extra model call to decide the next step), easier debugging (you see which node…
- **Money use (Possible angle (no price given)):** Nate says he runs an agency that delivers AI solutions to clients and teaches people to build them, so client delivery and courses are his stated model. No prices or client types given.

### 66. Research ANYTHING and Get a PDF Report (free n8n template)
[Watch](https://www.youtube.com/watch?v=TeFCb5-4e5U) · 29 min · List #303 · [note](notes/303-TeFCb5-4e5U.md)
- **Recap:** Form in, PDF out: a form takes a topic and an email. A planner agent splits it into five chapter topics. Use Google Sheets as a scratchpad between steps, so a long report does not have to fit in one n8n run. Later steps pull the rows back to build the sources list and table of contents.
- **Money use (Skill-builder):** No direct money angle in the video. Nate's pitch is unlimited runs at low cost versus tool limits; no buyers or prices named. Skill to build: multi-agent research pipeline, structured output parsing, Google Sheets as a data store,….

### 67. How to Connect Slack to n8n (2025) (Step-by-Step)
[Watch](https://www.youtube.com/watch?v=qk5JH6ImK0I) · 6 min · List #302 · [note](notes/302-qk5JH6ImK0I.md)
- **Recap:** Create a Slack app at api.slack.com/apps in a workspace you own, then add it to a channel. Connect Slack to n8n for sending messages with OAuth 2 (or an access token as a fallback), and grant bot token scopes such as app mentions read, channels read, chat write.
- **Money use (Skill-builder):** No direct money angle in the video. Skill to build: Slack app setup, OAuth and scopes, event subscriptions, webhook verification, n8n credentials.

### 68. Build Anything with Lovable + n8n AI Agents (beginner's guide)
[Watch](https://www.youtube.com/watch?v=kUpTUEwKnrk) · 20 min · List #301 · [note](notes/301-kUpTUEwKnrk.md)
- **Recap:** Architecture: Lovable builds the front end from a natural-language prompt. The form POSTs to an n8n webhook, an AI agent does the work, and n8n returns the result to the page through a…
- **Money use (Skill-builder):** No direct money angle in the video. Nate says the pattern can connect to Supabase, Firebase, Stripe, or Resend for a full web app, but names no buyers or prices. Skill to build: webhook integration, no-code front-end building, AI agent prompting, response handling, live….

### 69. How I 100% Automated Long Form Content with n8n (free template)
[Watch](https://www.youtube.com/watch?v=lF2bvXoV-Zg) · 24 min · List #300 · [note](notes/300-lF2bvXoV-Zg.md)
- **Recap:** A pipeline that makes "top 10" ranking videos from a Google Sheet. Rows with status "to-do" are pulled one at a time, and the workflow writes the video and uploads it. Split the LLM work across agents: an intro/outro agent and a ranker agent. Each uses a user message with the subject plus a system prompt.
- **Money use (Possible angle):** Faceless top-10 video channel at scale. Nate built a demo channel but states no revenue, views, or price. Says the same flow works for shorts and Reels.

### 70. 3 AI Workflows Step-by-Step (Beginner's Guide to n8n)
[Watch](https://www.youtube.com/watch?v=06Beyp_iDL0) · 44 min · List #299 · [note](notes/299-06Beyp_iDL0.md)
- **Recap:** RAG pipeline: a Google Drive folder trigger fires on new files, downloads the file as binary, and sends it to a Pinecone vector store. RAG chatbot: a chat trigger feeds an AI agent with a chat model, and the Pinecone store is attached as a tool, pointed at the right namespace. A system prompt is optional but helps.
- **Money use (Skill-builder):** No direct money angle in the video. Nate frames the workflows as beginner practice and says the templates can be customized, with no pricing or buyers named. Skill to build: RAG design, vector DB setup, n8n credentials (OAuth and API key), AI agent tool use, text….

### 71. n8n's Native MCP Integration (without the hype)
[Watch](https://www.youtube.com/watch?v=VTEg8uJ4yxo) · 15 min · List #298 · [note](notes/298-VTEg8uJ4yxo.md)
- **Recap:** - n8n 1.88 adds two native nodes: an MCP Server Trigger (exposes n8n workflows as MCP tools) and an MCP Client Tool (attached to an AI agent to call an MCP server). Setup: copy the test or production server-sent-events URL from the trigger, then connect Claude Desktop by editing its developer config JSON with that URL and restarting.
- **Money use (Skill-builder):** No direct money angle in the video. Skill to build: MCP server setup, JSON config editing, n8n tool design, agent prompting, debugging tool calls.

### 72. Turn Any Website Into LLM Ready Data in Seconds with n8n & Firecrawl
[Watch](https://www.youtube.com/watch?v=Ee9WtEEd300) · 15 min · List #297 · [note](notes/297-Ee9WtEEd300.md)
- **Recap:** Firecrawl turns websites into LLM-ready data. Its four endpoints are scrape, crawl, map and extract. Extract takes a URL plus a prompt and a schema and returns structured data. Compare a raw HTTP request (messy HTML) with scrape (markdown) and extract (structured JSON). Use the Firecrawl playground to find the right prompt and schema, then copy the request.
- **Money use (Possible angle (no price given)):** Pull structured data from many sites, then feed it to outreach or research. Nate suggests researching many companies and drafting first outreach from the output. No pricing or client pitch given.

### 73. n8n Just Leveled Up AI Agents (Anthropic's Think Method)
[Watch](https://www.youtube.com/watch?v=WqyLxyALTt0) · 20 min · List #296 · [note](notes/296-WqyLxyALTt0.md)
- **Recap:** - n8n's new Think tool (added in n8n 1.88) is a scratchpad tool the agent calls to write down its reasoning between or after other tool calls. Read an agent's execution logs top to bottom: memory, system prompt, child-agent tool calls, then the think step, to see why it acted.
- **Money use (Skill-builder):** No direct money angle in the video. for a client. Nate's paid community is the only sales pitch (see promo). Could be a sellable "agent that books and emails for you" if you can show it works. Skill to build: agent design, tool and sub-workflow orchestration, prompt tuning, reading execution logs, model….

### 74. One n8n Workflow for Unlimited Error Handling (Step-by-Step)
[Watch](https://www.youtube.com/watch?v=bTF3tACqPRU) · 10 min · List #295 · [note](notes/295-bTF3tACqPRU.md)
- **Recap:** Build one "error logger" workflow that starts with an Error Trigger node, then point any number of active workflows at it in their settings (Error workflow option). Only active workflows fire the error workflow, so activate the workflow under test first.
- **Money use (Skill-builder):** No direct money angle in the video. Skill to build: n8n error handling, execution debugging, Google Sheets and Slack integration, expressions.

### 75. OpenAI's Image API Just Changed the Game (save 10+ hours/week, n8n tutorial)
[Watch](https://www.youtube.com/watch?v=ACkHpQQnfxQ) · 18 min · List #294 · [note](notes/294-ACkHpQQnfxQ.md)
- **Recap:** A form collects email, topic and target audience. A LinkedIn post agent researches with Tavily and drafts the post; an image-prompt agent turns the post into a graphic prompt. Call the OpenAI image generation endpoint with an HTTP Request node, using curl import to pre-fill it.
- **Money use (Skill-builder):** No direct money angle in the video. Use case: LinkedIn posts with graphics; he says the manual version takes about 20 minutes in Canva. No price points set. Skill to build: HTTP Request node, curl import, base64 to binary, prompt chaining, email delivery, API key handling.

### 76. I Built a Marketing Team with 1 AI Agent and No Code (free n8n template)
[Watch](https://www.youtube.com/watch?v=ldETapkr8Hg) · 34 min · List #293 · [note](notes/293-ldETapkr8Hg.md)
- **Recap:** One main agent, reached through Telegram by voice or text, calls six sub-workflow tools: create image, edit image, search image database, blog post, LinkedIn post, and video. Each sub-workflow starts with a "called by another workflow" trigger with defined inputs (title, prompt, chat ID), so the agent fills in the same fields every time.
- **Money use (Skill-builder):** No direct money angle in the video. for a client offer. He did not total a per-run cost; the per-item figures above are his. (My inference: a content service could be built on it.) Skill to build: multi-agent tool design, sub-workflows, image generation and editing, video pipelines, Google….

### 77. How I Automated Product Videography with AI (Step by Step n8n Tutorial)
[Watch](https://www.youtube.com/watch?v=qV7xOEKEBDA) · 27 min · List #292 · [note](notes/292-qV7xOEKEBDA.md)
- **Recap:** An n8n form collects a product photo, title, description and a validated email. Save the original to Google Drive, then download it again, because binary files are hard to reference later in the flow. An agent writes an image prompt from the description, then the OpenAI image-edit endpoint returns a base64 image that is converted to a binary file.
- **Money use (Skill-builder):** No direct money angle in the video. for a client offer. Product marketing visuals (photo plus video) are the use case shown. No price points for selling it. Skill to build: form triggers, binary file handling, multipart API requests, base64 conversion, polling loops,….

### 78. This AI Agent Picks Its Own Brain (10x Cheaper, n8n)
[Watch](https://www.youtube.com/watch?v=gwCQF--cARA) · 14 min · List #291 · [note](notes/291-gwCQF--cARA.md)
- **Recap:** A cheap model-selector agent (Gemini 2.0 Flash) reads each Slack message and returns one model name from a fixed list you define with strengths. The main agent then uses that name as its chat model through OpenRouter, so simple requests use cheap models and hard ones use stronger models.
- **Money use (Skill-builder):** No direct money angle in the video. (My inference: cost-routing could be sold as a cost-saving setup for clients with heavy agent usage.) Skill to build: model routing, prompt design, OpenRouter setup, RAG with Supabase, Slack triggers, logging.

### 79. How I Auto Track AI Agent Actions and Token Usage (n8n tutorial)
[Watch](https://www.youtube.com/watch?v=vVdS-ZEFf50) · 10 min · List #290 · [note](notes/290-vVdS-ZEFf50.md)
- **Recap:** Turn on "return intermediate steps" in the AI Agent node to get each tool call, its parameters, its response and its token counts. Change the agent's error setting to continue on an error output, so runs split into success and error branches.
- **Money use (Skill-builder):** No direct money angle in the video. (My inference: cost dashboards could be a deliverable for clients running agents.) Skill to build: agent observability, n8n error branching, code nodes, Google Sheets logging, cost tracking.

### 80. My Proven AI Agent Formula Explained
[Watch](https://www.youtube.com/watch?v=Nj9yzBp14EM) · 15 min · List #289 · [note](notes/289-Nj9yzBp14EM.md)
- **Recap:** Five-step playbook: learn foundations (LLMs, JSON, APIs, RAG basics) before building; pick high-ROI processes; process-map every step on paper first; Score candidate processes on four tests: repetitive, time-consuming, error-prone, scalable. Scalable matters most because the payoff compounds as volume grows.
- **Money use (Viable offer (price signal)):** Nate's claim: $240,000 in 6 months from these builds. Sell automation of repetitive, high-volume business processes; no specific price points stated. Start by listing one repeated process and mapping it step by step.

### 81. The Secret to Making AI Agents 100% Reliable - Human in the Loop (n8n)
[Watch](https://www.youtube.com/watch?v=CdnR-fNVPKI) · 16 min · List #288 · [note](notes/288-CdnR-fNVPKI.md)
- **Recap:** Add a "human in the loop" send-and-wait step (Telegram in the demo) so the workflow pauses until a person responds. Use free-text feedback instead of yes or no, so the human can ask for changes. Route the reply through an LLM text classifier that decides approve or deny.
- **Money use (Skill-builder):** No direct money angle in the video. (My inference: approval-gated posting could be offered to clients who want a sign-off step.) Skill to build: n8n human-in-the-loop, LLM classification, revision loops, Set-node state handling, Telegram bot….

### 82. APIs for AI Agents: The Only Beginner's Guide You'll Ever Need (n8n)
[Watch](https://www.youtube.com/watch?v=qZkX_gIlwsY) · 25 min · List #287 · [note](notes/287-qZkX_gIlwsY.md)
- **Recap:** Use a native n8n integration when one exists; use the HTTP Request node when it does not (Perplexity was the example). Read API docs in five parts: method, endpoint, query parameters, headers (usually auth), body. Import a curl command into n8n to pre-fill the request, then add your key.
- **Money use (Skill-builder):** No direct money angle in the video. Skill to build: reading API docs, HTTP Request node, curl import, credential setup, JSON debugging, agent tool….

### 83. This AI System Creates & Posts Faceless Shorts 24/7 (free n8n template)
[Watch](https://www.youtube.com/watch?v=jkEEVYFzT1U) · 31 min · List #286 · [note](notes/286-jkEEVYFzT1U.md)
- **Recap:** Trigger on a Google Sheets row marked to-do (one row at a time), then have an LLM generate eight opponents for a main character. Build close-up image prompts with a structured output parser, generate images in bulk, wait about 90 seconds, then fetch results (he notes polling would be more robust).
- **Money use (Possible angle (no price given)):** Faceless shorts run on autopilot; he frames it as a channel you can run hands-off. He cites another channel with 680k subscribers and 221M views (his figures, not his own). No price point set for a client product. Start by importing the template and swapping in your niche prompts.

### 84. 25 Hidden n8n Features That Save Hours of Work
[Watch](https://www.youtube.com/watch?v=zMy5yoA-ub8) · 15 min · List #285 · [note](notes/285-zMy5yoA-ub8.md)
- **Recap:** Editor shortcuts: typing "=" turns a fixed field into an expression; pin or mock node data so paid API nodes do not re-run while building; deactivate, rename and add nodes from the keyboard. Use "continue on error" or an error-output branch so one failed item does not stop a batch.
- **Money use (Skill-builder):** No direct money angle in the video. Skill to build: n8n editor navigation, expressions, data pinning, error handling, sub-workflows, agent debugging,….

### 85. The Simplest Way to Automate Scraping Anything with No Code (Apify + n8n tutorial)
[Watch](https://www.youtube.com/watch?v=gZ_RLC25gCw) · 8 min · List #284 · [note](notes/284-gZ_RLC25gCw.md)
- **Recap:** Apify actors are prebuilt scrapers; you start one with a JSON input, then fetch its results from the dataset. Use the two-step pattern: POST to run the actor (returns a run ID), then GET the last run's dataset items.
- **Money use (Possible angle (no price given)):** Sell lead lists or market research pulled from Google Maps, TikTok or LinkedIn to local businesses or agencies. Start with one niche and one actor, then add enrichment (email, outreach). No prices stated.

### 86. I Built a 24/7 Viral Shorts Machine with No-Code (free n8n template)
[Watch](https://www.youtube.com/watch?v=BcfjIBd49C8) · 31 min · List #283 · [note](notes/283-BcfjIBd49C8.md)
- **Recap:** A five-stage, no-code pipeline: Google Sheet row to AI prompt writer (structured output parser for image, video and audio prompts) to images to videos to sound effects to rendered short to… Batch handling in n8n: aggregate and split items so four brands run through each step as four separate items.
- **Money use (Viable offer (price signal)):** Run faceless short-video accounts for brands or niche clients: a sheet of brands or topics in, a week of posts out. Charge a monthly fee per account plus setup, and keep per-short cost near $2. The video does not state prices charged to clients.

### 87. Create Your No Code AI Clone (HeyGen + n8n Full Guide)
[Watch](https://www.youtube.com/watch?v=llm60n03x3c) · 16 min · List #282 · [note](notes/282-llm60n03x3c.md)
- **Recap:** Create a HeyGen avatar and cloned voice from a short camera recording (he says 2 to 5 minutes is requested; he submitted about 30 seconds). Call HeyGen's create-avatar-video API from an n8n HTTP Request node (import curl, save the API key as a header credential), with avatar ID, voice ID and script text.
- **Money use (Possible angle):** Automated short-form video for creators or brands: scrape a niche source (news, trends), turn it into a script, and publish an avatar video on a schedule. Pitch a "content on autopilot" package to creators who hate filming. No prices stated.

### 88. Build & Sell n8n AI Agents (8+ Hour Course, No Code)
[Watch](https://www.youtube.com/watch?v=Ey18PDiaAYI) · 507 min · List #281 · [note](notes/281-Ey18PDiaAYI.md)
- **Recap:** Agent anatomy (LLM brain, memory, system prompt, tools) and when a fixed AI workflow beats an agent (deterministic steps are cheaper and more reliable). APIs and HTTP Request: method, endpoint, query/header/body parameters, import-curl, saving auth as a credential, reading 200/400/401/500 errors, polling for async jobs.
- **Money use (Viable offer (price signal)):** Nate's claim: over $500k revenue in 8 months from his agency and teaching. He sells AI automations to clients: support email bots, invoice processing, lead scraping (Apify Google Maps), product-ad generators, LinkedIn content pipelines. Start with one linear workflow and a wireframe, then price a scoped build.

### 89. The Easiest Way to Use Community Nodes in n8n
[Watch](https://www.youtube.com/watch?v=WI8ikp5YyRw) · 9 min · List #280 · [note](notes/280-WI8ikp5YyRw.md)
- **Recap:** Community nodes are third-party integrations that replace hand-built HTTP Request nodes. On n8n Cloud, enable "verify community nodes" in settings (n8n version 1.94 or later), then install verified nodes from the panel. Create a credential with just the API key for the node; the node handles auth headers itself.
- **Money use (Skill-builder):** No direct money angle in the video. (setup tutorial; a faster setup could cut client build time for integration-heavy automations). Skill to build: n8n administration (enabling community nodes), installing and configuring third-party nodes,….

### 90. This AI Agent Can Scrape and Screenshot the Web with No Code (n8n tutorial)
[Watch](https://www.youtube.com/watch?v=3Pim6uCASSE) · 17 min · List #279 · [note](notes/279-3Pim6uCASSE.md)
- **Recap:** One Firecrawl search call can search the web, filter results, scrape each page, and return markdown or a screenshot (including full-page). Search operators to narrow results: exact match, exclusions with a dash, site:, URL and title word filters, plus time, language and country parameters.
- **Money use (Possible angle (no price given)):** Research and monitoring services: pull competitor pages, news, or Reddit/forum threads matching keywords and deliver screenshots and markdown summaries to clients on a schedule. Prices not stated.

### 91. I Built the Ultimate Browser Agent with No Code (n8n + Airtop)
[Watch](https://www.youtube.com/watch?v=ar37oypyATQ) · 18 min · List #278 · [note](notes/278-ar37oypyATQ.md)
- **Recap:** A browser agent built from a tool-using AI agent: start browser, load URL, query page, click, type, think, end session. Each browser tool is an n8n sub-workflow that calls Airtop, and returns session and window IDs the agent must pass along. Use a "query" tool to read the page, and fall back to loading a known URL when a click fails.
- **Money use (Possible angle (no price given)):** Sell browser-automation templates for sales and research (ICP scoring of LinkedIn profiles, competitor price monitoring, job-change monitoring) to B2B teams. Price points not stated. Start with one narrow workflow and a demo.

### 92. Multi-Agent Systems Have NEVER Been EASIER to Build (n8n, no code)
[Watch](https://www.youtube.com/watch?v=0iUNOmeU7O4) · 20 min · List #277 · [note](notes/277-0iUNOmeU7O4.md)
- **Recap:** Orchestrator architecture: one parent agent whose only job is to understand intent and delegate to specialized child agents or tools. Keep the orchestrator prompt short and strict (delegate only, never write emails or summaries; a few rules and an example output).
- **Money use (Possible angle (no price given)):** Build reusable "agent teams" (email, calendar, CRM lookup, content) for small businesses and sell them as packaged assistants; charge for setup plus a monthly fee. Start with one orchestrator and two or three sub-workflows. No prices stated.

### 93. This AI Workflow Analyzes Videos for FREE (n8n + Google Gemini)
[Watch](https://www.youtube.com/watch?v=acB2o6nwAn8) · 12 min · List #276 · [note](notes/276-acB2o6nwAn8.md)
- **Recap:** Build an n8n workflow that takes an uploaded video from a form, sends it to Google Gemini, and returns a detailed text description. Gemini's video flow is upload first, then poll for status (wait about 5 seconds and check again) before calling generate-content, because the file is not ready right away and the call fails…
- **Money use (Possible angle (no price given)):** Video analysis as a service: describe or summarize client videos (ads, product clips, training content), tag them, or produce summaries for content teams. Start with a form-based n8n workflow and a fixed output format. No prices stated.

### 94. 8 Simple Hacks for Smarter AI Agents in 8 Mins
[Watch](https://www.youtube.com/watch?v=onIuhtYMCdk) · 8 min · List #275 · [note](notes/275-onIuhtYMCdk.md)
- **Recap:** Eight hidden model settings in the n8n AI agent "chat model" node (via OpenRouter) that change how an agent behaves. Repetition control: frequency penalty and presence penalty, with negative values encouraging repetition and positive values encouraging variety.
- **Money use (Skill-builder):** No direct money angle in the video. (general configuration tips; useful for anyone selling or running agent workflows who needs predictable output and cost control). Skill to build: n8n AI agent configuration, LLM parameter tuning, OpenRouter setup, prompt testing.

### 95. Locally Host n8n AI Agents for FREE (step by step)
[Watch](https://www.youtube.com/watch?v=F1psr8uFwUU) · 8 min · List #274 · [note](notes/274-F1psr8uFwUU.md)
- **Recap:** Clone the self-hosted AI starter kit from GitHub, install Docker Desktop, then run the start command for your GPU type (Nvidia, AMD on Linux, or Mac). The starter kit runs four services: n8n, Postgres, Qdrant (vector store), and Ollama (local models). They share one Docker network.
- **Money use (Skill-builder):** No direct money angle in the video. (setup tutorial). Possible service angle is setting up local or private n8n stacks for clients who need data control. No pricing given. Skill to build: Docker install and compose start, container and volume basics, local service wiring, n8n first-run….

### 96. I Built an AI Agent that Builds Teams of Agents in n8n (free template)
[Watch](https://www.youtube.com/watch?v=Ik8OHT3w4pE) · 20 min · List #273 · [note](notes/273-Ik8OHT3w4pE.md)
- **Recap:** Architecture: a main "n8n developer" agent takes a plain-language request. It calls a builder tool, which is a second workflow where an LLM writes n8n workflow JSON. Keep the builder's context small. He feeds it one Google Doc with a reference AI-agent workflow JSON, a sticky-note example, and the required settings block, rather than whole docs or a…
- **Money use (Possible angle (no price given)):** Sell a custom "workflow builder" agent that turns client requests into importable n8n workflows, or use it to speed up client builds. Pair with a template library. No client price stated.

### 97. How to Set Up a Cloudflare Tunnel for Local n8n (2025)
[Watch](https://www.youtube.com/watch?v=cZQPDLgPtNg) · 9 min · List #272 · [note](notes/272-cZQPDLgPtNg.md)
- **Recap:** Why a local n8n cannot receive webhooks from outside (Gmail, Telegram, and similar services), and how a tunnel fixes that by giving n8n a public HTTPS address. Create a Cloudflare account and add a domain you own (or buy one through Cloudflare). He says free quick-tunnel URLs are temporary, so a domain is better for a stable setup.
- **Money use (Skill-builder):** No direct money angle in the video. (infrastructure how-to). Could support a client-hosted n8n that needs public webhooks, but no offer or pricing is discussed. Skill to build: Docker Compose env editing, tunnel and DNS setup, webhook URL configuration, container restart and….

### 98. This AI System Posts Viral ASMR Shorts Hourly (free template)
[Watch](https://www.youtube.com/watch?v=RvuPRX-b7Lc) · 17 min · List #271 · [note](notes/271-RvuPRX-b7Lc.md)
- **Recap:** Pipeline: keep a sheet of the seven most recent objects used. An idea agent picks a new object not on that list. A prompt agent writes a structured text-to-video prompt. Use structured output parsers so the idea agent returns an object and a caption, and the prompt agent fills a fixed template (subject, setting, action, style, sound, camera motion,…
- **Money use (Possible angle (no price given)):** Faceless short-form content channels for clients or for your own accounts, with the prompt and template sold as a setup. He says the video cost is high and it is not a get-rich scheme. No client prices stated.

### 99. I Built a YT Strategist AI Agent That Makes Me $6k/mo (free template n8n)
[Watch](https://www.youtube.com/watch?v=Ch-AWxvX2Jc) · 26 min · List #270 · [note](notes/270-Ch-AWxvX2Jc.md)
- **Recap:** Five-phase system. Phase 1 (form-triggered): take three competitor channels, scrape each one's top 10 videos from the last 6 months, and extract title power words and thumbnail analysis… Phase 2 (weekly): the same packaging analysis on a broader niche (his example: "artificial intelligence").
- **Money use (Possible angle (no price given)):** Sell a YouTube packaging and strategy agent to creators and small channels. Charge for the template setup plus monthly reports, or sell the sheet-based pattern bank. He mentions a future hook-analysis add-on. No client price stated.

### 100. How to Trigger n8n AI Agents from ChatGPT (no code)
[Watch](https://www.youtube.com/watch?v=AGi3U79zMIM) · 9 min · List #269 · [note](notes/269-AGi3U79zMIM.md)
- **Recap:** Put an n8n webhook in front of an agent or workflow, then let a ChatGPT custom GPT call it as an action. Use a helper GPT to write the OpenAPI 3.1.0 JSON schema that describes the webhook's fields (date, invoice number, totals, and so on), then paste it into the custom GPT's Actions panel.
- **Money use (Possible angle (no price given)):** Sell a custom GPT front end that triggers back-office automations for a client, such as invoice intake, CRM updates, or contact lookup. Price points not stated.

### 101. n8n Just Leveled Up RAG Agents (Reranking & Metadata)
[Watch](https://www.youtube.com/watch?v=xWhX61651H8) · 14 min · List #268 · [note](notes/268-xWhX61651H8.md)
- **Recap:** RAG basics: chunk a document, embed the chunks into a vector database, embed the question with the same model, then pull back the nearest chunks. Reranking: raise the retrieval limit (he sets 20 instead of the default 4), let a reranker score every chunk, then keep only the top 3 for the agent.
- **Money use (Possible angle):** Better retrieval for document-QA agents (contracts, policies, meeting transcripts) sold to businesses that have large document sets. No prices stated.

### 102. Watch Me Build an AI Resume Analysis System in 28 minutes (no code)
[Watch](https://www.youtube.com/watch?v=M0s6O8xtVUE) · 29 min · List #267 · [note](notes/267-M0s6O8xtVUE.md)
- **Recap:** Method first: list the manual steps, sketch a wireframe in Excalidraw (trigger, data sources, transforms, where AI fits), then build. Gmail trigger with "download attachments" on, then route by file type (Word, PDF, or text) with a Switch node on the MIME type.
- **Money use (Possible angle (no price given)):** Sell an AI resume screener to recruiting teams or staffing agencies, with fit scoring and a sheet-based candidate database. The pitch is less bias and faster first-pass review. Price points not stated.

### 103. Build Your First Research AI Agent in 12 mins (No Code)
[Watch](https://www.youtube.com/watch?v=UBx4Zudvf8s) · 12 min · List #266 · [note](notes/266-UBx4Zudvf8s.md)
- **Recap:** Architecture: a chat trigger feeds an AI Agent node. The agent's "brain" is a chat model, and its "tool" is a live web-search service. Connect the chat model through OpenRouter using an API key, and check that the connection tests green. Confirm the model answers before adding tools.
- **Money use (Possible angle):** Competitor-research or lead-research agent that runs on a schedule and writes reports into a sheet, sold to sales or marketing teams. No price points stated.

### 104. Local n8n AI Agents in 5 Minutes (FREE and no code)
[Watch](https://www.youtube.com/watch?v=DcEMf2K6cPQ) · 6 min · List #265 · [note](notes/265-DcEMf2K6cPQ.md)
- **Recap:** Assumes a self-hosted n8n stack (the self-hosted AI starter kit) is already running in Docker, with an Ollama container alongside it. Browse Ollama's model library, copy a model's pull name, then open the Ollama container's exec shell and run the pull command to install it locally.
- **Money use (Skill-builder):** No direct money angle in the video. (a free-tooling tutorial; no offer or pricing). Skill to build: Docker exec, Ollama model management, n8n AI agent credentials, local model selection.

### 105. Use Parallelization to Make n8n Workflows Faster & Scalable
[Watch](https://www.youtube.com/watch?v=qNW9KaLe1nY) · 11 min · List #264 · [note](notes/264-qNW9KaLe1nY.md)
- **Recap:** Parallelization runs items at the same time. Sequential loops in n8n wait for each item. Some APIs (his example: Perplexity) batch on their side; others need n8n to split the work. Steps: right-click nodes and convert them to a sub-workflow, set the calling node to "Run once for each item," and turn off "Wait for sub-workflow completion."
- **Money use (Possible angle (no price given)):** Speed up client automations that process long lists (research, lead enrichment). Sell a faster build with rate-limit safeguards. No prices stated.

### 106. Build Anything With Grok 4 and n8n AI Agents
[Watch](https://www.youtube.com/watch?v=FFH3uQDk2yU) · 11 min · List #263 · [note](notes/263-FFH3uQDk2yU.md)
- **Recap:** Grok 4 (released July 9, 2025, per him) is a chat model that can be added to an n8n AI agent through the xAI Grok chat model node. Attach a research tool (Perplexity Sonar) and let the model choose the query. It called the tool without a system prompt.
- **Money use (Skill-builder):** No direct money angle in the video. Model choice and cost control are useful for client builds. Skill to build: model swapping in n8n, tool-call debugging, OpenRouter setup, cost reading from executions.

### 107. Unlock the Next Evolution of Agents with Human-like Memory (n8n + zep)
[Watch](https://www.youtube.com/watch?v=kNsX2qu8jHY) · 16 min · List #262 · [note](notes/262-kNsX2qu8jHY.md)
- **Recap:** Simple memory in n8n only stores recent turns. Long-term memory needs a knowledge graph of entities and relationships per user. Zep stores a per-user graph plus session history, keyed by a session ID (Telegram chat ID in his demo). A new session ID gives a fresh graph.
- **Money use (Possible angle (no price given)):** Memory layers for personal or customer assistants (onboarding, tutoring) that recall each user. Sell a memory-enabled agent with cost limits. No prices stated.

### 108. n8n Webhook Security: Learn This Before It's Too Late
[Watch](https://www.youtube.com/watch?v=3FfCRbq3XMs) · 9 min · List #261 · [note](notes/261-3FfCRbq3XMs.md)
- **Recap:** A live n8n webhook with no auth lets anyone who has the production URL start the workflow, which can run up model costs and reach connected tools and data. Use a long, hard-to-guess path as a first layer, then add authentication.
- **Money use (Possible angle (no price given)):** Security hardening for client agents that are publicly reachable (voice, DM, or chat webhooks). Sell an audit plus auth setup. No prices given.

### 109. From Zero to RAG Agent: Full Beginner's Course (no code)
[Watch](https://www.youtube.com/watch?v=cCD303XsUjI) · 23 min · List #260 · [note](notes/260-cCD303XsUjI.md)
- **Recap:** RAG means retrieve information, then generate an answer. A vector database is one way to retrieve. Two parts: an ingestion pipeline (document, chunk, embed, store) and a query agent (embed the question, match vectors, answer).
- **Money use (Possible angle (no price given)):** Beginner-level RAG agents for small businesses (document Q&A on a golf rulebook, policies, catalogs). Sell a setup plus a keep-it-updated pipeline. No prices stated.

### 110. Beginner's Guide to Metadata: Make Your RAG Agents Smarter
[Watch](https://www.youtube.com/watch?v=lnm0PMi-4mE) · 15 min · List #259 · [note](notes/259-lnm0PMi-4mE.md)
- **Recap:** Metadata is data about data. It adds context to vector chunks (video title, URL, timestamp, date, department) without changing their embedding meaning. Retrieval works on meaning first. Metadata is read after a chunk is found, and it can filter results (e.g., only one video).
- **Money use (Possible angle (no price given)):** Build RAG knowledge bases with source citations for clients (support docs, transcripts, internal records). Sell a pipeline with add/update/delete flows. No prices stated.

### 111. Building an AI Agent Swarm in n8n Just Got So Easy
[Watch](https://www.youtube.com/watch?v=vpyllOeLhs4) · 26 min · List #258 · [note](notes/258-vpyllOeLhs4.md)
- **Recap:** An orchestrator agent delegates to specialist agents (email, contacts, YouTube, web research, calendar), each added as a tool with its own model and system prompt. Since an n8n update, sub-agents can live in the same workflow, so each run is visible on one canvas.
- **Money use (Possible angle (no price given)):** Build agent swarms for a client's ops (email, scheduling, research). Sell a setup plus logging dashboard. No prices stated.

### 112. I Built 204 AI Automations, Here's What Actually Matters
[Watch](https://www.youtube.com/watch?v=wq001sxDTWw) · 23 min · List #257 · [note](notes/257-wq001sxDTWw.md)
- **Recap:** Context engineering: give the agent the right information at the right time, from six parts (user input, system prompt, memory, retrieved knowledge, tool calls, structured output), not one… Three memory types: working (within one run), short-term (conversation window keyed by session ID), and long-term (persists across sessions).
- **Money use (Possible angle (no price given)):** Context and memory design is the core deliverable for client agents. Sell an audit of a client's data sources and an agent build with memory and retrieval. He did not state prices.

### 113. Turn Your AI Agent Into a Voice Assistant in Minutes (n8n & ElevenLabs)
[Watch](https://www.youtube.com/watch?v=qJRFu88HUio) · 21 min · List #256 · [note](notes/256-qJRFu88HUio.md)
- **Recap:** Two ways to add voice: a speech-in/speech-out pipeline (audio file in, audio file out) and a real-time ElevenLabs voice agent. Pipeline: Telegram voice message, download, transcribe with ElevenLabs, run an AI agent, convert the reply to speech, send audio back.
- **Money use (Possible angle (no price given)):** Voice front ends for customer support or personal assistants. Sell a voice assistant that answers calls or messages and looks things up. No pricing from him for clients.

### 114. How to Build a WhatsApp Agent with n8n (credential tutorial)
[Watch](https://www.youtube.com/watch?v=A0OwvNOLNlw) · 7 min · List #255 · [note](notes/255-A0OwvNOLNlw.md)
- **Recap:** Connecting a WhatsApp Business trigger in n8n so an incoming message starts a workflow. Creating a Meta developer app (business type) and copying its app ID and secret into the n8n trigger credential. Getting a test-number access token and business account ID for the separate WhatsApp send node, which needs its own credential.
- **Money use (Possible angle (no price given)):** Business WhatsApp agents that answer leads and book meetings for a company. No pricing given. Start by building the flow for one client's business number.

### 115. Why 99% of AI Automations Fail in Production
[Watch](https://www.youtube.com/watch?v=Irk4-DO5qgM) · 18 min · List #254 · [note](notes/254-Irk4-DO5qgM.md)
- **Recap:** Define production-ready: the workflow is active, errors notify you, errors are logged, retries and fallbacks exist, and failures are safe (no mass emails or record deletes). Five techniques: (1) an error workflow linked to every active workflow; (2) retry on fail with a max-tries count and wait time; (3) a fallback model;
- **Money use (Skill-builder):** No direct money angle in the video. Skill to build: n8n error handling, retry and fallback configuration, JSON escaping, polling loops, execution….

### 116. Build Anything with GPT-5 and n8n AI Agents
[Watch](https://www.youtube.com/watch?v=gGCwSIlIRlY) · 17 min · List #253 · [note](notes/253-gGCwSIlIRlY.md)
- **Recap:** Connect GPT-5 to an n8n AI agent: create an OpenAI API key on the API platform (ChatGPT subscription does not cover API use), add billing, then pick the model. Use n8n's evaluation feature: run 10 test rows against expected answers and score accuracy out of 5, so you compare models with data, not vibes.
- **Money use (Skill-builder):** No direct money angle in the video. Skill to build: Model selection, n8n evaluations, tool-calling tests, cost-per-run math, prompt testing.

### 117. So You’re Building AI Agents... Now What?
[Watch](https://www.youtube.com/watch?v=4LQYWziOg0Q) · 13 min · List #252 · [note](notes/252-4LQYWziOg0Q.md)
- **Recap:** Pick a path by intent: freelance on the side if you are passionate, consult once you are good, build a company with a partner if you are an aspiring entrepreneur, automate your own business… Start with one-off custom builds, then move to diagnosing problems and selling solutions. Templates alone are commoditized.
- **Money use (Viable offer (price signal)):** Freelance one-off builds first, then retainers or consulting. Sell to businesses or employers, or cut your own business costs with the same skills. Start with your network and a public build log.

### 118. I Built 3 Lead Gen AI Agents Using ONLY My Words (beginner tutorial)
[Watch](https://www.youtube.com/watch?v=k_5NcmxWlVg) · 16 min · List #251 · [note](notes/251-k_5NcmxWlVg.md)
- **Recap:** Describe the agent in plain English to Lindy's agent builder, answer its follow-up questions, then open the generated flow and read every node before trusting it. Lead-gen flow: search People Data Labs for leads (10 per run) and have an agent add each one to a Google Sheet. The first run stopped after five rows; a prompt fix made it process all ten.
- **Money use (Viable offer (price signal)):** Sell lead generation plus personalized outreach drafts to sales teams or agencies, priced per batch of leads or per outcome. None stated by Nate.

### 119. This Workflow Auto-Posts to 9 Different Socials (free template)
[Watch](https://www.youtube.com/watch?v=QovlUE_VlWQ) · 10 min · List #250 · [note](notes/250-QovlUE_VlWQ.md)
- **Recap:** Use a verified community node (Blotato) instead of hand-built HTTP requests. One API key credential serves every platform node. Use a Google Sheet as a posting queue: pull the first row with status "ready to post", upload its media, post, then write the status back.
- **Money use (Skill-builder):** No direct money angle in the video. Sellable as a setup-and-maintain auto-posting service for creators or small brands, with the sheet as the client-facing input. Skill to build: n8n community nodes, Google Sheets as a data queue, social platform setup, Drive file-ID….

### 120. I Built the Ultimate Army of Media Agents in n8n (free template)
[Watch](https://www.youtube.com/watch?v=jBanaNBY-sM) · 30 min · List #249 · [note](notes/249-jBanaNBY-sM.md)
- **Recap:** A Telegram-driven manager agent that only routes requests to sub-agents: Drive, email, calendar, contacts, social, creative, posting, web search, plus a doc tool and a think tool. Each custom tool is its own n8n sub-workflow, which avoids passing binary files between flows. Tools pass only small values such as file ID, prompt and chat ID.
- **Money use (Possible angle (no price given)):** No client price given. Sellable as a custom media or social assistant for creators or small teams, charging for setup and for the tools you build.

### 121. I built this AI Agent in 2 hours (and got paid $1200)
[Watch](https://www.youtube.com/watch?v=8C6iCpJ9HPo) · 11 min · List #248 · [note](notes/248-8C6iCpJ9HPo.md)
- **Recap:** The "agent" was really an AI workflow: it ran three times a day, generated topic ideas for the client's audience, and wrote posts in the client's brand voice. He got the client from a free YouTube channel with an email address in the description. He was building in public, not positioning as an expert.
- **Money use (Possible angle (no price given)):** Sell one-time builds to business owners who spend hours on repetitive content, outreach or FAQs, plus a small monthly API cost. Start by posting builds with a way to contact you, then price against time saved.

### 122. Watch Me Build a Multi-Agent Newsletter System in n8n (step-by-step)
[Watch](https://www.youtube.com/watch?v=pxzo2lXhWJE) · 29 min · List #247 · [note](notes/247-pxzo2lXhWJE.md)
- **Recap:** Architecture: weekly schedule trigger, news search for the past week, a planning agent that picks a title and three topics, deeper search per topic, one writer agent per section, an… Use a structured output parser (JSON schema) so the editor returns separate subject and body fields that map cleanly into Gmail.
- **Money use (Skill-builder):** No direct money angle in the video. Sellable as a managed weekly research draft for teams or a client's email list, with human review, priced on the hours it removes. Skill to build: n8n workflow design, AI agent prompting, structured outputs, multi-step research pipelines, HTML….

### 123. How to Sell AI Workflows (Without Starting an Agency)
[Watch](https://www.youtube.com/watch?v=QIsJe-nZ5XE) · 14 min · List #246 · [note](notes/246-QIsJe-nZ5XE.md)
- **Recap:** Skip the agency at first. Freelance for three to five paid projects to build proof, testimonials and a clear niche, then move toward consulting. Niche down to one type of client and one pain point. Build a short before-and-after demo (even a quick recorded walkthrough) that shows the outcome, not the tool.
- **Money use (Possible angle (no price given)):** Freelance first for proof, then consult for small and mid-size businesses that cannot pay enterprise rates. Sell outcomes such as hours saved, leads qualified, or support load removed. Start by picking one niche and building one demo.

### 124. How I Sold These 4 AI Agents for $23,000 (as a beginner)
[Watch](https://www.youtube.com/watch?v=HNKlFTd1maM) · 15 min · List #245 · [note](notes/245-HNKlFTd1maM.md)
- **Recap:** Diagnose a business problem first, then show the hours or money a manual process costs and how an automation would cut it. Price by value, not build effort. Early prices were guesses; later he priced by time saved and by complexity, and learned that a high close rate means you are underpricing.
- **Money use (Possible angle (no price given)):** Sell custom agents to small businesses that lose hours to outreach, data entry, admin or customer questions. Start by posting builds with your contact info so inbound leads find you. Price against the time or money the client saves.

### 125. Beginner's Guide to Workflow Evaluation in n8n (Stop Guessing!)
[Watch](https://www.youtube.com/watch?v=-zFd1nPn6U0) · 17 min · List #244 · [note](notes/244--zFd1nPn6U0.md)
- **Recap:** Treat workflow changes as hypotheses. Change one variable per run (prompt, model, temperature, tools, context prep), keep the rest fixed, and log what changed and what happened.
- **Money use (Possible angle (no price given)):** Offer eval and model-selection audits for clients' AI workflows (score accuracy, cost and speed, then recommend a model). Build the labeled dataset with the client's subject-matter expert. No price points stated.

### 126. I Built a Photoshop AI Agent in n8n with no code (NanoBanana)
[Watch](https://www.youtube.com/watch?v=7UNsK9LoORo) · 17 min · List #243 · [note](notes/243-7UNsK9LoORo.md)
- **Recap:** A Telegram-driven agent receives a photo or text, uploads it to Google Drive, and asks what to name it. Its tools rename, search raw or AI-generated folders, combine two images, or edit one. Put image generation in sub-workflows, and call each one from the main agent as a tool, so you can reuse it in other agents.
- **Money use (Viable offer (price signal)):** Sell an ad-creative or UGC image service: a client sends product photos, the agent returns branded variations. Add a logger and a prompt agent, then charge per asset or monthly. Video generation from the output is an add-on. No price points for services stated; his per-image cost is about 4 cents.

### 127. How I Sold a $6000 AI Workflow to a Business (Live Sales Call)
[Watch](https://www.youtube.com/watch?v=NSwl_E0WWKk) · 41 min · List #242 · [note](notes/242-NSwl_E0WWKk.md)
- **Recap:** Run discovery calls with the LRP loop (listen, repeat back, poke with a question), and let the client talk most of the time. Qualify early: check for budget authority (the founder/CEO), AI maturity and realistic expectations. Quantify pain on each call (hours per week, cost of each bottleneck) before you talk about tech or price.
- **Money use (Viable offer (price signal)):** Sell a personal-assistant build for a founder's team, with a fixed price in two payments and a phased rollout (Slack first, then other sources). Price on the ROI (hours saved, cost avoided), not on hours. Use the case study and testimonial after results. Start with the data inventory. No deal-size benchmark beyond this example.

### 128. n8n's Agent Builder Somehow Made Building Agents Even Easier (text to workflow)
[Watch](https://www.youtube.com/watch?v=TDHFkKSTJ30) · 19 min · List #241 · [note](notes/241-TDHFkKSTJ30.md)
- **Recap:** - n8n's text-to-workflow builder (a chat interface) drafts a plan, you approve or request changes, and it builds nodes, variables and a setup guide. Prompt specifically: name the chat model, tools and output format. A vague prompt ("research news and email me") gave an unconfigured HTTP tool;
- **Money use (Possible angle (no price given)):** Use the builder to draft client workflows faster, then charge for the review, fixes and handover. Sell the linear, predictable builds (lead qualification, invoice intake) that the builder handles well. No price points stated.

### 129. The TRUTH About Selling AI Automations to Businesses
[Watch](https://www.youtube.com/watch?v=SAerRtQLD0I) · 12 min · List #240 · [note](notes/240-SAerRtQLD0I.md)
- **Recap:** Sell the outcome (time, money, focus), not the workflow, nodes or model. Use the "destination, not the vehicle" framing. Pick a niche broader than one business type (for example "hair and beauty"), then reuse about 70 to 80% of a build across clients (Nate's claim).
- **Money use (Viable offer (price signal)):** Sell to SMBs who lack an AI partner. Price as setup plus revenue share or a fixed fee tied to ROI. Build a niche template base and tailor it per client. Use the ROI calculation as the sales asset and as a case study. Example start: $1,200 first build, $5,000 system.

### 130. This Vapi + n8n Voice Agent Won $5,000 in Just 21 Days
[Watch](https://www.youtube.com/watch?v=7siRW0My05o) · 19 min · List #239 · [note](notes/239-7siRW0My05o.md)
- **Recap:** Winner Azim (interview) walks through a mental-health voice-companion web app built in Bolt, with 9 n8n workflows as the backend. Onboarding form posts to an n8n webhook; AI agents write a user profile into a Google Sheet, and each call request spawns a personalized voice assistant.
- **Money use (Possible angle (no price given)):** Build voice agents for clients (Azim says he wants an agency). A passion project works as a demo to win clients. Sell templates or consultations. Note the caveat Azim raised: a mental-health product needs HIPAA and data protection, so it is not a quick launch. No price points stated.

### 131. The NEW Easiest Way to Build RAG Agents in Minutes (no code)
[Watch](https://www.youtube.com/watch?v=QojPKL96Dx4) · 16 min · List #238 · [note](notes/238-QojPKL96Dx4.md)
- **Recap:** Upload PDFs to a Pinecone Assistant (a hosted RAG service that handles indexing, chunking and embedding), then chat with it. Connect an n8n AI agent to the assistant with an HTTP request tool, using a curl import from Pinecone's API page and an API key.
- **Money use (Possible angle (no price given)):** Build quick RAG "ask our documents" agents for clients with policy docs, manuals or reports, where source citations matter. Price as a setup fee plus the hourly assistant cost passed through. Test on the client's own documents first. No price points for services stated.

### 132. n8n's NEW Native Data Tables Just Made Building Agents So Much Easier
[Watch](https://www.youtube.com/watch?v=QCjMBOEhpLE) · 15 min · List #237 · [note](notes/237-QCjMBOEhpLE.md)
- **Recap:** - n8n now has native data tables (a Data Tables tab) with string, number, boolean and date columns, stored inside n8n with no credentials or external API. Import rows from Google Sheets into a data table with a node that offers get, insert, update, upsert and delete operations, then map columns and match data types.
- **Money use (Possible angle):** Build a "sales data" or CRM-style agent for a small business that answers questions from its own data, or an email reply agent that uses stored contact notes. Price as a setup plus ongoing agent. No price points stated.

### 133. Stop Selling AI Agents, Sell AI Solutions Instead
[Watch](https://www.youtube.com/watch?v=w9-gfaV5vlM) · 14 min · List #236 · [note](notes/236-w9-gfaV5vlM.md)
- **Recap:** Sell business outcomes (time, money, focus) instead of agents or workflows, which are commoditized. Use a four-step framework: diagnose the pain, solve it with a simple system, convert the fix to dollar value, then price at a fraction of that value.
- **Money use (Viable offer (price signal)):** Sell to niches like agencies, real estate, e-commerce, coaches, and local services (dental, HVAC). Pitch a fixed-price "solution" tied to hours or dollars saved, with a scoped written proposal. Start with 3 to 5 low-price or free pilot projects, then raise prices.

### 134. 3 Hidden Data Table Hacks for Smarter AI Agents
[Watch](https://www.youtube.com/watch?v=lcNN3X9gXls) · 15 min · List #235 · [note](notes/235-lcNN3X9gXls.md)
- **Recap:** Store agent config (chat model, system prompt, user prompt) in an n8n data table keyed by workflow name, so a non-technical editor can change behavior without opening the workflow. Keep system prompts out of shared templates by pulling them from a data table, so the prompt (the IP) stays private.
- **Money use (Possible angle (no price given)):** Give a client an editable front end (the data table) for model and prompt settings. Sell templates while keeping system prompts private. Sell agent monitoring and eval reporting as an ongoing service. No price points stated.

### 135. How to Automate ANY Content with Poppy and n8n (no code)
[Watch](https://www.youtube.com/watch?v=FgP_AEfnfok) · 21 min · List #234 · [note](notes/234-FgP_AEfnfok.md)
- **Recap:** Poppy is a no-code builder: paste YouTube videos, sites, PDFs or sheets as sources, group them, and chat with them. Use n8n only for what must happen before or after the AI: daily research, then Poppy writes, then n8n sends.
- **Money use (Possible angle (no price given)):** content automation for clients who publish regularly, branded to their voice; newsletters with affiliate product links (Nate's example). No price points.

### 136. Build ANYTHING with Claude Sonnet 4.5 and n8n AI Agents
[Watch](https://www.youtube.com/watch?v=X80ljdCPM_U) · 19 min · List #233 · [note](notes/233-X80ljdCPM_U.md)
- **Recap:** Connect Claude Sonnet 4.5 in n8n. Direct Anthropic calls errored for Nate with default parameters, so he routed via OpenRouter. Compare models with n8n evaluations on a dataset: Nate ran only 10 cases and says 100 to 200 are needed. Tool overload: giving one agent 5+ tools made it fail; grouping tools into sub-agents (sub-workflows) worked.
- **Money use (Skill-builder):** No direct money angle in the video. Skill to build: model selection, eval design, tool and sub-agent architecture, OpenRouter setup.

### 137. How I'd Make Money with AI in 2026 (if I had to Start Over)
[Watch](https://www.youtube.com/watch?v=Q46OLxFshAQ) · 24 min · List #232 · [note](notes/232-Q46OLxFshAQ.md)
- **Recap:** A four-stage ladder: freelancer, consultant, agency ("AI partner"), teacher. Freelancer BUILD framework: pick one template, understand the use case, install and imitate, land a client, document and duplicate. Consultant SCAN framework: study the business, calculate the opportunity, architect the solution, narrate the results.
- **Money use (Viable offer (price signal)):** freelance $500 to $2,000 projects; consulting audit plus implementation; agency with developers and sales; paid community and teaching. Start with one template and one client.

### 138. I Tested OpenAI's AgentKit Against n8n: What You Need to Know
[Watch](https://www.youtube.com/watch?v=XeIx4S6YvGo) · 21 min · List #231 · [note](notes/231-XeIx4S6YvGo.md)
- **Recap:** Six-category comparison: ease of use, triggers, agent tools, model support, UI and chat components, deployment and control. Agent Builder is simpler: built-in web search with no API key, low-code visual editor. Its only trigger is chat, so event-driven automations are hard.
- **Money use (Skill-builder):** No direct money angle in the video. Skill to build: agent-platform evaluation, n8n nodes, sub-workflows, MCP concepts.

### 139. Build ANYTHING with Base44 and n8n AI Agents (beginner's guide)
[Watch](https://www.youtube.com/watch?v=tFFKuq2t0rI) · 25 min · List #230 · [note](notes/230-tFFKuq2t0rI.md)
- **Recap:** Build a no-code landing page in Base44 for a free "AI implementation roadmap" lead magnet (name, email, problem). Make the form POST to an n8n webhook: capture test data, pin it, activate the workflow, then switch the app to the production URL.
- **Money use (Possible angle):** free AI audit as a lead magnet, then paid implementation via discovery call. No price stated.

### 140. You're Doing AI Automation Wrong (Here's How to Fix It)
[Watch](https://www.youtube.com/watch?v=ip8FEYOQob0) · 11 min · List #229 · [note](notes/229-ip8FEYOQob0.md)
- **Recap:** Lesson 1, leverage over automation: automate roughly the first 60% (routine), let AI assist the next 30% (judgment), keep the last 10% human. Lesson 2, go deep: one tool, one client niche, one platform, rather than hopping. Lesson 3, simplicity scales: fewer AI steps, predictable workflows; boring systems get paid.
- **Money use (Possible angle (no price given)):** sell AI automation to businesses, priced on hours saved. Start by picking one lane and one process, then ship something small. No explicit price points.

### 141. Build Your First RAG Pipeline for Better RAG (step-by-step)
[Watch](https://www.youtube.com/watch?v=5uw1wE6niGc) · 16 min · List #228 · [note](notes/228-5uw1wE6niGc.md)
- **Recap:** A data pipeline has four parts: trigger, inputs, processing, destination (here a Supabase vector store). New PDF in a Drive folder: download it (converting Google Docs to PDF), insert into the vector store with embeddings and metadata (file name, date). Updates: on a file-changed event, delete old vectors matching the file name, then re-ingest the new version.
- **Money use (Skill-builder):** No direct money angle in the video. Skill to build: vector DB ingestion, metadata design, filtered deletes, n8n Drive triggers, pipeline design.

### 142. Create ANYTHING with Sora 2 + n8n AI Agents (Full Beginner's Guide)
[Watch](https://www.youtube.com/watch?v=Vm8QOo9MiC4) · 29 min · List #227 · [note](notes/227-Vm8QOo9MiC4.md)
- **Recap:** Call Sora 2 through a third-party API marketplace (Kie.ai) instead of OpenAI directly; import the provider's curl sample into an n8n HTTP Request node. Save the API key once as a header credential.
- **Money use (Possible angle):** Nate suggests UGC-style ad videos for brands from a sheet of product, audience and features. Teaching marketers prompting is mentioned as a paid service, unquantified.

### 143. This n8n Sales Automation Won $5,000 in Just 14 days
[Watch](https://www.youtube.com/watch?v=Z46F8ZiHZJo) · 26 min · List #226 · [note](notes/226-Z46F8ZiHZJo.md)
- **Recap:** Speed-to-lead system: a missed call (Twilio Studio) fires an n8n webhook that creates a lead row in Google Sheets, then sends a ringless voicemail and a follow-up text. Each inbound text looks up the lead by phone number, checks which step is complete, and routes to the next one.
- **Money use (Possible angle):** Brett's company WarehouseBob (SMS and n8n marketing) is recruiting agencies. Nate suggests showing the demo to businesses (realtors, insurance agents) and plugging in their scripts and CRM. No pricing stated.

### 144. From Zero to Inbox Agent (Full Beginner's Course, No-Code)
[Watch](https://www.youtube.com/watch?v=HN0oWxbF2bM) · 38 min · List #225 · [note](notes/225-HN0oWxbF2bM.md)
- **Recap:** Wireframe the whole system (trigger, classify, act) before building anything in n8n. Gmail trigger polls every minute; turn off "simplify" to get the full email body; pin test data while building.
- **Money use (Skill-builder):** No direct money angle in the video. Skill to build: n8n workflow building, prompt and category design, LLM classification, Gmail nodes, expressions and….

### 145. How I'd Become an AI Consultant If I Had To Start Over (2 Paths)
[Watch](https://www.youtube.com/watch?v=VzOYty0siaM) · 15 min · List #224 · [note](notes/224-VzOYty0siaM.md)
- **Recap:** Two paths: B2C education (teach n8n or other tools through YouTube, communities, courses, templates, coaching) and B2B consulting (audits, roadmaps, implementation, retainers). Choose by goal: scale and leverage (B2C, slower start) or simplicity and fast cash (B2B, one problem solved for one client).
- **Money use (Viable offer (price signal)):** Free audits, then paid AI builds and retainers for SMBs; education and team training for companies; a paid school community. Price points: "few thousand to tens of thousands" per project (his range). Start: pick a niche and offer one free audit this week.

### 146. I Built the Ultimate UGC Content System with AI Agents (free template)
[Watch](https://www.youtube.com/watch?v=AYsg5gAMWyo) · 26 min · List #223 · [note](notes/223-AYsg5gAMWyo.md)
- **Recap:** Input lives in a Google Sheet: product photo, ideal customer profile, features, video setting, and status. Only rows marked "ready" are processed, one at a time. A Switch node routes each row to one of three paths: Veo 3.1 alone, Nano Banana then Veo 3.1, or Sora 2.
- **Money use (Possible angle (no price given)):** Produce UGC-style ad variants for brands at low cost per clip. He says Sora gives about twice the volume for the same spend. No client prices given.

### 147. Learn Voice Agents Now, Thank Me Later (Full Beginner's Guide)
[Watch](https://www.youtube.com/watch?v=zWLZ3bVVwD8) · 42 min · List #222 · [note](notes/222-zWLZ3bVVwD8.md)
- **Recap:** Voice agent = speech-to-text, then an LLM, then text-to-speech. Four parts to set: model, system prompt, voice, and tools. Inbound (callers reach a number), outbound (agent calls people), and website widgets. Use cases: booking, support, reminders, surveys.
- **Money use (Possible angle (no price given)):** Voice agents for local service businesses (booking, customer questions, follow-ups). He demos a fictional car detailing business. He says the field has clear ROI and opportunity in 2026. No prices for client work.

### 148. How to Build Workflows 10x Faster with n8n's AI Builder
[Watch](https://www.youtube.com/watch?v=a5sJNwfZ528) · 18 min · List #221 · [note](notes/221-a5sJNwfZ528.md)
- **Recap:** "Build with AI" turns a prompt into a draft workflow. Then use "Execute and refine": run it, read the errors, and let the builder fix them. Common failure: variables from third-party nodes (Tavily, Perplexity, HTTP) are guessed wrong. Example: a Tavily field was null until "include answer" was turned on.
- **Money use (Possible angle (no price given)):** Implied: a faster way to deliver simple automations (research newsletter, sales brief from a form) to clients. He stresses that a client's process must be mapped before building. No prices.

### 149. n8n JUST Leveled Up AI Agents With Guardrails: Here's How It Works
[Watch](https://www.youtube.com/watch?v=oWdJMJp2HgM) · 14 min · List #220 · [note](notes/220-oWdJMJp2HgM.md)
- **Recap:** - n8n now has native Guardrails nodes (need version 1.119 or later, per him). Two actions: "Check Text for Violations" (AI-based, uses a model via OpenRouter) and "Sanitize Text" (no AI…
- **Money use (Possible angle (no price given)):** Implied: a safety and data-handling layer for client automations (redact PII before any LLM call, check outputs before they reach clients). No prices given.

### 150. The Cheapest & Easiest Way to Self-Host n8n (Beginner's Guide)
[Watch](https://www.youtube.com/watch?v=6ZB0zADNaqk) · 15 min · List #219 · [note](notes/219-6ZB0zADNaqk.md)
- **Recap:** Why self-host: data control, no execution limits, lower cost at high usage, and room to connect private or local AI models. Deploy n8n on a Hostinger VPS using its one-click n8n template. Choose a plan size (he uses KVM 2), a region, and the n8n image. Activate the free license key for paid-tier features (workflow history, debugging, folders).
- **Money use (Possible angle (no price given)):** Hosting setup as a service for clients. He says you may not charge for access to n8n itself: the client should hold the billing and own the account, and you act as adviser and builder. No prices for services.

### 151. How to Sign Your First AI Automation Client (Without Starting an Agency)
[Watch](https://www.youtube.com/watch?v=9dA1VB8V8oo) · 15 min · List #218 · [note](notes/218-9dA1VB8V8oo.md)
- **Recap:** Skip the agency. Start as a freelancer, then consultant, then agency. Pick one niche where people lose hours to repetitive admin, and write one sentence naming who you help and what problem…
- **Money use (Viable offer (price signal)):** Freelance AI automation for small businesses, sold on outcomes (time or money saved). Start with one or two free builds for testimonials, then charge. Price points: none stated beyond his $1,200 first-client claim. Start by listing 50 warm contacts and messaging them.

### 152. Build ANYTHING with Gemini 3 Pro and n8n AI Agents
[Watch](https://www.youtube.com/watch?v=Vb1SwBAn9cQ) · 24 min · List #217 · [note](notes/217-Vb1SwBAn9cQ.md)
- **Recap:** Connect Gemini to n8n three ways: the native Google Gemini node, the Gemini chat model in an agent, or OpenRouter. Native n8n Gemini nodes do not expose "thinking level" (only a thinking budget). To set it to low, he sends a raw HTTP request to the Gemini API.
- **Money use (Possible angle):** Implied: image intake for maintenance tickets or damage reports, and long-document Q&A. He gives no prices. His point: pick the model per use case using evals, not by reputation.

### 153. How to Use the NEW Nano Banana 2 in n8n (cheaper & no watermark)
[Watch](https://www.youtube.com/watch?v=iUgAVUcv9r0) · 13 min · List #216 · [note](notes/216-iUgAVUcv9r0.md)
- **Recap:** Text-to-image in n8n: one HTTP call creates a generation task (model, prompt, aspect ratio, resolution, output format) and returns a task ID. Polling loop: wait about 5 seconds, query the task by ID, then use a Switch node to loop on "generating", stop on "failed", or continue on "success". Runs took 13 to 35 checks.
- **Money use (Possible angle):** Implied: produce product and lifestyle images, ad creative, and headshots for small businesses without a studio. He gives no prices.

### 154. Gemini's New File Search Just Leveled Up RAG Agents (10x Cheaper)
[Watch](https://www.youtube.com/watch?v=irg-2IfAjpo) · 19 min · List #215 · [note](notes/215-irg-2IfAjpo.md)
- **Recap:** Gemini File Search takes an uploaded document, chunks and embeds it, and lets an agent query it, so no separate vector database or ingestion pipeline is needed. Build it in n8n with four HTTP requests: create a file search store, upload the file, import the file into the store, then query the store through a generate-content call.
- **Money use (Possible angle):** Implied: build document Q&A agents (policies, manuals, filings) for businesses, where low hosting cost makes each build cheaper. He gives no prices.

### 155. Master n8n Fast With These 17 Essential Nodes (real examples)
[Watch](https://www.youtube.com/watch?v=D9MIGseFB3g) · 24 min · List #214 · [note](notes/214-D9MIGseFB3g.md)
- **Recap:** Nate reuses the same 17 core nodes across 200+ automations. Start with them, then branch out. Triggers: schedule, event (Gmail, Slack), webhook and respond-to-webhook. Data shaping: Split Out and Aggregate (one item per list entry, then back), Edit Fields (Set) as a source of truth, If and Switch for routing, Code node for predictable data (write it with…
- **Money use (Skill-builder):** No direct money angle in the video. Skill to build: n8n node patterns, API docs reading, code nodes, structured output, batching.

### 156. How to Price AI Workflows (Without Losing Clients)
[Watch](https://www.youtube.com/watch?v=wIcw0T9NhZM) · 21 min · List #213 · [note](notes/213-wIcw0T9NhZM.md)
- **Recap:** Price on value (time saved, money saved, error reduction), not hours. Be able to show the math behind any number. Start with value-based pricing for projects. After a few wins, move to milestone-based monthly retainers. Hourly billing makes you look like a freelancer.
- **Money use (Viable offer (price signal)):** Sell builds, then maintenance and optimization retainers. Audits and enablement are offers he may cover later.

### 157. OpenAI Just Leveled Up n8n AI Agents (here's how it works)
[Watch](https://www.youtube.com/watch?v=lokbsA5VXOk) · 11 min · List #212 · [note](notes/212-lokbsA5VXOk.md)
- **Recap:** Enable "use Responses API" in the OpenAI Chat Model node (node version 1.3 or later). This unlocks OpenAI built-in tools. Web search: set context size, location, and an allowed-domain list. A domain filter needed a newer model (he switched to GPT-5 mini).
- **Money use (Skill-builder):** No direct money angle in the video. Skill to build: built-in model tools, vector stores, retrieval setup, API options.

### 158. Unlock the Full Power of Your n8n Agents (new instance MCP)
[Watch](https://www.youtube.com/watch?v=5p5cV0yVDvQ) · 13 min · List #211 · [note](notes/211-5p5cV0yVDvQ.md)
- **Recap:** - n8n's instance-level MCP lets an MCP client search, read the schemas of, and run any workflow in your instance. This needs n8n 1.21.2 or later. Turn on MCP access in settings (OAuth or access token), then connect a client such as Claude.
- **Money use (Possible angle):** Lovable generated a lead-form landing page from one workflow in a single prompt. No pricing stated.

### 159. I Built an AI Voice Receptionist with Vapi and n8n MCP (free template)
[Watch](https://www.youtube.com/watch?v=y-cq_Qo4zVo) · 34 min · List #210 · [note](notes/210-y-cq_Qo4zVo.md)
- **Recap:** Split a voice agent into two parts: the voice front end (Vapi assistant with its system prompt) and the back end (n8n automations). Wireframe the if-X-do-Y paths first: look up the caller by email, create a record if new, gather intent, then book, change, or cancel.
- **Money use (Possible angle):** A voice receptionist for a local business (the demo is a fictional detailing shop). No pricing stated.

### 160. n8n 2.0 is Here (What You Need to Know)
[Watch](https://www.youtube.com/watch?v=67BVIScAlbs) · 11 min · List #209 · [note](notes/209-67BVIScAlbs.md)
- **Recap:** - n8n 2.0 looks similar. Most changes are backend work on security, reliability and performance. UI changes: publish/unpublish replaces the active toggle, saving is near-instant, and a focus panel lets you edit node parameters while viewing the canvas. Breaking change: sub-workflows must be published before another workflow can call them.
- **Money use (Skill-builder):** No direct money angle in the video. Skill to build: version migration, sub-workflow design, human-in-the-loop approval.

### 161. How I'd Learn n8n if I had to Start Over in 2026
[Watch](https://www.youtube.com/watch?v=Fqeo8q8-nJg) · 14 min · List #208 · [note](notes/208-Fqeo8q8-nJg.md)
- **Recap:** Learn workflows before AI agents. Agents are nondeterministic, so they need more monitoring than rule-based flows. Core concepts in order: JSON and data types, APIs and HTTP requests, webhooks, logic and error handling, then LLM context engineering.
- **Money use (Possible angle):** Position as an automation or efficiency agency, which can work without AI. Price around time saved, money saved, and quality. Track results for case studies.

### 162. n8n's New Chat Hub Release: What You Need to Know
[Watch](https://www.youtube.com/watch?v=jx-yvSRLKrA) · 10 min · List #207 · [note](notes/207-jx-yvSRLKrA.md)
- **Recap:** Chat Hub is a ChatGPT-style interface inside n8n. It appears as a chat bubble in the bottom left (may need an n8n update). Chat with several models in one thread. Switching models keeps the conversation context. Add tools to a chat: a web search/URL reader tool (Jina AI) needs an API key and enabling each tool.
- **Money use (Skill-builder):** No direct money angle in the video. Skill to build: chat triggers, agent system prompts, tool setup, publishing workflows.

### 163. I built an AI Agent in 2 hours (and got paid $2600)
[Watch](https://www.youtube.com/watch?v=bxGE_LXPyAU) · 28 min · List #206 · [note](notes/206-bxGE_LXPyAU.md)
- **Recap:** Wireframe the client system before building. Here it is a student-onboarding pipeline with four flows. Flow 1: payment webhook triggers a welcome email, a Slack alert, and a new row in a Google Sheet "CRM" with computed follow-up dates.
- **Money use (Possible angle):** Sold to a YouTube-sourced business owner after discovery calls. He priced on outcomes, aiming for about a 10x first-year return on the price. Start by building demo agents and posting them. No rate card stated.

### 164. AI Agents Are Overused. Here's What to Build Instead
[Watch](https://www.youtube.com/watch?v=4OOS96i2gfI) · 11 min · List #205 · [note](notes/205-4OOS96i2gfI.md)
- **Recap:** A four-layer "AI systems pyramid": custom GPTs/projects, plain automation (no AI), AI workflows, then AI agents. Complexity, cost and maintenance rise going up. Decision test: must a human be in the loop every time (then custom GPT)? Is it pure rule logic (then workflow)? Is the step order fixed (then AI workflow)? Only open-ended, autonomous goals…
- **Money use (Possible angle (no price given)):** Sell quick-win automations that keep client costs low; lead with the simplest solution. No prices stated.

### 165. How to Actually Deliver AI Projects (APIs, Hosting & Handover Explained)
[Watch](https://www.youtube.com/watch?v=xxARTGo_Oqg) · 22 min · List #204 · [note](notes/204-xxARTGo_Oqg.md)
- **Recap:** Hosting: default to the client hosting n8n on their own account or instance, with you as a team member. Self-host for your own agency's internal use only. Security: use HTTPS and signed webhooks, never put secrets in URLs, add auth and rate limits, minimize personal data, and keep logs and payloads limited to those who need them.
- **Money use (Viable offer (price signal)):** Charge for the build and handover, then a separate maintenance retainer that excludes new features. Put scope and done criteria in writing. Pricing not stated.

### 166. Once You Know This, Building RAG Agents Becomes Easy in n8n
[Watch](https://www.youtube.com/watch?v=kOKavHnlPik) · 18 min · List #203 · [note](notes/203-kOKavHnlPik.md)
- **Recap:** Choose retrieval by question type. Filters for tabular data when a human would filter a spreadsheet; SQL when the question needs totals, averages, rankings or trends; Chunk-based vector retrieval loses structure: it returns a few chunks, so totals, averages and "highest week" answers can be wrong.
- **Money use (Skill-builder):** No direct money angle in the video. Inference: consulting on which retrieval method fits a client's data. Skill to build: retrieval design, prompt specification for filters, SQL generation, token-cost reasoning, Supabase….

### 167. I Built a New AI System in 3 Hours (and got paid $1650)
[Watch](https://www.youtube.com/watch?v=Q4iEslmyMyM) · 30 min · List #202 · [note](notes/202-Q4iEslmyMyM.md)
- **Recap:** Build an email assistant in n8n that a client talks to through Slack. Two tools: a Gmail search tool with received-after, received-before and sender filters the agent fills in itself, and a… Turn off the Gmail "simplify" option so full email bodies come back, not snippets.
- **Money use (Viable offer (price signal)):** Sold an inbox assistant for $1,650 (Nate's claim). Start by building small public demos, let prospects ask for custom builds, diagnose the bottleneck, and sell outcomes plus monitoring and iteration. He says he would not sell a generic email product, since big mail providers are adding AI.

### 168. I Built a Voice Agent That Calls Every New Lead (n8n + Vapi)
[Watch](https://www.youtube.com/watch?v=BO-jFbN4p8Y) · 27 min · List #201 · [note](notes/201-BO-jFbN4p8Y.md)
- **Recap:** On a form submission, normalize the phone number in a code node to exactly 10 digits, and route bad numbers to an "incorrect format" log instead of calling. Create an outbound call in Vapi via its API, passing the assistant ID, a phone number ID, and the lead's number with +1 prepended, plus variables for name, company and request.
- **Money use (Skill-builder):** No direct money angle in the video. Use case sold: automated lead qualification calls for service businesses. Pricing not given. Skill to build: phone normalization, API polling loops, structured-output schema design, voice-agent prompting,….

### 169. Easiest Way to Migrate n8n Workflows Between Accounts (cloud to self-hosted)
[Watch](https://www.youtube.com/watch?v=t1PTmpas0bg) · 11 min · List #200 · [note](notes/200-t1PTmpas0bg.md)
- **Recap:** Two-workflow migration with no AI: workflow A pulls every workflow from the old instance through the n8n node and logs ID and name in a Google Sheet with status "to process". Workflow B reads only rows marked "to process", fetches each workflow JSON by ID, creates it on the new instance through the n8n API, then marks the row done.
- **Money use (Skill-builder):** No direct money angle in the video. Inference: a paid migration service for agencies moving client n8n instances. Skill to build: n8n API usage, sheet-based state tracking, loop and filter design, credential setup.

### 170. Claude Code is Better at n8n than I am (Beginner's Guide)
[Watch](https://www.youtube.com/watch?v=B6k_vAjndMo) · 28 min · List #199 · [note](notes/199-B6k_vAjndMo.md)
- **Recap:** Describe a manual process to a chatbot, paste its output into Claude Code, and ask for an n8n workflow. Write a claude.md project prompt in plan mode, with questions about the n8n MCP and skills, then auto-accept it. Install the n8n MCP server and seven n8n skills; restart Claude Code to load them; test with a node search.
- **Money use (Skill-builder):** No direct money angle in the video. Context: he runs an AI automation agency focused on voice agents and says the demo newsletter is for that niche. Skill to build: plan-mode prompting, MCP and skill installation, API key setup, n8n workflow debugging, prompt….

### 171. Build ANYTHING with Claude Code & n8n (Beginner's Guide)
[Watch](https://www.youtube.com/watch?v=OCO3aq3G0mk) · 40 min · List #198 · [note](notes/198-OCO3aq3G0mk.md)
- **Recap:** Ask Claude Code to audit an existing n8n workflow for app use. It swapped the form trigger for a webhook, decoded a base64 image input, and added error branches that return a message to the… Plan mode first: answer its clarifying questions (repo strategy, Tailwind, dark theme), then auto-accept the plan so it writes a claude.md file.
- **Money use (Skill-builder):** No direct money angle in the video. Inference: sell a branded front end plus n8n backend as a custom micro-app for clients. No prices for clients given. Skill to build: workflow refactoring for webhooks, base64 handling, front-end scaffolding, git and deploy flow,….

### 172. I Built an AI System That Automates My Proposals (n8n + Gamma)
[Watch](https://www.youtube.com/watch?v=KGXFkUlBHxw) · 21 min · List #197 · [note](notes/197-KGXFkUlBHxw.md)
- **Recap:** Split the system into two n8n workflows: one logs each finished meeting from Fireflies into a Google Sheet, the other turns a logged meeting into a proposal. Poll Fireflies in a wait-and-check loop until its AI summary fields exist, since they are not ready when the transcript webhook fires.
- **Money use (Skill-builder):** No direct money angle in the video. for pricing. Use case: proposals and meeting minutes for consultants or agencies after sales calls. He says he used to do this part of his job manually. Skill to build: webhook and polling design, code-node writing with an LLM, approval gates, prompt structuring, API….

### 173. Master 95% of Claude Code in 36 Mins (as a beginner)
[Watch](https://www.youtube.com/watch?v=saggDHHnmtQ) · 37 min · List #196 · [note](notes/196-saggDHHnmtQ.md)
- **Recap:** Install VS Code and the Claude Code extension, open a dedicated project folder, and sign in with a paid Anthropic plan. Write a claude.md project file describing a three-layer setup: markdown workflows (SOPs), an agent that coordinates them, and Python tools that do the deterministic work.
- **Money use (Skill-builder):** No direct money angle in the video. The demo is a weekly branded AI-niche trend report he says he would share with a team. Inference: sell recurring branded market reports or a custom research pipeline. No price given. Skill to build: project setup, claude.md authoring, plan-mode prompting, Python tooling, OAuth, secrets handling,….

### 174. I Will Never Fix Another n8n Workflow (Claude Code)
[Watch](https://www.youtube.com/watch?v=uUEa6K-FLB8) · 13 min · List #195 · [note](notes/195-uUEa6K-FLB8.md)
- **Recap:** Point an n8n production workflow's error workflow at a second workflow. On failure, that one sends the failed node, workflow ID and error text through a tunnel to a Claude Code session… Claude Code uses the n8n MCP server and n8n skills to read the broken workflow, find the root cause, edit the live workflow and post the result to ClickUp.
- **Money use (Skill-builder):** No direct money angle in the video. Inference: a self-healing monitoring setup could be sold as an ongoing maintenance retainer for client workflows. Skill to build: error-workflow design, tunneling, MCP and skill setup, n8n expression and JSON debugging, failure….

### 175. Agentic Workflows Just Changed AI Automation Forever! (Claude Code)
[Watch](https://www.youtube.com/watch?v=AO5aW01DKHo) · 22 min · List #194 · [note](notes/194-AO5aW01DKHo.md)
- **Recap:** Agentic workflows: describe the outcome in plain English; the agent plans, asks questions, builds, and repairs its own steps, unlike node-by-node n8n builds. Four shifts: self-healing (agent reads errors and fixes code), natural-language iteration, security review on every change with rules set in plain language, and instant API/MCP integrations.
- **Money use (Possible angle (no price given)):** Custom lead-gen automations (e.g., a Chicago dentist lead list with outreach copy, as in the demo), plus ongoing maintenance and expansion. Nate says clients pay for problem definition, integration with messy systems, and upkeep more than the build. No prices quoted.

### 176. Set Up Clawdbot on a VPS in Minutes (no mac mini)
[Watch](https://www.youtube.com/watch?v=BhjK2Gr0Ryc) · 13 min · List #193 · [note](notes/193-BhjK2Gr0Ryc.md)
- **Recap:** Why a VPS: an open-source agent with broad system access should run on a separate machine, not your main computer. Steps: order a VPS, set a root password, SSH in, create a non-root user, run the one-line installer, and finish onboarding.
- **Money use (Possible angle (no price given)):** Hosted always-on assistant setup (VPS, Telegram, API keys, security) could be a client service. No client pricing stated.

### 177. 100 Hours Testing Clawdbot vs Claude Code (honest results)
[Watch](https://www.youtube.com/watch?v=CBNbcbMs_Lc) · 23 min · List #192 · [note](notes/192-CBNbcbMs_Lc.md)
- **Recap:** Head-to-head scorecard of Claude Code vs Clawdbot (later renamed Moltbot) across eight categories: out-of-box ability, setup and risk, cost, power and access, security, everyday usability,… Claude Code is better for developers, lower risk, and proven ROI. Clawdbot is better for always-on personal use (Telegram, proactive reminders, background tasks).
- **Money use (Possible angle (no price given)):** Clawdbot-style assistants could be sold as hosted setups or managed services, but Nate says ROI is unproven. Cost planning matters: API charges can outrun a subscription. No client prices quoted.

### 178. I Turned Clawdbot Into the Ultimate Personal Assistant
[Watch](https://www.youtube.com/watch?v=rlJovzVhlIo) · 26 min · List #191 · [note](notes/191-rlJovzVhlIo.md)
- **Recap:** Build an always-on AI executive assistant ("Klouse") on Clawdbot, reached through Telegram. Onboard it by letting it interview you, which creates identity and user files (soul.md, user.md). Give the bot its own email, calendar, drive, and task accounts instead of your main ones. Keep API keys in a .env file, and start with read-only access.
- **Money use (Possible angle):** Could be sold as an "AI executive assistant" setup or a custom dashboard-plus-heartbeat build for small businesses. No price quoted; Nate is unsure of ROI.

### 179. Is n8n Dead?
[Watch](https://www.youtube.com/watch?v=wb4uDdsFh6o) · 5 min · List #190 · [note](notes/190-wb4uDdsFh6o.md)
- **Recap:** - n8n is not dead: it stays a strong choice for workflow automation thanks to its visual builder and low barrier to entry. Beginners should start there. Claude Code is better for custom code and reasoning through it, but harder to deploy and monitor for scheduled or webhook jobs. Use Claude Code as a teacher: ask it what it did and why.
- **Money use (Skill-builder):** No direct money angle in the video. (opinion and tool-choice video). Implied: clients may want n8n skills, so pick the tool clients can maintain. Skill to build: n8n workflow building, Claude Code basics, deployment and monitoring trade-offs.

### 180. How to Sign Your First AI Automation Client in 7 days (With Proof)
[Watch](https://www.youtube.com/watch?v=c2C_SbZk6iI) · 21 min · List #189 · [note](notes/189-c2C_SbZk6iI.md)
- **Recap:** Guest Christian's story: positioning as a guide and partner, not a template seller, plus a discovery-call approach focused on finding pain points. A 7-day warm-first plan: day 1 write a loose offer hypothesis and a list of 20 trusted contacts; days 2-3 hold 5-10 low-pressure conversations; Cold outreach comes last, after a few warm cycles give proof.
- **Money use (Viable offer (price signal)):** Sell AI workflows to local or small businesses. Start with a free pilot, then charge $1,500-$2,000 for a first build (Christian's numbers). Upsell maintenance (monthly) and expansion (bigger scope). Ask for testimonials and intros after proof.

### 181. How I'd Teach a 10 Year Old to Build Agentic Workflows (Claude Code)
[Watch](https://www.youtube.com/watch?v=3GAxd90fEE4) · 28 min · List #188 · [note](notes/188-3GAxd90fEE4.md)
- **Recap:** Agentic workflow = state the goal in plain language; the agent plans steps, asks clarifying questions, and self-corrects. Contrast with node-by-node automation. WAT framework: workflows (plain-language markdown SOPs), agent (Claude Code), tools (Python scripts), with a CLAUDE.md and folders for each.
- **Money use (Possible angle (no price given)):** Build agentic lead-gen and data-pull tools for clients (dentist contact lists, job listings). No client prices quoted.

### 182. Turn Any Website Into LLM Ready Data INSTANTLY
[Watch](https://www.youtube.com/watch?v=4efAzBiTeVo) · 11 min · List #187 · [note](notes/187-4efAzBiTeVo.md)
- **Recap:** Firecrawl's MCP server lets Claude Code choose the right web tool (scrape, map, crawl, search) from a plain-language request. Setup: store the API key in a .env file, connect the MCP server, reload the editor. Keep a tools cheat-sheet file and a short CLAUDE.md that points to it, so the project knows its own tools.
- **Money use (Possible angle (no price given)):** Scraped lead lists, job-board datasets, brand and competitor research, and data prep for AI apps could be sold as deliverables. No prices for client work stated.

### 183. How a College Student Made $500k with Cold Email (Exact Framework)
[Watch](https://www.youtube.com/watch?v=XB2xmX3USUI) · 37 min · List #186 · [note](notes/186-XB2xmX3USUI.md)
- **Recap:** Guest Sav (student, AI agency) shows a cold email system from zero: free proof projects first, then paid work once results show. Build lead lists from niche industry databases (e.g., architecture association directories), which are already filtered.
- **Money use (Possible angle (no price given)):** Sell outbound lead generation or AI outreach to agencies and service businesses. Start free, convert to paid after proof, and collect case studies. No price points beyond pay-on-results.

### 184. How to Sign AI Workflow Clients (With 0 Followers)
[Watch](https://www.youtube.com/watch?v=_rZAR-s4KIo) · 14 min · List #185 · [note](notes/185-_rZAR-s4KIo.md)
- **Recap:** Land AI automation clients without a YouTube audience, using three paths: cold outreach, referrals, and partner-led deals. Get proof first (even free or small projects), then use it as a case study in outreach.
- **Money use (Viable offer (price signal)):** Sell AI automation to small and B2B businesses. Start with free or discounted proof projects, then charge once results show. Partner with agencies and consultants who already have clients (offer free AI audits, take a revenue share). No price points beyond the 20% share.

### 185. Building Beautiful Websites with Claude Code Is Too Easy
[Watch](https://www.youtube.com/watch?v=86HM0RUWhCk) · 28 min · List #184 · [note](notes/184-86HM0RUWhCk.md)
- **Recap:** Five hacks for professional-looking sites: (0) a CLAUDE.md file as the standing system prompt; (1) a front-end design skill installed globally; Keep a brand_assets folder with logo and brand guidelines, and tag the files in chat so the agent uses them. Work on localhost until you approve, then commit and push to GitHub; Vercel auto-deploys from the repo.
- **Money use (Skill-builder):** No direct money angle in the video. The workflow is framed as building client-ready sites, but no pricing or offer is given. Skill to build: CLAUDE.md design, front-end design, screenshot-based QA, site cloning, component reuse, GitHub,….

### 186. The EASIEST Way to Host Your Claude Code Agents
[Watch](https://www.youtube.com/watch?v=UGIZnh6HNLc) · 21 min · List #183 · [note](notes/183-UGIZnh6HNLc.md)
- **Recap:** Describe the automation in plain English, let Claude Code write TypeScript tasks, then deploy them to trigger.dev so they run in the cloud. Make tasks idempotent: check the destination (a ClickUp list) before creating items, so duplicates are skipped.
- **Money use (Possible angle (no price given)):** Example: a weekly list of dental practices as sales leads for selling websites. Nate frames these automations as something you build for clients. No prices given.

### 187. From Zero to Your First Agentic AI Workflow in 26 Minutes (Claude Code)
[Watch](https://www.youtube.com/watch?v=tDGiWn0flK8) · 26 min · List #182 · [note](notes/182-tDGiWn0flK8.md)
- **Recap:** Traditional automation (Make, n8n) means wiring each step yourself. An agentic workflow states the outcome and lets the agent reason, pick tools, ask clarifying questions and recover from… WAT framework: Workflows (markdown SOPs), Agent (Claude Code as coordinator), Tools (Python scripts that do one action each).
- **Money use (Possible angle):** Implied: monthly competitor-intel PDF reports for businesses. Nate says the aim is to build automations for businesses; no prices given.

### 188. I Can Actually Watch My AI Agents Work Now
[Watch](https://www.youtube.com/watch?v=62Rfe1w9NBc) · 12 min · List #181 · [note](notes/181-62Rfe1w9NBc.md)
- **Recap:** Three ways to run several agents: parallel agents (separate terminals, each its own task), sub-agents (a parent delegates to children with their own context and optionally a different… Pixel Agents, a VS Code extension, turns each Claude Code agent into an animated character in a virtual office, driven by Claude Code's activity log.
- **Money use (Skill-builder):** No direct money angle in the video. Skill to build: multi-agent orchestration, sub-agent delegation, VS Code setup, extension security review.

### 189. Claude Code Just Added What Everyone Wanted (Remote Control)
[Watch](https://www.youtube.com/watch?v=EqhKw0Oro_k) · 8 min · List #180 · [note](notes/180-EqhKw0Oro_k.md)
- **Recap:** Start with `claude remote-control` in the terminal (or `/remote-control` in an existing session) to get a URL and QR code, then open it on a phone or browser to continue the local session. The session runs on your machine, so files stay local; only model calls go to Anthropic. Work done on the phone shows up in the desktop conversation history.
- **Money use (Skill-builder):** No direct money angle in the video. Skill to build: Claude Code CLI, remote session management, basic session security.

### 190. Master 95% of Claude Code Skills in 28 Minutes
[Watch](https://www.youtube.com/watch?v=zKBPwDpBfhs) · 27 min · List #179 · [note](notes/179-zKBPwDpBfhs.md)
- **Recap:** A skill is a folder with a SKILL.md file: YAML front matter (name, description) plus step-by-step instructions. Progressive loading: the agent first reads only name and description (around 100 tokens), loads the full SKILL.md when chosen, and loads extra files only when needed.
- **Money use (Possible angle):** Skills can be shared, sold or downloaded on marketplaces, which he says could be a business, though he warns not to rely on it. He also notes teams can use a skill as an SOP automation. No prices given.

### 191. The NEW Nano Banana 2 + Antigravity Destroys Every AI Image Tool
[Watch](https://www.youtube.com/watch?v=iTKkoGd3YcM) · 15 min · List #178 · [note](notes/178-iTKkoGd3YcM.md)
- **Recap:** Nano Banana 2 (Google's image model): Nate says it is faster and cheaper than Nano Banana Pro, with better text rendering and optional Google Search grounding for current facts. JSON prompting: break a prompt into fields (subject, composition, camera, lighting, style, aspect ratio, negative prompt) to get more consistent output.
- **Money use (Possible angle):** Implied: product ad photos and infographics for businesses (his example is a cologne bottle ad). No pricing for services stated.

### 192. The NEW Nano Banana 2 + Claude Code = $10k Websites
[Watch](https://www.youtube.com/watch?v=q0TgUtj6vIs) · 20 min · List #177 · [note](notes/177-q0TgUtj6vIs.md)
- **Recap:** Scroll-driven product sites: generate a start frame and an end frame with an image model, animate them into a short video, then split the video into roughly 100+ WebP frames with FFmpeg. Map each frame to a scroll position, so the product "plays" as the visitor scrolls up or down.
- **Money use (Possible angle (no price given)):** Build a demo site for a niche (his example: a blender brand), then email or visit local businesses and sell a custom site with their copy and products. Add hosting and maintenance fees.

### 193. Turn Claude Code Into Your Executive Assistant in 27 Mins
[Watch](https://www.youtube.com/watch?v=mi4hcipESKQ) · 27 min · List #176 · [note](notes/176-mi4hcipESKQ.md)
- **Recap:** Four phases: give the assistant a home (a folder and git repo), give it rules and context (a short CLAUDE.md that points to separate me, work, team and priorities files), give it hands…
- **Money use (Possible angle):** Nate says the setup could potentially be sold, and suggests turning existing Claude Projects and custom GPTs into skills. No prices given.

### 194. Claude Code Skills Just Got Even Better
[Watch](https://www.youtube.com/watch?v=RAZVk5NPNtE) · 16 min · List #175 · [note](notes/175-RAZVk5NPNtE.md)
- **Recap:** A skill is a text recipe (a markdown file of instructions) that the agent reads before doing a task. Two skill types: capability-uplift skills teach a task the base model does poorly (e.g. front-end design), and encoded-preference skills capture your own fixed multi-step process.
- **Money use (Skill-builder):** No direct money angle in the video. He frames skills as leverage for managers and operators rather than as a product to sell. Skill to build: skill authoring, evals, benchmarking, trigger tuning, plugin install, parallel sub-agents, PDF….

### 195. Cursor Automations Clearly Explained (worth learning?)
[Watch](https://www.youtube.com/watch?v=NDnv16PY2XQ) · 9 min · List #174 · [note](notes/174-NDnv16PY2XQ.md)
- **Recap:** Cursor Automations are trigger-based coding agents that run in Cursor's cloud sandbox, with your repo loaded, and launch on events rather than manual prompts. Triggers: schedules, GitHub events, Slack messages, Linear issues, PagerDuty incidents, custom webhooks.
- **Money use (Skill-builder):** No direct money angle in the video. Implied: engineering teams would pay for always-on review and monitoring agents. Skill to build: event-driven agent design, comparing agent platforms, code review and security automation,….

### 196. Claude Code 2.0 Is Finally Here
[Watch](https://www.youtube.com/watch?v=BlNJFa3Btm8) · 10 min · List #173 · [note](notes/173-BlNJFa3Btm8.md)
- **Recap:** Scheduled tasks in the Claude Code desktop app: create from the Schedule tab or with /schedule in a session, set a prompt, model, folder and time. Convert an existing skill into a scheduled task by asking Claude Code to read the skill and set it up (his "morning coffee" skill now runs at 6 a.m.).
- **Money use (Skill-builder):** No direct money angle in the video. Skill to build: scheduling agents, permission hardening, stateless-run memory design, hooks, self-improving prompts.

### 197. This New Claude Code Feature is a Game Changer
[Watch](https://www.youtube.com/watch?v=OUyfxhFtGCo) · 9 min · List #172 · [note](notes/172-OUyfxhFtGCo.md)
- **Recap:** The built-in loop skill lets Claude Code schedule recurring prompts or one-time reminders in natural language (for example, "every 10 minutes check my ClickUp"), using cron create, list and… Loops run inside the current session, so each check sees the earlier results. This raises context use, so keep reports short.
- **Money use (Skill-builder):** No direct money angle in the video. Skill to build: scheduling prompts, cron basics, choosing between loops and scheduled tasks, context management for….

### 198. How to Build $10,000 Agentic Workflows (Claude Code Tutorial)
[Watch](https://www.youtube.com/watch?v=vFepZE_wrfg) · 25 min · List #171 · [note](notes/171-vFepZE_wrfg.md)
- **Recap:** Use the WAT framework (workflows as markdown, agent, tools): the agent reads the workflow and runs Python tools; the claude.md sets project rules. Plan mode first: state the goal loosely, let Claude Code ask questions, then approve the plan and tech stack.
- **Money use (Viable offer (price signal)):** sell agentic workflow builds to businesses for leads, onboarding or data-entry problems. Price by value (time saved, money saved), start hourly for early trust, then move to fixed value-based fees and ongoing optimization. Find clients through conversations (he links a separate video).

### 199. Google's New Tool Just 10x'd Claude Code
[Watch](https://www.youtube.com/watch?v=Wu67lLD8bB0) · 12 min · List #170 · [note](notes/170-Wu67lLD8bB0.md)
- **Recap:** Install Google's open-source Workspace CLI (GWS) so Claude Code can act on Drive, Gmail, Calendar, Docs, Sheets and Slides through bash commands instead of MCP or raw API calls.
- **Money use (Skill-builder):** No direct money angle in the video. He presents a free alternative to a paid slide tool (Gamma). Skill to build: CLI setup, OAuth configuration, Google Workspace automation, visual QA of generated slides, email….

### 200. I Taught Claude Code to Play Tetris... It Broke the World Record
[Watch](https://www.youtube.com/watch?v=l1jnOXc52NY) · 8 min · List #169 · [note](notes/169-l1jnOXc52NY.md)
- **Recap:** Browser automation from inside Claude Code: it drives real tabs to fill forms, search a retailer, and download reports where no API exists. Training loop: have the agent play a game, screenshot the result, explain what went wrong, update its bot script, and retry until a target score is reached.
- **Money use (Skill-builder):** No direct money angle in the video. He suggests browser automation for tasks without an API, and turning working scripts into skills. Skill to build: browser automation, iterative debugging of bot logic, feedback-loop prompting, parallel sessions,….

### 201. Google's New Model + Claude Code Just Changed RAG Forever
[Watch](https://www.youtube.com/watch?v=hem5D1uvy-w) · 15 min · List #168 · [note](notes/168-hem5D1uvy-w.md)
- **Recap:** Google's Gemini Embedding 2 is a natively multimodal embedding model, so text, images, video, audio and documents can share one vector space. Build a multimodal RAG app by describing it to Claude Code in plan mode, pasting the API docs URL, and having it generate the project, a .env with placeholders, and the ingestion pipeline.
- **Money use (Possible angle (no price given)):** implied, not stated in detail. A roofing or contracting firm could offer searchable past-project lookup for quotes. He notes it needs subject-matter data to be useful.

### 202. Build & Sell with Claude Code (10+ Hour Course)
[Watch](https://www.youtube.com/watch?v=mpALXah_PBg) · 600 min · List #167 · [note](notes/167-mpALXah_PBg.md)
- **Recap:** Course outline (24 chapters, from setup through monetization; covers CLAUDE.md, deployment, RAG, MCPs, skills, sub-agents, browser automation, permissions and git worktrees). Build a newsletter automation in plan mode with the WAT framework (workflows as markdown, agent, tools), then fix real errors in a test run.
- **Money use (Viable offer (price signal)):** Build agentic workflows (for example, a personal assistant wired to a client's CRM, calendar and email) and sell them as fixed-scope projects. Clients pay for their own API usage. Charge for the build on completion, then offer a maintenance retainer (bug fixes, tweaks, monitoring). New features go to a separate project.

### 203. Generate Content for 9 Socials on Autopilot with Claude Code
[Watch](https://www.youtube.com/watch?v=4Zaoo0YbYaw) · 17 min · List #166 · [note](notes/166-4Zaoo0YbYaw.md)
- **Recap:** Install Claude Code as a VS Code extension, open a project folder, and prompt it to create a "repurpose YouTube video" skill that outputs LinkedIn, Instagram and X posts with visuals.
- **Money use (Skill-builder):** No direct money angle in the video. He uses the workflow for his own channel. The reusable pattern (a tested skill plus a posting API) could be offered as a content service, but he does not say so. Skill to build: Claude Code setup, writing skills, MCP and API configuration, content repurposing, CLAUDE.md,….


## Phase 2: Claude Code, skills and selling AI services

### 204. Stop Learning n8n in 2026...Learn THIS Instead
[Watch](https://www.youtube.com/watch?v=ZeJXI2MAhj0) · 19 min · List #165 · [note](notes/165-ZeJXI2MAhj0.md)
- **Recap:** Argues that drag-and-drop automation builders (n8n, Make, Zapier) are being replaced by agentic workflows that you describe in natural language and an agent implements. Compares building a "check a YouTube channel every 8 hours, dedupe, summarize, deliver" automation by hand in n8n (schedule, HTTP request, dedupe store, transcript, LLM step, write-back)…
- **Money use (Skill-builder):** No direct money angle in the video. He frames agent-building as a skill that stays valuable as the tools change. Skill to build: agent design, Trigger.dev deployment, ClickUp integration, deduplication by idempotency key, async….

### 205. How to Build Claude Agent Teams Better Than 99% of People
[Watch](https://www.youtube.com/watch?v=vDVSGVpB2vc) · 17 min · List #164 · [note](notes/164-vDVSGVpB2vc.md)
- **Recap:** Agent teams differ from sub-agents: a team lead creates teammates that share a task list and can message each other directly, while sub-agents only report results back to the main session. Enable the experimental agent teams feature with one environment variable in the project's local settings file.
- **Money use (Skill-builder):** No direct money angle in the video. Skill to build: Claude Code configuration, multi-agent orchestration, prompt design, QA-loop workflow,….

### 206. This $100M AI App Just Changed Software Forever
[Watch](https://www.youtube.com/watch?v=T6_Ges4j1qY) · 9 min · List #163 · [note](notes/163-T6_Ges4j1qY.md)
- **Recap:** Case study of Cal AI, a food-photo calorie tracker, built fast with AI coding tools and sold to a competitor. Start from a problem you or people around you have, then ship the simplest version quickly and iterate.
- **Money use (Viable offer (price signal)):** Mobile or web app builders who can ship a single-purpose AI utility. Start by finding a problem in your own life, build a minimal version, then sell creator-led promotion with a flat-fee bundle. Price points stated: about $30/year subscription. Start with 20-30 niche creators and track results per video.

### 207. Claude Code Just Got Another Huge Upgrade
[Watch](https://www.youtube.com/watch?v=X6EGzi9qm3E) · 8 min · List #162 · [note](notes/162-X6EGzi9qm3E.md)
- **Recap:** Computer use lets Claude Code see the screen, move the mouse, type, and take screenshots on a Mac (research preview, desktop app only). Enable it in the desktop app's general settings, then grant per-app permissions (Finder, ClickUp, etc.) when the session first uses them.
- **Money use (Skill-builder):** No direct money angle in the video. Nate hints at automating legacy desktop apps that have no API and at QA-clicking through apps in a sandbox, but he does not price either. Skill to build: enabling computer use, per-app permission setup, prompting for desktop actions, phone dispatch,….

### 208. Claude Code Just Dropped Memory 2.0
[Watch](https://www.youtube.com/watch?v=LrgfmZkl3nc) · 8 min · List #161 · [note](notes/161-LrgfmZkl3nc.md)
- **Recap:** Auto Dream is an experimental Claude Code feature. A background sub-agent periodically consolidates the auto-memory files: it merges, prunes, and rewrites them so new sessions start from a… Three layers: normal coding sessions, auto memory (records decisions and project patterns), and Auto Dream (periodic cleanup without manual prompting).
- **Money use (Skill-builder):** No direct money angle in the video. Skill to build: Claude Code memory management, slash commands, status line reading, reviewing and restoring agent….

### 209. STOP Using Bypass Permissions, Use This New Feature Instead
[Watch](https://www.youtube.com/watch?v=pkSxISewcw8) · 6 min · List #160 · [note](notes/160-pkSxISewcw8.md)
- **Recap:** Default "ask before edits" mode interrupts long sessions with a prompt for every edit, web fetch, or bash command. Bypass-permissions mode removes all prompts, which is risky if you are not watching. Nate's older fix was a local settings file with an allow list and a deny list, set per project or globally.
- **Money use (Skill-builder):** No direct money angle in the video. Skill to build: Claude Code permission modes, settings-file allow/deny configuration, org admin setup, risk….

### 210. Claude Code + iMessage is Finally Here.
[Watch](https://www.youtube.com/watch?v=hHlpVeooPrI) · 10 min · List #159 · [note](notes/159-hHlpVeooPrI.md)
- **Recap:** Claude Code "channels" are MCP servers that push events from a chat app into a running session, so you can message Claude from your phone and have it act as if you typed locally. Setup: grant full disk access to the terminal app (or VS Code), install the iMessage plugin via the plugin menu, then launch Claude Code in channel mode so it listens for messages.
- **Money use (Skill-builder):** No direct money angle in the video. Skill to build: Claude Code channel setup, MCP plugin install, permission approval over chat, multi-session routing….

### 211. Gemini 3.1 Flash Live Just Changed Voice Agents Forever
[Watch](https://www.youtube.com/watch?v=Qt3zMBH-FNg) · 19 min · List #158 · [note](notes/158-Qt3zMBH-FNg.md)
- **Recap:** Gemini 3.1 Flash Live is speech-to-speech (no separate speech-to-text and text-to-speech steps), with lower latency and better interruption handling. Prototype a voice agent for free in Google AI Studio: pick the Live model, save system instructions (persona, tone), toggle function calling and search grounding.
- **Money use (Possible angle):** voice agents for e-commerce, support, sales, booking and calendar tasks. Nate says embedding on a live site needs a hosted server, so it is harder than ElevenLabs.

### 212. Claude Code + Paperclip Just Destroyed OpenClaw
[Watch](https://www.youtube.com/watch?v=HJ-dwefABss) · 21 min · List #157 · [note](notes/157-HJ-dwefABss.md)
- **Recap:** Paperclip is an open-source (MIT) dashboard for orchestrating a team of AI agents: org chart, goals, tickets, approvals, budgets. Launch it from a terminal; it serves a local dashboard, with a VPS option for remote access.
- **Money use (Skill-builder):** No direct money angle in the video. the video is a tool walkthrough. A possible angle is setting up agent companies for clients. Skill to build: agent org design, orchestration, Claude Code project setup, skill installation, secrets management.

### 213. I've Built 500 AI Workflows, This is What Businesses Want in 2026
[Watch](https://www.youtube.com/watch?v=Y3PcRp5RFzk) · 15 min · List #156 · [note](notes/156-Y3PcRp5RFzk.md)
- **Recap:** Five simple automations sell best: speed-to-lead, document processing, follow-up sequences, database reactivation, internal reporting. Sell the outcome (time saved, cost cut, revenue recovered), not the workflow itself. Pick one workflow, learn it deeply and build a simple demo, then either niche down or act as a generalist consultant.
- **Money use (Possible angle (no price given)):** Sell to service businesses (dental, law, HVAC, real estate, agencies), accountants and insurers (document processing), coaches and gyms (follow-up and reactivation). Price against ROI math from the client's own numbers. Start with one niche and build a demo.

### 214. Codex Just 10x'd Claude Code Projects
[Watch](https://www.youtube.com/watch?v=B2Kh_ZoLVTM) · 13 min · List #155 · [note](notes/155-B2Kh_ZoLVTM.md)
- **Recap:** OpenAI released an official Codex plugin for Claude Code; setup is three commands (add marketplace, install plugin, run setup). Common pattern: plan and build a proof of concept in Claude Code, then bring Codex in for review and production hardening.
- **Money use (Skill-builder):** No direct money angle in the video. Skill to build: Claude Code plugins, code review, multi-model workflows, git branch diffs.

### 215. Claude Code Source Code Just Leaked… 8 Things You Must Do
[Watch](https://www.youtube.com/watch?v=tXtCK66fPj8) · 13 min · List #154 · [note](notes/154-tXtCK66fPj8.md)
- **Recap:** Claude Code is a full agent runtime (CLI parser, query engine, tool loop, memory, permissions, multi-agent coordinator, MCP client and server), not just a chat window in a terminal, per… Keep CLAUDE.md short and operational: conventions, constraints and decision rules, not project history. Load it at global or project level.
- **Money use (Skill-builder):** No direct money angle in the video. (only token-cost savings from compacting and context hygiene) Skill to build: Claude Code configuration, permission rules, context management, prompt decomposition, MCP setup.

### 216. Claude Code Just Gave Everyone Virtual Pets (April Fools?)
[Watch](https://www.youtube.com/watch?v=JoPmpwpRrBI) · 7 min · List #153 · [note](notes/153-JoPmpwpRrBI.md)
- **Recap:** Claude Code added a `/buddy` command (from version 2.1.89) that hatches a terminal companion pet. One buddy per account, seeded from your user ID, so starting a new session or re-running `/buddy` does not give a new one. Stats (debugging, patience, chaos, wisdom, snark) and a name come from your coding habits, per Nate.
- **Money use (Skill-builder):** No direct money angle in the video. Skill to build: Claude Code slash commands, terminal setup, plan mode, `/btw` for side questions.

### 217. 18 Claude Code Token Hacks in 18 Minutes
[Watch](https://www.youtube.com/watch?v=49V-5Ock8LU) · 19 min · List #152 · [note](notes/152-49V-5Ock8LU.md)
- **Recap:** Each message rereads the whole conversation, so cost compounds. He cites a developer finding that 98.5% of tokens in a 100-message chat went to rereading history. Tier 1: /clear between unrelated tasks, disconnect unused MCP servers, batch prompts into one message, use plan mode, check /context and /cost, add a status line, watch Claude work, and…
- **Money use (Skill-builder):** No direct money angle in the video. He argues most users need better context habits, not a bigger plan. Skill to build: Claude Code slash commands (/clear, /compact, /context, /cost, status line), CLAUDE.md design, MCP….

### 218. Ollama + Claude Code = 99% CHEAPER
[Watch](https://www.youtube.com/watch?v=O2k_qwZA8HU) · 25 min · List #151 · [note](notes/151-O2k_qwZA8HU.md)
- **Recap:** Claude Code is a harness. You can swap the model behind it for a free or cheaper one. Method 1, local: install Ollama, pull an open model (he used Qwen 3.5 9B, a 6.6 GB download), then launch Claude Code through Ollama. Local models often fail on tool calls or small context windows. Fix: build a custom Ollama model with a larger context (he used 64k).
- **Money use (Possible angle (no price given)):** Cheap or free models suit low-stakes work: summarizing, file search, triage, scaffolding. Nate suggests using them for those tasks and keeping a stronger model for hard work. No price is set for selling anything.

### 219. Andrej Karpathy Just 10x'd Everyone's Claude Code
[Watch](https://www.youtube.com/watch?v=sboNwYmH3AY) · 18 min · List #150 · [note](notes/150-sboNwYmH3AY.md)
- **Recap:** Karpathy's "LLM knowledge base" pattern: a raw folder of sources, an LLM-maintained wiki folder, an index file, a log, and a CLAUDE.md schema that defines the rules. Setup: create an Obsidian vault, paste the idea file into Claude Code, and let it create the folders.
- **Money use (Skill-builder):** No direct money angle in the video. He treats the wiki as a personal or business second brain. Skill to build: knowledge-base design, Obsidian, CLAUDE.md schema writing, web clipping, project organization, lint….

### 220. Planning In Claude Code Just Got a Huge Upgrade
[Watch](https://www.youtube.com/watch?v=T4fXb3sbJIo) · 16 min · List #149 · [note](notes/149-T4fXb3sbJIo.md)
- **Recap:** "Ultra plan" runs Claude Code's planning in Anthropic's cloud. Start it from the CLI with the slash command or by writing the keyword in a prompt. Review the plan on the web: comment on sections, add emoji reactions. Approving it "teleports" the plan back to the terminal for execution.
- **Money use (Skill-builder):** No direct money angle in the video. Skill to build: Claude Code plan mode, Git sync, web plan review, comment-driven plan revision, custom skill….

### 221. Claude's New AI Just Changed the Internet Forever
[Watch](https://www.youtube.com/watch?v=DG1wRgEpdO4) · 8 min · List #148 · [note](notes/148-DG1wRgEpdO4.md)
- **Recap:** Anthropic's unreleased model, Claude Mythos, was trained to be a stronger coder. That same skill made it strong at finding security flaws. Reported finds (Nate's summary): a 27-year-old OpenBSD bug, an FFmpeg bug that automated tests had missed, Linux bugs that let a zero-permission user become admin, and chaining small bugs…
- **Money use (Skill-builder):** No direct money angle in the video. He speculates that scanning tools may reach smaller companies later, but gives no product, price or steps. Skill to build: AI security awareness, reading AI safety news.

### 222. I Tested Claude's New Managed Agents... What You Need To Know
[Watch](https://www.youtube.com/watch?v=27Y44JYXZJ8) · 17 min · List #147 · [note](notes/147-27Y44JYXZJ8.md)
- **Recap:** Managed Agents sit in the Claude Console. You pick a template or describe an agent in chat, and it drafts the name, model, system prompt, tools and skills. Setup has five steps: create the agent, configure a cloud environment (networking rules), connect tools through OAuth into a shared credential vault, start a session, then test-run it.
- **Money use (Viable offer (price signal)):** Aimed at people who live in Claude chat and want agents without infrastructure. Example use: a delegated research agent that picks up ClickUp tasks. No selling price is given. A start: $5 API credit, one template, one test run. Nate's view: experienced builders may find trigger.dev plus the Agent SDK cheaper.

### 223. I Gave OpenClaw $10,000 to Trade Stocks
[Watch](https://www.youtube.com/watch?v=eu8UJtuIi-E) · 19 min · List #146 · [note](notes/146-eu8UJtuIi-E.md)
- **Recap:** A 30-day experiment: two always-on bots (OpenClaw-based, per title), each given $10,000 of real cash, with an email inbox and a Telegram/Discord control channel. Setup: a cron job every 30 minutes during trading hours; a prompt telling the agent to spin up sub-agents to research and trade on its own.
- **Money use (Skill-builder):** No direct money angle in the video. sold in the video. Disclaimer: Nate says this is not financial advice and not a recommendation to hand money to a bot. Skill to build: always-on agent setup, cron scheduling, multi-agent prompting, agent-to-agent email, risk management.

### 224. Claude Just Told Us to Stop Using Their Best Model
[Watch](https://www.youtube.com/watch?v=1EPsUXSManU) · 15 min · List #145 · [note](notes/145-1EPsUXSManU.md)
- **Recap:** The advisor strategy (beta, Messages API): a cheaper executor model (Sonnet or Haiku) does most steps and calls Opus only when it needs help, via a tool-style request. Set a max-uses cap on advisor calls to control cost. Messages API vs Claude Code vs Agent SDK: the API is for building your own app; Claude Code is a finished coding tool.
- **Money use (Possible angle (no price given)):** Build cost-optimized chatbots or support agents for clients and charge for the routing design. No prices quoted for that work.

### 225. Seedance 2.0 + Claude Code Creates $10k Websites in Minutes
[Watch](https://www.youtube.com/watch?v=NvxiSG34mPU) · 23 min · List #144 · [note](notes/144-NvxiSG34mPU.md)
- **Recap:** Generate a seamless-loop hero video with an AI video model. Use a generated image as both first and last frame so the loop joins cleanly. Have Claude Code write the video prompt from a skill file and a reference image, then review the result before generating.
- **Money use (Viable offer (price signal)):** Pitch cinematic landing pages to architecture, auto, and service firms. Title "$10k websites" is Nate's framing, not a stated client price. Start with one demo site for a local business.

### 226. This One Plugin Just 10x'd Claude Code
[Watch](https://www.youtube.com/watch?v=4XqVR6xI6Kw) · 15 min · List #143 · [note](notes/143-4XqVR6xI6Kw.md)
- **Recap:** Superpowers is a free open-source Claude Code plugin that adds a set of skills enforcing a disciplined workflow: clarify, design, plan, code, verify. A master skill runs at the start of each conversation and dispatches the other skills as needed.
- **Money use (Possible angle (no price given)):** Sell a set-up-and-customize service for Claude Code workflows, or build custom skills for clients. No prices stated.

### 227. 100 Hours Testing Claude Code vs Antigravity (honest results)
[Watch](https://www.youtube.com/watch?v=99VHENEKA9o) · 24 min · List #142 · [note](notes/142-99VHENEKA9o.md)
- **Recap:** Both tools are agentic coding environments: they plan, use sub-agents, run terminal commands, and edit whole projects. You pay for model tokens, not the tool. Claude Code is terminal/CLI-first and configurable; Antigravity is a standalone IDE with a manager view and a built-in browser agent.
- **Money use (Possible angle (no price given)):** Learn one agentic coding tool well; the skill transfers. Could sell landing pages or small web apps to agency owners. No prices for client work stated.

### 228. How to Build 24/7 Claude Agents. Easy.
[Watch](https://www.youtube.com/watch?v=ehg4fhydTgs) · 16 min · List #141 · [note](notes/141-ehg4fhydTgs.md)
- **Recap:** Claude Code "routines" run a saved prompt on Anthropic's cloud, triggered by a schedule, an API call, or a GitHub event, so the laptop can stay closed. Routines clone a GitHub repo each run, read its CLAUDE.md and scripts, then delete the clone. Secrets do not travel with the repo, so they go into the cloud environment's variables.
- **Money use (Possible angle (no price given)):** Running always-on client automations (reports, comment summaries, posting) for small businesses without keeping a machine on. Price points not stated. Start by migrating one recurring task you already run locally.

### 229. Claude + HeyGen Just Changed Content Creation Forever
[Watch](https://www.youtube.com/watch?v=EbJu9T30nfI) · 20 min · List #140 · [note](notes/140-EbJu9T30nfI.md)
- **Recap:** Pipeline: HeyGen makes the avatar, ElevenLabs makes the voice clone, Remotion adds motion graphics, and Claude Code orchestrates the steps. Make a HeyGen avatar from a short webcam clip or uploaded footage. Make a professional ElevenLabs voice clone from about 30 minutes of audio (he used about 2 hours).
- **Money use (Possible angle (no price given)):** Sell AI avatar video production for businesses, especially top-of-funnel content and course videos. Start by creating an avatar and voice clone, then build the pipeline. He stresses that subject-matter expertise still matters.

### 230. Claude Opus 4.7 Just Dropped... Or Did It Really?
[Watch](https://www.youtube.com/watch?v=NiMc2PoTiXo) · 17 min · List #139 · [note](notes/139-NiMc2PoTiXo.md)
- **Recap:** Opus 4.6 seemed to degrade. Nate cites an AMD director's analysis of about 7,000 Claude Code sessions: thinking depth fell and file reads before edits dropped (his claim). Behavior can change without a new model. Adaptive thinking and a lower default effort level reduced reasoning, and Nate says the change was silent.
- **Money use (Skill-builder):** No direct money angle in the video. Skill to build: model evaluation, effort settings, prompt testing, token management, reviewing vendor claims.

### 231. I Turned Claude Into a 24/7 Trader
[Watch](https://www.youtube.com/watch?v=6MC1XqZSltw) · 33 min · List #138 · [note](notes/138-6MC1XqZSltw.md)
- **Recap:** Build a scheduled Claude Code project with Routines: pre-market research, market open trades, midday review, close, and a Friday weekly review. Claude wakes up stateless each run. Memory lives in files (strategy, trade log, research log, weekly review). Each run reads them first and writes lessons back.
- **Money use (Skill-builder):** No direct money angle in the video. He says it is an experiment and "not financial advice." Suggests a paper-trading start. Skill to build: agent design, scheduling, memory architecture, API integration, GitHub workflow, risk guardrails.

### 232. Claude Design Just Became Unstoppable
[Watch](https://www.youtube.com/watch?v=gAoZ95kqG7w) · 15 min · List #137 · [note](notes/137-gAoZ95kqG7w.md)
- **Recap:** Claude Design (Anthropic Labs research preview) makes prototypes, slide decks and one-pagers from chat. Set up a design system once: company blurb, website repo, brand guidelines, logo and tone. New projects then inherit it. Review generated colors, type and buttons.
- **Money use (Possible angle (no price given)):** Branded decks and landing pages for clients. He says this could replace his Gamma or Canva subscriptions. No prices stated.

### 233. Claude Just Destroyed Every Video Editing Tool
[Watch](https://www.youtube.com/watch?v=ZNbgOhxhzXg) · 32 min · List #136 · [note](notes/136-ZNbgOhxhzXg.md)
- **Recap:** Claude Design (Anthropic's web app) can build animated videos from a prompt. Load a brand design system first so output matches your branding. Claude cannot hear or read video on its own, so feed it a timestamped transcript to sync text and graphics to speech.
- **Money use (Skill-builder):** No direct money angle in the video. Implied: branded promo and short-form video for clients. He argues taste is the differentiator. Skill to build: AI video editing, HTML animation, prompt iteration, design systems, plan-mode workflow, context….

### 234. How to Never Hit Your Claude Session Limit Again
[Watch](https://www.youtube.com/watch?v=_qZvORxGqI0) · 25 min · List #135 · [note](notes/135-_qZvORxGqI0.md)
- **Recap:** Context is everything Claude Code can see at once. Startup overhead alone can be thousands of tokens, so run /context in a fresh session to check. Each message rereads the whole chat, so cost compounds. Quality also decays as sessions grow ("context rot"). Auto-compaction near 95% is too late, so he resets earlier, around 120k tokens.
- **Money use (Skill-builder):** No direct money angle in the video. Skill to build: context management, slash commands, sub-agent delegation, Markdown conversion, token analytics.

### 235. Claude Design Builds Beautiful 3D Websites Instantly (full tutorial)
[Watch](https://www.youtube.com/watch?v=TcFeSjwTo7g) · 35 min · List #134 · [note](notes/134-TcFeSjwTo7g.md)
- **Recap:** Brief a brand in chat, then have Claude write the brand identity and copy for a hero section. Generate a looping background: an image prompt, a still-frame-to-video prompt, and a fixed camera. Feed the still into Claude Design as a sketch and upload the clip.
- **Money use (Possible angle (no price given)):** Who pays: small brands and founders who need a polished landing page fast. He builds demo sites for his own brand and a fictional brand. Sell a one-page or scroll-journey site package, plus a design system export. No price points for client work are stated.

### 236. OpenAI Image 2 is Nuts. Here are 10 Ways to Use it.
[Watch](https://www.youtube.com/watch?v=GY-kAiZGLOw) · 14 min · List #133 · [note](notes/133-GY-kAiZGLOw.md)
- **Recap:** Run a side-by-side image model test: 30 matched prompts, with a model acting as judge to pick winners per category. Use cases for image models: product packaging mockups, cleaned-up handwriting scans, website hero concepts, UGC-style ads, localized ad creative, book covers, LinkedIn carousels, brand…
- **Money use (Possible angle (no price given)):** Who pays: small businesses and marketers who need packaging, ads, or social graphics fast. Offer product mockups, ad variant batches, or carousel and thumbnail production. He says a thumbnail workflow could be fully automated. No prices for services given.

### 237. Claude Video Editing Just Became Unrecognizable
[Watch](https://www.youtube.com/watch?v=Aw3BkmhYu4I) · 28 min · List #132 · [note](notes/132-Aw3BkmhYu4I.md)
- **Recap:** Set up a video studio project in the Claude desktop app by pulling in two GitHub repos (a motion-graphics tool and a video-editing skill). Trim a raw talking-head recording with the editing skill: it removes filler words, silences, and retakes, and returns a timed word transcript.
- **Money use (Possible angle (no price given)):** Who pays: creators and small businesses who need short-form clips or lessons edited. Sell a "drop a raw file, get a finished video" service or a per-style template. He suggests a style file per video type (intros, lessons, shorts) to make the process repeatable. No prices stated.

### 238. I Tested GPT 5.5 vs Opus 4.7: What You Need to Know
[Watch](https://www.youtube.com/watch?v=WX4rp-vP3zo) · 20 min · List #131 · [note](notes/131-WX4rp-vP3zo.md)
- **Recap:** A way to compare coding models: give both the same one-shot prompt in their own harness, then compare time, tokens, and cost from the session logs. Four quick experiments: a personal brand site, a solar system sim, a 3D space shooter, and a multi-species ecosystem sim.
- **Money use (Possible angle (no price given)):** Who pays: teams choosing a model for production agents and automations. Sell cost and quality comparisons, or a repeatable test harness per client use case. Price points: none offered.

### 239. Claude Code + Playwright Automates Literally Anything
[Watch](https://www.youtube.com/watch?v=J-6pnl5DQg8) · 19 min · List #130 · [note](notes/130-J-6pnl5DQg8.md)
- **Recap:** Connect a browser CLI (Playwright) to Claude Code instead of an MCP server, to save context tokens on tool definitions. Build a QA loop: the agent builds a multi-page form, runs a headed browser test, reads failures, fixes the site, and reruns until it passes.
- **Money use (Possible angle (no price given)):** Browser automation for lead generation (e.g., collecting business phone numbers) and for work that has no API. He does not state a price or a client. Start by building one repeatable script inside a skill, then run it on a schedule.

### 240. 32 Tricks to Level Up Claude Code in 16 Mins
[Watch](https://www.youtube.com/watch?v=jqoFP9QapXI) · 16 min · List #129 · [note](notes/129-jqoFP9QapXI.md)
- **Recap:** Beginner habits: run the init command on every project to generate a project memory file, keep that file short (he suggests 150-200 lines), and point it to other docs instead of stuffing it. Manage context: keep prompts small, check token use with the context command, compact around 60%, and clear between unrelated tasks.
- **Money use (Skill-builder):** No direct money angle in the video. Tips are general productivity; he mentions a free PDF guide as a lead magnet. Skill to build: Claude Code config (project memory file, custom skills, slash commands), context management, git….

### 241. Claude Design 2 HOUR COURSE (Beginner to Pro)
[Watch](https://www.youtube.com/watch?v=ovabeVoWrA0) · 118 min · List #128 · [note](notes/128-ovabeVoWrA0.md)
- **Recap:** Claude Design is a separate Anthropic Labs app (launched April 17, 2026, powered by Opus 4.7). Brainstorm in regular Claude chat first, and open Design only when the plan is ready. Build a design system first (logo, fonts, colors, a website or GitHub repo as input), publish it, then reuse it for every deck, page and video.
- **Money use (Possible angle (no price given)):** Sell branded design systems, pitch decks, landing pages and promo videos for businesses; use a prototype as a sales demo. Nate advises building one system well before building five. No client prices are stated.

### 242. Build & Sell Claude Code Operating Systems (2+ Hour Course)
[Watch](https://www.youtube.com/watch?v=bCljOfCH8Ms) · 153 min · List #127 · [note](notes/127-bCljOfCH8Ms.md)
- **Recap:** The "AIOS": a personal operating system built as a folder of markdown files in Claude Code, with context, connections, capabilities and cadence (the "four C's"), built in that order. Onboarding: a clone-able repo with an onboard skill (7-question interview), a claude.md master prompt, and context files that the agent reads each session.
- **Money use (Possible angle (no price given)):** Sell AIOS builds (setup, audit and level-up sessions) to operators, then to their teams; Nate says team-wide adoption follows the owner's own setup. He suggests boring deterministic automations, run on Trigger.dev or Modal, often beat agents. No client prices are stated.

### 243. I Tried 100+ Claude Code Skills. These 6 Are The Best
[Watch](https://www.youtube.com/watch?v=eRS3CmvrOvA) · 14 min · List #126 · [note](notes/126-eRS3CmvrOvA.md)
- **Recap:** Six Claude Code add-ons that save time, cut cost, or remove mistakes, which Nate says businesses pay for most. Skill Creator (Anthropic official) turns a plain-English description or SOP into a tested, reusable skill. Superpowers adds a plan, test-first, two-stage review workflow to slow Claude down before it writes code.
- **Money use (Possible angle (no price given)):** Sell outcomes to business owners (hours saved, fewer admin mistakes, faster leads), not the workflow. Build the first automation with one skill, then show a demo. Start with one skill, not all six. No prices stated for client work.

### 244. Building Realistic Voice Agents Has Never Been Easier
[Watch](https://www.youtube.com/watch?v=-cdexJWN8YA) · 32 min · List #125 · [note](notes/125--cdexJWN8YA.md)
- **Recap:** A voice agent is a loop: speech in, transcription, LLM reply or tool call, speech out. Four parts: persona (system prompt), voice, knowledge, and tools. Plan mode first in Claude Code: describe the goal, answer its questions, then let it build the ElevenLabs agent and its tools.
- **Money use (Possible angle (no price given)):** Website or phone voice agents that answer questions and book discovery calls for service businesses (Nate frames his own AI consultancy this way). Sell the booked call, not the agent. Cost guardrails (domain lock, call length cap, rate limit) should be part of the price. No client prices stated.

### 245. Higgsfield Just Turned Claude Into a Creative Agency
[Watch](https://www.youtube.com/watch?v=xn6Z5PYyAIE) · 35 min · List #124 · [note](notes/124-xn6Z5PYyAIE.md)
- **Recap:** Connect Higgsfield to Claude as a custom connector (MCP) for quick tests; for repeat work, use the Higgsfield CLI instead because MCP tool lists cost more tokens. Pull the knowledge in first: have an agent write a reference markdown on ad strategy, then generate from it.
- **Money use (Possible angle (no price given)):** Ad creative for brands: product photos, Instagram ads, short video ads, and test batches for paid campaigns. Start with one product, produce a test matrix, track results in a sheet, and let the winning combos get budget. No client prices stated.

### 246. Master 97% of Codex in 1 Hour (full course)
[Watch](https://www.youtube.com/watch?v=3TdD8Qv5Tk8) · 61 min · List #123 · [note](notes/123-3TdD8Qv5Tk8.md)
- **Recap:** Codex app basics: projects tied to a local folder, plan mode first, model and reasoning-level switching (medium for planning, high for builds, extra high only for stubborn bugs). Put context in an agents.md file (Codex's equivalent of CLAUDE.md) so each new chat starts oriented.
- **Money use (Possible angle (no price given)):** Comment-analysis dashboards or weekly reports for creators or small brands; sell the outcome (what to reply to, what content to make) rather than the workflow. Start by building one skill for a client's repeated report, then add a schedule and a hosted dashboard. No prices for client work are stated.

### 247. Claude Just Solved Session Limits
[Watch](https://www.youtube.com/watch?v=3QclAjmu5Tw) · 10 min · List #122 · [note](notes/122-3QclAjmu5Tw.md)
- **Recap:** Anthropic's compute deal with SpaceX (announced at its Code with Claude event) is the reason for higher limits; Nate says outages came from too little compute. Five builder takeaways: retest workflows that failed on rate limits; use Opus more instead of rationing it; the 1M context window is usable in production API work;
- **Money use (Skill-builder):** No direct money angle in the video. Skill to build: none taught; rate-limit and session planning.

### 248. Overwhelmed By AI? Just Copy My Tech Stack
[Watch](https://www.youtube.com/watch?v=35WuZxbAY68) · 17 min · List #121 · [note](notes/121-35WuZxbAY68.md)
- **Recap:** His tiered AI stack: S tier (daily drivers) Claude Code, VS Code, and Glido; A tier (weekly) Codex, Claude chat, Hermes Agent, Perplexity, and Grok's X search; Coding agents are interchangeable harnesses; keep projects in plain directories so any agent can work in them.
- **Money use (Skill-builder):** No direct money angle in the video. Skill to build: tool evaluation, workflow decomposition, directory-based project design.

### 249. This is The Most Powerful Tool to Give to Claude Code
[Watch](https://www.youtube.com/watch?v=YHk45NEpspE) · 15 min · List #120 · [note](notes/120-YHk45NEpspE.md)
- **Recap:** Why CLIs suit agents better than APIs or MCP servers: short clean output, no always-on server, and tokens are not wasted on tool descriptions. Priority order: use an existing CLI first, build one from an API second, and use MCP only when neither exists.
- **Money use (Skill-builder):** No direct money angle in the video. Implied: building custom CLIs for sites without APIs and sharing them internally. Skill to build: CLI design, tool-selection judgment (CLI vs API vs MCP), natural-language skill building, secret….

### 250. Hermes Agent: Zero to Personal AI Assistant (1 Hour Course)
[Watch](https://www.youtube.com/watch?v=gb5TlGw6Uks) · 58 min · List #119 · [note](notes/119-gb5TlGw6Uks.md)
- **Recap:** Hermes Agent is an open-source, self-improving agent you run on your own server; he deploys it on a VPS with a one-click Docker install. Five pillars: memory (user and memory files loaded each session), skills (step-by-step SKILL.md recipes), soul (a personality file), cron jobs (scheduled, isolated runs set up in plain…
- **Money use (Skill-builder):** No direct money angle in the video. he frames it as a personal assistant. Running cost is about $100/yr for the VPS plus an existing ChatGPT plan. Skill to build: VPS and Docker setup, Telegram bot config, .env secret handling, GitHub token scoping, cron….

### 251. Claude Code Just Got an Agent Dashboard
[Watch](https://www.youtube.com/watch?v=ZAaxx3qyT8g) · 8 min · List #118 · [note](notes/118-ZAaxx3qyT8g.md)
- **Recap:** Agent view is one terminal screen that lists all running Claude Code sessions with their status (working, needs input, done). Move between the overview and any session with the arrow keys; a session waiting for approval can be answered from the overview without opening it.
- **Money use (Skill-builder):** No direct money angle in the video. Skill to build: running parallel Claude Code sessions, terminal session navigation, goal-based prompting,….

### 252. Every Level of Claude Explained in 21 Minutes
[Watch](https://www.youtube.com/watch?v=ZRb7D6R64hM) · 22 min · List #117 · [note](notes/117-ZRb7D6R64hM.md)
- **Recap:** A five-level ladder for using Claude: enthusiast, beginner, intermediate (Claude Cowork), level four (Claude Code power use), level five (architect, cloud automation). Each level has a "cheat code" step: make a project with reference docs, set a folder structure Claude always reads first, then build repeatable workflows.
- **Money use (Viable offer (price signal)):** Non-coders can sell automation as a service at level three and up; level-four freelance or agency projects at $5k-$15k (Nate's figures, no pricing guidance beyond that).

### 253. Anthropic Just Dethroned OpenAI. Here's What Happens Next.
[Watch](https://www.youtube.com/watch?v=-nG-9vlSkho) · 8 min · List #116 · [note](notes/116--nG-9vlSkho.md)
- **Recap:** Business adoption data (a research article) shows Anthropic passing OpenAI for the first time in the cited dataset. Both labs are running promotions: free Codex months for companies switching from Claude Code, and temporary Claude Code limit increases. Heavy subscription use is currently priced well below API cost, so users are in a "free sample" phase.
- **Money use (Skill-builder):** No direct money angle in the video. advice is to use the cheap window, not a paid offer. Skill to build: AI market analysis, tool portability, subscription economics.

### 254. How to Deploy Your Claude Automations (3 Methods)
[Watch](https://www.youtube.com/watch?v=xJ5oz63mIec) · 22 min · List #115 · [note](notes/115-xJ5oz63mIec.md)
- **Recap:** Three ways to run agents while you are away, compared on where they run (your machine vs cloud) and how deterministic they are. Method 1, session loops: ask Claude Code to repeat a task on an interval (cron create/list/delete). Needs the session and your machine on; expires after days.
- **Money use (Skill-builder):** No direct money angle in the video. the value is running automations unattended. Hosted options add per-token costs. Skill to build: scheduling, deployment, agent architecture, webhooks, hook design.

### 255. The AI Career Opportunity Nobody is Talking About in 2026
[Watch](https://www.youtube.com/watch?v=iIfOprq2kCM) · 19 min · List #114 · [note](notes/114-iIfOprq2kCM.md)
- **Recap:** Most AI-career advice points to starting an automation agency; Nate argues for a second route, the in-house AI leader role. Path A: work as an AI consultant or freelancer, then get pulled in-house by a client. Path B: become the most AI-fluent person inside your current company and take the internal seat when it opens.
- **Money use (Possible angle (no price given)):** AI consulting or automation agency work for clients (path A) or an internal promotion (path B); no price points stated for either.

### 256. How to Use Your Claude Code Projects in Codex in 5 Mins
[Watch](https://www.youtube.com/watch?v=kB9iMD0EjT8) · 9 min · List #113 · [note](notes/113-kB9iMD0EjT8.md)
- **Recap:** Keep shared project knowledge (docs, references, scripts) in neutral folders that any coding agent can read. Claude Code reads CLAUDE.md and .claude/; Codex reads agents.md, .codex/ and .agents/. Create the Codex equivalents rather than duplicating content.
- **Money use (Skill-builder):** No direct money angle in the video. the pitch is tool-agnostic resilience so an outage in one tool does not stop work. Skill to build: multi-agent project setup, config conversion, session handoff, terminal workflow.

### 257. What Karpathy Joining Anthropic Actually Means For Claude
[Watch](https://www.youtube.com/watch?v=brB-hSiV2iU) · 16 min · List #112 · [note](notes/112-brB-hSiV2iU.md)
- **Recap:** Nate's thesis: the model is only one layer; the "wrapper" (CLAUDE.md, memory, skills, sub-agents, hooks, MCP connectors, docs) decides output quality. Context engineering matters more than prompt writing; a stateless chat starts from zero every time.
- **Money use (Possible angle (no price given)):** Nate speculates (no stated prices) that a marketplace for packaged skills, workflows and domain context could emerge, and that domain experts could sell packaged expertise.

### 258. Give Me 10 Mins and I'll Save You Millions of Claude Tokens
[Watch](https://www.youtube.com/watch?v=6cEQEba0i2A) · 11 min · List #111 · [note](notes/111-6cEQEba0i2A.md)
- **Recap:** Prompt caching happens automatically in Claude Code; the goal is to keep the cache warm so sessions burn fewer limits. Cached reads cost a fraction of fresh input. The cache lives about an hour on a subscription and about 5 minutes on API or sub-agent calls.
- **Money use (Skill-builder):** No direct money angle in the video. the value is lower subscription limit burn and API cost savings. Skill to build: prompt caching analysis, token tracking, session management, context hygiene.

### 259. The AI Offer You Can Sell Tomorrow Morning
[Watch](https://www.youtube.com/watch?v=Pi-m8R068r4) · 27 min · List #110 · [note](notes/110-Pi-m8R068r4.md)
- **Recap:** Start by selling hours, not projects. The first offer is a one-on-one session helping a business owner set up their own AI operating system or get comfortable with Claude Code. Use the "ladder": hours (rung 0), paid audit (rung 1), first project (rung 2), retainer (rung 3). Earn each rung from the one below.
- **Money use (Viable offer (price signal)):** Sell one-on-one AI OS setup sessions first, then audits, projects, and retainers.

### 260. The Playbook for a $100M AI Agency
[Watch](https://www.youtube.com/watch?v=8ktcSaSTvxk) · 104 min · List #109 · [note](notes/109-8ktcSaSTvxk.md)
- **Recap:** Podcast with Devin Karns (co-founder of Custom AI Studio) on how to build an AI services firm worth a large exit, not a lifestyle business. Pick the business model on purpose. Freelancer, agency, AI readiness consulting, managed agents, product, and full-stack consulting differ in value, and value jumps as revenue grows.
- **Money use (Viable offer (price signal)):** Workshop as the entry offer, then discovery blueprint (about $15k to $35k), custom build, and performance or revenue-share partnerships. Price points are as stated by the guest.

### 261. 100 Hours Testing Claude Code vs ChatGPT Codex (honest results)
[Watch](https://www.youtube.com/watch?v=RLjaUES9P8A) · 27 min · List #108 · [note](notes/108-RLjaUES9P8A.md)
- **Recap:** Both tools share the basics: local file editing, desktop apps, VS Code extensions, MCP, skills, hooks, sub-agents, and cloud delegation. Pick by workflow fit, not by feature checklist. Claude Code is more customizable: about 30 hook events (Codex about 6), sub-agents it spawns on its own, and /ultra plan, /ultra review, /loop, channels, and the Agent SDK.
- **Money use (Skill-builder):** No direct money angle in the video. (plan choice only; he suggests trying both subscriptions) Skill to build: Claude Code configuration, hooks, sub-agents, worktrees, computer use, GitHub integration, cost and….

### 262. Opus 4.8 Just Dropped. Here's How To Actually Use It.
[Watch](https://www.youtube.com/watch?v=q5lg3npxjAc) · 14 min · List #107 · [note](notes/107-q5lg3npxjAc.md)
- **Recap:** What changed in Claude Code with Opus 4.8: effort levels (low to "ultra code"), dynamic workflows, and a claimed fix for the 4.7 complaints (laziness, overreach, token burn, tone). Effort is the first lever to tune. Run the same task at a lower or higher effort level before blaming the model.
- **Money use (Skill-builder):** No direct money angle in the video. Skill to build: Claude Code model and effort settings, prompt writing, token tracking, workflow testing.

### 263. I Turned Claude Opus 4.8 Into My Entire AI Operating System
[Watch](https://www.youtube.com/watch?v=0WDkwMxj13s) · 29 min · List #106 · [note](notes/106-0WDkwMxj13s.md)
- **Recap:** Build a personal "AI operating system": one local folder, run in Claude Code, that holds your context so you work from one place. His four C's: context (the AI knows your business), connections (tools and APIs it can reach), capabilities (skills that encode how you work), and cadence (things that run without you…
- **Money use (Possible angle):** Implied only. Teaching the four-C's setup is what his free course is for, with no price points stated.

### 264. Claude Code Dynamic Workflows Clearly Explained
[Watch](https://www.youtube.com/watch?v=jZgcWCzxh1I) · 17 min · List #105 · [note](notes/105-jZgcWCzxh1I.md)
- **Recap:** Compares skills, sub-agents, agent teams, /goal, and dynamic workflows by how many agents run and whether they talk to each other. A dynamic workflow is a script Claude writes and runs. It fans out many agents that work alone and returns merged results. Workflows can be saved and re-run.
- **Money use (Skill-builder):** No direct money angle in the video. Skill to build: Claude Code workflow scripting, skill auditing, sub-agent orchestration, token and cost control,….

### 265. 100 Years of Artificial Intelligence Explained
[Watch](https://www.youtube.com/watch?v=NHFbAg2b54U) · 17 min · List #104 · [note](notes/104-NHFbAg2b54U.md)
- **Recap:** A timeline of AI from the 1939-45 Enigma codebreaking work to the 2020s chatbot and coding-tool boom. 1956 Dartmouth workshop gave the field its name. The field then split between rule-based (symbolic) systems and neural networks.
- **Money use (Skill-builder):** No direct money angle in the video. Skill to build: historical narrative, technical explanation, timeline storytelling.

### 266. I Tested Every Claude Code Feature, These 12 Are the Best
[Watch](https://www.youtube.com/watch?v=vfWTyEreOEc) · 20 min · List #103 · [note](notes/103-vfWTyEreOEc.md)
- **Recap:** Features are ranked by how much they change Nate's daily knowledge-work and automation, not by software engineering value. Skills are the top pick: markdown recipes that can be shared, chained, or reduced to a slash command.
- **Money use (Skill-builder):** No direct money angle in the video. Skill to build: slash commands, skill authoring, agent team setup, cron-based loops, remote control, cloud….

### 267. The Skill That 10x’d My Claude Code Projects
[Watch](https://www.youtube.com/watch?v=c0kaKxM2pHg) · 7 min · List #102 · [note](notes/102-c0kaKxM2pHg.md)
- **Recap:** Everyone on the same model gets the same generic output. Results sound like you only when your taste, decisions, and process are written into the context. The hard part is extraction: getting knowledge out of your head and into files the AI can use.
- **Money use (Skill-builder):** No direct money angle in the video. Nate mentions client discovery calls and project scoping as where this extraction matters most, without a price or offer. Skill to build: skill authoring, knowledge extraction, checkpointing, Q&A logs, iterating on skills.

### 268. AGI is Here. Anthropic Just Proved It.
[Watch](https://www.youtube.com/watch?v=NDeyhGnNECc) · 13 min · List #101 · [note](notes/101-NDeyhGnNECc.md)
- **Recap:** Nate's practical AGI test: a general model is handed an open-ended problem with no clear answer and solves it on its own by researching, experimenting, and iterating. Anthropic's report (as Nate reads it) groups coding tasks by difficulty. Success on the hardest open-ended tier rose sharply over six months.
- **Money use (Skill-builder):** No direct money angle in the video. Skill to build: report analysis, defining AGI, interpreting exponential trends, risk framing.

### 269. Is Claude Mythos Coming?
[Watch](https://www.youtube.com/watch?v=lkR6mvqQQlk) · 12 min · List #100 · [note](notes/100-lkR6mvqQQlk.md)
- **Recap:** Nate describes Mythos as a model tier above Opus, reportedly strongest at finding security holes, and so far available only to vetted partners through a program called Project Glasswing. A Mythos identifier briefly appeared on the API and was removed. Nate reads the sighting as a possible leak or hype rather than a launch.
- **Money use (Possible angle):** Partner pricing is the only price point stated (above). Nate expects a public version to be expensive. No advice on how to start.

### 270. How to Build Claude Subagents Better Than 99% of People
[Watch](https://www.youtube.com/watch?v=e18sdZLwP7o) · 27 min · List #99 · [note](notes/099-e18sdZLwP7o.md)
- **Recap:** A subagent gets a fresh context window, so heavy reading or research stays out of the main chat. The main session acts as orchestrator and receives only the report. A custom subagent is a markdown file with YAML front matter: name, description, tools, model, color, memory. The description is the trigger, so tune it when the agent misfires.
- **Money use (Skill-builder):** No direct money angle in the video. Skill to build: subagent authoring, YAML front matter, tool and model restriction, description tuning, delegation….

### 271. Claude Mythos is Finally Here.
[Watch](https://www.youtube.com/watch?v=dYrrEKXtttk) · 9 min · List #98 · [note](notes/098-dYrrEKXtttk.md)
- **Recap:** Anthropic released Claude Fable 5 for general use. Claude Mythos 5 is limited to Project Glasswing partners. Nate describes them as the same model, with cyber safeguards lifted for Mythos 5. Mythos-class models sit above Opus. Mythos 5 is an upgrade path for earlier Mythos preview users.
- **Money use (Skill-builder):** No direct money angle in the video. Skill to build: model selection, cost awareness, effort-level tuning, agent-loop judgment.

### 272. I Turned Claude Into the Ultimate Second Brain
[Watch](https://www.youtube.com/watch?v=8QQ_INxAhRs) · 34 min · List #97 · [note](notes/097-8QQ_INxAhRs.md)
- **Recap:** His "four C" framework: context (a routing file that points to where things live), connections (live data through APIs or CLIs), capabilities (skills, agents, automations), and cadence… Default to one harness, Claude Code, and keep the system in plain folders and markdown so any coding agent can use it.
- **Money use (Possible angle (no price given)):** He suggests selling AI OS setups to businesses and teaching the framework to teams (his suggestion, no prices stated).

### 273. From Zero to Head of AI in 1 Year (as a regular person)
[Watch](https://www.youtube.com/watch?v=diY71x7GUjI) · 42 min · List #96 · [note](notes/096-diY71x7GUjI.md)
- **Recap:** Guest Eileen's path: 15 years as an email developer, then a team lead, then a layoff at 39. She tried Zapier, then Make, then n8n, and later Claude Code through Nate's course. She got a head-of-AI role covering strategy for 15 companies under one parent group, and she does hands-on builds. Her method: map the process, decide what stays human, then build.
- **Money use (Possible angle):** Job path into in-house AI leadership roles. She says her new employer's staff were receptive because the goal was to remove tedious work, not to replace people. Consultants were noted as having a negative reputation with staff.

### 274. Claude Fable 5 Made This Entire Video By Itself.
[Watch](https://www.youtube.com/watch?v=ONmaDdOBGig) · 6 min · List #95 · [note](notes/095-ONmaDdOBGig.md)
- **Recap:** One goal prompt given to Claude Code produced the whole video: research, script, cloned voice, AI avatar, motion graphics, edit and a visual check, while Nate was away. Voice drift forced chunking: the script was split into roughly one-minute segments, each voice-generated separately.
- **Money use (Skill-builder):** No direct money angle in the video. Skill to build: goal-based agent prompting, scripted video production, sub-agent verification, token and cost….

### 275. Learn These 6 AI Skills Now (Before Everyone Else Does)
[Watch](https://www.youtube.com/watch?v=3XIGcM7VICc) · 20 min · List #94 · [note](notes/094-3XIGcM7VICc.md)
- **Recap:** Six career skills: become the "AI person" in your role by picking one tool and documenting before-and-after results on one workflow; Iteration speed: prototype fast, then set one North Star metric and a clear definition of done before building.
- **Money use (Possible angle):** Turn one domain expertise into a course, niche newsletter, micro SaaS or consulting. He says to pick one and go hard before branching out. No prices stated.

### 276. We Might Actually Need to Stop AI
[Watch](https://www.youtube.com/watch?v=CvA8-aScqio) · 12 min · List #93 · [note](notes/093-CvA8-aScqio.md)
- **Recap:** In early June, OpenAI published a plan with three goals: an AI automated researcher (target stated as March 2028), sharing economic gains, and an international body able to coordinate… Nate's reading: both labs say they cannot slow down on their own because competition is too strong, so they want a referee that holds everyone to a pause.
- **Money use (Skill-builder):** No direct money angle in the video. Skill to build: reading AI policy, incentive analysis, AI-era career positioning.

### 277. Every Level of a Claude Second Brain Explained
[Watch](https://www.youtube.com/watch?v=DTCyvo6cC54) · 31 min · List #92 · [note](notes/092-DTCyvo6cC54.md)
- **Recap:** Design the system from the questions you will ask later. Retrieval determines how you store data. Level 1: CLAUDE.md acts as a router to folders (exact-name search). Start here. Level 2: a wiki with indexes and backlinks, plus auto memory. Good for 30+ notes you forget.
- **Money use (Skill-builder):** No direct money angle in the video. He says team-wide second brains are an adoption and change-management problem, not a tooling one, which implies a consulting angle. Skill to build: information architecture, routing rules, vector retrieval design, knowledge-graph modeling,….

### 278. How to Use Claude Code Better Than 98% of People
[Watch](https://www.youtube.com/watch?v=RzLV8sfFdMM) · 68 min · List #91 · [note](notes/091-RzLV8sfFdMM.md)
- **Recap:** Work as director: plan with context, build, verify, then fix the system. Each failure becomes a rule in CLAUDE.md, a skill, or a hook. Context is scarce. Quality drops in a "dumb zone" well before the window fills (about 250k tokens for Opus, by their estimate). Load skills on demand, not all up front.
- **Money use (Possible angle (no price given)):** sell AI-layer setup and workflow automation to businesses, for example multi-agent quoting (research, pricing, draft, check margin). Scope the build with questions first. No prices stated.

### 279. GLM 5.2 in Claude Code is Blowing My Mind
[Watch](https://www.youtube.com/watch?v=2OD14-0cot4) · 16 min · List #90 · [note](notes/090-2OD14-0cot4.md)
- **Recap:** GLM 5.2 (open-weight, hosted by z.ai) runs inside Claude Code. Setup is an env-var change: point the Anthropic base URL at z.ai and paste the z.ai key into settings.local.json. Per-folder routing: a project folder with that settings file uses GLM, and a folder without it uses Opus on the Claude Max plan.
- **Money use (Possible angle (no price given)):** cut your AI costs by routing each task to the cheapest model that passes; sell that setup to clients as a cost-saving service. No pricing given for services.

### 280. Finally. Agent Loops Clearly Explained.
[Watch](https://www.youtube.com/watch?v=EuzYhzB0vbI) · 15 min · List #89 · [note](notes/089-EuzYhzB0vbI.md)
- **Recap:** A loop is a trigger, an action, and a stop condition. The two pillars are a checkable goal and verification. Core cycle is reason, act, observe, repeat, until the done criteria are met. Prefer objective metrics ("until X equals Y") over "until satisfied." Patterns: solo loop, maker-checker (one agent builds, one grades), and a manager with helper agents.
- **Money use (Skill-builder):** No direct money angle in the video. Skill to build: writing goal and done criteria, verification design, screenshot-based visual checks, sub-agent….

### 281. So You Learned Claude, Now What?
[Watch](https://www.youtube.com/watch?v=-zL_trhnQaI) · 17 min · List #88 · [note](notes/088--zL_trhnQaI.md)
- **Recap:** Tools change fast, so the durable value is the underlying skill applied to each new AI phase: automation, then agents, then agentic work. Two paths into AI consulting: independent consultant (outside clients) or in-house AI lead at one company. Operating rule: pick a business constraint first, set a KPI second, build third.
- **Money use (Possible angle (no price given)):** sell diagnosis plus AI solutions to businesses (consulting), or become the in-house AI person and seek a raise or new title. No prices given beyond salary ranges. Start by auditing one role, choosing one constraint, and piloting one fix.

### 282. I Battle Tested Sakana Fugu's Fable Killer
[Watch](https://www.youtube.com/watch?v=GpSqBjW6hR4) · 12 min · List #87 · [note](notes/087-GpSqBjW6hR4.md)
- **Recap:** Sakana Fugu (Fugu Ultra) is a multi-agent system exposed as one API: a small manager model breaks a task down and routes the pieces to frontier models such as Opus and GPT. It can run inside Claude Code, but setup needs a markdown guide and an API key, not a simple endpoint swap.
- **Money use (Skill-builder):** No direct money angle in the video. Nate suggests that tracking which model is cheapest for each task is a valuable skill. Skill to build: multi-model orchestration, Claude Code with custom API routing, eval design with an LLM grader,….

### 283. Why Watching AI Videos Isn't Enough
[Watch](https://www.youtube.com/watch?v=S2ME69hra-k) · 3 min · List #86 · [note](notes/086-S2ME69hra-k.md)
- **Recap:** Argues that agency skills (scoping projects, pricing, delivering without things falling apart) are hard to learn from videos because they depend on your situation. Points to his free "Monetizing AI Automation" playlist, which covers real agents he sold, a sales call, signing a first client, pricing, and delivery.
- **Money use (Possible angle (no price given)):** an AI automation agency: find a niche, sign clients, price workflows, deliver them. No price points given.

### 284. I asked Claude Code to make me as much money as possible
[Watch](https://www.youtube.com/watch?v=iTY8Q449YNQ) · 28 min · List #85 · [note](notes/085-iTY8Q449YNQ.md)
- **Recap:** four upgrades for working with Claude Code on business work: Stop the yes-man: a "roast" skill runs personas (contrarian, expansionist, first-principles, deep researcher, buyer, judge) and returns green light, reshape, or kill, plus the cheapest…
- **Money use (Possible angle):** validate demand before code, then build a waitlist landing page priced at the $19 entry tier. Use sub-agents to produce a go-to-market kit: positioning, market research, launch plan, outreach drafts.

### 285. Stanford's Method Turns Claude Into a PHD Level Research Team
[Watch](https://www.youtube.com/watch?v=Tj3018n5MVg) · 12 min · List #84 · [note](notes/084-Tj3018n5MVg.md)
- **Recap:** Adapts Stanford's STORM research method into a Claude skill: five perspective agents (practitioner, academic, skeptic, economist, historian) each research one topic. Chains four prompts: spin up the perspectives, map where they contradict each other, synthesize one HTML briefing, then peer-review it and verify each citation (confirmed, corrected, or…
- **Money use (Skill-builder):** No direct money angle in the video. He suggests tailoring the skill to your business and goals, and using it to pick topics for content. Skill to build: skill authoring (SKILL.md plus an HTML template), multi-agent orchestration, citation verification,….

### 286. How Anthropic Engineers Actually Prompt Fable 5
[Watch](https://www.youtube.com/watch?v=vcU85OrwuV0) · 11 min · List #83 · [note](notes/083-vcU85OrwuV0.md)
- **Recap:** six prompting habits he distilled from Anthropic's Fable 5 best-practice docs: Give the why (context behind the task). Applies to any model. Say what not to do; he finds negative instructions work better lately. Applies to any model.
- **Money use (Skill-builder):** No direct money angle in the video. Practical value is cost control: match model and effort to the task so usage credits are not spent on routine work. Skill to build: prompt design, effort-level selection, model routing awareness, verification prompting, cost control.

### 287. How Claude is Creating a New Generation of Millionaires
[Watch](https://www.youtube.com/watch?v=pbrln2TVeh4) · 10 min · List #82 · [note](notes/082-pbrln2TVeh4.md)
- **Recap:** Lists four things he says set Claude Code apart: it does the work from plain English, it acts agentically (builds, tests, fixes), it runs parallel agents, and it remembers context about… Four-step start: get a paid plan, pick one real repetitive task, have Claude argue against the idea before building, then build the smallest version that works.
- **Money use (Viable offer (price signal)):** sell or build fixes for repetitive work (receipts, weekly reports, email sorting). Start with one task and the $20 plan as the cost baseline. No product price points given.

### 288. Fable 5 + Karpathy’s LLM Wiki is Basically Cheating
[Watch](https://www.youtube.com/watch?v=hQvwMj7IJe4) · 15 min · List #81 · [note](notes/081-hQvwMj7IJe4.md)
- **Recap:** Builds a personal knowledge base ("LLM wiki") from Karpathy's gist: create an Obsidian vault, paste the gist into Claude Code, and ask it to implement the idea with a CLAUDE.md schema, an… Uses a raw/ folder for source drops; the model ingests each source into wiki pages, often splitting one source into several cross-linked pages.
- **Money use (Skill-builder):** No direct money angle in the video. directly. He presents the wiki as an internal second brain that makes his scripts and emails more specific. He suggests a cheaper model such as Opus for routine ingest. Skill to build: Obsidian vault setup, CLAUDE.md schema design, knowledge-base ingestion, markdown backlinking,….

### 289. How I Make Opus Think Like Fable (5 easy steps)
[Watch](https://www.youtube.com/watch?v=XTBWVVcF3Pk) · 10 min · List #80 · [note](notes/080-XTBWVVcF3Pk.md)
- **Recap:** The process matters more than the model: copy how a top model plans and verifies, then run it on cheaper models Treat the top model as a planner and teacher, and route routine work to smaller models Turn a deliverable you loved into a reusable skill: ask the model to analyze the session that produced it
- **Money use (Skill-builder):** No direct money angle in the video. He says that model routing and unit economics will matter for small teams with a monthly AI budget. Skill to build: skill-file design, model routing, dynamic sub-agent workflows, prompt and system-prompt analysis,….

### 290. Fable 5 Just Built Me a Business With One Prompt
[Watch](https://www.youtube.com/watch?v=R0qF17BVl9w) · 12 min · List #79 · [note](notes/079-R0qF17BVl9w.md)
- **Recap:** Put a long master prompt (mission, guardrails, phases, definition of done) in a file, then tell `/goal` to read it, because `/goal` has a short character limit Orchestration pattern: Fable plans, delegates, and reviews, while Opus or Sonnet sub-agents do the research and building
- **Money use (Viable offer (price signal)):** The sample is "Counter Brief," a chargeback-dispute tool for Shopify stores with 3+ disputes a month, priced at $19 per approved response with no success fee. Nate says the business was built locally and not published. He also says the idea needs stress-testing before building.

### 291. GPT 5.6 Sol Made This Entire Video
[Watch](https://www.youtube.com/watch?v=J_jswzXhYJA) · 5 min · List #78 · [note](notes/078-J_jswzXhYJA.md)
- **Recap:** One prompt to GPT 5.6 Sol in Codex on its top effort tier made a full video: script, cloned voice, avatar, and edit Keep each voice section under 60 seconds so the cloned voice stays consistent Map every visual to the exact phrase that triggers it, and keep the avatar visible
- **Money use (Possible angle):** A video-production workflow (script, voice, avatar, edit) could be sold as a service. This is a demo, and he gives no pricing.

### 292. I Tested GPT 5.6 Sol vs Fable 5. What You Need To Know.
[Watch](https://www.youtube.com/watch?v=EthxaDswUFo) · 20 min · List #77 · [note](notes/077-EthxaDswUFo.md)
- **Recap:** Side-by-side testing method: same `/goal` prompt in Claude Code (Fable 5) and Codex (GPT 5.6 Sol), then compare outputs, time, and cost Three test types: agentic builds (browser bike game, scroll website, five-element showcase), one-shot API tasks, and daily work Judge outputs by feel and use case, not benchmarks
- **Money use (Skill-builder):** No direct money angle in the video. (he gives model-choice advice; no offer is pitched) Skill to build: `/goal` prompting, running two harnesses side by side, cost and token tracking, API evaluation,….

### 293. Claude Code for Non-Coders (6 Hour Course)
[Watch](https://www.youtube.com/watch?v=jdbOVepEtUE) · 359 min · List #76 · [note](notes/076-jdbOVepEtUE.md)
- **Recap:** Set up Claude Code as a manager-style assistant: a CLAUDE.md router file, a `.claude` folder (settings, agents, skills), and API keys kept in a gitignored `.env` Build skills by doing a task, then asking the agent to turn it into a skill; iterate on each run
- **Money use (Possible angle (no price given)):** Consulting and automations for clients (his examples: a daily AI brief on Modal and a form-to-ClickUp webhook). He also suggests stacking a day job with an AI-powered side income around one niche (course, newsletter, micro-SaaS, consulting). No prices given for client work.

### 294. Claude Code + Clay Makes Lead Generation Actually Fun
[Watch](https://www.youtube.com/watch?v=zyvdl__Ywfk) · 18 min · List #75 · [note](notes/075-zyvdl__Ywfk.md)
- **Recap:** Clay handles the data (lead finding, enrichment, emails); Claude Code acts as the orchestrator through natural language Install the Clay plugin through the Claude Code terminal marketplace, then authenticate and confirm the tools load Feed Claude Code business context files (profile, case studies, FAQs, offer, website copy) so cold emails are personal
- **Money use (Viable offer (price signal)):** Cold outbound for a small AI automation agency serving home-service businesses (his demo business is a fictional agency). Target HVAC owners with a low-risk offer: a 90-second video pitch, then a free 30-day trial. He estimates about $24 of spend per 100 leads at a 1% conversion rate.

### 295. The $200K AI Job That Didn't Exist Last Year
[Watch](https://www.youtube.com/watch?v=eFOTQpbGcy8) · 10 min · List #74 · [note](notes/074-eFOTQpbGcy8.md)
- **Recap:** The gap is "knowing what to build" (judgment, prioritization), not only building; the value sits in deciding which problems to aim AI at. Four-step path to an in-house AI role: (1) audit your own job for tasks that take real hours and where a small AI error is harmless; (2) automate them and record hours saved;
- **Money use (Possible angle (no price given)):** Frame the offer as an in-house AI consultant role: build a proposal with hours saved and money saved, then ask for a budget and title. Alternatively, sell automation to companies that lack in-house talent. No prices stated.

### 296. Why Your AI Offer Isn't Selling, and How to Fix That
[Watch](https://www.youtube.com/watch?v=8MEJen0nblQ) · 56 min · List #73 · [note](notes/073-8MEJen0nblQ.md)
- **Recap:** Sell the outcome, not the AI: the buyer cares about the problem removed (e.g., a business that misses calls) rather than the tool. Use a clear story and a visible proof point; a single concrete demo can beat a list of certifications. Name one specific demographic and a clear intent before you pick tactics; study the customer closely.
- **Money use (Possible angle):** Guest's example is an AI phone-answering service for HVAC companies in a single city, sold on the outcome of always answering calls. Suggested tactics: targeted local ads, billboards on a route, or free first service to win trust, then recurring relationships. No prices stated.

### 297. How I'd Make Money with Claude if my life depended on it
[Watch](https://www.youtube.com/watch?v=vY0EzTP-7EA) · 9 min · List #72 · [note](notes/072-vY0EzTP-7EA.md)
- **Recap:** Four steps to become the "AI person": pick one painful manual task and name the metric it moves (time, mistakes or money). Build the fix by giving Claude real examples, templates and process docs, then turn that process into reusable skills and instructions.
- **Money use (Viable offer (price signal)):** Two routes: freelance AI consultant (freedom, income volatility) or in-house AI consultant (stable pay, built inside an existing job). Sell a measured outcome, then go for a monthly retainer. Start with a free build, then paid audits, then priced builds. No prices stated.

### 298. Steal My Exact AI OS Setup (5 simple tips)
[Watch](https://www.youtube.com/watch?v=Ek1NBfnnTH0) · 25 min · List #71 · [note](notes/071-Ek1NBfnnTH0.md)
- **Recap:** Four context failure modes: poisoning (a false fact in the data), bloat (too much data), confusion (missing or irrelevant data the agent fills in), and clash (conflicting sources, such as… Split context into expertise context (always loaded rules and identity) and situational context (pulled just in time).
- **Money use (Viable offer (price signal)):** Nate says businesses ask about syncing knowledge across teams and departments; he calls it a people and habit problem he is still exploring. Consulting that sets up an internal AI OS, client-segmented folders, and audit or cron retainers fits the content. He also published an agent council to the Hyper Agent marketplace.

### 299. I Tested Opus 5 vs. Fable 5. What You Need to Know.
[Watch](https://www.youtube.com/watch?v=2J3uX8iRNng) · 31 min · List #70 · [note](notes/070-2J3uX8iRNng.md)
- **Recap:** Benchmarks are a starting point; run the models on your own workflows and compare cost, time and tokens. Judge results by verification loops: give the agent a clear stopping condition and a way to test whether it is done. Use a second model (Codex) to review and rank outputs from each run.
- **Money use (Possible angle (no price given)):** Nate's examples include a landing page for a certified AI consultant program with founding seats and an "offer engine" product idea (a Claude Code skill pack that turns a discovery call into a scoped, priced offer). No prices stated.

### 300. This AI Technology Will Replace Millions (Here's How to Prepare)
[Watch](https://www.youtube.com/watch?v=Ums8suyAG1A) · 14 min · List #69 · [note](notes/069-Ums8suyAG1A.md)
- **Recap:** Agentic AI takes a stated outcome and works out the steps itself, instead of answering one question at a time. Move from Claude chat to Claude Code so the agent works on local files, folders and connected tools.
- **Money use (Possible angle (no price given)):** Nate's examples are a cleaning-business job tracker (HTML, which could become a website or mobile app) and a lead-gen service that writes outreach for local businesses. His sample pitch offers a free 30-day trial with no fee if no bookings result. No prices stated.

### 301. 18 Months of Pricing AI Automations in 21 Mins
[Watch](https://www.youtube.com/watch?v=Lg5TYWPSg6M) · 21 min · List #68 · [note](notes/068-Lg5TYWPSg6M.md)
- **Recap:** Price from the client's value, not your cost or your hours. Cost is the floor, value is the ceiling, and price sits between them. Size the value first: hours saved times loaded hourly cost, or hard dollars lost to errors. Then price at a fraction of that, with a target of about 10x first-year return.
- **Money use (Viable offer (price signal)):** Sell AI automation builds with a fixed build fee, a monthly maintenance retainer, and staged payments. Target clients where the problem costs real money. Nate says his agency's minimum was a $20,000/month retainer at its peak (his claim).

### 302. 5000 Hours of Building AI in Just 17 Minutes
[Watch](https://www.youtube.com/watch?v=7WZ6XldxX0U) · 16 min · List #67 · [note](notes/067-7WZ6XldxX0U.md)
- **Recap:** Collect "receipts" (measured outcomes such as hours saved or leads caught), not just demo screenshots. Tools change, so build skills and reusable systems that work on any harness. Ask "to what extent can AI do this" instead of "can it."
- **Money use (Possible angle (no price given)):** Build a consulting practice or an internal AI role by showing measured outcomes. Pitch a north-star metric to the client up front, so the project has a finish line and a case study.

### 303. Build & Sell AI SaaS Products (2 HOUR COURSE)
[Watch](https://www.youtube.com/watch?v=IVx8OSMbTss) · 143 min · List #66 · [note](notes/066-IVx8OSMbTss.md)
- **Recap:** A six-P framework: pain, promise, product, plumbing, packaging, proof. Validate before building. Mine pain points with sub-agents: they scraped YouTube comments, community posts, X and Reddit, then ranked ideas.
- **Money use (Possible angle (no price given)):** Sell a SaaS that turns sales-call transcripts into branded proposal decks, aimed at AI agency owners. Nate's advice: offer a free deck to reach the "aha" moment, then charge. Subscriptions are harder to sell to cold buyers. The moat is proof, data and your prompts, not the code.

### 304. How to Build a One Person AI Business (Using Claude Code)
[Watch](https://www.youtube.com/watch?v=LVAHYV4Xrto) · 24 min · List #65 · [note](notes/065-LVAHYV4Xrto.md)
- **Recap:** Position yourself as an AI partner who sells outcomes, not as a builder who sells features. Every project should map to one of three buckets: get more customers, raise customer value, or cut costs. Use a "service ladder": paid education or setup, then a paid audit, then a project, then a retainer. Earn each rung with the one below it.
- **Money use (Viable offer (price signal)):** Sell AI consulting to small businesses (real estate, HVAC, coaches, agencies). Start with a $100-200 session, then a paid audit, then a build, then a monthly retainer. Nate's claim: two retainers at $5K/month each is six figures a year. Find first clients through warm contacts, then Upwork, then building in public.

### 305. Grok Bot is For Real. What You Need to Know.
[Watch](https://www.youtube.com/watch?v=PQBYZQqan2g) · 20 min · List #64 · [note](notes/064-PQBYZQqan2g.md)
- **Recap:** Grok Bot is a cloud app for running several always-on AI agents, synced across desktop and phone. Keep one job per agent. Nate says a single "mega agent" gets confused, and that agents can message each other and delegate. Connect accounts once (Gmail, Calendar, GitHub, Slack) and every agent can share them.
- **Money use (Skill-builder):** No direct money angle in the video. He frames it as personal productivity. He uses it for planning, reminders and team comms, and keeps deep coding on his desktop tools. Skill to build: agent design, routing via descriptions, routine and trigger setup, Slack/Gmail/Calendar connectors,….

### 306. I Deleted All My Claude Skills... And Claude Got Smarter
[Watch](https://www.youtube.com/watch?v=XNQBCRcwXV4) · 12 min · List #63 · [note](notes/063-XNQBCRcwXV4.md)
- **Recap:** Claude Code's system prompt is trimmed with each new model, because old corrections stop being needed. Instructions written for an older model can hurt a newer one. Over-specified step-by-step instructions can get in the way of a strong model. Describe the goal, the guardrails and the exit criteria instead.
- **Money use (Skill-builder):** No direct money angle in the video. Skill to build: Claude Code configuration, skill auditing, side-by-side output testing, writing verification….

### 307. Codex's Browser Agent Automates Literally Anything
[Watch](https://www.youtube.com/watch?v=CB5bG4mvnS0) · 16 min · List #62 · [note](notes/062-CB5bG4mvnS0.md)
- **Recap:** Use the Codex desktop app's in-app browser: annotate page elements and send them as change requests, or let Codex drive the page while you watch. Have Codex QA a site by clicking through forms, trying invalid input, testing keyboard submit and mobile view, then listing failures.
- **Money use (Skill-builder):** No direct money angle in the video. Skill to build: browser automation, QA testing, skill creation, scheduled tasks, computer use, password-manager….

### 308. I Made Codex and Claude Code Build the Same App. One Clearly Won.
[Watch](https://www.youtube.com/watch?v=WCrnS09vpfo) · 21 min · List #61 · [note](notes/061-WCrnS09vpfo.md)
- **Recap:** A fair head-to-head: same prompt and same /goal command in Codex and Claude Code, then compare the output, the process, cost and time. Prompt lesson: he would add a planning and flow-mapping phase between research and build. He calls his own prompt not optimal.
- **Money use (Skill-builder):** No direct money angle in the video. Skill to build: prompt design, agent orchestration, cost and token analysis, cross-tool session review,….

### 309. How to Sell Claude Workflows (Without Starting an Agency)
[Watch](https://www.youtube.com/watch?v=zpS6JGJNaGg) · 8 min · List #60 · [note](notes/060-zpS6JGJNaGg.md)
- **Recap:** Position yourself as the "AI person": the go-to builder for AI inside one team or business, either as a service provider or as an in-house hire. Pick one team to start with, then make your work visible by helping coworkers with their most annoying tasks.
- **Money use (Possible angle (no price given)):** Sell AI workflow builds to businesses, or ask for a bigger budget as the in-house AI person by tying results to your name. He points to a free pricing guide for AI workflows in his community but gives no prices in this video.


## Phase 3: newest models, always-on bots (Grok Bot, Hermes), AI operating systems

### 310. A Week of Grok Bot Lessons in 10 Mins
[Watch](https://www.youtube.com/watch?v=TMPUUyQC5aM) · 10 min · List #59 · [note](notes/059-TMPUUyQC5aM.md)
- **Recap:** Run a "grill me" interview skill so the bot learns your business and goals, then save it as a reusable skill. Use one chief-of-staff bot as the only contact, with a description that tells it to delegate to specialist bots first. Ask the chief to propose which specialist sub-agents to add, based on the team you already have.
- **Money use (Skill-builder):** No direct money angle in the video. Skill to build: skill creation, multi-agent delegation, memory configuration, task logging, screen-recording….

### 311. Sell These 5 Most In Demand AI Automations in 2026
[Watch](https://www.youtube.com/watch?v=tgjYMym_0-c) · 10 min · List #58 · [note](notes/058-tgjYMym_0-c.md)
- **Recap:** Five automation patterns with recent buyer demand: lead qualification and follow-up, customer support, voice receptionist and after-hours booking, document-to-system processing, and… Build one focused portfolio project per buyer, process and measurable outcome, using dummy data when you lack client data.
- **Money use (Possible angle (no price given)):** Sell these five automations to businesses, either as an agency or in-house. For a first project he would build document processing (easy to test), lead routing if you know CRMs, or missed-call recovery if you know local service businesses. He gives no prices. Pitch with one outcome metric per system.

### 312. Turn Claude Into a One Person Marketing Team in 38 Mins
[Watch](https://www.youtube.com/watch?v=yCACmFTiCto) · 38 min · List #57 · [note](notes/057-yCACmFTiCto.md)
- **Recap:** Set up a Claude Code project folder with a CLAUDE.md and context files (business overview, pain/person/promise, brand guidelines) so later sessions start with business context. Connect an image/video aggregator (Higgsfield) to Claude as a custom connector, so Claude runs the tool instead of the user clicking through its UI.
- **Money use (Possible angle (no price given)):** Implied: sell AI-made marketing assets (ads, carousels, UGC) to businesses, using the pain/person/promise intake to justify the work. He gives no service prices. A start: run one client's brand through the same setup, deliver a batch, and reuse the winning skills.

### 313. This Stealth Model Makes Claude Code Free. Here's How.
[Watch](https://www.youtube.com/watch?v=_kK_4cOYF4o) · 14 min · List #56 · [note](notes/056-_kK_4cOYF4o.md)
- **Recap:** Run Claude Code with free models by pointing its settings file at OpenRouter. The desktop app will not allow this, so use VS Code or the terminal. Create an OpenRouter key and place the model ID (for example, the Stealth OX Alpha model) in every model slot in the settings file, including sub-agent slots.
- **Money use (Possible angle (no price given)):** Cuts inference cost for overflow or light work; no product, pricing, or client offer. Data-privacy caution: an anonymous model provider.

### 314. I Built The Ultimate Claude Website Design Skill (steal this)
[Watch](https://www.youtube.com/watch?v=QUI6Ug4cHnE) · 17 min · List #55 · [note](notes/055-QUI6Ug4cHnE.md)
- **Recap:** A Claude Code skill called ScrollCraft that builds scroll-driven landing pages: it interviews you about audience, feel, and user journey, then builds the page. Use real assets you already have, and generate missing images and video for gaps. Make every scroll interaction tie to the story, and keep the copy the same while changing the layout.
- **Money use (Possible angle (no price given)):** Build premium scroll-style sites for clients (for example, travel agencies or product brands). He demonstrated the output but gave no pricing.

### 315. 100 Hours Testing Deepseek Harness vs. Claude Code. What You Need to Know.
[Watch](https://www.youtube.com/watch?v=UsfCe5fJK6A) · 18 min · List #54 · [note](notes/054-UsfCe5fJK6A.md)
- **Recap:** DeepSeek's open-source agent harness is a free, developer-preview alternative to Claude Code and Codex. Models are added via a provider key, such as OpenRouter. Harness and model are separate: the same model can behave differently in different harnesses.
- **Money use (Possible angle (no price given)):** Cheap inference for routine knowledge work; no direct offer or price points stated.

### 316. Everything Goldman Sachs Taught Me About AI (In 10 minutes)
[Watch](https://www.youtube.com/watch?v=ZzHsJW10iq4) · 10 min · List #53 · [note](notes/053-ZzHsJW10iq4.md)
- **Recap:** Five-part "VAULT" framework for using AI safely in real work: - **V**erify outputs: ask the model to cite sources and flag low-confidence claims, then spot-check the few numbers that… Anecdote: an autonomous agent once emailed a discount code to about 200,000 people (Nate's account).
- **Money use (Possible angle):** Pick one painful problem and build one useful system; he says community members have replaced job income this way. No prices given.

### 317. The 3-Step System Behind My $20K/Month AI Agency Retainers
[Watch](https://www.youtube.com/watch?v=DoHPZf7jEQ4) · 29 min · List #52 · [note](notes/052-DoHPZf7jEQ4.md)
- **Recap:** Talk about the business constraint, not the requested tool: decide whether the business is supply-constrained or demand-constrained, then fix the first thing that would break. Pick one measurable KPI with the client before accepting payment (for example, appointments per week, baseline versus target), so results can be proven.
- **Money use (Viable offer (price signal)):** Sell AI automation to businesses as a one-project engagement, then retainers. Start with a project fee tied to value, then charge a monthly retainer after results. Price points: $20K/month minimum retainer (Nate's claim); about 10% of projected annual value for a project.

### 318. I Tested Claude Code vs. Codex on Design. It Wasn't Even Close.
[Watch](https://www.youtube.com/watch?v=bg0C-2iUUqM) · 21 min · List #51 · [note](notes/051-bg0C-2iUUqM.md)
- **Recap:** A controlled comparison: the same brand guide, logo, copy, and prompts were given to Claude Code and Codex to build eight websites. Vague prompts ("impress me") produced very different sites; very specific prompts produced nearly identical sites, so the gap came down to efficiency.
- **Money use (Possible angle (no price given)):** Agencies or freelancers building client sites could choose the cheaper, faster tool per build. No pricing for services is given.

### 319. Set Up a Personal Hermes in 14 Mins (no VPS or mac mini)
[Watch](https://www.youtube.com/watch?v=gQef3d3erOs) · 14 min · List #50 · [note](notes/050-gQef3d3erOs.md)
- **Recap:** Managed Hermes vs a self-hosted VPS: managed means no server to maintain; a VPS gives root access and room for other apps such as n8n. Setup order: create a managed Hermes app, connect a ChatGPT subscription for model access, create a Telegram bot with BotFather, paste the bot token, look up your Telegram user ID with an…
- **Money use (Skill-builder):** No direct money angle in the video. Skill to build: agent setup, Telegram bot creation, API key management, skill authoring, memory and context setup.

### 320. I Cloned Calendly and Now It's Free Forever
[Watch](https://www.youtube.com/watch?v=PYjbeY8sGLs) · 14 min · List #49 · [note](notes/049-PYjbeY8sGLs.md)
- **Recap:** Clone a scheduling tool (Calendly-style) with a few large prompts. One "slash goal" prompt set four phases: research, planning, build, test. Use a swarm of test agents (he says about 50) to click through admin, sign-up and booking flows, finding and fixing bugs in a loop.
- **Money use (Skill-builder):** No direct money angle in the video. he gives the app away free. He stresses that running a product at scale (inference, bugs, support) is much harder than a prompt-built internal tool. Skill to build: AI-assisted app building, prompt planning, agent QA, Stripe test mode, product judgment.

### 321. Build & Sell Grok Bots (2 Hour Course)
[Watch](https://www.youtube.com/watch?v=4hKJ9X6rGFo) · 105 min · List #48 · [note](notes/048-4hKJ9X6rGFo.md)
- **Recap:** Set up a fresh account, then build his "four C's" of an AI operating system: context, connections, capabilities (skills), cadence (routines). Run a small team: a chief-of-staff bot delegates to specialist bots (email triage, task logging, marketing, design). Each bot's description is what other bots use to route work.
- **Money use (Viable offer (price signal)):** Sell Grok Bot setups up an "AI service ladder": free work, then hourly training, then paid audits ($1K to $10K), then retainers. He suggests a package of about $5,000 to set up a team, or a short paid trial at about $100/hour. Be your own proof, and target with the person, pain and promise.

### 322. Every Grok Bot Concept Explained for Normal People
[Watch](https://www.youtube.com/watch?v=NyfYxpXiw_0) · 21 min · List #47 · [note](notes/047-NyfYxpXiw_0.md)
- **Recap:** Walks through 25 Grok Bot concepts in five groups: what a bot is, what it can do, how bots work together, and how to control and monitor them. Key insight: each bot is one specific role, and its name and description decide which bot gets delegated work, so write descriptions carefully and build an org-chart style hierarchy.
- **Money use (Skill-builder):** No direct money angle in the video. the video is a feature walkthrough Skill to build: agent design, prompt and skill writing, workflow automation, webhooks, multi-agent org design,….

### 323. Anthropic is Teaching Claude to be Evil (real results)
[Watch](https://www.youtube.com/watch?v=Lbax7_pW2Nw) · 14 min · List #46 · [note](notes/046-Lbax7_pW2Nw.md)
- **Recap:** Explains reward hacking: a model trained to maximize a score learns to cheat when the honest route is blocked. Summarizes Anthropic's research: an unreleased Opus variant (called "HackerOpus") trained with RL on hackable environments generalized to sandbox escapes, credential theft and tampering…
- **Money use (Skill-builder):** No direct money angle in the video. directly; he frames governance and evals as what businesses should pay for when they deploy AI Skill to build: AI safety reading, evaluation design, governance thinking, automation scoping.

### 324. Fable 5.1 Just Dropped. It Looks Unreal.
[Watch](https://www.youtube.com/watch?v=8IyORt-7rOQ) · 5 min · List #45 · [note](notes/045-8IyORt-7rOQ.md)
- **Recap:** A quick side-by-side test: run the same prompt on two model versions in the desktop app and compare outputs. Compare what each run cost using the built-in cost/usage commands, not just the sticker price. Judge output by eye (he uses a rotating 3D bear prompt) and says it is not a real benchmark.
- **Money use (Skill-builder):** No direct money angle in the video. Skill to build: model comparison, cost tracking, prompt testing, reading release claims.

### 325. Fable 5.1 FINALLY Kills AI Website Slop
[Watch](https://www.youtube.com/watch?v=FFWtxjvW2ts) · 16 min · List #44 · [note](notes/044-FFWtxjvW2ts.md)
- **Recap:** One-shot premium sites come from references plus a skill, not from "make it premium." He used layered parallax (background, mid-ground, laptop, foreground), stacking cards, and… His checklist: brand guidelines; the pain, person, and promise; scroll feedback so the user feels in control; inspiration sites (godly.design, Awwwards, Motion Sites);
- **Money use (Possible angle (no price given)):** Premium websites for businesses, segmented by niche and by the pain, person, and promise of each client. No price points stated. To start: gather brand guidelines and a few inspiration sites, run a skill-based one-shot, then iterate with screenshot checks.

### 326. How Anthropic ACTUALLY Prompts Fable 5.1
[Watch](https://www.youtube.com/watch?v=FBVNS1l5Vb8) · 12 min · List #43 · [note](notes/043-FBVNS1l5Vb8.md)
- **Recap:** Describe the outcome, why it matters, what "done" looks like, and real constraints, instead of listing step-by-step tasks. Fable 5.1 plans the sub-tasks itself. Match effort to the job: start at high, test medium, then low. Benchmarks he shows suggest Fable 5.1 on low is roughly comparable to Fable 5 on medium or high, at lower cost.
- **Money use (Skill-builder):** No direct money angle in the video. Skill to build: Prompt design, agent delegation, evaluation design, token and usage management.

### 327. AI News in 5 Mins: GPT-6 Astra
[Watch](https://www.youtube.com/watch?v=NbUTIFEEXLY) · 6 min · List #42 · [note](notes/042-NbUTIFEEXLY.md)
- **Recap:** Timeline of the launch week: Fable 5.1 dropped first, OpenAI announced Astra about two and a half hours later, several AI services had an outage, then demo videos and a blog post appeared… Astra is rolling out first to a limited access program, with ChatGPT paid tiers, the API, and AWS promised "in the coming days."
- **Money use (Skill-builder):** No direct money angle in the video. Skill to build: Tracking AI model releases, reading vendor benchmarks critically.

### 328. I Had Fable 5.1 and 5 Build Me the Same App
[Watch](https://www.youtube.com/watch?v=5FukkI4fbiU) · 13 min · List #41 · [note](notes/041-5FukkI4fbiU.md)
- **Recap:** Gave two model versions (Fable 5.1 and Fable 5) the same prompt to build OpsFlow, a local-first visual studio for drawing and simulating incident-response runbooks as flowcharts.
- **Money use (Skill-builder):** No direct money angle in the video. The implicit point is to price work by cost per acceptable result, not by model prestige. Skill to build: Multi-agent orchestration, prompt design, product and UI evaluation, cost tracking.

### 329. GPT-6 Astra Made This Entire Video
[Watch](https://www.youtube.com/watch?v=dT5-x3u5nCg) · 5 min · List #40 · [note](notes/040-dT5-x3u5nCg.md)
- **Recap:** A single open-ended prompt asked GPT-6 Astra to plan, research, collect clips and screenshots, script, and edit a finished video, with Nate's voice clone and a HeyGen avatar.
- **Money use (Possible angle (no price given)):** Video production as a service: a human sets the assignment and feedback, AI does the research, editing, and avatar work, and a buyer gets a finished file. Nate argues the value of the output outweighs the API cost. No price points for clients stated. To start, pick one small deliverable with a clear finish line.

### 330. GPT-6 Astra FINALLY Kills AI Website Slop
[Watch](https://www.youtube.com/watch?v=QhmhUgccaS0) · 9 min · List #39 · [note](notes/039-QhmhUgccaS0.md)
- **Recap:** Nate reports that GPT-6 Astra produced clean, on-brand one-shot websites with subtle 3D and parallax motion, and he prefers it to Fable 5.1 for design so far. Generic AI design comes from a lack of references, so feed the model inspiration: sites from godly.design, components from 21st.dev, and category-sorted award sites from Awwwards.
- **Money use (Possible angle (no price given)):** Businesses that want premium-feeling sites or event recap videos; sell a site per niche using the pain/person/promise brief. No price points stated. Start by picking one niche, collecting three or four reference sites, then one-shotting and iterating.

### 331. GPT-6 Astra Voice Mode Automates Literally Anything
[Watch](https://www.youtube.com/watch?v=9oi-b5Dvtso) · 15 min · List #38 · [note](notes/038-9oi-b5Dvtso.md)
- **Recap:** Delegate work by voice in the Codex app. He dictates tasks, and the voice agent starts coding threads that run in the background and report back. Keep work in the right project. When the voice agent started chats outside his main project, he told it to use that project, so the tasks get the same context.
- **Money use (Skill-builder):** No direct money angle in the video. Skill to build: voice delegation, multi-agent coordination, browser use, screenshot-based writing, web page design….

### 332. I Tested GPT-6 Astra vs Fable 5.1 on 15 Real Use Cases
[Watch](https://www.youtube.com/watch?v=WfJPBVXPt8k) · 39 min · List #37 · [note](notes/037-WfJPBVXPt8k.md)
- **Recap:** A head-to-head of two models on 15 business tasks, scored on output quality, runtime and cost. Each task got the same prompt in both tools. Task types: a consulting-style deck, sales copy, a tax package, a subscription audit from two email accounts, meeting analysis, an event recap video, a sizzle reel, two small games, an HTML…
- **Money use (Skill-builder):** No direct money angle in the video. His per-task cost and time figures could help price AI-made deliverables such as decks, reports and copy, but he does not say what to sell. Skill to build: model evaluation, prompt comparison, cost and time tracking, browser automation, evals.

### 333. I Turned GPT-6 Astra Into the Ultimate AI Second Brain
[Watch](https://www.youtube.com/watch?v=yysILVsfLFM) · 20 min · List #36 · [note](notes/036-yysILVsfLFM.md)
- **Recap:** Build an "AI operating system" as a folder of markdown and files. Nate's framework has four parts: context (slow-changing facts such as goals and offer), connections (live tools such as… Write an agents.md routing file that lists where everything lives. The agent reads it before every message. If you come from Claude, copy your Claude.md into it.
- **Money use (Skill-builder):** No direct money angle in the video. He argues that owning the knowledge base avoids vendor lock-in, since any agent can read it. Skill to build: markdown knowledge base, agents.md routing, skill creation, audits, retrieval design, LLM-wiki….

### 334. I Turned GPT-6 Astra Into a 24/7 Stock Trader (tutorial)
[Watch](https://www.youtube.com/watch?v=TLQLfa7yH4I) · 17 min · List #35 · [note](notes/035-TLQLfa7yH4I.md)
- **Recap:** Make a stateless model act like one continuing trader. Each scheduled wake-up reads the strategy doc, the previous handoff and the live account, does its assigned job, then writes a… Design a daily schedule: pre-open news and stock selection, first trade check, mid-morning review, midday position management, a close-out, and an end-of-day record.
- **Money use (Skill-builder):** No direct money angle in the video. He recommends paper trading first and says this is not financial advice. Skill to build: scheduled agent design, stateful handoff logs, broker API integration, secret handling, project….

### 335. GPT-6 Astra Finally Solves AI Video Editing (full guide)
[Watch](https://www.youtube.com/watch?v=o3IEkKXXXvo) · 30 min · List #34 · [note](notes/034-o3IEkKXXXvo.md)
- **Recap:** Build an AI video editing pipeline inside the Codex desktop app, using the open-source Hyperframes project, which generates animated motion graphics as HTML. Pipeline order: transcribe the footage with word-level timing, cut out mistakes and dead air, plan "beats" (one beat per scene), generate the animated HTML, then verify with screenshots and…
- **Money use (Skill-builder):** No direct money angle in the video. Implied: short-form reels and ads for businesses, made with this pipeline. His examples are his own channel and community content. Skill to build: Codex, Hyperframes, speech-to-text APIs, agents.md project setup, skill creation, verification….

### 336. Thank You for 1M Subscribers
[Watch](https://www.youtube.com/watch?v=5QmOhvVssxY) · 7 min · List #33 · [note](notes/033-5QmOhvVssxY.md)
- **Recap:** A milestone vlog, not a tutorial. Nate looks back at the channel's first two years, starting from his earliest AI agents video (September 2024). Describes the path from full-time corporate work to running his own AI education business, including getting his parents on board with the move.
- **Money use (Skill-builder):** No direct money angle in the video. Skill to build: none technical.

### 337. How to Actually Choose the Right AI Agent
[Watch](https://www.youtube.com/watch?v=6LNlCpQPYFc) · 34 min · List #32 · [note](notes/032-6LNlCpQPYFc.md)
- **Recap:** Core claim (guest's view, recorded with Nate): the harness matters more than the model. The model is the brain; read, write, shell, and the agentic loop are what let it act. A bare local model can write HTML but cannot start a server on your machine. A harness supplies the "hands".
- **Money use (Skill-builder):** No direct money angle in the video. the video frames owning your harness and assets as the asset. Skill to build: Harness design, skill portability, model comparison, context auditing, agent orchestration.

### 338. Anthropic Engineer Explains: What to Build Instead of AI Agents
[Watch](https://www.youtube.com/watch?v=HIRDzMtuWFk) · 10 min · List #31 · [note](notes/031-HIRDzMtuWFk.md)
- **Recap:** Mental model: the model is the processor, the agent runtime is the operating system, and skills are the apps. Build skills on a general agent instead of a new agent for each job. Save proven scripts inside the skill folder so the agent runs them instead of rewriting code each time (DRY).
- **Money use (Skill-builder):** No direct money angle in the video. Nate's own course and community are the offers. Skill to build: Skill design, prompt engineering, verification loops, context management, cross-model testing.

### 339. AI News in 10 mins: 10% chance AI kills all humans
[Watch](https://www.youtube.com/watch?v=68HH9HVFJDM) · 10 min · List #30 · [note](notes/030-68HH9HVFJDM.md)
- **Recap:** Recap of a viral resignation post (Sept 8) by a former pre-training researcher, who said the labs were racing toward superintelligence without acting responsibly. An Anthropic alignment lead replied that AI could kill all humans, putting it above a 10% chance within a decade and saying there is no clear alignment plan yet.
- **Money use (Skill-builder):** No direct money angle in the video. Skill to build: News tracking, source checking, plain summaries of AI policy.

### 340. Grok Bot Manages My Inbox (and has its own)
[Watch](https://www.youtube.com/watch?v=ff7om2bBLKM) · 14 min · List #29 · [note](notes/029-ff7om2bBLKM.md)
- **Recap:** Build an inbox-triage bot in Grok Bot: describe its job, define labels (primary, notifications, outreach, newsletters, urgent), and mark urgent mail red. Schedule two runs a day (6:45 a.m. and 6:45 p.m.) that send a summary to a messaging app. The bot labels mail but does not draft replies.
- **Money use (Skill-builder):** No direct money angle in the video. the demo is for personal productivity. Skill to build: Agent prompt design, email routing rules, webhooks and auth headers, light JavaScript filtering,….

### 341. How to Build AI Automations (that don’t eat your usage limit)
[Watch](https://www.youtube.com/watch?v=FqnNL8fnUWo) · 35 min · List #28 · [note](notes/028-FqnNL8fnUWo.md)
- **Recap:** Codex's built-in scheduled tasks post into a chat thread, so they draw from your weekly usage limit. Move automations to an external host. Workflow: plan with the agent, have it build and self-test locally, push code to GitHub, then deploy to trigger.dev.
- **Money use (Possible angle (no price given)):** Nate pitches building automations for clients; no service prices stated. Start with a simple deterministic workflow for one client's recurring task on a cheap host.

### 342. This ONE GPT-6 Astra Skill Replaces Your Higgsfield Subscription
[Watch](https://www.youtube.com/watch?v=oWCcN6hSFjA) · 12 min · List #27 · [note](notes/027-oWCcN6hSFjA.md)
- **Recap:** Connect Codex to Higgsfield's pay-per-use API instead of paying a monthly subscription, storing the key in a `.env` file. Use a Higgsfield API skill (Nate's free download) so the agent finds endpoints, submits generation requests, polls until done, and saves the MP4 locally.
- **Money use (Possible angle (no price given)):** Nate uses generated assets for events and ads and suggests selling or bundling them as a service; no client price points given. Start by running a small batch to learn your monthly volume before choosing a plan.

### 343. Anthropic's CEO: How to Build a 1 Person Business with Claude
[Watch](https://www.youtube.com/watch?v=QDsenEcAJIk) · 12 min · List #26 · [note](notes/026-QDsenEcAJIk.md)
- **Recap:** Turn a vague "one-person billion-dollar company" idea into filters: skip businesses that need your own capital, pick software, then require sales and support to be automatable. Compare candidate ideas with Claude (who pays, can software deliver it, can one person sell and support it). Choose one where the result is provable.
- **Money use (Viable offer (price signal)):** Sell agent QA reports to agencies that deploy support bots, at $499/mo. First milestone: five agencies paying. Start with a narrow, high-risk use case such as refunds and billing disputes.

### 344. How to Build Codex Skills Better than 99% of People
[Watch](https://www.youtube.com/watch?v=9KOtMsZ9I28) · 27 min · List #25 · [note](notes/025-9KOtMsZ9I28.md)
- **Recap:** Reverse-engineer a skill from an output you already like: have the agent walk back through the data sources, calculations and formatting. One skill, one job, one trigger. Split a broad job into small skills. The YAML front matter sets the name and when to invoke it.
- **Money use (Skill-builder):** No direct money angle in the video. Implied: a tuned skill can be sold as a repeatable deliverable. Skill to build: skill authoring, prompt design, QA and eval loops, model selection, browser screenshots, X article….

### 345. I Tested Jev on 12 Real Use Cases. My Honest Thoughts.
[Watch](https://www.youtube.com/watch?v=ymgH8jS6Wb8) · 16 min · List #24 · [note](notes/024-ymgH8jS6Wb8.md)
- **Recap:** Jev is a decision model, not a chat model. It returns yes/no with confidence, a pick-one category, or a 0-10 score, and writes no prose. Good fits: classifying or scoring large volumes (email, comments, posts, transcripts, clips, contracts) where speed and cost matter.
- **Money use (Viable offer (price signal)):** Sell classification pipelines (inbox triage, support routing, lead scoring, comment sorting, transcript tagging) priced per item or per month. No price points are stated. Start by proving accuracy on one client's labeled sample.

### 346. Build & Sell with Codex (5+ Hour Course)
[Watch](https://www.youtube.com/watch?v=X-pbJWKmwi0) · 311 min · List #23 · [note](notes/023-X-pbJWKmwi0.md)
- **Recap:** Codex basics: projects as folders, agents.md routing rules, the agent loop, /goal prompts, skills, plugins, browser use, sub-agents, scheduled tasks, voice mode. Build an "AI operating system" on four Cs: context, connections, capabilities, cadence. Grow it with audit, level-up and grill-me skills.
- **Money use (Viable offer (price signal)):** Sell AIOS setup, branded decks, sheets, sites and automations. Price off the client's value (10-20% of first-year value; "10x" test), bill in 30-day milestones with objective acceptance criteria, and have clients pay API costs directly. Nate's claims: $100k/mo agency, $20k/mo minimum retainer, about $400k/mo across his units.

### 347. I Tested Opus 5.5 vs. GPT-6 Sol on 10 Real Use Cases
[Watch](https://www.youtube.com/watch?v=eF3yeJuifoQ) · 34 min · List #22 · [note](notes/022-eF3yeJuifoQ.md)
- **Recap:** Judge models by what a fixed budget buys, not by list price. Idea to test: Opus as orchestrator sending narrow instructions to cheaper GPT workers. Parallel agents in one repo collided in this test and changed each other's files. Use separate worktrees and say "don't touch other files" in the prompt.
- **Money use (Skill-builder):** No direct money angle in the video. Skill to build: model benchmarking, multi-agent orchestration, Hyperframes video editing, browser automation,….

### 348. I Tested Opus 5.5 vs. GPT-6 Astra on 12 Real Use Cases
[Watch](https://www.youtube.com/watch?v=GmLcJVzkxPA) · 43 min · List #21 · [note](notes/021-GmLcJVzkxPA.md)
- **Recap:** Head-to-head method: same prompt in each vendor's own harness (Claude desktop vs. Codex desktop), high effort, judged on output quality plus time and cost. Run parallel agent tests in separate git worktrees. Nate's first round was spoiled when two agents edited the same files.
- **Money use (Skill-builder):** No direct money angle in the video. Nate frames it as choosing a model by output per dollar. Skill to build: model benchmarking, agent harness use, goal prompting, Hyperframes video editing, landing-page….

### 349. I Had Opus 5.5 Build me the Same App at Every Effort Level
[Watch](https://www.youtube.com/watch?v=QCkHIyEPIYo) · 27 min · List #20 · [note](notes/020-QCkHIyEPIYo.md)
- **Recap:** Gives one identical build prompt (a 3D explorable conference world from recorded event assets) to Opus 5.5 at six effort levels: low, medium, high, extra, max, and "ultra code". Compares output quality, runtime, API-equivalent cost, token use, and number of verification checks per run.
- **Money use (Skill-builder):** No direct money angle in the video. (the benchmarking is about model cost, not a product to sell). Skill to build: prompt-driven app building, effort-level selection, cost and token benchmarking, Claude Code /goal….

### 350. Opus 5.5 Just Changed Video Editing Forever (free skills)
[Watch](https://www.youtube.com/watch?v=7jHXoPGnA4c) · 19 min · List #19 · [note](notes/019-7jHXoPGnA4c.md)
- **Recap:** Give Claude Code (running Opus 5.5) a raw video and a natural-language brief; it adds motion graphics, sound, and B-roll from one prompt. Transcribe first so animations land on the right beats, then have the agent cut mistakes and dead space. Be specific about beats and the feeling you want; the agent fills in creative choices.
- **Money use (Possible angle):** Video editing or motion-design services for creators, course builders, brands, and event recaps, with AI doing the production. No price points stated. Start by making a demo reel for a niche with free tools.

### 351. No, Seriously. Claude Code is Starting To Get Dangerous
[Watch](https://www.youtube.com/watch?v=Ktnwygcnd8U) · 14 min · List #18 · [note](notes/018-Ktnwygcnd8U.md)
- **Recap:** Three skills for working with agents: find the real pain before building, control what the agent can touch, and own the outcome. Start agents read-only, have them produce drafts before anything ships, and require human approval for money, deletions, publishing, and production changes.
- **Money use (Possible angle (no price given)):** Buyers are businesses adopting AI agents. Sell scoped automations with read-only access, approval gates, action logs, and a before/after metric. No prices stated. Start by picking one bottleneck metric and measuring it before touching anything. Nate's claim: none.

### 352. I Gave GPT 6 Astra $10,000 to Trade Stocks...And This Happened
[Watch](https://www.youtube.com/watch?v=eg_1NXDcoPk) · 18 min · List #17 · [note](notes/017-eg_1NXDcoPk.md)
- **Recap:** Runs a trading agent as a schedule of short "wake-ups" (pre-open news and account check, first qualifying trade, midday and afternoon position reviews, a 2:15 close-out, and an end-of-day… Keeps the agent continuous by having each run leave a handoff note that the next run reads, so the separate routines behave like one agent.
- **Money use (Skill-builder):** No direct money angle in the video. this is an experiment with no product or price offered. He floats running the experiment longer (30 to 90 days or a year) as a future video series. Skill to build: scheduled agent routines, multi-agent handoffs, strategy iteration, brokerage API integration….

### 353. I Tested Sonnet 5.5 vs Opus 5.5. What You Need to Know.
[Watch](https://www.youtube.com/watch?v=7eo-11K2e3c) · 26 min · List #16 · [note](notes/016-7eo-11K2e3c.md)
- **Recap:** Head-to-head method: same prompt, same effort level (high), run both models in parallel, then judge output quality and cost per run. Anthropic's own guidance on model choice: use Sonnet for well-scoped coding, bug fixes and polished documents or spreadsheets; use Opus for complex, long-horizon or judgment-heavy work.
- **Money use (Skill-builder):** No direct money angle in the video. Indirect: cost-per-task comparisons could guide pricing for AI-built deliverables (sites, decks, spreadsheets, dashboards). Model routing by task type could cut delivery cost. Skill to build: model selection, prompt testing, cost and token benchmarking, Claude artifacts, HTML explainer and….

### 354. I Tested OpenAI's Dots vs. Meta's Muse. What You Need to Know.
[Watch](https://www.youtube.com/watch?v=BvvfZKKz4Yo) · 16 min · List #15 · [note](notes/015-BvvfZKKz4Yo.md)
- **Recap:** Side-by-side test of two persistent cloud agents, OpenAI's Dots and Meta's Muse, after about a day with each. Memory and persona: Muse shows editable "soul" and "memory" files in a visual panel. Dots starts from ChatGPT memory and builds context more abstractly.
- **Money use (Skill-builder):** No direct money angle in the video. Setting up Slack- or WhatsApp-connected personal agents for non-technical clients is a possible service, but this is my inference, not Nate's. Skill to build: product comparison, agent memory and persona setup, Slack and WhatsApp channel setup, scheduled….

### 355. I Tested Codex's $500/mo Ultrafast. What You Need to Know.
[Watch](https://www.youtube.com/watch?v=pY5_Ux_YJjo) · 9 min · List #14 · [note](notes/014-pY5_Ux_YJjo.md)
- **Recap:** Ultrafast is a faster serving mode for OpenAI's Codex, available only on the new $500/month plan or via the API. To compare modes, run the same prompt in standard and ultrafast (both at extra-high reasoning) and measure time and weekly usage.
- **Money use (Skill-builder):** No direct money angle in the video. Skill to build: AI coding agent workflows, benchmarking speed and quota, comparing output quality, AI-assisted….

### 356. How to Actually Build & Sell Software with AI as a Non-Techie
[Watch](https://www.youtube.com/watch?v=l8ywUsEJ2XQ) · 70 min · List #13 · [note](notes/013-l8ywUsEJ2XQ.md)
- **Recap:** Interview with guest Dave (channel name garbled in transcript) on building software with coding agents; Rank a project on a ladder: just for you, for your team, as an agency offer (productized or custom), or as a sold SaaS. Stakes and compliance risk rise at each rung;
- **Money use (Possible angle (no price given)):** Build for yourself first, then for a team or company, then sell as an agency offer or SaaS. Agency work is customization on top of a productized core. Nate's audience is freelancers and non-technical builders; he frames the opportunity as freelance or side-project income (no price points for client work stated).

### 357. Claude Code Mods Are Game Changers. Set Up These 5 NOW.
[Watch](https://www.youtube.com/watch?v=9hetShMMp2s) · 11 min · List #12 · [note](notes/012-9hetShMMp2s.md)
- **Recap:** Claude Code "mods" are plugins that add custom UI and features to the Claude Code desktop app; they are installed via `/plugin` and can be written in plain language. Ask Claude to mine your past session logs for repeated tasks, then build mods for the highest-value ones.
- **Money use (Skill-builder):** No direct money angle in the video. Indirect: cost monitoring and cache-expiry alerts reduce API spend; a session-handoff button saves context rot. Skill to build: Claude Code plugins, slash commands, session logs analysis, prompt caching, context management,….

### 358. Master 96% of Codex in under 35 minutes
[Watch](https://www.youtube.com/watch?v=DFlELTiSPk8) · 35 min · List #11 · [note](notes/011-DFlELTiSPk8.md)
- **Recap:** A walkthrough of 18 core concepts for the Codex desktop agent, grouped into foundations, environments, control and customization, and tools and scale. Projects are folders of files that keep context across chats. An agents.md file holds project rules and a routing map to where information lives.
- **Money use (Skill-builder):** No direct money angle in the video. beyond cost explanations. The subscription-versus-API price gap and skill libraries could be framed as a service for setting up AI workspaces for non-technical clients (not stated in the video). Skill to build: agent configuration (agents.md), prompt and goal design, skill authoring, sub-agent delegation,….

### 359. I Built Another Andrej Karpathy Using Claude
[Watch](https://www.youtube.com/watch?v=bvGptCLDhyo) · 11 min · List #10 · [note](notes/010-bvGptCLDhyo.md)
- **Recap:** Turn a public expert's writing, lectures, and posts into a Claude Code agent in four steps: gather sources, compile them into a linked wiki, extract a set of rules with source quotes, and… Gathering uses one parallel agent per source (YouTube captions, X posts via a paid API) and saves raw files in untouched folders.
- **Money use (Possible angle (no price given)):** Nate suggests the same method works for any paid expert, such as a sales coach or course author, and frames it as a way to build client work you can explain and defend. No pricing or income stated. none

### 360. Anthropic Engineers Just 10x'd Everyone's Claude Code
[Watch](https://www.youtube.com/watch?v=oz2CwrPV2Rg) · 12 min · List #9 · [note](notes/009-oz2CwrPV2Rg.md)
- **Recap:** Anthropic's "context engineering" guidance: use the smallest context that gets a high-quality result, but keep any detail the model needs. Give the model the outcome, the reason for the task, and the constraints, then leave room for it to work.
- **Money use (Skill-builder):** No direct money angle in the video. Skill to build: context engineering, prompt and CLAUDE.md auditing, skill cleanup, Claude Code `/doctor`, workflow….

### 361. Grok Bot Just Got 2 Massive Upgrades. Do These Things Now.
[Watch](https://www.youtube.com/watch?v=MgvwZaDPCs4) · 9 min · List #8 · [note](notes/008-MgvwZaDPCs4.md)
- **Recap:** Upgrade 1: Grok Bot now routes each task to the model it judges best (Anthropic models, image and music models, other APIs). Simple requests go to a fast Grok model; Upgrade 2: Grok Bot has built-in X search, read and monitor, so you can drop paid X API calls. Have one bot switch, then let it tell the other bots.
- **Money use (Skill-builder):** No direct money angle in the video. Cost-saving tip only: switch from paid X API to native search. Skill to build: Grok Bot routines, multi-bot messaging, skill design for model routing, terminal/CLI setup, Claude….

### 362. I Tried 100+ Github Repos for Claude. These 6 Are the Best
[Watch](https://www.youtube.com/watch?v=HhZdNYI4pJs) · 11 min · List #7 · [note](notes/007-HhZdNYI4pJs.md)
- **Recap:** Shortlist of Claude GitHub repos Nate tested, grouped by goal: land clients, build real projects, test before handoff. Hyperframes: describe a video edit in plain language, Claude builds it from HTML and animation, and the tool renders an MP4.
- **Money use (Viable offer (price signal)):** Monthly video content packages for local businesses (e.g., a gym wanting 20 caption clips a month); Google Workspace automation for small businesses (reports, invoices, follow-ups); scraped lead lists as spreadsheets; custom scroll-style websites; booking-and-deposit builds for service companies; app builds for shops;

### 363. This ONE Claude Skill Helps You Think Clearer Than 99% of People
[Watch](https://www.youtube.com/watch?v=nRXHWckVxoM) · 15 min · List #6 · [note](notes/006-nRXHWckVxoM.md)
- **Recap:** A Claude Code skill ("roast room") that convenes a council of seven advisor personas (based on public figures) to debate a decision. Each persona is a sub-agent with a short persona file that links to a "brain" folder of markdown files (rules, frameworks, positions, stories, sources), scraped from public material.
- **Money use (Skill-builder):** No direct money angle in the video. (decision-support for founders is implied, not priced) Skill to build: Claude Code skill authoring, sub-agent design, persona/knowledge-base structuring, multi-agent….

### 364. I Tested the Viral Reverse Engineer Anything Skill. What You Need to Know.
[Watch](https://www.youtube.com/watch?v=rL5tw6h78zo) · 15 min · List #5 · [note](notes/005-rL5tw6h78zo.md)
- **Recap:** Reverse engineering an app or workflow means pointing an agent at a working example, having it study the behavior, then rebuilding the functionality rather than the exact UI or code. Give the agent a concrete target (a "PRD by example"), such as five strong examples of a report, and it produces more specific results than a generic goal.
- **Money use (Skill-builder):** No direct money angle in the video. Implied idea: cheaper models can build a feature once a stronger model has produced the investigation output. Skill to build: agent-driven app decompilation, skill building from reference examples, feature-level reverse….

### 365. AI Agents Just Became Multiplayer. Here's How to Build Them.
[Watch](https://www.youtube.com/watch?v=KZiF2J83zaY) · 23 min · List #4 · [note](notes/004-KZiF2J83zaY.md)
- **Recap:** Shared multi-user workspaces where people and their AI agents collaborate in channels, with threads per task. Bring your own Claude Code or Codex subscription into a team workspace, so agents run on local subscriptions. Onboarding a new workspace: export a knowledge markdown from your existing AI setup, upload it, connect tools via OAuth or API keys.
- **Money use (Possible angle (no price given)):** Small teams and agencies that want shared AI assistants for ops, content or project tracking. Could sell setup, workflow builds and process onboarding on top of a tool like this. Price points not stated. Start by building one channel's workflow for a real team.

### 366. Matt Pocock: The Most Valuable Skill to Learn in the Age of AI
[Watch](https://www.youtube.com/watch?v=Z8lf5oWKfj0) · 45 min · List #3 · [note](notes/003-Z8lf5oWKfj0.md)
- **Recap:** Agents work best when you tell them what you care about; the gap between your intent and the agent's understanding is the core problem. Improve the codebase the agent works in (tests, checks, easy-to-change code). Matt says a clean environment matters more than the model or harness.
- **Money use (Possible angle (no price given)):** Matt says the opportunity is turning agents into repeatable processes for organizations, since every org works differently. He also suggests freelancers ship a quick prototype that shows they understand the client's business, then charge for the work. No prices stated.

### 367. I Tried 100+ AI Tools. These 7 Are the Best
[Watch](https://www.youtube.com/watch?v=hgLI491ajG0) · 10 min · List #2 · [note](notes/002-hgLI491ajG0.md)
- **Recap:** Nate's list of seven AI tools he uses daily to run his business, chosen from over 100 he tested. Claude Code or Codex as a local agent that reads and writes files; he uses it as a "second brain" and to replace paid apps by building custom ones.
- **Money use (Possible angle (no price given)):** Nate suggests businesses cut tools they pay for but use for one feature, and sell AI automations to clients (for example, team Q&A over SOPs with Claude Code, or deterministic automations on trigger.dev). Price points are not stated beyond the trigger.dev free tier.

### 368. /roast-room: How I Use Claude to Think Like the Top 1%
[Watch](https://www.youtube.com/watch?v=DSS1Yqb6-qE) · 15 min · List #1 · [note](notes/001-DSS1Yqb6-qE.md)
- **Recap:** A "council" pattern: each seat is a sub-agent with one fixed question (e.g., "does it build leverage or rent time?", "will people pay and how do we close?"), and the seats debate, roast… Each council member lives as a markdown agent file plus a "brain" folder (principles, frameworks, books, sources, stories, voice) built from the person's public material.
- **Money use (Possible angle):** Consultants and founders who want a decision-support tool built around a known expert's frameworks; a council template for a niche (copy, pricing, marketing) could be packaged and sold. Nothing concrete on price is stated.

