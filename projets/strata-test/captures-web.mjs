// Captures web pour le montage : Chrome sans interface, piloté par le protocole DevTools.
// node projets/strata-test/captures-web.mjs "D:/_Technovore/Youtube/Strata test/captures web" [code…]  (sans code : toutes ; ex. C8 le jour du montage)
import { spawn } from 'node:child_process';
import { mkdirSync, writeFileSync } from 'node:fs';
import { join } from 'node:path';
import { tmpdir } from 'node:os';

const OUT = process.argv[2];
const ONLY = process.argv.slice(3);
const CHROME = 'C:/Program Files/Google/Chrome/Application/chrome.exe';
const PORT = 9333;
const W = 1280, H = 720, DPR = 3;
const GH = 'https://github.com/Niko1221/Strata';

// style : 'mark' (surligné) ou 'strike' (barré). top : capture du haut de page (pas de phrase).
const JOBS = [
  { code: 'P02', url: GH, shots: [
    { id: 'haut', top: true },
    { id: 'licence-mit', text: 'MIT license', near: 'on any consumer' },
  ] },
  { code: 'P03', url: 'https://huggingface.co/ISTA-DASLab/Qwen3.8-Flash-Next-GSQ-RCO-Coder-GGUF', shots: [
    { id: 'haut', top: true },
    { id: 'moitie-des-experts', text: 'half of its experts removed' },
    { id: 'experimental', text: 'This is an experimental release' },
    { id: 'scores', text: ['82.80', '79.20', '95.7%'], near: 'BF16 base (354 GB)' },
    { id: 'taille', text: 'reduces to only 29.6 GB' },
  ] },
  { code: 'C1', url: `${GH}/issues/4997`, shots: [
    { id: 'haut', top: true },
    { id: 'machine', text: ['RTX 5070 Ti, 16 GiB VRAM', 'Ryzen 7 9700X', '31.2 GiB'], near: 'GPU and VRAM:' },
    { id: 'vitesse', text: ['70.4', 'thinking off for the suite; temperature 0'] },
    { id: 'sans-test', text: 'Speed only: no correctness check was run' },
  ] },
  { code: 'C2', url: `${GH}/issues/5104`, shots: [
    { id: 'haut', top: true },
    { id: 'plantage', text: ['exit code -6', 'could not copy experts'] },
    { id: 'faux-message', text: 'The usual cause is running out of RAM', style: 'strike' },
    { id: 'vraie-cause', text: 'Root cause confirmed' },
  ] },
  { code: 'C3', url: `${GH}/issues/5046`, shots: [
    { id: 'haut', top: true },
    { id: 'logits', text: ['RTX 5080', 'non-finite logits', 'IQ3_S and IQ3_XXS'] },
  ] },
  { code: 'C4', url: `${GH}/blob/main/docs/MODELS.md`, suffix: 'models', shots: [
    { id: 'will-it-fit', text: ['Will it fit?', 'RAM is at least the experts plus about 10 GB'] },
    { id: '32-go-16-go', text: 'a 32 GB PC with a 12 to 16 GB GPU runs the Coder' },
    { id: 'anglais', text: 'weaker outside code and in languages other than English' },
  ] },
  { code: 'C4', url: `${GH}/blob/main/docs/DETAILS.md`, suffix: 'details', shots: [
    { id: 'vitesses-coder', text: ['Output (tokens/s)', '58.9', '43.0'] },
  ] },
  { code: 'C6', url: `${GH}/releases`, shots: [
    { id: 'haut', top: true },
  ] },
  { code: 'C6', url: 'https://api.github.com/repos/Niko1221/Strata', suffix: 'creation', shots: [
    { id: 'date', text: '"created_at": "2026-09-24' },
  ] },
  { code: 'C7', url: `${GH}/issues/2250`, shots: [
    { id: 'haut', top: true },
    { id: 'carte', text: ['9600 XT', '30.3 GiB', '37.6'] },
  ] },
  { code: 'C8', url: 'https://claude.com/pricing', shots: [
    { id: 'haut', top: true },
    { id: 'pro', text: ['$20 if billed monthly', 'Claude Code'] },
  ] },
];

