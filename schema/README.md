# Schema (structured data) for every page

One paste-ready file per page on complete360.org, in `schema/pages/` (same folders as
`ghl-snippets/`). Each file is a `<script type="application/ld+json">` block that tells
Google and AI tools what the page is: the company, the service, its FAQs, and so on.

## How to add one to a page in GHL
Schema goes in GHL's own schema editor, not Tracking Code and not the page snippet.
1. **Sites → Websites → Complete360 site → Edit** the page.
2. Left panel: **SEO & AI search optimization → Schema Markup** → open the editor → **JSON view**.
3. Select all and delete (this also clears old or auto-generated schema), then paste the JSON
   from the page's file: everything between the `<script>` tags, from the first `{` to the last `}`.
4. **Validate & Save**, then **Save and Publish** the page.
5. Check the live URL at https://validator.schema.org (Google's Rich Results Test only lists
   the business item).

What GHL accepts:
- Paste one complete block per page in JSON view. Don't use **+ Add schema** or Form view
  (Form view drops fields).
- Every item needs a single `@type`. A list like `["Organization", "ProfessionalService"]`
  makes GHL silently discard the save, so the company item is `ProfessionalService`.
- `@id` links between items (WebPage → WebSite → organization) work.
- The GHL reviews widget adds its own Organization/LocalBusiness items with the live rating.
  They're valid; leave them.

## Keeping it current
- FAQs and descriptions are pulled word for word from the snippets in `ghl-snippets/`.
  After changing a page's FAQ or hero text, run `python3 schema/build_schema.py`, commit,
  and re-paste that page's file into GHL.
- Company details (phones, address, hours, social profiles) live in `ORGANIZATION` at the
  top of `build_schema.py`. Change them there and every page picks it up.
- Pages whose code isn't in the repo yet get a basic description written for them. Once the
  page's code is added, re-run the script and their FAQs are picked up automatically.
- Prices are only included for SEO Services and AI Agents (from PROJECT.md). If those change,
  update `offers` in the script.

## Notes
- Google shows FAQ rich results mainly for government and health sites, so FAQ schema won't
  enlarge your Google listing. It still helps Google and AI tools read your answers.
- The schema repeats whatever the page says. Pages listed under Known issues in PROJECT.md
  ("cancel anytime", 30-day notice) will be repeated in their FAQ schema until the page is fixed.
- The logo is currently the favicon. Swap in the full logo URL in `ORGANIZATION` when you have it.

## Pages

Pages marked **⚠ HOLD** repeat outdated refund or cancellation wording from the page itself.
Don't paste them until the page is fixed and this script is re-run.

