#!/usr/bin/env python3
import os, sys, json, html, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
from build_site import shell, W, SITE, FIRM, EMAIL
import generate_articles_northpeak as G

ARTS = G.ARTICLES
n = len(ARTS)

# ART_CSS moved into the shared stylesheet in build_site.py — it is used by
# both the articles and the local guides, and inlining it duplicated ~45KB
# across the article pages.

for i, a in enumerate(ARTS):
    secs, toc = [], []
    for j, (h, p) in enumerate(a["sections"], 1):
        sid = f"s{j}"
        toc.append(f'<li><a href="#{sid}">{html.escape(h)}</a></li>')
        secs.append(f'<h2 id="{sid}"><span class="num">{j:02d}</span>{html.escape(h)}</h2>\n<p>{p}</p>')
    body_html = "\n".join(secs)
    toc_html = "".join(toc)

    rel = "".join(f'''<a class="art" href="{ARTS[(i+k)%n]["slug"]}.html">
      <span class="cat">{html.escape(ARTS[(i+k)%n]["cat"])}</span>
      <h3>{html.escape(ARTS[(i+k)%n]["title"])}</h3>
      <span class="rd">{ARTS[(i+k)%n]["read"]}</span></a>''' for k in (1, 2, 3))

    body = f"""
<div class="wrap crumb"><a href="../index.html">Home</a> &rsaquo; <a href="index.html">Articles</a>
 &rsaquo; <span>{html.escape(a['cat'])}</span></div>
<article>
<div class="aw ahead">
  <p class="eyebrow">{html.escape(a['cat'])}</p>
  <h1>{html.escape(a['title'])}</h1>
  <p class="lead">{html.escape(a['lede'])}</p>
  <div class="abyline">
    <span>By <strong>{G.FOUNDER}</strong>, {FIRM}</span><span class="dot"></span><span>{a['read']}</span>
  </div>
  <div class="toc"><p>In this guide</p><ol>{toc_html}</ol></div>
</div>
<div class="aw abody">
{body_html}
  <div class="acta">
    <h3>Have a question about your situation?</h3>
    <p>Book a free 30-minute consultation and we'll walk through it together.</p>
    <a href="../contact.html" class="btn gold">Schedule a Consultation</a>
  </div>
  <p class="adisc">This article is general information, not individualized tax, legal, or financial
  advice. Every situation is different &mdash; reach out and we'll look at yours directly.</p>
  <div class="arel"><h3>Related guides</h3><div class="arts">{rel}</div></div>
</div>
</article>
"""

    jsonld = {
        "@context": "https://schema.org", "@type": "Article",
        "headline": a["title"], "description": a["desc"],
        "author": {"@type": "Person", "name": G.FOUNDER,
                   "jobTitle": "Founder & Principal",
                   "image": f"{SITE}/assets/chaudhry-ahmad-headshot.jpg",
                   "worksFor": {"@type": "Organization", "name": FIRM, "url": SITE}},
        "publisher": {"@type": "Organization", "name": FIRM,
                      "logo": {"@type": "ImageObject", "url": f"{SITE}/assets/favicon.svg"}},
        "datePublished": G.PUBDATE, "dateModified": G.PUBDATE,
        "articleSection": a["cat"],
        "mainEntityOfPage": {"@type": "WebPage", "@id": f"{SITE}/articles/{a['slug']}"},
        "isPartOf": {"@type": "WebSite", "name": FIRM, "url": SITE},
    }

    seo_t = G.SEO_TITLES.get(a["slug"], a["title"])
    full = f"{seo_t} | NorthPeak"
    page_title = html.escape(full if len(full) <= 60 else seo_t)
    W(f"articles/{a['slug']}.html", shell(
        title=page_title,
        desc=html.escape(a["desc"]), canon=f"{SITE}/articles/{a['slug']}",
        body=body, active="Articles", depth=1, keywords=html.escape(a["keywords"]),
        og_type="article", jsonld=jsonld))

print(f"Rebuilt {n} articles with site shell")