// Script injecté dans la page : floute les pseudos et les avatars, cache ce qui flotte, pose les marques.
const PAGE_LIB = String.raw`
(() => {
  if (window.__cap) return;
  const RESERVED = new Set(['features','pricing','login','signup','about','topics','enterprise','sponsors','orgs','settings','marketplace','explore','collections','trending','security','team','customer-stories','readme','solutions','resources','apps','site','contact','search','notifications','new','codespaces','github','join','home']);
  const style = document.createElement('style');
  style.textContent = '.__blur{filter:blur(7px)!important}'
    + 'img.__blur{filter:blur(10px)!important}'
    + 'mark.__m{color:inherit!important;background:transparent;border-radius:3px;transition:none}'
    + 'html.__hl mark.__m.__on{background:rgba(255,214,0,.6)!important;box-shadow:0 0 0 3px rgba(255,214,0,.6)!important}'
    + 'html.__hl mark.__m.__on.__strike{background:transparent!important;box-shadow:none!important;text-decoration:line-through!important;text-decoration-color:#e11d48!important;text-decoration-thickness:4px!important}';
  document.head.appendChild(style);

  const textNodes = (root) => {
    const out = [];
    const w = document.createTreeWalker(root, NodeFilter.SHOW_TEXT, { acceptNode: n =>
      n.parentElement && !n.parentElement.closest('script,style,noscript,template') ? NodeFilter.FILTER_ACCEPT : NodeFilter.FILTER_REJECT });
    for (let n; (n = w.nextNode());) out.push(n);
    return out;
  };

  // Cherche une phrase (espaces normalisés) et entoure chaque morceau d'une balise.
  const wrap = (phrase, make) => {
    const nodes = textNodes(document.body);
    let norm = '', map = [], prevSpace = true;
    for (const n of nodes) {
      const t = n.data;
      for (let i = 0; i < t.length; i++) {
        const sp = /\s/.test(t[i]);
        if (sp) { if (prevSpace) continue; norm += ' '; } else norm += t[i];
        map.push([n, i]); prevSpace = sp;
      }
    }
    const target = phrase.replace(/\s+/g, ' ').trim();
    const starts = [];
    for (let from = 0; starts.length < 40;) {
      const at = norm.indexOf(target, from);
      if (at < 0) break;
      starts.push(at); from = at + target.length;
    }
    // De la dernière occurrence à la première : découper la fin d'un nœud garde valides les positions du début.
    const results = [];
    for (const at of starts.reverse()) {
      const pieces = new Map();
      for (let k = at; k < at + target.length; k++) {
        const [n, i] = map[k];
        const p = pieces.get(n) || [i, i]; p[0] = Math.min(p[0], i); p[1] = Math.max(p[1], i); pieces.set(n, p);
      }
      const els = [];
      for (const [n, [a, b]] of [...pieces].reverse()) {
        const mid = n.splitText(a); mid.splitText(b - a + 1);
        const el = make(); mid.parentNode.insertBefore(el, mid); el.appendChild(mid); els.unshift(el);
      }
      results.unshift(els);
    }
    return results;
  };

  const isVisible = (el) => { const r = el.getBoundingClientRect(); return r.width > 0 && r.height > 0; };

  window.__cap = {
    clean() {
      // Ce qui flotte (en-têtes collants, bandeaux de cookies) gêne quand on fait défiler.
      for (const el of document.querySelectorAll('body *')) {
        const cs = getComputedStyle(el);
        if (cs.position === 'fixed') el.style.setProperty('display', 'none', 'important');
        else if (cs.position === 'sticky') el.style.setProperty('position', 'static', 'important');
      }
    },
    blur() {
      const logins = new Set(['Niko1221']);
      const host = location.hostname;
      if (host.endsWith('github.com')) {
        for (const a of document.querySelectorAll('a[href]')) {
          let u; try { u = new URL(a.href); } catch { continue; }
          if (u.hostname !== 'github.com') continue;
          const seg = u.pathname.replace(/^\/|\/$/g, '');
          if (!seg || seg.includes('/') || RESERVED.has(seg.toLowerCase())) continue;
          const txt = a.textContent.trim().replace(/^@/, '');
          if (txt === seg) logins.add(seg);
        }
        for (const el of document.querySelectorAll('[data-hovercard-url^="/users/"], .author, [data-testid*="author"]')) {
          const t = el.textContent.trim().replace(/^@/, '');
          if (t && !/\s/.test(t) && t.length < 40 && !/^(Owner|Author|Member|Contributor|Collaborator|Maintainer)$/.test(t)) logins.add(t);
        }
      }
      for (const img of document.querySelectorAll('img')) {
        if (/avatars\.githubusercontent|cdn-avatars\.huggingface|gravatar/.test(img.src)) img.classList.add('__blur');
      }
      const found = [];
      for (const login of logins) {
        const re = new RegExp('(^|[^A-Za-z0-9_-])(@?' + login.replace(/[^A-Za-z0-9_-]/g, '\\$&') + ')(?![A-Za-z0-9_-])');
        for (const n of textNodes(document.body)) {
          let node = n;
          for (let guard = 0; guard < 50; guard++) {
            const m = re.exec(node.data);
            if (!m) break;
            const start = m.index + m[1].length;
            const mid = node.splitText(start);
            const rest = mid.splitText(m[2].length);
            const s = document.createElement('span'); s.className = '__blur';
            mid.parentNode.insertBefore(s, mid); s.appendChild(mid);
            node = rest;
          }
        }
        found.push(login);
      }
      return found;
    },
    // Première phrase : sa première occurrence visible. Les suivantes : l'occurrence visible la plus proche de celle-là.
    mark(shotId, phrases, strike, near) {
      const missing = [];
      let anchorY = null;
      const yOf = (g) => g[0].getBoundingClientRect().top + scrollY;
      if (near) { const g = wrap(near, () => { const m = document.createElement('mark'); m.className = '__m'; return m; }).find(g => g.length && g.every(isVisible)); if (g) anchorY = yOf(g); }
      for (const p of phrases) {
        const groups = wrap(p, () => { const m = document.createElement('mark'); m.className = '__m'; return m; })
          .filter(g => g.length && g.every(isVisible));
        if (!groups.length) { missing.push(p); continue; }
        let pick = groups[0];
        if (anchorY !== null) pick = groups.reduce((a, g) => Math.abs(yOf(g) - anchorY) < Math.abs(yOf(a) - anchorY) ? g : a);
        else anchorY = yOf(pick);
        for (const el of pick) el.classList.add('__s-' + shotId, ...(strike ? ['__strike'] : []));
      }
      return missing;
    },
    focus(shotId) {
      document.documentElement.classList.remove('__hl');
      for (const m of document.querySelectorAll('mark.__m')) m.classList.toggle('__on', m.classList.contains('__s-' + shotId));
      const els = [...document.querySelectorAll('mark.__s-' + shotId)].filter(isVisible);
      if (!els.length) return false;
      // Centre le groupe de marques dans l'écran.
      const rs = els.map(e => e.getBoundingClientRect());
      const top = Math.min(...rs.map(r => r.top)) + scrollY, bottom = Math.max(...rs.map(r => r.bottom)) + scrollY;
      scrollTo(0, Math.max(0, (top + bottom) / 2 - innerHeight / 2));
      return { span: Math.round(bottom - top) };
    },
    highlight(on) { document.documentElement.classList.toggle('__hl', on); },
  };
})();
`;

