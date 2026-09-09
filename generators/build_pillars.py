#!/usr/bin/env python3
"""
Pillar pages: one page that owns each service.

WHY THESE EXIST
The 2026-09-08 engine run (MARKETING/reports/seo/northpeakfp-2026-09-08.md)
found that three of the site's four services had no page of their own: the
home page and the packages table on services.html carried all of them at once,
and nothing on the site answered the first question a buyer types, which is
what the service costs. A pillar page is the page that answers that question
in plain words, names the town, says how to choose, and collects the links from
every article about the service, so the site reads as one authority on it
rather than a set of scattered posts.

Three pillars: accounting services (bookkeeping folds in here, since on this
site it is the first line of the Starter package), controller services, and
CFO advisory. The articles under each are in articles_cluster.py and carry a
"pillar" key that points back here; the existing articles that belong to a
cluster are listed below by slug.

WHAT THE COPY MAY SAY
Only what the site already says. The packages and their contents, the free
30-minute call, the reply within one business day, the fixed figure in
writing, the individually quoted scope, Wilmette, and remote work nationwide.
No fees are printed because none are published. No outcomes are promised.
Chaudhry Ahmad is not a CPA and nothing here implies otherwise.

Each pillar carries: an answer-block lede of 35 to 70 words that opens with the
cost question, the town, and how to choose; h2s phrased as questions; a visible
FAQ emitted as FAQPage; Service and BreadcrumbList markup; a tap-to-call link
and a consultation button above the fold; links to the contact page and to
every article in its cluster.
"""
import html
import sys
import pathlib

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
from build_site import shell, W, SITE, FIRM, EMAIL
import generate_articles_northpeak as G

ART_BY_SLUG = {a["slug"]: a for a in G.ARTICLES}
PHONE_TEL = "tel:+18476442288"
PHONE = "(847) 644-2288"


def _a(href, text):
    return f'<a href="{href}">{text}</a>'