| Page | URL | Schema file | Types | FAQs | Status |
|---|---|---|---|---|---|
| Complete360: Digital Marketing for Local Businesses | `/` | `schema/pages/home.html` | WebPage, WebSite, FAQPage | 6 | ✅ |
| Local Service Ads | `/local-service-ads` | `schema/pages/services/local-service-ads.html` | WebPage, Service, FAQPage | 7 | ✅ |
| Google Business Profile Management | `/gbp-management` | `schema/pages/services/gbp-management.html` | WebPage, Service, FAQPage | 6 | ✅ |
| Google Business Profile Setup & Optimization | `/google-business-profile` | `schema/pages/services/gbp-setup.html` | WebPage, Service, FAQPage | 7 | ✅ |
| Local SEO Booster | `/local-seo-booster` | `schema/pages/services/local-seo-booster.html` | WebPage, Service, FAQPage | 7 | ✅ |
| SEO Services | `/seo-services` | `schema/pages/services/seo-services.html` | WebPage, Service, FAQPage | 8 | ✅ |
| Geo-Fencing Advertising | `/geo-fencing` | `schema/pages/services/geo-fencing.html` | WebPage, Service, FAQPage | 7 | ✅ |
| Google Ads (PPC) Management | `/google-ppc` | `schema/pages/services/google-ads.html` | WebPage, Service, FAQPage | 7 | ✅ |
| Meta Ads Management | `/meta-ads` | `schema/pages/services/meta-ads.html` | WebPage, Service, FAQPage | 7 | ✅ |
| Google Social Posting | `/google-social-posting` | `schema/pages/services/google-social-posting.html` | WebPage, Service, FAQPage | 6 | ✅ |
| Meta Social Posting | `/meta-social-posting` | `schema/pages/services/meta-social-posting.html` | WebPage, Service, FAQPage | 6 | ✅ |
| Reputation Management | `/reputation-management` | `schema/pages/services/reputation-management.html` | WebPage, Service, FAQPage | 10 | ✅ |
| Local Display Network | `/local-display-network` | `schema/pages/services/local-display-network.html` | WebPage, Service, FAQPage | 10 | ✅ |
| Dispensary Advertising | `/dispensary` | `schema/pages/services/dispensary.html` | WebPage, Service, FAQPage | 7 | ✅ |
| ProCard Digital Business Card | `/procard` | `schema/pages/services/procard.html` | WebPage, Service, FAQPage | 7 | ✅ |
| Website Design | `/websites-home` | `schema/pages/services/websites-home.html` | WebPage, Service, FAQPage | 5 | ✅ |
| AI Agents | `/ai-agents` | `schema/pages/services/ai-employee.html` | WebPage, Service, FAQPage | 6 | ✅ |
| Make a Payment | `/payments` | `schema/pages/services/payments.html` | WebPage, FAQPage | 5 | ✅ |
| Website Pricing | `/website-pricing` | `schema/pages/pricing/website-pricing.html` | WebPage, FAQPage | 7 | ✅ |
| Complete360 CRM Pricing | `/pricing` | `schema/pages/pricing/saas-pricing.html` | WebPage | — | ⬜ (basic schema until code is added) |
| Complete360 CRM | `/crm-home` | `schema/pages/crm-platform/crm-home.html` | WebPage, SoftwareApplication, FAQPage | 8 | ✅ |
| Capture Leads | `/capture` | `schema/pages/crm-platform/capture.html` | WebPage | — | ⬜ (basic schema until code is added) |
| Nurture Leads | `/nurture` | `schema/pages/crm-platform/nurture.html` | WebPage | — | ⬜ (basic schema until code is added) |
| Close Sales | `/close` | `schema/pages/crm-platform/close.html` | WebPage | — | ⬜ (basic schema until code is added) |
| All-in-One Inbox | `/all-in-one-inbox-feature-page` | `schema/pages/crm-platform/inbox.html` | WebPage | — | ⬜ (basic schema until code is added) |
| Online Booking Calendar | `/calendar-feature` | `schema/pages/crm-platform/calendar.html` | WebPage | — | ⬜ (basic schema until code is added) |
| Website Chat Widget | `/chat-widget-feature-page` | `schema/pages/crm-platform/chat-widget.html` | WebPage | — | ⬜ (basic schema until code is added) |
| Frequently Asked Questions | `/faq` | `schema/pages/company/faq.html` | FAQPage | 41 | ✅ |
| Contact Complete360 | `/contact-us` | `schema/pages/company/contact-us.html` | ContactPage, FAQPage | 5 | ✅ |
| Schedule a Free Strategy Call | `/schedule-demo` | `schema/pages/company/schedule-demo.html` | WebPage | — | ⬜ (basic schema until code is added) |
| Request a Demo | `/request-a-demo` | `schema/pages/company/request-demo.html` | WebPage | — | ⬜ (basic schema until code is added) |
| Training | `/training` | `schema/pages/company/training.html` | — | — | No schema (noindex instead) |
| Video Library | `/video-library` | `schema/pages/company/video-library.html` | CollectionPage | — | ✅ |
| Complete360 Links | `/links` | `schema/pages/company/link-tree.html` | WebPage | — | ✅ |
| Thank You | `/thank-you-for-demo` | `schema/pages/company/thank-you-after-schedule.html` | — | — | No schema (noindex instead) |
| Thank You | `/thank-you-form` | `schema/pages/company/thank-you-after-form-fill.html` | — | — | No schema (noindex instead) |
| Page Not Found | `/404` | `schema/pages/global/404.html` | — | — | No schema (noindex instead) |
| Terms of Service | `/tos` | `schema/pages/legal/tos.html` | WebPage | — | ✅ |
| Privacy Policy | `/privacy-policy` | `schema/pages/legal/privacy-policy.html` | WebPage | — | ✅ |
| Return & Refund Policy | `/return-policy` | `schema/pages/legal/return-policy.html` | WebPage | — | ✅ |
| Farmers Insurance Agent Program | `/farmers-insurance` | `schema/pages/partners/farmers-insurance.html` | WebPage, FAQPage | 8 | ✅ |
| Checkout: Local Service Ads | `/lsa-checkout` | `schema/pages/checkout/local-service-ads.html` | CheckoutPage, FAQPage | 8 | ✅ |
| Checkout: Google Business Profile Management | `/gbp-management-checkout` | `schema/pages/checkout/gbp-management.html` | CheckoutPage, FAQPage | 7 | ✅ |
| Checkout: Google Business Profile Setup | `/gbp-setup-checkout` | `schema/pages/checkout/gbp-setup.html` | CheckoutPage, FAQPage | 8 | ✅ |
| Checkout: Google Platinum Package | `/google-platinum-checkout` | `schema/pages/checkout/google-platinum.html` | CheckoutPage, FAQPage | 8 | ✅ |
| Checkout: Local SEO Booster | `/local-seo-checkout` | `schema/pages/checkout/local-seo-booster.html` | CheckoutPage, FAQPage | 9 | ✅ |
| Checkout: Google Ads (PPC) Management | `/google-ads-checkout` | `schema/pages/checkout/google-ads-checkout.html` | CheckoutPage | — | ⬜ (basic schema until code is added) |
| Checkout: Meta Ads Management | `/meta-checkout` | `schema/pages/checkout/meta-ads.html` | CheckoutPage | — | ✅ |
| Checkout: Geo-Fencing (Mobile) | `/geo-mobile-checkout` | `schema/pages/checkout/geo-fencing-mobile-checkout.html` | CheckoutPage | — | ⬜ (basic schema until code is added) |
| Checkout: Geo-Fencing (Connected TV) | `/geo-ctv-checkout` | `schema/pages/checkout/geo-fencing-ctv-checkout.html` | CheckoutPage | — | ⬜ (basic schema until code is added) |
| Checkout: Google Social Posting | `/google-social-checkout` | `schema/pages/checkout/google-social-posting.html` | CheckoutPage | — | ✅ |
| Checkout: Meta Social Posting | `/meta-social-checkout` | `schema/pages/checkout/meta-social-posting.html` | CheckoutPage | — | ✅ |
| Checkout: ProCard | `/procard-checkout` | `schema/pages/checkout/procard-checkout.html` | CheckoutPage | — | ⬜ (basic schema until code is added) |
| Checkout: Website Design | `/website-checkout` | `schema/pages/checkout/website-checkout.html` | CheckoutPage | — | ⬜ (basic schema until code is added) |
| Checkout: Dispensary Advertising | `/dispensary-checkout` | `schema/pages/checkout/dispensary-checkout.html` | CheckoutPage | — | ⬜ (basic schema until code is added) |
| Checkout: AI Agents | `/ai-checkout` | `schema/pages/checkout/ai-employee-checkout.html` | CheckoutPage | — | ⬜ (basic schema until code is added) |
| Checkout: Complete360 CRM Lifetime Deal | `/lifetime-checkout` | `schema/pages/checkout/lifetime-deal-checkout.html` | CheckoutPage | — | ⬜ (basic schema until code is added) |
| Checkout: Complete360 CRM Tier 1 plan | `/checkout-1` | `schema/pages/checkout/tier-1-plan-checkout.html` | CheckoutPage | — | ⬜ (basic schema until code is added) |
| Checkout: Complete360 CRM Tier 2 plan | `/checkout-2` | `schema/pages/checkout/tier-2-plan-checkout.html` | CheckoutPage | — | ⬜ (basic schema until code is added) |
| Checkout: Complete360 CRM Tier 3 plan | `/checkout-3` | `schema/pages/checkout/tier-3-plan-checkout.html` | CheckoutPage | — | ⬜ (basic schema until code is added) |
