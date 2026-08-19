#!/usr/bin/env python3
import os, sys, json, html, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
from build_site import shell, W, ROOT, SITE, FIRM, EMAIL, CAL_PLACEHOLDER, FORM_PLACEHOLDER
import generate_articles_northpeak as G

ARTS = G.ARTICLES
CATS = sorted({a["cat"] for a in ARTS})
TICK = ('<svg class="tick" width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" '
        'stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round"><polyline points="20 6 9 17 4 12"/></svg>')

def crumb(items, depth=0):
    p = "../" * depth
    out = []
    for i, (n, h) in enumerate(items):
        out.append(f'<a href="{p}{h}">{n}</a>' if h else f'<span>{n}</span>')
    return f'<div class="wrap crumb">{" &rsaquo; ".join(out)}</div>'

# ============================================================ SERVICES
TIERS = [
    ("starter", "Starter Package", "Quoted", "for your scope",
     "For small businesses that need clean, reliable financials",
     ["Bookkeeping &amp; transaction categorization", "Monthly financial reports",
      "Bank &amp; account reconciliations", "Basic profit &amp; loss reporting",
      "Individual &amp; business tax preparation"],
     "Startups, solopreneurs, small service businesses", False),
    ("growth", "Growth Package", "Quoted", "for your scope",
     "For growing businesses that need structure and visibility",
     ["<strong>Everything in Starter, plus:</strong>", "Controller-level oversight",
      "Structured monthly close process", "Financial statement preparation",
      "Budget vs. actual reporting", "KPI &amp; performance tracking", "Monthly financial review call"],
     "$500K&ndash;$5M revenue businesses scaling operations", True),
    ("cfo", "CFO Package", "Quoted", "for your scope",
     "For established businesses that need strategic financial leadership",
     ["<strong>Everything in Growth, plus:</strong>", "Fractional CFO advisory",
      "Cash flow forecasting &amp; planning", "Strategic budgeting &amp; modeling",
      "Profitability &amp; margin analysis", "Executive-level financial reporting",
      "Weekly or bi-weekly strategy calls", "Growth &amp; decision support"],
     "$2M&ndash;$100M revenue companies needing financial leadership", False),
]

tier_html = ""
for tid, name, price, per, who, feats, fit, feat in TIERS:
    cls = "tier feat" if feat else "tier"
    tag = '<span class="tag">Most Popular</span>' if feat else ""
    pcls = "price quote" if price == "Custom" else "price"
    tier_html += f"""
      <div class="{cls} rv" id="{tid}">{tag}
        <h2>{name}</h2>
        <p class="who">{who}</p>
        <div class="{pcls}">{price}<small> {per}</small></div>
        <ul>{"".join(f"<li>{f}</li>" for f in feats)}</ul>
        <p class="fit"><strong>Best for:</strong> {fit}</p>
        <a href="contact.html?plan={tid}" class="btn{' gold' if feat else ' ghost'}" style="justify-content:center">
          {"Request a Quote" if price=="Custom" else "Get Started"}</a>
      </div>"""

