#!/usr/bin/env python3
"""Process the founder headshot + build the branded social share card."""
from PIL import Image, ImageDraw, ImageFont, ImageFilter
import os, pathlib

SRC = "/mnt/user-data/uploads/IMG_3496.jpeg"
AST = os.environ.get("NP_ASSETS") or str(
    pathlib.Path(__file__).resolve().parent.parent / "site" / "assets")
os.makedirs(AST, exist_ok=True)

im = Image.open(SRC).convert("RGB")
W, H = im.size   # 681 x 1181

# ── 1. SQUARE HEADSHOT (LinkedIn / Google Business Profile / schema) ──
# Face centre ≈ x240, head top ≈ y60. Square of 655 from top-left.
side = 655
sq = im.crop((0, 5, side, 5 + side))
sq.resize((800, 800), Image.LANCZOS).save(f"{AST}/chaudhry-ahmad-headshot.jpg",
                                          quality=90, optimize=True, progressive=True)
sq.resize((400, 400), Image.LANCZOS).save(f"{AST}/chaudhry-ahmad-headshot-400.jpg",
                                          quality=88, optimize=True, progressive=True)

# ── 2. PORTRAIT for the About page (4:5, flattering crop) ──
pw, ph = 660, 825
por = im.crop((10, 0, 10 + pw, ph))
por.resize((640, 800), Image.LANCZOS).save(f"{AST}/chaudhry-ahmad-about.jpg",
                                           quality=88, optimize=True, progressive=True)

# ── 3. OG IMAGE — 1200x630 branded share card ──
OW, OH = 1200, 630
DEEP, ACC2, GOLD2 = (14, 51, 38), (42, 143, 109), (212, 164, 55)
card = Image.new("RGB", (OW, OH), DEEP)
d = ImageDraw.Draw(card)

# subtle peak geometry
d.polygon([(0, OH), (330, 300), (500, 400), (690, 250), (1200, OH)], fill=(18, 63, 46))
d.line([(0, OH), (330, 300), (500, 400), (690, 250), (1200, OH)], fill=(120, 90, 20), width=2)
d.rectangle([0, 0, OW, 5], fill=(184, 134, 11))

# photo panel on the right, soft-faded left edge
panel_w = 430
ph_img = im.crop((0, 0, 681, int(681 * OH / panel_w)))
ph_img = ph_img.resize((panel_w, OH), Image.LANCZOS)
mask = Image.new("L", (panel_w, OH), 255)
md = ImageDraw.Draw(mask)
for x in range(150):
    md.line([(x, 0), (x, OH)], fill=int(255 * (x / 150)))
card.paste(ph_img, (OW - panel_w, 0), mask)

def font(sz, bold=True):
    for p in ["/usr/share/fonts/truetype/dejavu/DejaVuSerif-Bold.ttf" if bold
              else "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf",
              "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"]:
        if os.path.exists(p):
            try: return ImageFont.truetype(p, sz)
            except: pass
    return ImageFont.load_default()

# logo mark
lx, ly, ls = 74, 62, 46
d.rounded_rectangle([lx, ly, lx+ls, ly+ls], radius=12, fill=DEEP, outline=(42,143,109), width=2)
u = ls/34
d.polygon([(lx+7*u, ly+ls-10*u), (lx+13.2*u, ly+ls-20*u), (lx+17.2*u, ly+ls-14*u),
           (lx+20.6*u, ly+ls-19.4*u), (lx+27*u, ly+ls-10*u)], fill=ACC2)
d.polygon([(lx+16.6*u, ly+ls-23.8*u), (lx+21*u, ly+ls-17*u),
           (lx+17.6*u, ly+ls-15.8*u), (lx+13.6*u, ly+ls-21.8*u)], fill=GOLD2)

d.text((lx+ls+16, ly+6), "NORTHPEAK", font=font(25), fill=(255,255,255))
d.text((lx+ls+17, ly+34), "F I N A N C I A L   P A R T N E R S", font=font(11, False),
       fill=(159,188,176))

d.text((74, 248), "ACCOUNTING · CONTROLLER · CFO", font=font(15, False), fill=GOLD2)
d.text((74, 292), "Financial Clarity.", font=font(56), fill=(255,255,255))
d.text((74, 362), "Strategic Growth.", font=font(56), fill=GOLD2)
d.text((74, 470), "Chaudhry Ahmad · Founder & Principal", font=font(19, False), fill=(201,217,210))
d.text((74, 512), "northpeakfp.com  ·  (847) 644-2288", font=font(17, False), fill=(159,188,176))

card.save(f"{AST}/og-image.jpg", quality=88, optimize=True, progressive=True)

for f in ["chaudhry-ahmad-headshot.jpg", "chaudhry-ahmad-headshot-400.jpg",
          "chaudhry-ahmad-about.jpg", "og-image.jpg"]:
    p = f"{AST}/{f}"
    print(f"  ✓ {f:38s} {Image.open(p).size}  {os.path.getsize(p)//1024}KB")
