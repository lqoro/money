# Playbook 01: Prospecting (finding businesses to sell LeadDrop to)

Our prospects are the **sellers** in `MEMORY.ICP`, the businesses that would buy lead lists from us.
Work one niche (`STATE.current_niche`) in 2–3 cities at a time until it's exhausted or the weekly review says to switch.

## Steps
1. Pick the city: continue `STATE.current_cities`. If you found fewer than 10 new prospects there yesterday, add the next city
   (US metros of 100k–1M people, working outward from the owner's timezone).
2. Search publicly: Google Maps ("marketing agency in Tulsa"), Clutch.co, the local chamber of commerce directory, and industry association member lists.
3. For each candidate, open **their own website** and confirm:
   - It's a real, active business (site loads, updated in the last ~2 years, has a services page)
   - It's small (2–15 people: a team page, an "about us", or a LinkedIn company size seen on *public* search results only)
   - It sells to other businesses or to local businesses, so it needs leads
   - It has a public contact route: a role email on the site (hello@, info@, a named person's email *if they publish it*) or a contact form
4. Check for duplicates: skip it if the domain is already in the Pipeline sheet or on `suppression_list`.
5. Write down **one specific observation** you'll use in the email. Examples: "case studies page only shows 2 clients from 2023",
   "they just posted a job for a sales rep", "their blog says they're focusing on dentists now". It must come from a page you visited.

## Pipeline row
`date_added | business | website | city | niche | contact_name | contact_role | contact_route | observation | source_url | status=new`

## Quality bar
If you aren't sure the business is real, small, and reachable, skip it. Target: `daily_send_cap + 5` per day.
Never guess email addresses (no "firstname@domain" guessing), and never log in to any site.
