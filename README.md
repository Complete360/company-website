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

All custom code blocks live in `ghl-snippets/`:

- `global/` — site-wide pieces (header, footer, 404)
- `home.html` — home page
- `services/` — one page per service
- `pricing/` — pricing pages
- `checkout/` — checkout pages
- `crm-platform/` — CRM platform home and feature pages
- `company/` — demo, contact, FAQ, thank-you pages, training and resources
- `legal/` — terms of service, privacy policy, return policy
- `partners/` — partner landing pages

## Page checklist
38 of 63 pages have code. Multi-snippet pages (checkouts) are a folder of
numbered snippets, pasted around GHL's native order form in order. Files marked ⬜ contain only a
`PLACEHOLDER` comment — replace it with the page's custom code from GHL
and change the status here to ✅. Use Notes for
anything still to do on a page (🔁 = needs rebuild).

### Global (site-wide)

| File | GHL page | Status | Notes |
|---|---|---|---|
| `global/header.html` | Header (on every page) | ✅ Code in repo | v1.9.5: AI menu says "no per-minute AI fees" — compare with live header (v1.9.4 not in repo) before pasting |
| `global/footer.html` | Footer (on every page) | ✅ Code in repo |  |
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

### Pricing

| File | GHL page | Status | Notes |
|---|---|---|---|
| `pricing/website-pricing.html` | Website Pricing | ✅ Code in repo | Nov 10 update live in GHL (Nov 10) — schema still to paste |
| `pricing/saas-pricing.html` | SaaS Pricing | ⬜ Placeholder |  |

### Checkout

| File | GHL page | Status | Notes |
|---|---|---|---|
| `checkout/local-service-ads/` (4 snippets: `1-pricing`, `2-order-summary`, `3-reviews`, `4-faq`) | Local Service Ads Checkout | ✅ Code in repo | v1.0 imported as-is from live GHL (/lsa-checkout). 🔁 Fix next: "cancel anytime", refund wording, "money back from Google", "Performance Promise" vs legal guarantee; confirm background-check cost and setup-fee waiver |
| `checkout/gbp-management/` (4 snippets: `1-pricing`, `2-order-summary`, `3-reviews`, `4-faq`) | GBP Management Checkout | ✅ Code in repo | Imported as-is from live GHL (/gbp-management-checkout); snippets keep their own live version headers (v2 / v2.2 / v2). 🔁 Fix next: "30-Day Satisfaction Guarantee" vs legal guarantee, "cancel anytime", refund wording, "GBP" in copy |
| `checkout/gbp-setup/` (4 snippets: `1-pricing`, `2-order-summary`, `3-reviews`, `4-faq`) | GBP Setup Checkout | ✅ Code in repo | v1.0 imported as-is from live GHL (/gbp-setup-checkout). 🔁 Fix next: refund wording ("once the discovery call is completed"), "Quality Promise"/satisfaction wording vs guarantee scope, "GBP" in copy |
| `checkout/local-seo-booster/` (4 snippets: `1-pricing`, `2-order-summary`, `3-reviews`, `4-faq`) | Local SEO Checkout | ✅ Code in repo | v1.0 imported as-is from live GHL (/local-seo-checkout). 🔁 Fix next: "cancel anytime", annual no-refund wording, "GBP" in copy, ranking promise in FAQ |
| `checkout/geo-fencing-ctv-checkout.html` | Geo Fencing CTV Checkout | ⬜ Placeholder |  |
| `checkout/geo-fencing-mobile-checkout.html` | Geo Fencing Mobile Checkout | ⬜ Placeholder |  |
| `checkout/google-ads-checkout.html` | Google Ads Checkout | ⬜ Placeholder |  |
| `checkout/meta-ads-checkout.html` | Meta Ads Checkout | ⬜ Placeholder |  |
| `checkout/google-social-posting/` (4 snippets: `1-pricing`, `2-order-summary`, `3-reviews`, `4-faq`) | Google Social Posting Checkout | ✅ Code in repo | v1.0 imported as-is from live GHL (/google-social-checkout). ⚠ 6/12-month prices ($774/$1,308) differ from the service page ($715/$1,252). 🔁 Fix next: "30 days' notice", 30-day guarantee, "144+" reviews, "Yext" named, "GBP" in copy; snippets 2 and 4 use older c360wr-/c360wf- styling |
| `checkout/meta-social-posting/` (4 snippets: `1-pricing`, `2-order-summary`, `3-reviews`, `4-faq`) | Meta Social Posting Checkout | ✅ Code in repo | v1.0 imported as-is from live GHL (/meta-social-checkout). 🔁 Fix next: "cancel anytime" / "30 days' notice", 30-day guarantee, "144+" reviews; snippets 2 and 4 use older c360wr-/c360wf- styling |
| `checkout/procard-checkout.html` | ProCard Checkout | ⬜ Placeholder |  |
| `checkout/website-checkout.html` | Website Checkout | ⬜ Placeholder |  |
| `checkout/ai-employee-checkout.html` | AI Employee Checkout | ⬜ Placeholder |  |
| `checkout/dispensary-checkout.html` | Dispensary Checkout | ⬜ Placeholder |  |
| `checkout/google-platinum/` (4 snippets: `1-pricing`, `2-order-summary`, `3-reviews`, `4-faq`) | Google Platinum Checkout | ✅ Code in repo | v1.0 imported as-is from live GHL. 🔁 Fix next: "cancel anytime", refund wording, "GBP" in copy, bundle contents vs PROJECT.md |
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
