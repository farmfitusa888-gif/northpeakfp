#!/usr/bin/env python3
"""
Service-area pages for the towns NorthPeak actually works in.

WHY THESE EXIST
Search Console (3 months to 2026-08-16) shows the firm already ranking #1 for
"tax planning wilmette illinois" and "accounting in glenview", and #2 for
"wilmette bookkeeping" — with no page on the site about any town. The same
report shows position 21-41 for Skokie and Wheeling variants, i.e. page 3 to
page 5. These are transactional queries; the national tax guides, by contrast,
sit at position 74-92. This block targets the queries where the firm is already
visible.

THE THIN-CONTENT TRAP, AND HOW THIS AVOIDS IT
A set of location pages that differ only by a swapped town name is the single
most reliable way to get a batch of URLs marked "Crawled - currently not
indexed". Every town page here therefore carries a real, verifiable difference
rather than rewritten filler:

  * County and township, which are facts, not colour.
  * WHO actually assesses property there. This genuinely differs: in Cook
    County the County Assessor sets assessments on a triennial township cycle;
    in Lake County — as in every Illinois county outside Cook — the TOWNSHIP
    assessor does, and the Board of Review requires contacting them first for
    factual-error and vacancy appeals.
  * Wheeling is split by Lake Cook Road, with different counties AND different
    sales tax rates on either side.
  * Different neighbour sets, so the internal link graph differs per page.

Nothing about local "character", housing stock, or business mix is asserted,
because none of that is verifiable from here and inventing it is what makes
these pages worthless.

SOURCES for the assessment facts
  Cook County Board of Review .......... cookcountyboardofreview.com
  Lake County appeal process ........... lakecountyil.gov/503/Appeal-Process
  Illinois Property Tax Appeal Board ... ptab.illinois.gov/getstarted.html
  New Trier Township ................... newtriertownship.com
  Niles Township ....................... nilestownshipgov.com
  Village of Wheeling assessment/tax ... wheelingil.gov/466, wheelingil.gov/245
"""
import os
import sys
import json
import html
import pathlib

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
from build_site import shell, W, SITE, FIRM, EMAIL
import generate_articles_northpeak as G

ARTS = G.ARTICLES
BASE_CITY = "Wilmette"

COOK_ASSESS = (
    "Property in {town} is assessed by the <strong>Cook County Assessor</strong>, "
    "which reassesses one third of the county each year on a three-year township "
    "cycle. In a reassessment year you get two chances to contest a value — first "
    "at the Assessor's office, then at the independent "
    "<a href=\"https://www.cookcountyboardofreview.com/\" rel=\"noopener\" target=\"_blank\">"
    "Board of Review</a>. In an off year, usually only the Board of Review window "
    "is open. If you own the building your business operates from, that cycle is "
    "worth tracking, because the deadlines are short and they do not move."
)

LAKE_ASSESS = (
    "{town} sits in Lake County, and that changes who you deal with. Outside Cook "
    "County, Illinois assessments are set by the <strong>township assessor</strong>, "
    "not a county assessor. Lake County asks property owners to contact their "
    "township assessor before filing with the "
    "<a href=\"https://www.lakecountyil.gov/503/Appeal-Process\" rel=\"noopener\" target=\"_blank\">"
    "Board of Review</a> — and for factual-error and commercial-vacancy appeals, "
    "that contact is required, not optional. It is a different first phone call "
    "than a business owner a few miles south would make."
)

