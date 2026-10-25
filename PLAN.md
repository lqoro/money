# Plan: Make money online from Spain (Jan 2027 semester)

## Context
You're studying abroad in Spain next semester and want ~$1,000/week online, either from a US remote AI job or from an AI-driven income stream. You have until January (~10 weeks, today is Oct 22). Resources: Mac Mini at home (always-on), ChatGPT/Claude Plus-tier plan, 20-30 hrs/week available, US citizen, Spanish visa appointment in Houston on **Nov 5**.

Honest framing: "$1k/week fully automated by AI" is not realistic as a first income. Truly passive AI products (faceless channels, AI-generated sites, etc.) are saturated and take months to pay. What works in a 10-week window is **AI-assisted services sold to small businesses** (human sells + checks, AI does the bulk of the work, Mac Mini runs the automations). That can reach $1k/week with 3-5 retainer clients. A **part-time US remote job** is the stable floor in parallel. Plan runs both tracks.

## Step 0: Visa/legal gate (do first, Nov 5)
- Ask at the Houston consulate appointment: does the student visa permit remote work for non-Spanish clients/employers? (Student visas generally restrict working in Spain; remote work for foreign clients is a gray area. Get the answer in writing/specific wording.)
- Ask about tax: US citizen still files US taxes; freelancing as a self-employed person may need a Spanish autónomo registration if resident >183 days. Book a short consult with a tax pro before taking first payment from abroad.
- Everything below can be built and tested pre-departure; don't take paid work abroad until this is answered.

## Your profile (from resume + answers)
TCU BSN student (transfer, Fall 2026, exp. May 2029), active NHA CMA (phlebotomy, EKG, intake, documentation), BLS, 3.877 GPA with Dean's List, Pell recipient, fluent in Spanish, no coding (uses Claude), works 40-46 hrs/wk at QuikTrip until leaving. Resume is strong; small upgrades: add a Skills line (Spanish fluent, EHR/documentation if applicable, Claude/AI tools) and a bilingual mention in the summary. Keep your phone number off public repos.
Implication: your edge is healthcare + bilingual + AI literacy, not coding. Lead with that; the generic AI-automation service is secondary.

