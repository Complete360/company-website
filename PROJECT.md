# Complete360 — Project Brief for AI Agents

> Read this first. It is the shared context for any AI agent (Claude Code, Claude
> Projects, Cowork, or other assistants) working on Complete360's website, AI agents,
> or customer-facing copy. Last updated: 2026-11-12.
>
> If something here conflicts with an older page, prompt, or knowledge base, **this
> document and the legal pages (ToS / Return Policy v2.1) win.** If you change a fact
> that lives here, update this file in the same commit.

---

## 1. The company

| | |
|---|---|
| **Name** | Complete360 (formerly Community Marketing Partnership; acquired and renamed) |
| **What we do** | Digital marketing agency helping local service businesses get more calls and customers: Google, paid ads, websites, and an all-in-one CRM platform |
| **Location** | 3444 N Country Club Rd, Ste 105, Tucson, AZ 85716 · Arizona LLC · serves clients nationwide |
| **In business since** | 2018 |
| **Hours** | Mon–Thu 7am–4pm, Fri 7am–1pm MST (Arizona, no daylight saving). Closed weekends. |
| **Website** | complete360.org (built on GoHighLevel) · CRM login: app.complete360.org · Geo Ads portal: portal.cmpusa.org |

### Phone lines — use the right one
| Line | Number | Use for |
|---|---|---|
| **Customer service / finance** (group ring line) | **(800) 863-2541** | The public number for existing clients: billing, refunds, cancellations, failed payments, receipts, account support, guarantee eligibility |
| **Main / sales** | **(866) 527-6205** | Prospects, new business, general questions, pre-purchase questions |
| Luis — direct line | (520) 556-7400 | Luis's direct customer service line for Complete360 customers. Missed calls are answered by the AI agent Jessica ("Luis's Answering Service"). |
| Gabriel — onboarding line | (520) 492-0951 | Gabriel's line for clients in onboarding/setup. Missed calls are answered by the AI agent Jessica ("Gabriel's Answering Service"). |

AI agents never read out team members' direct lines; they take a message or route to the right person.

### Team roles
| Person | Role | Handles |
|---|---|---|
| **Jared** | Runs Complete360 overall | Manages the whole company as a project: direction, website, AI agents, products and policies. Repo owner. |
| **Liz** | Supervisor (reports to Jared) | Day-to-day supervision of the team. New to the role as of Nov 2026; also takes website tasks such as adding schema to GHL pages. |
| **Luis** | Customer Service | Billing, pricing, plan changes, account questions; primary contact for active campaigns (LSA, Google PPC, Meta, GBP, listings) |
| **Gabriel** | Deliverables & Deployment | Setup, builds, ad account setup, technical backend. Not offered to callers as a contact unless they ask for him. |

### Trust signals you may use
Certified Google Partner · Google Product Expert on the team · 147 five-star reviews (5.0 on Google) · in business since 2018 · Tucson-based, serving nationwide.
**Never claim** Meta Business Partner or BBB accreditation.

---

## 2. Products and services

Every product below has a live page (slug shown). **Prices live on each service page —
the page is the source of truth.** Do not copy prices into other places without checking
the current page.