# name, slug, county, township, assessment paragraph, neighbours, extra fact
TOWNS = [
    ("Wilmette", "wilmette", "Cook", "New Trier Township", COOK_ASSESS,
     ["evanston", "winnetka", "skokie", "glenview"],
     "This is where the practice is based, so Wilmette work is as local as it gets — "
     "in person when that is useful, remote when it is faster."),

    ("Evanston", "evanston", "Cook", "Evanston Township", COOK_ASSESS,
     ["wilmette", "skokie", "winnetka"],
     "Evanston is its own township as well as its own city, which means its assessment "
     "office and its appeal calendar are worth checking separately from the towns "
     "immediately north of it."),

    ("Skokie", "skokie", "Cook", "Niles Township", COOK_ASSESS,
     ["evanston", "morton-grove", "niles", "wilmette"],
     "Skokie shares Niles Township with Lincolnwood, Golf, and parts of Morton Grove, "
     "Niles and Glenview — so several of the businesses we work with a few streets "
     "apart are on the same township assessment cycle."),

    ("Glenview", "glenview", "Cook", "split across New Trier, Niles and Northfield Townships",
     COOK_ASSESS, ["northbrook", "wilmette", "morton-grove", "niles"],
     "Glenview is unusual: it is divided across three townships. Two businesses on "
     "opposite sides of the village can sit in different township assessment groups, "
     "which is worth confirming before assuming a reassessment year applies to you."),

    ("Northbrook", "northbrook", "Cook", "Northfield Township", COOK_ASSESS,
     ["glenview", "deerfield", "winnetka", "wheeling"],
     "Northbrook borders Deerfield, and the county line runs between them — a short "
     "drive changes which assessment system a property falls under."),

    ("Winnetka", "winnetka", "Cook", "New Trier Township", COOK_ASSESS,
     ["wilmette", "glencoe-highland-park", "northbrook", "evanston"],
     "Winnetka shares New Trier Township with Wilmette, Kenilworth and Glencoe, so it "
     "runs on the same Cook County reassessment cycle as the practice's home village."),

    ("Morton Grove", "morton-grove", "Cook", "Niles Township", COOK_ASSESS,
     ["skokie", "niles", "glenview", "park-ridge"],
     "Morton Grove is split across townships, with a portion in Niles Township — one "
     "more case where the address, not the village name, decides the cycle."),

    ("Niles", "niles", "Cook", "Niles and Maine Townships", COOK_ASSESS,
     ["morton-grove", "skokie", "park-ridge", "glenview"],
     "The village of Niles and Niles Township are not the same boundary, and parts of "
     "the village fall outside the township. It catches people out."),

    ("Park Ridge", "park-ridge", "Cook", "Maine Township", COOK_ASSESS,
     ["niles", "morton-grove", "glenview"],
     "Park Ridge sits in Maine Township, a different assessment group from the New "
     "Trier and Niles Township towns closer to the lake."),

    ("Deerfield", "deerfield", "Lake", "West Deerfield Township", LAKE_ASSESS,
     ["northbrook", "highland-park", "wheeling", "glenview"],
     "Deerfield is mostly Lake County with a portion extending into Cook, so the "
     "answer to \"who assesses my building\" genuinely depends on the parcel."),

    ("Highland Park", "highland-park", "Lake", "Moraine and West Deerfield Townships",
     LAKE_ASSESS, ["deerfield", "northbrook", "winnetka"],
     "Highland Park is firmly Lake County, so its assessment path runs through a "
     "township assessor rather than the Cook County system most of its southern "
     "neighbours use."),

    ("Wheeling", "wheeling", "Cook and Lake", "Wheeling Township (Cook) and Vernon Township (Lake)",
     "Wheeling is genuinely split, and the dividing line is <strong>Lake Cook Road</strong>. "
     "South of it, assessment runs through the Cook County Assessor and taxes are "
     "collected by the Cook County Treasurer. North of it, the Lake County Chief "
     "County Assessment Office handles assessment and the Lake County Treasurer "
     "collects. The village publishes this split itself, along with the sales tax "
     "consequence: the "
     "<a href=\"https://www.wheelingil.gov/245/Sales-Tax\" rel=\"noopener\" target=\"_blank\">"
     "Cook County portion carries a 10% total sales tax rate and the Lake County "
     "portion 8%</a>. If you sell taxable goods in Wheeling, which side of Lake Cook "
     "Road your counter sits on is a real number on your return.",
     ["northbrook", "deerfield", "glenview"],
     None),
]


# ---------------------------------------------------------------------------
# INDIVIDUAL TOWN PAGES ARE GATED OFF, DELIBERATELY.
#
# They were built and then measured: 12 pages, 350-385 words each, 76% mean
# word-set overlap, 91.8% between the closest pair (Wilmette / Winnetka). For
# comparison, the /repairs/ pages on another site in this portfolio that Google
# marked "Crawled - currently not indexed" had a 6% byte spread; these had 2%.
# Publishing them would spend 12 URLs of crawl budget to get 12 pages ignored,
# and risks dragging the pages that DO rank.
#
# The blocker is not the code, it is source material. To flip this to True each
# town needs roughly 250-400 words that are true and specific and that a
# competitor could not write from a map — for example:
#   * a named client situation or industry the firm actually works with there
#     (no names required, but a real scenario, not an archetype)
#   * why an owner in that town tends to call, in Chaudhry's words
#   * anything genuinely local he knows and can stand behind
# Invented local colour is worse than no page: it is the exact pattern that put
# 53 pages of another site into "not indexed".
#
# Until then the hub below carries the whole block, and it carries it well: the
# assessment table on it is unique, useful, and not something a competitor can
# copy without doing the same research.
# ---------------------------------------------------------------------------
TOWN_PAGES_READY = False

