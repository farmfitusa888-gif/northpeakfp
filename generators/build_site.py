#!/usr/bin/env python3
"""Build the complete NorthPeak Financial Partners website."""
import os, sys, json, shutil, html, pathlib, re, posixpath
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
import generate_articles_northpeak as G

# Output directory. Defaults to <repo>/site so the build is machine-independent.
# Override with:  NP_ROOT=/some/path python3 build.py
ROOT = os.environ.get("NP_ROOT") or str(
    (pathlib.Path(__file__).resolve().parent.parent / "site"))
os.makedirs(ROOT, exist_ok=True)

SITE, FIRM, EMAIL = G.SITE, G.FIRM, G.EMAIL
CAL_PLACEHOLDER = "PASTE_YOUR_GOOGLE_CALENDAR_APPOINTMENT_URL_HERE"
FORM_PLACEHOLDER = "https://formspree.io/f/xpqvvbqg"

# Google Analytics 4 measurement ID for the northpeakfp.com web data stream
# (stream ID 15461234948). Set to "" to strip analytics from every page.
GA4_ID = "G-CQWJKFGY3T"

# Loaded async so it never blocks first paint. IP anonymisation is on and ad
# personalisation signals are off: this is a B2B accounting site measuring
# consultation requests, not building advertising audiences, and the narrower
# configuration is the one that stays defensible if privacy rules tighten.
GA4_SNIPPET = f"""<script async src="https://www.googletagmanager.com/gtag/js?id={GA4_ID}"></script>
<script>
window.dataLayer=window.dataLayer||[];function gtag(){{dataLayer.push(arguments)}}
gtag('js',new Date());
gtag('config','{GA4_ID}',{{anonymize_ip:true,allow_google_signals:false,allow_ad_personalization_signals:false}});
</script>""" if GA4_ID else ""

