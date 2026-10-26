# Scheduled tasks

Create each of these in Muse. Times are in the owner's timezone. Every prompt starts the same way,
because each run starts with no memory of the last one.

> Shared preamble (already included in each prompt below):
> "Read SOUL, MEMORY (STATE + HANDOFF), and the named playbook first. Follow the hard rules. Update STATE and the Pipeline sheet before you finish."

---

### 1. Prospecting: daily, 6:00am
```
Read SOUL, MEMORY (STATE + HANDOFF), and playbooks/01-prospecting.md first. Follow the hard rules.
Find new prospects for STATE.current_niche in STATE.current_cities (pick a new city if the current ones are exhausted).
Target: (daily_send_cap + 5) new qualified prospects, each checked against suppression_list and the Pipeline sheet for duplicates.
Add them to the Pipeline sheet with status "new". Update STATE and the Pipeline sheet before you finish.
```

### 2. Outreach drafts + approval: daily, 7:30am
```
Read SOUL, MEMORY (STATE + HANDOFF), playbooks/02-outreach.md, playbooks/07-humanizer.md and templates/emails.md first. Follow the hard rules.
Draft first-touch emails for today's "new" prospects (up to daily_send_cap), plus any follow-ups that are due.
Run the humanizer pass (playbook 07) on every draft, including the ZeroGPT check on the template and 1 in 5 drafts.
Send the batch to the owner on WhatsApp for approval, in the numbered format from the playbook. Do NOT send any email yet.
When the owner replies, send only the approved emails, spaced at least 2 minutes apart, between 8am and 11am in the recipient's timezone.
Mark them "emailed" with the date. Update STATE and the Pipeline sheet before you finish.
```

### 3. Inbox triage: event-driven (new email in sending_inbox), or every 2 hours 8am–8pm
```
Read SOUL, MEMORY (STATE + HANDOFF), playbooks/03-replies.md and playbooks/07-humanizer.md first. Follow the hard rules.
Classify each new email: interested / question / not now / opt-out / bounce / client / other.
Opt-outs and bounces go on suppression_list immediately. For interested prospects and questions, draft a reply, run the humanizer pass (playbook 07) on it, and send it to the owner for approval.
If a prospect says yes to a sample, add "make sample" to STATE.todo. Update STATE and the Pipeline sheet before you finish.
```

### 4. Free samples: daily, 1:00pm
```
Read SOUL, MEMORY (STATE + HANDOFF), playbooks/04-sample.md, playbooks/07-humanizer.md and templates/lead-sheet.md first. Follow the hard rules.
For every "make sample" in STATE.todo: build a 10-lead sample sheet in Drive/samples/, quality-check it, humanize the openers and the delivery email (playbook 07), then send the
owner the delivery email plus the sheet link for approval. After approval, send it and set the prospect to "sample_sent".
Schedule a follow-up note in STATE for 2 days later (ask how the leads look, then offer the $400/mo plan with payment_link).
Update STATE and the Pipeline sheet before you finish.
```

### 5. Client delivery: weekly, Sunday 2:00pm (delivers before Monday 9am)
```
Read SOUL, MEMORY (STATE + HANDOFF), playbooks/05-delivery.md, playbooks/07-humanizer.md and templates/lead-sheet.md first. Follow the hard rules.
For each active client in STATE.clients: build this week's 25-lead tab in their sheet, with no repeats from earlier weeks,
then run the quality check and humanize the openers and delivery notes (playbook 07). Send the owner one WhatsApp summary for approval of all delivery emails, then send them.
Log the delivery dates. Update STATE and the Pipeline sheet before you finish.
```

### 6. Weekly review: Friday, 4:00pm
```
Read SOUL, MEMORY (STATE + HANDOFF), and playbooks/06-weekly-review.md first. Follow the hard rules.
Compute the funnel and MRR for the week, compare it to last week, and write 3 lessons into STATE.lessons.
Recommend at most 2 changes for next week (niche, city, subject line, send cap). Send the owner a WhatsApp report
in under 150 words. Apply a change only once the owner says yes. Update STATE before you finish.
```

### 7. Night handoff: daily, 11:00pm
```
Read SOUL and MEMORY. Look at today's activity log, Gmail sent/received, and the Pipeline sheet.
Overwrite the HANDOFF block in memory with: done_today, open_threads, next_up, and blockers_for_owner.
Fix any STATE counts that don't match the Pipeline sheet. Don't contact anyone. Keep the handoff under 120 words.
```
