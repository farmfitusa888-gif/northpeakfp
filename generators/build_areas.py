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


# ---------------------------------------------------------------------------
# LOCAL GUIDES
#
# These replace the twelve near-identical town pages. Each is a genuinely
# different document about a real, verifiable local mechanic, rather than the
# same page with the town name swapped. They target the same local intent
# without the duplication that gets location pages ignored.
#
# LICENCE BOUNDARY, DELIBERATE AND LOAD-BEARING: Chaudhry Ahmad is not a CPA and
# not an attorney. Illinois property tax appeals are filed by the owner or by an
# attorney. Every one of these pages says what he does (read the numbers, model
# the impact, get the books to support a filing) and what he does not (file the
# appeal, act as counsel), and points the reader to the official process. That
# boundary is the point, not a disclaimer bolted on the end.
#
# VERIFIED SOURCES
#   Cook County north-suburban triennial group and 2016/2019/2022/2025 cycle
#     -- cookcountyassessoril.gov, corroborated by KSN Law and Younis Law Group
#   Cook County Board of Review .......... cookcountyboardofreview.com
#   Lake County appeal process ........... lakecountyil.gov/503/Appeal-Process
#   Illinois PTAB ........................ ptab.illinois.gov/getstarted.html
#   Wheeling split + sales tax rates ..... wheelingil.gov/466, wheelingil.gov/245
# No deadline DATES are stated anywhere: they move annually and a stale date on
# a tax page is a liability. Structure is described; dates are linked.
# ---------------------------------------------------------------------------

COOK_TOWNS = [t[0] for t in TOWNS if t[2] == "Cook"]

