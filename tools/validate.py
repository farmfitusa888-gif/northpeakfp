#!/usr/bin/env python3
"""
Pre-deploy validator for the NorthPeak site. No dependencies — stdlib only, so
it runs anywhere the build runs and can gate a deploy.

    python3 tools/validate.py            # exits non-zero if any ERROR is found
    python3 tools/validate.py --warn     # also fail on warnings

Checks, per page unless noted:
  * exactly one <h1>
  * <title> present, unique, <= 60 chars (Google truncates beyond that)
  * meta description present, unique, 70-165 chars
  * canonical present, absolute, apex host, and matching the page's own URL
  * every JSON-LD block parses as valid JSON
  * every <img> has a non-empty alt
  * every referenced local asset exists on disk
  * every internal link resolves to a real page (directory indexes included)
  * heading levels never skip (h2 -> h4)
  * site-wide: no orphans (every sitemap URL is linked from somewhere)
  * site-wide: sitemap matches the set of indexable pages
  * site-wide: footer grid has its four columns (regression guard — a stray
    </div> in a commented block silently broke this in production once)
  * site-wide: summit.js imports match what the vendored three bundle exports
"""
import argparse
import json
import pathlib
import html as _html
import re
import sys
from html.parser import HTMLParser

ROOT = pathlib.Path(__file__).resolve().parent.parent
SITE = ROOT / "site"
HOST = "https://northpeakfp.com"
VOID = {"br", "img", "meta", "link", "input", "hr", "source", "path", "rect",
        "polyline", "circle", "use", "area", "base", "col", "embed", "param",
        "track", "wbr", "stop", "line", "ellipse", "polygon"}

errors, warnings = [], []


def err(page, msg):
    errors.append(f"{page}: {msg}")


def warn(page, msg):
    warnings.append(f"{page}: {msg}")


def rel(p):
    return str(p.relative_to(SITE))


def url_for(p):
    """The canonical URL a file is served at."""
    r = rel(p)
    if r == "index.html":
        return "/"
    if r.endswith("/index.html"):
        return "/" + r[: -len("/index.html")]
    return "/" + r[: -len(".html")]


def resolve(href):
    """Map an internal href onto the file that serves it."""
    h = href.split("#")[0].split("?")[0]
    if not h:
        return None
    if h == "/":
        return SITE / "index.html"
    h = h.lstrip("/")
    if re.search(r"\.(css|js|svg|jpg|jpeg|png|webp|woff2|xml|txt|ico|pdf)$", h):
        return SITE / h
    direct = SITE / (h + ".html")
    if direct.exists():
        return direct
    return SITE / h / "index.html"


