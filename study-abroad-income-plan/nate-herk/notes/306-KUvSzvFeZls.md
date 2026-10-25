## 306. How I Built JARVIS with No Code (Tutorial w/ Lovable, ElevenLabs, n8n)
- **Link:** https://www.youtube.com/watch?v=KUvSzvFeZls | **Length:** 34 min | **AI-relevant:** yes
- **Teaches:**
  - Architecture: an ElevenLabs voice agent sends each spoken request to one n8n webhook tool with a single "query" field.
  - A main n8n agent (GPT-4o) picks one of four sub-agent workflows (email, calendar, contacts in Airtable, web content), and each sub-agent calls its own Gmail, Calendar, or Airtable tools.
  - Put a "Respond to Webhook" node at the end so the voice agent waits for the result, and switch to the production URL when the workflow is active.
  - Build the web front end in Lovable through chat, then paste in the ElevenLabs embed code.
  - Write voice-agent prompts that say exactly when to call the tool and what to send.
- **Tools / prices / numbers:** Lovable; ElevenLabs (Starter plan, about $5 a month per Nate); OpenAI GPT-4o; Tavily search; Airtable; Gmail; Google Calendar; n8n. Nate says he earns a small kickback from the tool links in his description. The build took him a little over 20 minutes in Lovable.
- **Skills shown:** voice agent design, webhook integration, multi-agent routing, prompt writing, no-code front-end building.
- **Money angle:** none stated. He frames it as a personal assistant build and mentions a paid community, without pricing a client offer.
- **Duet-relevant:** yes, a voice-driven personal assistant that checks calendar, sends and labels email, and searches the web for you.
- **Promo:** Free School Community (agent templates and system prompts); paid community (step-by-step builds); tool links with kickback; 5 live calls per week.