svc_body = f"""
{crumb([("Home","index.html"),("Services",None)])}
<div class="wrap pagehead">
  <p class="eyebrow">Services &amp; Pricing</p>
  <h1>Three levels of financial support</h1>
  <p class="lead" style="max-width:640px">Start where you are. Every engagement is scoped to your business,
  and you can move up a tier whenever complexity grows.</p>
</div>
<section style="padding-top:44px">
  <div class="wrap">
    <div class="grid g3" style="align-items:stretch">{tier_html}</div>
    <p style="text-align:center;color:var(--mute);font-size:.88rem;margin-top:30px">
      Every engagement is quoted individually based on your scope.
      <a href="contact.html">Book a free consultation</a> and we'll tell you honestly which level fits
      &mdash; including if you don't need us yet.</p>
  </div>
</section>

<section class="alt">
  <div class="wrap">
    <div class="sec-head rv"><p class="eyebrow">Compare</p><h2>What's included at each level</h2></div>
    <div class="viz rv" style="overflow-x:auto">
      <table style="width:100%;border-collapse:collapse;min-width:560px">
        <thead><tr style="border-bottom:2px solid var(--rule)">
          <th style="text-align:left;padding:14px 10px;font-size:.86rem;color:var(--mute);font-weight:600">Capability</th>
          <th style="padding:14px 10px;font-size:.9rem">Starter</th>
          <th style="padding:14px 10px;font-size:.9rem;color:var(--gold)">Growth</th>
          <th style="padding:14px 10px;font-size:.9rem">CFO</th></tr></thead>
        <tbody>
        {"".join(f'''<tr style="border-bottom:1px solid var(--rule)">
          <td style="padding:13px 10px;font-size:.92rem;color:var(--soft)">{r[0]}</td>
          <td style="text-align:center;padding:13px 10px">{TICK if r[1] else '<span style="color:var(--rule)">&mdash;</span>'}</td>
          <td style="text-align:center;padding:13px 10px">{TICK if r[2] else '<span style="color:var(--rule)">&mdash;</span>'}</td>
          <td style="text-align:center;padding:13px 10px">{TICK if r[3] else '<span style="color:var(--rule)">&mdash;</span>'}</td></tr>'''
        for r in [
          ("Bookkeeping &amp; categorization",1,1,1),("Bank reconciliations",1,1,1),
          ("Monthly financial reports",1,1,1),
          ("Individual &amp; business tax preparation",1,1,1),
          ("Controller-level oversight",0,1,1),("Structured monthly close",0,1,1),
          ("Budget vs. actual reporting",0,1,1),("KPI &amp; performance tracking",0,1,1),
          ("Monthly review call",0,1,1),("Fractional CFO advisory",0,0,1),
          ("Cash flow forecasting",0,0,1),("Strategic modeling &amp; budgeting",0,0,1),
          ("Profitability &amp; margin analysis",0,0,1),("Weekly/bi-weekly strategy calls",0,0,1)])}
        </tbody></table>
    </div>
  </div>
</section>

<section>
  <div class="wrap"><div class="split rv">
    <div class="sh"><h2>Not sure where you fit?</h2></div>
    <div class="sb"><p class="lead" style="max-width:54ch">Tell us about your business in a free 30-minute call and we'll recommend the right level &mdash;
    or tell you if you're not ready for one yet.</p>
      <div style="margin-top:22px"><a href="contact.html" class="btn gold lg">Book a Free Consultation</a></div></div>
  </div></div>
</section>
"""

W("services.html", shell(
    title=f"Services &amp; Pricing | {FIRM}",
    desc="Compare NorthPeak's Starter, Growth, and CFO packages: bookkeeping, controller services, and fractional CFO advisory with transparent monthly pricing.",
    canon=f"{SITE}/services", body=svc_body, active="Services",
    keywords="accounting packages, bookkeeping pricing, controller services, fractional CFO pricing",
    jsonld={"@context":"https://schema.org","@type":"Service","serviceType":"Accounting and CFO Advisory",
            "provider":{"@type":"AccountingService","name":FIRM,"url":SITE},
            "hasOfferCatalog":{"@type":"OfferCatalog","name":"Advisory Packages","itemListElement":[
              {"@type":"Offer","name":"Starter Package",
               "description":"Bookkeeping, reconciliations, monthly reports, and individual and business tax preparation."},
              {"@type":"Offer","name":"Growth Package","description":"Controller-level oversight, monthly close, KPI tracking."},
              {"@type":"Offer","name":"CFO Package","description":"Fractional CFO advisory, forecasting, strategic modeling."}]}}))

