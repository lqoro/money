# Working with Muse through Claude

Claude can't connect to Muse directly (there's no Muse connector). So you're the bridge:
paste each message below into Muse, then paste Muse's reply back into your Claude session.
Claude checks the reply against the playbooks and tells you what to send next, or what to correct.

Do these after SETUP steps 1–5 (inbox, Stripe, Drive, MEMORY filled in, files uploaded).

---

### Message 1: make Muse check its own setup
```
Read your soul file, your memory file, and every uploaded playbook and template.
Then reply with exactly this checklist, with a yes or no on each line and a one-line note:
1. I can read and write the Pipeline sheet (give the tab names you see)
2. I can read the sending inbox and draft (not send) an email
3. I can message the owner on WhatsApp
4. I can use my browser to open a public website
5. I can create scheduled tasks
6. Any FILL_ME left in memory (list them)
7. The three hard rules I will never break (in your own words)
Don't contact anyone and don't create any tasks yet.
```
**Paste Muse's reply back to Claude.** Any "no" means a connector or a permission is missing, and Claude will tell you which.

### Message 2: humanizer practice (SETUP step 6)
Use the practice draft and instructions in SETUP.md step 6. **Paste the before, after and score back to Claude.**

### Message 3: one dry prospecting run
```
Run playbook 01 for marketing agencies in one US city of your choice, but stop at 5 prospects.
Add them to the Pipeline sheet with status "new". Then show me the 5 rows here.
Don't email anyone.
```
**Paste the 5 rows back to Claude.** Claude checks that each one is real, small, publicly reachable, and has a
specific observation with a source URL.

### Message 4: one dry outreach draft
```
Run playbook 02 and playbook 07 on those 5 prospects, but don't send anything.
Show me the 5 humanized drafts with their ZeroGPT scores, in the approval format from playbook 02.
```
**Paste the drafts back to Claude.** Claude reviews tone, facts and the required footer before you approve any real send.

### Message 5: turn it on
Only after Messages 3 and 4 look right:
```
Create the 7 scheduled tasks exactly as written in ROUTINES.md, in my timezone from memory.
Then list them back to me with their schedules.
```
**Paste the list back to Claude** so it can confirm the schedules match ROUTINES.md.

---

## Daily (optional): let Claude review the batch
Before replying `all` to Muse's morning outreach batch, you can paste the batch here and Claude will flag
anything risky: invented facts, a missing opt-out line, a name on the suppression list, or a weak observation.
