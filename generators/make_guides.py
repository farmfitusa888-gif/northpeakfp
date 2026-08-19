import pathlib
#!/usr/bin/env python3
from reportlab.lib.pagesizes import letter
from reportlab.lib.units import inch
from reportlab.lib import colors
from reportlab.platypus import (SimpleDocTemplate, Paragraph, Spacer, PageBreak,
                                ListFlowable, ListItem, Table, TableStyle, HRFlowable)
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.enums import TA_LEFT

INK=colors.HexColor("#0a1a14"); ACCENT=colors.HexColor("#1f6f54")
DEEP=colors.HexColor("#0e3326"); GOLD=colors.HexColor("#b8860b")
ALT=colors.HexColor("#f2efe6"); SOFT=colors.HexColor("#4a5f56")
RULE=colors.HexColor("#e0dacb"); RED=colors.HexColor("#9c3535")

S=getSampleStyleSheet()
H1=ParagraphStyle("H1",parent=S["Title"],textColor=INK,fontName="Helvetica-Bold",fontSize=22,leading=26,spaceAfter=6,alignment=TA_LEFT)
SUB=ParagraphStyle("SUB",parent=S["Normal"],textColor=SOFT,fontSize=11,leading=15.5,spaceAfter=15)
H2=ParagraphStyle("H2",parent=S["Heading1"],textColor=DEEP,fontName="Helvetica-Bold",fontSize=14.5,leading=18,spaceBefore=16,spaceAfter=7)
H3=ParagraphStyle("H3",parent=S["Heading2"],textColor=ACCENT,fontName="Helvetica-Bold",fontSize=11.5,leading=15,spaceBefore=10,spaceAfter=4)
B=ParagraphStyle("B",parent=S["Normal"],textColor=INK,fontSize=10,leading=15,spaceAfter=7)
BS=ParagraphStyle("BS",parent=B,textColor=SOFT)
LI=ParagraphStyle("LI",parent=B,spaceAfter=4)
CODE=ParagraphStyle("CODE",parent=S["Code"],textColor=DEEP,fontSize=8.6,leading=12,backColor=ALT,borderPadding=6,spaceAfter=7)
NOTE=ParagraphStyle("NOTE",parent=B,textColor=DEEP,fontSize=9.6,leading=14,backColor=ALT,borderPadding=9,spaceAfter=9)
WARN=ParagraphStyle("WARN",parent=B,textColor=RED,fontSize=9.6,leading=14,backColor=colors.HexColor("#faf0ef"),borderPadding=9,spaceAfter=9)

def mk(story,path,title):
    SimpleDocTemplate(path,pagesize=letter,leftMargin=.8*inch,rightMargin=.8*inch,
        topMargin=.75*inch,bottomMargin=.65*inch,title=title).build(story)
    print("built",path)

def rule(st,c=GOLD): st.append(Spacer(1,3)); st.append(HRFlowable(width="100%",thickness=1.2,color=c,spaceAfter=9))
def nums(st,items): st.append(ListFlowable([ListItem(Paragraph(x,LI),leftIndent=13) for x in items],bulletType="1",leftIndent=5))
def bul(st,items): st.append(ListFlowable([ListItem(Paragraph(x,LI),leftIndent=13,value="•") for x in items],bulletType="bullet",start="•",leftIndent=5))
def tbl(st,rows,widths):
    d=[[Paragraph(f"<b>{c}</b>",B) for c in rows[0]]]+[[Paragraph(c,B) for c in r] for r in rows[1:]]
    t=Table(d,colWidths=widths)
    t.setStyle(TableStyle([("BACKGROUND",(0,0),(-1,0),DEEP),("TEXTCOLOR",(0,0),(-1,0),colors.white),
      ("GRID",(0,0),(-1,-1),.5,RULE),("VALIGN",(0,0),(-1,-1),"TOP"),
      ("ROWBACKGROUNDS",(0,1),(-1,-1),[colors.white,ALT]),
      ("TOPPADDING",(0,0),(-1,-1),5),("BOTTOMPADDING",(0,0),(-1,-1),5),("LEFTPADDING",(0,0),(-1,-1),7)]))
    st.append(t); st.append(Spacer(1,9))

# ══════════════════════════════════════════ GUIDE 1: SETUP & LAUNCH
g=[]
g.append(Paragraph("NorthPeak Website — Setup &amp; Launch Guide",H1))
g.append(Paragraph("Everything needed to connect the booking calendar and contact form, publish the new "
  "site on northpeakfp.com, and retire the Squarespace site safely.",SUB))