# ============================================================ ABOUT
about_body = f"""
{crumb([("Home","index.html"),("About",None)])}
<div class="wrap pagehead">
  <p class="eyebrow">About NorthPeak</p>
  <h1>Strategic consulting, elevated</h1>
  <p class="lead" style="max-width:660px">NorthPeak Financial Partners was created to give growing
  businesses the financial clarity, structure, and strategic insight normally reserved for large enterprises.</p>
</div>

<section style="padding-top:48px">
  <div class="wrap grid g2" style="gap:52px;align-items:start">
    <div class="rv">
      <h2 style="font-size:1.7rem;margin-bottom:16px">Why NorthPeak exists</h2>
      <p style="color:var(--soft);margin-bottom:16px">Most businesses don't struggle because they lack
      revenue. They struggle because they lack financial clarity &mdash; the reporting is late, the
      categories are inconsistent, and nobody can answer simple questions about margin or runway with confidence.</p>
      <p style="color:var(--soft);margin-bottom:16px">We help owners move beyond basic bookkeeping and
      gain a real understanding of their financial performance, so they can make confident, data-driven decisions.</p>
      <p style="color:var(--soft)"><strong>Chaudhry Ahmad</strong>, Founder &amp; Principal, brings controller-level experience helping businesses improve
      financial clarity, strengthen reporting processes, and make better strategic decisions through
      accurate data and structured reporting. NorthPeak was built to bring that level of financial
      leadership to businesses ready to scale.</p>
      <p style="color:var(--soft);font-size:.92rem;border-top:1px solid var(--rule);padding-top:16px;margin-top:18px">
      Reach Chaudhry directly at <a href="tel:+18476442288">(847) 644-2288</a> or
      <a href="mailto:info@northpeakfp.com">info@northpeakfp.com</a>.</p>
    </div>
    <div class="rv">
      <figure style="margin:0 0 22px;background:var(--card);border:1px solid var(--rule);
        border-radius:var(--r);overflow:hidden;box-shadow:var(--shadow)">
        <img src="assets/chaudhry-ahmad-about.jpg" width="640" height="800"
             alt="Chaudhry Ahmad, Founder and Principal of NorthPeak Financial Partners"
             style="width:100%;height:auto;display:block" loading="lazy">
        <figcaption style="padding:16px 20px;border-top:1px solid var(--rule)">
          <strong style="display:block;font-family:'Fraunces',serif;font-size:1.15rem;
            color:var(--ink-2)">Chaudhry Ahmad</strong>
          <span style="font-size:.88rem;color:var(--accent)">Founder &amp; Principal</span>
        </figcaption>
      </figure>
      <div class="viz">
      <h3>What you get with NorthPeak</h3>
      <p class="cap">The four outcomes every engagement is built around</p>
      <ul style="list-style:none">
        {"".join(f'<li style="display:flex;gap:12px;padding:14px 0;border-bottom:1px solid var(--rule);align-items:flex-start"><span style="color:var(--accent);flex-shrink:0;margin-top:3px">{TICK}</span><span style="font-size:.95rem;color:var(--soft)"><strong style="color:var(--ink-2)">{t}</strong><br>{d}</span></li>' for t,d in [
          ("Accurate, timely reporting","Financials that close on schedule, every month."),
          ("Clear performance visibility","You know your margins, trends, and drivers &mdash; not just your balance."),
          ("Strong internal controls","Process safeguards that scale with the business."),
          ("Strategic growth guidance","Decision support grounded in your actual numbers.")])}
      </ul>
      </div>
    </div>
  </div>
</section>

<section class="alt">
  <div class="wrap">
    <div class="sec-head rv"><p class="eyebrow">Who We Serve</p>
      <h2>Built for businesses outgrowing basic accounting</h2>
      <p class="lead">We work with small to mid-sized businesses that need more than data entry.</p></div>
    <div class="grid g3">
      {"".join(f'<div class="card rv"><h3 style="font-size:1.12rem">{t}</h3><p>{d}</p></div>' for t,d in [
        ("Individuals &amp; Families","Tax preparation and year-round planning."),
        ("Service-Based Businesses","Bookkeeping, accounting, and tax compliance."),
        ("Professional Firms","Tax planning, preparation, and advisory services."),
        ("Manufacturing &amp; Distribution","Cost accounting, bookkeeping, and tax strategy."),
        ("Startups &amp; Scaling Orgs","Accounting setup, bookkeeping, and planning for growth."),
        ("Owner-Operated Businesses","Bookkeeping, tax filing, and ongoing tax planning.")])}
    </div>
    <p style="text-align:center;color:var(--soft);margin-top:34px;font-size:1.02rem">
      If your business is growing but your financial visibility isn't keeping up, we bridge that gap.</p>
  </div>
</section>

<section class="dark">
  <div class="wrap narrow" style="text-align:center">
    <p class="eyebrow">Our Mission</p>
    <h2 style="font-size:clamp(1.6rem,3.4vw,2.2rem);margin-bottom:20px;line-height:1.3">
      To deliver financial clarity and strategic guidance that helps businesses grow with confidence,
      control, and long-term stability.</h2>
    <p style="margin-bottom:32px">We believe strong financial systems are the foundation of every
    successful business &mdash; and that businesses simply perform better when they understand their numbers.</p>
    <a href="contact.html" class="btn gold lg">Work With Us</a>
  </div>
</section>
"""
W("about.html", shell(
    title=f"About | {FIRM}",
    desc="NorthPeak Financial Partners brings controller-level financial leadership to growing businesses: accurate reporting, clear visibility, and strategic guidance.",
    canon=f"{SITE}/about", body=about_body, active="About",
    keywords="about northpeak financial partners, controller services, financial consulting firm",
    jsonld={"@context":"https://schema.org","@type":"AboutPage","name":f"About {FIRM}",
            "url":f"{SITE}/about",
            "about":{"@type":"AccountingService","name":FIRM,"url":SITE,
                     "founder":{"@type":"Person","name":G.FOUNDER,"jobTitle":"Founder & Principal",
                                "image":f"{SITE}/assets/chaudhry-ahmad-headshot.jpg"},
                     "image":f"{SITE}/assets/chaudhry-ahmad-headshot.jpg",
                     "telephone":"+1-847-644-2288",
                     "address":{"@type":"PostalAddress","addressLocality":"Wilmette",
                                "addressRegion":"IL","addressCountry":"US"}}}))

