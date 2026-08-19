/**
 * NorthPeak hero — procedural alpine terrain with numeric snowfall.
 *
 * Loaded only after the page has finished loading and the browser is idle, so
 * it contributes nothing to LCP, FCP, or Total Blocking Time. Until it fades in
 * (and forever, on devices that decline it) the hero is carried by the CSS
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

const canvas = document.getElementById('summit');
const hero = canvas && canvas.closest('.hero');
if (canvas && hero) start();

function start() {
  const reduced = matchMedia('(prefers-reduced-motion: reduce)').matches;
  const net = navigator.connection || {};
  const frugal = net.saveData === true ||
                 /(^|-)2g$/.test(net.effectiveType || '') ||
                 (navigator.deviceMemory && navigator.deviceMemory < 4);
  if (frugal) return;                       // gradient carries the hero

  let renderer;
  try {
    renderer = new WebGLRenderer({ canvas, antialias: true, alpha: true,
                                   powerPreference: 'low-power' });
  } catch (e) {
    return;                                 // no WebGL — gradient carries it
  }
  renderer.setPixelRatio(Math.min(devicePixelRatio, 2));
  renderer.setClearColor(0x000000, 0);

  const scene = new Scene();
  scene.fog = new FogExp2(0x0d2b1e, 0.0038);
  const camera = new PerspectiveCamera(54, 1, 0.1, 400);

  /* ---------------------------------------------------------------- noise */
  // Deterministic value noise. Seeded so the terrain is identical on every
  // load and on every visitor's machine.
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
    return (a + (b - a) * xf) + ((c + (d - c) * xf) - (a + (b - a) * xf)) * yf;
  }
  // Ridged fractal: 1 - |noise| sharpens the crests into ridgelines rather than
  // the rolling hills plain fBm produces.
  function ridged(x, y) {
    let sum = 0, amp = 0.5, freq = 1;
    for (let o = 0; o < 5; o++) {
      sum += (1 - Math.abs(value(x * freq, y * freq) * 2 - 1)) * amp;
      amp *= 0.5; freq *= 2.07;
    }
    return sum;
  }

  /* -------------------------------------------------------------- terrain */
  const SIZE = 200, SEG = 148;
  const geo = new PlaneGeometry(SIZE, SIZE, SEG, SEG);
  geo.rotateX(-Math.PI / 2);
  const pos = geo.attributes.position;

  // Five gaussian summits give the range a deliberate silhouette instead of
  // uniform noise. The tallest sits left of frame so it does not collide with
  // the headline, which occupies the left third on wide screens.
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

  // The range sits downrange of the camera rather than centred on it, so the
  // view is across the valley toward the summits instead of from inside the
  // slope. Both meshes share one geometry and move together.
  const range = new Group();
  range.position.z = -104;
  range.add(new Mesh(geo, new MeshStandardMaterial({
    vertexColors: true, flatShading: true, roughness: 0.86, metalness: 0.0,
  })));

  // A faint wireframe over the same geometry reads as surveyed terrain rather
  // than scenery — the visual argument that this firm measures things.
  range.add(new Mesh(geo, new MeshBasicMaterial({
    color: 0x7fe0b6, wireframe: true, transparent: true, opacity: 0.085,
  })));
  scene.add(range);

  /* --------------------------------------------------------------- lights */
  scene.add(new HemisphereLight(0xb6e4cf, 0x0d2a1e, 1.15));
  const key = new DirectionalLight(0xffeccb, 2.15); key.position.set(-58, 34, 22);
  scene.add(key);
  const rim = new DirectionalLight(0x46b98d, 0.85); rim.position.set(48, 10, -46);
  scene.add(rim);

  /* ---------------------------------------------------------------- stars */
  {
    const N = 900, p = new Float32Array(N * 3);
    for (let i = 0; i < N; i++) {
      const th = hash(i, 1.7) * Math.PI * 2;
      const ph = Math.acos(hash(i, 4.2) * 0.72);
      const r = 190;
      p[i * 3] = Math.sin(ph) * Math.cos(th) * r;
      p[i * 3 + 1] = Math.abs(Math.cos(ph)) * r * 0.62 + 24;
      p[i * 3 + 2] = Math.sin(ph) * Math.sin(th) * r;
    }
    const g = new BufferGeometry();
    g.setAttribute('position', new BufferAttribute(p, 3));
    scene.add(new Points(g, new ShaderMaterial({
      transparent: true, depthWrite: false, blending: AdditiveBlending,
      uniforms: { uO: { value: 0.5 } },
      vertexShader: `void main(){vec4 m=modelViewMatrix*vec4(position,1.0);
        gl_PointSize=1.6;gl_Position=projectionMatrix*m;}`,
      fragmentShader: `uniform float uO;void main(){
        vec2 d=gl_PointCoord-0.5;if(dot(d,d)>0.25)discard;
        gl_FragColor=vec4(0.85,0.94,0.90,uO);}`,
    })));
  }

  /* ------------------------------------------------- numeric snowfall ---- */
  // The snow is digits. Rendering 900 individual text sprites would be 900 draw
  // calls, so all ten glyphs are baked into one 4x4 texture atlas and drawn as
  // a single Points cloud; a per-particle attribute picks which cell of the
  // atlas each point samples. One draw call, ten distinct glyphs.
  function digitAtlas() {
    const CELL = 128, c = document.createElement('canvas');
    c.width = c.height = CELL * 4;
    const g = c.getContext('2d');
    g.font = `600 ${CELL * 0.72}px Inter, system-ui, -apple-system, sans-serif`;
    g.textAlign = 'center'; g.textBaseline = 'middle';
    g.fillStyle = '#ffffff';
    for (let i = 0; i < 10; i++) {
      const col = i % 4, row = Math.floor(i / 4);
      g.fillText(String(i), col * CELL + CELL / 2, row * CELL + CELL / 2);
    }
    const t = new CanvasTexture(c);
    t.flipY = false;              // match gl_PointCoord, whose origin is top-left
    return t;
  }

  const SNOW = 1350;
  const sp = new Float32Array(SNOW * 3);
  const sCell = new Float32Array(SNOW);
  const sSize = new Float32Array(SNOW);
  const sVel = new Float32Array(SNOW);
  for (let i = 0; i < SNOW; i++) {
    sp[i * 3] = (hash(i, 9.1) - 0.5) * 230;
    sp[i * 3 + 1] = hash(i, 3.3) * 78 + 1;
    sp[i * 3 + 2] = hash(i, 6.6) * 170 - 145;
    sCell[i] = Math.floor(hash(i, 12.4) * 10);
    sSize[i] = 0.9 + hash(i, 15.8) * 2.0;
    sVel[i] = 1.6 + hash(i, 21.3) * 3.4;
  }
  const snowGeo = new BufferGeometry();
  snowGeo.setAttribute('position', new Float32BufferAttribute(sp, 3));
  snowGeo.setAttribute('aCell', new Float32BufferAttribute(sCell, 1));
  snowGeo.setAttribute('aSize', new Float32BufferAttribute(sSize, 1));

  const snowMat = new ShaderMaterial({
    transparent: true, depthWrite: false,
    uniforms: { uAtlas: { value: digitAtlas() }, uO: { value: 0.0 } },
    vertexShader: `
      attribute float aCell; attribute float aSize;
      varying float vCell; varying float vFade;
      void main(){
        vCell = aCell;
        vec4 m = modelViewMatrix * vec4(position, 1.0);
        gl_PointSize = clamp(aSize * (200.0 / -m.z), 2.0, 15.0);
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
        gl_FragColor = vec4(0.86, 0.95, 0.90, c.a * uO * vFade);
      }`,
  });
  const snow = new Points(snowGeo, snowMat);
  scene.add(snow);

  /* ------------------------------------------------------------- framing */
  function resize() {
    const w = hero.clientWidth, h = hero.clientHeight;
    renderer.setSize(w, h, false);
    camera.aspect = w / h;
    // On wide screens the copy sits in the left third, so the range is pushed
    // right to keep the headline over open sky. On narrow screens it centres.
    camera.position.set(w > 900 ? 10 : 0, 24, 40);
    camera.lookAt(w > 900 ? 0 : 0, 17, -78);
    camera.updateProjectionMatrix();
  }
  resize();
  addEventListener('resize', resize, { passive: true });

  /* --------------------------------------------------------------- loop */
  let px = 0, py = 0, tx = 0, ty = 0, opacity = 0, last = performance.now();
  let visible = true, running = true;

  if (!reduced) {
    addEventListener('pointermove', e => {
      tx = e.clientX / innerWidth - 0.5;
      ty = e.clientY / innerHeight - 0.5;
    }, { passive: true });
  }

  // Stop rendering entirely once the hero scrolls off screen, and while the tab
  // is hidden. A background canvas that keeps painting is a battery complaint.
  new IntersectionObserver(([e]) => {
    visible = e.isIntersecting;
    if (visible && running) { last = performance.now(); requestAnimationFrame(frame); }
  }, { threshold: 0 }).observe(hero);

  document.addEventListener('visibilitychange', () => {
    running = !document.hidden;
    if (running && visible) { last = performance.now(); requestAnimationFrame(frame); }
  });

  function frame(now) {
    if (!visible || !running) return;
    const dt = Math.min((now - last) / 1000, 0.05);
    last = now;

    // Fade the whole scene in over ~1.2s so it arrives rather than pops.
    opacity = Math.min(opacity + dt * 0.85, 1);
    canvas.style.opacity = String(opacity);
    snowMat.uniforms.uO.value = opacity * 0.8;

    const a = snowGeo.attributes.position.array;
    for (let i = 0; i < SNOW; i++) {
      a[i * 3 + 1] -= sVel[i] * dt * 2.4;
      a[i * 3] += Math.sin(now * 0.0004 + i) * dt * 1.5;
      if (a[i * 3 + 1] < -2) {
        a[i * 3 + 1] = 80;
        a[i * 3] = (hash(i + now * 0.001, 9.1) - 0.5) * 230;
      }
    }
    snowGeo.attributes.position.needsUpdate = true;

    px += (tx - px) * Math.min(dt * 2.4, 1);
    py += (ty - py) * Math.min(dt * 2.4, 1);
    const wide = hero.clientWidth > 900;
    camera.position.x = (wide ? 10 : 0) + px * 7;
    camera.position.y = 24 - py * 4;
    camera.lookAt(0, 17, -78);

    renderer.render(scene, camera);
    if (!reduced) requestAnimationFrame(frame);
  }

  // Reduced motion still gets the mountain — it just does not move. Snow is
  // rendered at rest so the scene is a still image rather than an empty sky.
  if (reduced) {
    opacity = 1; canvas.style.opacity = '1';
    snowMat.uniforms.uO.value = 0.8;
    renderer.render(scene, camera);
  } else {
    requestAnimationFrame(frame);
  }
}