# slug, nav label, title, description, keywords, eyebrow, h1, lede, sections,
# includes (label, items), fit, existing article slugs, faq
PILLARS = [
{
 "slug": "accounting-services",
 "label": "Accounting Services",
 "title": "Accounting Services in Wilmette, IL | NorthPeak",
 "desc": "Bookkeeping, reconciliations, monthly reports, and tax preparation for small businesses, from a Wilmette, IL practice serving clients nationwide.",
 "keywords": "accounting services Wilmette, small business accountant Wilmette IL, bookkeeping services Wilmette, accounting firm north shore",
 "eyebrow": "Accounting &amp; Bookkeeping &middot; Wilmette, IL",
 "h1": "Accounting Services in Wilmette, IL",
 "lede": ("How much do accounting services cost in Wilmette? It depends on the volume and complexity "
          "of your books, so NorthPeak quotes every engagement individually, as a fixed figure in "
          "writing, after a free 30-minute call. Choose a firm by who does the work, when the reports "
          "arrive, and what is left out of scope. We are based in Wilmette, Illinois, and work with "
          "clients nationwide."),
 "package": "starter",
 "package_name": "Starter Package",
 "sections": [
   ("How much do accounting services cost?",
    ["The fee follows the work. A business with a few dozen transactions a month, two bank accounts, "
     "and no payroll is a different job from one with hundreds of transactions, a credit line, staff, "
     "and sales tax in two states. That is why there is no price list on this site. A number printed "
     "before anyone has looked at your books would be either padded or wrong.",
     "What we do instead is quote a fixed figure in writing after the discovery call, and that figure "
     "does not move unless the scope does. Catch-up work, if your books are behind, is scoped and "
     "priced on its own so the one-time cost never hides inside the monthly one. Our guide to "
     + _a("articles/accountant-cost-small-business.html", "what an accountant costs a small business")
     + " goes through what drives the number."]),
   ("What is included in accounting services?",
    ["Bookkeeping and transaction categorisation, bank and credit card reconciliations, monthly "
     "financial reports, basic profit and loss reporting, and tax preparation for the business and "
     "for the people who own it. That is the Starter package, and it is the foundation every other "
     "level of service stands on.",
     "The work runs monthly. Transactions are categorised, every account is matched to its statement, "
     "and the reports arrive on a schedule you agreed to at the start. At year end the return is a "
     "transfer from clean books rather than a reconstruction from a shoebox."]),
   ("How do you choose an accounting firm in Wilmette?",
    ["Ask who will actually see your transactions each month and whether you can reach that person. "
     "Ask how the fee is set and what would change it. Ask when reports arrive and what they will "
     "contain. Ask what is excluded, which is the question that decides whether the first invoice "
     "surprises you. And ask whether the firm will say so if you do not need it yet.",
     "At NorthPeak the founder is the person you deal with, the fee is fixed in writing, and the "
     "first call sometimes ends with the advice to keep doing your own books for another year. Our "
     + _a("articles/questions-to-ask-an-accountant.html", "questions to ask an accountant")
     + " has the full list."]),
   ("Who are accounting services for?",
    ["Startups, solo operators, and small service businesses that need clean, reliable financials "
     "without a finance department. Owners who have been doing their own books and have reached the "
     "point where the hours cost more than the help would. Businesses whose books are behind and "
     "need a scoped clean-up before anything else.",
     "Chaudhry Ahmad, the founder, brings controller-level experience to every engagement, which "
     "means the bookkeeping is done with the reporting in mind. When the business grows past what "
     "bookkeeping and a monthly report can tell you, the next level is "
     + _a("controller-services.html", "controller services") + ", and the move is a conversation, "
     "not a new firm."]),
   ("Does bookkeeping have to be local?",
    ["No. The practice is in Wilmette and meets North Shore clients in person when that is useful, "
     "but the work itself is remote: connected bank feeds, shared software, and scheduled video "
     "reviews. Clients in other states get the same monthly rhythm as clients a few streets away. "
     "If you are elsewhere on the North Shore, the "
     + _a("service-areas/index.html", "service areas") + " page lists the towns we are in most often."]),
 ],
 "includes": ("What the Starter package covers",
              ["Bookkeeping and transaction categorisation", "Bank and credit card reconciliations",
               "Monthly financial reports", "Basic profit and loss reporting",
               "Individual and business tax preparation"]),
 "fit": "Startups, solopreneurs, and small service businesses that need clean, reliable financials.",
 "cluster": ["accountant-cost-small-business", "diy-bookkeeping-or-hire",
             "bookkeeping-mistakes-that-cost-money", "questions-to-ask-an-accountant",
             "bookkeeping-basics", "when-to-hire-accountant", "cash-vs-accrual",
             "business-expense-categories", "tax-planning-vs-tax-prep"],
 "faq": [
   ("Do you publish prices for accounting services?",
    "No. Every engagement is quoted individually after a free 30-minute call, because scope depends on transaction volume, entity count, and how much clean-up is needed. You receive a fixed figure in writing before any work begins."),
   ("Can you take over books that are behind?",
    "Yes. Catch-up and clean-up work is common. It is scoped separately from the ongoing service so you know exactly what the one-time effort costs."),
   ("Do I need to switch accounting software?",
    "Usually not. We work with the major platforms and will say plainly if your current setup is holding you back before recommending any change."),
   ("Is tax preparation included?",
    "Yes. Individual and business tax preparation is part of the Starter package and every level above it."),
   ("Do you work with businesses outside Illinois?",
    "Yes. Engagements are handled remotely with scheduled video reviews, so location is not a constraint."),
 ],
},

{
 "slug": "controller-services",
 "label": "Controller Services",
 "title": "Controller Services in Wilmette, IL | NorthPeak",
 "desc": "Outsourced controller services for growing businesses: a structured monthly close, financial statements, budget vs. actual, and KPI tracking. From Wilmette, IL.",
 "keywords": "controller services Wilmette, outsourced controller, fractional controller Illinois, monthly close services, controller services small business",
 "eyebrow": "Controller Services &middot; Wilmette, IL",
 "h1": "Controller Services in Wilmette, IL",
 "lede": ("How much do controller services cost in Wilmette? A fractional controller is quoted as a "
          "fixed monthly figure for the close, the statements, budget against actual, "
          "and a monthly review call. The fee is set by your books, in writing, after a free 30-minute "
          "call. Choose a controller by who owns the close and when reports land. NorthPeak is based in "
          "Wilmette, Illinois, and works with clients nationwide."),
 "package": "growth",
 "package_name": "Growth Package",
 "sections": [
   ("What does a controller do that a bookkeeper does not?",
    ["A bookkeeper records what happened. A controller is accountable for it being right, on time, "
     "and understood. That means owning the month-end close on a fixed schedule, reviewing every "
     "reconciliation rather than just performing it, preparing financial statements a lender would "
     "accept, comparing results to the budget with the variances explained, and tracking the few "
     "numbers that actually describe the business.",
     "It also means controls: who approves spending, how payroll is checked, where the safeguards sit "
     "that stop errors and leakage as the business grows. Our guide to "
     + _a("articles/bookkeeper-vs-controller-vs-cfo.html", "bookkeeper, controller, and CFO")
     + " draws the lines between the three."]),
   ("How much do controller services cost?",
    ["The scope sets the fee. Transaction volume and the number of accounts matter, as they do for "
     "bookkeeping, and then the things particular to a controller engagement: how many entities need "
     "consolidating, whether there is inventory or job costing, how many KPIs you want tracked, and "
     "how often you want to meet. Everything in the Starter package is included, so the fee covers "
     "the bookkeeping too.",
     "We quote a fixed figure in writing after the discovery call and a look at your current setup. "
     "No rate card, no hourly billing. If the books need a clean-up first, that is scoped and priced "
     "on its own before the monthly rhythm starts. "
     + _a("articles/controller-cost-fractional-vs-full-time.html", "What a controller costs")
     + " compares the fractional arrangement with a full-time hire."]),
   ("How does the monthly close work?",
    ["On the same working days every month. Bank and card accounts are reconciled, uncategorised "
     "transactions cleared, accruals and depreciation recorded, payroll checked against what posted, "
     "receivables aged, payables reviewed. Then the profit and loss, balance sheet, and cash flow "
     "statement are produced and a snapshot of all three is saved.",
     "Once a month we go through the reports with you on a review call: what changed, why, and what "
     "needs a decision. The rhythm settles after the first few closes, and the call gets shorter as "
     "the surprises get fewer. "
     + _a("articles/how-controller-services-work.html", "How controller services work, month by month")
     + " walks through the whole cycle, and "
     + _a("articles/how-long-month-end-close-takes.html", "how long a close takes")
     + " explains what stretches it."]),
   ("Who needs a controller?",
    ["Businesses scaling operations, in the range of about half a million to five million in "
     "revenue, whose books are clean but whose statements arrive late, are not trusted, or are never "
     "compared to a plan. Owners managing from the bank balance because the reports do not tell them "
     "anything in time. Companies about to talk to a lender who will ask for statements that hold up.",
     "If the books are not reconciled monthly yet, "
     + _a("accounting-services.html", "accounting services") + " come first. If the statements are "
     "already good and the questions are about next year rather than last month, "
     + _a("cfo-advisory.html", "CFO advisory") + " is the next level. The three stack, and you move "
     "up when the complexity does."]),
   ("How do you choose a controller in Wilmette?",
    ["Ask who owns the close and whether that person is reachable between calls. Ask what the reports "
     "will contain and when they will arrive, and ask to see a sample. Ask how the fee is set and what "
     "would change it. Ask what is excluded. And ask whether the firm will tell you when you are ready "
     "for the next level rather than selling it to you early.",
     "NorthPeak's founder, Chaudhry Ahmad, brings controller-level experience and is the person you "
     "deal with directly. The practice is in Wilmette, meets North Shore clients in person when it "
     "helps, and runs the same monthly rhythm remotely for everyone else."]),
 ],
 "includes": ("What the Growth package covers",
              ["Everything in Starter: bookkeeping, reconciliations, monthly reports, tax preparation",
               "Controller-level oversight", "Structured monthly close process",
               "Financial statement preparation", "Budget vs. actual reporting",
               "KPI and performance tracking", "Monthly financial review call"]),
 "fit": "Businesses scaling operations, in the range of about half a million to five million in revenue.",
 "cluster": ["controller-cost-fractional-vs-full-time", "bookkeeper-vs-controller-vs-cfo",
             "how-controller-services-work", "how-long-month-end-close-takes",
             "financial-statements-explained", "cash-flow-management", "payroll-setup-guide",
             "1099-vs-w2"],
 "faq": [
   ("What is the difference between a controller and an accountant?",
    "Accountant is the broad term. A controller is the accountant who owns the monthly close, the financial statements, and the internal controls inside a business."),
   ("Do controller services include bookkeeping?",
    "Yes. The Growth package includes everything in Starter: bookkeeping, reconciliations, monthly reports, and tax preparation, with controller oversight on top."),
   ("How is the fee set?",
    "Every engagement is quoted individually after a free 30-minute call and confirmed as a fixed figure in writing before work begins. There is no hourly billing."),
   ("How often do we meet?",
    "Once a month on a review call, plus whatever questions come up between calls. Weekly or bi-weekly strategy calls belong to the CFO package."),
   ("Can you work with our existing software?",
    "Usually, yes. We work with the major platforms and will say plainly if the current setup is holding the close back."),
 ],
},

{
 "slug": "cfo-advisory",
 "label": "CFO Advisory",
 "title": "Fractional CFO Advisory in Wilmette, IL | NorthPeak",
 "desc": "Fractional CFO advisory for established businesses: cash flow forecasting, budgeting, margin analysis, and a standing strategy call. From Wilmette, IL.",
 "keywords": "fractional CFO Wilmette, CFO advisory services, outsourced CFO Illinois, cash flow forecasting, fractional CFO north shore",
 "eyebrow": "CFO Advisory &middot; Wilmette, IL",
 "h1": "Fractional CFO Advisory in Wilmette, IL",
 "lede": ("How much does CFO advisory cost in Wilmette? A fractional CFO is quoted as a fixed monthly "
          "figure for cash flow forecasting, budgeting, margin analysis, and a weekly or bi-weekly "
          "strategy call. The fee is set by the size and complexity of the business, in writing, after "
          "a free 30-minute call. Choose a CFO by who you will meet with. NorthPeak is based in "
          "Wilmette, Illinois, and serves clients nationwide."),
 "package": "cfo",
 "package_name": "CFO Package",
 "sections": [
   ("What does a fractional CFO do?",
    ["Looks forward. A controller tells you what last month was. A CFO builds the rolling cash flow "
     "forecast so the next quarter is planned rather than survived, the budget and the model behind "
     "decisions that are expensive to reverse, and the margin analysis that shows which customers "
     "and services actually make money. The reporting is written for an owner or a board, and it "
     "comes with a strategy call every week or every other week where the numbers meet the decisions.",
     "The word fractional means part-time by design. A business in the low millions of revenue "
     "needs that judgment for a few hours a week, not a full-time executive salary. "
     + _a("articles/do-you-need-a-cfo-yet.html", "Do you need a CFO yet") + " sets out the signs "
     "that a business is ready and the signs that it is not."]),
   ("How much does CFO advisory cost?",
    ["The size and complexity of the business set the fee: the number of revenue lines and entities, "
     "the model you need, how often you want the strategy call, and whether there is a specific "
     "project in front of you such as a financing round, an acquisition, or a new location. The CFO "
     "package includes everything in Growth and Starter, so the controller close and the bookkeeping "
     "are inside the same fee.",
     "We quote a fixed monthly figure in writing after a free 30-minute call and a look at the "
     "business. There is no rate card and no hourly billing. "
     + _a("articles/fractional-cfo-cost.html", "What a fractional CFO costs") + " explains what "
     "should drive the number and how it compares with a full-time hire."]),
   ("Why does the CFO package include the controller work?",
    ["Because advice built on unreliable statements is guesswork with better vocabulary. A forecast "
     "starts from a balance sheet that reconciles and a profit and loss that is right. If that "
     "foundation is not in place, it is built first, and the advisory begins once the statements can "
     "carry it. The levels stack for this reason, and it is why we would rather tell a business it "
     "needs "
     + _a("controller-services.html", "controller services") + " first than sell it a forecast it "
     "cannot trust."]),
   ("Who is CFO advisory for?",
    ["Established businesses, in the range of about two million to one hundred million in revenue, "
     "with decisions waiting on numbers nobody in the building can produce. Whether the next hire is "
     "affordable. How long the cash lasts if a large customer pays late. What a second location does "
     "to margin. Owners with a lender or an investor asking for projections and a plan.",
     "It is also for owners who want someone in the room whose job is to disagree with them when the "
     "numbers do. That is the part of the role a spreadsheet does not replace."]),
   ("How do you choose a fractional CFO in Wilmette?",
    ["Ask who you will meet with and how often. Ask what the forecast and the reports will look like "
     "for a business like yours, and ask to see them. Ask whether the controller work is included or "
     "assumed. Ask for the scope and the fee in writing. And listen for promised outcomes, because "
     "nobody honest promises what your margin or your valuation will do.",
     "At NorthPeak the founder, Chaudhry Ahmad, is the person on every strategy call. The practice is "
     "in Wilmette and meets North Shore clients in person when that helps; the forecasting, "
     "modelling, and calls run remotely for clients anywhere. Our guide to "
     + _a("articles/how-to-choose-a-fractional-cfo.html", "choosing a fractional CFO")
     + " has the full list of questions."]),
 ],
 "includes": ("What the CFO package covers",
              ["Everything in Growth: controller oversight, monthly close, statements, budget vs. actual, KPIs",
               "Fractional CFO advisory", "Cash flow forecasting and planning",
               "Strategic budgeting and modelling", "Profitability and margin analysis",
               "Executive-level financial reporting", "Weekly or bi-weekly strategy calls",
               "Growth and decision support"]),
 "fit": "Established businesses, in the range of about two million to one hundred million in revenue, that need strategic financial leadership.",
 "cluster": ["fractional-cfo-cost", "how-to-choose-a-fractional-cfo", "do-you-need-a-cfo-yet",
             "cash-flow-management", "financial-statements-explained", "llc-vs-s-corp",
             "year-end-tax-moves", "section-179-deduction"],
 "faq": [
   ("What is a fractional CFO?",
    "A CFO who works with the business part-time on a standing basis: forecasting, budgeting, modelling, margin analysis, executive reporting, and a regular strategy call, without a full-time executive salary."),
   ("How is CFO advisory priced?",
    "As a fixed monthly figure, quoted individually after a free 30-minute call and confirmed in writing before the engagement starts."),
   ("Does the CFO package include bookkeeping and the monthly close?",
    "Yes. The CFO package includes everything in the Growth and Starter packages, because advisory is only as good as the statements underneath it."),
   ("How often are the strategy calls?",
    "Weekly or every other week, agreed at the start of the engagement."),
   ("Do I need to be near Wilmette?",
    "No. The forecasting, modelling, and calls run remotely. Local clients can meet in person when that is useful."),
 ],
}
]


