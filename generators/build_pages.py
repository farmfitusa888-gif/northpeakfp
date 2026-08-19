#!/usr/bin/env python3
"""Build all NorthPeak page bodies. Imports shell/assets from build_site."""
import os, sys, json, html, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
from build_site import (shell, W, ROOT, SITE, FIRM, EMAIL, CAL_PLACEHOLDER,
                        FORM_PLACEHOLDER)
import generate_articles_northpeak as G

ARTS = G.ARTICLES
CATS = sorted({a["cat"] for a in ARTS})

TICK = ('<svg class="tick" width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" '
        'stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round"><polyline points="20 6 9 17 4 12"/></svg>')

def ico(d):
    return (f'<div class="icon"><svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="#fff" '
            f'stroke-width="1.9" stroke-linecap="round" stroke-linejoin="round">{d}</svg></div>')

I_CHART = '<path d="M3 3v18h18"/><path d="M7 15l4-5 3 3 5-7"/>'
I_SHIELD = '<path d="M12 22s8-4 8-10V5l-8-3-8 3v7c0 6 8 10 8 10z"/>'
I_TREND = '<polyline points="22 7 13.5 15.5 8.5 10.5 2 17"/><polyline points="16 7 22 7 22 13"/>'
I_CLOCK = '<circle cx="12" cy="12" r="9"/><polyline points="12 7 12 12 15.5 14"/>'
I_DOC = '<path d="M14 2H6a2 2 0 00-2 2v16a2 2 0 002 2h12a2 2 0 002-2V8z"/><polyline points="14 2 14 8 20 8"/>'
I_USERS = '<path d="M17 21v-2a4 4 0 00-4-4H5a4 4 0 00-4 4v2"/><circle cx="9" cy="7" r="4"/><path d="M23 21v-2a4 4 0 00-3-3.87"/>'
I_CALC = '<rect x="4" y="2" width="16" height="20" rx="2"/><line x1="8" y1="6" x2="16" y2="6"/><line x1="8" y1="11" x2="8" y2="11"/><line x1="12" y1="11" x2="12" y2="11"/><line x1="16" y1="11" x2="16" y2="11"/><line x1="8" y1="16" x2="8" y2="16"/><line x1="12" y1="16" x2="12" y2="16"/><line x1="16" y1="16" x2="16" y2="16"/>'

# ============================================================ HOME
HERO_BACKDROP = """  <!-- Painted immediately by CSS. This is the hero's real background: the
       WebGL scene below is an enhancement layered on top of it, and on any
       device that declines the scene (reduced motion, Data Saver, 2g, low
       memory, no WebGL) this gradient is what the visitor sees, permanently.
       There is deliberately no poster image — a gradient costs zero bytes and
       paints before the first network round trip completes. -->
  <div class="fallback" aria-hidden="true"></div>
  <canvas id="summit" aria-hidden="true"></canvas>"""

