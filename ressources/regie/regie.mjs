#!/usr/bin/env node
// La régie : lit les .md du dépôt et pilote le suivi des vidéos (statuts du README, cases à cocher).
// Lancement : node ressources/regie/regie.mjs [port], puis http://localhost:4321
import http from 'node:http';
import fs from 'node:fs';
import path from 'node:path';

const ROOT = path.resolve(process.env.REGIE_DEPOT ?? path.join(import.meta.dirname, '../..'));
const PORT = Number(process.argv[2]) || 4321;
const HOTES = new Set([`localhost:${PORT}`, `127.0.0.1:${PORT}`]);
const IGNORES = new Set(['node_modules', 'claude-youtube']);
const STATUTS = ['Fiche', 'Brouillon', 'Recherche', 'Script', 'Voix', 'Montage', 'Programmé', 'Publié'];
const RE_STATUT = /^(\*\*)?(Fiche|Brouillon|Recherche|Script|Voix|Montage|Programmé|Publiée?)(?!\p{L})(\*\*)?/u;
const RE_CASE = /^(\s*(?:>\s*)*(?:[-*+]|\d+[.)])\s+\[)([ xX])(\])(?=\s)/;
const LIEN_FICHE = /\]\(projets\/([\w-]+)\/fiche\.md\)/;
const MOIS = ['janv', 'févr', 'mars', 'avr', 'mai', 'juin', 'juil', 'août', 'sept', 'oct', 'nov', 'déc'];
// Les étapes d'un dossier, dans l'ordre de production de CLAUDE.md (la voix avant le storyboard, calé sur elle)
const ETAPES = [
  ['fiche', /^fiche\.md$/], ['brouillon', /^brouillon.*\.md$/i], ['script', /^script\.md$/], ['grill', /^grill.*\.md$/],
  ['sources', /^sources\.md$/], ['prompteur', /^teleprompteur\.md$/], ['voix', /^[^/]+\.(m4a|wav)$/],
  ['storyboard', /^storyboard\.md$/i], ['upload', /^upload\.md$/], ['miniatures', /^miniature\//],
];
const TYPES = {
  '.html': 'text/html; charset=utf-8', '.md': 'text/plain; charset=utf-8', '.txt': 'text/plain; charset=utf-8',
  '.srt': 'text/plain; charset=utf-8', '.json': 'application/json', '.js': 'text/javascript', '.css': 'text/css',
  '.png': 'image/png', '.jpg': 'image/jpeg', '.jpeg': 'image/jpeg', '.webp': 'image/webp', '.gif': 'image/gif',
  '.svg': 'image/svg+xml', '.woff2': 'font/woff2', '.m4a': 'audio/mp4', '.wav': 'audio/wav', '.pdf': 'application/pdf',
};

const erreur = (status, message) => Object.assign(new Error(message), { status });

function chemin(rel) {
  const abs = path.resolve(ROOT, rel);
  if (!abs.startsWith(ROOT + path.sep) || rel.split('/').some(p => p.startsWith('.'))) throw erreur(403, 'Chemin refusé');
  return abs;
}
const lire = rel => fs.readFileSync(chemin(rel), 'utf8');

function fichiers(dir = '') {
  const out = [];
  for (const e of fs.readdirSync(path.join(ROOT, dir), { withFileTypes: true })) {
    if (e.name.startsWith('.') || IGNORES.has(e.name)) continue;
    const rel = dir ? `${dir}/${e.name}` : e.name;
    if (e.isDirectory()) out.push(...fichiers(rel)); else out.push(rel);
  }
  return out;
}

const cellules = ligne => ligne.trim().slice(1, -1).split('|').map(c => c.trim());

// Les lignes « - [ ] » hors des blocs de code : le n-ième rendu par la page est le n-ième ici
function lignesCases(lignes) {
  const idx = [];
  let code = false;
  lignes.forEach((l, i) => {
    if (/^\s*(```|~~~)/.test(l)) code = !code;
    else if (!code && RE_CASE.test(l)) idx.push(i);
  });
  return idx;
}

function compteCases(src) {
  const lignes = src.split('\n');
  const idx = lignesCases(lignes);
  return { fait: idx.filter(i => lignes[i].match(RE_CASE)[2] !== ' ').length, total: idx.length };
}

// ponytail: relit tous les .md des projets à chaque appel (~3 Mo, quelques ms) ; un cache par mtime si ça rame un jour
function projets() {
  const tous = fichiers();
  const piliers = {};
  for (const l of lire('calendrier.md').split('\n')) {
    const m = l.startsWith('|') && l.match(LIEN_FICHE);
    if (m && !(m[1] in piliers)) piliers[m[1]] = cellules(l)[3]?.split(' ')[0];
  }
  // Le tableau du README est chronologique : l'année avance quand le mois recule
  let annee, moisPrec;
  return lire('README.md').split('\n').filter(l => l.startsWith('|') && LIEN_FICHE.test(l)).map(l => {
    const [video, format, publication, cellule] = cellules(l);
    const nom = video.match(LIEN_FICHE)[1];
    let date = null;
    const d = publication.match(/(\d{1,2})(?:er)?\s+([a-zéû]+)/i);
    const mois = d ? MOIS.findIndex(m => d[2].toLowerCase().startsWith(m)) : -1;
    if (mois >= 0) {
      const auj = new Date();
      if (annee === undefined) {
        annee = auj.getFullYear();
        const ecart = (new Date(annee, mois, +d[1]) - auj) / 864e5;
        if (ecart > 182) annee--; else if (ecart < -182) annee++;
      } else if (mois < moisPrec) annee++;
      moisPrec = mois;
      date = `${annee}-${String(mois + 1).padStart(2, '0')}-${d[1].padStart(2, '0')}`;
    }
    const s = cellule.match(RE_STATUT);
    const statut = s ? (s[2] === 'Publiée' ? 'Publié' : s[2]) : null;
    const dossier = `projets/${nom}/`;
    const siens = tous.filter(f => f.startsWith(dossier)).map(f => f.slice(dossier.length));
    return {
      nom, titre: video.match(/^\[(.+?)\]\(/)?.[1] ?? nom, format, publication, date,
      pilier: piliers[nom] ?? null, statut, etape: STATUTS.indexOf(statut),
      note: s ? cellule.slice(s[0].length).trim() : cellule,
      etapes: ETAPES.map(([etape, re]) => ({
        etape, fichier: siens.filter(f => re.test(f)).sort((a, b) => b.endsWith('.md') - a.endsWith('.md') || a.length - b.length || b.localeCompare(a))[0] ?? null,
      })),
      docs: siens.filter(f => f.endsWith('.md')).map(f => ({ chemin: dossier + f, ...compteCases(lire(dossier + f)) })),
    };
  });
}

// Remplace le statut en tête de la cellule et date le changement ; garde le reste de la note
function nouvelleCellule(cellule, statut) {
  const jour = new Date().toLocaleDateString('fr-FR', { day: '2-digit', month: '2-digit' });
  const s = cellule.match(RE_STATUT);
  if (!s) return `**${statut}** (${jour})${cellule ? ` · ${cellule}` : ''}`;
  const reste = cellule.slice(s[0].length);
  return `**${statut}**` + (/^ \(\d{1,2}\/\d{1,2}/.test(reste) ? reste.replace(/\d{1,2}\/\d{1,2}/, jour) : ` (${jour})${reste}`);
}

function majLigne(fichier, nom, statut) {
  const lignes = lire(fichier).split('\n');
  const i = lignes.findIndex(l => l.startsWith('|') && l.includes(`(projets/${nom}/fiche.md)`));
  if (i < 0) return false;
  const l = lignes[i].trimEnd(), fin = l.lastIndexOf('|'), debut = l.lastIndexOf('|', fin - 1);
  lignes[i] = `${l.slice(0, debut + 1)} ${nouvelleCellule(l.slice(debut + 1, fin).trim(), statut)} ${l.slice(fin)}`;
  fs.writeFileSync(chemin(fichier), lignes.join('\n'));
  return true;
}

function changerStatut({ nom, statut }) {
  if (!/^[\w-]+$/.test(nom ?? '') || !STATUTS.includes(statut)) throw erreur(400, 'Projet ou statut inconnu');
  if (!majLigne('README.md', nom, statut)) throw erreur(404, `projets/${nom} n'est pas dans le tableau du README`);
  // Le calendrier dit « Publiée » (la vidéo)
  const cal = majLigne('calendrier.md', nom, statut === 'Publié' ? 'Publiée' : statut);
  return { fichiers: cal ? ['README.md', 'calendrier.md'] : ['README.md'] };
}

function cocher({ chemin: rel, index, total, coche }) {
  if (typeof rel !== 'string' || !rel.endsWith('.md')) throw erreur(400, 'Fichier .md attendu');
  const lignes = lire(rel).split('\n');
  const idx = lignesCases(lignes);
  const i = idx[index];
  if (idx.length !== total || i === undefined || (lignes[i].match(RE_CASE)[2] !== ' ') === !!coche)
    throw erreur(409, `${rel} a changé entre-temps : la page se recharge, refais ton clic`);
  lignes[i] = lignes[i].replace(RE_CASE, `$1${coche ? 'x' : ' '}$3`);
  fs.writeFileSync(chemin(rel), lignes.join('\n'));
  return { ok: true };
}

function envoyerFichier(res, abs) {
  if (!fs.existsSync(abs) || !fs.statSync(abs).isFile()) throw erreur(404, 'Fichier introuvable');
  res.writeHead(200, { 'Content-Type': TYPES[path.extname(abs).toLowerCase()] ?? 'application/octet-stream', 'Cache-Control': 'no-store' });
  fs.createReadStream(abs).pipe(res);
}

// Le direct : chaque fichier modifié (par toi, par Claude ou par la page) est poussé aux pages ouvertes
const ecoutes = new Set();
fs.watch(ROOT, { recursive: true }, (_, f) => {
  if (!f || /(^|\/)(\.|node_modules\/|claude-youtube\/)/.test(f)) return;
  for (const res of ecoutes) res.write(`data: ${JSON.stringify(f)}\n\n`);
});

http.createServer(async (req, res) => {
  const repondre = (status, corps) => {
    res.writeHead(status, { 'Content-Type': typeof corps === 'string' ? 'text/plain; charset=utf-8' : 'application/json' });
    res.end(typeof corps === 'string' ? corps : JSON.stringify(corps));
  };
  // Seulement localhost : protège du « DNS rebinding » ; le JSON obligatoire bloque les formulaires d'autres sites
  if (!HOTES.has(req.headers.host) || (req.headers.origin && !HOTES.has(req.headers.origin.replace(/^https?:\/\//, ''))))
    return repondre(403, 'Origine refusée');
  const url = new URL(req.url, 'http://localhost');
  try {
    if (req.method === 'POST') {
      if (!req.headers['content-type']?.startsWith('application/json')) throw erreur(415, 'JSON attendu');
      let corps = '';
      for await (const morceau of req) corps += morceau;
      if (url.pathname === '/api/statut') return repondre(200, changerStatut(JSON.parse(corps)));
      if (url.pathname === '/api/case') return repondre(200, cocher(JSON.parse(corps)));
      throw erreur(404, 'Introuvable');
    }
    if (url.pathname === '/') return envoyerFichier(res, path.join(import.meta.dirname, 'index.html'));
    if (url.pathname === '/api/arbre') return repondre(200, fichiers().filter(f => f.endsWith('.md')));
    if (url.pathname === '/api/projets') return repondre(200, projets());
    if (url.pathname === '/api/direct') {
      res.writeHead(200, { 'Content-Type': 'text/event-stream', 'Cache-Control': 'no-store' });
      res.write(': ok\n\n');
      ecoutes.add(res);
      return req.on('close', () => ecoutes.delete(res));
    }
    if (url.pathname.startsWith('/raw/')) return envoyerFichier(res, chemin(decodeURIComponent(url.pathname.slice(5))));
    throw erreur(404, 'Introuvable');
  } catch (e) {
    repondre(e.status ?? 500, e.message);
  }
}).listen(PORT, '127.0.0.1', () => console.log(`La régie tourne : http://localhost:${PORT}`));
