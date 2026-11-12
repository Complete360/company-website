# Company Website

Version-controlled library of custom code snippets for the
Complete360 GoHighLevel site. Snippets are pasted directly
into GHL Custom Code blocks — this repo is not a standalone
deployable site.

## Start here
AI agents and new contributors: read `PROJECT.md` first.

## Structure
`ai-agents/` holds the prompts for every GHL AI agent (see its README).

`schema/` holds paste-ready structured data (JSON-LD) for every page, generated from the snippets (see its README).

`ghl-meta/` holds copy/paste GHL SEO meta data (title, description, slug, canonical) for new pages, one file per page.

All custom code blocks live in `ghl-snippets/`:

- `global/` — site-wide pieces (header, footer, 404)
- `home.html` — home page
- `services/` — one page per service
- `industries/` — industry pages, live under `/industries/[industry]` (build worksheet: INDUSTRY-PAGES-WORKSHEET)
- `pricing/` — pricing pages
- `checkout/` — checkout pages
- `crm-platform/` — CRM platform home and feature pages
- `company/` — demo, contact, FAQ, thank-you pages, training and resources
- `legal/` — terms of service, privacy policy, return policy
- `partners/` — partner landing pages

## Page checklist
48 of 65 pages have code. Multi-snippet pages (checkouts) are a folder of
numbered snippets, pasted around GHL's native order form in order. Files marked ⬜ contain only a
`PLACEHOLDER` comment — replace it with the page's custom code from GHL
and change the status here to ✅. Use Notes for
anything still to do on a page (🔁 = needs rebuild).

### Global (site-wide)

| File | GHL page | Status | Notes |
|---|---|---|---|
| `global/header.html` | Header (on every page) | ✅ Code in repo | v2.2.1: imported live v2.1, then added SEO Services; mobile "All AI Agents" icon fixed (Pro-only icon) (Solutions + Pricing, desktop + mobile), AI prices $399/$599, "no per-minute AI fees". Paste into GHL global header. Open: Paid Lead Gen rail "From $499/mo" |
| `global/footer.html` | Footer (on every page) | ✅ Code in repo | v1.7.3: pills glued to the label; Platform Overview icon fixed (was a Pro-only icon) (v1.7 live Nov 11). Paste into GHL global footer |
| `global/404.html` | 404 | ⬜ Placeholder |  |

### Home

| File | GHL page | Status | Notes |
|---|---|---|---|
| `home.html` | Main Home Page | ✅ Code in repo |  |

### Services

| File | GHL page | Status | Notes |
|---|---|---|---|
| `services/local-service-ads.html` | Local Service Ads | ✅ Code in repo | v1.6 live in GHL (Nov 10) — schema still to paste |
| `services/gbp-management.html` | Google Business Management | ✅ Code in repo | v1.3.3 live in GHL (Nov 10) — schema still to paste |
| `services/gbp-setup.html` | Google Business Profile Setup | ✅ Code in repo | Up to date |
| `services/local-seo-booster.html` | SEO Booster | ✅ Code in repo | v2.7 live in GHL (Nov 10) — schema still to paste |
| `services/geo-fencing.html` | Geo Fencing | ✅ Code in repo | v1.1 live in GHL (Nov 10) — schema still to paste |
| `services/google-ads.html` | Google Ads | ✅ Code in repo | v2.6 live in GHL (Nov 10) — schema still to paste |
| `services/meta-ads.html` | Meta Ads | ✅ Code in repo | v2.3 live in GHL (Nov 10) — schema still to paste |
| `services/google-social-posting.html` | Google Social Posting | ✅ Code in repo | v1.2 live in GHL (Nov 10) — schema still to paste |
| `services/meta-social-posting.html` | Meta Social Posting | ✅ Code in repo | v1.2 live in GHL (Nov 10) — schema still to paste |
| `services/reputation-management.html` | Reputation Management | ✅ Code in repo | v1.8 live in GHL (Nov 10) — schema still to paste |
| `services/procard.html` | Pro Card | ✅ Code in repo | Up to date |
| `services/websites-home.html` | Website Home | ✅ Code in repo | Up to date |
| `services/ai-employee.html` | AI Employee Website | ✅ Code in repo | v1.14 live in GHL (Nov 10) — schema still to paste |
| `services/local-display-network.html` | Local Display Network | ✅ Code in repo | Up to date |
| `services/dispensary.html` | Dispensary | ✅ Code in repo | Up to date |
| `services/seo-services.html` | SEO Services (new page — create in GHL) | ✅ Code in repo | v1.4 live in GHL; not in nav yet; checkout page created, snippets to build |
| `services/payments.html` | Payments | ✅ Code in repo | v1.1 live in GHL (Nov 10) — schema still to paste |

