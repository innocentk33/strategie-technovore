#!/usr/bin/env node
// La régie : lit les .md du dépôt et pilote le suivi des vidéos (statuts du README, cases à cocher).
// Lancement : node ressources/regie/regie.mjs [port], puis http://localhost:4321
import http from 'node:http';
import fs from 'node:fs';
import path from 'node:path';
import { createHash } from 'node:crypto';
import { createYouTube } from './youtube.mjs';
import { readYouTubeKey } from './config.mjs';

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
  ['sources', /^sources\.md$/], ['prompteur', /^teleprompteur\.(md|txt)$/], ['voix', /^[^/]+\.(m4a|wav)$/],
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

const versionSources = sources => createHash('sha256').update(JSON.stringify(sources)).digest('hex');
const sourcesSuivi = () => ({ readme: lire('README.md'), calendrier: lire('calendrier.md') });
const parisYear = () => Number(new Intl.DateTimeFormat('fr', { timeZone: 'Europe/Paris', year: 'numeric' }).format(new Date()));

// Les années viennent de l'en-tête explicite du calendrier ; aucun glissement selon la date du lancement.
function datesPublication(src, anneeInitiale) {
  let annee = anneeInitiale, moisPrec;
  const dates = new Map();
  for (const ligne of src.split('\n')) {
    if (!ligne.startsWith('|') || !LIEN_FICHE.test(ligne)) continue;
    const c = cellules(ligne), nom = ligne.match(LIEN_FICHE)[1];
    const texte = c.length > 4 ? c[1] : c[2];
    const d = texte.match(/(\d{1,2})(?:er)?\s+([a-zéû]+)\.?(?:\s+(20\d{2}))?/i);
    const mois = d ? MOIS.findIndex(m => d[2].toLowerCase().startsWith(m)) : -1;
    if (mois < 0) continue;
    if (d[3]) annee = Number(d[3]); else if (moisPrec !== undefined && mois < moisPrec) annee++;
    moisPrec = mois;
    const jour = Number(d[1]);
    if (new Date(Date.UTC(annee, mois, jour)).getUTCDate() !== jour) continue;
    dates.set(nom, `${annee}-${String(mois + 1).padStart(2, '0')}-${String(jour).padStart(2, '0')}`);
  }
  return dates;
}

function creneaux() {
  const src = lire('calendrier.md');
  const annee = Number(src.match(/^#.*?\b(20\d{2})\b/m)?.[1] ?? parisYear());
  const lignes = src.split('\n').filter(l => l.startsWith('|') && /^\d+$/.test(cellules(l)[0]) && !LIEN_FICHE.test(l));
  const enrichi = src.split('\n').map((l, i) => lignes.includes(l) ? l.replace(/\|([^|]*)\|([^|]*)\|([^|]*)\|/, `|$1|$2| [créneau](projets/creneau-${i}/fiche.md) |`) : l).join('\n');
  const dates = datesPublication(enrichi, annee);
  return src.split('\n').flatMap((l, i) => {
    if (!lignes.includes(l)) return [];
    const c = cellules(l), date = dates.get(`creneau-${i}`);
    return date ? [{ date, heure: '18:00', timezone: 'Europe/Paris', titre: c[2].replace(/\*/g, '') === 'Radar' ? 'Radar · sujet à choisir' : c[2].replace(/\*/g, ''), pilier: c[3] || null, note: c[6] || '' }] : [];
  });
}

function videoPublication(cellule, statut) {
  if (statut !== 'Publié') return null;
  // Une référence d'inspiration dans les notes n'associe jamais une vidéo au projet.
  const debut = cellule.split(/;| · /)[0];
  const m = debut.match(/:\s*\[[^\]]+\]\((https:\/\/[^)]+)\)/);
  if (!m) return null;
  try {
    const u = new URL(m[1]);
    const id = ['youtube.com', 'www.youtube.com', 'm.youtube.com'].includes(u.hostname) && u.pathname === '/watch' ? u.searchParams.get('v') : u.hostname === 'youtu.be' ? u.pathname.slice(1) : null;
    return /^[\w-]{11}$/.test(id ?? '') ? id : null;
  } catch { return null; }
}