| Product | Live page | Repo file | Billing |
|---|---|---|---|
| Local Service Ads (LSA) | /local-service-ads | `services/local-service-ads.html` | One-time setup + recurring management |
| Google Business Profile Management | /gbp-management | `services/gbp-management.html` | Recurring (monthly or prepaid terms) |
| Google Business Profile Setup & Optimization | /google-business-profile | `services/gbp-setup.html` | One-time |
| SEO Services (website SEO) | /seo-services (**live; not in nav yet**) | `services/seo-services.html` | $599/mo or $5,990/yr. One package, 4 parts: website SEO setup (technical fixes, Search Console + Analytics, competitor review + keyword plan, AI crawler check, structured data) · up to 5 main pages optimized for Google and AI search · every month: 2 service/city pages + 2 blog posts + 1 page refreshed · monthly report (rank tracking, AI visibility check, site health scan). No ranking or AI-recommendation guarantees. |
| Local SEO Booster | /local-seo-booster | `services/local-seo-booster.html` | Annual (monthly plans also offered) |
| Geo-Fencing (Mobile + CTV) | /geo-fencing | `services/geo-fencing.html` | Recurring / impression packages |
| Google PPC (Google Ads) | /google-ppc | `services/google-ads.html` | Recurring management; ad spend billed by Google |
| Meta Ads | /meta-ads | `services/meta-ads.html` | Recurring management; ad spend billed by Meta |
| Google Social Posting | /google-social-posting | `services/google-social-posting.html` | Recurring |
| Meta Social Posting | /meta-social-posting | `services/meta-social-posting.html` | Recurring |
| Reputation Management | /reputation-management | `services/reputation-management.html` | Recurring |
| Local Display Network (in-store screen ads) | (not in site nav yet) | `services/local-display-network.html` | Recurring |
| Dispensary / cannabis geo-fencing | /dispensary | `services/dispensary.html` | Recurring — specialist-handled |
| ProCard | /procard | `services/procard.html` | **One-time** |
| Websites (Essentials / Pro / Premium) + hosting | /websites-home, /website-pricing | `services/websites-home.html`, `pricing/website-pricing.html` | Deposit + final payment; hosting monthly |
| AI Agents (AI Voice Agent, AI Assistant, Custom) | /ai-agents | `services/ai-employee.html` | Monthly or annual + one-time setup |
| CRM Platform (SaaS tiers, Lifetime Deal) | /crm-home, /pricing | `crm-platform/crm-home.html`, `pricing/saas-pricing.html` | Monthly (all tiers) |
| Google Platinum Package | — (checkout only, **no service page yet**) | — | Bundle of Google services (GBP Management + LSA) |
| Farmers Insurance agent program | /farmers-insurance | `partners/farmers-insurance.html` | Partner program |

**AI Agents pricing (as published on /ai-agents):** AI Voice Agent $399/mo or $3,990/yr ·
AI Assistant $599/mo or $5,990/yr · $2,000 one-time setup for both · Custom Agents quoted.
Annual = 2 months free. **Unlimited AI usage — "no per-minute AI fees." Phone service
(number + calling minutes) is billed separately.** Never say "no per-minute fees" alone.

---

## 3. Policies (must match everywhere)

Source: Terms of Service and Return & Refund Policy v2.1 (`ghl-snippets/legal/`).

- **Refunds:** All payments are **non-refundable from the time of purchase.** Only two
  exceptions, both case by case: billing errors (duplicate or unauthorized charges,
  reported within 7 calendar days) and refunds approved by management at its sole
  discretion. Never promise or imply a refund.
- **Cancellation:** Recurring services require **at least 10 days' notice before the next
  billing date**, confirmed in writing. Later notice takes effect after the following
  cycle. Annual services are not refunded or prorated; cancel at least 10 days before
  renewal to stop it renewing. Verbal cancellations are not accepted.
- **Satisfaction guarantee:** For **GBP Management and all advertising campaigns**
  (Google PPC, Meta Ads, Geo-Fencing, Local Display Network, LSA): if the client isn't
  satisfied at the end of the service period, the campaign is extended at no charge.
  Conditions: onboarding completed and approvals on time, concern raised at the end of
  the initial period (not mid-campaign), account in good standing.
- **Ad spend** is separate from management fees and billed through the ad platform.
- **Banned phrases** in customer-facing copy and AI agents: "cancel anytime",
  "money-back guarantee", "no per-minute fees" (without "AI").

---

## 4. Brand and copy rules

- **Never name the underlying software** (HighLevel, GoHighLevel, LeadConnector) in
  customer-facing copy. Say "Complete360 CRM" or "the platform." Only exception: telling
  clients to search "LeadConnector" to download the mobile app.
- Agents call the search product **"Google PPC"** (a visitor saying "Google Ads" means the
  same thing). Google PPC and Local Service Ads are **separate products**.
- Customer-facing: write **"Google Business Profile"**, not "GBP".
- Never quote paid-ads (Google PPC / Meta) prices in chat or voice — send the page or book a call.
- All services are live — never "coming soon".
- **Colors:** navy `#122078` · green `#127825` · sand `#F1EFE8`. **Font:** Poppins.
  **Icons:** Font Awesome 6.5.1 (loaded by the global header).

---

## 5. The website repo — `github.com/Complete360/company-website`

The site runs on GoHighLevel. This repo is a **version-controlled library of custom code
snippets**, not a deployable site. Code goes live only when someone pastes it into a GHL
Custom Code block.

