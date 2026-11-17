import assert from 'node:assert/strict';
import test from 'node:test';
import { createYouTube } from './youtube.mjs';
const id = 'abcdefghijk';
const response = { ok: true, json: async () => ({ items: [{ id, snippet: { title: 'Vidéo', publishedAt: '2026-11-16T17:00:00Z', thumbnails: { high: { url: 'https://example.org/image.jpg' } } }, contentDetails: { duration: 'PT9M35S' }, statistics: { viewCount: '0', likeCount: '24' } }] }) };

test('aucune clé : aucun réseau, indisponibilité explicite', async () => {
  let calls = 0;
  const yt = createYouTube({ key: '', fetchImpl: () => { calls++; throw new Error(); } });
  assert.deepEqual((await yt.get([id])).videos, {});
  assert.equal((await yt.get([id], { force: true })).configured, false);
  assert.equal(calls, 0);
});

test('cache quotidien, refresh, champs absents distincts de zéro', async () => {
  let calls = 0, time = 0;
  const yt = createYouTube({ key: 'secret-test', now: () => time, fetchImpl: async (url, options) => { calls++; assert.equal(url.searchParams.get('id'), id); assert.ok(options.signal); return response; } });
  const data = await yt.get([id, id, 'invalide']);
  assert.equal(data.videos[id].views, 0);
  assert.equal(data.videos[id].comments, null);
  assert.equal(data.videos[id].duration, 'PT9M35S');
  await yt.get([id]); assert.equal(calls, 1);
  time += 24 * 60 * 60 * 1000;
  await yt.get([id]); assert.equal(calls, 2);
  await yt.get([id], { force: true }); assert.equal(calls, 3);
});

test('lots groupés et identifiants absents non inventés', async () => {
  const ids = Array.from({ length: 51 }, (_, i) => String(i).padStart(11, '0'));
  let calls = 0;
  const yt = createYouTube({ key: 'test', fetchImpl: async url => { calls++; assert.ok(url.searchParams.get('id').split(',').length <= 50); return { ok: true, json: async () => ({ items: [] }) }; } });
  assert.deepEqual((await yt.get(ids)).videos, {});
  assert.equal(calls, 2);
});

test('quota épuisé et erreurs API sans fuite de clé', async () => {
  let fail = false;
  const yt = createYouTube({ key: 'secret-test', fetchImpl: async () => fail ? { ok: false, status: 403, json: async () => ({ error: { errors: [{ reason: 'quotaExceeded' }] } }) } : response });
  const good = await yt.get([id]);
  fail = true;
  const failed = await yt.get([id], { force: true });
  assert.match(failed.error, /Quota/);
  assert.equal(failed.fetchedAt, good.fetchedAt);
  assert.equal(failed.videos[id].views, 0, 'dernières données conservées et horodatées');
  assert.ok(!JSON.stringify(failed).includes('secret-test'));
  const network = createYouTube({ key: 'secret-test', fetchImpl: async () => { throw new Error('https://example.org/?key=secret-test'); } });
  assert.equal((await network.get([id])).error, 'Connexion YouTube indisponible.');
  const invalid = createYouTube({ key: 'test', fetchImpl: async () => ({ ok: true, json: async () => ({}) }) });
  assert.match((await invalid.get([id])).error, /invalide/);
});

test('timeout explicite et appels simultanés regroupés', async () => {
  const timeout = createYouTube({ key: 'test', fetchImpl: async () => { throw Object.assign(new Error(), { name: 'TimeoutError' }); } });
  assert.match((await timeout.get([id])).error, /Délai/);
  let calls = 0;
  const yt = createYouTube({ key: 'test', fetchImpl: async () => { calls++; return response; } });
  await Promise.all([yt.get([id]), yt.get([id])]);
  assert.equal(calls, 1);
});


test('erreur réessayée après une minute, données périmées retirées après trente jours', async () => {
  let time = 0, calls = 0, fail = false;
  const yt = createYouTube({ key: 'test', now: () => time, fetchImpl: async () => {
    calls++;
    if (fail) throw new Error('réseau absent');
    return response;
  } });
  await yt.get([id]); fail = true;
  await yt.get([id], { force: true });
  assert.equal(calls, 2);
  time += 59000;
  await yt.get([id]); assert.equal(calls, 2);
  time += 1000;
  await yt.get([id]); assert.equal(calls, 3);
  time = 31 * 24 * 60 * 60 * 1000;
  const old = await yt.get([id]);
  assert.deepEqual(old.videos, {});
  assert.equal(old.fetchedAt, null);
  assert.ok(old.error);
});