# ============================================================ ARTICLES HUB
chips = '<button class="chip on" data-f="all">All topics</button>' + "".join(
    f'<button class="chip" data-f="{html.escape(c)}">{html.escape(c)}</button>' for c in CATS)
# The hub is an index, so it is built as one — a ruled list rather than a deck
# of shadowed tiles. Same data, same filter hooks (data-cat / data-s), and it
# scales to 50+ entries without turning into an endless wall of boxes.
cards = "".join(f"""<a class="entry art" href="{a['slug']}.html" data-cat="{html.escape(a['cat'])}"
   data-s="{html.escape((a['title']+' '+a['desc']+' '+a['keywords']).lower())}">
   <span class="ec">{html.escape(a['cat'])}</span>
   <div><h3>{html.escape(a['title'])}</h3>
   <p>{html.escape(a['desc'][:130])}&hellip;</p></div>
   <span class="er">{a['read']}</span></a>""" for a in ARTS)

hub_body = f"""
{crumb([("Home","index.html"),("Articles",None)], depth=1)}
<div class="wrap pagehead">
  <p class="eyebrow">Insights &amp; Guides</p>
  <h1>Financial guidance, written plainly</h1>
  <p class="lead" style="max-width:640px">{len(ARTS)} practical guides on tax, bookkeeping, payroll,
  entity structure, and financial strategy &mdash; for business owners and individuals.</p>
</div>
<section style="padding-top:40px">
  <div class="wrap">
    <label for="asearch" class="visually-hidden" style="position:absolute;left:-9999px">Search articles</label>
    <input class="search" id="asearch" type="search" placeholder="Search articles &mdash; try &lsquo;deductions&rsquo;, &lsquo;payroll&rsquo;, &lsquo;LLC&rsquo;&hellip;">
    <div class="filters">{chips}</div>
    <h2 class="vh">All guides</h2>
    <div class="elist">{cards}</div>
    <p id="nores" style="display:none;text-align:center;color:var(--mute);padding:44px 0">
      No articles match that search. Try a different term or clear the filter.</p>
  </div>
</section>
<section class="alt pad-s">
  <div class="wrap"><div class="split rv">
    <div class="sh"><h2>Questions about your own situation?</h2></div>
    <div class="sb">
      <p class="lead" style="max-width:52ch">Articles are general guidance. A 30-minute call gets you answers specific to your business.</p>
      <div style="margin-top:22px"><a href="../contact.html" class="btn gold lg">Book a Free Consultation</a></div>
    </div>
  </div></div>
</section>
"""
W("articles/index.html", shell(
    title=f"Articles &amp; Guides | {FIRM}",
    desc=f"{len(ARTS)} plain-English guides on small business tax, bookkeeping, payroll, entity structure, and financial strategy from NorthPeak Financial Partners.",
    canon=f"{SITE}/articles", body=hub_body, active="Articles", depth=1,
    keywords="small business tax articles, bookkeeping guides, accounting resources",
    jsonld={"@context":"https://schema.org","@type":"CollectionPage","name":"Articles & Guides",
            "url":f"{SITE}/articles","hasPart":[
              {"@type":"Article","headline":a["title"],"url":f"{SITE}/articles/{a['slug']}"} for a in ARTS]}))

