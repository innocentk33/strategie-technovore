import fs from 'node:fs';
import path from 'node:path';
import { parseEnv } from 'node:util';

// Ne charge que la clé attendue, sans modifier les autres variables du processus.
export function readYouTubeKey(root, env = process.env) {
  if (Object.hasOwn(env, 'YOUTUBE_API_KEY')) return env.YOUTUBE_API_KEY.trim();
  try {
    return (parseEnv(fs.readFileSync(path.join(root, '.env.local'), 'utf8')).YOUTUBE_API_KEY ?? '').trim();
  } catch (error) {
    if (error.code === 'ENOENT') return '';
    // Ne jamais recopier le contenu du fichier ni un message contenant un secret.
    throw new Error('Impossible de lire .env.local : vérifie son format et ses permissions.');
  }
}