rule(g)

g.append(Paragraph("Before You Start: What Must Be Filled In",H2))
g.append(Paragraph("The site is complete and ready to deploy. One item still needs you (the form "
  "endpoint), and one is strongly recommended.",B))
tbl(g,[["Item","Where it appears","Status"],
 ["Phone (847) 644-2288","Footer, Contact page, schema","Done"],
 ["Wilmette, IL","Footer, Contact page, schema","Done"],
 ["Starter price $149/month","Services page, FAQ, schema","Done"],
 ["PASTE_YOUR_FORMSPREE_ENDPOINT","contact.html","<b>Needs you</b> &mdash; Part 1 of this guide"],
 ["Founder name + bio","about.html","<b>Recommended</b> &mdash; see note below"]],[1.75*inch,2.0*inch,2.45*inch])
g.append(Paragraph("Also strongly recommended: add the founder's real name and a short bio to "
  "<b>about.html</b>. Google's quality guidelines treat financial content as 'Your Money or Your Life' and "
  "weigh author identity heavily. An anonymous financial site ranks worse than a named one.",NOTE))

g.append(Paragraph("Part 1 — Contact Form Delivery (required)",H2))
g.append(Paragraph("There is no booking calendar on the site by design. Enquiries come in two ways: the "
  "contact form, and the phone number (847) 644-2288 shown in the footer of every page and on the Contact "
  "page. The form is the only piece that needs connecting.",NOTE))
g.append(Paragraph("A plain HTML form can't send email by itself; it needs a delivery service. The form is "
  "already built and validated — it just needs an endpoint. <b>Formspree</b> has a free tier and takes "
  "about three minutes.",B))
nums(g,["Go to formspree.io and create a free account using <b>info@northpeakfp.com</b>.",
 "Click <b>New Form</b>, name it 'NorthPeak Website Inquiries'.",
 "Set the notification email to info@northpeakfp.com.",
 "Copy the form endpoint it gives you (it looks like https://formspree.io/f/xxxxxxx).",
 "Open <b>contact.html</b>, find <b>PASTE_YOUR_FORMSPREE_ENDPOINT_HERE</b> — it appears twice, in "
 "<b>data-endpoint</b> and <b>action</b>. Replace both with the endpoint.",
 "Save, then submit a test message and confirm it arrives."])
g.append(Paragraph("<b>Built-in safety net:</b> if the endpoint is left unset, the form automatically falls "
  "back to opening the visitor's email app addressed to info@northpeakfp.com. Nothing silently disappears. "
  "A hidden anti-spam honeypot field is already included.",NOTE))
g.append(Paragraph("Free alternatives: <b>Web3Forms</b>, <b>FormSubmit</b>, or <b>Netlify Forms</b> (free "
  "and automatic if you host on Netlify — see Part 3).",B))

g.append(PageBreak())
g.append(Paragraph("Part 2 — Publishing the Site",H2))
g.append(Paragraph("The site is plain HTML/CSS/JS, so it runs anywhere. Two recommended options:",B))
g.append(Paragraph("Option A — Netlify (recommended: free, fastest, includes forms)",H3))
nums(g,["Create a free account at netlify.com.",
 "Choose <b>Add new site &rarr; Deploy manually</b>.",
 "Drag the entire <b>northpeak-site</b> folder onto the upload area. It deploys in seconds and gives you "
 "a temporary address like <b>random-name.netlify.app</b>.",
 "Test everything on that temporary address <i>before</i> pointing the real domain at it.",
 "When satisfied, go to <b>Domain settings &rarr; Add custom domain</b> and enter <b>northpeakfp.com</b>.",
 "Netlify will show the DNS records to set. Do NOT change DNS yet — finish reading Part 3 first."])
g.append(Paragraph("Option B — Cloudflare Pages / GitHub Pages",H3))
g.append(Paragraph("Both are free and work identically for a static site. Cloudflare Pages accepts a direct "
  "folder upload; GitHub Pages requires putting the files in a repository first. Netlify is the simplest "
  "for someone who doesn't want to touch Git.",B))
g.append(Paragraph("Free HTTPS is automatic on all three. Don't launch without it — browsers flag sites "
  "without HTTPS as 'Not secure', which is fatal for a financial services firm.",NOTE))

