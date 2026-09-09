#!/usr/bin/env python3
import os, sys, json, html, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
from build_site import shell, W, SITE, FIRM, EMAIL
import generate_articles_northpeak as G
from articles_cluster import PILLAR_LABELS

ARTS = G.ARTICLES
n = len(ARTS)

# ART_CSS moved into the shared stylesheet in build_site.py — it is used by
# both the articles and the local guides, and inlining it duplicated ~45KB
# across the article pages.


def _paras(p):
    """A section body is either one HTML string (the original 25 articles and
    the two tax clusters) or a list of paragraphs (the service cluster)."""
    if isinstance(p, (list, tuple)):
        return "\n".join(f"<p>{x}</p>" for x in p)
    return f"<p>{p}</p>"


for i, a in enumerate(ARTS):
    secs, toc = [], []
    for j, (h, p) in enumerate(a["sections"], 1):
        sid = f"s{j}"
        toc.append(f'<li><a href="#{sid}">{html.escape(h)}</a></li>')
        secs.append(f'<h2 id="{sid}"><span class="num">{j:02d}</span>{html.escape(h)}</h2>\n{_paras(p)}')
    body_html = "\n".join(secs)
    toc_html = "".join(toc)

    # Related guides: an article in a service cluster points at its cluster
    # siblings so the cluster reads as one topic; everything else keeps the
    # original rotation through the list.
    pillar = a.get("pillar")
    if pillar:
        sibs = [b for b in ARTS if b.get("pillar") == pillar and b["slug"] != a["slug"]][:3]
    else:
        sibs = [ARTS[(i + k) % n] for k in (1, 2, 3)]
    rel = "".join(f'''<a class="art" href="{b["slug"]}.html">
      <span class="cat">{html.escape(b["cat"])}</span>
      <h3>{html.escape(b["title"])}</h3>
      <span class="rd">{b["read"]}</span></a>''' for b in sibs)

    # The cluster bar sits under the byline, above the fold: which service the
    # guide belongs to, the pillar link, the consultation action and the
    # tap-to-call number. Only cluster articles carry it.
    cluster_bar = ""
    if pillar:
        cluster_bar = (
            f'<p class="acluster">This guide is part of our '
            f'<a href="../{pillar}.html">{PILLAR_LABELS[pillar].lower()}</a> in Wilmette, IL. '
            f'<a href="../contact.html">Book a free consultation</a> or call '
            f'<a href="tel:+18476442288">(847) 644-2288</a>.</p>')

    faq_html = ""
    faqs = a.get("faq") or []
    if faqs:
        faq_html = ('<h2 id="faq">Common questions</h2>\n<div class="afaq">' + "".join(
            f'<details class="faq"><summary>{html.escape(q)}</summary><p>{html.escape(ans)}</p></details>'
            for q, ans in faqs) + "</div>")

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
  {cluster_bar}
  <div class="toc"><p>In this guide</p><ol>{toc_html}</ol></div>
</div>
<div class="aw abody">
{body_html}
{faq_html}
  <div class="acta">
    <h3>Have a question about your situation?</h3>
    <p>Book a free 30-minute consultation and we'll walk through it together.</p>
    <a href="../contact.html" class="btn gold">Schedule a Consultation</a>
  </div>
  <p class="adisc">This article is general information, not individualized tax, legal, or financial
  advice. Every situation is different. Reach out and we'll look at yours directly.</p>
  <div class="arel"><h3>Related guides</h3><div class="arts">{rel}</div></div>
</div>
</article>
"""

    article_ld = {
        "@context": "https://schema.org", "@type": "Article",
        "headline": a["title"], "description": a["desc"],
        "author": {"@type": "Person", "name": G.FOUNDER,
                   "jobTitle": "Founder & Principal",
                   "image": f"{SITE}/assets/chaudhry-ahmad-headshot.jpg",
                   "worksFor": {"@type": "Organization", "name": FIRM, "url": SITE}},
        "publisher": {"@type": "Organization", "name": FIRM,
                      "logo": {"@type": "ImageObject", "url": f"{SITE}/assets/favicon.svg"}},
        "datePublished": a.get("published", G.PUBDATE), "dateModified": G.LASTMOD,
        "articleSection": a["cat"],
        "mainEntityOfPage": {"@type": "WebPage", "@id": f"{SITE}/articles/{a['slug']}"},
        "isPartOf": {"@type": "WebSite", "name": FIRM, "url": SITE},
    }
    if pillar:
        article_ld["about"] = {"@type": "Service", "name": PILLAR_LABELS[pillar],
                               "url": f"{SITE}/{pillar}"}

    # Articles sit two levels deep, so the hierarchy is worth stating explicitly
    # rather than leaving Google to infer it. BreadcrumbList is also the cheapest
    # rich-result surface available to a page like this. Each block is emitted
    # on its own (rather than inside one @graph) so dateModified sits at the
    # top level of the Article, where readers that look for it actually look.
    blocks = [article_ld, {
        "@context": "https://schema.org", "@type": "BreadcrumbList", "itemListElement": [
            {"@type": "ListItem", "position": 1, "name": "Home", "item": f"{SITE}/"},
            {"@type": "ListItem", "position": 2, "name": "Articles",
             "item": f"{SITE}/articles"},
            {"@type": "ListItem", "position": 3, "name": a["title"],
             "item": f"{SITE}/articles/{a['slug']}"}]}]
    if faqs:
        blocks.append({"@context": "https://schema.org", "@type": "FAQPage", "mainEntity": [
            {"@type": "Question", "name": q, "acceptedAnswer": {"@type": "Answer", "text": ans}}
            for q, ans in faqs]})

    seo_t = G.SEO_TITLES.get(a["slug"], a["title"])
    full = f"{seo_t} | NorthPeak"
    page_title = html.escape(full if len(full) <= 60 else seo_t)
    W(f"articles/{a['slug']}.html", shell(
        title=page_title,
        desc=html.escape(a["desc"]), canon=f"{SITE}/articles/{a['slug']}",
        body=body, active="Articles", depth=1, keywords=html.escape(a["keywords"]),
        og_type="article", jsonld=blocks))

print(f"Rebuilt {n} articles with site shell")
