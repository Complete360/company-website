#!/usr/bin/env python3
"""
Complete360 — structured data (JSON-LD) for every page on complete360.org.

Run from the repo root:   python3 schema/build_schema.py
Needs:                    pip install beautifulsoup4

What it does
- Reads PAGES below (every page on the GHL "Complete360 Main Website",
  with its live URL and its snippet file in ghl-snippets/).
- For pages with code, pulls the description (hero paragraph) and every
  FAQ question + answer straight from the snippet, word for word.
- Writes one paste-ready file per page to schema/pages/<same path as the
  snippet>.html, and rebuilds schema/README.md.

Re-run it whenever a page's FAQ or hero copy changes, then re-paste that
page's file into GHL. Never edit files in schema/pages/ by hand.
"""
import json, os, re, sys
from bs4 import BeautifulSoup

sys.path.insert(0, os.path.dirname(__file__))
from faq_extract import extract as extract_faqs

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SNIPPETS = os.path.join(ROOT, "ghl-snippets")
OUT = os.path.join(ROOT, "schema", "pages")
SITE = "https://complete360.org"
ORG_ID = SITE + "/#organization"
WEBSITE_ID = SITE + "/#website"
CRM_ID = SITE + "/crm-home#software"

# ── Company facts (keep in sync with PROJECT.md) ─────────────────────────
ORGANIZATION = {
    "@type": "ProfessionalService",  # one @type per item: GHL discards saves with a type list
    "@id": ORG_ID,
    "name": "Complete360",
    "legalName": "Home Town Hero Partners LLC",  # per the Privacy Policy
    "alternateName": "Community Marketing Partnership",
    "url": SITE + "/",
    # TODO: swap for the full-size logo file; this is the site favicon.
    "logo": "https://assets.cdn.filesafe.space/1pBjHBEIsKGbwvAUTY9u/media/6a1f2413027d0d5be15b7a20.png",
    "image": "https://assets.cdn.filesafe.space/1pBjHBEIsKGbwvAUTY9u/media/6a1f2413027d0d5be15b7a20.png",
    "description": "Digital marketing agency helping local service businesses get more calls and customers through Google, paid ads, websites, AI agents and an all-in-one CRM platform.",
    "foundingDate": "2018",
    "telephone": "+1-866-527-6205",
    "priceRange": "$$",
    "address": {
        "@type": "PostalAddress",
        "streetAddress": "3444 N Country Club Rd, Ste 105",
        "addressLocality": "Tucson",
        "addressRegion": "AZ",
        "postalCode": "85716",
        "addressCountry": "US",
    },
    "areaServed": {"@type": "Country", "name": "United States"},
    "openingHoursSpecification": [
        {"@type": "OpeningHoursSpecification",
         "dayOfWeek": ["Monday", "Tuesday", "Wednesday", "Thursday"],
         "opens": "07:00", "closes": "16:00"},
        {"@type": "OpeningHoursSpecification",
         "dayOfWeek": "Friday", "opens": "07:00", "closes": "13:00"},
    ],
    "contactPoint": [
        {"@type": "ContactPoint", "contactType": "sales",
         "telephone": "+1-866-527-6205", "areaServed": "US", "availableLanguage": "English"},
        {"@type": "ContactPoint", "contactType": "customer service",
         "telephone": "+1-800-863-2541", "areaServed": "US", "availableLanguage": "English"},
    ],
    "hasMap": "https://maps.app.goo.gl/3zNANtaqrr1FJC1z6",
    "sameAs": [
        "https://www.facebook.com/complete360marketing",
        "https://www.instagram.com/Complete360marketing/",
        "https://twitter.com/Complete360mktg",
    ],
}
ORG_REF = {"@id": ORG_ID}

CRM_APP = {
    "@type": "SoftwareApplication",
    "@id": CRM_ID,
    "name": "Complete360 CRM",
    "applicationCategory": "BusinessApplication",
    "operatingSystem": "Web, iOS, Android",
    "description": "All-in-one CRM for local businesses: capture leads, follow up automatically, book appointments and close sales from one platform.",
    "url": SITE + "/crm-home",
    "publisher": ORG_REF,
}

