## 308. How MCPs Make Agents Smarter (for non-techies)
- **Link:** https://www.youtube.com/watch?v=m0YrxLnFPzQ | **Length:** 16 min | **AI-relevant:** yes
- **Teaches:**
  - An LLM becomes an agent when it can call tools, but hardcoded tools need one node per operation, which does not scale.
  - An MCP server sits between the agent and a service and tells the agent what tools, schemas, and resources exist.
  - Demo: an agent with the prompt "you are a helpful assistant" and no other instructions found and used the Airbnb and Firecrawl MCP tools on its own.
  - Firecrawl's extract call failed twice with HTTP 400 because the parameters were wrong, then worked on the third try. Fix the parameter schema and prompt.
  - Security: an MCP server exposing your own data can be queried by anyone who gets in, so guard it.
- **Tools / prices / numbers:** n8n; Airbnb MCP; Firecrawl MCP (about nine actions per Nate); Airtable (seven hand-built tools versus 13 via MCP); Excalidraw for the diagram. No prices.
- **Skills shown:** MCP concepts, agent tool design, debugging API parameters.
- **Money angle:** none stated.
- **Duet-relevant:** no
- **Promo:** paid community mentioned for discussion; no sponsor or affiliate link.