home_body = f"""
<section class="hero">
{HERO_BACKDROP}
  <div class="wrap hero-in">
    <p class="eyebrow" style="color:#d4a437">Accounting &middot; Controller &middot; CFO Advisory</p>
    <h1>Financial Clarity.<em>Strategic Growth.</em></h1>
    <p>Most businesses don't struggle because they lack revenue &mdash; they struggle because they lack
    financial clarity. NorthPeak brings structure, accurate reporting, and CFO-level insight to growing companies.</p>
    <div class="hero-cta">
      <a href="contact.html" class="btn gold lg">Book a Free Consultation</a>
      <a href="services.html" class="btn ghost lg">Compare Packages</a>
    </div>
    <div class="trust">
      <div>{TICK} Controller-level experience</div>
      <div>{TICK} Fixed quotes agreed in writing</div>
      <div>{TICK} Wilmette, IL &mdash; serving clients nationwide</div>
    </div>
  </div>
</section>

<section class="dark pad-s">
  <div class="wrap rv">
    <div class="figrow">
      <div class="fighero">
        <div class="n" data-count="82" data-suf="%">0%</div>
        <div class="l">of small businesses fail from cash-flow problems, not lack of profit</div>
      </div>
      <div class="figrest">
        <div><div class="n" data-count="21" data-suf=" hrs">0</div>
          <div class="l">average time owners lose to bookkeeping each month</div></div>
        <div><div class="n" data-count="30" data-suf="%">0%</div>
          <div class="l">of eligible small businesses never claim deductions they qualify for</div></div>
        <div><div class="n" data-count="1" data-suf=" day">0</div>
          <div class="l">our standard response time to every inquiry</div></div>
      </div>
    </div>
    <p style="font-size:.78rem;color:#7a9087;margin-top:22px;max-width:62ch">
      Figures reflect widely reported small-business benchmarks and are illustrative, not guarantees.</p>
  </div>
</section>

<section>
  <div class="wrap">
    <div class="split rv">
      <div class="sh">
        <p class="eyebrow">What We Do</p>
        <h2>Beyond bookkeeping &mdash; financial leadership</h2>
        <p>We help owners move past basic data entry and actually understand what their numbers
        are telling them, so decisions get made on evidence instead of instinct.</p>
      </div>
      <div class="sb">
        <div class="ledger">
          <div class="lrow"><div class="ln">01</div><h3>Accounting &amp; Bookkeeping</h3>
            <p>Clean, reconciled books you can trust &mdash; transaction categorization, monthly closes, and
            reporting delivered on a predictable schedule.</p>
            <a class="lgo" href="services.html">Details &rarr;</a></div>
          <div class="lrow"><div class="ln">02</div><h3>Controller Services</h3>
            <p>Oversight, structured month-end close, budget-vs-actual reporting, and KPI tracking that turns
            raw data into visibility.</p>
            <a class="lgo" href="services.html">Details &rarr;</a></div>
          <div class="lrow"><div class="ln">03</div><h3>CFO Advisory</h3>
            <p>Cash-flow forecasting, margin analysis, strategic modeling, and decision support &mdash;
            executive financial leadership without a full-time hire.</p>
            <a class="lgo" href="services.html">Details &rarr;</a></div>
          <div class="lrow"><div class="ln">04</div><h3>Tax Planning &amp; Prep</h3>
            <p>Proactive planning through the year, not just filing in April. Entity strategy, deduction
            capture, and quarterly estimate management.</p>
            <a class="lgo" href="services.html">Details &rarr;</a></div>
          <div class="lrow"><div class="ln">05</div><h3>Internal Controls</h3>
            <p>Process and safeguard design that protects your business from errors, leakage, and the
            surprises that catch growing companies off guard.</p>
            <a class="lgo" href="services.html">Details &rarr;</a></div>
          <div class="lrow"><div class="ln">06</div><h3>Individuals &amp; Families</h3>
            <p>Personal tax preparation and planning, coordinated with your business so both sides of the
            picture work together.</p>
            <a class="lgo" href="services.html">Details &rarr;</a></div>
        </div>
      </div>
    </div>
  </div>
</section>

<section class="alt">
  <div class="wrap">
    <div class="split rv">
      <div class="sh">
        <p class="eyebrow">The Data</p>
        <h2>Where growing businesses actually lose money</h2>
        <p>These are the gaps we're hired to close. Every one is fixable with structure and
        consistent reporting.</p>
      </div>
      <div class="sb">
        <div class="viz">
          <h3>Owner hours lost per month</h3>
          <p class="cap">Time spent on financial admin instead of running the business</p>
          <div class="bar hl"><span class="lb">Bookkeeping</span><div class="track"><div class="fill" data-w="88">21 hrs</div></div></div>
          <div class="bar"><span class="lb">Chasing invoices</span><div class="track"><div class="fill" data-w="52">12 hrs</div></div></div>
          <div class="bar"><span class="lb">Tax prep scramble</span><div class="track"><div class="fill" data-w="40">9 hrs</div></div></div>
          <div class="bar"><span class="lb">Report building</span><div class="track"><div class="fill" data-w="33">8 hrs</div></div></div>
          <p style="font-size:.78rem;color:var(--mute);margin-top:14px">Illustrative benchmarks based on
          commonly reported small-business survey ranges.</p>
        </div>
        <div class="viz" style="margin-top:34px">
          <h3>Most-missed tax deductions</h3>
          <p class="cap">Share of eligible small businesses that never claim them</p>
          <div class="bar hl"><span class="lb">Home office</span><div class="track"><div class="fill" data-w="72">~72%</div></div></div>
          <div class="bar"><span class="lb">Mileage</span><div class="track"><div class="fill" data-w="61">~61%</div></div></div>
          <div class="bar"><span class="lb">Startup costs</span><div class="track"><div class="fill" data-w="55">~55%</div></div></div>
          <div class="bar"><span class="lb">Retirement</span><div class="track"><div class="fill" data-w="44">~44%</div></div></div>
          <p style="font-size:.78rem;color:var(--mute);margin-top:14px">Directional estimates for
          illustration. <a href="articles/tax-deductions-small-business.html">See the full breakdown &rarr;</a></p>
        </div>
      </div>
    </div>
  </div>
</section>

<section class="dark pad-s">
  <div class="wrap">
    <div class="rhead rv"><span>How It Works</span><span>Four steps</span></div>
    <h2 class="rv" style="font-size:clamp(1.75rem,3.4vw,2.5rem);color:#fff;margin:26px 0 34px;max-width:18ch">A clear path from chaos to clarity</h2>
    <div class="ledger rv">
      <div class="lrow"><div class="ln">01</div><h3>Discovery Call</h3>
        <p>A free 30-minute conversation about your business, your numbers, and where the gaps are.</p><span></span></div>
      <div class="lrow"><div class="ln">02</div><h3>Financial Review</h3>
        <p>We assess your current books, reporting, and structure, then show you exactly what's missing.</p><span></span></div>
      <div class="lrow"><div class="ln">03</div><h3>Build the System</h3>
        <p>Clean-up, chart of accounts, close process, and reporting cadence tailored to how you actually operate.</p><span></span></div>
      <div class="lrow"><div class="ln">04</div><h3>Ongoing Insight</h3>
        <p>Monthly reporting and review calls so you always know where you stand &mdash; and what to do next.</p><span></span></div>
    </div>
  </div>
</section>

<!-- The 3D range at full strength, carrying the closing call to action. The
     hero runs the same scene at 42% opacity so the headline wins there; here
     it is the subject of the section. -->
<section class="mband">
  <div class="mfall" aria-hidden="true"></div>
  <canvas id="summit-band" aria-hidden="true"></canvas>
  <div class="wrap"><div class="mb-in rv">
    <h2>Let's get your numbers working for you</h2>
    <p>Book a free 30-minute consultation. No pressure, no obligation &mdash; just a clear read on
    where you stand and what would help most.</p>
    <div style="margin-top:26px"><a href="contact.html" class="btn gold lg">Book a Free Consultation</a></div>
  </div></div>
</section>
"""

