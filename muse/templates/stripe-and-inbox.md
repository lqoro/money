# Copy to paste into Stripe, Google Workspace and the website host

## Stripe Payment Link (Dashboard → Payment Links → New)
- Product name: `LeadDrop Weekly Lead List`
- Description: `25 researched local prospects every Monday, each with a contact route, a reason to talk now, and an opening line. Cancel any time.`
- Price: `$400.00 USD`, **Recurring**, **Monthly**
- Collect: customer name and email (on by default), plus a custom text field `What do you sell, and who is your best customer?`
- After payment: show a confirmation page with `Thanks. Your first 25 leads arrive by next Monday. Reply to the receipt email with anything we should know about your ideal customer.`
- Statement descriptor: `LEADDROP`
- Then copy the link into `muse/MEMORY.md` → `payment_link` and run `python3 scripts/build.py`.

## Inbox signature (Gmail → Settings → Signature)
```
Lenny Ramirez
LeadDrop · {{domain}}
{{physical_address}}
```

## Inbox auto-reply: leave it off
Muse answers within 2 hours with your approval. An auto-reply makes the first touch look automated.

## Website (free hosting, about 5 minutes)
1. Run `python3 scripts/build.py` once every FILL_ME is filled in.
2. Go to https://app.netlify.com/drop and drag the `build/site` folder onto the page.
3. In Netlify: Domain management → Add a domain → enter your domain, then add the DNS records it shows at your registrar.
   (Cloudflare Pages works the same way if you'd rather use that.)

Your repo is private, so GitHub Pages would need a paid plan. Netlify Drop is free.
