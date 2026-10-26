# Playbook 02: Outreach drafts and the approval gate

## Drafting
1. Take today's `status=new` rows (up to `daily_send_cap`) and any follow-ups that are due (day 3 and day 7 after `emailed`, max 2 follow-ups).
2. Use `templates/emails.md`. Fill in the **observation** from prospecting, which is what makes each email specific.
3. Keep the first email to 50–90 words. One ask: "Want me to send 10 free leads for [their niche] in [their city]?"
4. **Run playbook 07 (humanizer) on every draft**, then the required-lines check: business name, physical address, opt-out line.
5. Re-check `suppression_list` right before you queue a draft.

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
Send only the approved emails, one at a time, at least 2 minutes apart, 8–11am in the recipient's timezone.
Log each one: `status=emailed`, `emailed_on`, `touch=1|2|3`.
