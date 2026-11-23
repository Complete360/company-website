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
74 of 91 pages have code. Multi-snippet pages (checkouts) are a folder of
numbered snippets, pasted around GHL's native order form in order. Files marked ⬜ contain only a
`PLACEHOLDER` comment — replace it with the page's custom code from GHL
and change the status here to ✅. Use Notes for
anything still to do on a page (🔁 = needs rebuild).

### Global (site-wide)

| File | GHL page | Status | Notes |
|---|---|---|---|
| `global/header.html` | Header (on every page) | ✅ Code in repo | **v2.5: 🔁 paste into GHL** — 1440px width site-wide (all non-checkout pages + header bar/mega menu). **v2.4: 🔁 paste into GHL** — site-wide motion (smooth anchor scrolling + eased FAQ open/close on every page) and a site-wide 1440px/64px width rule for all industry pages (v2.3). No per-page re-paste needed. v2.2.1: imported live v2.1, then added SEO Services; mobile "All AI Agents" icon fixed (Pro-only icon) (Solutions + Pricing, desktop + mobile), AI prices $399/$599, "no per-minute AI fees". Paste into GHL global header. Open: Paid Lead Gen rail "From $499/mo" |
| `global/footer.html` | Footer (on every page) | ✅ Code in repo | **v1.8: 🔁 paste into GHL** — 1440px/64px, lines up with header and content. v1.7.3: pills glued to the label; Platform Overview icon fixed (was a Pro-only icon) (v1.7 live Nov 11). Paste into GHL global footer |
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
| `services/geo-fencing.html` | Geo Fencing | ✅ Code in repo | **🔁 paste into GHL** — 1440px width standard (2026-11-23). v1.1 live in GHL (Nov 10) — schema still to paste |
| `services/google-ads.html` | Google Ads | ✅ Code in repo | v2.6 live in GHL (Nov 10) — schema still to paste |
| `services/meta-ads.html` | Meta Ads | ✅ Code in repo | v2.3 live in GHL (Nov 10) — schema still to paste |
| `services/google-social-posting.html` | Google Social Posting | ✅ Code in repo | v1.2 live in GHL (Nov 10) — schema still to paste |
| `services/meta-social-posting.html` | Meta Social Posting | ✅ Code in repo | v1.2 live in GHL (Nov 10) — schema still to paste |
| `services/reputation-management.html` | Reputation Management | ✅ Code in repo | v1.8 live in GHL (Nov 10) — schema still to paste |
| `services/procard.html` | Pro Card | ✅ Code in repo | Up to date |
| `services/websites-home.html` | Website Home | ✅ Code in repo | Up to date |
| `services/ai-employee.html` | AI Employee Website | ✅ Code in repo | v1.14 live in GHL (Nov 10) — schema still to paste |
| `services/local-display-network.html` | Local Display Network | ✅ Code in repo | Up to date |
| `services/dispensary.html` | Dispensary | ✅ Code in repo | **🔁 paste into GHL** — 1440px width standard (2026-11-23). Up to date |
| `services/seo-services.html` | SEO Services (new page — create in GHL) | ✅ Code in repo | v1.4 live in GHL; not in nav yet; checkout page created, snippets to build |
| `services/payments.html` | Payments | ✅ Code in repo | v1.1 live in GHL (Nov 10) — schema still to paste |

### Industries

Each industry page has three files: the snippet here, `ghl-meta/industries/[slug].md` (meta data for GHL),
and `schema/pages/industries/[slug].html` (schema, pasted in one batch after every industry page is live).