# ---------------------------------------------------------------- CSS
CSS = r"""
/* Self-hosted variable fonts. Previously loaded from fonts.googleapis.com,
   which cost a render-blocking stylesheet plus DNS+TLS to two third-party
   hosts before any text could paint. Google serves one variable file per
   family/subset — the per-weight URLs are byte-identical — so four weights
   are covered by a single file each. Only the latin subset is shipped; the
   latin-ext subset added 145KB of accented glyphs this site never uses. */
@font-face{font-family:'Inter';font-style:normal;font-weight:400 700;font-display:swap;
  src:url('/assets/fonts/inter-var-latin.woff2') format('woff2');
  unicode-range:U+0000-00FF,U+0131,U+0152-0153,U+02BB-02BC,U+02C6,U+02DA,U+02DC,U+0304,U+0308,U+0329,U+2000-206F,U+20AC,U+2122,U+2191,U+2193,U+2212,U+2215,U+FEFF,U+FFFD}
@font-face{font-family:'Fraunces';font-style:normal;font-weight:400 700;font-display:swap;
  src:url('/assets/fonts/fraunces-var-latin.woff2') format('woff2');
  unicode-range:U+0000-00FF,U+0131,U+0152-0153,U+02BB-02BC,U+02C6,U+02DA,U+02DC,U+0304,U+0308,U+0329,U+2000-206F,U+20AC,U+2122,U+2191,U+2193,U+2212,U+2215,U+FEFF,U+FFFD}
:root{
  --ink:#0a1a14; --ink-2:#12261f; --soft:#4a5f56; --mute:#7b8d85;
  --paper:#fbfaf6; --paper-2:#f2efe6; --card:#ffffff;
  --accent:#1f6f54; --accent-2:#2a8f6d; --deep:#0e3326; --gold:#b8860b; --gold-2:#d4a437;
  --rule:#e0dacb; --shadow:0 1px 2px rgba(10,26,20,.04),0 8px 24px rgba(10,26,20,.06);
  --shadow-lg:0 2px 4px rgba(10,26,20,.05),0 24px 60px rgba(10,26,20,.12);
  --r:14px; --maxw:1180px;
}
*{box-sizing:border-box;margin:0;padding:0}
html{scroll-behavior:smooth;-webkit-text-size-adjust:100%}
body{font-family:'Inter',system-ui,-apple-system,sans-serif;color:var(--ink);background:var(--paper);
  line-height:1.7;font-size:1.02rem;-webkit-font-smoothing:antialiased;overflow-x:hidden}
img{max-width:100%;display:block}
a{color:var(--accent)}
.wrap{max-width:var(--maxw);margin:0 auto;padding:0 28px}
.narrow{max-width:760px;margin:0 auto;padding:0 28px}
h1,h2,h3,h4{font-family:'Fraunces',Georgia,serif;font-weight:600;letter-spacing:-.02em;line-height:1.12}
.serif{font-family:'Fraunces',Georgia,serif}
.eyebrow{font-size:.75rem;font-weight:700;letter-spacing:.16em;text-transform:uppercase;color:var(--accent);margin-bottom:14px}
.lead{font-size:1.18rem;color:var(--soft);line-height:1.65}

/* ---------- skip link + a11y ---------- */
.vh{position:absolute;width:1px;height:1px;padding:0;margin:-1px;overflow:hidden;clip:rect(0 0 0 0);white-space:nowrap;border:0}
.skip{position:absolute;left:-9999px;top:0;background:var(--deep);color:#fff;padding:12px 20px;z-index:999}
.skip:focus{left:0}
:focus-visible{outline:2px solid var(--gold);outline-offset:3px;border-radius:4px}

/* ---------- nav ---------- */
.nav{position:sticky;top:0;z-index:100;background:rgba(251,250,246,.85);backdrop-filter:blur(14px);
  border-bottom:1px solid var(--rule);transition:box-shadow .25s}
.nav.scrolled{box-shadow:0 4px 24px rgba(10,26,20,.07)}
.nav-in{display:flex;align-items:center;justify-content:space-between;padding:16px 0;gap:20px}
.brand{display:flex;align-items:center;gap:11px;text-decoration:none;color:var(--ink);flex-shrink:0}
.brand svg{flex-shrink:0}
.brand b{font-family:'Fraunces',serif;font-size:1.06rem;font-weight:600;letter-spacing:-.01em;line-height:1.15}
.brand span{display:block;font-family:'Inter',sans-serif;font-size:.63rem;letter-spacing:.15em;
  text-transform:uppercase;color:var(--mute);font-weight:600;margin-top:2px}
.links{display:flex;align-items:center;gap:22px}
@media(min-width:901px) and (max-width:1130px){.links{gap:15px}.links a{font-size:.88rem}}
.links a{color:var(--soft);text-decoration:none;font-size:.93rem;font-weight:500;position:relative;padding:4px 0}
.links a:hover,.links a[aria-current="page"]{color:var(--accent)}
.links a[aria-current="page"]::after{content:"";position:absolute;left:0;right:0;bottom:-2px;height:2px;background:var(--gold);border-radius:2px}
.btn{display:inline-flex;align-items:center;gap:8px;background:var(--accent);color:#fff;font-weight:600;
  text-decoration:none;padding:12px 24px;border-radius:9px;font-size:.94rem;border:none;cursor:pointer;
  transition:transform .18s cubic-bezier(.2,.8,.2,1),box-shadow .18s;box-shadow:0 4px 14px rgba(31,111,84,.24)}
.btn:hover{transform:translateY(-2px);box-shadow:0 8px 22px rgba(31,111,84,.32)}
.btn.gold{background:var(--gold);color:#1a1405;box-shadow:0 4px 14px rgba(184,134,11,.28)}
.btn.ghost{background:transparent;color:var(--accent);border:1.5px solid var(--accent);box-shadow:none}
.btn.ghost:hover{background:var(--accent);color:#fff}
.btn.lg{padding:15px 32px;font-size:1rem}
.burger{display:none}

/* ---------- nav: one non-scrolling row at every width ----------
   No hamburger and no horizontal scroll, which means seven destinations have to
   physically fit. Three things buy the space on a phone: the wordmark drops to
   the mark alone, the CTA button leaves the bar (the hero, footer and every
   page body already carry one), and "Service Areas" shortens to "Areas" via the
   .nav-long span. Measured to fit down to 320px. */
@media(max-width:900px){
  .nav-in{padding:11px 0;gap:12px}
  .brand span{display:none}
  .nav-cta{display:none}
  .links{gap:11px;flex:1;justify-content:flex-end;overflow:visible}
  .links a{font-size:.8rem;padding:3px 0;letter-spacing:-.005em}
  .nav-long{display:none}
}
@media(max-width:420px){
  .nav .wrap{padding:0 14px}
  .links{gap:8px}
  .links a{font-size:.735rem}
}
@media(max-width:350px){.links{gap:6px}.links a{font-size:.69rem}}

/* ---------- nav: adopts the section behind it ----------
   Over a dark section the bar goes dark with light text; over paper it returns
   to the translucent cream. Driven by app.js, which measures which themed
   section sits under the bar on scroll. */
.nav{transition:background .35s ease,border-color .35s ease,box-shadow .25s ease}
.nav.on-dark{background:rgba(7,25,18,.78);border-bottom-color:rgba(255,255,255,.10)}
.nav.on-dark .brand{color:#fff}
.nav.on-dark .brand b{color:#fff}
.nav.on-dark .brand span{color:#a9c4b9}
.nav.on-dark .links a{color:#d7e5de}
.nav.on-dark .links a:hover,.nav.on-dark .links a[aria-current="page"]{color:var(--gold-2)}
.nav.on-dark .burger span{background:#fff}

/* ---------- hero w/ video ---------- */
.hero{position:relative;min-height:clamp(560px,88vh,860px);display:flex;align-items:center;
  overflow:hidden;background:var(--deep);isolation:isolate}
.hero .fallback{position:absolute;inset:0;width:100%;height:100%;z-index:-3}
.hero .fallback{background:
  radial-gradient(760px 420px at 72% 26%,rgba(212,164,55,.20) 0%,transparent 62%),
  radial-gradient(1100px 620px at 18% 4%,#1d5c45 0%,transparent 58%),
  radial-gradient(900px 520px at 88% 84%,#12392a 0%,transparent 66%),
  linear-gradient(168deg,#0f3728 0%,#0a2419 52%,#061710 100%)}
.hero::after{content:"";position:absolute;inset:0;z-index:-1;pointer-events:none;
  background:
    radial-gradient(115% 88% at 20% 52%,rgba(6,23,16,.93) 0%,rgba(6,23,16,.80) 30%,
      rgba(6,23,16,.42) 55%,rgba(6,23,16,.10) 74%,rgba(6,23,16,0) 88%),
    linear-gradient(0deg,rgba(6,23,16,.55) 0%,rgba(6,23,16,.12) 26%,rgba(6,23,16,0) 52%)}
@media(max-width:900px){.hero::after{background:linear-gradient(178deg,rgba(6,23,16,.45) 0%,
  rgba(6,23,16,.74) 44%,rgba(6,23,16,.92) 100%)}}
#summit{position:absolute;inset:0;width:100%;height:100%;z-index:-2;opacity:0;transition:opacity .9s ease;pointer-events:none;display:block}
.hero-in{padding-top:120px;padding-bottom:100px;max-width:720px;color:#fff}
@media(max-width:900px){.hero-in{padding-top:78px;padding-bottom:64px}}
.hero h1{font-size:clamp(2.5rem,6vw,4.4rem);color:#fff;margin-bottom:22px}
.hero h1 em{font-style:normal;color:var(--gold-2);display:block}
.hero p{font-size:clamp(1.05rem,2vw,1.24rem);color:#cfe0d8;max-width:590px;margin-bottom:34px}
.hero-cta{display:flex;gap:14px;flex-wrap:wrap;margin-bottom:44px}
.hero .btn.ghost{color:#fff;border-color:rgba(255,255,255,.45)}
.hero .btn.ghost:hover{background:#fff;color:var(--deep);border-color:#fff}
.trust{display:flex;gap:30px;flex-wrap:wrap;padding-top:26px;border-top:1px solid rgba(255,255,255,.16)}
.trust div{color:#a9c4b9;font-size:.85rem;display:flex;align-items:center;gap:8px}
.trust svg{flex-shrink:0}

/* ───────────────────────── editorial layout system ─────────────────────────
   Added to break the repeated eyebrow -> h2 -> lead -> 3-up-card-grid rhythm
   that ran on every section. Same palette, same type, different structure. */

/* Split: a heading column that stays put while its content scrolls past.
   Deliberately unequal — 4/12 against 7/12 with a gutter column between. */
.split{display:grid;grid-template-columns:minmax(0,4fr) 1fr minmax(0,7fr);align-items:start}
.split > .sh{position:sticky;top:104px}
.split > .sh h2{font-size:clamp(1.75rem,3.2vw,2.45rem);line-height:1.08;
  letter-spacing:-.03em;color:var(--ink-2)}
.split > .sh p{color:var(--soft);font-size:.97rem;margin-top:14px;max-width:34ch}
.split > .sb{grid-column:3}
.dark .split > .sh h2{color:#fff}
.dark .split > .sh p{color:#b6cdc3}
@media(max-width:900px){.split{grid-template-columns:1fr;gap:34px}
  .split > .sh{position:static}.split > .sb{grid-column:1}}

/* Ledger: numbered rows on hairlines. Replaces card grids for anything that
   is really a list — services, tiers, articles. Four unequal columns. */
.ledger{border-top:1px solid var(--rule)}
.lrow{display:grid;grid-template-columns:54px minmax(0,1.05fr) minmax(0,1.5fr) auto;
  gap:26px;align-items:baseline;padding:26px 0;border-bottom:1px solid var(--rule);
  transition:background .18s}
.lrow:hover{background:rgba(31,111,84,.04)}
.lrow .ln{font-family:'Fraunces',serif;font-size:.95rem;color:var(--mute);letter-spacing:.04em}
.lrow h3{font-family:'Fraunces',serif;font-size:1.35rem;letter-spacing:-.02em;color:var(--ink-2)}
.lrow p{color:var(--soft);font-size:.97rem;line-height:1.58}
.lrow .lgo{font-size:.85rem;color:var(--accent);text-decoration:none;white-space:nowrap}
.lrow .lgo:hover{text-decoration:underline}
.dark .ledger{border-color:rgba(255,255,255,.16)}
.dark .lrow{border-color:rgba(255,255,255,.16)}
.dark .lrow:hover{background:rgba(255,255,255,.04)}
.dark .lrow h3{color:#fff}.dark .lrow p{color:#b6cdc3}
.dark .lrow .ln{color:#7f9a8e}.dark .lrow .lgo{color:var(--gold-2)}
@media(max-width:760px){.lrow{grid-template-columns:38px 1fr;gap:8px 16px}
  .lrow p,.lrow .lgo{grid-column:2}.lrow .lgo{margin-top:6px}}

/* Figures: one dominant number carrying the point, the rest in support.
   Replaces the four-equal-cells stat band. */
.figrow{display:grid;grid-template-columns:minmax(0,1.15fr) minmax(0,2fr);
  gap:clamp(28px,5vw,72px);align-items:center}
.fighero .n{font-family:'Fraunces',serif;font-size:clamp(3.6rem,9vw,6.4rem);font-weight:600;
  color:var(--gold-2);line-height:.86;letter-spacing:-.045em}
.fighero .l{color:#b6cdc3;font-size:1.02rem;line-height:1.45;margin-top:16px;max-width:26ch}
.figrest{display:grid;grid-template-columns:repeat(auto-fit,minmax(150px,1fr));
  border-top:1px solid rgba(255,255,255,.16)}
.figrest > div{padding:22px 24px 22px 0;border-bottom:1px solid rgba(255,255,255,.16)}
.figrest .n{font-family:'Fraunces',serif;font-size:1.85rem;font-weight:600;color:#fff;line-height:1;
  letter-spacing:-.03em}
.figrest .l{font-size:.82rem;color:#9fbcb0;margin-top:9px;line-height:1.45}
@media(max-width:900px){.figrow{grid-template-columns:1fr}}

/* Entry list: articles as an index, not a deck of cards. */
.elist{border-top:1px solid var(--rule)}
.entry{display:grid;grid-template-columns:minmax(0,150px) minmax(0,1fr) auto;gap:26px;
  align-items:baseline;padding:24px 0;border-bottom:1px solid var(--rule);
  text-decoration:none;color:inherit;transition:background .18s}
.entry:hover{background:rgba(31,111,84,.04)}
.entry .ec{font-size:.72rem;letter-spacing:.14em;text-transform:uppercase;color:var(--accent);
  padding-top:5px}
.entry h3{font-family:'Fraunces',serif;font-size:1.22rem;letter-spacing:-.018em;
  color:var(--ink-2);line-height:1.25}
.entry p{color:var(--soft);font-size:.93rem;margin-top:7px;line-height:1.55}
.entry .er{font-size:.8rem;color:var(--mute);white-space:nowrap}
.entry:hover h3{color:var(--accent)}
@media(max-width:760px){.entry{grid-template-columns:1fr;gap:6px}.entry .er{display:none}}

/* Rule head: a section label sitting on a hairline instead of a centred
   eyebrow + heading + lead stack. */
.rhead{display:flex;justify-content:space-between;align-items:baseline;gap:20px;
  border-bottom:1px solid var(--ink-2);padding-bottom:11px;margin-bottom:6px;
  font-size:.72rem;letter-spacing:.19em;text-transform:uppercase;color:var(--mute)}
.dark .rhead{border-color:rgba(255,255,255,.4);color:#9fbcb0}

/* Service-area county groups: the assessor is stated once per county instead
   of repeated on every row, and the township label carries the towns that share
   it. */
.acounty{margin-bottom:44px}
.acounty:last-child{margin-bottom:0}
.acounty .rhead h2{font-family:'Inter',sans-serif;font-size:.72rem;letter-spacing:.19em;
  text-transform:uppercase;color:var(--mute);font-weight:600}
.acounty .lrow{grid-template-columns:minmax(0,200px) minmax(0,1.6fr) minmax(0,150px) auto}
.acounty .lrow .ln{font-family:'Inter',sans-serif;font-size:.78rem;letter-spacing:.06em;
  text-transform:uppercase;color:var(--accent);font-weight:600}
.acounty .lrow h3{font-family:'Inter',sans-serif;font-size:1rem;font-weight:500;letter-spacing:0}
.acounty .lrow h3 a{color:var(--ink-2);text-decoration:none;border-bottom:1px solid var(--rule)}
.acounty .lrow h3 a:hover{color:var(--accent);border-color:var(--accent)}
.acounty .lrow p{font-size:.8rem;color:var(--mute)}
@media(max-width:760px){.acounty .rhead h2{font-family:'Inter',sans-serif;font-size:.72rem;letter-spacing:.19em;
  text-transform:uppercase;color:var(--mute);font-weight:600}
.acounty .lrow{grid-template-columns:1fr}
  .acounty .lrow p{grid-column:1}}

/* Mountain band: full-bleed, the 3D scene at full strength as its own moment
   in the page rather than only as hero wallpaper. */
.mband{position:relative;background:var(--deep);overflow:hidden;isolation:isolate;
  min-height:clamp(420px,54vh,640px);display:flex;align-items:flex-end}
.mband .mfall{position:absolute;inset:0;z-index:-3;background:
  radial-gradient(760px 420px at 68% 22%,rgba(212,164,55,.18) 0%,transparent 62%),
  linear-gradient(172deg,#10402f 0%,#0a2419 58%,#061710 100%)}
#summit-band{position:absolute;inset:0;width:100%;height:100%;z-index:-2;opacity:0;
  transition:opacity 1s ease;pointer-events:none;display:block}
.mband::after{content:"";position:absolute;inset:0;z-index:-1;pointer-events:none;
  background:linear-gradient(0deg,rgba(6,23,16,.92) 0%,rgba(6,23,16,.45) 42%,
    rgba(6,23,16,.06) 78%,rgba(6,23,16,0) 100%)}
.mband > .wrap{width:100%}
.mband .mb-in{padding:0 0 52px;color:#fff;max-width:44ch}
.mband h2{font-size:clamp(1.7rem,3.4vw,2.5rem);letter-spacing:-.03em;line-height:1.1;color:#fff}
.mband p{color:#c2d8ce;margin-top:14px;font-size:1.02rem}
@media print{.mband{min-height:0}#summit-band{display:none}}

/* ---- long-form prose (articles and local guides) ----
   Previously inlined per page via extra_head, so this rode along on all 25
   article pages instead of being cached once. Moved here when the local
   guides began using the same .aw / .abody container. */
.aw{max-width:760px;margin:0 auto;padding:0 28px}
.ahead{padding-top:52px}
.ahead h1{font-size:clamp(2rem,4.6vw,3rem);margin-bottom:20px;color:var(--ink-2)}
.abyline{display:flex;align-items:center;gap:12px;flex-wrap:wrap;padding:16px 0;
  border-top:1px solid var(--rule);border-bottom:1px solid var(--rule);font-size:.88rem;color:var(--soft);margin-bottom:8px}
.abyline strong{color:var(--ink-2)}
.abyline .dot{width:4px;height:4px;border-radius:50%;background:var(--gold)}
.abody{padding-top:14px;padding-bottom:30px;font-size:1.06rem}
.abody h2{font-size:1.55rem;color:var(--deep);margin:42px 0 13px}
.abody h2 .num{color:var(--gold);font-size:.95rem;font-weight:700;display:block;margin-bottom:5px;
  letter-spacing:.06em;font-family:'Inter',sans-serif}
.abody p{margin-bottom:19px;color:var(--ink)}
.abody a{color:var(--accent);text-underline-offset:2px}
.toc{background:var(--paper-2);border-radius:12px;padding:22px 26px;margin:28px 0 8px}
.toc p{font-size:.74rem;font-weight:700;letter-spacing:.13em;text-transform:uppercase;color:var(--accent);margin-bottom:12px}
.toc ol{margin-left:18px;font-size:.93rem}
.toc li{margin-bottom:7px}
.toc a{color:var(--soft);text-decoration:none}
.toc a:hover{color:var(--accent);text-decoration:underline}
.acta{background:linear-gradient(140deg,var(--deep),#0a2519);border-radius:16px;padding:38px 32px;
  margin:44px 0;text-align:center;color:#fff;box-shadow:var(--shadow-lg)}
.acta h3{color:#fff;font-size:1.35rem;margin-bottom:10px}
.acta p{color:#b6cdc3;margin-bottom:22px;font-size:.97rem}
.adisc{font-size:.85rem;color:var(--mute);font-style:italic;border-top:1px solid var(--rule);padding-top:18px}
.arel{margin:46px 0 10px}
.arel h3{font-size:1.25rem;color:var(--deep);margin-bottom:16px}
.arel .arts{grid-template-columns:repeat(auto-fill,minmax(240px,1fr))}

/* ---------- reveal ---------- */
/* Reveal-on-scroll, as progressive enhancement rather than a dependency.
   The hidden state is scoped to html.js, a class added by an inline script in
   the head ONLY when IntersectionObserver exists to remove it again. Before
   this, .rv set opacity:0 unconditionally — so if app.js failed to load, was
   blocked, or errored, 34 elements of page content stayed invisible forever. */
.js .rv{opacity:0;transform:translateY(26px);transition:opacity .7s cubic-bezier(.2,.8,.2,1),transform .7s cubic-bezier(.2,.8,.2,1)}
.js .rv.in{opacity:1;transform:none}

/* ---------- sections ---------- */
section{padding:96px 0}
.pad-s{padding:58px 0}
.pad-l{padding:132px 0}
.pad-t0{padding-top:0}
.sec-head{max-width:660px;margin-bottom:50px}
.sec-head h2{font-size:clamp(1.9rem,4vw,2.7rem);margin-bottom:16px;color:var(--ink-2)}
.alt{background:var(--paper-2)}
.dark{background:var(--deep);color:#e6efea}
.dark h2,.dark h3{color:#fff}
.dark .lead,.dark p{color:#b6cdc3}
.dark .eyebrow{color:var(--gold-2)}

/* ---------- stat band (data driven) ---------- */
.stats{display:grid;grid-template-columns:repeat(auto-fit,minmax(190px,1fr));gap:2px;background:rgba(255,255,255,.1);
  border-radius:var(--r);overflow:hidden}
.stat{background:var(--deep);padding:34px 26px;text-align:center}
.stat .n{font-family:'Fraunces',serif;font-size:clamp(2rem,4.5vw,2.9rem);font-weight:600;color:var(--gold-2);line-height:1;letter-spacing:-.03em}
.stat .l{font-size:.83rem;color:#9fbcb0;margin-top:10px;line-height:1.45}

/* ---------- cards / 3D ---------- */
.grid{display:grid;gap:24px}
.g2{grid-template-columns:repeat(auto-fit,minmax(300px,1fr))}
.g3{grid-template-columns:repeat(auto-fit,minmax(285px,1fr))}
.card{background:transparent;border:0;border-top:1px solid var(--rule);border-radius:0;
  padding:30px 30px 30px 0;box-shadow:none;transition:background .2s,border-color .2s}
.card:hover{background:rgba(31,111,84,.035);border-color:var(--accent)}
.card h3{font-size:1.28rem;margin-bottom:10px;color:var(--ink-2)}
.card p{color:var(--soft);font-size:.97rem}
.icon{width:46px;height:46px;border-radius:11px;display:grid;place-items:center;margin-bottom:18px;
  background:linear-gradient(140deg,var(--accent),var(--deep));box-shadow:0 6px 16px rgba(31,111,84,.26)}

/* pricing 3D tilt */
.tier{background:var(--card);border:1px solid var(--rule);border-radius:6px;padding:34px 30px;
  display:flex;flex-direction:column;position:relative;box-shadow:var(--shadow);
  transition:transform .35s cubic-bezier(.2,.8,.2,1),box-shadow .35s;transform-style:preserve-3d}
.tier:hover{border-color:var(--accent)}
.tier.feat{border:1.5px solid var(--gold);box-shadow:0 2px 6px rgba(10,26,20,.06),0 26px 60px rgba(184,134,11,.16)}
.tag{position:absolute;top:-12px;left:50%;transform:translateX(-50%);background:var(--gold);color:#1a1405;
  font-size:.7rem;font-weight:700;letter-spacing:.12em;text-transform:uppercase;padding:6px 16px;border-radius:20px;white-space:nowrap}
.tier h2{font-size:1.4rem;margin-bottom:6px}
.tier .who{color:var(--mute);font-size:.87rem;margin-bottom:20px;min-height:38px}
.price{font-family:'Fraunces',serif;font-size:2.5rem;font-weight:600;color:var(--ink-2);letter-spacing:-.03em;line-height:1}
.price small{font-size:.9rem;color:var(--mute);font-family:'Inter',sans-serif;font-weight:500;letter-spacing:0}
.price.quote{font-size:1.6rem;color:var(--accent)}
.tier ul{list-style:none;margin:24px 0;flex-grow:1}
.tier li{padding-left:27px;position:relative;margin-bottom:11px;font-size:.94rem;color:var(--soft)}
.tier li::before{content:"";position:absolute;left:0;top:8px;width:15px;height:15px;border-radius:50%;
  background:var(--accent);opacity:.13}
.tier li::after{content:"";position:absolute;left:5px;top:11px;width:4px;height:7px;border-right:2px solid var(--accent);
  border-bottom:2px solid var(--accent);transform:rotate(42deg)}
.fit{font-size:.83rem;color:var(--mute);border-top:1px solid var(--rule);padding-top:15px;margin-bottom:20px}

/* ---------- charts ---------- */
.viz{background:var(--card);border:1px solid var(--rule);border-radius:6px;padding:28px;box-shadow:none}
.viz h2,.viz h3{font-size:1.03rem;margin-bottom:4px;color:var(--ink-2)}
.viz .cap{font-size:.82rem;color:var(--mute);margin-bottom:22px}
.bar{display:flex;align-items:center;gap:14px;margin-bottom:15px}
.bar .lb{width:112px;font-size:.85rem;color:var(--soft);flex-shrink:0;text-align:right}
.bar .track{flex-grow:1;height:26px;background:var(--paper-2);border-radius:7px;overflow:hidden}
.bar .fill{height:100%;border-radius:7px;width:0;transition:width 1.3s cubic-bezier(.2,.8,.2,1);
  background:linear-gradient(90deg,var(--accent),var(--accent-2));display:flex;align-items:center;
  justify-content:flex-end;padding-right:10px;color:#fff;font-size:.76rem;font-weight:600}
.bar.hl .fill{background:linear-gradient(90deg,var(--gold),var(--gold-2));color:#1a1405}
.donut-wrap{display:flex;align-items:center;gap:26px;flex-wrap:wrap;justify-content:center}
.legend{list-style:none;font-size:.87rem}
.legend li{display:flex;align-items:center;gap:9px;margin-bottom:9px;color:var(--soft)}
.legend i{width:11px;height:11px;border-radius:3px;flex-shrink:0}

/* ---------- process ---------- */
.steps{counter-reset:s;display:grid;gap:22px;grid-template-columns:repeat(auto-fit,minmax(220px,1fr))}
.step{position:relative;padding:28px 24px;background:rgba(255,255,255,.05);border:1px solid rgba(255,255,255,.11);border-radius:var(--r)}
.step::before{counter-increment:s;content:"0" counter(s);font-family:'Fraunces',serif;font-size:1.9rem;
  color:var(--gold-2);opacity:.85;display:block;margin-bottom:12px;line-height:1}
.step h3{font-size:1.1rem;margin-bottom:8px}
.step p{font-size:.92rem}

/* ---------- articles ---------- */
.filters{display:flex;gap:9px;flex-wrap:wrap;margin-bottom:34px}
.chip{background:var(--card);border:1px solid var(--rule);color:var(--soft);padding:8px 17px;border-radius:22px;
  font-size:.86rem;cursor:pointer;font-family:inherit;font-weight:500;transition:.2s}
.chip:hover{border-color:var(--accent);color:var(--accent)}
.chip.on{background:var(--accent);border-color:var(--accent);color:#fff}
.arts{display:grid;gap:20px;grid-template-columns:repeat(auto-fill,minmax(300px,1fr))}
.art{background:var(--card);border:1px solid var(--rule);border-radius:var(--r);padding:26px;text-decoration:none;
  display:flex;flex-direction:column;box-shadow:var(--shadow);transition:transform .28s cubic-bezier(.2,.8,.2,1),box-shadow .28s,border-color .28s}
.art:hover{background:rgba(31,111,84,.04);border-color:var(--accent)}
.art .cat{font-size:.7rem;font-weight:700;letter-spacing:.13em;text-transform:uppercase;color:var(--accent);margin-bottom:11px}
.art h3{font-size:1.14rem;line-height:1.3;margin-bottom:10px;color:var(--ink-2)}
.art p{font-size:.9rem;color:var(--soft);flex-grow:1;margin-bottom:16px}
.art .rd{font-size:.79rem;color:var(--mute);display:flex;align-items:center;gap:6px}
.search{width:100%;padding:14px 18px;border:1px solid var(--rule);border-radius:10px;font-size:.97rem;
  font-family:inherit;margin-bottom:20px;background:var(--card);color:var(--ink)}
.search:focus{outline:none;border-color:var(--accent);box-shadow:0 0 0 3px rgba(31,111,84,.12)}

/* ---------- FAQ ---------- */
.faq{border-bottom:1px solid var(--rule)}
.faq summary{padding:20px 0;cursor:pointer;font-weight:600;font-size:1.04rem;list-style:none;
  display:flex;justify-content:space-between;align-items:center;gap:16px;color:var(--ink-2)}
.faq summary::-webkit-details-marker{display:none}
.faq summary::after{content:"+";font-size:1.4rem;color:var(--accent);flex-shrink:0;transition:transform .25s;font-weight:400}
.faq[open] summary::after{transform:rotate(45deg)}
.faq p{padding:0 0 22px;color:var(--soft);font-size:.97rem;max-width:74ch}

/* ---------- forms ---------- */
.form{background:var(--card);border:1px solid var(--rule);border-radius:6px;padding:34px;box-shadow:none}
.fg{margin-bottom:19px}
.fg label{display:block;font-size:.86rem;font-weight:600;margin-bottom:7px;color:var(--ink-2)}
.fg input,.fg select,.fg textarea{width:100%;padding:12px 15px;border:1px solid var(--rule);border-radius:9px;
  font-size:.96rem;font-family:inherit;background:var(--paper);color:var(--ink);transition:.2s}
.fg input:focus,.fg select:focus,.fg textarea:focus{outline:none;border-color:var(--accent);
  box-shadow:0 0 0 3px rgba(31,111,84,.12);background:#fff}
.fg textarea{min-height:130px;resize:vertical}
.req{color:#b23b3b}
.hp{position:absolute;left:-9999px}
.note{font-size:.83rem;color:var(--mute);margin-top:14px}

/* ---------- calculator ---------- */
.calc{background:linear-gradient(150deg,var(--deep),#0a2519);border-radius:6px;padding:36px;color:#fff;box-shadow:none}
.calc h2{color:#fff;font-size:1.4rem;margin-bottom:8px}
.calc .sub{color:#a9c4b9;font-size:.92rem;margin-bottom:26px}
.calc label{display:block;font-size:.85rem;color:#cfe0d8;margin-bottom:8px;font-weight:500}
.calc input[type=range]{width:100%;accent-color:var(--gold-2);margin-bottom:6px}
.calc .val{font-family:'Fraunces',serif;font-size:1.3rem;color:var(--gold-2);margin-bottom:20px}
.calc-out{background:rgba(255,255,255,.07);border:1px solid rgba(255,255,255,.13);border-radius:12px;padding:24px;margin-top:24px}
.calc-out .big{font-family:'Fraunces',serif;font-size:2.4rem;color:var(--gold-2);line-height:1;letter-spacing:-.03em}
.calc-out .lbl{font-size:.83rem;color:#a9c4b9;margin-top:8px}
.disc{font-size:.76rem;color:#8fa9a0;margin-top:18px;line-height:1.55}

/* ---------- footer ---------- */
footer{background:var(--ink);color:#9db3aa;padding:64px 0 30px;font-size:.9rem}
footer h2{color:#fff;font-size:1rem;margin-bottom:16px;font-family:'Inter',sans-serif;font-weight:600;letter-spacing:0}
footer a{color:#9db3aa;text-decoration:none}
footer a:hover{color:var(--gold-2)}
.fgrid{display:grid;gap:38px;grid-template-columns:1.6fr 1fr 1fr 1fr;margin-bottom:40px}
@media(max-width:820px){.fgrid{grid-template-columns:1fr 1fr}}
@media(max-width:520px){.fgrid{grid-template-columns:1fr}}
.fgrid ul{list-style:none}
.bbs{display:inline-flex;align-items:center;gap:8px;opacity:.5;transition:opacity .2s;
  text-decoration:none;flex-shrink:0}
.bbs:hover{opacity:1}
.bbs span{font-size:.7rem;letter-spacing:.1em;text-transform:uppercase;color:#7f948b}
.bbs img{height:20px;width:auto;display:block}
@media(max-width:700px){.fbot{flex-direction:column;align-items:flex-start;gap:14px}
  .bbs{margin-top:2px}}
.fgrid li{margin-bottom:9px}
.fbot{border-top:1px solid rgba(255,255,255,.1);padding-top:24px;display:flex;justify-content:space-between;
  gap:16px;flex-wrap:wrap;font-size:.83rem;color:#7a9087}
.soc{display:flex;gap:12px;margin-top:18px}
.soc a{width:36px;height:36px;border-radius:9px;background:rgba(255,255,255,.07);display:grid;place-items:center;transition:.22s}
.soc a:hover{background:var(--accent);transform:translateY(-2px)}

/* ---------- misc ---------- */
.crumb{font-size:.83rem;color:var(--mute);padding-top:22px}
.crumb a{color:var(--accent);text-decoration:none}
.pagehead{padding-top:64px;padding-bottom:10px}
.pagehead h1{font-size:clamp(2.1rem,5vw,3.2rem);margin-bottom:16px;color:var(--ink-2)}
.cta-band{background:linear-gradient(140deg,var(--deep),#0a2519);border-radius:6px;padding:56px 40px;text-align:center;color:#fff}
.cta-band h2{color:#fff;font-size:clamp(1.7rem,3.6vw,2.4rem);margin-bottom:14px}
.cta-band p{color:#b6cdc3;max-width:520px;margin:0 auto 28px}
.tick{color:var(--accent);flex-shrink:0}
@media(prefers-reduced-motion:reduce){
  *{animation:none!important;transition:none!important;scroll-behavior:auto!important}
  .rv{opacity:1;transform:none}
}
@media print{.nav,footer,#summit{display:none}}
"""

