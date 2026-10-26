# Playbook 09: Muse builds the business setup

You do the setup work. The owner answers questions, approves each purchase, and does only the steps that need their identity.
Send the owner **one WhatsApp message per step**, wait for the answer, then act. Never batch purchases into one approval.
Keep a checklist in `STATE.setup` and update it after each step. Post a one-line progress FYI on the Claude channel when a step finishes (no card, account or ID details).

## Questions to ask the owner first (one message, numbered)
1. Which city and state should the business show for timezone and address purposes?
2. Mailing address: use home address, a USPS PO box (needs an in-person visit with ID), or a virtual mailbox (needs notarized USPS Form 1583)? Recommend the PO box or home address, because a mailbox service needs paperwork you can't do for them.
3. Which virtual card should you use? Tell the owner to make a **virtual card with a $100 limit** at their bank or a card provider, and give you the **last four digits only** for the record. You enter the full number only on checkout pages, never anywhere else.
4. Which email address should the registrar and Workspace accounts be created under for now? (Their personal address is fine at first.)
5. The WhatsApp number to use for approvals.

## Step order (each purchase needs a yes first, per SOUL)
| # | Step | You do | Owner does |
|---|---|---|---|
| 1 | **Domain.** Check availability of 3 names like `leaddrop.co`, `getleaddrop.com`, `leaddrophq.com` and pick the cheapest of the plain `.com` / `.co` / `.net` with no add-ons. Decline add-ons, privacy upsells that cost extra, and auto-renew extras. | Search, ask to buy at the exact price, pay with the virtual card | Approve with `yes` |
| 2 | **Google Workspace** (Business Starter, one user) on the new domain, inbox `hello@`. | Sign up, ask before paying, add the domain, verify it | Enter any 2-step-verification code or ID check Google asks for |
| 3 | **DNS: SPF, DKIM, DMARC** in the registrar's DNS and the Workspace admin. Start DMARC at `p=none`, then move to `quarantine` after 2 weeks of clean reports. | Add the records, then confirm with a test email to a free check site and report the result | Nothing |
| 4 | **Stripe** account and the $400/month Payment Link using `muse/templates/stripe-and-inbox.md`. | Fill in everything you can up to the identity page | **The owner** enters their SSN, ID, bank account and tax details. Never do this yourself |
| 5 | **Pipeline sheet and Drive folders.** Create the 4 tabs from `muse/templates/pipeline-tracker.md` (or import `build/Pipeline.xlsx` if you can open it), and the Drive folders. | Create them and put the URLs in memory | Nothing |
| 6 | **Website.** Deploy `site/index.html` (with `{{...}}` filled from memory) on a free Netlify site, then connect the new domain. | Deploy, add DNS, report the URL | Approve before it goes live |
| 7 | **Email signature, footer, suppression list** set up per templates. | Do it | Nothing |
| 8 | **Test sends** from the new inbox to the owner and to a free spam-checker address, then report the placement. Do not send to any prospect until the owner says the warm-up can start. | Send 5 | Reply `start warm-up` |
| 9 | **Warm-up:** follow `send_ramp` days 1–7 (20 a day total) to prospects, using bulk approval. | Prospect, draft, ask for `go` | `go` each day |

## Rules while doing setup
- **Ask, don't guess.** If a form asks for something you don't know, ask the owner. Don't invent a business address, EIN, phone number or ID.
- **Be honest on every form.** The business is a sole proprietorship run by the owner. Don't claim a company, employees or revenue that don't exist.
- **Save nothing sensitive.** Record accounts as "created, owner has the login" in `STATE.setup`. No passwords, card numbers or recovery codes in memory, files or comments.
- **If a site blocks you** (CAPTCHA, ID check, phone verification), stop and tell the owner exactly what's needed.
- **More inboxes later:** when `send_ramp` calls for another inbox, repeat steps 1–3 for a new domain, and ask for approval on each purchase again.
