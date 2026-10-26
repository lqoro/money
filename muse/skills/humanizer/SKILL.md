---
name: humanizer
description: "Rewrite text that sounds AI-generated while keeping the writer's facts,\nmeaning, and voice. Use when editing or reviewing prose for inflated claims,\nsales language, vague sources, repetitive structure, stock AI words, passive\nvoice, filler, or chatbot artifacts. Based on Wikipedia's \"Signs of AI writing.\"\n"
license: MIT
metadata:
  version: "2.13.0"
---

# Humanizer: remove AI writing patterns

Rewrite text that sounds AI-generated so it reads like the writer, not a chatbot. Keep the writer's facts, meaning, and voice.

The patterns below come from Wikipedia's ["Signs of AI writing"](https://en.wikipedia.org/wiki/Wikipedia:Signs_of_AI_writing), maintained by WikiProject AI Cleanup.

## What to do

When given text to humanize:

1. **Find AI patterns.** Check the text against the patterns below.
2. **Keep every claim.** You may shorten dull parts, expand useful parts, and merge or split paragraphs. Keep the information even when you change the structure.
3. **Do not invent facts.** Do not add a fact, name, number, date, quote, or citation unless it comes from the source or the user. If a sentence needs a missing detail, ask for it or use a simpler sentence. You may add an opinion or reaction when the writer's voice calls for one, but you may not add a factual claim. Fiction is exempt because invented details are part of the task.
4. **Match the voice.** Use the right tone for the text, such as formal, casual, or technical. Add personality only when the text and the writer call for it.