# ---------------------------------------------------------------- JS
JS = r"""
// nav — sticky, and it adopts the section behind it.
// The bar sits over a dark hero on some pages and over paper on others, and it
// crosses dark bands mid-page. Rather than picking one colour and living with
// the bad half, it measures which themed section is under the bar and flips.
const nav=document.querySelector('.nav');
if(nav){
  // Sections that render on a dark ground. Read once, then only their offsets
  // are re-measured, so scrolling stays cheap.
  const darkSel='.hero,.dark,.mband';
  let bands=[],navH=nav.offsetHeight,ticking=false;
  const measure=()=>{
    navH=nav.offsetHeight;
    bands=[...document.querySelectorAll(darkSel)].map(el=>{
      const r=el.getBoundingClientRect();
      return [r.top+scrollY, r.bottom+scrollY];
    });
  };
  const apply=()=>{
    ticking=false;
    nav.classList.toggle('scrolled',scrollY>10);
    // Probe just BELOW the bar's bottom edge. Sampling inside the bar's own
    // height misses a section that starts exactly where the bar ends, which is
    // every hero on this site.
    const y=scrollY+navH+4;
    let dark=false;
    for(const [top,bot] of bands){ if(y>=top&&y<bot){dark=true;break} }
    nav.classList.toggle('on-dark',dark);
  };
  const onScroll=()=>{ if(!ticking){ticking=true;requestAnimationFrame(apply)} };
  measure(); apply();
  addEventListener('scroll',onScroll,{passive:true});
  addEventListener('resize',()=>{measure();apply()},{passive:true});
  // The 3D hero and lazy content change section heights after first paint.
  addEventListener('load',()=>{measure();apply()});
}

// reveal + counters + bars
const rm=matchMedia('(prefers-reduced-motion:reduce)').matches;
const io=new IntersectionObserver((es)=>{es.forEach(e=>{if(!e.isIntersecting)return;
  e.target.classList.add('in');
  e.target.querySelectorAll?.('[data-count]').forEach(el=>{
    const t=parseFloat(el.dataset.count),p=el.dataset.pre||'',s=el.dataset.suf||'',d=el.dataset.dec?+el.dataset.dec:0;
    if(rm){el.textContent=p+t.toFixed(d)+s;return}
    let st=null;const dur=1400;
    const tick=(ts)=>{st=st||ts;const k=Math.min((ts-st)/dur,1);const e2=1-Math.pow(1-k,3);
      el.textContent=p+(t*e2).toFixed(d)+s;if(k<1)requestAnimationFrame(tick)};requestAnimationFrame(tick);});
  e.target.querySelectorAll?.('.fill').forEach(f=>{f.style.width=(f.dataset.w||0)+'%'});
  io.unobserve(e.target);})},{threshold:.18});
document.querySelectorAll('.rv').forEach(el=>io.observe(el));

// 3D tilt
if(!rm&&matchMedia('(pointer:fine)').matches){
 document.querySelectorAll('[data-tilt]').forEach(c=>{
  c.addEventListener('mousemove',ev=>{const r=c.getBoundingClientRect();
    const x=(ev.clientX-r.left)/r.width-.5,y=(ev.clientY-r.top)/r.height-.5;
    c.style.transform=`perspective(900px) rotateX(${-y*5}deg) rotateY(${x*5}deg) translateY(-6px)`});
  c.addEventListener('mouseleave',()=>c.style.transform='');});
}

// Hero scene — loaded only after the page is fully loaded AND the browser is
// idle, so it cannot affect LCP, FCP or Total Blocking Time. summit.js decides
// for itself whether the device should run it at all; until then (and forever,
// on devices that decline) the CSS gradient is the hero background.
if(document.getElementById('summit')){
  const boot=()=>{
    const go=()=>import('/assets/summit.js').catch(()=>{});
    'requestIdleCallback' in window ? requestIdleCallback(go,{timeout:2500}) : setTimeout(go,900);
  };
  document.readyState==='complete' ? boot() : addEventListener('load',boot,{once:true});
}

// article filter + search
const chips=document.querySelectorAll('.chip'),cards=document.querySelectorAll('.art'),sb=document.getElementById('asearch');
let cat='all';
const apply=()=>{const q=(sb?.value||'').toLowerCase().trim();let n=0;
 cards.forEach(c=>{const okc=cat==='all'||c.dataset.cat===cat;
  const okq=!q||c.dataset.s.includes(q);const ok=okc&&okq;
  c.style.display=ok?'':'none';if(ok)n++});
 const e=document.getElementById('nores');if(e)e.style.display=n?'none':'block';};
chips.forEach(c=>c.addEventListener('click',()=>{chips.forEach(x=>x.classList.remove('on'));
 c.classList.add('on');cat=c.dataset.f;apply()}));
sb&&sb.addEventListener('input',apply);

// savings calculator
const rev=document.getElementById('rev'),hrs=document.getElementById('hrs');
if(rev&&hrs){
 const fmt=n=>'$'+Math.round(n).toLocaleString();
 const calc=()=>{
  const R=+rev.value,H=+hrs.value;
  document.getElementById('revV').textContent=fmt(R);
  document.getElementById('hrsV').textContent=H+' hrs/month';
  const ownerRate=75;                       // conservative owner opportunity cost
  const timeBack=H*ownerRate*12;            // hours reclaimed, annualized
  const cleanBooks=R*0.012;                 // conservative margin/expense recapture
  const total=timeBack+cleanBooks;
  document.getElementById('outTime').textContent=fmt(timeBack);
  document.getElementById('outBooks').textContent=fmt(cleanBooks);
  document.getElementById('outTotal').textContent=fmt(total);
 };
 rev.addEventListener('input',calc);hrs.addEventListener('input',calc);calc();
}

// contact form (Formspree-ready, graceful fallback to mailto)
const cf=document.getElementById('cform');
if(cf){cf.addEventListener('submit',async ev=>{
  if(cf.querySelector('[name=_gotcha]').value){ev.preventDefault();return}
  const ep=cf.dataset.endpoint||'';
  if(!ep||ep.includes('PASTE_YOUR')){ev.preventDefault();
    const d=new FormData(cf),g=k=>encodeURIComponent(d.get(k)||'');
    location.href=`mailto:${cf.dataset.email}?subject=${encodeURIComponent('Inquiry — '+(d.get('service')||'General'))}`+
      `&body=${g('name')}%0D%0A${g('email')}%0D%0A${g('phone')}%0D%0A%0D%0A${g('message')}`;
    return}
  ev.preventDefault();const st=document.getElementById('fstat');
  st.textContent='Sending…';
  try{const r=await fetch(ep,{method:'POST',body:new FormData(cf),headers:{Accept:'application/json'}});
    if(r.ok){cf.reset();st.textContent='Thank you — your inquiry has been sent. We reply within one business day.';
      st.style.color='var(--accent)'}else{throw 0}}
  catch{st.textContent='Something went wrong. Please email '+cf.dataset.email+' directly.';st.style.color='#b23b3b'}
})}

// year
document.querySelectorAll('.yr').forEach(e=>e.textContent=new Date().getFullYear());
"""

