# Playbook 04: The free 10-lead sample (this is what closes the deal)

1. Confirm what the prospect sells and who their best customer is (from the thread and their website), and the city they serve.
2. Find **10 prospects for them**, the same way as playbook 01 but aimed at *their* customer. Example: an agency that does
   dentist websites gets 10 local dental offices with weak websites.
3. Fill the sheet using `templates/lead-sheet.md`. Each row needs a source URL you visited and a "why now" trigger.
   Write each opener for *the client* to send, then run **playbook 07** on the opener column. The goal: openers that don't read like a bot wrote them.
4. Quality check (all must pass): no duplicates, every URL loads, every contact route is public, every "why now" is a fact from the source, and no personal guessed emails.
5. Save it to `Drive/samples/<business>-sample.gsheet`, shared as "anyone with the link can view".
6. Draft the delivery email (`templates/emails.md` → Sample delivery), humanize it, and send it to the owner for approval with the link.
7. After approval, send it. Set `status=sample_sent` and add a todo for 2 days out: "check in + offer".
8. **Day 2 check-in:** ask which leads looked best and offer the plan with `payment_link` (template: Offer). Humanize it and get approval.
9. When Stripe sends a payment email to the inbox, add the client to `STATE.clients`, set `mrr += 400`, and set `status=won`.
   Send the owner: "New client: <name>. MRR now $X (= $Y/hr)."
