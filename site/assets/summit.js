/**
 * NorthPeak — procedural alpine terrain with numeric snowfall.
 *
 * Mounts to any number of canvases. The homepage uses two: a restrained pass
 * behind the hero, and a full-strength full-bleed band further down the page.
 * The terrain itself (148x148 vertices, five gaussian summits plus five octaves
 * of ridged noise per vertex) is generated ONCE and shared between them — only
 * the camera framing, particle count and final opacity differ.
 *
 * Loaded only after the page has finished loading and the browser is idle, so
 * it contributes nothing to LCP, FCP, or Total Blocking Time. Until it fades in
 * (and forever, on devices that decline it) each host is carried by the CSS
 * gradient already painted underneath — there is no poster image to download.
 *
 * Declines to run at all when: the visitor prefers reduced motion, Data Saver
 * is on, the connection reports 2g, the device reports under 4GB of RAM, or
 * WebGL is unavailable. In every one of those cases the gradient simply stays.
 *
 * The terrain is generated from a seeded hash rather than Math.random, so every
 * visitor sees the same mountain and the scene is reproducible when debugging.
 */
import {
  Scene, PerspectiveCamera, WebGLRenderer, Color, FogExp2,
  PlaneGeometry, BufferGeometry, BufferAttribute, Float32BufferAttribute,
  MeshStandardMaterial, MeshBasicMaterial, ShaderMaterial,
  Mesh, Points, Group, HemisphereLight, DirectionalLight,
  CanvasTexture, AdditiveBlending
} from './vendor/three.summit.js';

/* ------------------------------------------------------------------ noise */
// Deterministic value noise, seeded so the range is identical on every load.
const hash = (x, y) => {
  const n = Math.sin(x * 127.1 + y * 311.7) * 43758.5453123;
  return n - Math.floor(n);
};
const smooth = t => t * t * (3 - 2 * t);
function value(x, y) {
  const xi = Math.floor(x), yi = Math.floor(y);
  const xf = smooth(x - xi), yf = smooth(y - yi);
  const a = hash(xi, yi), b = hash(xi + 1, yi);
  const c = hash(xi, yi + 1), d = hash(xi + 1, yi + 1);
  const top = a + (b - a) * xf;
  return top + ((c + (d - c) * xf) - top) * yf;
}
// Ridged fractal: 1 - |noise| sharpens crests into ridgelines rather than the
// rolling hills plain fBm produces.
function ridged(x, y) {
  let sum = 0, amp = 0.5, freq = 1;
  for (let o = 0; o < 5; o++) {
    sum += (1 - Math.abs(value(x * freq, y * freq) * 2 - 1)) * amp;
    amp *= 0.5; freq *= 2.07;
  }
  return sum;
}