g.append(Paragraph("Part 3 — Switching Off Squarespace (do this in order)",H2))
g.append(Paragraph("The order matters. Cancelling Squarespace before the DNS move completes will take the "
  "site offline and can cost you the domain if it's registered through Squarespace.",WARN))
g.append(Paragraph("Step 1 — Find out where the domain is registered",H3))
nums(g,["Log into Squarespace &rarr; <b>Settings &rarr; Domains</b>.",
 "If northpeakfp.com is listed as a <b>Squarespace-managed domain</b>, it was bought through them and must "
 "be transferred out or its DNS repointed. If it says <b>third-party domain</b>, it lives at another "
 "registrar (GoDaddy, Namecheap, etc.) and this is much easier."])
g.append(Paragraph("Step 2 — Point DNS at the new host",H3))
nums(g,["In the domain's DNS settings, remove the existing A / CNAME records pointing to Squarespace.",
 "Add the records your new host gave you (Netlify/Cloudflare shows these).",
 "Save. DNS changes typically take 15 minutes to a few hours; allow up to 48 hours.",
 "Confirm the new site loads at northpeakfp.com over <b>https://</b> and that the padlock shows."])
g.append(Paragraph("Step 3 — Preserve the old links",H3))
g.append(Paragraph("The current site has pages at <b>/about</b>, <b>/new-page</b>, <b>/new-page-1</b>, and "
  "<b>/submit</b>. Anything already indexed by Google will 404 unless redirected. On Netlify, create a file "
  "named <b>_redirects</b> (no extension) in the site folder containing:",B))
g.append(Paragraph("/new-page&nbsp;&nbsp;&nbsp;&nbsp;/about.html&nbsp;&nbsp;301<br/>"
 "/new-page-1&nbsp;&nbsp;/articles/&nbsp;&nbsp;301<br/>"
 "/submit&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;/contact.html&nbsp;&nbsp;301<br/>"
 "/about&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;/about.html&nbsp;&nbsp;301<br/>"
 "/cart&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;/services.html&nbsp;&nbsp;301",CODE))
g.append(Paragraph("Step 4 — Only now, cancel Squarespace",H3))
nums(g,["Confirm the new site has been live and working for at least <b>7 days</b>.",
 "Export anything you still need from Squarespace (any form submissions, order history, images).",
 "If the domain is Squarespace-managed, <b>transfer the domain out first</b> to a registrar like "
 "Cloudflare or Namecheap. This can take 5&ndash;7 days and cannot be rushed.",
 "Once the domain is safely elsewhere and the site is live, cancel the Squarespace subscription.",
 "Keep a downloaded backup of the old site content for your records."])
g.append(Paragraph("Do not skip the 7-day wait. If anything is wrong with DNS, keeping Squarespace active "
  "means you can revert instantly. Once cancelled, that safety net is gone.",WARN))

g.append(PageBreak())
g.append(Paragraph("Part 4 — Background Video for the Hero",H2))
g.append(Paragraph("The homepage is built to play a looping video behind the headline. It already works "
  "without one (an animated gradient and a moving topographic 'peaks' animation show instead), so this is "
  "an upgrade, not a requirement.",B))
g.append(Paragraph("Where to get royalty-free footage",H3))
tbl(g,[["Source","Cost","Notes"],
 ["Pexels Videos","Free","No attribution required, commercial use OK. Best overall selection."],
 ["Coverr","Free","Purpose-built for website hero backgrounds; short seamless loops."],
 ["Mixkit","Free","Curated, high quality, free for commercial use."],
 ["Videvo","Free / paid","Check each clip's licence — some require attribution."],
 ["Artgrid / Storyblocks","Paid sub","Highest quality if he wants something distinctive."]],[1.5*inch,.95*inch,3.75*inch])
g.append(Paragraph("What to search for (fits the NorthPeak brand)",H3))
bul(g,["<b>Aerial mountain ridgelines / drone over peaks above clouds</b> — directly reinforces the "
 "'NorthPeak' name and the climb-to-the-summit metaphor. This is the strongest thematic match.",
 "<b>Slow drone push over misty forest or alpine terrain at sunrise</b> — calm, premium, optimistic.",
 "<b>Abstract flowing dark-teal gradients or soft light rays</b> — safest option; never competes with the text.",
 "<b>Time-lapse city skyline at dusk from above</b> — classic professional-services look, though less distinctive.",
 "<b>Slow-moving data visualization / particle network in dark tones</b> — leans into the "
 "'data-driven' positioning."])
