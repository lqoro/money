# Playbook 07: Humanizer pass (run on everything a human will read)

This is the Muse version of the owner's **humanizer** skill. The full skill is in
`skills/humanizer/SKILL.md`. Read it once at setup and again whenever this playbook isn't enough.
The owner's voice profile is `skills/humanizer/references/voice-owner.md`.

**When to run it:** on every cold email, follow-up, reply draft, sample/delivery email, the "why now" and opener
columns in lead sheets, and anything else a prospect or client will read. Run it **before** the draft goes to the
owner for approval, so the owner approves the final text. You don't need it for STATE, HANDOFF or internal notes.

## Step 1. Draft, then mark the patterns
Check the draft against the patterns in SKILL.md. These come up most in sales email:

| § | Pattern | Fix in a cold email |
|---|---|---|
| 4, 7 | Sales words: boasts, vibrant, renowned, stunning, crucial, key, valuable, enhance, leverage, delve, showcase, landscape | Say the plain thing: "you have 14 reviews", "your site isn't mobile friendly" |
| 9 | "It's not just X, it's Y" / clipped endings like "no strings" | One clear clause |
| 10 | Groups of three ("more leads, more calls, more revenue") | One concrete outcome |
| 14 | Em/en dashes | **Zero dashes, ever.** Use a period or comma. The owner's voice profile also bans them |
| 20, 22 | "I hope this finds you well", "Great question!", "Let me know if..." as filler | Open on their business; end on one specific ask |
| 23 | Filler ("in order to", "I wanted to reach out") | Cut it |
| 25 | Upbeat send-off ("Looking forward to helping you grow!") | End on the last useful fact or the ask |
| 33 | Fake-candid hooks ("Honestly?", "Here's the thing") | State the point |
| 36 | Sentences that could be lifted out and still stand alone | Make sentences lean on the one before (that, this, it, so) |
| 38 | Stock pairings ("take your business to the next level") | Use a pairing only their business supplies ("the Elm St location you opened in March") |

## Step 2. Match the owner's voice (adapted for business email)
The voice profile comes from a college essay. These habits carry over to email. The essay-only ones (MLA format, quotations, reading reactions) don't:
- No dashes, no semicolons, and no "however / additionally / moreover / furthermore / thus".
- Contractions about 3 per 100 words (it's, you're, I'd, that's, doesn't).
- Plain words and phrasal verbs: "sent over", "pulled together", "looked up", "ends up", not "compiled", "curated", "leverage".
- Light hedges are fine, about one per 100 words: just, pretty, actually, basically. Never two in one sentence.
- Relaxed commas after short openers ("When I looked at your site the contact form was broken").
- No rhetorical questions in the body. The one question allowed is the ask at the end.
- Claims stay modest and specific. Never "powerful", "game changing", "transform".

## Step 3. Three questions before you finish
1. What still sounds AI-generated?
2. Could any sentence be lifted out and still stand alone? Tie it to its neighbor.
3. **Did I add or lose any fact?** Every fact must come from the lead's source URL, MEMORY, or the email thread. No invented numbers, results, clients, or testimonials (this is also a hard rule in SOUL).

## Step 4. Detector check (ZeroGPT, using Muse's own browser)
Run this on **templates** and on any email over 60 words that's a reply or a sample/delivery email.
For high-volume first-touch emails, check the template plus 1 in 5 drafts so a day's batch doesn't take hours.

1. **Strip personal data first.** ZeroGPT is a third-party site. Swap in placeholders of the same shape:
   prospect and owner names → "Sam Carter", emails → `name@example.com`, phones → `(000) 000-0000`,
   street addresses → "100 Main St", and business names → "Acme Services". Put the real values back afterward.
   **Never paste client lead sheets or whole email threads**, only the draft you're checking.
2. Open `https://www.zerogpt.com/`, paste into the textarea, press **Detect Text**, and wait about 10 seconds.
   Read the score from the result card next to "AI GPT", **not** from the marketing percentages on the page.
   Check that the result card shows the text you just pasted (the old result stays up while a new scan runs).
3. **Target: under 10%.** If it's higher, rewrite **only the highlighted sentences**, keep the professional register
   (no slang), and rescan the whole text. Don't split flagged sentences in half, because both halves usually flag.
4. **Stop** when it's under 10%, after 3 rounds (keep the lowest-scoring version that kept every fact), when only the
   signature/address/opt-out lines are flagged (that's the floor and it's fine), or when the browser isn't working.
   If the browser doesn't work, say "scan didn't run". **Never report a score you didn't read this run.**
5. Note on emails under ~60 words: a 0% score there is weak evidence.

## Step 5. What to send the owner
In the approval message, put the final text plus one line per email: `ZeroGPT: 4%`, or `ZeroGPT: skipped (spot check)`,
or `ZeroGPT: scan didn't run`. Add any lessons (which phrasings kept flagging) to `STATE.lessons`.

## Keep the required lines as they are
The opt-out line, physical address and business name are required by law (SOUL hard rules). Never remove or blur them
to lower a score. The same goes for the price, the guarantee wording and the payment link.
