<!-- Modèle (origine de chaque variable : ../sous-agents.md, « D’où viennent les variables »). Remplace : {{TITRE}}, {{PROJET}}, {{DEPOT_PROJET}} (<DEPOT>/projets/<nom>), {{VERSIONS}} (description de chaque version clonée, durée, défauts connus), {{CHUTES}} (phrases-chutes du script), {{CHIFFRES}} (liste des prix, chiffres et références de cartes à vérifier), {{SCRATCH}}. Exemple réel : exemples/brief-voix-32go.md. Modèle : Opus. -->
Tu montes la voix off d'une vidéo YouTube française de la chaîne Technovore : « {{TITRE}} ». Réponds en français. Ne commite rien. Ne touche à rien hors du projet et de `{{SCRATCH}}`.

## Projet
- Dossier : `{{PROJET}}/` (lance tout depuis cette racine).
- **La voix est une voix clonée** (VoiceStudio / OmniVoice, voix de l'auteur) : {{VERSIONS}}. Comme c'est une synthèse, des passages peuvent sonner bizarres (prononciation ratée, mot sauté ou répété, son parasite, claquement de bouche, rire ou soupir qui sonne faux).
- Texte attendu : `sources/teleprompteur.txt`. Texte envoyé au moteur (nombres en lettres, liaisons, balises) : `{{DEPOT_PROJET}}/voicestudio-stories.txt` et ses notes `voicestudio.md` ; garde un `[sigh]` ou un `[laughter]` seulement s'il sonne naturel.
- **La méthode existe** : lis en entier l'en-tête de `scripts/voix.py` (deux sources, PSOLA, gains, fond commun, micro-pauses) et suis l'ordre `w2v_transcrire.py (chaque version) → prises.py → choix_prises.py → strata_psola.py → voix.py → verif_sources.py (→ cale_gains.py / cale_hauteur.py, et on recommence)`. torch et parselmouth ne sont dans aucun Python : `uv run --no-project --with torch --with transformers --with numpy python …` et `uv run --no-project --with praat-parselmouth --with numpy python …`, en arrière-plan pour les longs. Remesure planchers et seuils (une synthèse n'a presque pas de bruit de fond : pas de trou numérique, pas d'effet de porte).

## Ce que l'auteur demande
1. **La meilleure prise de chaque phrase** : par défaut la version la plus fidèle ; l'autre quand un mot y est coupé, avalé, déformé ou un chiffre changé. Change de source entre deux phrases et vérifie par mesure que ça ne s'entend pas (niveau, hauteur, débit, timbre). Hauteur seulement par PSOLA (formants gardés), jamais `asetrate` ; accélération ×1,25 au plus.
2. **Aucun raté** (mot doublé, sauté, tranché, débris, clic, bruit, blanc > 0,8 s), vérifié en verbatim wav2vec2. **Un chiffre ou un prix changé est corrigé** (greffe depuis l'autre version) ou signalé. À vérifier un par un : {{CHIFFRES}}.
3. **Micro-pauses** (silence = fond de la même source) : 0,15-0,3 s sur les virgules et deux-points porteurs de sens, 0,35-0,5 s entre les phrases, 0,6-0,8 s aux changements de partie (titres `###` du script), un petit temps avant les chutes ({{CHUTES}}). Jamais plus de 0,8 s. Liste dans `edit-plan/voice-pauses.json`.
4. Débit naturel et dynamique, environ 165-185 mots/min hors pauses.

## Sorties
`assets/audio/voix.flac` (48 kHz), `sources/voix-avant-master.flac`, `sources/voix.words.json`, `sources/voix.phrases.json` (une entrée par phrase avec `section`), `edit-plan/voice-keep.json`, `voice-cuts.json`, `voice-map.json`, `voice-pauses.json`, `voice-report.json`, `renders/controle-raccords.m4a` (+ .txt). Relance wav2vec2 sur la voix finale et vérifie-toi (`verif_texte.py`, `verif_voix.py`, `verif_sources.py`).

## Ta réponse finale (courte)
Durée, LUFS et crête, nombre de raccords et de changements de source, phrases sans prise propre (temps dans chaque source), chiffres corrigés ou douteux, sort du soupir et du rire, points dont tu doutes (temps dans la voix finale).