```
ghl-snippets/
  global/        header.html, footer.html (on every page), 404.html
  home.html
  services/      one file per service page
  industries/    industry pages at /industries/[industry] (hvac, roofing done; see the worksheet)
  pricing/       pricing pages (more coming)
  checkout/      checkout pages: each becomes a folder of numbered snippets
                 (1-pricing, 2-order-summary, 3-reviews, 4-faq) placed around
                 GHL's native order form. Done (v1.0, as-is): google-platinum/, local-service-ads/,
                 local-seo-booster/, gbp-setup/,
                 gbp-management/, google-social-posting/,
                 meta-social-posting/, meta-ads/,
                 procard/, dispensary/,
                 geo-fencing-mobile/, website/,
                 geo-fencing-ctv/, google-ads/,
                 ai-agents/, seo-services/
  crm-platform/  CRM home, Capture/Nurture/Close, feature pages
  company/       FAQ, contact, demo, thank-you, training, video library, link tree
  legal/         tos, privacy-policy, return-policy
  partners/      farmers-insurance
ai-agents/       prompts for every GHL AI agent (see its README)
schema/          JSON-LD for every page (schema/pages/), built by schema/build_schema.py
ghl-meta/        copy/paste GHL SEO meta data for new pages (industries/ first)
README.md        structure + page checklist (status and notes per file)
PROJECT.md       this file
```

### Conventions
- **Filenames:** lowercase, hyphens, `.html`. Name after the page; where the live URL is
  odd, the README checklist maps file → GHL page name.
- **Placeholders:** a file with no code yet contains only a comment starting
  `<!--\n  PLACEHOLDER: no code yet` with the GHL page name and next step. Replace the
  whole file with real code.
- **Every snippet starts with a header comment:** page name, version, which GHL page it
  goes on, and a short changelog. Bump the version on every change.
- **CSS prefixes:** each page scopes its classes (e.g. `c360-tos-`, `c360-rp-`,
  `c360-faq-`, `c360ga-`, `c360ma-`, `c360ai-`, `c360-gbp-`, `c360w-`) so nothing collides
  with the global header/footer. New pages need a new, unique prefix.
- Header and footer are global GHL sections — **never include them in page snippets.**
- **README checklist:** when you add or change a file, update its row (✅ Code in repo /
  ⬜ Placeholder, plus Notes such as "🔁 Rebuild needed" or "paste into GHL") and the
  "X of Y files have code" count.
- Legal files use CRLF line endings — preserve them.

### Status (2026-11-12): 49 of 66 page files have code
- **Done:** global header/footer, home, all 16 service pages, website pricing, CRM home,
  legal (3), FAQ, contact, training, video library, link tree, Farmers Insurance.
- **Live in GHL (Nov 10):** Terms v2.1, Return Policy v2.1, FAQ v2.4 and every policy-aligned service page (see README). Schema still to paste on most pages.
- **Next (in order):** CRM platform pages (SaaS Pricing, Capture, Nurture, Close, Inbox,
  Calendar, Chat Widget; decide on Forms) → remaining pricing pages → new pages (Google
  Platinum Package, possibly Landing Page) → company rebuilds (Request a Demo, both
  Thank You pages) → 404 → **checkouts last** (19 pages, each 3–4 snippets).
- **Later:** /about and /blog (linked in nav but disabled for now).

---

### Schema (structured data)
- Every page's JSON-LD lives in `schema/pages/` (same folders as `ghl-snippets/`). It goes in
  GHL's own schema editor: page editor → SEO & AI search optimization → Schema Markup → JSON
  view. Not Tracking Code, not the snippet. Steps and GHL's quirks are in `schema/README.md`.
- Every item has a single `@type` (GHL discards saves with a type list); the company item is
  `ProfessionalService`.
- Generated by `python3 schema/build_schema.py`: FAQs and descriptions are pulled word for word
  from the snippets (checkout folders are read as one page); company facts are in
  `ORGANIZATION` at the top of the script. Re-run after changing a page's FAQ or hero copy,
  commit, and re-paste that page's schema.
- The builder holds back (⚠ HOLD) any page whose copy still conflicts with the refund/cancellation
  policy; fix the page, re-run, then paste.
- Thank-you pages, /training, /404 and **all checkout pages** get no schema; set them to noindex in GHL.
  (Checkouts decided Nov 11, 2026: search traffic should land on the service pages, and the checkout
  FAQs repeat the service-page FAQs.)

