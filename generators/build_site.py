#!/usr/bin/env python3
"""Build the complete NorthPeak Financial Partners website."""
import os, sys, json, shutil, html, pathlib, pathlib
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

# ---------------------------------------------------------------- CSS
CSS = r"""
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
.links{display:flex;align-items:center;gap:28px}
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
.burger{display:none;background:none;border:none;cursor:pointer;padding:8px}
.burger span{display:block;width:22px;height:2px;background:var(--ink);margin:4px 0;border-radius:2px;transition:.25s}
@media(max-width:900px){
  .links{position:fixed;inset:64px 0 auto 0;flex-direction:column;background:var(--paper);
    padding:26px;gap:18px;border-bottom:1px solid var(--rule);transform:translateY(-120%);transition:transform .3s;box-shadow:var(--shadow-lg)}
  .links.open{transform:translateY(0)}
  .burger{display:block}
}

/* ---------- hero w/ video ---------- */
.hero{position:relative;min-height:clamp(560px,88vh,860px);display:flex;align-items:center;
  overflow:hidden;background:var(--deep);isolation:isolate}
.hero video,.hero .fallback{position:absolute;inset:0;width:100%;height:100%;object-fit:cover;z-index:-2}
.hero .fallback{background:
  radial-gradient(1200px 600px at 20% 10%,#1b5741 0%,transparent 60%),
  radial-gradient(900px 500px at 85% 80%,#14402f 0%,transparent 65%),
  linear-gradient(160deg,#0e3326,#071d15)}
.hero::after{content:"";position:absolute;inset:0;z-index:-1;
  background:linear-gradient(105deg,rgba(7,29,21,.93) 0%,rgba(7,29,21,.82) 42%,rgba(7,29,21,.55) 100%)}
#peaks{position:absolute;inset:0;width:100%;height:100%;z-index:-1;opacity:.5}
.hero-in{padding:120px 0 100px;max-width:720px;color:#fff}
.hero h1{font-size:clamp(2.5rem,6vw,4.4rem);color:#fff;margin-bottom:22px}
.hero h1 em{font-style:normal;color:var(--gold-2);display:block}
.hero p{font-size:clamp(1.05rem,2vw,1.24rem);color:#cfe0d8;max-width:590px;margin-bottom:34px}
.hero-cta{display:flex;gap:14px;flex-wrap:wrap;margin-bottom:44px}
.hero .btn.ghost{color:#fff;border-color:rgba(255,255,255,.45)}
.hero .btn.ghost:hover{background:#fff;color:var(--deep);border-color:#fff}
.trust{display:flex;gap:30px;flex-wrap:wrap;padding-top:26px;border-top:1px solid rgba(255,255,255,.16)}
.trust div{color:#a9c4b9;font-size:.85rem;display:flex;align-items:center;gap:8px}
.trust svg{flex-shrink:0}

/* ---------- reveal ---------- */
.rv{opacity:0;transform:translateY(26px);transition:opacity .7s cubic-bezier(.2,.8,.2,1),transform .7s cubic-bezier(.2,.8,.2,1)}
.rv.in{opacity:1;transform:none}

/* ---------- sections ---------- */
section{padding:92px 0}
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
.card{background:var(--card);border:1px solid var(--rule);border-radius:var(--r);padding:30px;
  box-shadow:var(--shadow);transition:transform .3s cubic-bezier(.2,.8,.2,1),box-shadow .3s;
  transform-style:preserve-3d;will-change:transform}
.card:hover{transform:translateY(-6px);box-shadow:var(--shadow-lg)}
.card h3{font-size:1.28rem;margin-bottom:10px;color:var(--ink-2)}
.card p{color:var(--soft);font-size:.97rem}
.icon{width:46px;height:46px;border-radius:11px;display:grid;place-items:center;margin-bottom:18px;
  background:linear-gradient(140deg,var(--accent),var(--deep));box-shadow:0 6px 16px rgba(31,111,84,.26)}

/* pricing 3D tilt */
.tier{background:var(--card);border:1px solid var(--rule);border-radius:18px;padding:34px 30px;
  display:flex;flex-direction:column;position:relative;box-shadow:var(--shadow);
  transition:transform .35s cubic-bezier(.2,.8,.2,1),box-shadow .35s;transform-style:preserve-3d}
.tier:hover{box-shadow:var(--shadow-lg)}
.tier.feat{border:1.5px solid var(--gold);box-shadow:0 2px 6px rgba(10,26,20,.06),0 26px 60px rgba(184,134,11,.16)}
.tag{position:absolute;top:-12px;left:50%;transform:translateX(-50%);background:var(--gold);color:#1a1405;
  font-size:.7rem;font-weight:700;letter-spacing:.12em;text-transform:uppercase;padding:6px 16px;border-radius:20px;white-space:nowrap}
.tier h3{font-size:1.4rem;margin-bottom:6px}
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
.viz{background:var(--card);border:1px solid var(--rule);border-radius:var(--r);padding:28px;box-shadow:var(--shadow)}
.viz h4{font-size:1.03rem;margin-bottom:4px;color:var(--ink-2)}
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
.art:hover{transform:translateY(-5px);box-shadow:var(--shadow-lg);border-color:rgba(31,111,84,.32)}
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
.form{background:var(--card);border:1px solid var(--rule);border-radius:var(--r);padding:34px;box-shadow:var(--shadow)}
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
.calc{background:linear-gradient(150deg,var(--deep),#0a2519);border-radius:18px;padding:36px;color:#fff;box-shadow:var(--shadow-lg)}
.calc h3{color:#fff;font-size:1.4rem;margin-bottom:8px}
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
footer h4{color:#fff;font-size:1rem;margin-bottom:16px;font-family:'Inter',sans-serif;font-weight:600;letter-spacing:0}
footer a{color:#9db3aa;text-decoration:none}
footer a:hover{color:var(--gold-2)}
.fgrid{display:grid;gap:38px;grid-template-columns:1.6fr 1fr 1fr 1fr;margin-bottom:40px}
@media(max-width:820px){.fgrid{grid-template-columns:1fr 1fr}}
@media(max-width:520px){.fgrid{grid-template-columns:1fr}}
.fgrid ul{list-style:none}
.fgrid li{margin-bottom:9px}
.fbot{border-top:1px solid rgba(255,255,255,.1);padding-top:24px;display:flex;justify-content:space-between;
  gap:16px;flex-wrap:wrap;font-size:.83rem;color:#7a9087}
.soc{display:flex;gap:12px;margin-top:18px}
.soc a{width:36px;height:36px;border-radius:9px;background:rgba(255,255,255,.07);display:grid;place-items:center;transition:.22s}
.soc a:hover{background:var(--accent);transform:translateY(-2px)}

/* ---------- misc ---------- */
.crumb{font-size:.83rem;color:var(--mute);padding:22px 0 0}
.crumb a{color:var(--accent);text-decoration:none}
.pagehead{padding:64px 0 10px}
.pagehead h1{font-size:clamp(2.1rem,5vw,3.2rem);margin-bottom:16px;color:var(--ink-2)}
.cta-band{background:linear-gradient(140deg,var(--deep),#0a2519);border-radius:20px;padding:56px 40px;text-align:center;color:#fff;box-shadow:var(--shadow-lg)}
.cta-band h2{color:#fff;font-size:clamp(1.7rem,3.6vw,2.4rem);margin-bottom:14px}
.cta-band p{color:#b6cdc3;max-width:520px;margin:0 auto 28px}
.tick{color:var(--accent);flex-shrink:0}
@media(prefers-reduced-motion:reduce){
  *{animation:none!important;transition:none!important;scroll-behavior:auto!important}
  .rv{opacity:1;transform:none}
}
@media print{.nav,footer,.hero video,#peaks{display:none}}
"""

