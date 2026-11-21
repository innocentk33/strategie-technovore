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
ecrire('calendrier.md', '# Calendrier 2026 → 2027\n| # | Lundi | Vidéo | Pilier | Format | Charge | Statut |\n| 1 | 26 oct | [Uber](projets/uber/fiche.md) | Génie | — | — | Fiche |\n');
ecrire('projets/uber/fiche.md', '# Uber');
ecrire('projets/uber/etapes.md', '- [ ] un\n```\n- [ ] dans le code\n```\n> - [x] deux\n');
ecrire('projets/waze/fiche.md', '# Waze');
ecrire('projets/uber/teleprompteur.txt', 'Texte');
ecrire('projets/uber/miniature/rendus/b.webp', 'image');
ecrire('projets/uber/miniature/rendus/a.png', 'image');
ecrire('projets/uber/miniature/rendus/00-apercu.png', 'planche');
ecrire('projets/uber/miniature/rendus/00-planche.png', 'planche');
ecrire('projets/uber/miniature/refs/00-ref.png', 'concurrent');
ecrire('projets/uber/miniature/00-photo-telephone.png', 'photo');
ecrire('projets/uber/miniature.png', 'repli');
ecrire('projets/waze/miniature/refs/00-ref.png', 'concurrent');
ecrire('projets/waze/miniature/rendus/apercu.png', 'planche');
ecrire('projets/waze/miniature/00-photo-telephone.png', 'photo');

const port = 4400 + Math.floor(Math.random() * 500);
const serveur = spawn(process.execPath, [path.join(import.meta.dirname, 'regie.mjs'), port], { env: { ...process.env, REGIE_DEPOT: depot, YOUTUBE_API_KEY: '' } });
await new Promise((ok, non) => { serveur.stdout.once('data', ok); serveur.once('error', non); serveur.once('exit', code => non(new Error(`Serveur de test arrêté (${code}) : autorise l'écoute localhost.`))); });
const postBrut = (url, corps) => fetch(`http://localhost:${port}${url}`, { method: 'POST', headers: { 'Content-Type': 'application/json' }, body: JSON.stringify(corps) });
const charger = async () => (await fetch(`http://localhost:${port}/api/projets`)).json();
const post = async (url, corps) => postBrut(url, url === '/api/statut' ? { ...corps, version: (await charger())[0].version } : corps);
const lire = f => fs.readFileSync(path.join(depot, f), 'utf8');
const jour = new Date().toLocaleDateString('fr-FR', { day: '2-digit', month: '2-digit', timeZone: 'Europe/Paris' });