## Track A: Remote job (stable floor), weeks 1-4
- **Best fit first**: medical/clinical expert roles on AI-training platforms (Mercor, Outlier, DataAnnotation, Surge-type, Handshake AI): review and write medical Q&A, rate chatbot answers. CMA + nursing student + 3.9 GPA can qualify for domain-expert pay tiers (often well above generalist pay). Apply to the medical/health domain, not generic tasks.
- **Remote medical scribe / documentation** (bilingual Spanish scribes in demand), telehealth patient intake/scheduling support, bilingual patient outreach, prior-authorization or care-coordination support. Check each employer's rules on working from outside the US.
- No tutoring (you said live teaching isn't your thing). Dropped.
- Also still fine: part-time/contract AI ops, support/QA, junior ops at US startups.
- Time-zone fit: Spain is 6-9 hrs ahead of the US, so async/contract roles beat fixed-hours roles.
- Actions: build a 1-page portfolio + resume, apply to 5-10 roles/week, sign up for 2-3 AI-training platforms right away (these pay $20-50/hr and onboard in days; they can bridge income).

## AI-assist rules (you approve everything)
- Fine: Claude drafts, you review, edit and approve. Use it for tutoring prep and lesson plans, outreach drafts, resume and portfolio, automation builds, admin, and study summaries.
- Check each platform/employer/scholarship policy before using AI on their work. Where AI is banned or must be disclosed (many AI-trainer tasks, assessments, scholarship essays), your own words only. Disclose where required.
- Do not use the humanizer to hide AI use where AI is prohibited. It is for polishing drafts you are allowed to use, not for beating detectors. Getting caught means permanent bans or a rescinded scholarship.
- Medical judgment stays yours. Never submit AI-generated clinical answers as your expertise, and never imply credentials you lack.
- Log the policy for each platform in `tracks/job-search.md` ("AI allowed? Y/N/disclose").

## Track B: AI automation service (upside), weeks 1-10
Offer: done-for-you AI workflows for local small businesses (lead follow-up, review replies, appointment reminders, content repurposing, invoice/data entry).
1. **Weeks 1-2 Pick one niche** (e.g. dentists, real-estate agents, gyms, restaurants) and one repeatable offer. Build the demo on the Mac Mini (n8n or Make + Claude/OpenAI API).
2. **Weeks 3-4 Get 2-3 pilot clients** at a discount for testimonials. Outreach: 20 personalized messages/day (email/LinkedIn/in person back home before you leave).
3. **Weeks 5-10 Convert to retainers** ($300-1,000/mo each; setup fees $500-1,500). Target 3-5 clients by January.
4. **Mac Mini setup**: always-on, remote access (Tailscale), n8n self-hosted, nightly backups, monitoring alerts to your phone.
- Rough math: 4 retainers x $600 + 1-2 setups/mo x $1,000 ≈ $3.5-4.5k/month, roughly $1k/week.

### What the Nate Herk recap (368 videos) adds to Track B
Source: `053bd192-ALL-VIDEOS-RECAP.md` (his own claims, not verified; he also sells courses/community). The recap's own bottom line: one small-business pain, one automation, one retainer. Not recommended by the recap itself: faceless AI channels, AI trading bots, scraping/cold email without checking rules.
- **Ladder** (#259): sell hours (help a business owner set up AI) -> paid audit -> first project -> retainer. Earn each rung from the one below.
- **Getting the first client** (#151, #180, #184): warm first. Day 1 write a one-sentence offer + list 20 trusted contacts; days 2-3 hold 5-10 low-pressure conversations; one or two free pilots for testimonials; cold outreach last. Claimed first-build prices: $1,200-$2,600 (#121, #163, #167, #180: $1,500-$2,000).
- **What sells** (#213, #311): speed-to-lead / missed-call text-back, document processing, follow-up sequences, database reactivation, customer support, voice receptionist/after-hours booking. Sell the outcome (hours saved, revenue recovered), not the tool.
- **Pricing** (#156, #301): price on client value, not your hours; build fee + monthly maintenance retainer; get a baseline KPI before you start. Ignore the "$20K/month retainer" claims; they're not a beginner benchmark.
- **Delivery** (#165): client owns the accounts (their n8n/Google), scope and "done" in writing, separate maintenance retainer, signed webhooks/HTTPS, minimal personal data.
- **Claude-first build path** (#171, #173, #187, #198, #293 "Claude Code for Non-Coders", #356): since you don't code, build workflows by describing them to Claude and approving the plan, instead of learning n8n node-by-node. Use n8n or Claude Code on the Mac Mini.
- **"AI person" path** (#255, #295, #297, #309): become the go-to AI builder inside one team. For you that could be a clinic or health-system role later; it also supports the remote-job track.
- **Your niche fit**: bilingual clinics, dental offices, and similar local-service businesses (#213 lists dental). Start with missed-call text-back, appointment reminders, review replies, and intake follow-up that touch no patient health data. HIPAA warning (#130): anything with PHI is not a quick launch.
- **Watch order (about 3-4 hours)**: #123 how to sell without an agency, #151 sign first client, #133 sell solutions, #213 what businesses want, #156 pricing, #165 delivery, #293 Claude Code for non-coders. Skip the model-release and trading videos.

## Track C: Class-action settlements (small, honest cash)
Reality: payouts are typically $5-$100 each, so this is a few hundred dollars total, not income. "No proof" means no receipt is needed, but every form is a sworn statement that you are in the class. Only file for ones you actually qualify for; false claims are fraud and get flagged/denied.
- **Apple Siri/AI settlement ($250M, Landsheft v. Apple)**: you bought an iPhone 15 Pro/Pro Max or 16 model new (Jun 10, 2024 - Mar 29, 2025). $25/device, possibly up to $95. File at smartphoneaisettlement.com. **Deadline Dec 21, 2026**; payouts after the Feb 24, 2027 hearing.
- Build `tracks/settlements.md`: a table of open settlements (name, eligibility test, deadline, official claim URL, filed Y/N). Only list ones where you meet the test. Sources to scan: official administrator sites, openclassactions.com. Near-term deadlines seen: pork price-fixing (Oct 29), Bestway pool (Oct 30), CVS privacy (Nov 16); verify each yourself.
- Do the Apple claim first. Check other Apple devices (Mac, etc.) against active Apple settlements.
- I can prepare drafts and checklists, but you submit each form yourself (it is your sworn attestation).

## Track D: Scholarships (mass apply, free only)
- Never pay to apply; skip any "guaranteed" or fee-based service.
- Pell recipient: **Gilman** (up to $5,000) for study abroad. Fall cycle closed Oct 1; the next cycle (for spring/summer/academic-year programs) is typically ~March 2027. Confirm at gilmanscholarship.org.
- **Boren** (up to $25k, language/national security): campus deadlines come first, e.g. ~early Jan 2027; national deadline late Jan. Ask your school's fellowships advisor now.
- **Study abroad office**: ask for every Spain/spring-2027 award and its deadline (many program-specific funds close soon).
- **Hispanic Scholarship Fund (HSF)**: you're a Hispanic student with a 3.877 GPA; the HSF application typically closes around Feb 15 (verify at hsf.net). Also check Pell/need-based aid at TCU as a transfer student, and TCU nursing-specific scholarships.
- **Nursing scholarships**: Texas Nurses Association/Foundation, Hispanic-nursing associations (e.g., NAHN), health-system sponsored awards. Your CMA + Dean's List + work hours (40-46/wk) is a strong "overcame obstacles" essay.
- General: build one master profile (essay bank, resume, recommenders) and reuse across Fastweb, Scholarships.com, Bold.org, Going Merry, and your school's portal.
- Build `tracks/scholarships.md`: table of name, amount, deadline, requirements, status. Target 5 applications/week.

## Milestones
- Nov 5: visa answer on remote work.
- Nov 15: platform signups done, portfolio live, niche chosen, demo built.
- Dec 1: first pilot client or first AI-training payout.
- Jan 1: 2+ paying clients or a job offer; systems running unattended.
- Feb-Mar (in Spain): scale to $1k/week, keep ~10 hrs/week on delivery.

## Open items
- Answered: skills = healthcare + bilingual + Claude, no coding; QuikTrip until you leave; direction = both tracks.
- Track B niche decision: pick a healthcare-adjacent one (bilingual, e.g. clinics/dental practices serving Spanish speakers: appointment reminders, intake follow-up, review replies). Compliance caution: no patient health data in tools without a HIPAA agreement; start with marketing/scheduling workflows that touch no PHI.
- Confirm with the study abroad office/clinical program: does the BSN schedule allow a semester abroad and any clinical hour requirements? (Affects hours available.)
- Visa: note remote-work legality and that medical roles may require a license/credential you must not misrepresent.

## Immediate actions once plan is approved
1. `lqoro/money` now exists (created by the user) and is cloned at `/home/user/money` (contains only the initial README.md). On a branch `claude/money-plan`, copy `money/PLAN.md` from the `appideas` PR (#5) to `/home/user/money/PLAN.md`, link it from README.md, commit, push, and open a draft PR. Then close appideas PR #5 and remove its branch content, since the plan lives in `money` now.
2. (Done) `tracks/job-search.md` and `tracks/automation-service.md` trackers are in the money repo, PR #1.
3. In `/home/user/money` on branch `claude/money-plan`, add `tracks/settlements.md` and `tracks/scholarships.md`, update the README links, commit, push (the open PR #1 picks it up).
4. Draft a scholarship master profile (essay bank outline, resume bullets) once you share your major, GPA, and school.

## Verification
- Repo `money` exists with the plan committed and readable.
- Weekly review checklist: applications sent, outreach messages sent, clients signed, revenue.