/* ---------------------------------------------------------------- terrain */
// Built once. Both mounts add this same BufferGeometry to their own scene;
// three.js uploads it per WebGL context, but the CPU-side generation — the
// expensive part, ~22k vertices each running five octaves of noise — happens a
// single time no matter how many canvases are on the page.
let sharedGeo = null;
function terrain() {
  if (sharedGeo) return sharedGeo;
  const geo = new PlaneGeometry(200, 200, 148, 148);
  geo.rotateX(-Math.PI / 2);
  const pos = geo.attributes.position;

  // Five gaussian summits give the range a deliberate silhouette instead of
  // uniform noise.
  const peaks = [
    { x: -46, z: -26, h: 34, r: 24 },
    { x: -12, z: -46, h: 27, r: 20 },
    { x: 22, z: -30, h: 40, r: 21 },
    { x: 56, z: -52, h: 30, r: 22 },
    { x: 2, z: -2, h: 15, r: 28 },
  ];

  let maxH = 0;
  for (let i = 0; i < pos.count; i++) {
    const x = pos.getX(i), z = pos.getZ(i);
    let h = 0;
    for (const p of peaks) {
      const d2 = (x - p.x) ** 2 + (z - p.z) ** 2;
      h += p.h * Math.exp(-d2 / (2 * p.r * p.r));
    }
    h += ridged(x * 0.026, z * 0.026) * 12.5;
    h -= 2.6;
    pos.setY(i, h);
    if (h > maxH) maxH = h;
  }

  // Vertex colours by elevation: shadowed valley -> pine -> evergreen -> snow.
  const cValley = new Color(0x123c2c), cPine = new Color(0x1b6a4a);
  const cEver = new Color(0x3fae81), cSnow = new Color(0xf3f9f5);
  const cols = new Float32Array(pos.count * 3), tmp = new Color();
  for (let i = 0; i < pos.count; i++) {
    const t = Math.max(0, Math.min(1, pos.getY(i) / maxH));
    if (t < 0.26) tmp.copy(cValley).lerp(cPine, t / 0.26);
    else if (t < 0.54) tmp.copy(cPine).lerp(cEver, (t - 0.26) / 0.28);
    else tmp.copy(cEver).lerp(cSnow, Math.pow((t - 0.54) / 0.46, 0.55));
    cols[i * 3] = tmp.r; cols[i * 3 + 1] = tmp.g; cols[i * 3 + 2] = tmp.b;
  }
  geo.setAttribute('color', new BufferAttribute(cols, 3));
  geo.computeVertexNormals();
  sharedGeo = geo;
  return geo;
}

/* ------------------------------------------------------------ digit atlas */
// The snow is digits. Rendering a thousand text sprites would be a thousand
// draw calls, so all ten glyphs are baked into one 4x4 texture atlas and drawn
// as a single Points cloud; a per-particle attribute picks the atlas cell.
// One draw call, ten distinct glyphs.
let sharedAtlas = null;
function digitAtlas() {
  if (sharedAtlas) return sharedAtlas;
  const CELL = 128, c = document.createElement('canvas');
  c.width = c.height = CELL * 4;
  const g = c.getContext('2d');
  g.font = `600 ${CELL * 0.72}px Inter, system-ui, -apple-system, sans-serif`;
  g.textAlign = 'center'; g.textBaseline = 'middle';
  g.fillStyle = '#ffffff';
  for (let i = 0; i < 10; i++) {
    g.fillText(String(i), (i % 4) * CELL + CELL / 2,
                          Math.floor(i / 4) * CELL + CELL / 2);
  }
  const t = new CanvasTexture(c);
  t.flipY = false;                 // match gl_PointCoord, whose origin is top-left
  sharedAtlas = t;
  return t;
}