# ---------------------------------------------------------------- shell
LOGO = ('<svg width="34" height="34" viewBox="0 0 34 34" fill="none" aria-hidden="true">'
        '<rect width="34" height="34" rx="9" fill="#0e3326"/>'
        '<path d="M7 24l6.2-10 4 6 3.4-5.4L27 24H7z" fill="#2a8f6d"/>'
        '<path d="M16.6 10.2L21 17l-3.4 1.2-4-6 3-2z" fill="#d4a437"/></svg>')

def shell(*, title, desc, canon, body, active="", extra_head="", jsonld=None,
          depth=0, keywords="", og_type="website"):
    p = "../" * depth
    # The second element of the label tuple is the part that is dropped on
    # narrow screens, so seven destinations still fit on one non-scrolling row.
    nav_items = [("Services", "", "services.html"),
                 ("Areas", "Service ", "service-areas/index.html"),
                 ("About", "", "about.html"), ("Articles", "", "articles/index.html"),
                 ("Resources", "", "resources.html"), ("Contact", "", "contact.html")]
    links = "".join(
        f'<a href="{p}{h}"{" aria-current=\"page\"" if active in (n, pre + n) else ""}>'
        f'{f"<span class=\"nav-long\">{pre}</span>" if pre else ""}{n}</a>'
        for n, pre, h in nav_items)
    ld = f'<script type="application/ld+json">\n{json.dumps(jsonld, indent=2)}\n</script>' if jsonld else ""
    return f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>{title}</title>