The input type controls what you return. See [How to return the result](#how-to-return-the-result). Use the same rewrite process in every mode.

## Match the writer's voice

If the user provides a writing sample (their own previous writing), analyze it before rewriting:

1. Read the sample first. Note its sentence length, word choice, paragraph openings, punctuation, repeated phrases, and transitions.
2. Go deeper than tone. Measure or estimate these, because they are what a reader and a detector notice:
   - **Sentence length spread**, not just the average. A writer who mixes 3-word and 40-word sentences should not be turned into even 15-word sentences.
   - **Punctuation inventory.** Rates of contractions, dashes, semicolons, colons, and parentheses, and what each one is used for. A writer who uses colons only before quotations should not get a colon reveal.
   - **Verb habits.** Phrasal verbs ("talk him into") versus Latinate verbs ("persuade"), *get*-passives versus *be*-passives.
   - **Hedges and intensifiers** the writer actually uses (*pretty*, *just*, *actually*, *kind of*), with their rate.
   - **Where first person appears**, and what it does: a claim, a reaction, or a report of the reading process.
   - **How sentences connect**: backward-pointing openers (*That*, *So*, *Then*, *But*), how quotes are introduced and followed up, and how long sentences are built (chained with *and*/*so* or nested).
   - **Comma habits**, including commas the writer leaves out after short opening phrases.
   - **What the writer never does.** Absences are as identifying as habits.
3. Match those habits. Do not replace casual words with formal ones or remove deliberate quirks.
4. If there is no sample, use the guidance below.

A writing sample takes priority over these style rules. If the sample uses em dashes, keep them at about the same rate. Do not apply §14 as a ban. The same goes for every other section: if the sample uses a §7 word, a qualifier from §24, or a repeated frame from §37, keep it at the sample's rate.

### Saved voice profiles

Some writers already have a profile built from a confirmed sample of their own writing. Load the profile before rewriting when the user is that writer, or asks for "my voice," or for "my essay" or schoolwork:

- **The owner**: `references/voice-owner.md` (kept out of this public repo; upload it to Muse directly, see SETUP step 6). Built from a confirmed sample of the owner's writing. In brief: no dashes, semicolons, rhetorical questions or stock transitions; about 3 contractions per 100 words; light hedges; phrasal verbs and *get*-passives; relaxed commas after short openers.

A profile is a sample that has already been analyzed, so it outranks the style rules in this skill the same way a sample does. A newer sample from the same writer outranks the profile.

## Add personality only when it fits

Removing AI patterns is only half the job. The result should still sound like a person.

Use personality in blog posts, essays, opinions, and personal writing when it fits the writer. Keep reference, technical, legal, and factual text neutral. Do not add opinions or first-person language where they do not belong.

When personality fits, keep the writer's opinions, uncertainty, mixed feelings, humor, asides, and uneven rhythm. Never invent facts to make the text feel personal.

## Content patterns

### 1. Inflated claims about importance and legacy

**Words to watch:** stands/serves as, is a testament/reminder, a vital/significant/crucial/pivotal/key role/moment, underscores/highlights its importance/significance, reflects broader, symbolizing its ongoing/enduring/lasting, contributing to the, setting the stage for, marking/shaping the, represents/marks a shift, key turning point, evolving landscape, focal point, indelible mark, deeply rooted
**Problem:** AI writing often claims that ordinary details mark a major change, prove a legacy, or reflect a broad trend.
**Before:**
> The Statistical Institute of Catalonia was officially established in 1989, marking a pivotal moment in the evolution of regional statistics in Spain. This initiative was part of a broader movement across Spain to decentralize administrative functions and enhance regional governance.
**After:**
> The Statistical Institute of Catalonia was established in 1989, part of a wider decentralization of administrative functions in Spain.

### 2. Name-dropping to prove importance

**Words to watch:** independent coverage, local/regional/national media outlets, written by a leading expert, active social media presence
**Problem:** AI writing often lists well-known publications or follower counts to prove that a person matters. The list usually gives no useful context.
**Before:**
> Her views have been cited in The New York Times, BBC, Financial Times, and The Hindu. She maintains an active social media presence with over 500,000 followers.
**After:**
> Her views have been cited in The New York Times and the BBC.

If the source explains what the person said and where, keep that useful citation. Do not invent context for a shorter version.

### 3. Shallow analysis with -ing phrases

**Words to watch:** highlighting/underscoring/emphasizing..., ensuring..., reflecting/symbolizing..., contributing to..., cultivating/fostering..., encompassing..., showcasing...
**Problem:** AI writing often adds an -ing phrase to make a simple fact sound deeper than it is.
**Before:**
> The temple's color palette of blue, green, and gold resonates with the region's natural beauty, symbolizing Texas bluebonnets, the Gulf of Mexico, and the diverse Texan landscapes, reflecting the community's deep connection to the land.
**After:**
> The temple is painted blue, green, and gold, colors meant to evoke Texas bluebonnets and the Gulf of Mexico.

### 4. Sales language

**Words to watch:** boasts a, vibrant, rich (figurative), profound, enhancing its, showcasing, exemplifies, commitment to, natural beauty, nestled, in the heart of, groundbreaking (figurative), renowned, breathtaking, must-visit, stunning
**Problem:** AI writing often sounds like an advertisement, especially when it describes places, culture, products, or organizations.
**Before:**
> Nestled within the breathtaking region of Gonder in Ethiopia, Alamata Raya Kobo stands as a vibrant town with a rich cultural heritage and stunning natural beauty.
**After:**
> Alamata Raya Kobo is a town in the Gonder region of Ethiopia.

### 5. Vague sources

**Words to watch:** Industry reports, Observers have cited, Experts argue, Some critics argue, several sources/publications (when few cited)
**Problem:** AI writing often assigns a claim to unnamed experts, critics, reports, or observers.
**Before:**
> Due to its unique characteristics, the Haolai River is of interest to researchers and conservationists. Experts believe it plays a crucial role in the regional ecosystem.
**After:**
> Researchers and conservationists study the Haolai River for its unusual characteristics.

Name a real source when the source text provides one. Otherwise, remove the unsupported claim. Never invent a source.

### 6. Formulaic challenges and outlook sections

**Words to watch:** Despite its... faces several challenges..., Despite these challenges, Challenges and Legacy, Future Outlook
**Problem:** AI articles often add a stock section about challenges, future prospects, or continued growth. These sections usually repeat vague claims instead of adding facts.
**Before:**
> Despite its industrial prosperity, Korattur faces challenges typical of urban areas, including traffic congestion and water scarcity. Despite these challenges, with its strategic location and ongoing initiatives, Korattur continues to thrive as an integral part of Chennai's growth.
**After:**
> Korattur has recurring traffic congestion and water shortages.

Add details such as dates or public actions only when they come from the source or the user.

## Language and grammar patterns

### 7. Overused AI words

**High-frequency AI words:** Actually, additionally, align with, crucial, delve, emphasizing, enduring, enhance, fostering, garner, gate/gated/gating (figurative; preserve established technical usage), highlight (verb), interplay, intricate/intricacies, key (adjective), landscape (abstract noun), pivotal, quietly, showcase, tapestry (abstract noun), testament, underscore (verb), valuable, vibrant
**Problem:** AI writing uses these words much more often than most people do, especially in groups.
**Before:**
> Additionally, a distinctive feature of Somali cuisine is the incorporation of camel meat. An enduring testament to Italian colonial influence is the widespread adoption of pasta in the local culinary landscape, showcasing how these dishes have integrated into the traditional diet.
**After:**
> Somali cuisine also includes camel meat, which is considered a delicacy. Pasta dishes, introduced during Italian colonization, remain common, especially in the south.

### 8. Avoiding is and are

**Words to watch:** serves as/stands as/marks/represents [a], boasts/features/offers [a]
**Problem:** AI writing often replaces simple verbs such as *is*, *are*, and *has* with longer phrases.
**Before:**
> Gallery 825 serves as LAAA's exhibition space for contemporary art. The gallery features four separate spaces and boasts over 3,000 square feet.
**After:**
> Gallery 825 is LAAA's exhibition space for contemporary art. The gallery has four rooms totaling 3,000 square feet.

### 9. Not X but Y and clipped negative endings
**Problem:** AI writing overuses forms such as "Not only...but..." and "It's not just X, it's Y."

It also adds clipped endings such as "no guessing" instead of writing a clear clause.
**Before:**
> It's not just about the beat riding under the vocals; it's part of the aggression and atmosphere. It's not merely a song, it's a statement.
**After:**
> The heavy beat adds to the aggressive tone.
**Before (tailing negation):**
> The options come from the selected item, no guessing.
**After:**
> The options come from the selected item without forcing the user to guess.

### 10. Forced groups of three
**Problem:** AI writing often forces ideas into groups of three to sound complete.
**Before:**
> The event features keynote sessions, panel discussions, and networking opportunities. Attendees can expect innovation, inspiration, and industry insights.
**After:**
> The event includes talks and panels. There's also time for informal networking between sessions.

### 11. Changing names and repeating sentence openings
**Problem:** AI writing handles repetition by rule instead of by ear. It may keep renaming the same person or thing. It may also start several sentences with the same subject, often *she* or *he*.

Use one clear name for the same subject. For repeated openings, merge sentences, change the subject when that helps, or begin with the action.
**Before (synonym cycling):**
> The protagonist faces many challenges. The main character must overcome obstacles. The central figure eventually triumphs. The hero returns home.
**After:**
> The protagonist faces many challenges but eventually triumphs and returns home.
**Before (repeated openings):**
> She noted the door. She noted the lock on it. She filed both away.
**After:**
> She noted the door and its lock, then filed both away.

Do not ban the repeated word. Fix the repeated sentence pattern. The remaining sentence may still start with "She."

### 12. False from X to Y ranges
**Problem:** AI writing often uses "from X to Y" when X and Y do not form a real range.
**Before:**
> Our journey through the universe has taken us from the singularity of the Big Bang to the grand cosmic web, from the birth and death of stars to the enigmatic dance of dark matter.
**After:**
> The book covers the Big Bang, star formation, and current theories about dark matter.

### 13. Passive voice and missing subjects
**Problem:** AI writing often hides who acts or drops the subject. Use active voice when it makes the actor and action clearer.
**Before:**
> No configuration file needed. The results are preserved automatically.
**After:**
> You do not need a configuration file. The system preserves the results automatically.

## Style patterns

### 14. Em and en dashes

**Rule:** The final rewrite must not contain em dashes (—) or en dashes (–), unless the writer's sample uses them. Replace a dash with a period, comma, colon, or parentheses, or rewrite the sentence. Also check for spaced dashes (` — `) and double hyphens (` -- `) used as dashes.
**Before:**
> The term is primarily promoted by Dutch institutions—not by the people themselves. You don't say "Netherlands, Europe" as an address—yet this mislabeling continues—even in official documents.
**After:**
> The term is primarily promoted by Dutch institutions, not by the people themselves. You don't say "Netherlands, Europe" as an address, yet this mislabeling continues in official documents.
**Before:**
> The new policy — announced without warning — affects thousands of workers. The changes -- long overdue according to critics -- will take effect immediately.
**After:**
> The new policy, announced without warning, affects thousands of workers. The changes, long overdue according to critics, will take effect immediately.

Before returning the rewrite, search for `—` and `–`. Remove each one unless the writer's sample uses that mark. In that case, match the sample's rate.

### 15. Too much bold text
**Problem:** AI chatbots often bold words and phrases without a clear reason.
**Before:**
> It blends **OKRs (Objectives and Key Results)**, **KPIs (Key Performance Indicators)**, and visual strategy tools such as the **Business Model Canvas (BMC)** and **Balanced Scorecard (BSC)**.
**After:**
> It blends OKRs, KPIs, and visual strategy tools like the Business Model Canvas and Balanced Scorecard.

### 16. Lists with bold mini-headings
**Problem:** AI writing often uses vertical lists in which every item starts with a bold label and a colon.
**Before:**
> - **User Experience:** The user experience has been significantly improved with a new interface.
> - **Performance:** Performance has been enhanced through optimized algorithms.
> - **Security:** Security has been strengthened with end-to-end encryption.
**After:**
> The update improves the interface, speeds up load times through optimized algorithms, and adds end-to-end encryption.

### 17. Title case in headings
**Problem:** AI chatbots often capitalize every main word in a heading.
**Before:**
> ## Strategic Negotiations And Global Partnerships
**After:**
> ## Strategic negotiations and global partnerships

### 18. Emojis
**Problem:** AI chatbots often add emojis to headings and list items as decoration.
**Before:**
> 🚀 **Launch Phase:** The product launches in Q3
> 💡 **Key Insight:** Users prefer simplicity
> ✅ **Next Steps:** Schedule follow-up meeting
**After:**
> The product launches in Q3. User research showed a preference for simplicity. Next step: schedule a follow-up meeting.

### 19. Curly quotation marks
**Problem:** ChatGPT often uses curly quotes (“...”) where the writer or target format uses straight quotes ("...").
**Before:**
> He said “the project is on track” but others disagreed.
**After:**
> He said "the project is on track" but others disagreed.

## Chatbot patterns

### 20. Chatbot text left in the answer

**Words to watch:** I hope this helps, Of course!, Certainly!, You're absolutely right!, Would you like..., Want me to...?, Want me to give examples?, Should I continue?, let me know, here is a...
**Problem:** A chatbot's greeting, offer, or closing sometimes remains in text that should stand on its own.
**Before:**
> Here is an overview of the French Revolution. I hope this helps! Let me know if you'd like me to expand on any section.
**After:**
> The French Revolution began in 1789 when financial crisis and food shortages led to widespread unrest.

### 21. Knowledge-limit disclaimers and guesses

**Words to watch:** as of [date], Up to my last training update, While specific details are limited/scarce..., based on available information, not publicly available, maintains a low profile, keeps personal details private, prefers to stay out of the spotlight, likely [grew up/studied/began], it is believed that
**Problem:** Older models may mention the date when their knowledge ends. A model may also explain that it could not find a source, then fill the gap with a plausible guess. State what the source does not show, or remove the sentence. Do not present a guess as a fact.
**Before (cutoff disclaimer):**
> While specific details about the company's founding are not extensively documented in readily available sources, it appears to have been established sometime in the 1990s.
**After:**
> The company's founding date is not documented in the available sources. (Or cut the sentence. State a date only if a source provides one.)
**Before (speculative gap-fill):**
> Information about her early life is not publicly available, suggesting she maintains a low profile and keeps personal details private. She likely grew up in a middle-class household, which shaped her later interest in education reform.
**After:**
> Her early life is not documented in the available sources. (Or omit the section.)

### 22. Overly agreeable tone
**Problem:** AI assistants often praise the user or agree before giving the answer.
**Before:**
> Great question! You're absolutely right that this is a complex topic. That's an excellent point about the economic factors.
**After:**
> The economic factors you mentioned are relevant here.

## Filler and hedging

### 23. Filler phrases

**Before → After:**
- "In order to achieve this goal" → "To achieve this"
- "Due to the fact that it was raining" → "Because it was raining"
- "At this point in time" → "Now"
- "In the event that you need help" → "If you need help"
- "The system has the ability to process" → "The system can process"
- "It is important to note that the data shows" → "The data shows"

### 24. Too many qualifiers

**Phrases to watch:** to be fair, it's also possible, could potentially, might arguably, in some cases it may, this is an inference
**Problem:** Repeated editing can add one qualifier after another until every claim sounds uncertain. Keep a qualifier only when the source supports it and the meaning needs it. Remove caveats that only repair an earlier overstatement.
**Before:**
> It could potentially possibly be argued that the policy might have some effect on outcomes.
**After:**
> The policy may affect outcomes.

### 25. Generic positive endings
**Problem:** AI writing often ends with vague optimism instead of the last useful fact.
**Before:**
> The future looks bright for the company. Exciting times lie ahead as they continue their journey toward excellence. This represents a major step in the right direction.
**After:**
> (Cut the paragraph. End on the last concrete fact instead of a send-off. If the source states real plans, use those.)

### 26. Too many hyphenated word pairs

**Words to watch:** third-party, cross-functional, client-facing, data-driven, decision-making, well-known, high-quality, real-time, long-term, end-to-end
**Problem:** AI writing often hyphenates these pairs everywhere. Keep the hyphen before a noun when grammar needs it, as in `a high-quality report`. Drop it after the noun, as in `the report is high quality`.
**Before:**
> The cross-functional team delivered a high-quality, data-driven report. The team is cross-functional, the report is high-quality, and the methodology is data-driven.
**After:**
> The cross-functional team delivered a high-quality, data-driven report. The team is cross functional, the report is high quality, and the methodology is data driven.

### 27. Pretending to reveal a deeper truth

**Phrases to watch:** The real question is, at its core, in reality, what really matters, fundamentally, the deeper issue, the heart of the matter
**Problem:** AI writing uses these phrases to make an ordinary point sound like a hidden truth.
**Before:**
> The real question is whether teams can adapt. At its core, what really matters is organizational readiness.
**After:**
> The question is whether teams can adapt. That mostly depends on whether the organization is ready to change its habits.

### 28. Announcing the next point

**Phrases to watch:** Let's dive in, let's explore, let's break this down, here's what you need to know, now let's look at, without further ado, heads up, quick note, before I forget
**Problem:** AI writing often announces the next point instead of stating it. A casual phrase such as "one thing that bit me" can have the same problem. Remove the announcement, not just its formal tone.
**Before:**
> Let's dive into how caching works in Next.js. Here's what you need to know.
**After:**
> Next.js caches data at multiple layers, including request memoization, the data cache, and the router cache.
**Before (casual register):**
> One thing that bit me hard, so pay attention to this part: the webpack dev server doesn't send the CORS header by default.
**After:**
> The webpack dev server doesn't send the CORS header by default.

### 29. A heading repeated in the first sentence

**Signs to watch:** A heading followed by a one-line paragraph that simply restates the heading before the real content begins.
**Problem:** AI writing often follows a heading with a sentence that only repeats the heading. Remove the repeated sentence.
**Before:**
> ## Performance
>
> Speed matters.
>
> When users hit a slow page, they leave.
**After:**
> ## Performance
>
> When users hit a slow page, they leave.

### 30. Writing about the previous version
**Problem:** Documentation and comments should describe the current behavior. Mention the previous version only in change logs, release notes, migration guides, and other documents about change.
**Before:**
> This function was added to replace the previous approach of iterating through all items, which caused O(n²) performance.
**After:**
> This function uses a hash map for O(1) lookups, avoiding the O(n²) cost of naive iteration.

### 31. Forced punchlines and dramatic fragments
**Problem:** AI writing often turns each sentence into a dramatic closing line. One short sentence can add emphasis. A row of short fragments usually feels forced.
**Before:**
> Then AlphaEvolve arrived. It had no preference for symmetry. No aesthetic prior. No nostalgia for human taste. The old rules were gone.
**After:**
> AlphaEvolve changed the search because it did not favor symmetry or human-looking designs. That made some of the older assumptions less useful.

### 32. Formulaic sayings

**Words to watch:** X is the Y of Z, X becomes a trap, X is not a tool but a mirror, the language of, the currency of, the architecture of
**Problem:** AI writing often turns an ordinary claim into a saying that sounds deep but adds no detail. Replace the saying with the specific claim.
**Before:**
> Symmetry is the language of trust. Efficiency becomes a trap when teams forget the human layer.
**After:**
> Symmetric layouts often feel more predictable to users. Teams can over-optimize workflows and miss how people actually use them.

### 33. Fake-candid openings

**Phrases to watch:** Honestly?, Look, Here's the thing, The thing is, Let's be honest, Real talk, when used as standalone hooks or fake-candid pauses before an ordinary point.
**Problem:** AI writing often starts with a staged pause or claim of honesty before making a routine point. State the point directly.
**Before:**
> Is it worth the price? Honestly? It depends on how often you'll use it.
**After:**
> Whether it's worth the price depends on how often you'll use it.

### 34. Answering objections no one raised

**Phrases to watch:** This isn't (mainly/really) about, I'm not saying/arguing/trying to, To be clear, Don't get me wrong, This is not to say, You could argue/frame this differently but, Some might say... but
**Problem:** AI writing may answer an objection that does not appear in the text. Watch for an unattributed statement about what the writer does not mean, especially when the topic appears nowhere else. A direct claim such as "the API is not thread-safe" is not this pattern.
**Before:**
> This isn't mainly about prompt length, and I'm not arguing that documentation doesn't matter. You could categorize the problem another way, but the issue is whether the agent can use the instruction when it acts.
**After:**
> The issue is whether the agent can use the instruction when it acts.

Remove only the unsupported defense. If it contains a real claim, state that claim directly. Keep an objection when the text names its source or answers it in full.

### 35. Rejecting fake alternatives

**Phrases to watch:** A tempting option/approach would be, One might be tempted to, An obvious approach would be, You might think... but, It would be easy to just, Some would suggest
**Problem:** AI writing may introduce an option that no reader would consider, reject it in a clause, and never mention it again. This often leaves an old drafting idea in the final text. Remove the fake option and state the real constraint directly.
**Before:**
> Session tokens are rotated every 24 hours. A tempting approach would be to rotate them by restarting the auth service on a cron job, but that would drop every active session. Rotation happens in place, and clients refresh transparently.
**After:**
> Session tokens are rotated every 24 hours, in place, and clients refresh transparently.

One rejected option may be valid. Several short, unrelated rejections are a stronger sign. Ask what new information each sentence adds. If it only records an earlier edit, rewrite the paragraph around its main point.

## What survives a sentence-level classifier

Tools that score text sentence by sentence flag some sentences and leave others alone. The split is measurable, and it is not what most style advice predicts. The patterns below were checked against a real highlight map, revising two earlier guesses that turned out to be wrong.

Sentence length is not the lever. A six-word sentence can read clean and a nine-word sentence can flag. Splitting a flagged sentence in half usually produces two flagged sentences and sometimes drags the next one in with it.

### 36. Self-contained statements

**Problem:** A sentence that can be lifted out of the paragraph and still make complete sense is a sentence a model could have produced from nothing. Sentences that need the previous one to be understood carry information the model has to guess at, and they survive.
**Flagged:**
> He splits a bowl of tomato soup down the middle.
**Clean:**
> In Gotham it does the opposite.
> The machines get hired for exactly that.
> Batman won't take the last step.

The clean examples are shorter than the flagged one. What they have is an antecedent: *it*, *that*, *the last step* all point backward. Write paragraphs where the sentences depend on each other, and prefer pronouns, demonstratives, and idioms that need a referent over restating the noun.

### 37. One frame reused across sections

**Problem:** AI writing reaches for the same sentence frame in section after section. "In X, ... In Y, ..." or "While A emphasized B, C emphasized D." Any one of them is fine. Together they expose the template.

Keep the frame where it works best and rewrite the others around whatever is specific to them. This matters most in questionnaires, FAQs, and any document with repeated headings, where the reader sees every instance at once.

### 38. Stock collocations

**Problem:** Word pairs that travel together in ordinary usage are the easiest thing in the world to predict. Odd pairings are not. This holds regardless of grammatical form, which is why rewriting a noun phrase as a gerund does nothing on its own.
**Flagged:**
> Taking an eye for an eye, The Dark Knight
**Clean:**
> Parting the soup, Bruce Almighty

Both are gerund phrases of nearly the same length. "Taking an eye for an eye" is a fixed expression. "Parting the soup" is a collision of a biblical verb with lunch. Look for the place where the writer's actual subject lets you put two words together that have not been put together before, and do not manufacture strangeness where the subject does not supply it.

### 39. Reference lines have a floor

**Problem:** Labeled citations, quoted scripture, definitions, and glosses read as reference text because that is what they are. `Bible reference: Exodus 14, the Red Sea.` will flag. So will a verbatim famous quotation. Paraphrasing around them helps a little; nothing removes them.

Do not degrade a citation, a quotation, or a required field label to lower a score. Fold the citation into a sentence that also does something else where the format allows it, leave it alone where the format does not, and tell the writer that the residue is their sources rather than their prose.

## Check for false positives

### What not to flag

A person may use some of these patterns. Do not treat any item below as proof by itself:

- **Perfect grammar and consistent style.** Many writers are professionals or have been edited. Polish does not equal AI.
- **Mixed casual and formal styles.** This can reflect the writer's field, age, or personal habits.
- **"Bland" or "robotic" prose.** AI prose has *specific* tells. Generic dryness without those tells is just dry writing.
- **Formal or academic words.** §7 lists specific words that AI writing overuses. Do not simplify every formal word.
- **Letter-style opening or closing on a comment.** Salutations and sign-offs predate ChatGPT by centuries.
- **Common transition words in isolation.** *Additionally*, *moreover*, *consequently* are AI-coded only when piled up. One *however* is not a tell.
- **Curly quotes alone.** macOS, Word, Google Docs, and most CMSes auto-curl by default. Curly quotes only count when stacked with other tells.
- **Em dashes alone.** Many editors and journalists use them often. Em dashes are evidence only when paired with formulaic sales-y rhythm.
- **One short sentence for emphasis.** Flag dramatic fragments only when several appear in a row.
- **Deliberate repeated openings.** Writers may repeat an opening to build rhythm or pressure, as in "She came. She saw. She conquered." Change it only when the repetition adds nothing.
- **"Honestly" or "look" mid-sentence.** These are ordinary in casual writing. The tell is the standalone theatrical opener, not the word itself.
- **Useful limits and disclaimers.** Keep scope statements, legal and safety notices, real corrections, named objections, replies, and FAQ answers.
- **Real alternatives.** Keep options that a reader may consider in a design document, tutorial, or argument. Remove only an unlikely option that the text dismisses and never uses again.
- **Unsourced claims.** Most of the web is unsourced. Lack of citations doesn't prove anything.
- **Correct, complex formatting.** Visual editors and templates produce clean output without any AI.
- **Secondhand text.** Do not rewrite watched phrases inside quotations, titles, proper names, or examples where the phrase is being discussed rather than used.
- **Spoken register in academic writing.** Student essays often use contractions, "pretty much," "the guy who," "ends up," and generic "you" inside an MLA frame. That mix is a human tell, not a flaw to fix.
- **Missing commas after short openers.** "In Eden God gave..." or "If you don't know Genesis the ending is..." is how many people write. Do not add commas just for correctness.
- **A comparison frame in a comparison essay.** "In Genesis... In the movie..." repeated across paragraphs is normal when the second half of each sentence changes. §37 applies to templated documents, not to an argument that compares two things.

When unsure, look for several patterns together. One em dash proves nothing. Several stock patterns in the same passage are stronger evidence.

### Human details to keep

These details often carry the writer's voice. Keep them unless they hurt the meaning:

- **Specific, unusual details.** Keep a real address, an odd quote, or a phrase such as "the lawyer who used to work upstairs from my dentist."
- **Mixed feelings and unresolved tension.** Keep lines such as "I think this is mostly good, but it bothers me, and I can't fully explain why."
- **Dated, era-bound references.** Slang, memes, or in-jokes that map to a specific year and subculture. Models lag by a year or more.
- **Deliberate first-person choices.** Keep a cut or word choice when the writer can explain why it belongs.
- **Variety in sentence length.** Real writing alternates short and long. AI writing tends toward an even, mid-length cadence.
- **Reading-process first person.** "That scene reminded me of...", "The more I thought about it, the more...", "Knowing Genesis changed how I saw this ending." A writer describing their own reading in the moment does something a model rarely does without being told to.
- **Quote, then plain gloss.** A quotation followed by a short everyday restatement ("The angels are there to keep people from getting back in.") reads as a person working through a source.
- **Genuine asides, parentheticals, or self-corrections.** "(I keep wanting to say 'almost' here, but it really was certain.)" Models rarely interrupt themselves like this.
- **Edits made before November 30, 2022.** ChatGPT's public launch. Anything older than that is, with very rare exceptions, not AI-written.

---

## How to return the result

**Pasted text (default).** Return the draft, a short list of remaining AI patterns, the final rewrite, and its ZeroGPT score from the verification loop.

**File mode.** When the user names a file, run the full rewrite process but write only the final text to the file. Change prose only. Keep code blocks, YAML metadata, data, and link targets unchanged. Then give the user a short summary that includes the ZeroGPT score.

**Embedded mode.** When another task uses this skill for a pull request, commit message, or document, return only the final text, and report the ZeroGPT score to the user separately.

## Rewrite process

1. Read the source and mark each AI pattern. If a saved voice profile applies (see [Saved voice profiles](#saved-voice-profiles)), load it now and use its checklist in steps 2 and 4.
2. Write a draft. Read it aloud. Check the rhythm, details, simple verbs such as *is* and *has*, and the right level of formality.
3. Ask three questions:
   - **"What still sounds AI-generated?"**
   - **"Could any sentence here be lifted out and still stand alone?"** See §36.
   - **"Did the rewrite add or remove any fact, name, number, date, quote, citation, ranking, or other claim?"**
   Treat any unsupported addition or lost claim as an error.
4. Write the final version. State each point naturally instead of patching one flagged phrase at a time. If a sentence stays awkward, rewrite the paragraph around its main point. Apply the dash rule in §14.
5. Run the [detector verification loop](#detector-verification-loop) on the final version. Keep rewriting until it scores under 10% or an exit condition applies.

Return the result required by [How to return the result](#how-to-return-the-result).

## Detector verification loop

Run this after every rewrite, in every return mode. The target is a ZeroGPT score **under 10%**. Keep rewriting and rescanning until the score is under 10% or an exit condition below applies. Never report a score you did not read from the result panel in this run.

### Before submitting: remove personal data

ZeroGPT is a third-party site, and anything pasted there leaves the user's machine. Before each submission, replace identifying data with placeholders of the same shape, then restore the real values in the final text returned to the user:

- Student, employee, patient, account, or other ID numbers: the same number of zeros (`123456789` becomes `000000000`)
- Phone numbers: `(000) 000-0000`
- Email addresses: `name@example.com`
- Street addresses and dates of birth: a generic placeholder of the same form
- The writer's own full name: a neutral placeholder name of similar length

The detector scores prose, so swapping these does not change the result in any meaningful way. If the text is mostly sensitive material, such as medical or legal records or anything the user marked private, ask before submitting it at all.

### Submitting and reading the result

Use the Chrome browser tools and open `https://www.zerogpt.com/` in a tab in this session's group.

Set the text and press the button with one script. The site is a React app, so set the value through the native setter and fire an `input` event. A plain `.value =` assignment does not register, and clicking the button by ref or by coordinates is unreliable because its position moves with the length of the text.

```js
const T = `...text with placeholders...`;
const ta = document.querySelector('textarea');
Object.getOwnPropertyDescriptor(HTMLTextAreaElement.prototype, 'value').set.call(ta, T);
ta.dispatchEvent(new Event('input', { bubbles: true }));
[...document.querySelectorAll('button')].find(b => /Detect Text/i.test(b.innerText)).click();
```

Wait 10 seconds, which is the longest single wait the browser tool allows, then read the result from the result card only. If the card is missing or still shows the previous text, wait another 10 seconds and read again:

```js
const card = [...document.querySelectorAll('div')]
  .filter(d => /Your Text/.test(d.innerText) && /AI GPT/.test(d.innerText) && d.querySelector('.highlights'))
  .sort((a, b) => a.innerText.length - b.innerText.length)[0];
const txt = card ? card.innerText : '';
JSON.stringify({
  verdict: (txt.match(/Your Text[^\n]*/) || [''])[0],
  pct: (txt.match(/([\d.]+)%\s*AI GPT/) || [])[1],
  analyzed: card ? card.querySelector('.highlights').innerText.slice(0, 40) : '',
  flagged: card ? [...card.querySelectorAll('.highlight')].map(m => m.innerText.trim()).filter(t => t.length > 2) : []
});
```

That script avoids three traps, each of which produced a wrong reading in testing:

- **Marketing numbers.** The page advertises accuracy percentages, so a page-wide search for `%` returns those instead of the score. Read the percentage only from the result card, next to "AI GPT".
- **Varying verdict text.** The verdict can read "Your Text is Human written", "Your Text is Most Likely Human written...", "Your Text contains mixed signals...", or "Your Text is AI/GPT Generated". Match on "Your Text", not "Your Text is".
- **Stale results.** The previous result card stays on the page while a new scan runs. Before trusting the score, check that `analyzed` starts with the text just submitted. If it does not, wait and read again. If the card still shows old text after two reads, reload the page and resubmit.

If the result card is missing after the wait, take a screenshot before assuming anything, because the scan may still be running.

### Rewriting between rounds

Rewrite only the sentences listed in `flagged`. Leave sentences that came back clean exactly as they are, since changing them can make them flag.

**Keep the register the text needs.** A lower score is never worth a change in tone the reader will notice. Emails to offices, instructors, and employers, applications, cover letters, and academic writing stay professional through every round. Lower their scores with structure: context-dependence, paraphrase, and sentence order. Do not reach for slang, casual asides, contractions the writer did not use, or jokey idioms. Formal stock phrases flag as readily as casual filler, so "I am writing to inquire about" and "Thank you for your time and consideration" are not the professional alternative. A specific, connected formal sentence is.

Apply what the highlight maps showed:

- Make each flagged sentence depend on its neighbors (§36). A backward-pointing *it*, *that*, *there*, or *this* is the strongest single fix.
- Define a term by paraphrase instead of naming the stock construct in the definitional slot. "The dependent variable is what they do about that worry" came back clean where "The dependent variable is self-protective behavior" flagged.
- Anchor an opening claim to a concrete fact. "For most of the time I've had my CMA, I figured being bilingual was..." came back clean where "I used to think being bilingual was the whole job" flagged.
- Break a colon label off the sentence it introduces. `Research question, in hypothesis form.` as its own sentence let the hypothesis after it score clean.
- Replace stock collocations with pairings that the writer's own subject supplies (§38), without leaving the register.
- Do not split a flagged sentence in half. Both halves usually flag.
- Do not cut the small words that carry voice in order to hit a length limit. Restoring "found out" and "actually" took one answer from 21.7% to 0%.
- In emails, fold boilerplate into real sentences. A bare "Thank you," and a contact line both flagged on their own.
- In emails, open on the concrete subject instead of an introduction or a list of credentials, and put ID numbers in the signature. That change took a registrar email from 26.6% to 0%.
- Rescan the whole text every round. Whether a sentence flags depends on the sentences around it, so an unchanged line can flip. The same email subject line came back clean in one round and flagged in the next.
- In professional writing, formality markers raise the score more than tone does. In testing, expanding the writer's own contractions, switching to passive voice ("could be added"), and using a compound noun such as "enrollment status" in place of a plain one together took three clean sentences to flagged. Restoring the writer's contractions and active voice, and replacing generic requests with specific ones ("a different route into that section"), took the same professional email from 57.9% to 0% without any slang.

Every rewrite still follows the rules above: no invented facts, no lost claims, the writer's voice, and no em dashes.

### Exit conditions

Stop and report instead of rewriting again when any of these holds:

1. **Under 10%.** The loop is done.
2. **Eight rounds without reaching 10%.** Return the lowest-scoring version that kept every claim, with its score and the sentences still flagged.
3. **Only reference material is still flagged.** If every flagged sentence is a citation, a quotation, a required field label, a date or credential line, a course list, or contact information, the remaining score is the floor described in §39. Report it as the floor. Resumes scored between 77% and 88% this way while being entirely factual.
4. **Lowering the score would break a real requirement.** Examples are a phrase a rubric requires, a mandated label, a word or character limit, a person, tense, or level of formality the context requires, or a claim the writer needs. Name the requirement and what it costs in score, and let the writer choose.
5. **No browser.** If the Chrome tools are not connected, say that the scan did not run. Do not estimate a score.

Very short texts, under about 60 words, sometimes score 0% whether or not they were rewritten. Treat a 0% on very short text as weak evidence and say so.

Close the tab when the loop ends.

## Source

This skill is based on [Wikipedia: Signs of AI writing](https://en.wikipedia.org/wiki/Wikipedia:Signs_of_AI_writing), maintained by WikiProject AI Cleanup. Its patterns come from reviews of AI-generated text on Wikipedia.

Wikipedia's main point: "LLMs use statistical algorithms to guess what should come next. The result tends toward the most statistically likely result that applies to the widest variety of cases."
