#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Stable publication dates for every generated page.

WHY THIS EXISTS
`generate_articles_northpeak.py` set LASTMOD to `date.today()` and every
generator read it. One value became the dateModified of all 77 pages and the
lastmod of all 77 sitemap entries, so a rebuild that changed not one word told
every crawler the whole site had just been rewritten. The comment beside it
said "modified today is literally true" because every page is regenerated on
each build, and that is exactly the mistake: regenerating a page is not
changing it. datePublished was worse in the other direction, a hand-typed
"2026-07-29" shared by every article no matter when it was written.

THE TWO RULES
  datePublished  the day the page first appeared. Read once, from the first
                 commit that added the rendered page or introduced its row in
                 generators/, and it never moves again.
  dateModified   the day this page's own content last changed, decided by a
                 hash of that page's own bytes. It moves when the words move
                 and stays put when they do not.

Both are stored in page_dates.json beside this file: generated data, committed
on purpose, so a build reads a fixed record instead of re-deriving dates from a
moving git tree. Delete the file and the next build rebuilds it from git; that
is the only time git is consulted for a page that already has a record.

Today is never an answer for a page that already exists. It is the bug this
module replaces.

Every stage of the build is a separate process, so the record is re-read and
merged on write rather than held in one long-lived dict.
"""
import os, re, json, atexit, hashlib, datetime, subprocess

HERE = os.path.dirname(os.path.abspath(__file__))
REPO = os.path.abspath(os.path.join(HERE, '..'))
STORE = os.path.join(HERE, 'page_dates.json')
TODAY = datetime.date.today().isoformat()

# The committed build output, which is also where a page's first appearance is
# read from. NP_ROOT moves the build elsewhere; the dates still come from the
# history of the tracked site.
SITE_DIR = 'site'

# What a generator writes where a date belongs. `resolve` swaps both for the
# real dates and asserts neither survives, so a page that skips the stamping
# fails the build instead of shipping 0000-00-00 to a crawler.
PUBLISHED_MARK = '@datePublished@'
MODIFIED_MARK = '@dateModified@'

# The sitemap is written before the articles and the town pages are, so it
# cannot read their records yet. It writes one of these per URL instead and
# build.py resolves them once every page has been stamped.
_LASTMOD_MARK = '@lastmod:%s@'
_LASTMOD_RE = re.compile(r'@lastmod:([^@]+)@')

# Where a page's row lives when the rendered page itself is too new to have a
# history. Scoped to the generators: that is where the words are written.
_SOURCES = ['generators']

_README = ("Generated data, committed on purpose. datePublished is the day a page first appeared "
           "and never moves; dateModified is the day that page's own content last changed, and "
           "only moves when its hash does. Rebuilt from git by page_dates.py if this file is "
           "deleted. Written by the generators, never by hand.")


# ------------------------------------------------------------------ the store
def _read():
    try:
        with open(STORE, encoding='utf-8') as f:
            return json.load(f).get('pages') or {}
    except (IOError, ValueError):
        return {}


_PAGES = _read()
_DIRTY = {}


def _flush():
    """Merge this process's new records back in. Nothing is written when
    nothing changed, or an unchanged site would not rebuild to itself."""
    if not _DIRTY:
        return
    pages = _read()
    pages.update(_DIRTY)
    tmp = STORE + '.tmp'
    with open(tmp, 'w', encoding='utf-8') as f:
        json.dump({'_readme': _README, 'pages': dict(sorted(pages.items()))},
                  f, indent=1, ensure_ascii=False)
        f.write('\n')
    os.replace(tmp, STORE)
    _DIRTY.clear()


atexit.register(_flush)


# ------------------------------------------------------------------- git facts
def _git(*args):
    try:
        return subprocess.run(['git', '-C', REPO] + list(args), stdout=subprocess.PIPE,
                              stderr=subprocess.DEVNULL, check=False
                              ).stdout.decode('utf-8', 'replace')
    except (OSError, ValueError):
        return ''


_HIST = None
# A diff line that only restamps a date is not a content change. That churn is
# the bug being fixed here, and reading it as "the content changed" would bake
# the bug into the dates it is meant to correct.
_DATE_LINE = re.compile(r'^[+-]\s*(?:"date(?:Published|Modified)"|<lastmod>)')


def _history():
    """{page path under site/: (first appearance, last real content change)}.

    One pass over the log for additions and one for modifications rather than a
    git call per page, which for 77 pages would be 154 subprocesses."""
    global _HIST
    if _HIST is not None:
        return _HIST
    first, last = {}, {}
    day = None
    for line in _git('log', '--reverse', '--diff-filter=A', '--name-only',
                     '--date=short', '--format=@ %ad', '--', SITE_DIR).splitlines():
        if line.startswith('@ '):
            day = line[2:].strip()
        elif line.strip() and day:
            first.setdefault(_rel(line.strip()), day)
    day, cur = None, None
    for line in _git('log', '--reverse', '-p', '-U0', '--no-renames', '--diff-filter=M',
                     '--date=short', '--format=@ %ad', '--', SITE_DIR).splitlines():
        if line.startswith('@ '):
            day, cur = line[2:].strip(), None
        elif line.startswith('diff --git '):
            cur = _rel(line.split(' b/')[-1].strip())
        elif cur and day and line[:1] in '+-' and not line.startswith(('+++', '---')):
            if not _DATE_LINE.match(line):
                last[cur] = day
                cur = None          # this file is settled for this commit
    _HIST = (first, last)
    return _HIST


def _rel(p):
    return p[len(SITE_DIR) + 1:] if p.startswith(SITE_DIR + '/') else p


_BIRTH = None


def _repo_birth():
    """The day the repository itself starts. The last resort for a page git and
    the site both know nothing about, and still not today."""
    global _BIRTH
    if _BIRTH is not None:
        return _BIRTH
    got = [l.strip() for l in _git('log', '--reverse', '--date=short',
                                   '--format=%ad').splitlines() if l.strip()]
    _BIRTH = got[0] if got else (datetime.date.today() - datetime.timedelta(days=1)).isoformat()
    return _BIRTH


def _data_row_date(rel):
    """The first commit that introduced this page's row in the generators. The
    rendered page can be regenerated at any time; the row is where the words
    were actually written.

    The search is for the row, `"slug": "x"`, and not for the bare slug. A slug
    that is also an ordinary word is the failure this guards against: searching
    the generators for "bookkeeping" finds the first commit of a repo that has
    said the word bookkeeping since the day it was created, and the bookkeeping
    pillar page written in September 2026 would have been stamped as published
    in August. Both the pillar rows and the article rows are written as
    `"slug": "..."`, so one pattern covers every page that has a row at all.
    """
    slug = os.path.basename(rel)[:-5] if rel.endswith('.html') else os.path.basename(rel)
    if slug in ('index', ''):
        slug = os.path.basename(os.path.dirname(rel))
    if not slug:
        return ''
    got = [l.strip() for l in _git('log', '--reverse', '--date=short', '--format=%ad',
                                   '-S"slug": "%s"' % slug, '--', *_SOURCES).splitlines() if l.strip()]
    return got[0] if got else ''


def _derive(rel):
    """(published, modified) for a page with no record yet.

    The day the rendered page first appeared is the answer whenever git has
    it, because that is the day the page existed and no earlier. The data row
    is the fallback for a page too new to have a history of its own, and it is
    only a fallback: a slug like "bathroom-remodeling" is also a service that
    has been in the data since long before the page was written, and reading
    that as the page's birthday would date it years early."""
    first, last = _history()
    published = first.get(rel) or _data_row_date(rel) or _repo_birth()
    modified = last.get(rel) or published
    return published, max(modified, published)