def offer(name, price, period=None):
    o = {"@type": "Offer", "name": name, "price": str(price), "priceCurrency": "USD"}
    if period:
        o["priceSpecification"] = {"@type": "UnitPriceSpecification", "price": str(price),
                                   "priceCurrency": "USD", "unitText": period}
    return o

# ── Every page on the site ───────────────────────────────────────────────
# kind: home | service | crm | crm-home | pricing | checkout | contact | faq
#       | legal | company | collection | partner | page | skip
# desc: only needed where the page has no code yet (or to override).
P = []
def page(path, file, name, kind, desc=None, **kw):
    P.append(dict(path=path, file=file, name=name, kind=kind, desc=desc, **kw))

page("/", "home.html", "Complete360: Digital Marketing for Local Businesses", "home")

# Services
page("/local-service-ads", "services/local-service-ads.html", "Local Service Ads", "service",
     service="Local Service Ads Management", serviceType="Google Local Services Ads management")
page("/gbp-management", "services/gbp-management.html", "Google Business Profile Management", "service",
     service="Google Business Profile Management", serviceType="Google Business Profile management")
page("/google-business-profile", "services/gbp-setup.html", "Google Business Profile Setup & Optimization", "service",
     service="Google Business Profile Setup & Optimization", serviceType="Google Business Profile setup and optimization")
page("/local-seo-booster", "services/local-seo-booster.html", "Local SEO Booster", "service",
     service="Local SEO Booster", serviceType="Local business listings management")
page("/seo-services", "services/seo-services.html", "SEO Services", "service",
     service="SEO Services", serviceType="Search engine optimization",
     offers=[offer("SEO Services (monthly)", 599, "MONTH"), offer("SEO Services (annual)", 5990, "YEAR")])
page("/geo-fencing", "services/geo-fencing.html", "Geo-Fencing Advertising", "service",
     service="Geo-Fencing Advertising", serviceType="Geofencing advertising on mobile and connected TV")
page("/google-ppc", "services/google-ads.html", "Google Ads (PPC) Management", "service",
     service="Google Ads (PPC) Management", serviceType="Pay-per-click advertising management")
page("/meta-ads", "services/meta-ads.html", "Meta Ads Management", "service",
     service="Meta Ads Management", serviceType="Facebook and Instagram advertising management")
page("/google-social-posting", "services/google-social-posting.html", "Google Social Posting", "service",
     service="Google Social Posting", serviceType="Google Business Profile posting")
page("/meta-social-posting", "services/meta-social-posting.html", "Meta Social Posting", "service",
     service="Meta Social Posting", serviceType="Facebook and Instagram social media posting")
page("/reputation-management", "services/reputation-management.html", "Reputation Management", "service",
     service="Reputation Management", serviceType="Online review and reputation management")
page("/local-display-network", "services/local-display-network.html", "Local Display Network", "service",
     service="Local Display Network", serviceType="In-store digital screen advertising")
page("/dispensary", "services/dispensary.html", "Dispensary Advertising", "service",
     service="Dispensary Geo-Fencing Advertising", serviceType="Cannabis dispensary geofencing advertising")
page("/procard", "services/procard.html", "ProCard Digital Business Card", "service",
     service="ProCard", serviceType="Digital business card")
page("/websites-home", "services/websites-home.html", "Website Design", "service",
     service="Website Design", serviceType="Website design and hosting")
page("/ai-agents", "services/ai-employee.html", "AI Agents", "service",
     service="AI Agents", serviceType="AI voice agent and AI chat assistant",
     offers=[offer("AI Voice Agent (monthly)", 399, "MONTH"), offer("AI Voice Agent (annual)", 3990, "YEAR"),
             offer("AI Assistant (monthly)", 599, "MONTH"), offer("AI Assistant (annual)", 5990, "YEAR"),
             offer("AI Agent setup (one time)", 2000)])
page("/payments", "services/payments.html", "Make a Payment", "page",
     desc="Pay your Complete360 invoice securely online.")

# Pricing
page("/website-pricing", "pricing/website-pricing.html", "Website Pricing", "pricing")
page("/pricing", "pricing/saas-pricing.html", "Complete360 CRM Pricing", "pricing", about_crm=True,
     desc="Compare Complete360 CRM plans and monthly pricing for local businesses.")