LOCAL_GUIDES = [
  ("cook-county-property-tax-appeals",
   "Cook County Property Tax Appeals: What North Suburban Business Owners Should Know",
   "Cook County reassesses the north suburbs every three years. What that means if "
   "your business owns its building, and where an accountant stops and an attorney starts.",
   "cook county property tax appeal, north suburbs reassessment, business property tax illinois",
   f"""
<p class="lead">If your business owns the building it operates from &mdash; or you are on a
lease that passes the property tax through to you &mdash; the Cook County reassessment cycle
is one of the few large, predictable costs you can actually do something about. Most owners
find out about it after the bill arrives, which is the one point in the process where the
options are worst.</p>

<h2>The cycle is fixed, and every town we work in is on the same one</h2>
<p>Cook County does not reassess everything at once. It splits the county into three groups
&mdash; the City of Chicago, the north and northwest suburbs, and the south and west suburbs
&mdash; and reassesses one group each year, so any given property is reassessed every three
years.</p>
<p>Every Cook County community in our service area sits in the <strong>north suburban
group</strong>: {", ".join(COOK_TOWNS[:-1])} and {COOK_TOWNS[-1]}. That group was reassessed
in 2016, 2019, 2022 and 2025, which puts the next one in <strong>2028</strong>. If you own
property in any of those towns, you are on the same clock as every one of your neighbours.</p>

<h2>Why the year matters more than most people expect</h2>
<p>In a reassessment year you get two separate opportunities to contest a value: first with
the <a href="https://www.cookcountyassessoril.gov/" rel="noopener" target="_blank">Assessor's
office</a>, and then, independently, with the
<a href="https://www.cookcountyboardofreview.com/" rel="noopener" target="_blank">Board of
Review</a>. In an off year you generally get one &mdash; the Board of Review window only.</p>
<p>Both windows are short, they open by township rather than county-wide, and they do not
move because you were busy. That is the entire practical argument for knowing which year you
are in before it arrives rather than after.</p>

<h2>What actually moves an assessment</h2>
<p>An appeal is an evidence exercise, not an argument about whether taxes are too high. The
grounds that tend to matter:</p>
<ul>
  <li><strong>Comparable properties.</strong> Similar buildings, assessed lower. This is the
  most common basis and the most work.</li>
  <li><strong>Factual error.</strong> The record says your building is bigger than it is, or
  the wrong class, or counts space that no longer exists. These are the cleanest cases.</li>
  <li><strong>Vacancy.</strong> For income-producing commercial property that sat empty,
  documented occupancy matters.</li>
</ul>
<p>All three depend on records you either have or do not have. That is where a bookkeeping
problem quietly becomes a tax problem: if your fixed asset schedule, lease documents and
occupancy history are a mess, the evidence is expensive to assemble under a deadline.</p>

<h2>Where we help, and where we stop</h2>
<p>We are accountants, not attorneys. We do not file property tax appeals and we do not act
as counsel. What we do is the part that sits upstream of the filing: keeping the fixed asset
and lease records in a state where evidence can actually be pulled from them, modelling what
a given assessment change does to your cash position across the year, and telling you plainly
whether the amount at stake justifies the cost of pursuing it. When a filing is worth making,
we will say so and point you to a property tax attorney &mdash; several work in these
townships specifically.</p>
<p>Illinois also runs a state-level
<a href="http://www.ptab.illinois.gov/getstarted.html" rel="noopener" target="_blank">Property
Tax Appeal Board</a> for owners who want to go further than the county Board of Review.</p>
""",
   ["cash-flow-management", "business-expense-categories", "when-to-hire-accountant"]),

  ("cook-county-vs-lake-county",
   "Cook County vs. Lake County: What Changes for a Business at the Line",
   "The county line runs through the north suburbs. Who assesses your property, how you "
   "appeal, and what you charge in sales tax can all change within a few miles.",
   "cook county vs lake county business, lake county illinois property assessment, sales tax difference",
   """
<p class="lead">Northbrook and Deerfield share a border. So do Highland Park and the towns
below it. A business a mile apart from another can be operating under a different assessment
authority, a different appeal procedure, and a different sales tax rate &mdash; and nothing
about the neighbourhood tells you which.</p>

<h2>Who values your property</h2>
<p>This is the difference most owners never hear about until they try to contest something.</p>
<ul>
  <li><strong>Cook County</strong> is the exception in Illinois. A single <em>county</em>
  assessor values property, working through a three-year township cycle.</li>
  <li><strong>Lake County</strong> &mdash; like every other Illinois county &mdash; assesses
  through the <strong>township assessor</strong>. There are many of them, and yours depends on
  your township, not your village.</li>
</ul>
<p>The practical consequence is that the first phone call is different. In Cook, you are
dealing with a county office and its published township calendar. In Lake, the county
<a href="https://www.lakecountyil.gov/503/Appeal-Process" rel="noopener" target="_blank">asks
you to contact your township assessor before filing</a> with the Board of Review &mdash; and
for factual-error and commercial-vacancy appeals, that contact is required rather than
suggested.</p>

<h2>Wheeling is the clearest illustration, because it is both</h2>
<p>The Village of Wheeling straddles the line, and the boundary is
<strong>Lake Cook Road</strong>. South of it, assessment runs through the Cook County Assessor
and the Cook County Treasurer collects. North of it, Lake County's Chief County Assessment
Office assesses and the Lake County Treasurer collects. Same village, same village hall, two
systems.</p>
<p>It shows up in sales tax too. The village publishes the numbers itself: the
<a href="https://www.wheelingil.gov/245/Sales-Tax" rel="noopener" target="_blank">Cook County
portion of Wheeling carries a 10% total sales tax rate and the Lake County portion 8%</a>. On
a retail or restaurant business that is not a rounding difference &mdash; it is two points of
every taxable dollar, on the same street.</p>

<h2>What this changes if you are choosing a location</h2>
<p>If you are signing a lease or buying a building near the line, three questions are worth
answering before you sign rather than after:</p>
<ul>
  <li>Which county and township is the parcel actually in? Village boundaries and township
  boundaries do not match, and in Glenview the village spans three townships.</li>
  <li>If you sell taxable goods, what is the combined rate at that exact address? In Wheeling
  this is a two-point swing.</li>
  <li>If you will own the property, which assessment and appeal process applies, and when is
  the next reassessment?</li>
</ul>
<p>None of these are hard questions. They are just easier to answer before money moves.</p>

<h2>Where we help</h2>
<p>We are not attorneys and we do not file appeals or give legal advice on property matters.
What we do is model the actual cash difference between two locations &mdash; rate differences,
assessment exposure, and the timing of when each hits &mdash; so the decision is made on a
number rather than a hunch.</p>
""",
   ["cash-flow-management", "sales-tax-guide", "choosing-business-entity"]),

  ("wheeling-sales-tax-lake-cook-road",
   "Sales Tax in Wheeling: Which Side of Lake Cook Road Are You On?",
   "Wheeling is split between Cook and Lake counties at Lake Cook Road, and the total "
   "sales tax rate differs by two points across it. What that means if you sell there.",
   "wheeling illinois sales tax rate, lake cook road county line, cook county sales tax rate",
   """
<p class="lead">Wheeling is one of the few places in the north suburbs where a single road
changes which county you file under, who assesses your building, and what you charge a
customer at the register. That road is <strong>Lake Cook Road</strong>.</p>

<h2>The split, as the village describes it</h2>
<p>The Village of Wheeling sits in both Cook and Lake counties. South of Lake Cook Road,
property assessment runs through the Cook County Assessor and taxes are collected by the Cook
County Treasurer. North of it, Lake County's Chief County Assessment Office assesses and the
Lake County Treasurer collects.</p>
<p>The village also publishes the sales tax consequence directly: the
<a href="https://www.wheelingil.gov/245/Sales-Tax" rel="noopener" target="_blank">Cook County
portion of Wheeling carries a total sales tax rate of 10%, and the Lake County portion 8%</a>.</p>

<h2>Two points is not a rounding difference</h2>
<p>For a business selling taxable goods, the rate is not a cost you absorb &mdash; you collect
and remit it. But it is a real competitive fact. A customer comparing two shops a few minutes
apart pays a different total, and for larger-ticket items that difference is visible on the
receipt. If you are choosing between two Wheeling storefronts, the county line belongs in the
comparison alongside the rent.</p>

<h2>What to actually do about it</h2>
<ul>
  <li><strong>Confirm the address, not the town.</strong> "Wheeling" does not determine the
  rate. The parcel does. Verify which side of Lake Cook Road your location sits on before you
  configure anything.</li>
  <li><strong>Set the rate at the point of sale correctly from day one.</strong> Under-collecting
  is not a discount you gave &mdash; it is a liability you still owe, and it compounds quietly
  until someone looks.</li>
  <li><strong>Check it again if you move, add a second location, or start shipping.</strong>
  Destination rules can change which rate applies to a given sale.</li>
  <li><strong>Keep the returns and the books reconciled to each other.</strong> Sales tax
  problems are almost always discovered as a difference between what the register says and
  what was filed.</li>
</ul>

<h2>Where we help</h2>
<p>We are not a sales tax filing service and we do not give legal opinions on nexus. What we
do is make sure the books reconcile to what was actually collected and remitted, that the
liability is visible on your balance sheet rather than a surprise, and that if you are picking
between locations, the rate difference is in the model before you sign.</p>
<p>For the underlying rules on when you owe and how collection works, our
<a href="../articles/sales-tax-guide.html">guide to sales tax for small business</a> covers
the general mechanics.</p>
""",
   ["sales-tax-guide", "bookkeeping-basics", "cash-flow-management"]),
]

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


    # ------------------------------------------------------------ local guides
    for slug, title, desc, kw, body_html, reads in LOCAL_GUIDES:
        rel = [ART_BY_SLUG[r] for r in reads if r in ART_BY_SLUG]
        read_rows = "".join(
            f'<a class="entry" href="../articles/{a["slug"]}.html">'
            f'<span class="ec">{html.escape(a["cat"])}</span>'
            f'<div><h3>{html.escape(a["title"])}</h3></div>'
            f'<span class="er">{a["read"]}</span></a>' for a in rel)

        body = f"""
<div class="wrap crumb"><a href="../index.html">Home</a> &rsaquo;
  <a href="index.html">Service Areas</a> &rsaquo; <span>{html.escape(title.split(":")[0])}</span></div>
<div class="wrap pagehead">
  <p class="eyebrow">North suburbs &middot; Guide</p>
  <h1>{html.escape(title)}</h1>
</div>
<section style="padding-top:26px"><div class="aw abody">{body_html}</div></section>
<section class="alt pad-s">
  <div class="wrap">
    <div class="split rv">
      <div class="sh"><h2>Want this looked at properly?</h2></div>
      <div class="sb"><p class="lead" style="max-width:54ch">A free 30-minute call gets you a
      straight read on whether any of this is worth your time in your situation &mdash;
      including if the answer is that it is not.</p>
      <div style="margin-top:22px"><a href="../contact.html" class="btn gold lg">Book a Free Consultation</a></div></div>
    </div>
  </div>
</section>
<section class="pad-s">
  <div class="wrap">
    <div class="rhead rv"><span>Related reading</span><span>Guides</span></div>
    <div class="elist rv" style="margin-top:26px">{read_rows}</div>
  </div>
</section>
"""
        W(f"service-areas/{slug}.html", shell(
            title=(title[:57] + "...") if len(title) > 60 else title,
            desc=desc, canon=f"{SITE}/service-areas/{slug}", body=body,
            active="", depth=1, keywords=kw, og_type="article",
            jsonld={"@context": "https://schema.org", "@type": "Article",
                    "headline": title, "description": desc,
                    "author": {"@type": "Person", "name": G.FOUNDER,
                               "jobTitle": "Founder & Principal",
                               "worksFor": {"@type": "Organization", "name": FIRM, "url": SITE}},
                    "publisher": {"@type": "Organization", "name": FIRM, "url": SITE},
                    "datePublished": G.PUBDATE, "dateModified": G.PUBDATE,
                    "mainEntityOfPage": f"{SITE}/service-areas/{slug}",
                    "about": {"@type": "AdministrativeArea", "name": "Cook and Lake Counties, Illinois"}}))
    print(f"local guides: {len(LOCAL_GUIDES)}")

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

    guide_rows = "".join(
        f'<a class="entry" href="{g[0]}.html"><span class="ec">Local guide</span>'
        f'<div><h3>{html.escape(g[1])}</h3><p>{html.escape(g[2][:120])}&hellip;</p></div>'
        f'<span class="er">Read &rarr;</span></a>' for g in LOCAL_GUIDES)

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
  <div class="wrap">
    <div class="rhead rv"><span>Local guides</span><span>{len(LOCAL_GUIDES)}</span></div>
    <div class="elist rv" style="margin-top:26px">{guide_rows}</div>
  </div>
</section>

<section class="alt pad-s">
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
        desc=("Accounting, bookkeeping and tax services for businesses across Chicago's "
              "north suburbs — Evanston, Skokie, Glenview, Northbrook and more, "
              "from Wilmette, IL."),
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