def _rows(slugs):
    out = ""
    for s in slugs:
        a = ART_BY_SLUG.get(s)
        if not a:
            continue
        out += (f'<a class="entry" href="articles/{a["slug"]}.html">'
                f'<span class="ec">{html.escape(a["cat"])}</span>'
                f'<div><h3>{html.escape(a["title"])}</h3></div>'
                f'<span class="er">{a["read"]}</span></a>')
    return out


def build():
    for p in PILLARS:
        secs = "".join(
            f'<h2 id="s{j}">{html.escape(h)}</h2>' + "".join(f"<p>{x}</p>" for x in paras)
            for j, (h, paras) in enumerate(p["sections"], 1))
        inc_label, inc_items = p["includes"]
        inc_html = "".join(
            f'<li style="display:flex;gap:11px;padding:10px 0;border-bottom:1px solid var(--rule);'
            f'font-size:.95rem;color:var(--soft)"><span style="color:var(--accent);flex-shrink:0">&#10003;</span>{x}</li>'
            for x in inc_items)
        faq_html = "".join(
            f'<details class="faq"><summary>{html.escape(q)}</summary><p>{html.escape(a)}</p></details>'
            for q, a in p["faq"])
        toc = "".join(f'<li><a href="#s{j}">{html.escape(h)}</a></li>'
                      for j, (h, _) in enumerate(p["sections"], 1))

        body = f"""
<div class="wrap crumb"><a href="index.html">Home</a> &rsaquo; <a href="services.html">Services</a>
 &rsaquo; <span>{p['label']}</span></div>
<div class="wrap pagehead">
  <p class="eyebrow">{p['eyebrow']}</p>
  <h1>{p['h1']}</h1>
  <p class="lead" style="max-width:66ch">{p['lede']}</p>
  <div style="margin-top:26px;display:flex;gap:14px;flex-wrap:wrap">
    <a href="contact.html" class="btn gold lg">Book a Free Consultation</a>
    <a href="{PHONE_TEL}" class="btn ghost lg">{PHONE}</a>
  </div>
  <p style="margin-top:14px;font-size:.9rem;color:var(--mute)">Free 30-minute call. We reply to every
  message within one business day.</p>
</div>

<section style="padding-top:36px;padding-bottom:20px">
  <div class="wrap grid g2" style="gap:52px;align-items:start">
    <div class="aw abody rv" style="max-width:none;padding:0">
      <div class="toc" style="margin-top:0"><p>On this page</p><ol>{toc}</ol></div>
      {secs}
    </div>
    <div class="rv">
      <div class="viz" style="margin-bottom:24px">
        <h2 style="font-size:1.3rem">{inc_label}</h2>
        <p class="cap">{p['package_name']} &middot; quoted for your scope</p>
        <ul style="list-style:none">{inc_html}</ul>
        <p style="font-size:.9rem;color:var(--soft);margin-top:16px"><strong>Best for:</strong> {p['fit']}</p>
        <p style="margin-top:18px"><a href="services.html#{p['package']}">Compare all three packages &rarr;</a></p>
      </div>
      <div class="viz">
        <h2 style="font-size:1.3rem">Talk to NorthPeak</h2>
        <p class="cap">Wilmette, IL &middot; serving clients nationwide</p>
        <p style="font-family:Fraunces,serif;font-size:1.4rem;color:var(--deep);margin-bottom:6px">
          <a href="{PHONE_TEL}" style="text-decoration:none;color:inherit">{PHONE}</a></p>
        <p style="font-size:.95rem;margin-bottom:16px"><a href="mailto:{EMAIL}">{EMAIL}</a></p>
        <a href="contact.html" class="btn" style="justify-content:center;width:100%">Request a Consultation</a>
      </div>
    </div>
  </div>
</section>

<section class="alt pad-s" id="faq">
  <div class="wrap narrow" style="padding:0">
    <div class="sec-head rv" style="margin-bottom:26px"><p class="eyebrow">FAQ</p>
      <h2>Common questions about {p['label'].lower()}</h2></div>
    <div class="rv">{faq_html}</div>
  </div>
</section>

<section class="pad-s">
  <div class="wrap">
    <div class="rhead rv"><span>Guides on {p['label'].lower()}</span><span>{len([s for s in p['cluster'] if s in ART_BY_SLUG])} articles</span></div>
    <div class="elist rv" style="margin-top:26px">{_rows(p['cluster'])}</div>
  </div>
</section>

<section class="alt pad-s">
  <div class="wrap"><div class="split rv">
    <div class="sh"><h2>Not sure this is the right level?</h2></div>
    <div class="sb"><p class="lead" style="max-width:54ch">Tell us about your business in a free 30-minute
    call and we will say which level fits, including if the honest answer is that you do not need us yet.</p>
      <div style="margin-top:22px;display:flex;gap:14px;flex-wrap:wrap">
        <a href="contact.html" class="btn gold lg">Book a Free Consultation</a>
        <a href="{PHONE_TEL}" class="btn ghost lg">Call {PHONE}</a>
      </div></div>
  </div></div>
</section>
"""

        url = f"{SITE}/{p['slug']}"
        service = {
            "@context": "https://schema.org", "@type": "Service",
            "name": p["label"], "serviceType": p["label"],
            "description": html.unescape(p["desc"]), "url": url,
            "provider": {"@type": "AccountingService", "name": FIRM, "url": SITE,
                         "telephone": "+1-847-644-2288", "email": EMAIL,
                         "founder": {"@type": "Person", "name": G.FOUNDER,
                                     "jobTitle": "Founder & Principal"},
                         "address": {"@type": "PostalAddress", "addressLocality": "Wilmette",
                                     "addressRegion": "IL", "addressCountry": "US"}},
            "areaServed": [{"@type": "City", "name": "Wilmette",
                            "containedInPlace": {"@type": "AdministrativeArea",
                                                 "name": "Cook County, Illinois"}},
                           {"@type": "Country", "name": "United States"}],
            "offers": {"@type": "Offer", "name": p["package_name"],
                       "description": "; ".join(html.unescape(x) for x in inc_items),
                       "url": f"{SITE}/services#{p['package']}"},
        }
        webpage = {
            "@context": "https://schema.org", "@type": "WebPage",
            "name": html.unescape(p["title"].split(" | ")[0]), "url": url,
            "datePublished": "2026-09-09", "dateModified": G.LASTMOD,
            "isPartOf": {"@type": "WebSite", "name": FIRM, "url": SITE},
            "about": {"@type": "Service", "name": p["label"], "url": url},
        }
        faqpage = {"@context": "https://schema.org", "@type": "FAQPage", "mainEntity": [
            {"@type": "Question", "name": q, "acceptedAnswer": {"@type": "Answer", "text": a}}
            for q, a in p["faq"]]}
        crumbs = {"@context": "https://schema.org", "@type": "BreadcrumbList", "itemListElement": [
            {"@type": "ListItem", "position": 1, "name": "Home", "item": f"{SITE}/"},
            {"@type": "ListItem", "position": 2, "name": "Services", "item": f"{SITE}/services"},
            {"@type": "ListItem", "position": 3, "name": p["label"], "item": url}]}

        W(f"{p['slug']}.html", shell(
            title=p["title"], desc=p["desc"], canon=url, body=body, active="Services",
            keywords=p["keywords"], jsonld=[webpage, service, faqpage, crumbs]))
    print(f"pillars: {', '.join(p['slug'] for p in PILLARS)}")


if __name__ == "__main__":
    build()