# CRM platform
page("/crm-home", "crm-platform/crm-home.html", "Complete360 CRM", "crm-home")
page("/capture", "crm-platform/capture.html", "Capture Leads", "crm",
     desc="Step 1 of the Complete360 CRM: capture every lead from your website, calls, texts and forms in one place.")
page("/nurture", "crm-platform/nurture.html", "Nurture Leads", "crm",
     desc="Step 2 of the Complete360 CRM: follow up automatically by text and email so no lead goes cold.")
page("/close", "crm-platform/close.html", "Close Sales", "crm",
     desc="Step 3 of the Complete360 CRM: book appointments, send invoices and close more sales from one platform.")
page("/all-in-one-inbox-feature-page", "crm-platform/inbox.html", "All-in-One Inbox", "crm",
     desc="See calls, texts, emails, chats and social messages in one inbox with the Complete360 CRM.")
page("/calendar-feature", "crm-platform/calendar.html", "Online Booking Calendar", "crm",
     desc="Let customers book appointments online with the Complete360 CRM calendar, with automatic reminders.")
page("/chat-widget-feature-page", "crm-platform/chat-widget.html", "Website Chat Widget", "crm",
     desc="Add a chat widget to your website that turns visitors into leads and sends every conversation to the Complete360 CRM.")

# Company
page("/faq", "company/faq.html", "Frequently Asked Questions", "faq",
     desc="Answers to common questions about Complete360's services, pricing, billing, cancellations and support.")
page("/contact-us", "company/contact-us.html", "Contact Complete360", "contact")
page("/schedule-demo", "company/schedule-demo.html", "Schedule a Free Strategy Call", "company",
     desc="Book a free 15-minute strategy call with the Complete360 team.")
page("/request-a-demo", "company/request-demo.html", "Request a Demo", "company",
     desc="Request a free demo of Complete360's marketing services and CRM platform.")
page("/training", "company/training.html", "Training", "skip")
page("/video-library", "company/video-library.html", "Video Library", "collection")
page("/links", "company/link-tree.html", "Complete360 Links", "page")
page("/thank-you-for-demo", "company/thank-you-after-schedule.html", "Thank You", "skip")
page("/thank-you-form", "company/thank-you-after-form-fill.html", "Thank You", "skip")
page("/404", "global/404.html", "Page Not Found", "skip")

# Legal
page("/tos", "legal/tos.html", "Terms of Service", "legal")
page("/privacy-policy", "legal/privacy-policy.html", "Privacy Policy", "legal")
page("/return-policy", "legal/return-policy.html", "Return & Refund Policy", "legal")

# Partners
page("/farmers-insurance", "partners/farmers-insurance.html", "Farmers Insurance Agent Program", "partner")

# Checkouts (built in GHL; schema only marks them as checkout pages)
for path, file, product in [
    ("/lsa-checkout", "checkout/local-service-ads", "Local Service Ads"),
    ("/gbp-management-checkout", "checkout/gbp-management", "Google Business Profile Management"),
    ("/gbp-setup-checkout", "checkout/gbp-setup", "Google Business Profile Setup"),
    ("/google-platinum-checkout", "checkout/google-platinum", "the Google Platinum Package"),
    ("/local-seo-checkout", "checkout/local-seo-booster", "Local SEO Booster"),
    ("/google-ads-checkout", "checkout/google-ads-checkout.html", "Google Ads (PPC) Management"),
    ("/meta-checkout", "checkout/meta-ads-checkout.html", "Meta Ads Management"),
    ("/geo-mobile-checkout", "checkout/geo-fencing-mobile-checkout.html", "Geo-Fencing (Mobile)"),
    ("/geo-ctv-checkout", "checkout/geo-fencing-ctv-checkout.html", "Geo-Fencing (Connected TV)"),
    ("/google-social-checkout", "checkout/google-social-posting", "Google Social Posting"),
    ("/meta-social-checkout", "checkout/meta-social-posting-checkout.html", "Meta Social Posting"),
    ("/procard-checkout", "checkout/procard-checkout.html", "ProCard"),
    ("/website-checkout", "checkout/website-checkout.html", "Website Design"),
    ("/dispensary-checkout", "checkout/dispensary-checkout.html", "Dispensary Advertising"),
    ("/ai-checkout", "checkout/ai-employee-checkout.html", "AI Agents"),
    ("/lifetime-checkout", "checkout/lifetime-deal-checkout.html", "the Complete360 CRM Lifetime Deal"),
    ("/checkout-1", "checkout/tier-1-plan-checkout.html", "the Complete360 CRM Tier 1 plan"),
    ("/checkout-2", "checkout/tier-2-plan-checkout.html", "the Complete360 CRM Tier 2 plan"),
    ("/checkout-3", "checkout/tier-3-plan-checkout.html", "the Complete360 CRM Tier 3 plan"),
]:
    page(path, file, "Checkout: " + re.sub(r"^the ", "", product), "checkout",
         desc=f"Secure checkout for {product} from Complete360.")