const sleep = (ms) => new Promise(r => setTimeout(r, ms));

async function cdp(wsUrl) {
  const ws = new WebSocket(wsUrl);
  await new Promise((res, rej) => { ws.onopen = res; ws.onerror = rej; });
  let id = 0; const pending = new Map(); const listeners = [];
  ws.onmessage = (ev) => {
    const msg = JSON.parse(ev.data);
    if (msg.id && pending.has(msg.id)) { const { res, rej } = pending.get(msg.id); pending.delete(msg.id); msg.error ? rej(new Error(JSON.stringify(msg.error))) : res(msg.result); }
    else if (msg.method) for (const l of listeners) l(msg);
  };
  const send = (method, params = {}) => new Promise((res, rej) => { const i = ++id; pending.set(i, { res, rej }); ws.send(JSON.stringify({ id: i, method, params })); });
  const once = (method, timeout = 30000) => new Promise((res) => {
    const t = setTimeout(() => res(null), timeout);
    const l = (m) => { if (m.method === method) { clearTimeout(t); listeners.splice(listeners.indexOf(l), 1); res(m.params); } };
    listeners.push(l);
  });
  return { send, once, close: () => ws.close() };
}

async function evaluate(c, expr) {
  const r = await c.send('Runtime.evaluate', { expression: expr, returnByValue: true, awaitPromise: true });
  if (r.exceptionDetails) throw new Error(r.exceptionDetails.exception?.description || r.exceptionDetails.text);
  return r.result.value;
}

