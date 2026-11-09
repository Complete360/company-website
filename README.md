# Company Website

Version-controlled library of custom code snippets for the
Complete360 GoHighLevel site. Snippets are pasted directly
into GHL Custom Code blocks — this repo is not a standalone
deployable site.

## Structure
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
30 of 62 files have code. Files marked ⬜ contain only a
`PLACEHOLDER` comment — replace it with the page's custom code from GHL
and change the status here to ✅. Use Notes for
anything still to do on a page (🔁 = needs rebuild).

### Global (site-wide)

| File | GHL page | Status | Notes |
|---|---|---|---|
| `global/header.html` | Header (on every page) | ✅ Code in repo |  |
| `global/footer.html` | Footer (on every page) | ✅ Code in repo |  |
| `global/404.html` | 404 | ⬜ Placeholder |  |

### Home

| File | GHL page | Status | Notes |
|---|---|---|---|
| `home.html` | Main Home Page | ✅ Code in repo |  |

### Services

| File | GHL page | Status | Notes |
|---|---|---|---|
| `services/local-service-ads.html` | Local Service Ads | ✅ Code in repo | Up to date |
| `services/gbp-management.html` | Google Business Management | ✅ Code in repo | Up to date |
| `services/gbp-setup.html` | Google Business Profile Setup | ✅ Code in repo |  |
| `services/local-seo-booster.html` | SEO Booster | ✅ Code in repo | Up to date |
| `services/geo-fencing.html` | Geo Fencing | ✅ Code in repo | Up to date (header note added) |
| `services/google-ads.html` | Google Ads | ✅ Code in repo | Up to date |
| `services/meta-ads.html` | Meta Ads | ✅ Code in repo | Up to date |
| `services/google-social-posting.html` | Google Social Posting | ✅ Code in repo | Up to date |
| `services/meta-social-posting.html` | Meta Social Posting | ✅ Code in repo | Up to date |
| `services/reputation-management.html` | Reputation Management | ✅ Code in repo | Up to date |
| `services/procard.html` | Pro Card | ✅ Code in repo | Up to date |
| `services/websites-home.html` | Website Home | ✅ Code in repo | Up to date |
| `services/ai-employee.html` | AI Employee Website | ✅ Code in repo | Up to date |
| `services/local-display-network.html` | Local Display Network | ✅ Code in repo | Up to date |
| `services/dispensary.html` | Dispensary | ✅ Code in repo | Up to date |
| `services/payments.html` | Payments | ✅ Code in repo | Up to date |

### Pricing

| File | GHL page | Status | Notes |
|---|---|---|---|
| `pricing/website-pricing.html` | Website Pricing | ✅ Code in repo | Up to date |
| `pricing/saas-pricing.html` | SaaS Pricing | ⬜ Placeholder |  |

### Checkout

| File | GHL page | Status | Notes |
|---|---|---|---|
| `checkout/local-service-ads-checkout.html` | Local Service Ads Checkout | ⬜ Placeholder |  |
| `checkout/gbp-management-checkout.html` | GBP Management Checkout | ⬜ Placeholder |  |
| `checkout/gbp-setup-checkout.html` | GBP Setup Checkout | ⬜ Placeholder |  |
| `checkout/local-seo-booster-checkout.html` | Local SEO Checkout | ⬜ Placeholder |  |
| `checkout/geo-fencing-ctv-checkout.html` | Geo Fencing CTV Checkout | ⬜ Placeholder |  |
| `checkout/geo-fencing-mobile-checkout.html` | Geo Fencing Mobile Checkout | ⬜ Placeholder |  |
| `checkout/google-ads-checkout.html` | Google Ads Checkout | ⬜ Placeholder |  |
| `checkout/meta-ads-checkout.html` | Meta Ads Checkout | ⬜ Placeholder |  |
| `checkout/google-social-posting-checkout.html` | Google Social Posting Checkout | ⬜ Placeholder |  |
| `checkout/meta-social-posting-checkout.html` | Meta Social Posting Checkout | ⬜ Placeholder |  |
| `checkout/procard-checkout.html` | ProCard Checkout | ⬜ Placeholder |  |
| `checkout/website-checkout.html` | Website Checkout | ⬜ Placeholder |  |
| `checkout/ai-employee-checkout.html` | AI Employee Checkout | ⬜ Placeholder |  |
| `checkout/dispensary-checkout.html` | Dispensary Checkout | ⬜ Placeholder |  |
| `checkout/google-platinum-checkout.html` | Google Platinum Checkout | ⬜ Placeholder |  |
| `checkout/lifetime-deal-checkout.html` | Lifetime Deal Checkout | ⬜ Placeholder |  |
| `checkout/tier-1-plan-checkout.html` | Tier 1 Plan Check Out | ⬜ Placeholder |  |
| `checkout/tier-2-plan-checkout.html` | Tier 2 Plan Check Out | ⬜ Placeholder |  |
| `checkout/tier-3-plan-checkout.html` | Tier 3 Plan Check Out | ⬜ Placeholder |  |

### CRM platform

| File | GHL page | Status | Notes |
|---|---|---|---|
| `crm-platform/crm-home.html` | CRM Home Page | ✅ Code in repo |  |
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
| `company/faq.html` | FAQS | ✅ Code in repo | Up to date |
| `company/request-demo.html` | Request A Demo | ⬜ Placeholder | 🔁 Rebuild as custom HTML (current GHL page OK for now) |
| `company/schedule-demo.html` | Schedule A Demo | ⬜ Placeholder | Valid; may need future updates |
| `company/thank-you-after-schedule.html` | Thank You Page After Schedule | ⬜ Placeholder | 🔁 Rebuild needed (current GHL page OK for now) |
| `company/thank-you-after-form-fill.html` | Thank You Page After Form Fill | ⬜ Placeholder | 🔁 Rebuild needed (current GHL page OK for now) |
| `company/training.html` | Training | ✅ Code in repo | Up to date |
| `company/video-library.html` | Video Library | ✅ Code in repo |  |
| `company/link-tree.html` | Link Tree | ✅ Code in repo |  |

### Legal

| File | GHL page | Status | Notes |
|---|---|---|---|
| `legal/tos.html` | Terms of Service | ✅ Code in repo |  |
| `legal/privacy-policy.html` | Privacy Policy | ✅ Code in repo |  |
| `legal/return-policy.html` | Refund/Return Policy | ✅ Code in repo |  |

### Partners

| File | GHL page | Status | Notes |
|---|---|---|---|
| `partners/farmers-insurance.html` | Farmers Insurance | ✅ Code in repo |  |