SKIP_WHY = {
    "/thank-you-for-demo": "Thank-you pages shouldn't appear in search. Set this page to noindex in GHL instead of adding schema.",
    "/thank-you-form": "Thank-you pages shouldn't appear in search. Set this page to noindex in GHL instead of adding schema.",
    "/404": "Error pages don't get schema.",
    "/training": "This page is password-protected client training, so it shouldn't appear in search. Set it to noindex in GHL instead of adding schema.",
}

# ── Policy guard ─────────────────────────────────────────────────────────
# Schema repeats page copy word for word, so a page with outdated policy text
# would put it into Google and AI tools. Any page whose schema matches one of
# these is written with a HOLD notice and flagged in the README until the
# page itself is fixed. (ToS / Return Policy v2.1: 10 days' written notice,
# non-refundable from purchase, no money-back guarantee.)
POLICY_CONFLICTS = [
    (r"cancel(?:led)?\s+(?:any\s?time|at any time)", "\"cancel anytime\""),
    (r"\b30\s+days'?\s+notice", "30 days' notice"),
    (r"money[- ]back", "money-back guarantee"),
    (r"non-refundable\s+(?:once|after)\s+(?:work|the management period)", "refundable until work begins"),
    (r"no per-minute fees", "\"no per-minute fees\" without \"AI\""),
]
def policy_conflicts(text):
    return [label for rx, label in POLICY_CONFLICTS if re.search(rx, text, re.I)]

# ── Helpers ──────────────────────────────────────────────────────────────
def read_snippet(rel):
    """A page's code: one .html file, or a folder of numbered snippets
    (checkouts) read in order and joined."""
    p = os.path.join(SNIPPETS, rel)
    if os.path.isdir(p):
        parts = sorted(x for x in os.listdir(p) if x.endswith(".html"))
        html = "\n".join(open(os.path.join(p, x), encoding="utf-8").read() for x in parts)
        return html or None
    if not os.path.exists(p):
        return None
    html = open(p, encoding="utf-8").read()
    return None if html.lstrip().startswith("<!--\n  PLACEHOLDER") or "PLACEHOLDER: no code yet" in html[:400] else html

def hero_description(html):
    soup = BeautifulSoup(html, "html.parser")
    h1 = soup.find("h1")
    p = h1.find_next("p") if h1 else soup.find("p")
    if not p:
        return None
    for t in p.select("i, svg, script, style"):
        t.decompose()
    txt = re.sub(r"\s+", " ", p.get_text(" ", strip=True))
    txt = re.sub(r"\s+([,.;:!?)])", r"\1", txt)
    if len(txt) > 300:  # cut at a sentence end
        cut = txt[:300].rsplit(". ", 1)[0]
        txt = cut + "." if not cut.endswith(".") else cut
    return txt or None

def faq_node(pairs, url):
    return {
        "@type": "FAQPage", "@id": url + "#faq", "url": url,
        "mainEntity": [{"@type": "Question", "name": q,
                        "acceptedAnswer": {"@type": "Answer", "text": a}} for q, a in pairs],
    }

