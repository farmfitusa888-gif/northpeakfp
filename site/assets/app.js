
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
