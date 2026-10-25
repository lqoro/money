## 311. Store All Data Types with Agentic RAG in n8n
- **Link:** https://www.youtube.com/watch?v=BhGaGFH0jR4 | **Length:** 19 min | **AI-relevant:** yes
- **Teaches:**
  - Traditional RAG chunks documents, embeds them, and returns the nearest chunks. It misses whole-document context and gets numeric questions wrong.
  - Agentic RAG lets the agent choose a source: vector search for text, SQL for tabular data, or full file retrieval for a whole document.
  - Use a template that sets up Supabase (pgvector) tables for documents, spreadsheet rows, and metadata.
  - If a SQL query fails, the agent falls back to listing documents and fetching file contents.
  - Keep the vector limit small, since raising it only returns more random chunks.
- **Tools / prices / numbers:** Supabase with pgvector; OpenAI GPT-4o mini; n8n. In the demo, SQL returned week 4 as the highest total sales (19,423), matching the sheet. The sales table had 30 rows, and a missing value in week 19 caused failed queries.
- **Skills shown:** RAG architecture, SQL, vector databases, agent tool routing, Supabase setup.
- **Money angle:** none stated.
- **Duet-relevant:** no
- **Promo:** Free School Community (template download); paid community (classroom, deep dives, live calls). Nate credits the template's creator and links to that creator's video.