# ============================================================ RESOURCES
res_body = f"""
{crumb([("Home","index.html"),("Resources",None)])}
<div class="wrap pagehead">
  <p class="eyebrow">Free Tools</p>
  <h1>Resources for business owners</h1>
  <p class="lead" style="max-width:620px">Practical tools and checklists you can use right now &mdash;
  no signup required.</p>
</div>
<section style="padding-top:44px">
  <div class="wrap grid g2" style="gap:36px;align-items:start">
    <div class="calc rv">
      <h2>Clarity Value Estimator</h2>
      <p class="sub">Estimate what disorganized financials cost you annually</p>
      <label for="rev">Annual revenue</label>
      <input type="range" id="rev" min="100000" max="10000000" step="50000" value="1200000">
      <div class="val" id="revV">$1,200,000</div>
      <label for="hrs">Hours on financial admin monthly</label>
      <input type="range" id="hrs" min="2" max="60" step="1" value="21">
      <div class="val" id="hrsV">21 hrs/month</div>
      <div class="calc-out">
        <div class="big" id="outTotal">$0</div>
        <div class="lbl">Estimated annual value recovered</div>
        <div style="display:flex;gap:24px;margin-top:18px;flex-wrap:wrap">
          <div><div style="font-family:Fraunces,serif;font-size:1.2rem;color:#fff" id="outTime">$0</div>
            <div style="font-size:.76rem;color:#a9c4b9">Time reclaimed</div></div>
          <div><div style="font-family:Fraunces,serif;font-size:1.2rem;color:#fff" id="outBooks">$0</div>
            <div style="font-size:.76rem;color:#a9c4b9">Cleaner financials</div></div>
        </div>
      </div>
      <p class="disc">Estimate only. Assumes $75/hour owner opportunity cost and 1.2% expense recapture.
      Not a guarantee of results or a substitute for professional advice.</p>
    </div>
    <div class="rv">
      <div class="viz" style="margin-bottom:24px">
        <h2>Month-End Close Checklist</h2>
        <p class="cap">Run this every month and tax season stops being an event</p>
        <ul style="list-style:none">
        {"".join(f'<li style="display:flex;gap:11px;padding:10px 0;border-bottom:1px solid var(--rule);font-size:.93rem;color:var(--soft)"><span style="color:var(--accent);flex-shrink:0">{TICK}</span>{x}</li>' for x in [
          "Reconcile every bank and credit card account",
          "Categorize all uncategorized transactions",
          "Review and clear the suspense/ask-my-accountant account",
          "Record accruals, prepaids, and depreciation",
          "Verify payroll posted correctly",
          "Review AR aging and follow up on overdue invoices",
          "Review AP and upcoming obligations",
          "Compare actuals against budget and note variances",
          "Produce P&amp;L, balance sheet, and cash flow statement",
          "Save a PDF snapshot of all three statements"])}
        </ul>
      </div>
      <div class="viz">
        <h2>Records Retention Quick Guide</h2>
        <p class="cap">General guidance &mdash; confirm specifics for your situation</p>
        <ul style="list-style:none">
        {"".join(f'<li style="display:flex;justify-content:space-between;gap:16px;padding:11px 0;border-bottom:1px solid var(--rule);font-size:.92rem"><span style="color:var(--soft)">{k}</span><strong style="color:var(--ink-2);white-space:nowrap">{v}</strong></li>' for k,v in [
          ("Tax returns &amp; supporting docs","3&ndash;7 years"),("Payroll records","4+ years"),
          ("Bank &amp; credit card statements","3&ndash;7 years"),("Receipts for deductions","3&ndash;7 years"),
          ("Asset purchase records","Life of asset + 3 yrs"),("Corporate formation docs","Permanently")])}
        </ul>
      </div>
    </div>
  </div>
</section>
<section class="alt">
  <div class="wrap">
    <div class="sec-head rv"><p class="eyebrow">Deep Dives</p><h2>Start with these guides</h2></div>
    <div class="arts">
      {"".join(f'''<a class="art" href="articles/{a["slug"]}.html">
        <span class="cat">{html.escape(a["cat"])}</span><h3>{html.escape(a["title"])}</h3>
        <p>{html.escape(a["desc"][:120])}&hellip;</p><span class="rd">{a["read"]}</span></a>'''
        for a in [ARTS[3], ARTS[2], ARTS[10], ARTS[7]])}
    </div>
  </div>
</section>
"""
W("resources.html", shell(
    title=f"Free Tools &amp; Resources | {FIRM}",
    desc="Free tools for business owners: a financial clarity value estimator, month-end close checklist, and records retention guide from NorthPeak Financial Partners.",
    canon=f"{SITE}/resources", body=res_body, active="Resources",
    keywords="month end close checklist, records retention guide, small business financial tools"))

# ============================================================ CONTACT
FAQS = [
    ("How quickly will I hear back?", "Every inquiry gets a reply within one business day. If it's "
     "urgent, call (847) 644-2288 directly."),
    ("What happens on the first call?", "It's a free 30-minute conversation about your business, your "
     "current books, and where the gaps are. No pitch deck &mdash; we'll tell you honestly what would help most, "
     "including if you don't need us yet."),
    ("Do I need to switch accounting software?", "Usually not. We work with the major platforms and will "
     "tell you plainly if your current setup is holding you back before recommending any change."),
    ("How is pricing structured?", "Every engagement is quoted individually after the discovery call, "
     "because scope depends on transaction volume, entity count, complexity, and how much clean-up is "
     "needed. There is no one-size-fits-all package price. You'll receive a fixed figure in writing "
     "before any work begins &mdash; no hourly surprises."),
    ("Can you clean up books that are behind?", "Yes &mdash; catch-up and clean-up work is common. We'll scope "
     "it separately from ongoing service so you know exactly what the one-time effort costs."),
    ("Do you work with businesses outside your state?", "Yes. Engagements are handled remotely with "
     "scheduled video reviews, so location isn't a constraint."),
]
faq_html = "".join(f'<details class="faq"><summary>{q}</summary><p>{a}</p></details>' for q, a in FAQS)