### Industries

Each industry page has three files: the snippet here, `ghl-meta/industries/[slug].md` (meta data for GHL),
and `schema/pages/industries/[slug].html` (schema, pasted in one batch after every industry page is live).

| File | GHL page | Status | Notes |
|---|---|---|---|
| `industries/hvac.html` | HVAC Marketing (new page at /industries/hvac) | ✅ Code in repo | v1.0: images to make (`hvac-hero`, `hvac-on-the-job`), then create the page in GHL, paste, complete meta data from `ghl-meta/industries/hvac.md`, publish. Breadcrumb links to /industries (hub not built yet). Schema waits for the batch. |

### Pricing

| File | GHL page | Status | Notes |
|---|---|---|---|
| `pricing/website-pricing.html` | Website Pricing | ✅ Code in repo | Nov 10 update live in GHL (Nov 10) — schema still to paste |
| `pricing/saas-pricing.html` | SaaS Pricing | ⬜ Placeholder |  |

### Checkout

All checkout pages are set to **noindex** in GHL and get no schema (decided Nov 11, 2026).

| File | GHL page | Status | Notes |
|---|---|---|---|
| `checkout/local-service-ads/` (4 snippets: `1-pricing`, `2-order-summary`, `3-reviews`, `4-faq`) | Local Service Ads Checkout | ✅ Code in repo | v1.1 (Nov 11): cancellation/refund copy fixed; "money back" -> credits. Open: "Performance Promise" wording, background-check cost and setup-fee waiver claims; "Tucson businesses" headline. Paste into GHL. |
| `checkout/gbp-management/` (4 snippets: `1-pricing`, `2-order-summary`, `3-reviews`, `4-faq`) | GBP Management Checkout | ✅ Code in repo | Repo v1.1 (Nov 11): 30-day guarantee replaced with the Terms' guarantee; cancellation/refund and "GBP" fixed. Open: confirm the guarantee wording. Paste into GHL. |
| `checkout/gbp-setup/` (4 snippets: `1-pricing`, `2-order-summary`, `3-reviews`, `4-faq`) | GBP Setup Checkout | ✅ Code in repo | v1.1 (Nov 11): refund now non-refundable from purchase; "GBP" fixed. Open: "Quality Promise"/keep-working wording (management review); "hundreds of profiles" claim. Paste into GHL. |
| `checkout/local-seo-booster/` (4 snippets: `1-pricing`, `2-order-summary`, `3-reviews`, `4-faq`) | Local SEO Checkout | ✅ Code in repo | v1.1 (Nov 11): cancellation/annual refund copy, ranking answer and "GBP" fixed. Open: "Tucson businesses" headline. Paste into GHL. |
| `checkout/geo-fencing-ctv/` (4 snippets: `1-pricing`, `2-order-summary`, `3-reviews`, `4-faq`) | Geo Fencing CTV Checkout | ✅ Code in repo | v1.0/v1.1 (Nov 11): imported from live GHL; typos fixed ("$1,390" -> "$1,399", "CTVads"). Prices/CPMs match /geo-fencing. Open: "#1 Location Intelligence Platform". Paste into GHL. |
| `checkout/geo-fencing-mobile/` (4 snippets: `1-pricing`, `2-order-summary`, `3-reviews`, `4-faq`) | Geo Fencing Mobile Checkout | ✅ Code in repo | v1.0/v1.1 (Nov 11): imported from live GHL; 10-day notice + prepaid non-refundable; 12-mo effective $208.30 -> $209.30. Prices match /geo-fencing. Open: ad spend separate vs 8,000 impressions included; "#1 Location Intelligence Platform"; "completely legal" competitor targeting. Paste into GHL. |
| `checkout/google-ads/` (4 snippets: `1-pricing`, `2-order-summary`, `3-reviews`, `4-faq`) | Google Ads Checkout | ✅ Code in repo | Repo v1.1 (Nov 11): imported from live GHL; 90-day guarantee removed (matches /google-ads v2.6); 10-day notice; prepaid non-refundable from purchase. Prices match. ⚠ Strip the internal HTML comments (agent-only $299 floor) before pasting — comments show in page source. Open: "don't auto-renew" vs Terms; Most Popular tier (6-mo here, 12-mo on page). Paste into GHL. |
| `checkout/meta-ads/` (4 snippets: `1-pricing`, `2-order-summary`, `3-reviews`, `4-faq`) | Meta Ads Checkout | ✅ Code in repo | v1.1 (Nov 11): 90-day guarantee removed (matches /meta-ads v2.3); 10-day notice; non-refundable from purchase. Older c360wr-/c360wf- styling. Paste into GHL. |
| `checkout/google-social-posting/` (4 snippets: `1-pricing`, `2-order-summary`, `3-reviews`, `4-faq`) | Google Social Posting Checkout | ✅ Code in repo | v1.1 (Nov 11): 30-day guarantee removed; 10-day notice; 147 reviews; "GBP"/vendor name fixed. ⚠ Open: 6/12-month prices ($774/$1,308) vs service page ($715/$1,252). Older c360wr-/c360wf- styling. Paste after prices are settled. |
| `checkout/meta-social-posting/` (4 snippets: `1-pricing`, `2-order-summary`, `3-reviews`, `4-faq`) | Meta Social Posting Checkout | ✅ Code in repo | v1.1 (Nov 11): 30-day guarantee removed; 10-day notice; 147 reviews. Older c360wr-/c360wf- styling. Paste into GHL. |
| `checkout/procard/` (4 snippets: `1-pricing`, `2-order-summary`, `3-reviews`, `4-faq`) | ProCard Checkout | ✅ Code in repo | v1.0/v1.1 (Nov 11): imported from live GHL; reviews 144+ -> 147. Prices match /procard. Open: "lifetime license / own it forever" wording; free minor edits promise; "Tucson businesses" headline. Older c360wr-/c360wf- styling. Paste into GHL. |
| `checkout/website/` (4 snippets: `1-pricing`, `2-order-summary`, `3-reviews`, `4-faq`) | Website Checkout | ✅ Code in repo | v1.0/v1.1 (Nov 11): imported from live GHL; 30-day guarantee removed; 147 reviews; cancel FAQ now matches /website-pricing (10-day notice). Prices match. Open: page counts (5/10/15+ vs 4/6/8–9 on /website-pricing); "one-time setup" vs deposit + final payment; "own your domain". Older c360wr-/c360wf- styling. Paste into GHL. |
| `checkout/ai-agents/` (4 snippets: `1-pricing`, `2-order-summary`, `3-reviews`, `4-faq`) | AI Employee Checkout | ✅ Code in repo | Repo v1.1 (Nov 11): imported from live GHL (/ai-checkout); per-minute conflict resolved to PROJECT.md wording (unlimited AI usage, phone line & carrier billed separately); 30-day guarantee removed; 10-day notice; annual cancel FAQ per Terms; 147 reviews. Prices match /ai-agents. Pricing snippet carries its own Custom Quote modal + form_embed.js. Older-style c360ai- recap/FAQ. Paste into GHL. |
| `checkout/seo-services/` (4 snippets: `1-pricing`, `2-order-summary`, `3-reviews`, `4-faq`) | SEO Services Checkout (/seo-services-checkout) | ✅ Code in repo | v1.0 live in GHL (Nov 11) — schema still to paste. Built on the Platinum checkout layout with /seo-services v1.4 content ($599/mo, $5,990/yr). Next: point the /seo-services Get Started buttons here. |
| `checkout/dispensary/` (4 snippets: `1-pricing`, `2-order-summary`, `3-reviews`, `4-faq`) | Dispensary Checkout | ✅ Code in repo | v1.0/v1.1 (Nov 11): imported from live GHL; reviews 144+ -> 147; billing FAQ adds 10-day notice + annual non-refundable. Prices match /dispensary. ⚠ Open: legal review of "fully legal"/"no platform policy violations" and VFW/Legion naming; ad spend separate vs fixed impressions; CTV/desktop formats vs cards; "priced slightly higher" monthly. Older c360wr-/c360wf- styling. |
| `checkout/google-platinum/` (4 snippets: `1-pricing`, `2-order-summary`, `3-reviews`, `4-faq`) | Google Platinum Checkout | ✅ Code in repo | v1.1 (Nov 11): cancellation/refund/"GBP" copy fixed. Open: Reputation Management in the bundle vs PROJECT.md; "won't be double-billed" upgrade promise; "Tucson businesses" reviews headline. Paste into GHL. |
| `checkout/lifetime-deal-checkout.html` | Lifetime Deal Checkout | ⬜ Placeholder |  |
| `checkout/tier-1-plan-checkout.html` | Tier 1 Plan Check Out | ⬜ Placeholder |  |
| `checkout/tier-2-plan-checkout.html` | Tier 2 Plan Check Out | ⬜ Placeholder |  |
| `checkout/tier-3-plan-checkout.html` | Tier 3 Plan Check Out | ⬜ Placeholder |  |

