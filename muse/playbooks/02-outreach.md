# Playbook 02: Outreach drafts and the approval gate

## Drafting
1. Take today's `status=new` rows (up to today's `send_ramp` total) and any follow-ups that are due (day 3 and day 7 after `emailed`, max 2 follow-ups).
2. Use `templates/emails.md`. Fill in the **observation** from prospecting, which is what makes each email specific.
3. Keep the first email to 50–90 words. One ask: "Want me to send 10 free leads for [their niche] in [their city]?"
4. **Run playbook 07 (humanizer) on every draft**, then the required-lines check: business name, physical address, opt-out line.
5. Re-check `suppression_list` right before you queue a draft.

## Approval at higher volume (bulk approval)
Reading every email stops working past about 40 a day. So the owner approves the **template and targeting once**, and each day's batch with a sample:
1. First day, and whenever a template or the niche changes: send the owner the full template, 5 filled examples and the ZeroGPT scores. Wait for yes.
2. Every day: draft the whole batch (humanized, footer checked), then message the owner the counts and **10 randomly chosen full emails**
   (not the best 10, use a random pick and say how you picked). The owner replies `go`, `stop`, or the numbers to cut.
3. Send the rest only after `go`. If the owner finds a problem in any sample, stop the whole batch, fix the pattern, and show the fixed samples again.
No `go` by 4pm recipient time means nothing is sent that day.

## Approval message (WhatsApp to owner)
```
Outreach batch {date}: {n} emails ({first} first-touch, {fu} follow-ups)
1. Bright Pixel Co (Tulsa) - "Quick idea for Bright Pixel's next clients"
   <full email text>
   ZeroGPT: 6%
2. ...
Reply: "all", "none", or "all except 3, 7"
```
Don't send anything until the owner replies. If there's no reply by 11am, carry the batch over to tomorrow without sending.

## Sending
Send only approved emails, one at a time, at least 2 minutes apart **per inbox**, 8am–4pm in the recipient's timezone, rotating across inboxes so no inbox goes over its per-inbox cap.
Log each one: `status=emailed`, `emailed_on`, `touch=1|2|3`.
