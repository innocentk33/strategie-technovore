# Voix : sa vraie voix (prise brute)

L'auteur enregistre d'une traite, avec plusieurs essais pour beaucoup de phrases, des faux départs et un peu d'improvisation. Il **ne refait aucune prise** : tout se règle au montage. Méthode éprouvée sur Strata (15/11), « Même carte » (18/11) et « Qwen 27B sur 8 Go » (19/11). Le script de référence est `2026-11-qwen-27b-8go/scripts/voix.py` : **lis son en-tête en entier**, il contient l'historique des réglages et pourquoi.

Fais faire ce travail par un sous-agent Opus (brief : `briefs/modele-voix-reelle.md`), puis une revue indépendante (`verifications.md`).

## Entrées
- `sources/prise-originale.flac` (souvent 44,1 kHz mono).
- `sources/teleprompteur.txt` : le texte voulu, nombres en chiffres, dits en toutes lettres.

## Étapes
1. **Transcription verbatim** de la prise (en arrière-plan : torch n'est installé dans aucun Python de la machine, d'où `uv run`) :
   ```bash
   uv run --no-project --with torch --with transformers --with numpy python scripts/w2v_transcrire.py sources/prise-originale.flac sources/prise-originale.w2v.json
   ```
   Modèle : `jonatasgrosman/wav2vec2-large-xlsr-53-french`. Le script découpe seulement dans les silences (morceaux de 4 à 28 s), jamais dans un mot.
2. **Choix des morceaux** dans `edit-plan/voice-keep.json` (`{"_doc": …, "keep": [...]}`), phrase par phrase contre le téléprompteur. Pour chaque phrase, la **meilleure prise complète** (souvent la dernière). Chaque entrée :
   - `from`, `to` : temps dans la prise ; `text` : ce qui est dit (forme du téléprompteur) ; `cut` : pourquoi ce choix (prises écartées et leurs temps) ;
   - options : `pause` (pause voulue avant, en s), `fade_in`, `tight` (intervalles où resserrer), `no_tempo` / `force_tempo` (intervalles sans ou avec ×1,1), `merge_prev` (greffe : le premier mot du morceau et le dernier du précédent ne font qu'un mot affiché, ex. « 4060 Ti » recousu le 18/11).
   Outils de lecture : `python3 scripts/mots.py début fin` (mots et pauses d'une fenêtre), `python3 scripts/vue.py [début fin]` (îlots d'énergie et mots dedans), `scripts/w2v_candidats.py audio requetes.json` (classe des transcriptions candidates par perte CTC, pour trancher un chiffre douteux).
   - Une reformulation qui garde le sens passe. **Un chiffre changé se corrige par une greffe** prise ailleurs dans la prise, sinon on le signale.
   - Une phrase improvisée absente du téléprompteur peut rester si elle sert (l'accroche du 8 Go) : note-la dans `cut`.
3. **Remesure le plancher de bruit** de cette prise avant de lancer (il change d'une prise à l'autre : −73,7 dB sur « Même carte », mais −75 puis −66 dB sur le 8 Go à cause d'une ventilation). Les seuils sont exprimés au-dessus de deux références (plancher local et plancher « parole ») : voir l'en-tête de `voix.py`.
4. **Génère la voix** : `python3 scripts/voix.py` (depuis la racine). Ce qu'il fait :
   - bords de chaque morceau calés sur l'énergie (coupe dans le silence, ou au creux le plus bas entre deux mots collés) ;
   - souffles et bruits hors mots atténués de 35 dB ; jamais dans les 60 ms avant un mot ni 30 ms après (attaques /s/, /t/) ; l'explosion d'une consonne finale est gardée ;
   - pauses resserrées : 0,18 s ou moins gardées, puis 0,34 s au plus (0,29-0,34 s entre deux phrases) ; raccords à 0,30 s avant une phrase, 0,16 s au milieu ;
   - passages au débit lent (sous le 45e centile de la prise) accélérés à ×1,1 (hauteur conservée), changement de vitesse seulement dans les pauses ; l'auteur l'a demandé (« ×1,1 sur les passages lents », 12/11) ;
   - fondus de 6 ms à chaque jointure ; mastering 2 passes loudnorm, −16 LUFS, LRA 9, crête −2,5 dBTP, 48 kHz.
5. **Retouches de fond** si besoin : `python3 scripts/retouche_voix.py` (à réécrire pour la vidéo) comble les trous de silence numérique au milieu du bruit de fond (effet de porte) avec du bruit de salle pris tout près, coupe sous 80 Hz (ventilation) et remplace les clics isolés. Il garde `sources/voix-avant-retouche.flac`.
6. **Contrôle par l'agent lui-même** :
   ```bash
   uv run --no-project --with torch --with transformers --with numpy python scripts/w2v_transcrire.py assets/audio/voix.flac sources/voix.w2v.json
   python3 scripts/verif_texte.py
   python3 scripts/verif_voix.py
   python3 scripts/verif_begaiements.py sources/voix.w2v.json
   python3 scripts/verif_souffles.py
   uv run --no-project --with torch --with transformers --with numpy python scripts/verif_raccords.py
   ```
   `verif_texte.py` compare au texte voulu, cherche les répétitions dans une fenêtre de 4 mots, les débris, les blancs de plus de 0,8 s, chaque nombre et mesure le niveau (exemple sur le 8 Go : −16,4 LUFS, −2,9 dBTP). Les nombres qu'il signale sont souvent de simples erreurs de transcription (« troisvirguledeux ») : retranscris ±2 s pour trancher.

## Sorties
- `assets/audio/voix.flac` (masterisée), `sources/voix-avant-master.flac`.
- `sources/voix.words.json` : `[{"text": "qwen", "start": 0.03, "end": 0.181}, …]`, temps dans la voix finale, nombres en chiffres comme au téléprompteur, « 14 000 » en un seul mot avec espace insécable.
- `sources/voix.phrases.json` : une entrée par phrase (`id`, `section`, `text`, `start`, `end`, `said`).
- `edit-plan/voice-keep.json`, `voice-cuts.json`, `voice-map.json` (temps finaux ↔ temps de la prise), `voice-report.json` (plancher, seuils, durées).
- `renders/controle-raccords.m4a` (+ `.txt`) : la bobine de chaque raccord, pour que l'auteur puisse écouter.

## Ce que l'auteur a déjà reproché (et qu'il ne faut plus jamais livrer)
- deux mots superposés, « et et », « un un » (Qwen 4, 12/11) ;
- des souffles gardés, un raté laissé (« Sur une… ») ;
- un mot tranché par un raccord hérité d'un ancien montage ;
- une parole hachée : il préfère une parole fluide, sans blanc, un peu accélérée.