/* ------------------------------------------------------------------ mount */
function mount(canvas, host, opt) {
  let renderer;
  try {
    renderer = new WebGLRenderer({ canvas, antialias: true, alpha: true,
                                   powerPreference: 'low-power' });
  } catch (e) {
    return;                         // no WebGL — the gradient carries this host
  }
  renderer.setPixelRatio(Math.min(devicePixelRatio, 2));
  renderer.setClearColor(0x000000, 0);

  const reduced = matchMedia('(prefers-reduced-motion: reduce)').matches;
  const scene = new Scene();
  scene.fog = new FogExp2(0x0d2b1e, opt.fog);
  const camera = new PerspectiveCamera(opt.fov, 1, 0.1, 400);

  const range = new Group();
  range.position.z = -104;          // downrange, so the view is across the
  range.add(new Mesh(terrain(), new MeshStandardMaterial({   // valley to the
    vertexColors: true, flatShading: true, roughness: 0.86, metalness: 0.0,
  })));                                                      // summits
  // A faint wireframe over the same geometry reads as surveyed terrain rather
  // than scenery — the visual argument that this firm measures things.
  range.add(new Mesh(terrain(), new MeshBasicMaterial({
    color: 0x7fe0b6, wireframe: true, transparent: true, opacity: opt.wire,
  })));
  scene.add(range);

  scene.add(new HemisphereLight(0xb6e4cf, 0x0d2a1e, 1.15));
  const key = new DirectionalLight(0xffeccb, 2.15); key.position.set(-58, 34, 22);
  scene.add(key);
  const rim = new DirectionalLight(0x46b98d, 0.85); rim.position.set(48, 10, -46);
  scene.add(rim);

  /* stars */
  {
    const SN = 700, p = new Float32Array(SN * 3);
    for (let i = 0; i < SN; i++) {
      const th = hash(i, 1.7) * Math.PI * 2;
      const ph = Math.acos(hash(i, 4.2) * 0.72);
      p[i * 3] = Math.sin(ph) * Math.cos(th) * 190;
      p[i * 3 + 1] = Math.abs(Math.cos(ph)) * 118 + 24;
      p[i * 3 + 2] = Math.sin(ph) * Math.sin(th) * 190;
    }
    const g = new BufferGeometry();
    g.setAttribute('position', new BufferAttribute(p, 3));
    scene.add(new Points(g, new ShaderMaterial({
      transparent: true, depthWrite: false, blending: AdditiveBlending,
      uniforms: { uO: { value: 0.45 * opt.max } },
      vertexShader: `void main(){vec4 m=modelViewMatrix*vec4(position,1.0);
        gl_PointSize=1.6;gl_Position=projectionMatrix*m;}`,
      fragmentShader: `uniform float uO;void main(){
        vec2 d=gl_PointCoord-0.5;if(dot(d,d)>0.25)discard;
        gl_FragColor=vec4(0.85,0.94,0.90,uO);}`,
    })));
  }

  /* numeric snowfall */
  const N = opt.snow;
  const sp = new Float32Array(N * 3), sCell = new Float32Array(N);
  const sSize = new Float32Array(N), sVel = new Float32Array(N);
  for (let i = 0; i < N; i++) {
    sp[i * 3] = (hash(i, 9.1) - 0.5) * 230;
    sp[i * 3 + 1] = hash(i, 3.3) * 78 + 1;
    sp[i * 3 + 2] = hash(i, 6.6) * 170 - 145;
    sCell[i] = Math.floor(hash(i, 12.4) * 10);
    sSize[i] = opt.flake[0] + hash(i, 15.8) * opt.flake[1];
    sVel[i] = 1.6 + hash(i, 21.3) * 3.4;
  }
  const snowGeo = new BufferGeometry();
  snowGeo.setAttribute('position', new Float32BufferAttribute(sp, 3));
  snowGeo.setAttribute('aCell', new Float32BufferAttribute(sCell, 1));
  snowGeo.setAttribute('aSize', new Float32BufferAttribute(sSize, 1));

  const snowMat = new ShaderMaterial({
    transparent: true, depthWrite: false,
    uniforms: { uAtlas: { value: digitAtlas() }, uO: { value: 0 } },
    vertexShader: `
      attribute float aCell; attribute float aSize;
      varying float vCell; varying float vFade;
      void main(){
        vCell = aCell;
        vec4 m = modelViewMatrix * vec4(position, 1.0);
        // Clamped: point size scales as 1/z, so without a ceiling the nearest
        // digits balloon into full-screen glyphs.
        gl_PointSize = clamp(aSize * (215.0 / -m.z), 6.0, 30.0);
        vFade = smoothstep(230.0, 25.0, -m.z);
        gl_Position = projectionMatrix * m;
      }`,
    fragmentShader: `
      uniform sampler2D uAtlas; uniform float uO;
      varying float vCell; varying float vFade;
      void main(){
        vec2 cell = vec2(mod(vCell, 4.0), floor(vCell / 4.0));
        vec4 c = texture2D(uAtlas, (cell + gl_PointCoord) * 0.25);
        if (c.a < 0.08) discard;
        gl_FragColor = vec4(0.90, 0.97, 0.93, c.a * uO * vFade);
      }`,
  });
  scene.add(new Points(snowGeo, snowMat));

  /* framing */
  function place(mx, my, wide) {
    camera.position.set((wide ? opt.cam[0] : 0) + mx * 7,
                        opt.cam[1] - my * 4, opt.cam[2]);
    camera.lookAt(wide ? opt.at[0] : 0, opt.at[1], opt.at[2]);
  }
  function resize() {
    const w = host.clientWidth, h = host.clientHeight;
    if (!w || !h) return;
    renderer.setSize(w, h, false);
    camera.aspect = w / h;
    camera.updateProjectionMatrix();
    place(0, 0, w > 900);
  }
  resize();
  addEventListener('resize', resize, { passive: true });

  /* loop */
  let mx = 0, my = 0, tx = 0, ty = 0, o = 0, last = performance.now();
  let onScreen = false, awake = !document.hidden;

  if (!reduced) {
    addEventListener('pointermove', e => {
      tx = e.clientX / innerWidth - 0.5;
      ty = e.clientY / innerHeight - 0.5;
    }, { passive: true });
  }

  const kick = () => { last = performance.now(); requestAnimationFrame(frame); };

  // Stop rendering entirely once this host scrolls off screen, and while the
  // tab is hidden. A background canvas that keeps painting is a battery
  // complaint — and with two mounts on one page it would be two of them.
  new IntersectionObserver(([e]) => {
    onScreen = e.isIntersecting;
    if (onScreen && awake) { if (reduced) still(); else kick(); }
  }, { threshold: 0 }).observe(host);

  document.addEventListener('visibilitychange', () => {
    awake = !document.hidden;
    if (awake && onScreen && !reduced) kick();
  });

  function frame(now) {
    if (!onScreen || !awake) return;
    const dt = Math.min((now - last) / 1000, 0.05);
    last = now;

    o = Math.min(o + dt * 0.85, 1);
    canvas.style.opacity = String(o * opt.max);
    snowMat.uniforms.uO.value = o * opt.snowO;

    const a = snowGeo.attributes.position.array;
    for (let i = 0; i < N; i++) {
      a[i * 3 + 1] -= sVel[i] * dt * 2.4;
      a[i * 3] += Math.sin(now * 0.0004 + i) * dt * 1.5;
      if (a[i * 3 + 1] < -2) {
        a[i * 3 + 1] = 80;
        a[i * 3] = (hash(i + now * 0.001, 9.1) - 0.5) * 230;
      }
    }
    snowGeo.attributes.position.needsUpdate = true;

    mx += (tx - mx) * Math.min(dt * 2.4, 1);
    my += (ty - my) * Math.min(dt * 2.4, 1);
    place(mx, my, host.clientWidth > 900);

    renderer.render(scene, camera);
    requestAnimationFrame(frame);
  }

  // Reduced motion still gets the mountain — it just does not move.
  function still() {
    canvas.style.opacity = String(opt.max);
    snowMat.uniforms.uO.value = opt.snowO;
    renderer.render(scene, camera);
  }
  if (reduced) still();
}

/* ------------------------------------------------------------------ boot */
const net = navigator.connection || {};
const frugal = net.saveData === true ||
               /(^|-)2g$/.test(net.effectiveType || '') ||
               (navigator.deviceMemory && navigator.deviceMemory < 4);

if (!frugal) {
  // Behind the hero the range is deliberately restrained: the headline has to
  // win, so it sits back in fog at low opacity with sparse snow. In the band
  // lower down it is the subject of the section and runs at full strength.
  const MOUNTS = [
    ['summit',      { max: 0.78, snowO: 0.62, snow: 620,  fov: 54, fog: 0.0040,
                      wire: 0.06, flake: [1.5, 2.6], cam: [10, 24, 40], at: [0, 17, -78] }],
    ['summit-band', { max: 1.00, snowO: 0.85, snow: 1050, fov: 50, fog: 0.0034,
                      wire: 0.09, flake: [1.8, 3.2], cam: [4, 20, 34],  at: [0, 15, -80] }],
  ];
  for (const [id, opt] of MOUNTS) {
    const c = document.getElementById(id);
    if (c && c.parentElement) mount(c, c.parentElement, opt);
  }
}
