// Calques PhotoCraft, après l'ajustement des textes :
//   ?layer=decor  cache les textes qui deviennent des calques de texte (les textes tournés restent dans le décor)
//   ?dump=1       écrit leur position et leur style en JSON dans <pre id="dump"> (lu par psd.py via --dump-dom)
document.fonts.ready.then(() => setTimeout(() => {
  const q = new URLSearchParams(location.search);
  const hex = c => '#' + c.match(/\d+/g).slice(0, 3).map(v => (+v).toString(16).padStart(2, '0')).join('');
  const font = f => /Archivo/.test(f) ? 'Archivo Black' : /Anton/.test(f) ? 'Anton' : /JetBrains/.test(f) ? 'JetBrains Mono' : /Inter/.test(f) ? 'Inter' : /Mono/.test(f) ? 'Menlo' : 'System Font';
  // Contour (-webkit-text-stroke) et première ombre (text-shadow), repris en styles de calque par psd.py
  const stroke = cs => parseFloat(cs.webkitTextStrokeWidth) > 0 ? { w: parseFloat(cs.webkitTextStrokeWidth), color: hex(cs.webkitTextStrokeColor) } : null;
  const shadow = cs => {
    const m = cs.textShadow.match(/(rgba?\([^)]*\))\s+(-?[\d.]+)px\s+(-?[\d.]+)px\s+([\d.]+)px/);
    return m ? { color: hex(m[1]), dx: +m[2], dy: +m[3], blur: +m[4] } : null;
  };
  const items = [...document.querySelectorAll('.t')].filter(e => {
    const m = new DOMMatrix(getComputedStyle(e).transform);
    return Math.abs(m.b) < 1e-3 && getComputedStyle(e).display !== 'none';
  });
  if (q.get('layer') === 'decor') items.forEach(e => e.style.visibility = 'hidden');
  if (!q.get('dump')) return;
  const out = items.map(e => {
    const cs = getComputedStyle(e), probe = document.createElement('span');
    probe.style.cssText = 'display:inline-block;width:0;height:0';
    e.prepend(probe); // ligne de base de la première ligne (type.create l'attend)
    const base = probe.getBoundingClientRect().top;
    probe.remove();
    const runs = [], w = document.createTreeWalker(e, NodeFilter.SHOW_TEXT | NodeFilter.SHOW_ELEMENT);
    while (w.nextNode()) {
      if (w.currentNode.nodeName === 'BR') { runs.push({ t: '\r', color: runs.length ? runs[runs.length - 1].color : hex(cs.color), weight: +cs.fontWeight }); continue; }
      if (w.currentNode.nodeType !== Node.TEXT_NODE) continue;
      const p = getComputedStyle(w.currentNode.parentElement);
      let t = w.currentNode.textContent.replace(/ /g, ' ').replace(/ /g, ' ');
      if (p.textTransform === 'uppercase') t = t.toUpperCase();
      if (t) runs.push({ t, color: hex(p.color), weight: +p.fontWeight, size: parseFloat(p.fontSize) });
    }
    const size = parseFloat(cs.fontSize);
    return { x: e.getBoundingClientRect().left, y: base, size, font: font(cs.fontFamily), weight: +cs.fontWeight,
      tracking: Math.round((parseFloat(cs.letterSpacing) || 0) / size * 1000), hscale: Math.round(new DOMMatrix(cs.transform).a * 100),
      opacity: +cs.opacity, leading: parseFloat(cs.lineHeight) || null, stroke: stroke(cs), shadow: shadow(cs), runs };
  });
  const pre = document.createElement('pre');
  pre.id = 'dump';
  pre.textContent = JSON.stringify(out);
  document.body.appendChild(pre);
}, 0));