# ── Build ────────────────────────────────────────────────────────────────
def build(pg):
    url = SITE + ("/" if pg["path"] == "/" else pg["path"])
    html = read_snippet(pg["file"])
    desc = pg["desc"] or (hero_description(html) if html else None) or pg["name"]
    faqs = extract_faqs(html) if html else []

    if pg["kind"] == "skip":
        return None, {"faqs": 0, "types": "—", "has_code": bool(html), "url": url}

    page_type = {"checkout": "CheckoutPage", "contact": "ContactPage", "faq": "FAQPage",
                 "collection": "CollectionPage"}.get(pg["kind"], "WebPage")
    webpage = {"@type": page_type, "@id": url + "#webpage", "url": url, "name": pg["name"],
               "description": desc, "isPartOf": {"@id": WEBSITE_ID},
               "publisher": ORG_REF, "inLanguage": "en-US"}
    graph = [ORGANIZATION]

    if pg["kind"] == "home":
        graph.append({"@type": "WebSite", "@id": WEBSITE_ID, "url": SITE + "/", "name": "Complete360",
                      "publisher": ORG_REF, "inLanguage": "en-US"})
        webpage["about"] = ORG_REF
    else:
        webpage["breadcrumb"] = {"@type": "BreadcrumbList", "itemListElement": [
            {"@type": "ListItem", "position": 1, "name": "Home", "item": SITE + "/"},
            {"@type": "ListItem", "position": 2, "name": pg["name"], "item": url}]}

    if pg["kind"] == "service":
        svc = {"@type": "Service", "@id": url + "#service", "name": pg["service"],
               "serviceType": pg["serviceType"], "description": desc, "url": url,
               "provider": ORG_REF, "areaServed": {"@type": "Country", "name": "United States"}}
        if pg.get("offers"):
            svc["offers"] = pg["offers"]
        webpage["mainEntity"] = {"@id": url + "#service"}
        graph.append(svc)
    if pg["kind"] == "crm-home":
        graph.append(CRM_APP)
        webpage["mainEntity"] = {"@id": CRM_ID}
    if pg["kind"] == "crm" or pg.get("about_crm"):
        webpage["about"] = {"@id": CRM_ID}

    if pg["kind"] == "faq":
        webpage["mainEntity"] = [{"@type": "Question", "name": q,
                                  "acceptedAnswer": {"@type": "Answer", "text": a}} for q, a in faqs]
    elif faqs:
        graph.append(faq_node(faqs, url))

    graph.insert(1 if pg["kind"] != "home" else 2, webpage)
    data = {"@context": "https://schema.org", "@graph": graph}
    types = [page_type] + [n["@type"] if isinstance(n["@type"], str) else "Organization"
                           for n in graph if n is not webpage and n is not ORGANIZATION]
    return data, {"faqs": len(faqs), "types": ", ".join(types), "has_code": bool(html), "url": url}

def main():
    rows = []
    for pg in P:
        data, info = build(pg)
        out = os.path.join(OUT, pg["file"] if pg["file"].endswith(".html") else pg["file"] + ".html")
        os.makedirs(os.path.dirname(out), exist_ok=True)
        head = (f"<!-- Schema (JSON-LD) for {pg['name']} — {info['url']}\n"
                f"     GHL: page editor > SEO & AI search optimization > Schema Markup > JSON view.\n"
                f"     Paste only the JSON between the script tags (from the first {{ to the last }}).\n"
                f"     Generated by schema/build_schema.py from ghl-snippets/{pg['file']}. Do not edit by hand. -->\n")
        info["hold"] = []
        if data is None:
            body = f"<!-- No schema for this page. {SKIP_WHY.get(pg['path'], '')} -->\n"
        else:
            js = json.dumps(data, indent=2, ensure_ascii=False)
            info["hold"] = policy_conflicts(js)
            if info["hold"]:
                head = ("<!-- ⚠ HOLD — DO NOT PASTE. This page's copy conflicts with the refund/cancellation\n"
                        f"     policy ({', '.join(info['hold'])}). Fix ghl-snippets/{pg['file']} first,\n"
                        "     then re-run build_schema.py. -->\n") + head
            body = '<script type="application/ld+json">\n' + js + "\n</script>\n"
        open(out, "w", encoding="utf-8").write(head + body)
        rows.append((pg, info))
    write_readme(rows)
    held = [(pg["path"], i["hold"]) for pg, i in rows if i.get("hold")]
    print(f"{len(rows)} pages written to schema/pages/")
    for path, why in held:
        print(f"  HOLD {path}: {', '.join(why)}")

