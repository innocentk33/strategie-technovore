// Métadonnées publiques seulement. Clé exclusivement serveur, aucune recherche de vidéos.
const TTL = 24 * 60 * 60 * 1000;
const RETRY = 60 * 1000;
const MAX_STALE = 30 * TTL;
const compteur = value => value === undefined || value === null || !/^\d+$/.test(String(value)) ? null : Number(value);

export function createYouTube({ key = process.env.YOUTUBE_API_KEY, fetchImpl = globalThis.fetch, now = () => Date.now(), ttl = TTL, timeout = 8000 } = {}) {
  let cache = { configured: Boolean(key), fetchedAt: null, videos: {} }, signature = '', checkedAt = null, pending = null;
  async function charger(ids) {
    const videos = {};
    try {
      for (let i = 0; i < ids.length; i += 50) {
        const url = new URL('https://www.googleapis.com/youtube/v3/videos');
        url.search = new URLSearchParams({ part: 'snippet,contentDetails,statistics', id: ids.slice(i, i + 50).join(','), key }).toString();
        const response = await fetchImpl(url, { signal: AbortSignal.timeout(timeout) });
        if (!response.ok) {
          let reason;
          try { reason = (await response.json()).error?.errors?.[0]?.reason; } catch {}
          throw new Error(reason === 'quotaExceeded' || reason === 'dailyLimitExceeded' ? 'Quota YouTube épuisé.' : `YouTube indisponible (HTTP ${response.status}).`);
        }
        const data = await response.json();
        if (!Array.isArray(data.items)) throw new Error('Réponse YouTube invalide.');
        for (const item of data.items) {
          if (!ids.includes(item.id)) continue;
          const snippet = item.snippet ?? {}, stats = item.statistics ?? {}, thumbs = snippet.thumbnails ?? {};
          videos[item.id] = { title: snippet.title ?? null, thumbnail: thumbs.maxres?.url ?? thumbs.high?.url ?? thumbs.medium?.url ?? thumbs.default?.url ?? null,
            duration: item.contentDetails?.duration ?? null, publishedAt: snippet.publishedAt ?? null,
            views: compteur(stats.viewCount), likes: compteur(stats.likeCount), comments: compteur(stats.commentCount) };
        }
      }
      cache = { configured: true, fetchedAt: new Date(now()).toISOString(), videos };
    } catch (e) {
      // Ne jamais exposer l'URL, la clé ni les messages réseau arbitraires.
      const message = e.name === 'TimeoutError' || e.name === 'AbortError' ? 'Délai YouTube dépassé.' : /^(Quota YouTube|YouTube indisponible|Réponse YouTube)/.test(e.message) ? e.message : 'Connexion YouTube indisponible.';
      cache = { ...cache, configured: true, error: message };
    }
    checkedAt = now();
    return cache;
  }
  return { async get(input, { force = false } = {}) {
    if (!key) return { configured: false, fetchedAt: null, videos: {}, error: 'YOUTUBE_API_KEY non configurée sur le serveur.' };
    const ids = [...new Set(input.filter(id => /^[\w-]{11}$/.test(id)))].sort();
    const nextSignature = ids.join(',');
    if (pending) { await pending; return this.get(ids, { force: false }); }
    if (signature !== nextSignature) { cache = { configured: true, fetchedAt: null, videos: {} }; checkedAt = null; }
    if (cache.fetchedAt && now() - Date.parse(cache.fetchedAt) > MAX_STALE) cache = { ...cache, fetchedAt: null, videos: {} };
    if (!force && checkedAt !== null && now() - checkedAt < (cache.error ? RETRY : ttl)) return cache;
    signature = nextSignature;
    pending = charger(ids);
    try { return await pending; } finally { pending = null; }
  } };
}