contact_body = f"""
{crumb([("Home","index.html"),("Contact",None)])}
<div class="wrap pagehead">
  <p class="eyebrow">Get Started</p>
  <h1>Request a free consultation</h1>
  <p class="lead" style="max-width:620px">A 30-minute conversation about your business and your numbers.
  No obligation, no pressure &mdash; just a clear read on where you stand. We reply to every message
  within one business day.</p>
</div>

<section style="padding-top:44px">
  <div class="wrap grid g2" style="gap:40px;align-items:start">

    <div class="rv">
      <div class="viz" style="margin-bottom:22px">
        <h2>What happens next</h2>
        <p class="cap">From first message to first report</p>
        <ol style="list-style:none;counter-reset:cs;margin:0">
        <li style="counter-increment:cs;position:relative;padding:0 0 20px 44px;border-left:2px solid var(--rule);margin-left:13px">
            <span style="position:absolute;left:-15px;top:0;width:28px;height:28px;border-radius:50%;background:var(--accent);color:#fff;display:grid;place-items:center;font-size:.8rem;font-weight:700">1</span>
            <strong style="color:var(--ink-2);font-size:.97rem">You send the form</strong>
            <span style="display:block;color:var(--soft);font-size:.91rem;margin-top:3px">Takes two minutes. Tell us what's working and what isn't.</span></li><li style="counter-increment:cs;position:relative;padding:0 0 20px 44px;border-left:2px solid var(--rule);margin-left:13px">
            <span style="position:absolute;left:-15px;top:0;width:28px;height:28px;border-radius:50%;background:var(--accent);color:#fff;display:grid;place-items:center;font-size:.8rem;font-weight:700">2</span>
            <strong style="color:var(--ink-2);font-size:.97rem">We reply within 1 business day</strong>
            <span style="display:block;color:var(--soft);font-size:.91rem;margin-top:3px">A real response from us, not an autoresponder.</span></li><li style="counter-increment:cs;position:relative;padding:0 0 20px 44px;border-left:2px solid var(--rule);margin-left:13px">
            <span style="position:absolute;left:-15px;top:0;width:28px;height:28px;border-radius:50%;background:var(--accent);color:#fff;display:grid;place-items:center;font-size:.8rem;font-weight:700">3</span>
            <strong style="color:var(--ink-2);font-size:.97rem">Free 30-minute call</strong>
            <span style="display:block;color:var(--soft);font-size:.91rem;margin-top:3px">We review your situation and tell you honestly what would help &mdash; including if you don't need us yet.</span></li><li style="counter-increment:cs;position:relative;padding:0 0 20px 44px;border-left:2px solid var(--rule);margin-left:13px">
            <span style="position:absolute;left:-15px;top:0;width:28px;height:28px;border-radius:50%;background:var(--accent);color:#fff;display:grid;place-items:center;font-size:.8rem;font-weight:700">4</span>
            <strong style="color:var(--ink-2);font-size:.97rem">Written scope &amp; fixed price</strong>
            <span style="display:block;color:var(--soft);font-size:.91rem;margin-top:3px">You see exactly what's included and what it costs before anything starts.</span></li>
        </ol>
      </div>
      <div class="viz">
        <h2>Prefer to talk now?</h2>
        <p class="cap">Direct line and email</p>
        <p style="font-family:Fraunces,serif;font-size:1.5rem;color:var(--deep);margin-bottom:6px">
          <a href="tel:+18476442288" style="text-decoration:none;color:inherit">(847) 644-2288</a></p>
        <p style="font-size:.97rem;margin-bottom:14px"><a href="mailto:{EMAIL}">{EMAIL}</a></p>
        <p style="font-size:.9rem;color:var(--soft);border-top:1px solid var(--rule);padding-top:14px;margin:0">
          Wilmette, IL &mdash; serving clients remotely nationwide.</p>
      </div>
    </div>

    <div class="rv">
      <div class="form">
        <h2 style="font-size:1.5rem;margin-bottom:8px">Or send an inquiry</h2>
        <p style="color:var(--soft);font-size:.95rem;margin-bottom:24px">Tell us a bit about your business
        and we'll reply within one business day.</p>
        <form id="cform" data-endpoint="{FORM_PLACEHOLDER}" data-email="{EMAIL}"
              action="{FORM_PLACEHOLDER}" method="POST">
          <input type="text" name="_gotcha" class="hp" tabindex="-1" autocomplete="off" aria-hidden="true">
          <div class="fg"><label for="name">Name <span class="req">*</span></label>
            <input id="name" name="name" type="text" required autocomplete="name"></div>
          <div class="fg"><label for="email">Email <span class="req">*</span></label>
            <input id="email" name="email" type="email" required autocomplete="email"></div>
          <div class="fg"><label for="phone">Phone</label>
            <input id="phone" name="phone" type="tel" autocomplete="tel"></div>
          <div class="fg"><label for="company">Business name</label>
            <input id="company" name="company" type="text" autocomplete="organization"></div>
          <div class="fg"><label for="service">What do you need help with?</label>
            <select id="service" name="service">
              <option>Not sure yet &mdash; need guidance</option>
              <option>Bookkeeping &amp; monthly reporting</option>
              <option>Controller services</option>
              <option>CFO advisory</option>
              <option>Tax preparation</option>
              <option>Tax planning</option>
              <option>Catch-up / clean-up work</option>
              <option>Individual / family taxes</option>
            </select></div>
          <div class="fg"><label for="revenue">Approximate annual revenue</label>
            <select id="revenue" name="revenue">
              <option>Prefer not to say</option><option>Under $250K</option><option>$250K &ndash; $500K</option>
              <option>$500K &ndash; $2M</option><option>$2M &ndash; $10M</option><option>$10M+</option>
            </select></div>
          <div class="fg"><label for="message">Tell us about your situation <span class="req">*</span></label>
            <textarea id="message" name="message" required
              placeholder="What's working, what isn't, and what you'd like to change."></textarea></div>
          <button type="submit" class="btn lg" style="width:100%;justify-content:center">Send Inquiry</button>
          <p id="fstat" role="status" aria-live="polite" style="margin-top:14px;font-size:.9rem"></p>
          <p class="note">We'll only use your details to respond to this inquiry.</p>
        </form>
      </div>
    </div>
  </div>
</section>

<section class="alt" id="faq">
  <div class="wrap narrow" style="padding:0">
    <div class="sec-head rv" style="margin-bottom:30px"><p class="eyebrow">FAQ</p>
      <h2>Common questions</h2></div>
    <div class="rv">{faq_html}</div>
  </div>
</section>
"""
W("contact.html", shell(
    title=f"Contact &amp; Book a Consultation | {FIRM}",
    desc="Book a free 30-minute consultation with NorthPeak Financial Partners, or send an inquiry. We reply to every message within one business day.",
    canon=f"{SITE}/contact", body=contact_body, active="Contact",
    keywords="book accounting consultation, contact accountant, financial consultation",
    jsonld={"@context":"https://schema.org","@graph":[
      {"@type":"FAQPage","mainEntity":[
        {"@type":"Question","name":q,"acceptedAnswer":{"@type":"Answer","text":a.replace("&mdash;","—")}}
        for q,a in FAQS]},
      {"@type":"AccountingService","name":FIRM,"url":SITE,"email":EMAIL,
       "telephone":"+1-847-644-2288",
       "address":{"@type":"PostalAddress","addressLocality":"Wilmette","addressRegion":"IL","addressCountry":"US"},
       "areaServed":{"@type":"Country","name":"United States"}}]}))