<meta name="description" content="{desc}">
{f'<meta name="keywords" content="{keywords}">' if keywords else ''}
<meta name="author" content="{FIRM}">
<meta name="robots" content="index,follow,max-image-preview:large">
<link rel="canonical" href="{canon}">
<meta property="og:type" content="{og_type}">
<meta property="og:site_name" content="{FIRM}">
<meta property="og:title" content="{title}">
<meta property="og:description" content="{desc}">
<meta property="og:url" content="{canon}">
<meta property="og:image" content="{SITE}/assets/og-image.jpg">
<meta name="twitter:card" content="summary_large_image">
<meta name="twitter:title" content="{title}">
<meta name="twitter:description" content="{desc}">
<meta name="twitter:image" content="{SITE}/assets/og-image.jpg">
<meta name="theme-color" content="#0e3326">
<link rel="icon" href="{p}assets/favicon.svg" type="image/svg+xml">
<link rel="preload" href="/assets/fonts/inter-var-latin.woff2" as="font" type="font/woff2" crossorigin>
<link rel="preload" href="/assets/fonts/fraunces-var-latin.woff2" as="font" type="font/woff2" crossorigin>
<script>if("IntersectionObserver" in window)document.documentElement.classList.add("js")</script>
<link rel="stylesheet" href="{p}assets/style.css">
{GA4_SNIPPET}
{ld}
{extra_head}
</head>
<body>
<a href="#main" class="skip">Skip to content</a>
<header class="nav">
  <div class="wrap nav-in">
    <a class="brand" href="{p}index.html">{LOGO}<span><b>NorthPeak</b><span>Financial Partners</span></span></a>
    <nav class="links" aria-label="Main">{links}
      <a href="{p}contact.html" class="btn nav-cta" style="color:#fff">Book a Consultation</a>
    </nav>
    <button class="burger" aria-label="Menu" aria-expanded="false"><span></span><span></span><span></span></button>
  </div>
