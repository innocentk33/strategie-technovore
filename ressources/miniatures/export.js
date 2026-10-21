// Calques PhotoCraft, après l'ajustement des textes :
//   ?layer=decor  cache les textes qui deviennent des calques de texte (les textes tournés restent dans le décor)
//   ?dump=1       écrit leur position et leur style en JSON dans <pre id="dump"> (lu par psd.py via --dump-dom)
document.fonts.ready.then(() => setTimeout(() => {
  const q = new URLSearchParams(location.search);
  const hex = c => '#' + c.match(/\d+/g).slice(0, 3).map(v => (+v).toString(16).padStart(2, '0')).join('');
  const font = f => /Archivo/.test(f) ? 'Archivo Black' : /JetBrains/.test(f) ? 'JetBrains Mono' : /Inter/.test(f) ? 'Inter' : /Mono/.test(f) ? 'Menlo' : 'System Font';
  const items = [...document.querySelectorAll('.t')].filter(e => {
    const m = new DOMMatrix(getComputedStyle(e).transform);
    return Math.abs(m.b) < 1e-3 && getComputedStyle(e).display !== 'none';
  });
  if (q.get('layer') === 'decor') items.forEach(e => e.style.visibility = 'hidden');
  if (!q.get('dump')) return;
  const out = items.map(e => {
    const cs = getComputedStyle(e), probe = document.createElement('span');
    probe.style.cssText = 'display:inline-block;width:0;height:0';
    e.appendChild(probe);
    const base = probe.getBoundingClientRect().top;
    probe.remove();
    const runs = [], w = document.createTreeWalker(e, NodeFilter.SHOW_TEXT);
    while (w.nextNode()) {
      const p = getComputedStyle(w.currentNode.parentElement);
      let t = w.currentNode.textContent.replace(/ /g, ' ').replace(/ /g, ' ');
      if (p.textTransform === 'uppercase') t = t.toUpperCase();
      if (t) runs.push({ t, color: hex(p.color), weight: +p.fontWeight });
    }
    const size = parseFloat(cs.fontSize);
    return { x: e.getBoundingClientRect().left, y: base, size, font: font(cs.fontFamily), weight: +cs.fontWeight,
      tracking: Math.round((parseFloat(cs.letterSpacing) || 0) / size * 1000), hscale: Math.round(new DOMMatrix(cs.transform).a * 100),
      opacity: +cs.opacity, runs };
  });
  const pre = document.createElement('pre');
  pre.id = 'dump';
  pre.textContent = JSON.stringify(out);
  document.body.appendChild(pre);
}, 0));