# ============================================================ 404 + robots + sitemap
W("404.html", shell(title=f"Page Not Found | {FIRM}",
  desc="This page could not be found. Browse our accounting guides or contact NorthPeak Financial Partners for help with your business finances.", canon=f"{SITE}/404",
  extra_head='<meta name="robots" content="noindex,follow">',
  body="""<section style="padding:110px 0"><div class="wrap narrow" style="text-align:center">
  <p class="eyebrow">404</p><h1 style="font-size:2.4rem;margin-bottom:16px">We couldn't find that page</h1>
  <p class="lead" style="margin-bottom:30px">The link may be outdated. Try the articles library or get in touch.</p>
  <a href="index.html" class="btn lg">Back to Home</a>
  <a href="articles/index.html" class="btn ghost lg" style="margin-left:10px">Browse Articles</a>
  </div></section>"""))

W("robots.txt", f"User-agent: *\nAllow: /\n\nSitemap: {SITE}/sitemap.xml\n")

pages = [("", "1.0", "weekly"), ("services", "0.9", "monthly"), ("about", "0.7", "monthly"),
         ("articles", "0.9", "weekly"), ("resources", "0.8", "monthly"), ("contact", "0.8", "monthly")]
urls = "".join(f"  <url>\n    <loc>{SITE}/{p}</loc>\n    <changefreq>{c}</changefreq>\n    <priority>{pr}</priority>\n  </url>\n"
               for p, pr, c in pages)
urls += "".join(f"  <url>\n    <loc>{SITE}/articles/{a['slug']}</loc>\n    <changefreq>monthly</changefreq>\n    <priority>0.7</priority>\n  </url>\n"
                for a in ARTS)