async function shoot(c, file, full) {
  let params = { format: 'png' };
  if (full) {
    const m = await c.send('Page.getLayoutMetrics');
    const h = Math.min(Math.ceil(m.cssContentSize.height), 9000);
    params = { format: 'png', captureBeyondViewport: true, clip: { x: 0, y: 0, width: W, height: h, scale: 2 / DPR } };
  }
  const { data } = await c.send('Page.captureScreenshot', params);
  writeFileSync(file, Buffer.from(data, 'base64'));
}

const main = async () => {
  mkdirSync(OUT, { recursive: true });
  const prof = join(tmpdir(), 'captures-web-chrome');
  const chrome = spawn(CHROME, ['--headless=new', `--remote-debugging-port=${PORT}`, `--user-data-dir=${prof}`, `--window-size=${W},${H}`,
    '--hide-scrollbars', '--no-first-run', '--no-default-browser-check', '--lang=en-US', '--force-color-profile=srgb', 'about:blank'], { stdio: 'ignore' });
  let pages;
  for (let i = 0; i < 50; i++) { try { pages = await (await fetch(`http://127.0.0.1:${PORT}/json/list`)).json(); if (pages.length) break; } catch {} await sleep(200); }
  const c = await cdp(pages.find(p => p.type === 'page').webSocketDebuggerUrl);
  await c.send('Page.enable'); await c.send('Runtime.enable');
  await c.send('Emulation.setDeviceMetricsOverride', { width: W, height: H, deviceScaleFactor: DPR, mobile: false });
  await c.send('Emulation.setEmulatedMedia', { features: [{ name: 'prefers-color-scheme', value: 'light' }] });
  const report = [];
  for (const job of JOBS) {
    if (ONLY.length && !ONLY.includes(job.code)) continue;
    const base = job.code + (job.suffix ? '-' + job.suffix : '');
    const loaded = c.once('Page.loadEventFired', 45000);
    await c.send('Page.navigate', { url: job.url });
    await loaded; await sleep(4000);
    await evaluate(c, PAGE_LIB);
    await evaluate(c, '__cap.clean()');
    const blurred = await evaluate(c, '__cap.blur()');
    const line = { page: base, url: job.url, blurred, shots: [] };
    let n = 0;
    for (const s of job.shots) {
      n++;
      const name = `${base}-${n}-${s.id}`;
      if (s.top) {
        await evaluate(c, '__cap.highlight(false); scrollTo(0,0)'); await sleep(400);
        await shoot(c, join(OUT, name + '.png'));
        line.shots.push({ name, ok: true });
        continue;
      }
      const phrases = Array.isArray(s.text) ? s.text : [s.text];
      const missing = await evaluate(c, `__cap.mark(${JSON.stringify(s.id)}, ${JSON.stringify(phrases)}, ${!!(s.style === 'strike')}, ${JSON.stringify(s.near || null)})`);
      const f = await evaluate(c, `__cap.focus(${JSON.stringify(s.id)})`);
      if (!f) { line.shots.push({ name, ok: false, missing }); continue; }
      await sleep(400);
      await shoot(c, join(OUT, name + '.png'));
      await evaluate(c, '__cap.highlight(true)'); await sleep(150);
      await shoot(c, join(OUT, name + (s.style === 'strike' ? '-barre' : '-surligne') + '.png'));
      line.shots.push({ name, ok: true, missing, span: f.span });
    }
    await evaluate(c, '__cap.highlight(false)');
    await shoot(c, join(OUT, `${base}-page.png`), true);
    report.push(line);
    console.log(JSON.stringify(line));
  }
  c.close(); chrome.kill();
};
main().catch(e => { console.error(e); process.exit(1); });