### CRM platform

| File | GHL page | Status | Notes |
|---|---|---|---|
| `crm-platform/crm-home.html` | CRM Home Page | ✅ Code in repo | v2.10: money-back guarantee + "cancel anytime" removed — paste into GHL. Open: trial vs 10-day rule |
| `crm-platform/capture.html` | Step 1 - Capture Leads | ⬜ Placeholder |  |
| `crm-platform/nurture.html` | Step 2 - Nurture Leads | ⬜ Placeholder |  |
| `crm-platform/close.html` | Step 3 - Close Sales | ⬜ Placeholder |  |
| `crm-platform/inbox.html` | All In One Inbox Feature Page | ⬜ Placeholder |  |
| `crm-platform/calendar.html` | Calendar Feature Page | ⬜ Placeholder |  |
| `crm-platform/chat-widget.html` | Chat Widget Feature Page | ⬜ Placeholder |  |
| `crm-platform/forms.html` | — | ⬜ Placeholder |  |

### Company

| File | GHL page | Status | Notes |
|---|---|---|---|
| `company/contact-us.html` | Contact Us Form | ✅ Code in repo | Up to date |
| `company/faq.html` | FAQS | ✅ Code in repo | v2.4 live in GHL (Nov 10) — schema still to paste |
| `company/request-demo.html` | Request A Demo | ⬜ Placeholder | 🔁 Rebuild as custom HTML (current GHL page OK for now) |
| `company/schedule-demo.html` | Schedule A Demo | ⬜ Placeholder | Valid; may need future updates |
| `company/thank-you-after-schedule.html` | Thank You Page After Schedule | ⬜ Placeholder | 🔁 Rebuild needed (current GHL page OK for now) |
| `company/thank-you-after-form-fill.html` | Thank You Page After Form Fill | ⬜ Placeholder | 🔁 Rebuild needed (current GHL page OK for now) |
| `company/training.html` | Training | ✅ Code in repo | v1.2 live in GHL (Nov 10) — schema still to paste |
| `company/video-library.html` | Video Library | ✅ Code in repo |  |
| `company/link-tree.html` | Link Tree | ✅ Code in repo |  |

### Legal

| File | GHL page | Status | Notes |
|---|---|---|---|
| `legal/tos.html` | Terms of Service | ✅ Code in repo | v2.1 live in GHL (Nov 10) — schema still to paste |
| `legal/privacy-policy.html` | Privacy Policy | ✅ Code in repo |  |
| `legal/return-policy.html` | Refund/Return Policy | ✅ Code in repo | v2.1 live in GHL (Nov 10) — schema still to paste |

### Partners

| File | GHL page | Status | Notes |
|---|---|---|---|
| `partners/farmers-insurance.html` | Farmers Insurance | ✅ Code in repo |  |