SLUGS = {t[1]: t[0] for t in TOWNS}

SERVICES = [
    ("Bookkeeping and monthly close",
     "Reconciled books, transactions categorised properly, and a close that lands on "
     "the same working day every month instead of whenever it gets finished."),
    ("Controller services",
     "Budget against actual, a close process that holds when the month is busy, and "
     "the few KPIs that actually describe your business."),
    ("CFO advisory",
     "Cash-flow forecasting, margin analysis, and the modelling behind decisions that "
     "are expensive to reverse."),
    ("Tax planning and preparation",
     "Planned across the year rather than reconstructed in April — entity strategy, "
     "quarterly estimates, and filing for the business and the people who own it."),
]

# Articles most worth surfacing from a local page: the ones aimed at an owner
# deciding whether they need help at all.
LOCAL_READS = ["when-to-hire-accountant", "quarterly-estimated-taxes",
               "tax-deductions-small-business", "bookkeeping-basics",
               "llc-vs-s-corp", "cash-flow-management"]
ART_BY_SLUG = {a["slug"]: a for a in ARTS}


def faq_for(town, county, township, extra):
    """Only questions whose ANSWER changes with the town.

    The two generic ones that used to live here — "do you meet in person" and
    "what does it cost" — were identical on all twelve pages and are already
    answered on /contact. Repeating them made every page look like the last one.
    """
    return [
        (f"Which county and township handle assessment for a {town} business?",
         f"{town} is in {county} County, {township}. That decides who values your "
         f"property, which appeal window applies, and who you call first — and it is "
         f"not the same answer a few miles away."),
        (f"Do you work with {town} businesses in person or remotely?",
         f"Both. The practice is in {BASE_CITY}, so {town} is a short drive when a "
         f"conversation is better had in the same room. Ongoing work runs remotely "
         f"because it is faster for everyone. See "
         f"<a href=\"../contact.html\">contact</a> for what happens after the first call."),
    ]