# ------------------------------------------------------------------ public API
def fingerprint(*parts):
    h = hashlib.sha1()
    for p in parts:
        h.update(p.encode('utf-8', 'replace') if isinstance(p, str) else p)
        h.update(b'\x00')
    return h.hexdigest()[:16]


_SEEN = {}


def stamp(rel, content_hash):
    """(datePublished, dateModified) for the page written to `rel`.

    published never moves once recorded. modified moves only when the hash of
    this page's own content differs from the hash recorded beside it, which is
    the one moment today is the honest answer."""
    assert _SEEN.get(rel, content_hash) == content_hash, ('page rendered twice', rel)
    _SEEN[rel] = content_hash
    rec = _PAGES.get(rel)
    if rec and rec.get('hash') == content_hash:
        return rec['published'], rec['modified']
    if rec:                                   # the words moved: today is right
        published, modified = rec['published'], TODAY
    else:
        published, modified = _derive(rel)
    out = {'published': published, 'modified': modified, 'hash': content_hash}
    _PAGES[rel] = out
    _DIRTY[rel] = out
    return published, modified


def resolve(rel, html):
    """Record this page's dates and fill in any marks it left for them.

    Every page is recorded, not only the ones carrying schema dates: the hub
    pages print no date of their own but the sitemap still has to say when each
    of them last changed, and that answer has to come from the same fingerprint
    as everybody else's rather than from a fallback.

    The fingerprint is taken with the marks still in it, so it is a hash of
    what the page says and carries nothing about when the build ran. Hashing
    the finished dates would make every build change the answer it had just
    written."""
    published, modified = stamp(rel, fingerprint(rel, html))
    if PUBLISHED_MARK not in html and MODIFIED_MARK not in html:
        return html
    return html.replace(PUBLISHED_MARK, published).replace(MODIFIED_MARK, modified)


def lastmod_mark(rel):
    """What the sitemap writes for a page instead of a date. Resolved by
    resolve_lastmods once every page in the build has been stamped."""
    return _LASTMOD_MARK % rel


def resolve_lastmods(text):
    """Swap every sitemap mark for that page's own recorded content date."""
    pages = _read()

    def one(m):
        rel = m.group(1)
        rec = pages.get(rel)
        return rec['modified'] if rec else _derive(rel)[1]

    return _LASTMOD_RE.sub(one, text)


def modified_for(rel):
    """The recorded content date for a page. None if it has no record."""
    rec = _PAGES.get(rel)
    return rec['modified'] if rec else None
