# Pipeline sheet (create as a Google Sheet called "Pipeline")

**Tab `prospects`**, one row per business we might sell to:
`date_added | business | website | city | niche | contact_name | contact_role | contact_route | observation | source_url | status | emailed_on | touch | last_reply_on | notes`

`status` values: `new → emailed → replied → sample_sent → won | lost | nurture`

**Tab `clients`:**
`client | niche | city | icp_notes | start_date | sheet_url | price | status | last_delivered | wins_reported`

**Tab `weekly`**, one row per week (written by the weekly review):
`week_of | prospects_added | emails_sent | replies | samples | won | lost | opt_outs | mrr | dollars_per_hour | median_zerogpt`

**Tab `suppression`**, mirroring `MEMORY.suppression_list`:
`email_or_domain | reason | date`