# Service-area URLs. Imported from build_areas rather than restated, so adding a
# town cannot leave the sitemap or the redirects behind.
from build_areas import (TOWNS as _TOWNS, TOWN_PAGES_READY as _TOWN_PAGES,
                         LOCAL_GUIDES as _GUIDES)
urls += f"  <url>\n    <loc>{SITE}/service-areas</loc>\n    <changefreq>monthly</changefreq>\n    <priority>0.8</priority>\n  </url>\n"
urls += "".join(f"  <url>\n    <loc>{SITE}/service-areas/{t[1]}</loc>\n    <changefreq>monthly</changefreq>\n    <priority>0.7</priority>\n  </url>\n"
                for t in (_TOWNS if _TOWN_PAGES else []))
urls += "".join(f"  <url>\n    <loc>{SITE}/service-areas/{g[0]}</loc>\n    <changefreq>monthly</changefreq>\n    <priority>0.7</priority>\n  </url>\n"
                for g in _GUIDES)
W("sitemap.xml", f'<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n{urls}</urlset>\n')

# ============================================================ _redirects
#
# Generated rather than hand-maintained because the article rules have to be
# enumerated one slug at a time. Netlify placeholders only match a WHOLE path
# segment, so a rule like `/articles/:slug.html` does not work — it matches
# `/articles/anything` and then emits the literal string ":slug" as the target,
# producing exactly the redirect loop the project handoff warned about. This was
# reproduced against a real Netlify redirect engine before being fixed here.
#
# Enumerating from ARTS means adding an article automatically adds its rule, so
# the two can never drift apart.
STATIC_PAGES = ["about", "services", "contact", "resources"]

redir = ["# GENERATED by build_pages2.py — do not edit by hand.",
         "# Verify any change with: ./tools/check_redirects.sh",
         "# First matching rule wins, top to bottom.",
         "",
         "# 1. Force the apex host. Every canonical points at the apex, so www",
         "#    must never serve a 200.",
         "https://www.northpeakfp.com/*   https://northpeakfp.com/:splat   301!",
         "",
         "# 2. Legacy Squarespace URLs, pointed straight at the final clean URL",
         "#    so Google never has to follow a chain.",
         "/new-page                 /about            301",
         "/new-page-1               /articles         301",
         "/submit                   /contact          301",
         "/cart                     /services         301",
         "/services-store-gN0tP/*   /services         301",
         "",
         "# 3. .html → clean URL. Closes the duplicate-content door: since the",
         "#    link canonicaliser landed, no internal link points at a .html URL,",
         "#    and now the file form 301s instead of serving a second 200 for the",
         "#    same content. `!` is required because a real file sits at that path.",
         "#    Cannot loop with section 4: those are rewrites (200), and Netlify",
         "#    serves a rewritten file directly instead of re-entering the",
         "#    redirect engine.",
         "/index.html               /                 301!"]
redir += [f"/{p}.html{' ' * max(1, 18 - len(p))}/{p}{' ' * max(1, 17 - len(p))}301!"
          for p in STATIC_PAGES]
redir += ["/articles/index.html      /articles         301!"]
redir += [f"/articles/{a['slug']}.html{' ' * max(1, 12 - len(a['slug']))}"
          f"/articles/{a['slug']}{' ' * max(1, 12 - len(a['slug']))}301!" for a in ARTS]
redir += ["",
          "/service-areas/index.html   /service-areas    301!"] + \
         [f"/service-areas/{t[1]}.html{' ' * max(1, 8 - len(t[1]))}"
          f"/service-areas/{t[1]}{' ' * max(1, 8 - len(t[1]))}301!"
          for t in (_TOWNS if _TOWN_PAGES else [])] + \
         [f"/service-areas/{g[0]}.html   /service-areas/{g[0]}   301!" for g in _GUIDES] + \
         ["",
          "# 4. Clean URL → file. Serves content without changing the address bar.",
          "/                         /index.html            200"]
redir += [f"/{p}{' ' * max(1, 25 - len(p))}/{p}.html{' ' * max(1, 13 - len(p))}200"
          for p in STATIC_PAGES]
redir += ["/articles                 /articles/index.html   200",
          "/articles/                /articles/index.html   200",
          "/articles/:slug           /articles/:slug.html   200",
          "/service-areas            /service-areas/index.html  200",
          "/service-areas/           /service-areas/index.html  200",
          "/service-areas/:slug      /service-areas/:slug.html  200",
          ""]
W("_redirects", "\n".join(redir))

print("services, about, articles hub, resources, contact, 404, robots, sitemap, _redirects")