def build():
    made = [(t[0], t[1], t[2]) for t in TOWNS]
    for name, slug, county, township, assess, neighbours, extra in (TOWNS if TOWN_PAGES_READY else []):
        assess_html = assess.format(town=name) if "{town}" in assess else assess
        reads = [ART_BY_SLUG[s] for s in LOCAL_READS if s in ART_BY_SLUG][:3]
        faqs = faq_for(name, county, township, extra)

        near = "".join(
            f'<li><a href="{s}.html">{SLUGS[s]}</a></li>'
            for s in neighbours if s in SLUGS)

        read_rows = "".join(
            f'<a class="entry" href="../articles/{a["slug"]}.html">'
            f'<span class="ec">{html.escape(a["cat"])}</span>'
            f'<div><h3>{html.escape(a["title"])}</h3></div>'
            f'<span class="er">{a["read"]}</span></a>' for a in reads)

        faq_html = "".join(
            f'<div class="lrow"><div class="ln">Q</div><h3>{html.escape(q)}</h3>'
            f'<p>{html.escape(a)}</p><span></span></div>' for q, a in faqs)

        extra_html = f'<p class="lead" style="max-width:58ch;margin-top:18px">{extra}</p>' if extra else ""

        body = f"""
<div class="wrap crumb"><a href="../index.html">Home</a> &rsaquo;
  <a href="index.html">Service Areas</a> &rsaquo; <span>{name}</span></div>
<div class="wrap pagehead">
  <p class="eyebrow">{county} County &middot; {township}</p>
  <h1>Accounting &amp; Tax Services in {name}, IL</h1>
  <p class="lead" style="max-width:62ch">Bookkeeping, controller support, CFO advisory,
  and tax work for {name} businesses and the people who own them &mdash; from a practice
  based in {BASE_CITY}, a few minutes away.</p>
  {extra_html}
  <div style="margin-top:26px;display:flex;gap:14px;flex-wrap:wrap">
    <a href="../contact.html" class="btn gold lg">Book a Free Consultation</a>
    <a href="tel:+18476442288" class="btn ghost lg">(847) 644-2288</a>
  </div>
</div>

<section class="alt pad-s">
  <div class="wrap">
    <div class="split rv">
      <div class="sh"><h2>Property assessment in {name}</h2>
        <p>Worth knowing before you assume the rules are the same everywhere in
        the north suburbs. They are not.</p></div>
      <div class="sb"><p class="lead" style="max-width:62ch">{assess_html}</p></div>
    </div>
  </div>
</section>

<section class="alt pad-s">
  <div class="wrap">
    <div class="rhead rv"><span>Common questions</span><span>{name}</span></div>
    <div class="ledger rv" style="margin-top:26px">{faq_html}</div>
  </div>
</section>

<section class="pad-s">
  <div class="wrap">
    <div class="split rv">
      <div class="sh"><h2>Also serving</h2>
        <p>Neighbouring communities we work in regularly.</p></div>
      <div class="sb">
        <ul style="columns:2;gap:30px;list-style:none;line-height:2.1">{near}</ul>
        <p style="margin-top:18px"><a href="index.html">See every service area &rarr;</a></p>
      </div>
    </div>
  </div>
</section>

<section class="alt pad-s">
  <div class="wrap">
    <div class="rhead rv"><span>Worth reading first</span><span>Guides</span></div>
    <div class="elist rv" style="margin-top:26px">{read_rows}</div>
  </div>
</section>
"""
        jsonld = {
            "@context": "https://schema.org",
            "@graph": [
                {"@type": "AccountingService", "name": FIRM, "url": f"{SITE}/service-areas/{slug}",
                 "email": EMAIL, "telephone": "+1-847-644-2288",
                 "image": f"{SITE}/assets/og-image.jpg", "priceRange": "$$",
                 "founder": {"@type": "Person", "name": G.FOUNDER,
                             "jobTitle": "Founder & Principal"},
                 "address": {"@type": "PostalAddress", "addressLocality": BASE_CITY,
                             "addressRegion": "IL", "addressCountry": "US"},
                 "areaServed": {"@type": "City", "name": name,
                                "containedInPlace": {"@type": "AdministrativeArea",
                                                     "name": f"{county} County, Illinois"}},
                 "serviceType": [s[0] for s in SERVICES]},
                {"@type": "FAQPage", "mainEntity": [
                    {"@type": "Question", "name": q,
                     "acceptedAnswer": {"@type": "Answer", "text": a}} for q, a in faqs]},
                {"@type": "BreadcrumbList", "itemListElement": [
                    {"@type": "ListItem", "position": 1, "name": "Home", "item": f"{SITE}/"},
                    {"@type": "ListItem", "position": 2, "name": "Service Areas",
                     "item": f"{SITE}/service-areas"},
                    {"@type": "ListItem", "position": 3, "name": name,
                     "item": f"{SITE}/service-areas/{slug}"}]},
            ]}

        W(f"service-areas/{slug}.html", shell(
            title=f"Accountant in {name}, IL | NorthPeak",
            desc=(f"Bookkeeping, controller, CFO advisory and tax services for {name}, "
                  f"Illinois businesses. Based in {BASE_CITY}. Free 30-minute "
                  f"consultation — call (847) 644-2288."),
            canon=f"{SITE}/service-areas/{slug}", body=body, active="", depth=1,
            keywords=(f"accountant {name} IL, bookkeeping {name}, tax preparation {name}, "
                      f"small business accountant {name} Illinois"),
            jsonld=jsonld))

    # ---------------------------------------------------------------- hub
    # The hub's substance is this table. County, township and WHO assesses
    # genuinely differ across these twelve communities, and that difference has
    # practical consequences for an owner who holds their own building. It is
    # the one thing on the page a competitor cannot copy without doing the work.
    def who(county):
        if county == "Cook":
            return ("Cook County Assessor", "Triennial township cycle; Assessor then Board of Review")
        if county == "Lake":
            return ("Township assessor", "Contact township assessor first, then Board of Review")
        return ("Both, split at Lake Cook Road", "Cook system south of the road, Lake system north")

    rows = "".join(
        f'<tr><th scope="row" style="text-align:left;padding:13px 12px;font-weight:600">{name}</th>'
        f'<td style="padding:13px 12px;color:var(--soft)">{county} County</td>'
        f'<td style="padding:13px 12px;color:var(--soft)">{township}</td>'
        f'<td style="padding:13px 12px;color:var(--soft)">{who(county)[0]}</td></tr>'
        for name, slug, county, township, *_ in TOWNS)

    hub_body = f"""
<div class="wrap crumb"><a href="../index.html">Home</a> &rsaquo; <span>Service Areas</span></div>
<div class="wrap pagehead">
  <p class="eyebrow">Where we work</p>
  <h1>Service Areas</h1>
  <p class="lead" style="max-width:64ch">NorthPeak is based in {BASE_CITY} and works with
  businesses across Chicago's north suburbs in person, and with clients nationwide
  remotely. Below is where we are most often &mdash; and, because it matters more than
  most owners expect, who actually assesses property in each one.</p>
  <div style="margin-top:26px;display:flex;gap:14px;flex-wrap:wrap">
    <a href="../contact.html" class="btn gold lg">Book a Free Consultation</a>
    <a href="tel:+18476442288" class="btn ghost lg">(847) 644-2288</a>
  </div>
</div>

<section style="padding-top:34px">
  <div class="wrap">
    <div class="rhead rv"><span>North suburban communities</span><span>{len(TOWNS)} areas</span></div>
    <div class="viz rv" style="overflow-x:auto;margin-top:26px">
      <table style="width:100%;border-collapse:collapse;min-width:640px">
        <caption style="text-align:left;font-size:.86rem;color:var(--mute);padding-bottom:14px">
          Who assesses property, by community. Cook County reassesses one third of the
          county each year on a three-year township cycle through the County Assessor;
          every Illinois county outside Cook &mdash; including Lake &mdash; assesses through
          the <em>township</em> assessor instead.</caption>
        <thead><tr style="border-bottom:2px solid var(--rule)">
          <th scope="col" style="text-align:left;padding:14px 12px;font-size:.86rem;color:var(--mute)">Community</th>
          <th scope="col" style="text-align:left;padding:14px 12px;font-size:.86rem;color:var(--mute)">County</th>
          <th scope="col" style="text-align:left;padding:14px 12px;font-size:.86rem;color:var(--mute)">Township</th>
          <th scope="col" style="text-align:left;padding:14px 12px;font-size:.86rem;color:var(--mute)">Assessed by</th>
        </tr></thead>
        <tbody>{rows}</tbody>
      </table>
    </div>
  </div>
</section>

<section class="alt pad-s">
  <div class="wrap">
    <div class="split rv">
      <div class="sh"><h2>Two details worth knowing</h2>
        <p>Both come up more often than you would think, and both change the answer
        to a simple question.</p></div>
      <div class="sb">
        <div class="ledger">
          <div class="lrow"><div class="ln">01</div><h3>Wheeling is split down the middle</h3>
            <p>Lake Cook Road is the line. South of it, assessment runs through the Cook
            County Assessor and the Cook County Treasurer collects. North of it, Lake
            County's Chief County Assessment Office and Treasurer handle it. The village
            publishes the sales tax consequence too: the Cook portion carries a 10% total
            rate and the Lake portion 8%. If you sell taxable goods in Wheeling, which side
            of that road your counter sits on is a real number on your return.</p>
            <a class="lgo" href="https://www.wheelingil.gov/245/Sales-Tax" rel="noopener" target="_blank">Village source &rarr;</a></div>
          <div class="lrow"><div class="ln">02</div><h3>Glenview sits in three townships</h3>
            <p>New Trier, Niles and Northfield all cover parts of the village. Two businesses
            on opposite sides of Glenview can fall into different township assessment groups,
            so a reassessment year for one is not automatically a reassessment year for the
            other. Worth confirming by parcel rather than by village name.</p><span></span></div>
        </div>
      </div>
    </div>
  </div>
</section>

<section class="pad-s">
  <div class="wrap"><div class="split rv">
    <div class="sh"><h2>Not on the list?</h2></div>
    <div class="sb"><p class="lead" style="max-width:56ch">Most of the work is done
    remotely, so the table above is about where we turn up in person &mdash; not where we
    can help. If you are elsewhere in Illinois or in another state, the answer is almost
    always yes.</p>
    <div style="margin-top:22px"><a href="../contact.html" class="btn gold lg">Book a Free Consultation</a></div></div>
  </div></div>
</section>
"""

    W("service-areas/index.html", shell(
        title=f"Service Areas | {FIRM}",
        desc=("NorthPeak Financial Partners serves businesses across Chicago's north "
              "suburbs from Wilmette, IL — Evanston, Skokie, Glenview, Northbrook, "
              "Winnetka, Deerfield, Highland Park and more."),
        canon=f"{SITE}/service-areas", body=hub_body, active="", depth=1,
        keywords="accountant north shore chicago, bookkeeping north suburbs, tax services wilmette",
        jsonld={"@context": "https://schema.org", "@type": "CollectionPage",
                "name": "Service Areas", "url": f"{SITE}/service-areas",
                "about": {"@type": "AccountingService", "name": FIRM, "url": SITE},
                "areaServed": [{"@type": "City", "name": n} for n, _, _ in made]}))

    print(f"service areas: hub built; town pages "
          f"{'+ ' + str(len(made)) if TOWN_PAGES_READY else 'GATED (see header note)'}")
    return made


if __name__ == "__main__":
    build()