class Page(HTMLParser):
    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.h1 = 0
        self.headings = []
        self.imgs = []
        self.links = []
        self.assets = []
        self.depth = 0
        self.fgrid_depth = None
        self.fgrid_children = 0
        self.in_ld = False
        self.ld_blocks = []

    def handle_starttag(self, tag, attrs):
        a = dict(attrs)
        if tag == "h1":
            self.h1 += 1
        if tag in ("h1", "h2", "h3", "h4", "h5", "h6"):
            self.headings.append(int(tag[1]))
        if tag == "img":
            self.imgs.append(a)
            if a.get("src", "").startswith("/"):
                self.assets.append(a["src"])
        if tag == "script" and a.get("type") == "application/ld+json":
            self.in_ld = True
            self.ld_blocks.append("")
        if tag in ("a", "link") and a.get("href", "").startswith("/"):
            (self.assets if tag == "link" else self.links).append(a["href"])
        if tag == "script" and a.get("src", "").startswith("/"):
            self.assets.append(a["src"])

        if tag in VOID:
            return
        cls = a.get("class", "")
        if self.fgrid_depth is None and "fgrid" in cls:
            self.fgrid_depth = self.depth
        elif self.fgrid_depth is not None and self.fgrid_depth >= 0 \
                and self.depth == self.fgrid_depth + 1:
            self.fgrid_children += 1
        self.depth += 1

    def handle_endtag(self, tag):
        if tag == "script":
            self.in_ld = False
        if tag in VOID:
            return
        self.depth -= 1
        if self.fgrid_depth is not None and self.fgrid_depth >= 0 \
                and self.depth == self.fgrid_depth:
            self.fgrid_depth = -1  # closed; stop counting

    def handle_data(self, data):
        if self.in_ld:
            self.ld_blocks[-1] += data


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--warn", action="store_true", help="treat warnings as failures")
    args = ap.parse_args()

    pages = sorted(SITE.rglob("*.html"))
    if not pages:
        print("no pages found — run python3 generators/build.py first")
        return 1

    titles, descs, all_links = {}, {}, set()

    for p in pages:
        name = rel(p)
        raw = p.read_text()
        noindex = 'name="robots" content="noindex' in raw

        doc = Page()
        doc.feed(raw)

        if doc.h1 != 1:
            err(name, f"{doc.h1} <h1> elements (want exactly 1)")

        m = re.search(r"(?s)<title>(.*?)</title>", raw)
        if not m:
            err(name, "no <title>")
        else:
            t = _html.unescape(m.group(1)).strip()
            if len(t) > 60:
                err(name, f"title is {len(t)} chars (Google truncates past 60): {t!r}")
            titles.setdefault(t, []).append(name)

        m = re.search(r'<meta name="description" content="([^"]*)"', raw)
        if not m:
            err(name, "no meta description")
        else:
            d = _html.unescape(m.group(1)).strip()
            if not (70 <= len(d) <= 165):
                err(name, f"meta description is {len(d)} chars (want 70-165)")
            descs.setdefault(d, []).append(name)

        m = re.search(r'<link rel="canonical" href="([^"]*)"', raw)
        if not m:
            err(name, "no canonical")
        else:
            c = m.group(1)
            if not c.startswith(HOST):
                err(name, f"canonical is not on the apex host: {c}")
            elif c.replace(HOST, "") or True:
                want = url_for(p)
                got = c.replace(HOST, "") or "/"
                if got != want:
                    err(name, f"canonical {got} does not match this page's URL {want}")

        for i, block in enumerate(doc.ld_blocks):
            try:
                json.loads(block)
            except json.JSONDecodeError as e:
                err(name, f"JSON-LD block {i + 1} is not valid JSON: {e}")

        for img in doc.imgs:
            if not img.get("alt", "").strip():
                err(name, f"<img> without alt: {img.get('src', '(no src)')}")

        for a in set(doc.assets):
            t = resolve(a)
            if t and not t.exists():
                err(name, f"missing asset {a}")

        for h in set(doc.links):
            t = resolve(h)
            if t and not t.exists():
                err(name, f"broken internal link {h}")
        all_links |= set(doc.links)

        levels = doc.headings
        for a, b in zip(levels, levels[1:]):
            if b > a + 1:
                warn(name, f"heading level skips h{a} -> h{b}")
                break

        if doc.fgrid_children not in (0, 4):
            err(name, f"footer grid has {doc.fgrid_children} columns (want 4) — "
                      "check for a stray closing tag in the commented social block")

        if not noindex and "canonical" not in raw:
            warn(name, "indexable page with no canonical")

    for t, ps in titles.items():
        if len(ps) > 1:
            err(", ".join(ps), f"duplicate <title>: {t!r}")
    for d, ps in descs.items():
        if len(ps) > 1:
            err(", ".join(ps), f"duplicate meta description: {d[:60]!r}...")

    # ---- iCloud / Finder conflict copies -----------------------------------
    # This repo lives on an iCloud-synced Desktop, and the build rewrites 60+
    # files in seconds. iCloud responds by forking "name 2.html" duplicates
    # mid-build. Eighty of them accumulated once, and five reached a commit.
    # They are byte-identical orphans: not in the sitemap, not linked, and pure
    # duplicate content if deployed.
    dupes = [p for p in SITE.rglob("*")
             if p.is_file() and re.search(r" \d+(\.[A-Za-z0-9]+)?$", p.stem + p.suffix)]
    for d in dupes:
        err(rel(d), "iCloud/Finder conflict copy — delete it and check .gitignore")

    # ---- sitemap ----------------------------------------------------------
    sm = SITE / "sitemap.xml"
    if not sm.exists():
        err("sitemap.xml", "missing")
    else:
        listed = set(re.findall(r"<loc>([^<]+)</loc>", sm.read_text()))
        listed_paths = {u.replace(HOST, "") or "/" for u in listed}
        indexable = {url_for(p) for p in pages
                     if 'content="noindex' not in p.read_text()}
        for missing in sorted(indexable - listed_paths):
            err("sitemap.xml", f"indexable page not listed: {missing}")
        for extra in sorted(listed_paths - indexable):
            err("sitemap.xml", f"lists a URL that is not an indexable page: {extra}")
        for orphan in sorted(listed_paths - all_links - {"/"}):
            err("orphan", f"{orphan} is in the sitemap but nothing links to it")

    # ---- 3D bundle parity -------------------------------------------------
    summit = SITE / "assets" / "summit.js"
    bundle = SITE / "assets" / "vendor" / "three.summit.js"
    if summit.exists() and bundle.exists():
        m = re.search(r"import \{(.*?)\} from", summit.read_text(), re.S)
        if m:
            want = {w.strip() for w in m.group(1).replace("\n", " ").split(",") if w.strip()}
            have = set()
            for blk in re.findall(r"export\{(.*?)\}", bundle.read_text(), re.S):
                for pair in blk.split(","):
                    have.add(pair.split(" as ")[-1].strip())
            for miss in sorted(want - have):
                err("assets/summit.js",
                    f"imports {miss!r}, which the vendored bundle does not export "
                    "— add it to tools/build_three.sh and re-run that script")

    # ---- report -----------------------------------------------------------
    print(f"checked {len(pages)} pages\n")
    for e in errors:
        print(f"  ERROR  {e}")
    for w in warnings:
        print(f"  warn   {w}")
    print(f"\n{len(errors)} error(s), {len(warnings)} warning(s)")
    if errors:
        return 1
    if warnings and args.warn:
        return 1
    print("PASS")
    return 0


if __name__ == "__main__":
    sys.exit(main())