try {
  const projets = await (await fetch(`http://localhost:${port}/api/projets`)).json();
  assert.deepEqual(projets.map(p => [p.nom, p.statut, p.date, p.pilier]), [['uber', 'Script', projets[0].date, 'Génie'], ['waze', 'Brouillon', projets[1].date, null]]);
  assert.equal(projets[0].date, '2026-10-26');
  assert.equal(projets[1].date, '2027-01-04');
  assert.equal(projets[0].heure, '18:00');
  assert.equal(projets[0].thumbnail, 'projets/uber/miniature/rendus/a.png');
  assert.deepEqual(projets[0].thumbnailVariants.map(v => [v.key, v.path]), [
    ['a', 'projets/uber/miniature/rendus/a.png'],
    ['b', 'projets/uber/miniature/rendus/b.webp'],
    ['miniature', 'projets/uber/miniature.png'],
  ], 'les variantes exposent uniquement les rendus admissibles du projet');
  assert.deepEqual(projets[1].thumbnailVariants, []);
  assert.equal(projets[1].thumbnail, null, 'aucune référence ou planche utilisée comme miniature');
  assert.equal(projets[0].etapes.find(e => e.etape === 'prompteur').fichier, 'teleprompteur.txt');
  assert.ok(projets[1].date > projets[0].date, 'janvier passe à l\'année suivante');
  assert.deepEqual(projets[0].docs.find(d => d.chemin.endsWith('etapes.md')), { chemin: 'projets/uber/etapes.md', fait: 1, total: 2 });

  ecrire('projets/waze/miniature.jpg', 'repli explicite');
  assert.equal((await charger())[1].thumbnail, 'projets/waze/miniature.jpg');
  const avant = { readme: lire('README.md'), calendrier: lire('calendrier.md') };
  assert.equal((await postBrut('/api/statut', { nom: 'uber', statut: 'Voix' })).status, 409, 'version obligatoire');
  ecrire('calendrier.md', avant.calendrier + '\nNote extérieure');
  assert.equal((await postBrut('/api/statut', { nom: 'uber', statut: 'Voix', version: projets[0].version })).status, 409);
  assert.equal(lire('README.md'), avant.readme, 'conflit sans écriture partielle');
  assert.ok(lire('calendrier.md').endsWith('Note extérieure'));
  const obstacle = path.join(depot, `.regie-calendrier.md-${serveur.pid}`);
  fs.mkdirSync(obstacle);
  assert.equal((await post('/api/statut', { nom: 'uber', statut: 'Voix' })).status, 500, 'préparation calendrier impossible');
  assert.equal(lire('README.md'), avant.readme, 'préparation échouée : README intact');
  assert.ok(lire('calendrier.md').endsWith('Note extérieure'));
  fs.rmdirSync(obstacle);
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
  const youtube = await (await fetch(`http://localhost:${port}/api/youtube`)).json();
  assert.equal(youtube.configured, false);
  assert.equal(youtube.fetchedAt, null);
  assert.deepEqual(youtube.videos, {});
  assert.match(youtube.error, /non configurée/);
  assert.equal((await post('/api/youtube/refresh', {})).status, 200);
  // Les liens d'inspiration ne deviennent pas l'identifiant d'une publication.
  ecrire('README.md', lire('README.md') + '\n| [Inspiré](projets/inspire/fiche.md) | Longue | 5 janv., 18 h | **Publié** : inspirée de [autre](https://youtu.be/abcdefghijk) |');
  ecrire('projets/inspire/fiche.md', '# Inspiré');
  assert.equal((await charger()).find(p => p.nom === 'inspire').youtubeVideoId, null);
  ecrire('README.md', lire('README.md').replace('**Publié** : inspirée de [autre]', '**Publié** : [autre]'));
  assert.equal((await charger()).find(p => p.nom === 'inspire').youtubeVideoId, 'abcdefghijk');
  ecrire('.regie-youtube.json', JSON.stringify({ uber: 'zyxwvutsrqp', inspire: 'bad', '../waze': 'abcdefghijk', waze: 123 }));
  const associes = await charger();
  assert.equal(associes.find(p => p.nom === 'uber').youtubeVideoId, 'zyxwvutsrqp');
  assert.equal(associes.find(p => p.nom === 'inspire').youtubeVideoId, 'abcdefghijk', 'association invalide ignorée, lien README conservé');
  assert.equal(associes.find(p => p.nom === 'waze').youtubeVideoId, null);
  ecrire('.regie-youtube.json', JSON.stringify({ inspire: 'zyxwvutsrqp' }));
  assert.equal((await charger()).find(p => p.nom === 'inspire').youtubeVideoId, 'zyxwvutsrqp', 'association manuelle prioritaire');
  ecrire('.regie-youtube.json', '{malformé');
  assert.equal((await charger()).find(p => p.nom === 'inspire').youtubeVideoId, 'abcdefghijk');
  ecrire('calendrier.md', lire('calendrier.md') + '\n| 2 | lun. 4 janv | *Radar* | IA | | | À choisir |');
  const creneaux = await (await fetch(`http://localhost:${port}/api/calendrier`)).json();
  assert.equal(creneaux[0].date, '2027-01-04');
  const suivis = await charger();
  const versionDate = suivis[0].version;
  assert.equal((await postBrut('/api/date', { nom: 'uber', date: '2027-02-31', version: versionDate })).status, 400);
  assert.equal((await postBrut('/api/date', { nom: 'uber', date: '2027-02-01', version: 'périmée' })).status, 409);
  assert.equal((await postBrut('/api/date', { nom: 'uber', date: '2027-02-01', version: versionDate })).status, 200);
  const deplaces = await charger();
  assert.equal(deplaces[0].date, '2027-02-01');
  assert.equal(deplaces[0].heure, '18:00');
  assert.equal(deplaces[0].statut, 'Publié');
  assert.equal(deplaces[0].note, suivis[0].note);
  assert.equal(deplaces[1].date, suivis[1].date, 'l’année des lignes suivantes du README est préservée');
  assert.equal((await (await fetch(`http://localhost:${port}/api/calendrier`)).json())[0].date, '2027-01-04', 'le créneau Radar garde son année');
  assert.match(lire('calendrier.md'), /Mis à jour le/);
  assert.equal((await postBrut('/api/date', { nom: 'waze', date: '2026-12-15', version: deplaces[0].version })).status, 200);
  assert.match(lire('calendrier.md'), /^\| 3 \| [^|]*15 déc\. 2026 \| \[Waze\]/m);
  const planifies = await charger();
  assert.equal(planifies[1].date, '2026-12-15');
  assert.equal(planifies[2].date, suivis[2].date, 'la date du projet suivant reste la même');
  const readmeAvantRadar = lire('README.md');
  const [radar] = await (await fetch(`http://localhost:${port}/api/calendrier`)).json();
  assert.equal(radar.creneau, '2');
  assert.equal((await postBrut('/api/date', { creneau: '3', date: '2027-03-03', version: radar.version })).status, 404);
  const mouvement = await postBrut('/api/date', { creneau: radar.creneau, date: '2027-03-03', version: radar.version });
  assert.equal(mouvement.status, 200);
  assert.deepEqual((await mouvement.json()).fichiers, ['calendrier.md']);
  assert.equal(lire('README.md'), readmeAvantRadar);
  const [radarDeplace] = await (await fetch(`http://localhost:${port}/api/calendrier`)).json();
  assert.deepEqual(radarDeplace, { ...radar, date: '2027-03-03', version: radarDeplace.version });
  assert.deepEqual((await charger()).map(p => p.date), planifies.map(p => p.date));
  console.log('La régie : tout est bon');
} finally {
  serveur.kill();
  fs.rmSync(depot, { recursive: true });
}
