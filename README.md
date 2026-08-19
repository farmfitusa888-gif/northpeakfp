# NorthPeak Financial Partners — northpeakfp.com

Static site. **The HTML is generated — never hand-edit it.** Edit the generators
and rebuild; anything typed directly into `site/` is destroyed on the next build.

## Build

```bash
python3 generators/build.py
```

Writes 32 HTML pages plus assets into `site/`. No dependencies, no build step at
runtime, no framework. Override the output path with `NP_ROOT=/some/path`.

## Verify

```bash
python3 tools/validate.py
```

Must report 0 errors before any deploy.

## Layout

| Path | What it is |
|---|---|
| `generators/` | Source of truth. Python that emits the whole site. |
| `generators/static/` | Files the generators don't write (redirects, headers, photos), copied verbatim into the output. |
| `site/` | Build output. Netlify's publish directory. Committed so deploys are reproducible. |
| `tools/` | Validator and audit scripts. |
| `docs/` | Handoff notes and the two client PDFs. |

## Where to change what

| Change | File |
|---|---|
| Firm name, phone, email, city, founder | `generators/generate_articles_northpeak.py` (CLIENT CONFIG) |
| Article text, add/remove articles | `generators/generate_articles_northpeak.py` (`ARTICLES`) |
| Colors, fonts, all styling | `generators/build_site.py` (the `CSS` string) |
| Nav, footer, meta tags on every page | `generators/build_site.py` (`shell()`) |
| Homepage | `generators/build_pages.py` |
| Services / About / Contact / Resources | `generators/build_pages2.py` |
| Article page layout | `generators/build_articles_shell.py` |
| Redirects and security headers | `generators/static/_redirects`, `generators/static/netlify.toml` |

## Hard constraints

- **Chaudhry Ahmad is not a CPA.** Nothing on the site, in schema, or in any
  metadata may state or imply CPA status. This is Illinois law, not style.
- **No invented statistics, testimonials, client counts, or guarantees.** The two
  illustrative benchmark figures on the homepage are labeled as illustrative;
  keep that labeling.
- **No published pricing.** Every engagement is quoted individually.
- **Do not touch the MX, SPF, or DKIM DNS records** at the registrar. They carry
  `info@northpeakfp.com` on Google Workspace.