W("index.html", shell(
    title="Accounting, Controller &amp; CFO Advisory | NorthPeak",
    desc="Accounting, controller services, and CFO-level advisory that give growing businesses real financial clarity. Book a free consultation with NorthPeak.",
    canon=f"{SITE}/", body=home_body, active="Home",
    keywords="accounting firm, controller services, fractional CFO, bookkeeping, tax planning, small business accountant",
    jsonld={
        "@context": "https://schema.org", "@type": "AccountingService",
        "name": FIRM, "url": SITE, "email": EMAIL,
        "telephone": "+1-847-644-2288",
        "founder": {"@type": "Person", "name": "Chaudhry Ahmad",
                    "jobTitle": "Founder & Principal",
                    "image": f"{SITE}/assets/chaudhry-ahmad-headshot.jpg"},
        "image": f"{SITE}/assets/og-image.jpg",
        "address": {"@type": "PostalAddress", "addressLocality": "Wilmette",
                    "addressRegion": "IL", "addressCountry": "US"},
        "description": "Accounting, controller, and CFO advisory services for growing businesses.",
        "priceRange": "$$",
        "areaServed": {"@type": "Country", "name": "United States"},
        "serviceType": ["Bookkeeping", "Controller Services", "CFO Advisory",
                        "Tax Preparation", "Tax Planning"],
        "sameAs": [],
    }))

print("index.html")