g.append(Paragraph("Avoid: stock footage of people shaking hands, coins stacking, or literal calculators. "
  "They read as generic and slightly dated, and they undercut a premium positioning.",B))
g.append(Paragraph("Technical requirements (important for speed)",H3))
tbl(g,[["Setting","Target","Why"],
 ["Format","MP4 (H.264)","Universal browser support"],
 ["Resolution","1920x1080","4K is wasted as a background and triples file size"],
 ["Length","8&ndash;15 seconds, seamless loop","Short loops keep the file small"],
 ["File size","Under 3 MB (ideally ~2 MB)","Video is the #1 cause of slow hero sections"],
 ["Audio","Removed entirely","It's muted anyway; the audio track is dead weight"],
 ["Motion","Slow and subtle","Fast motion makes headline text hard to read"]],[1.3*inch,1.9*inch,3.0*inch])
g.append(Paragraph("Installing it",H3))
nums(g,["Compress the clip first — <b>HandBrake</b> (free) or an online tool like FreeConvert. Target "
 "2&ndash;3 MB and strip audio.",
 "Name the file <b>hero.mp4</b> and put it in the <b>assets</b> folder.",
 "Export one still frame as <b>hero-poster.jpg</b> (also in assets) — it shows instantly while the video "
 "loads, so the hero never appears blank.",
 "That's it. The HTML already references both files."])
g.append(Paragraph("The video is already set to muted, autoplay, loop, and playsinline, and it is hidden "
  "automatically for visitors who have 'reduce motion' enabled in their operating system. A dark overlay "
  "sits between the video and the text so the headline stays readable on any footage.",NOTE))

mk(g,str(pathlib.Path(__file__).resolve().parent.parent / "docs" / "guides" / "01-Setup-and-Launch-Guide.pdf"),"NorthPeak Setup & Launch Guide")

# ══════════════════════════════════════════ GUIDE 2: SEO PLAYBOOK
s=[]
s.append(Paragraph("NorthPeak — SEO Playbook",H1))
s.append(Paragraph("What's already built into the site, what to do in the first week, and the ongoing "
  "routine that compounds over time.",SUB))
rule(s)

s.append(Paragraph("Already Done For You",H2))
s.append(Paragraph("These were built into every page — no action needed:",B))
bul(s,["Unique, length-optimized title tag and meta description on all 32 pages",
 "Canonical URLs on every page (prevents duplicate-content penalties)",
 "Open Graph and Twitter Card tags so shared links render properly",
 "JSON-LD structured data: <b>AccountingService</b> on the homepage, <b>Article</b> schema on all 25 "
 "guides, <b>FAQPage</b> on Contact, <b>Service</b> + offer catalog on Services, <b>CollectionPage</b> on the hub",
 "One H1 per page with a correct heading hierarchy beneath it",
 "XML sitemap covering all 31 public URLs, plus robots.txt pointing to it",
 "Internal linking: every article links to three related guides and back to the hub and contact page",
 "Outbound citations to IRS.gov and SBA.gov (authority signals)",
 "Mobile-responsive, accessible (skip links, focus states, reduced-motion support), and fast — "
 "no frameworks, no build step, ~20 KB of CSS",
 "A custom 404 page marked <b>noindex</b>"])

s.append(Paragraph("Week One Checklist",H2))
s.append(Paragraph("1. Google Search Console",H3))
nums(s,["Go to search.google.com/search-console and add <b>northpeakfp.com</b> as a Domain property.",
 "Verify via DNS TXT record (your host or registrar has a place to paste it).",
 "Under <b>Sitemaps</b>, submit: <b>sitemap.xml</b>",
 "Use <b>URL Inspection</b> on the homepage and click <b>Request Indexing</b> to speed up first crawl."])
s.append(Paragraph("2. Google Business Profile — highest ROI item on this list",H3))
s.append(Paragraph("For a local accounting practice this typically drives more qualified enquiries than "
  "everything else combined. You now have everything needed: <b>(847) 644-2288</b> and <b>Wilmette, IL</b>. "
  "Use these details identically everywhere online — Google matches on exact consistency.",B))
