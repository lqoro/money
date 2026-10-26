# Email templates

These are starting points. Every one gets a **playbook 07 humanizer pass** after filling in, so the sent text
isn't word-for-word identical across prospects. `{{observation}}` comes from a page you actually visited.
Footer on every cold email (required):

```
{{owner_name}}, {{business_name}}
{{physical_address}}
If you'd rather not hear from me again just reply "no thanks" and I won't email you again.
```

## First touch
Subject: `{{business}}'s next few clients` (or `leads for {{business}}`)

```
Hi {{first_name or "there"}},

I was looking at {{business}}'s site and {{observation}}. That made me think you're probably looking for more
{{their_customer_type}} in {{city}}.

I put together lists of local businesses that fit an agency's ideal client, with the person to contact and a reason they'd
want to talk now. I'd be happy to send you 10 for {{their_customer_type}} in {{city}} for free so you can see if they're any good.

Want me to send them over?
```

## Follow-up 1 (day 3)
```
Hi {{first_name or "there"}}, just checking this didn't get buried. The offer's still open: 10 {{their_customer_type}} leads in
{{city}}, free, no call needed. I'd just need to know you want them.
```

## Follow-up 2 (day 7, the last one)
```
Last note from me on this. If more {{their_customer_type}} clients aren't a priority right now that's fine and I'll stop here.
If they are, reply "send" and I'll have 10 leads to you within a day.
```

## Sample delivery
```
Hi {{first_name}}, here are the 10 {{their_customer_type}} leads for {{city}}: {{sheet_link}}

Each one has who to contact, how to reach them, and why they might want to talk now. Number {{best_row}} looked like the
strongest fit to me since {{best_reason}}. I also wrote an opener for each one you can use as is or change.
```

## Offer (day 2 after the sample)
```
Hi {{first_name}}, did any of those leads look worth reaching out to?

If you want this every week it's $400 a month for 25 new leads every Monday, no repeats, cancel whenever. If fewer than 20 of
them are a real fit I replace them that week. You can start here: {{payment_link}}
```

## Price question
```
It's $400 a month for 25 researched leads every Monday. There's no setup fee and you can cancel anytime. The free 10 are
the easiest way to see if the quality's worth it for you.
```
