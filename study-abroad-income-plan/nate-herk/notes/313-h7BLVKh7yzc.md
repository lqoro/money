## 313. How to Build an Outlook Inbox Manager in n8n (Step-by-Step, No Code)
- **Link:** https://www.youtube.com/watch?v=h7BLVKh7yzc | **Length:** 32 min | **AI-relevant:** yes
- **Teaches:**
  - Trigger on Outlook "message received", polling every minute, with Raw output so the full body comes through.
  - Clean the HTML body with an LLM step, then route with a Text Classifier using category descriptions and example phrases.
  - Each branch moves the email into an Outlook folder by message ID from the trigger, then acts: a Telegram alert for high priority, an AI-drafted reply for billing, and a fixed-subject decline for promotions.
  - Deleting an upstream node breaks later references, so remap them first.
  - Outlook replies are not threaded like Gmail. The draft goes out as a new email to the sender.
- **Tools / prices / numbers:** n8n; Outlook; OpenAI GPT-4o mini (about $5 loaded); Gemini 2.0 Flash for classification, which Nate calls free; Telegram bot.
- **Skills shown:** email automation, text classification, routing logic, agent drafting, Telegram alerts.
- **Money angle:** none stated.
- **Duet-relevant:** yes, an always-on inbox agent that moves, drafts, and sends email for you and pings you on Telegram.
- **Promo:** Free School Community (YouTube resources templates); paid community (step-by-step builds, classroom, five live calls per week).