</header>
<main id="main">
{body}
</main>
<footer>
  <div class="wrap">
    <div class="fgrid">
      <div>
        <a class="brand" href="{p}index.html" style="color:#fff">{LOGO}<span><b style="color:#fff">NorthPeak</b><span>Financial Partners</span></span></a>
        <p style="margin-top:16px;max-width:320px">Accounting, controller, and CFO-level advisory that gives growing businesses real financial clarity.</p>
        <!-- SOCIAL LINKS — currently hidden because no accounts exist yet.
             To enable: delete this comment's opening and closing markers, then
             replace each href="#" with the real profile URL.
             Priority order for an accounting firm: LinkedIn first, then Facebook.
             (See the marketing package: 05-copy/LinkedIn-Copy.md)
        <div class="soc">
          <a href="#" aria-label="LinkedIn"><svg width="17" height="17" viewBox="0 0 24 24" fill="#9db3aa"><path d="M4.98 3.5a2.5 2.5 0 11-.02 5 2.5 2.5 0 01.02-5zM3 8.98h4v12H3v-12zM9.5 8.98h3.8v1.64h.06c.53-1 1.83-2.06 3.76-2.06 4.02 0 4.76 2.65 4.76 6.09v6.33h-4v-5.61c0-1.34-.02-3.06-1.87-3.06-1.87 0-2.15 1.46-2.15 2.96v5.71h-4v-12z"/></svg></a>
          <a href="#" aria-label="Facebook"><svg width="17" height="17" viewBox="0 0 24 24" fill="#9db3aa"><path d="M13.5 22v-8h2.7l.4-3.1h-3.1V8.9c0-.9.25-1.5 1.55-1.5h1.65V4.6c-.29-.04-1.27-.13-2.41-.13-2.39 0-4.02 1.46-4.02 4.13v2.3H7.5V14h2.77v8h3.23z"/></svg></a>
        </div>
        -->
      </div>
      <div><h2>Services</h2><ul>
        <li><a href="{p}services.html#starter">Starter Package</a></li>
        <li><a href="{p}services.html#growth">Growth Package</a></li>
        <li><a href="{p}services.html#cfo">CFO Package</a></li>
        <li><a href="{p}services.html">Compare Plans</a></li></ul></div>
      <div><h2>Learn</h2><ul>
        <li><a href="{p}articles/index.html">All Articles</a></li>
        <li><a href="{p}resources.html">Free Tools</a></li>
        <li><a href="{p}service-areas/index.html">Service Areas</a></li>
        <li><a href="{p}about.html">About Us</a></li>
        <li><a href="{p}contact.html#faq">FAQ</a></li></ul></div>
      <div><h2>Contact</h2><ul>
        <li><a href="mailto:{EMAIL}">{EMAIL}</a></li>
        <li><a href="tel:+18476442288">(847) 644-2288</a></li>
        <li>Wilmette, IL</li>
        <li><a href="{p}contact.html">Request a Consultation</a></li></ul></div>
    </div>
    <div class="fbot">
      <span>&copy; <span class="yr"></span> {FIRM}. All rights reserved.</span>
      <span>Informational content only &mdash; not individualized tax, legal, or investment advice.</span>
      <a class="bbs" href="https://builtbysamski.com" rel="noopener" target="_blank"
         title="Site by BuiltBySam">
        <span>Site by</span>
        <img src="{p}assets/builtbysam-wordmark.png" alt="BuiltBySam"
             width="110" height="20" loading="lazy" decoding="async">
      </a>
    </div>
  </div>