# ---------------------------------------------------------------- JS
JS = r"""
// nav
const nav=document.querySelector('.nav');
addEventListener('scroll',()=>nav&&nav.classList.toggle('scrolled',scrollY>10),{passive:true});
const bg=document.querySelector('.burger'),lk=document.querySelector('.links');
if(bg&&lk){bg.addEventListener('click',()=>{const o=lk.classList.toggle('open');bg.setAttribute('aria-expanded',o)});
  lk.querySelectorAll('a').forEach(a=>a.addEventListener('click',()=>lk.classList.remove('open')));}

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

// animated peak topography (canvas)
const cv=document.getElementById('peaks');
if(cv&&!rm){
 const cx=cv.getContext('2d');let w,h,t=0;
 const rs=()=>{w=cv.width=cv.offsetWidth*devicePixelRatio;h=cv.height=cv.offsetHeight*devicePixelRatio};
 rs();addEventListener('resize',rs,{passive:true});
 const layer=(off,amp,al,sp)=>{cx.beginPath();cx.moveTo(0,h);
  for(let x=0;x<=w;x+=8){
    const y=h*off + Math.sin(x*0.0016+t*sp)*amp + Math.sin(x*0.0041+t*sp*1.7)*amp*0.45;
    cx.lineTo(x,y)}
  cx.lineTo(w,h);cx.closePath();
  const g=cx.createLinearGradient(0,h*off-amp,0,h);
  g.addColorStop(0,`rgba(42,143,109,${al})`);g.addColorStop(1,`rgba(14,51,38,0)`);
  cx.fillStyle=g;cx.fill();
  cx.strokeStyle=`rgba(184,134,11,${al*0.85})`;cx.lineWidth=1.1*devicePixelRatio;cx.stroke()};
 const loop=()=>{cx.clearRect(0,0,w,h);t+=.0055;
  layer(.62,26*devicePixelRatio,.16,1);layer(.72,20*devicePixelRatio,.12,1.35);
  layer(.82,15*devicePixelRatio,.09,1.7);requestAnimationFrame(loop)};loop();
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
    nav_items = [("Home", "index.html"), ("Services", "services.html"),
                 ("About", "about.html"), ("Articles", "articles/index.html"),
                 ("Resources", "resources.html"), ("Contact", "contact.html")]
    links = "".join(
        f'<a href="{p}{h}"{" aria-current=\"page\"" if active==n else ""}>{n}</a>'
        for n, h in nav_items)
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
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Fraunces:opsz,wght@9..144,400;9..144,500;9..144,600;9..144,700&family=Inter:wght@400;500;600;700&display=swap" rel="stylesheet">
<link rel="stylesheet" href="{p}assets/style.css">
{ld}
{extra_head}
</head>
<body>
<a href="#main" class="skip">Skip to content</a>
<header class="nav">
  <div class="wrap nav-in">
    <a class="brand" href="{p}index.html">{LOGO}<span><b>NorthPeak</b><span>Financial Partners</span></span></a>
    <nav class="links" aria-label="Main">{links}
      <a href="{p}contact.html" class="btn" style="color:#fff">Book a Consultation</a>
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
        --></div>
      </div>
      <div><h4>Services</h4><ul>
        <li><a href="{p}services.html#starter">Starter Package</a></li>
        <li><a href="{p}services.html#growth">Growth Package</a></li>
        <li><a href="{p}services.html#cfo">CFO Package</a></li>
        <li><a href="{p}services.html">Compare Plans</a></li></ul></div>
      <div><h4>Learn</h4><ul>
        <li><a href="{p}articles/index.html">All Articles</a></li>
        <li><a href="{p}resources.html">Free Tools</a></li>
        <li><a href="{p}about.html">About Us</a></li>
        <li><a href="{p}contact.html#faq">FAQ</a></li></ul></div>
      <div><h4>Contact</h4><ul>
        <li><a href="mailto:{EMAIL}">{EMAIL}</a></li>
        <li><a href="tel:+18476442288">(847) 644-2288</a></li>
        <li>Wilmette, IL</li>
        <li><a href="{p}contact.html">Request a Consultation</a></li></ul></div>
    </div>
    <div class="fbot">
      <span>&copy; <span class="yr"></span> {FIRM}. All rights reserved.</span>
      <span>Informational content only &mdash; not individualized tax, legal, or investment advice.</span>
    </div>
  </div>
</footer>
<script src="{p}assets/app.js" defer></script>
</body>
</html>"""


def W(path, content):
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
