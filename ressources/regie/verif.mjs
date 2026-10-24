// Vérifie les écritures de la régie sur un faux dépôt : node ressources/regie/verif.mjs
import { spawn } from 'node:child_process';
import fs from 'node:fs';
import os from 'node:os';
import path from 'node:path';
import assert from 'node:assert/strict';

const depot = fs.mkdtempSync(path.join(os.tmpdir(), 'regie-'));
const ecrire = (f, s) => { fs.mkdirSync(path.dirname(path.join(depot, f)), { recursive: true }); fs.writeFileSync(path.join(depot, f), s); };
ecrire('README.md', [
  '| Projet | Format | Publication | Statut |', '|---|---|---|---|',
  '| [Uber](projets/uber/fiche.md) | Longue | lun. 26 oct., 18 h | **Script** (23/10) : [final](projets/uber/script.md) |',
  '| [Waze](projets/waze/fiche.md) | Longue | lun. 4 janv., 18 h | Brouillon · essais |',
].join('\n'));
ecrire('calendrier.md', '| # | Lundi | Vidéo | Pilier | Format | Charge | Statut |\n| 1 | 26 oct | [Uber](projets/uber/fiche.md) | Génie | — | — | Fiche |\n');
ecrire('projets/uber/fiche.md', '# Uber');
ecrire('projets/uber/etapes.md', '- [ ] un\n```\n- [ ] dans le code\n```\n> - [x] deux\n');
ecrire('projets/waze/fiche.md', '# Waze');

const port = 4400 + Math.floor(Math.random() * 500);
const serveur = spawn(process.execPath, [path.join(import.meta.dirname, 'regie.mjs'), port], { env: { ...process.env, REGIE_DEPOT: depot } });
await new Promise(ok => serveur.stdout.once('data', ok));
const post = (url, corps) => fetch(`http://localhost:${port}${url}`, { method: 'POST', headers: { 'Content-Type': 'application/json' }, body: JSON.stringify(corps) });
const lire = f => fs.readFileSync(path.join(depot, f), 'utf8');
const jour = new Date().toLocaleDateString('fr-FR', { day: '2-digit', month: '2-digit' });

try {
  const projets = await (await fetch(`http://localhost:${port}/api/projets`)).json();
  assert.deepEqual(projets.map(p => [p.nom, p.statut, p.date, p.pilier]), [['uber', 'Script', projets[0].date, 'Génie'], ['waze', 'Brouillon', projets[1].date, null]]);
  assert.ok(projets[1].date > projets[0].date, 'janvier passe à l\'année suivante');
  assert.deepEqual(projets[0].docs.find(d => d.chemin.endsWith('etapes.md')), { chemin: 'projets/uber/etapes.md', fait: 1, total: 2 });

  assert.equal((await post('/api/statut', { nom: 'uber', statut: 'Voix' })).status, 200);
  assert.match(lire('README.md'), new RegExp(`\\| \\*\\*Voix\\*\\* \\(${jour}\\) : \\[final\\]\\(projets/uber/script\\.md\\) \\|`));
  assert.match(lire('calendrier.md'), new RegExp(`\\| Génie \\| — \\| — \\| \\*\\*Voix\\*\\* \\(${jour}\\) \\|`));
  await post('/api/statut', { nom: 'waze', statut: 'Script' });
  assert.match(lire('README.md'), new RegExp(`\\| \\*\\*Script\\*\\* \\(${jour}\\) · essais \\|$`));
  await post('/api/statut', { nom: 'uber', statut: 'Publié' });
  assert.match(lire('calendrier.md'), /\*\*Publiée\*\*/);
  assert.equal((await post('/api/statut', { nom: 'uber', statut: 'Fini' })).status, 400);
  assert.equal((await post('/api/statut', { nom: 'inconnu', statut: 'Voix' })).status, 404);

  assert.equal((await post('/api/case', { chemin: 'projets/uber/etapes.md', index: 1, total: 2, coche: false })).status, 200);
  assert.equal(lire('projets/uber/etapes.md'), '- [ ] un\n```\n- [ ] dans le code\n```\n> - [ ] deux\n');
  assert.equal((await post('/api/case', { chemin: 'projets/uber/etapes.md', index: 1, total: 2, coche: false })).status, 409, 'déjà décochée');
  assert.equal((await post('/api/case', { chemin: 'projets/uber/etapes.md', index: 0, total: 3, coche: true })).status, 409, 'le fichier a changé');
  assert.equal((await post('/api/case', { chemin: '../etapes.md', index: 0, total: 1, coche: true })).status, 403);
  console.log('La régie : tout est bon');
} finally {
  serveur.kill();
  fs.rmSync(depot, { recursive: true });
}