| File | GHL page | Status | Notes |
|---|---|---|---|
| `industries/industries-hub.html` | Industries (new hub page at /industries) | ✅ Code in repo | **v1.9: 🔁 create page in GHL + paste + meta data** (`ghl-meta/industries/industries-hub.md`). Publish before or with the industry pages (their breadcrumbs link here). Image to fill: `indhub-hero`. Medicare card links to /schedule-demo until approved (search "SWAP WHEN LIVE"). Landscaping not in the directory yet. Schema: CollectionPage + ItemList read from the hub's own links + FAQ (batch paste). |
| `industries/landscaping.html` | Landscaping & Hardscaping Marketing (new page at /industries/landscaping) | ✅ Code in repo | **🔁 create page in GHL + paste + meta data** (new). **v1.1** (1440px/64px width standard). v1.0: Wave 6. Same dimensions as the other industry pages, light-blue palette, own layout (bento hero with both photos and a code-built paver tile, plant-tag reality cards, material swatch board plan, stepping-stone journey, leaf badges + reviews widget, navy paver-pattern CTA band, FAQ with stone markers). Positioned for design-build and hardscape work; links maintenance companies to /industries/lawn-care. Plan (draft) to confirm with Jared. Images to make (`land-hero`, `land-on-the-job`), then create the page in GHL, paste, complete meta data from `ghl-meta/industries/landscaping.md`, publish. Schema waits for the batch. |
| `industries/handyman.html` | Handyman Marketing (new page at /industries/handyman) | ✅ Code in repo | v1.0: same dimensions as the other industry pages, light-blue palette, own layout (hero photo framed by a framing-square ruler, one big to-do notepad beside the second photo, pegboard plan with hanging service cards in three zones, 2x2 side-by-side journey cards, stats on a measuring tape + reviews widget, navy CTA with a "today's list" checklist, FAQ with pegboard markers). Platinum co-leads with reviews. Plan (draft, worksheet v1.4 Wave 5) to confirm with Jared. Images to make (`handy-hero`, `handy-on-the-job`), then create the page in GHL, paste, complete meta data from `ghl-meta/industries/handyman.md`, publish. Schema waits for the batch. |
| `industries/movers.html` | Moving Company Marketing (new page at /industries/movers) | ✅ Code in repo | v1.0: same dimensions as the other industry pages, light-blue palette, own layout (navy text panel left with the photo filling the right and a "move booked" card bridging them, "month in moving" bar strip above four pain cards, shipping-label plan (start here full width, grow with and also available side by side), tear-off calendar journey, round stat stickers on the reviews card, sky CTA with photo left, FAQ with truck markers). Platinum co-leads with reviews. Plan (draft, worksheet v1.4 Wave 5) to confirm with Jared. Images to make (`move-hero`, `move-on-the-job`), then create the page in GHL, paste, complete meta data from `ghl-meta/industries/movers.md`, publish. Schema waits for the batch. |
| `industries/junk-removal.html` | Junk Removal Marketing (new page at /industries/junk-removal) | ✅ Code in repo | v1.0: same dimensions as the other industry pages, light-blue palette, own layout (two-photo collage hero with booking chip, taped moving-box reality cards beside a heading column, code-built truck loaded with the plan plus three load cards, four steps beside one phone screen, reviews card with header bar, navy CTA with action cards and office hours, FAQ with box markers). Both images are in the hero. LSA-led. Plan (draft, worksheet v1.4 Wave 5) to confirm with Jared. Images to make (`junk-hero`, `junk-on-the-job`), then create the page in GHL, paste, complete meta data from `ghl-meta/industries/junk-removal.md`, publish. Schema waits for the batch. |
| `industries/tree-service.html` | Tree Service Marketing (new page at /industries/tree-service) | ✅ Code in repo | v1.0: same dimensions as the other industry pages, light-blue palette, own layout (three-column hero with tall photo and "calls we help you win" list, four-season reality strip, roots / trunk / branches plan layers, zigzag journey rows, tree-ring rating badge + reviews widget, bordered CTA card, FAQ in two groups). Platinum co-leads with reviews. Plan (draft, worksheet v1.4 Wave 5) to confirm with Jared. Images to make (`tree-hero`, `tree-on-the-job`), then create the page in GHL, paste, complete meta data from `ghl-meta/industries/tree-service.md`, publish. Schema waits for the batch. |
| `industries/appliance-repair.html` | Appliance Repair Marketing (new page at /industries/appliance-repair) | ✅ Code in repo | v1.0: same dimensions as the other industry pages, light-blue palette, own layout (photo band with an overlapping headline card and steel control-panel strip, knob-dial reality cards, EnergyGuide-style "Marketing Guide" plan label, four-column dispatch-board journey, stat chips + reviews widget, three-panel CTA with office hours, FAQ with a help bar). LSA-led. Plan (draft, worksheet v1.4 Wave 5) to confirm with Jared. Images to make (`appl-hero`, `appl-on-the-job`), then create the page in GHL, paste, complete meta data from `ghl-meta/industries/appliance-repair.md`, publish. Schema waits for the batch. |
| `industries/water-damage-restoration.html` | Water Damage Restoration Marketing (new page at /industries/water-damage-restoration) | ✅ Code in repo | **v1.1: 🔁 paste into GHL** (1440px/64px width standard). v1.0: same dimensions as the other industry pages, light-blue palette, own layout (hero with the photo bleeding off the right edge and three quick facts, floor-plan moisture map beside numbered readings, vertical-tab plan, stacked journey rows, reviews heading + stats in one row with full-width widget, centered navy CTA with photo strip, FAQ in two card columns). LSA-led. Plan (draft, worksheet v1.4 Wave 5) to confirm with Jared. Images to make (`water-hero`, `water-on-the-job`), then create the page in GHL, paste, complete meta data from `ghl-meta/industries/water-damage-restoration.md`, publish. Schema waits for the batch. |
| `industries/locksmiths.html` | Locksmith Marketing (new page at /industries/locksmiths) | ✅ Code in repo | v1.1: same dimensions as the other industry pages, light-blue palette, own layout (white hero with a square photo and lock-screen notification stack, key-cut reality cards, master-key-system plan tree, customer / your-business swimlanes, stat line + reviews widget, navy CTA band with a framed photo on the right, FAQ with key markers). LSA-led; locksmith ads need Google's Advanced Verification (no pre-badge ads). Plan (draft, worksheet v1.4 Wave 5) to confirm with Jared. Images to make (`lock-hero`, `lock-on-the-job`), then create the page in GHL, paste, complete meta data from `ghl-meta/industries/locksmiths.md`, publish. Schema waits for the batch. |
| `industries/garage-door-repair.html` | Garage Door Repair Marketing (new page at /industries/garage-door-repair) | ✅ Code in repo | v1.1: same dimensions as the other industry pages, light-blue palette, own layout (split headline hero over a panoramic photo with a dispatch log, dark "trouble lights" reality panel, labeled garage door diagram with numbered pins and a five-card legend, one-stuck-door timeline, navy rating band above the full-width reviews widget, sky CTA panel, boxed FAQ). LSA-led; garage door ads need Google's Advanced Verification (no pre-badge ads). Worksheet v1.4, Wave 5. Plan (draft) to confirm with Jared. Images to make (`gdr-hero`, `gdr-on-the-job`), then create the page in GHL, paste, complete meta data from `ghl-meta/industries/garage-door-repair.md`, publish. Schema waits for the batch. |
| `industries/insurance-agencies.html` | Insurance Agency Marketing (new page at /industries/insurance-agencies) | ✅ Code in repo | v1.0: same dimensions as the other industry pages, light-blue palette, own layout (navy hero with security-print pattern, shield-cropped photo and ID card, two-sided "what agents tell us / what fixes it" conversation, policy-declarations plan with a California-or-Florida switch for the Local Services Ads row, four stages around a renewal ring, ID-card stats, navy CTA panel, FAQ with heading column, not-affiliated note). Meta-led; LSA for CA/FL agents only. Plan (draft) to confirm with Jared; management/legal review suggested. Images to make (`pc-hero`, `pc-on-the-job`), then create the page in GHL, paste, complete meta data from `ghl-meta/industries/insurance-agencies.md`, publish. Schema waits for the batch. |
| `industries/restaurants.html` | Restaurant Marketing (new page at /industries/restaurants) | ✅ Code in repo | v1.3: same dimensions as the other industry pages, cleaning-services blue palette, own layout (hero with photo left and order ticket, kitchen tickets on a rail, recipe-card plan with ingredients and method, four phone screens journey, table-tent stats, reserved-card CTA). No LSA. Plan (draft) to confirm with Jared. Images to make (`rest-hero`, `rest-on-the-job`), then create the page in GHL, paste, complete meta data from `ghl-meta/industries/restaurants.md`, publish. Schema waits for the batch. |
| `industries/funeral-homes.html` | Funeral Home Marketing (new page at /industries/funeral-homes) | ✅ Code in repo | v1.0: same dimensions as the other industry pages, own deliberately quiet layout (sand hero with matted photo frame, two ruled columns around an arched photo, three-column plan divided by rules, at-need / pre-need moments, quiet stat line, framed CTA, ruled FAQ). No AI Voice Agent. Plan (draft) to confirm with Jared. Images to make (`fun-hero`, `fun-on-the-job`; respectful, no caskets), then create the page in GHL, paste, complete meta data from `ghl-meta/industries/funeral-homes.md`, publish. Schema waits for the batch. |
| `industries/auto-shops.html` | Auto Repair Shop Marketing (new page at /industries/auto-shops) | ✅ Code in repo | v1.0: same dimensions as the other industry pages, own layout (garage-door hero with open-bay photo, dashboard warning lights, menu-board plan, road-and-signposts journey, odometer reviews, checkered CTA, owner's-manual FAQ). Plan (draft) to confirm with Jared. Images to make (`auto-hero`, `auto-on-the-job`), then create the page in GHL, paste, complete meta data from `ghl-meta/industries/auto-shops.md`, publish. Schema waits for the batch. |
| `industries/mortgage.html` | Mortgage Marketing (new page at /industries/mortgage) | ✅ Code in repo | v1.1: same dimensions as the other industry pages, own layout (split hero with photo left and loan tracker, heading column + loan-file folders, Gantt-style plan timeline, hub-and-spoke journey with the loan officer photo at the center, chip reviews, certificate CTA with seal, dark FAQ, disclaimer). Management/legal review recommended (mortgage advertising rules, NMLS). Plan (draft) to confirm with Jared. Images to make (`mort-hero`, `mort-on-the-job` = loan officer portrait), then create the page in GHL, paste, complete meta data from `ghl-meta/industries/mortgage.md`, publish. Schema waits for the batch. |
| `industries/health-insurance.html` | Health Insurance Agent Marketing (new page at /industries/health-insurance) | ✅ Code in repo | v1.0: same dimensions as the other industry pages, own layout (white hero with mint shape and member card, audience cards plus agent strip, four coverage levels with meters, three-segment ribbon journey, mint review banner, booking-card CTA, tinted FAQ, not-affiliated note). Management/legal read recommended (insurance marketing). Plan (draft) to confirm with Jared. Images to make (`health-hero`, `health-on-the-job`), then create the page in GHL, paste, complete meta data from `ghl-meta/industries/health-insurance.md`, publish. Schema waits for the batch. |
| `industries/medicare-agents.html` | Medicare Agent Marketing (new page at /industries/medicare-agents) | ✅ Code in repo | v1.0: same dimensions as the other industry pages, own layout (inset hero card, Medicare calendar plus problem cards, summary-of-benefits plan table, center-spine journey, stat-band reviews, photo + two-option CTA, Q-badge FAQ, not-affiliated note). ⚠ Do not publish until management/legal review (CMS marketing rules; worksheet open item). Plan (draft) to confirm with Jared. Images to make (`medi-hero`, `medi-on-the-job`). Schema waits for the batch. |
| `industries/real-estate.html` | Real Estate Marketing (new page at /industries/real-estate) | ✅ Code in repo | v1.1: same dimensions as the other industry pages, own layout (photo hero with listing card, status-tag listing cards, five-stage pipeline-board plan, buyers/sellers tracks plus CRM follow-up strip, spec-row reviews, yard-sign CTA, house-marker FAQ). Meta-led, no LSA. Housing-ad and fair-housing wording needs management/legal review. Plan (draft) to confirm with Jared. Images to make (`re-hero`, `re-on-the-job`), then create the page in GHL, paste, complete meta data from `ghl-meta/industries/real-estate.md`, publish. Schema waits for the batch. |
| `industries/pest-control.html` | Pest Control Marketing (new page at /industries/pest-control) | ✅ Code in repo | v1.0: same dimensions as the other industry pages, own layout (diagonal-split hero with green edge, inspection-report table, perimeter plan with center core card, staircase journey, scorecard reviews, diagonal photo CTA, FAQ in two groups). Plan (draft) to confirm with Jared. Images to make (`pest-hero`, `pest-on-the-job`), then create the page in GHL, paste, complete meta data from `ghl-meta/industries/pest-control.md`, publish. Schema waits for the batch. |
| `industries/pool-service.html` | Pool Service Marketing (new page at /industries/pool-service) | ✅ Code in repo | v1.0: same dimensions as the other industry pages, own layout (deep-water hero with porthole photo and wave edge, rising-water reality cards, plan matrix with row labels, scroll-snap journey carousel, round stat badges, photo CTA with wave top, accent-bar FAQ). Plan (draft) to confirm with Jared. Images to make (`pool-hero`, `pool-on-the-job`), then create the page in GHL, paste, complete meta data from `ghl-meta/industries/pool-service.md`, publish. Schema waits for the batch. |
| `industries/cleaning-services.html` | Cleaning Business Marketing (new page at /industries/cleaning-services) | ✅ Code in repo | v1.0: same dimensions as the other industry pages, own layout (centered hero with booking/photo/review panels, checklist reality card, two package-style plan columns, four steps on a line plus visuals row, rating card beside reviews, mist CTA panel, FAQ with check markers). Plan (draft) to confirm with Jared. Images to make (`clean-hero`, `clean-on-the-job`), then create the page in GHL, paste, complete meta data from `ghl-meta/industries/cleaning-services.md`, publish. Schema waits for the batch. |
| `industries/lawn-care.html` | Lawn Care Marketing (new page at /industries/lawn-care) | ✅ Code in repo | **v1.2: 🔁 paste into GHL** (photos added: lawn-hero, lawn-on-the-job; social share image in meta file). **v1.1** (1440px/64px width standard). v1.0: same dimensions as the other industry pages, own layout (green hero with arch photo, mowing-stripe reality rows, bento plan, neighborhood map journey with callouts, light-green reviews, striped navy CTA, numbered FAQ). Plan (draft) to confirm with Jared. Images to make (`lawn-hero`, `lawn-on-the-job`), then create the page in GHL, paste, complete meta data from `ghl-meta/industries/lawn-care.md`, publish. Schema waits for the batch. |
| `industries/painting.html` | Painting Contractor Marketing (new page at /industries/painting) | ✅ Code in repo | v1.1: same dimensions as the other industry pages, own layout (editorial hero on a light blue wash with swatches, paint-chip reality cards, two-coat palette plan, before/after slider + three cards, big-number reviews, sand CTA, two-column FAQ). Plan (draft) to confirm with Jared. Images to make (`paint-hero`, `paint-on-the-job`), then create the page in GHL, paste, complete meta data from `ghl-meta/industries/painting.md`, publish. Schema waits for the batch. |
| `industries/general-contractors.html` | General Contractor Marketing (new page at /industries/general-contractors) | ✅ Code in repo | v1.1: same dimensions as the other industry pages, different layout (split sand hero, blueprint reality, phased plan, 2x2 journey cards, two-column FAQ). Plan (draft) to confirm with Jared. Images to make (`gc-hero`, `gc-on-the-job`), then create the page in GHL, paste, complete meta data from `ghl-meta/industries/general-contractors.md`, publish. Schema waits for the batch. |
| `industries/plumbing.html` | Plumbing Marketing (new page at /industries/plumbing) | ✅ Code in repo | v2.0: own layout (white hero with framed photo and floating chips, problem → fix cards, two-lane plan, tabbed journey, reviews split, photo CTA, FAQ card). Plan (draft) to confirm with Jared. Images to make (`plumb-hero`, `plumb-on-the-job`), then create the page in GHL, paste, complete meta data from `ghl-meta/industries/plumbing.md`, publish. Schema waits for the batch. |
| `industries/hvac.html` | HVAC Marketing (new page at /industries/hvac) | ✅ Code in repo | **v1.4: 🔁 paste into GHL** (1440px/64px width standard). v1.3: outcome-column plan, 1680px width, reviews widget; reputation folded into Google Business Profile Management. Images to make (`hvac-hero`, `hvac-on-the-job`), then create the page in GHL, paste, complete meta data from `ghl-meta/industries/hvac.md`, publish. Breadcrumb links to /industries (hub not built yet). Schema waits for the batch. |
| `industries/roofing.html` | Roofing Marketing (new page at /industries/roofing) | ✅ Code in repo | v2.0: own layout (centered hero, half-bleed reality photo, sticky plan intro with outcome rows, timeline journey, navy reviews, green CTA, two-column FAQ). Plan (draft) to confirm with Jared. Images to make (`roof-hero`, `roof-on-the-job`), then create the page in GHL, paste, complete meta data from `ghl-meta/industries/roofing.md`, publish. Schema waits for the batch. |

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
| `checkout/google-platinum/` (4 snippets: `1-pricing`, `2-order-summary`, `3-reviews`, `4-faq`) | Google Platinum Checkout | ✅ Code in repo | v1.2: bundle = LSA + Google Business Profile Management (reviews included) — paste snippets 1, 2, 4 into GHL |
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
| `partners/farmers-insurance.html` | Farmers Insurance | ✅ Code in repo | **🔁 paste into GHL** — 1440px width standard (2026-11-23).  |
