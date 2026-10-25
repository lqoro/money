## 309. How to Actually Scrape Twitter/X Data with n8n
- **Link:** https://www.youtube.com/watch?v=lEo7IAgj0UY | **Length:** 20 min | **AI-relevant:** no
- **Teaches:**
  - Build a loop: set a starting count, search tweets, extract fields, append rows to Google Sheets, then return to the search until the count hits a limit (three runs gave 58 tweets in the demo).
  - Use the response's next-cursor value as the pagination input for the next request, and reference the most recent count and cursor so each loop updates them.
  - Import the curl from the API docs into an HTTP Request node, and store the key as a header credential.
  - Use a Code node to flatten each tweet into ID, URL, text, likes, views, and date, then map those to sheet columns.
  - Use an If node to end the loop, with the initial count hardcoded in a Set node.
- **Tools / prices / numbers:** a pay-as-you-go Twitter/X data API at about $0.15 per 1,000 tweets (Nate's figure). His referral link gives $6 to start, versus about $1 normally. n8n; Google Sheets; Claude 3.7 used to write code nodes.
- **Skills shown:** pagination, loops, Code nodes, Google Sheets, API authentication.
- **Money angle:** Nate suggests market analysis, competitor analysis, and lead lists from scraped data. He gives no price for selling any of it.
- **Duet-relevant:** no
- **Promo:** referral link for the Twitter API ($6 start credit); Free School Community (workflow and Sheet template); paid community.