def write_readme(rows):
    lines = [
        "# Schema (structured data) for every page",
        "",
        "One paste-ready file per page on complete360.org, in `schema/pages/` (same folders as",
        "`ghl-snippets/`). Each file is a `<script type=\"application/ld+json\">` block that tells",
        "Google and AI tools what the page is: the company, the service, its FAQs, and so on.",
        "",
        "## How to add one to a page in GHL",
        "Schema goes in GHL's own schema editor, not Tracking Code and not the page snippet.",
        "1. **Sites → Websites → Complete360 site → Edit** the page.",
        "2. Left panel: **SEO & AI search optimization → Schema Markup** → open the editor → **JSON view**.",
        "3. Select all and delete (this also clears old or auto-generated schema), then paste the JSON",
        "   from the page's file: everything between the `<script>` tags, from the first `{` to the last `}`.",
        "4. **Validate & Save**, then **Save and Publish** the page.",
        "5. Check the live URL at https://validator.schema.org (Google's Rich Results Test only lists",
        "   the business item).",
        "",
        "What GHL accepts:",
        "- Paste one complete block per page in JSON view. Don't use **+ Add schema** or Form view",
        "  (Form view drops fields).",
        "- Every item needs a single `@type`. A list like `[\"Organization\", \"ProfessionalService\"]`",
        "  makes GHL silently discard the save, so the company item is `ProfessionalService`.",
        "- `@id` links between items (WebPage → WebSite → organization) work.",
        "- The GHL reviews widget adds its own Organization/LocalBusiness items with the live rating.",
        "  They're valid; leave them.",
        "",
        "## Keeping it current",
        "- FAQs and descriptions are pulled word for word from the snippets in `ghl-snippets/`.",
        "  After changing a page's FAQ or hero text, run `python3 schema/build_schema.py`, commit,",
        "  and re-paste that page's file into GHL.",
        "- Company details (phones, address, hours, social profiles) live in `ORGANIZATION` at the",
        "  top of `build_schema.py`. Change them there and every page picks it up.",
        "- Pages whose code isn't in the repo yet get a basic description written for them. Once the",
        "  page's code is added, re-run the script and their FAQs are picked up automatically.",
        "- Prices are only included for SEO Services and AI Agents (from PROJECT.md). If those change,",
        "  update `offers` in the script.",
        "",
        "## Notes",
        "- Google shows FAQ rich results mainly for government and health sites, so FAQ schema won't",
        "  enlarge your Google listing. It still helps Google and AI tools read your answers.",
        "- The schema repeats whatever the page says. Pages listed under Known issues in PROJECT.md",
        "  (\"cancel anytime\", 30-day notice) will be repeated in their FAQ schema until the page is fixed.",
        "- The logo is currently the favicon. Swap in the full logo URL in `ORGANIZATION` when you have it.",
        "",
        "## Pages",
        "",
        "Pages marked **⚠ HOLD** repeat outdated refund or cancellation wording from the page itself.",
        "Don't paste them until the page is fixed and this script is re-run.",
        "",
        "| Page | URL | Schema file | Types | FAQs | Status |",
        "|---|---|---|---|---|---|",
    ]
    for pg, info in rows:
        if info.get("hold"):
            code = "⚠ HOLD: page conflicts with policy (" + ", ".join(info["hold"]) + ")"
        elif pg["kind"] == "skip":
            code = "No schema (noindex instead)"
        else:
            code = "✅" if info["has_code"] else "⬜ (basic schema until code is added)"
        lines.append(f"| {pg['name']} | `{pg['path']}` | `schema/pages/{pg['file'] if pg['file'].endswith('.html') else pg['file'] + '.html'}` | {info['types']} | "
                     f"{info['faqs'] or '—'} | {code} |")
    open(os.path.join(ROOT, "schema", "README.md"), "w", encoding="utf-8").write("\n".join(lines) + "\n")

if __name__ == "__main__":
    main()