## 6. GoHighLevel

- **Main sub-account:** "Complete360" · location ID `1pBjHBEIsKGbwvAUTY9u`.
  (Other Complete360 sub-accounts exist for snapshots, affiliates, demos — don't edit those.)
- **Shared knowledge base:** `9xrTMivBdEHfIIRhf0GM`, trained by crawling 56 live pages on
  2026-07-25. **Stale** — retrain the ToS, Return Policy, and FAQ pages after they're pasted
  live, and retrain any page you change.
- **AI agents:** all prompts are in `ai-agents/`. That folder is the source of truth —
  change the file, then push to GHL.
  - Voice AI agents (Dakota, Riley EN/ES, Jessica ×2, Sarah) can be read and updated
    through the GHL API connector.
  - Conversation AI agents ("Live Chat Widget" — text chat on the site, on Auto-Pilot;
    "AI SMS Responder" — off) **cannot** be reached through the API. Edit the file, then
    paste into GHL by hand.

---

## 7. Known issues and open decisions

- **Checkout open items (decide at the end of the checkout imports; details in each README row):**
  Google Social 6/12-month prices ($774/$1,308 checkout vs $715/$1,252 page) ·
  Platinum: Reputation Management in the bundle, "won't be double-billed" upgrade line ·
  LSA: "Performance Promise", background-check cost, setup-fee waiver ·
  GBP Setup: "Quality Promise", "hundreds of profiles" · GBP Management: confirm the Terms'
  guarantee box (or drop it like Meta Ads) · ProCard: "lifetime license / own it forever",
  free minor edits · Dispensary: legal review of legality/compliance claims and VFW/Legion
  naming, ad spend vs fixed impressions, CTV/desktop formats vs cards, "slightly higher" monthly ·
  Geo Mobile: ad spend separate vs impressions included, "#1 Location Intelligence Platform" (also CTV),
  "completely legal" competitor targeting ·
  Website: page counts vs /website-pricing, "one-time setup" vs deposit + final payment,
  "own your domain" ·
  Google Ads: prepay "don't auto-renew" vs the Terms' renewal clause, Most Popular tier;
  strip internal HTML comments (agent-only pricing) before pasting ·
  all checkouts: "Tucson businesses" reviews headline · older checkouts
  use wrapper id `order-form` instead of `c360-order-form`.

- **14-day CRM free trial vs the 10-day cancellation rule:** the Terms don't mention trials. Decide how
  cancelling during a trial works and add it to the Terms (CRM Home v2.10 and Training v1.1 no longer
  promise "cancel anytime before day 14").
- **Header:** other pages reference a live header v1.9.4 that isn't in the repo; the repo header is now
  v1.9.5. Compare with GHL before pasting it.
- **"Cancel anytime" / 30 days' notice / money-back wording removed from every page (Nov 10)**, including
  CRM Home, Payments, the header menu and the internal Training scripts. In the repo; each page still
  needs pasting into GHL (see README notes).
- **Google Ads / Meta Ads 90-day guarantee:** removed from both pages and the training scripts (Nov 10).
  The Terms' guarantee (campaign extension) still applies to all ad campaigns.
- **/reputation-management-checkout** is linked 5× but doesn't exist in GHL — broken buttons.
- **Local Display Network** page isn't linked from header, footer, or home.
- **SEO Services** is live and in the nav (footer v1.7 live; header v2.2 adds it to Solutions + Pricing). The
  page's Get Started buttons still go to /schedule-demo; point them at /seo-services-checkout.
- **Header Pricing rail:** Paid Lead Generation says "From $499/mo" ($499 is the setup fee; monthly starts at
  $349 LSA / $399 PPC & Meta). Decide the label.
- **Google Platinum Package** has a checkout but no service page. **Landing Page** is pitched
  by the AI agents as a product but has no page or checkout.
- **Lifetime Deal** — confirm whether it's one-time (currently grouped with recurring CRM).
- **Riley** (AI Agents page) says "this call's recorded" but web-call recording is off.
- **Inactive GHL agents** "Gabriel AI Asst. (DO NOT USE)" and "Luis AI Asst. (DO NOT USE)"
  should be deleted — the Gabriel one tells callers their cancellation was processed.
- Both Jessica agents say they never transfer calls but have transfer actions configured.