function associationsYouTube() {
  const fichier = path.join(ROOT, '.regie-youtube.json');
  try {
    const data = JSON.parse(fs.readFileSync(fichier, 'utf8'));
    if (!data || typeof data !== 'object' || Array.isArray(data)) return {};
    return Object.fromEntries(Object.entries(data).filter(([nom, id]) => /^[\w-]+$/.test(nom) && typeof id === 'string' && /^[\w-]{11}$/.test(id)));
  } catch { return {}; }
}

function projets() {
  const tous = fichiers(), sources = sourcesSuivi(), version = versionSources(sources), associations = associationsYouTube();
  const annee = Number(sources.calendrier.match(/^#.*?\b(20\d{2})\b/m)?.[1] ?? sources.readme.match(/^#.*?\b(20\d{2})\b/m)?.[1] ?? parisYear());
  const dates = datesPublication(sources.calendrier, annee);
  const datesREADME = datesPublication(sources.readme, annee);
  const piliers = {};
  for (const l of sources.calendrier.split('\n')) {
    const m = l.startsWith('|') && l.match(LIEN_FICHE);
    if (m && !(m[1] in piliers)) piliers[m[1]] = cellules(l)[3]?.split(' ')[0];
  }
  return sources.readme.split('\n').filter(l => l.startsWith('|') && LIEN_FICHE.test(l)).map(l => {
    const [video, format, publication, cellule] = cellules(l);
    const nom = video.match(LIEN_FICHE)[1];
    const s = cellule.match(RE_STATUT);
    const statut = s ? (s[2] === 'Publiée' ? 'Publié' : s[2]) : null;
    const dossier = `projets/${nom}/`;
    const siens = tous.filter(f => f.startsWith(dossier)).map(f => f.slice(dossier.length));
    const images = siens.filter(f => {
      const normalise = f.normalize('NFD').replace(/\p{M}/gu, '').toLowerCase();
      if (/(?:^|[\/_. -])(?:refs?|references?|apercus?|planches?|hotes?|sources?|assets?)(?:[\/_. -]|$)/.test(normalise)) return false;
      return /^miniatures?\/rendus\/[^/]+\.(png|jpe?g|webp)$/i.test(f) || /^miniature\.(png|jpe?g|webp)$/i.test(f);
    }).sort((a, b) => Number(!a.includes('/rendus/')) - Number(!b.includes('/rendus/')) || a.localeCompare(b, 'en'));
    const heure = publication.match(/(?:^|[, ])(\d{1,2})\s*h(?:\s*(\d{2}))?/i);
    return {
      nom, titre: video.match(/^\[(.+?)\]\(/)?.[1] ?? nom, format, publication,
      date: dates.get(nom) ?? datesREADME.get(nom) ?? null,
      heure: heure && Number(heure[1]) < 24 && Number(heure[2] ?? 0) < 60 ? `${heure[1].padStart(2, '0')}:${heure[2] ?? '00'}` : null,
      timezone: 'Europe/Paris', version, thumbnail: images[0] ? dossier + images[0] : null,
      thumbnailVariants: images.map(f => {
        const name = path.basename(f, path.extname(f));
        const key = name.match(/^([a-z])(?:$|[-_])/i)?.[1].toLowerCase() ?? name.toLowerCase();
        return { key, label: key.length === 1 ? `Variante ${key.toUpperCase()}` : name, name, path: dossier + f };
      }),
      youtubeVideoId: Object.hasOwn(associations, nom) ? associations[nom] : videoPublication(cellule, statut),
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
  const jour = new Date().toLocaleDateString('fr-FR', { day: '2-digit', month: '2-digit', timeZone: 'Europe/Paris' });
  const s = cellule.match(RE_STATUT);
  if (!s) return `**${statut}** (${jour})${cellule ? ` · ${cellule}` : ''}`;
  const reste = cellule.slice(s[0].length);
  return `**${statut}**` + (/^ \(\d{1,2}\/\d{1,2}/.test(reste) ? reste.replace(/\d{1,2}\/\d{1,2}/, jour) : ` (${jour})${reste}`);
}

function majLigne(src, nom, statut) {
  const lignes = src.split('\n');
  const i = lignes.findIndex(l => l.startsWith('|') && l.includes(`(projets/${nom}/fiche.md)`));
  if (i < 0) return null;
  // Garde le « \r » des fichiers en CRLF (checkout Windows) pour ne pas mélanger les fins de ligne
  const cr = lignes[i].endsWith('\r') ? '\r' : '';
  const l = lignes[i].trimEnd(), fin = l.lastIndexOf('|'), debut = l.lastIndexOf('|', fin - 1);
  lignes[i] = `${l.slice(0, debut + 1)} ${nouvelleCellule(l.slice(debut + 1, fin).trim(), statut)} ${l.slice(fin)}${cr}`;
  return lignes.join('\n');
}

function changerStatut({ nom, statut, version }) {
  if (!/^[\w-]+$/.test(nom ?? '') || !STATUTS.includes(statut)) throw erreur(400, 'Projet ou statut inconnu');
  const avant = sourcesSuivi();
  if (typeof version !== 'string' || version !== versionSources(avant)) throw erreur(409, 'Le suivi a changé : actualise avant de changer le statut');
  const readme = majLigne(avant.readme, nom, statut);
  if (readme === null) throw erreur(404, `projets/${nom} n'est pas dans le tableau du README`);
  const calendrier = majLigne(avant.calendrier, nom, statut === 'Publié' ? 'Publiée' : statut);
  const changements = [['README.md', readme, avant.readme], ...(calendrier === null ? [] : [['calendrier.md', calendrier, avant.calendrier]])];
  // Prépare les deux fichiers avant remplacement ; aucune attente entre contrôle et écriture.
  const prepares = [];
  try {
    for (const [fichier, contenu] of changements) {
      const temporaire = path.join(ROOT, `.regie-${path.basename(fichier)}-${process.pid}`);
      fs.writeFileSync(temporaire, contenu, { flag: 'wx', mode: fs.statSync(chemin(fichier)).mode });
      prepares.push(temporaire);
    }
    if (version !== versionSources(sourcesSuivi())) throw erreur(409, 'Le suivi a changé : actualise avant de changer le statut');
    let ecrits = 0;
    try {
      for (let i = 0; i < changements.length; i++) { fs.renameSync(prepares[i], chemin(changements[i][0])); ecrits++; }
    } catch (e) {
      for (let i = 0; i < ecrits; i++) fs.writeFileSync(chemin(changements[i][0]), changements[i][2]);
      throw e;
    }
  } finally { for (const temporaire of prepares) fs.rmSync(temporaire, { force: true }); }
  return { fichiers: changements.map(c => c[0]), version: versionSources(sourcesSuivi()) };
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
const youtube = createYouTube({ key: readYouTubeKey(ROOT) });
const youtubeData = force => youtube.get(projets().map(p => p.youtubeVideoId).filter(Boolean), { force });
const ecoutes = new Set();
fs.watch(ROOT, { recursive: true }, (_, brut) => {
  // Sous Windows, fs.watch donne « projets\uber\fiche.md » : la page attend des « / »
  const f = brut?.split(path.sep).join('/');
  if (!f ||/(^|\/)(\.|node_modules\/|claude-youtube\/)/.test(f)) return;
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
      if (url.pathname === '/api/youtube/refresh') { JSON.parse(corps); return repondre(200, await youtubeData(true)); }
      if (url.pathname === '/api/statut') return repondre(200, changerStatut(JSON.parse(corps)));
      if (url.pathname === '/api/case') return repondre(200, cocher(JSON.parse(corps)));
      throw erreur(404, 'Introuvable');
    }
    if (url.pathname === '/') return envoyerFichier(res, path.join(import.meta.dirname, 'index.html'));
    if (url.pathname === '/api/arbre') return repondre(200, fichiers().filter(f => f.endsWith('.md')));
    if (url.pathname === '/api/calendrier') return repondre(200, creneaux());
    if (url.pathname === '/api/youtube') return repondre(200, await youtubeData(false));
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
