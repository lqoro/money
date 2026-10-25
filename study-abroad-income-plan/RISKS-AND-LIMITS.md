# Risks and limits (read before earning money)

This is a practical checklist, **not legal or tax advice**. Rules differ by country and change. When unsure, ask the official source named below.

## 1. Student visa and work rights (do this first)
- Many student visas limit **paid work** (hours per week, on or off campus) and some do not allow **self-employment or freelancing at all**, even when the clients and payments are abroad. In some countries (the US on an F-1 visa is a well-known strict example) self-employment off campus is generally not allowed without specific authorization.
- Doing unauthorized work can risk your visa and future applications. The penalty is not worth a first small client.
- **What to do:** ask your school's international student office and read the immigration authority's page for your visa type. Ask these exact questions:
  1. Is freelance or self-employed work allowed on my visa? With foreign clients? With my own company abroad?
  2. Is there an hours cap, and does unpaid work (free pilots) count?
  3. Do I need a permit, and is income from home-country clients treated differently?
- **Safe meanwhile:** learning, building demos, personal projects, open-source work, and free portfolio pieces that you do not charge for. Ask about "volunteer" or "unpaid pilot" rules before offering free pilots to businesses, since some places treat unpaid work for a business as work.
- Alternatives that may be allowed in some places (verify): on-campus jobs, paid internships or co-op placements, research-assistant roles, or a job at a company that sponsors work.

## 2. Taxes and money handling
- Income may be taxable in the country you study in and/or your home country, depending on residency rules. Ask the school's tax advice service or a qualified accountant.
- Keep records: invoices, payment receipts, expenses (tool subscriptions, hosting).
- Use a payment route you can document (invoice, contract, payment processor). Avoid cash-only arrangements.

## 3. Contracts and client risk
- Written scope, price, payment schedule, ownership of accounts and what is excluded (see [AGENT-INCOME-PLAYBOOK.md](AGENT-INCOME-PLAYBOOK.md) delivery checklist, from V204, V219, V312).
- Clients should own the accounts and pay API costs directly (V23, V204, V219).
- Do not promise results you cannot control. Avoid guarantees like "doubles your sales". V69's sample pitch offers a free 30-day trial with no fee if no bookings result; that shifts all the risk to you, so do not copy it blindly.
- You are liable for mistakes an automation makes on a client's behalf: use approval steps for outward actions (V288, V317), read-only access first (V191-V193), and logs.

## 4. Data privacy and regulated data
- Client email, calendar, documents and call recordings are personal data. Know the privacy rules where the client and the end customers live (for example GDPR in the EU).
- Health, legal and financial data have extra rules. V239 flags HIPAA for a mental-health voice product. Do not build for these areas without advice.
- Voice agents: check call-recording consent rules (V125, V222).
- Redact personal data before sending it to a model where possible (V220).

## 5. Platform terms and legal limits
- **Scraping:** scraping Google Maps or LinkedIn may breach their terms (V347 notes this for Google Maps; V355, V362 cover Google-based LinkedIn scraping). Use allowed sources or official APIs where possible.
- **Cold email and messages:** anti-spam and marketing rules apply in many places. My notes on V347 and V350 add this caution; the videos themselves do not cover it. Get consent where required and include opt-outs.
- **AI service terms:** each model provider has rules for automated use, resale and subscriptions. Nate claims accounts were banned for running a third-party bot on a Max subscription (V191). Verify current terms and use API keys where the terms require them.
- **Platform content:** faceless AI video channels (V271, V286, V300, V310) face platform spam and authenticity policies. I would not build a plan around them.
- **Trading bots:** V17, V35, V138 and V146 are experiments, "not financial advice". Do not offer trading automation to clients without licensing advice.

## 6. Security (yours and your client's)
- Separate accounts for bots; read-only first; secrets in `.env`; webhook authentication; no public endpoints without auth (V261, V191-V193, V29).
- Cited example: about 900 exposed always-on bot servers with no password (V192, from a tweet Nate cites).
- Treat session links, QR codes and webhook URLs like passwords (V180, V29).
- Keep logs and a way to pause every automation.

## 7. Money-claims red flags (Nate's content and others)
- Many videos include **income screenshots and revenue claims** ($100K/month agency, $20K/month retainers, $500K in 8 months, $240K in 6 months; V23, V52, V68, V281, V289). They are claims, not audited results.
- Nate funnels to a free school community, a paid "Plus" community (about $89/month per V232), courses (for example "Automation to Monetization", V242, V245) and sponsors (hosting, voice tools, video tools). Some links are affiliate. In V66 he notes he co-founded or joined a tool he presents, which he flags as a conflict.
- Guests' prices (for example $15K-$35K discovery blueprints in V109) are from large agencies and are not a baseline for a beginner.
- Rule of thumb: copy the *method* (free pilot, measured result, value-based price), not the *income number*.

## 8. Practical limits on this plan
- **Time:** study load comes first. The ranking in [INCOME-IDEAS.md](INCOME-IDEAS.md) assumes 5-15 hours a week once running, and the first client usually takes 4-8 weeks of outreach.
- **Skills:** early builds will be slower and need more testing. Price pilots honestly and learn from each.
- **Model and tool changes:** videos reference fast-moving products (model names, bot tools, pricing). Check current features and prices before relying on any detail.
- **Notes are AI-condensed:** my notes paraphrase the videos. A few videos had caption-language or length issues (for example V167 is a very long course and its note is based on parts of it). Spot checks of 12 key numbers against transcripts all matched.
