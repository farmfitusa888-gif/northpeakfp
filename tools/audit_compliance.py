#!/usr/bin/env python3
"""Compliance lens: the hard constraints this site must never violate.

Chaudhry Ahmad is not a CPA (Illinois restricts the title) and not a registered
investment adviser. No invented statistics, testimonials or client counts. No
published pricing. This checks all four mechanically so a future edit cannot
reintroduce a violation quietly.
"""
import pathlib, re, html as H
from collections import Counter

PAGES = sorted(pathlib.Path("site").rglob("*.html"))

def text(p):
    s = p.read_text()
    s = re.sub(r'(?is)<(script|style)\b.*?</\1>', ' ', s)
    s = re.sub(r'(?s)<!--.*?-->', ' ', s)
    return H.unescape(re.sub(r'(?s)<[^>]+>', ' ', s))

CACHE = {p: text(p) for p in PAGES}

def hits(patterns, flags=re.I):
    out = []
    for p, t in CACHE.items():
        for kw in patterns:
            for m in re.finditer(kw, t, flags):
                out.append((p.name, kw, " ".join(t[max(0, m.start()-80):m.end()+80].split())))
    return out

print(f"pages scanned: {len(PAGES)}\n")

cpa = hits([r'\bCPAs?\b', r'certified public account'], re.I)
print(f"[1] CPA / certified-public claims : {len(cpa)}")
for n, k, s in cpa[:6]:
    print(f"      {n}: ...{s}...")

adv = hits([r'registered investment advis', r'\bfiduciary\b', r'investment advice',
            r'financial advis[oe]r'])
print(f"\n[2] adviser / fiduciary claims    : {len(adv)}")
for n, k, s in adv[:6]:
    print(f"      {n} [{k}]: ...{s}...")

money = []
for p, t in CACHE.items():
    for m in re.finditer(r'\$[0-9][0-9,]*(?:\.[0-9]{2})?', t):
        money.append((p.name, m.group(0)))
print(f"\n[3] dollar figures                : {len(money)}")
for v, c in Counter(v for _, v in money).most_common():
    where = sorted({n for n, x in money if x == v})
    print(f"      {v:>10}  x{c:<3} on {', '.join(where[:4])}{'...' if len(where)>4 else ''}")

claims = hits([r'\bguarantee', r'\baward-winning\b', r'\bbest in\b', r'\b#1\b',
               r'\bnumber one\b', r'\btrusted by\b', r'\bover \d+ clients?\b',
               r'\b\d+\+ (?:clients|businesses|years)\b'])
print(f"\n[4] guarantee / superlative claims: {len(claims)}")
for n, k, s in claims[:8]:
    print(f"      {n} [{k}]: ...{s}...")

testi = hits([r'<blockquote', r'\btestimonial', r'\bsaid [\"“]', r'\brated \d'])
print(f"\n[5] testimonial-shaped content    : {len(testi)}")

stats = []
for p, t in CACHE.items():
    for m in re.finditer(r'\b\d{1,3}%', t):
        seg = " ".join(t[max(0, m.start()-110):m.end()+110].split())
        labelled = bool(re.search(r'illustrat|benchmark|directional|estimate|approx|~', seg, re.I))
        stats.append((p.name, m.group(0), labelled, seg))
unlabelled = [s for s in stats if not s[2]]
print(f"\n[6] percentage figures            : {len(stats)} total, "
      f"{len(unlabelled)} without a nearby 'illustrative/benchmark/estimate' qualifier")
for n, v, _, s in unlabelled[:10]:
    print(f"      {n} {v}: ...{s[:150]}...")