</footer>
<script src="{p}assets/app.js" defer></script>
</body>
</html>"""


_LINK_RE = re.compile(r'\b(?P<attr>href|src)="(?P<url>[^"]+)"')
# Anything already absolute, protocol-relative, a bare fragment, or already
# root-relative is left exactly as it is.
_ABSOLUTE = re.compile(r'^(?:[a-z][a-z0-9+.\-]*:|//|#|/)', re.I)


def canonicalize_links(markup, page_path):
    """Rewrite every relative link into the canonical root-relative URL.

    Every <link rel=canonical> on this site points at an extensionless URL
    (https://northpeakfp.com/services), but the generators historically emitted
    relative links with the extension (services.html). That put all 781 internal
    links on URLs that differ from the canonical they resolve to, which is what
    surfaces in Search Console as "Page with redirect" and splits link signals
    across two URL forms for the same page.

    Doing the rewrite here, at the single point where every file is written,
    means any link any generator emits from now on is canonical by construction
    — there is no second place to remember to update.

    Resolution is relative to the page being written, so an article linking to a
    sibling with "llc-vs-s-corp.html" and the homepage linking to
    "articles/llc-vs-s-corp.html" both correctly produce "/articles/llc-vs-s-corp".
    """
    base = posixpath.dirname(page_path)

    def fix(m):
        url = m.group("url")
        if _ABSOLUTE.match(url):
            return m.group(0)
        path_part, suffix = re.match(r'^([^#?]*)(.*)$', url).groups()
        if not path_part:
            return m.group(0)
        target = posixpath.normpath(posixpath.join(base, path_part))
        if target.endswith(".html"):
            target = target[:-len(".html")]
            if target == "index":
                target = ""
            elif target.endswith("/index"):
                target = target[:-len("/index")]
        return f'{m.group("attr")}="/{target}{suffix}"'

    return _LINK_RE.sub(fix, markup)


def W(path, content):
    if path.endswith(".html"):
        content = canonicalize_links(content, path)
    full = os.path.join(ROOT, path)
    os.makedirs(os.path.dirname(full), exist_ok=True)
    open(full, "w").write(content)


# ============================================================ ASSETS
os.makedirs(f"{ROOT}/assets", exist_ok=True)
W("assets/style.css", CSS)
W("assets/app.js", JS)
W("assets/favicon.svg",
  '<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 34 34"><rect width="34" height="34" rx="9" fill="#0e3326"/>'
  '<path d="M7 24l6.2-10 4 6 3.4-5.4L27 24H7z" fill="#2a8f6d"/>'
  '<path d="M16.6 10.2L21 17l-3.4 1.2-4-6 3-2z" fill="#d4a437"/></svg>')

print("assets written")
