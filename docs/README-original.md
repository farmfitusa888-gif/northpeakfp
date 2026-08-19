# NorthPeak Financial Partners — Project Root

**START WITH `HANDOFF.md`.** It contains everything needed to pick this up cold.

## Layout
- `HANDOFF.md`     — full project handoff. Read first.
- `generators/`    — Python scripts that build the site. The HTML is generated, not hand-written.
- `northpeak-site/`— the current built site (this is what deploys to Netlify)
- `guides/`        — setup/launch guide and SEO playbook PDFs

## Quick start
    pip install reportlab pillow beautifulsoup4
    # set ROOT in generators/build_site.py to your output path
    python3 generators/build_site.py
    python3 generators/build_pages.py
    python3 generators/build_pages2.py
    python3 generators/build_articles_shell.py
    python3 generators/mk_photos.py

## Immediate task
Google Search Console indexing errors. See HANDOFF.md §7 — the leading hypothesis
is duplicate URLs (`/services` and `/services.html` both return 200), with a
concrete `_redirects` fix proposed.
