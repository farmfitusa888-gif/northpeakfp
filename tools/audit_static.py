#!/usr/bin/env python3
"""Scripted audit lenses: weight, capability limits, security, integrity, SEO."""
import pathlib, re, gzip, json, html as H
from collections import Counter, defaultdict

SITE = pathlib.Path("site")
pages = sorted(SITE.rglob("*.html"))
assets = [p for p in SITE.rglob("*") if p.is_file() and not p.suffix == ".html"]

def gz(p): return len(gzip.compress(p.read_bytes(), 9))

print("── PERFORMANCE / WEIGHT ──")
hp = SITE/"index.html"
crit = [("index.html", gz(hp)), ("assets/style.css", gz(SITE/"assets/style.css")),
        ("assets/app.js", gz(SITE/"assets/app.js")),
        ("fonts/inter", (SITE/"assets/fonts/inter-var-latin.woff2").stat().st_size),
        ("fonts/fraunces", (SITE/"assets/fonts/fraunces-var-latin.woff2").stat().st_size)]
for n,b in crit: print(f"   {n:32} {b:>8,} B")
print(f"   {'CRITICAL PATH TOTAL':32} {sum(b for _,b in crit):>8,} B")
defer = gz(SITE/"assets/summit.js") + gz(SITE/"assets/vendor/three.summit.js")
print(f"   {'deferred (3D, cached 1yr)':32} {defer:>8,} B")
sizes = sorted(((gz(p), p) for p in pages), reverse=True)
print(f"   heaviest page: {sizes[0][1].name} at {sizes[0][0]:,} B gzip")
print(f"   total deploy: {sum(p.stat().st_size for p in SITE.rglob('*') if p.is_file()):,} B")

print("\n── CAPABILITY LIMITS ──")
arts = list((SITE/"articles").glob("*.html"))
hub = (SITE/"articles/index.html").read_text()
print(f"   articles: {len(arts)-1}; hub renders all of them inline: "
      f"{hub.count('class=\"entry art\"')} entries, hub gzip {gz(SITE/'articles/index.html'):,} B")
print(f"   at 10x articles (400) the hub would be roughly "
      f"{gz(SITE/'articles/index.html')*10//1000}KB gzip — pagination threshold")

print("\n── SECURITY / PRIVACY ──")
hdr = (SITE/"_headers").read_text()
for h in ["X-Frame-Options","X-Content-Type-Options","Referrer-Policy",
          "Strict-Transport-Security","Permissions-Policy","Content-Security-Policy"]:
    print(f"   {h:28} {'present' if h in hdr else 'MISSING'}")
ext = set()
for p in pages:
    ext |= set(re.findall(r'https?://([a-z0-9.\-]+)', p.read_text()))
third = sorted(d for d in ext if not d.endswith("northpeakfp.com")
               and d not in ("schema.org","www.w3.org","ogp.me"))
print(f"   third-party hosts referenced: {third}")
secrets = [p.name for p in pages if re.search(r'(api[_-]?key|secret|password|token)\s*[:=]\s*["\']', p.read_text(), re.I)]
print(f"   inline secrets: {secrets or 'none'}")

print("\n── LINK / TARGET HYGIENE ──")
noopener = 0; blank = 0
for p in pages:
    t = p.read_text()
    for m in re.finditer(r'<a\b[^>]*target="_blank"[^>]*>', t):
        blank += 1
        if 'rel=' not in m.group(0) or 'noopener' not in m.group(0): noopener += 1
print(f"   target=_blank links: {blank}; missing rel=noopener: {noopener}")
ext_links = Counter()
for p in pages:
    for m in re.finditer(r'href="(https?://[^"]+)"', p.read_text()):
        d = re.sub(r'^https?://', '', m.group(1)).split('/')[0]
        if not d.endswith("northpeakfp.com"): ext_links[d]+=1
print(f"   outbound citation domains: {dict(ext_links)}")

print("\n── STRUCTURED DATA ──")
types = Counter()
bad = []
for p in pages:
    for blk in re.findall(r'(?s)<script type="application/ld\+json">(.*?)</script>', p.read_text()):
        try:
            d = json.loads(blk)
        except Exception as e:
            bad.append((p.name, str(e))); continue
        nodes = d.get("@graph", [d]) if isinstance(d, dict) else d
        for n in nodes:
            if isinstance(n, dict): types[n.get("@type","?")] += 1
print(f"   schema types: {dict(types)}")
print(f"   invalid JSON-LD: {bad or 'none'}")
missing = [p.name for p in pages if 'application/ld+json' not in p.read_text()]
print(f"   pages with NO structured data: {len(missing)} {missing[:6]}")

print("\n── INTERNAL LINK GRAPH ──")
inb = Counter()
for p in pages:
    for h in set(re.findall(r'href="(/[^"#?]*)"', p.read_text())):
        if not re.search(r'\.(css|js|svg|jpg|png|woff2|xml|txt)$', h): inb[h]+=1
allurls = set()
for p in pages:
    u = "/" if p.name=="index.html" and p.parent==SITE else None
    if u is None:
        r = str(p.relative_to(SITE))
        u = "/"+r[:-len("/index.html")] if r.endswith("/index.html") else "/"+r[:-5]
    allurls.add(u)
weak = sorted((c,u) for u,c in inb.items() if u in allurls)[:8]
print(f"   fewest inbound internal links:")
for c,u in weak: print(f"      {c:>3}  {u}")
never = sorted(allurls - set(inb))
print(f"   never linked: {never or 'none'}")