nums(s,["Create the profile at google.com/business.",
 "Category: <b>Accountant</b> (add <b>Bookkeeping service</b> and <b>Tax preparation service</b> as secondary).",
 "If he works from home, choose <b>service-area business</b> — the address stays private but he still ranks locally.",
 "Add hours, services, and the website link. Post the articles to the profile's Updates feed.",
 "Ask the first 5 clients for Google reviews. Review count and recency are among the strongest local ranking factors."])
s.append(Paragraph("3. Bing Webmaster Tools",H3))
s.append(Paragraph("Takes two minutes and imports directly from Search Console. Bing powers a meaningful "
  "slice of search and now feeds some AI assistants.",B))
s.append(Paragraph("4. Analytics",H3))
s.append(Paragraph("Add Google Analytics 4 (or a lighter, privacy-friendly option like Plausible or "
  "Fathom). Paste the tracking snippet just before the closing &lt;/body&gt; tag in each HTML file, or "
  "use your host's script-injection feature to add it site-wide at once.",B))

s.append(PageBreak())
s.append(Paragraph("The Ongoing Routine",H2))
tbl(s,[["Frequency","Action","Why it matters"],
 ["Weekly","Publish or refresh one article","Consistent publishing is the single biggest ranking driver for a new site"],
 ["Weekly","Post an article link to Google Business Profile","Activity signal + a free traffic channel"],
 ["Monthly","Check Search Console for queries you rank for","Tells you what to write next — real demand, not guesses"],
 ["Monthly","Fix any crawl errors or broken links reported","Small issues compound if ignored"],
 ["Quarterly","Update the oldest articles with current figures","Freshness signal; tax numbers change annually"],
 ["Ongoing","Request a review after every good client outcome","Reviews drive local rankings and conversion together"]],[1.0*inch,2.2*inch,3.0*inch])

s.append(Paragraph("Backlinks — the honest version",H2))
s.append(Paragraph("A backlink is another website linking to yours. Google treats them as votes of "
  "confidence, so they genuinely move rankings. Two things matter:",B))
s.append(Paragraph("<b>Never buy them.</b> Link-selling services ('500 backlinks for $20') can get a site "
  "penalized or removed from Google entirely. For a financial services firm, that risk is not worth taking.",WARN))
s.append(Paragraph("Legitimate ways to earn them, roughly in order of effort:",B))
bul(s,["Local chamber of commerce membership (usually includes a member directory link)",
 "Professional association directories and any state or trade body listings",
 "Reciprocal referral partners — a business attorney, a financial advisor, an insurance broker. "
 "Each of you links to the other's site as a trusted referral.",
 "Local business directories: Yelp, Bing Places, Apple Business Connect, industry-specific listings",
 "Guest articles for a local business publication or a partner's blog",
 "Being genuinely useful — the 25 guides exist partly so other sites have something worth linking to"])

s.append(Paragraph("Getting Found by AI Assistants",H2))
s.append(Paragraph("A growing share of people now ask ChatGPT, Claude, or Perplexity for recommendations "
  "instead of searching. The same structured data that helps Google helps here — it's already in place. "
  "Three things additionally help:",B))
bul(s,["Clear, direct answers near the top of each article (the guides are already written this way)",
 "FAQ schema — already on the Contact page; consider adding FAQs to individual service pages",
 "Consistent business details (name, address, phone) everywhere they appear online. Inconsistency "
 "confuses both local search and AI retrieval."])

s.append(Paragraph("What to Measure",H2))
s.append(Paragraph("Ignore vanity metrics. For a firm this size, four numbers matter:",B))
tbl(s,[["Metric","Where","Target trend"],
 ["Consultation bookings","Calendar / form inbox","The only number that pays the bills"],
 ["Impressions in Search Console","Search Console","Should climb steadily from month 2 onward"],
 ["Google Business Profile calls/clicks","Business Profile dashboard","Usually the first channel to convert"],
 ["Which articles get traffic","Search Console &rarr; Pages","Tells you what to write more of"]],[1.6*inch,1.9*inch,2.7*inch])
s.append(Paragraph("Realistic expectation: a brand-new site typically sees little organic traffic for the "
  "first 8&ndash;12 weeks, then compounds. The Google Business Profile will produce results much sooner. "
  "Don't judge the SEO work before the three-month mark.",NOTE))

mk(s,str(pathlib.Path(__file__).resolve().parent.parent / "docs" / "guides" / "02-SEO-Playbook.pdf"),"NorthPeak SEO Playbook")
