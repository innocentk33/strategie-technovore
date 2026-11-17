import { test } from 'node:test';
import assert from 'node:assert/strict';
import fs from 'node:fs';
import os from 'node:os';
import path from 'node:path';
import { readYouTubeKey } from './config.mjs';

test('configuration locale facultative, syntaxe env et priorité environnement', () => {
  const root = fs.mkdtempSync(path.join(os.tmpdir(), 'regie-config-'));
  try {
    assert.equal(readYouTubeKey(root, {}), '');
    fs.writeFileSync(path.join(root, '.env.local'), '# clé de test factice\nYOUTUBE_API_KEY="test-local"\nPORT=9999\n');
    const env = {};
    assert.equal(readYouTubeKey(root, env), 'test-local');
    assert.deepEqual(env, {}, 'aucune autre variable importée');
    assert.equal(readYouTubeKey(root, { YOUTUBE_API_KEY: 'test-env' }), 'test-env');
    assert.equal(readYouTubeKey(root, { YOUTUBE_API_KEY: '' }), '', 'clé explicitement vide désactive la connexion');
  } finally { fs.rmSync(root, { recursive: true }); }
});

test('erreur de lecture sans exposition de contenu', () => {
  const root = fs.mkdtempSync(path.join(os.tmpdir(), 'regie-config-'));
  try {
    fs.mkdirSync(path.join(root, '.env.local'));
    assert.throws(() => readYouTubeKey(root, {}), /^Error: Impossible de lire \.env\.local/);
  } finally { fs.rmSync(root, { recursive: true }); }
});
