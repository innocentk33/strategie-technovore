# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Nature du dépôt

Ce dépôt n'est pas une application : c'est la planification de la chaîne YouTube **Technovore** (tech en français, public surtout africain et jeune). Presque tout est du Markdown en français. Le code se limite à quelques outils de production (miniatures, voix). Il n'y a ni build, ni lint, ni tests.

Tout s'écrit en français et s'adresse à l'auteur en le tutoyant, comme le font déjà les documents (« Range-le ici », « Ne te plaît pas »).

## Documents pilotes, à garder cohérents

Une décision touche souvent plusieurs fichiers à la fois. Quand une date, un titre ou un statut change, mets à jour **tous** les endroits qui le citent :

- `strategie.md` (v4) : positionnement, les 3 piliers (« Le génie derrière l'app », « IA chez moi », « Les grandes histoires de la tech »), objectifs à 1, 3 et 6 mois, les idées classées. Les fiches renvoient à ses numéros d'idée.
- `calendrier.md` : grille de publication jusqu'au 26/04/2027. **Une vidéo longue chaque lundi à 18 h, aucun Short** (décidé le 21/10). Ses changements sont notés en tête (« Mis à jour le … »).
- `README.md` : tableau de suivi des projets. Statuts : Fiche → Brouillon → Recherche → Script → Voix → Montage → Programmé → Publié (avec le lien YouTube).
- `idees.md` (réserve), `archive/README.md` (abandons, avec date et raison), `etudes/` (chaînes concurrentes, données vidIQ datées, audits de la chaîne `audit-AAAA-MM-JJ.md`, `suggestions-2026-10-23.md` (où YouTube suggère nos vidéos et pourquoi), `storytelling-2026-10-23.md` (les 30 premières secondes et les liaisons de Cam, V2F et Dis Cyril, transcriptions dans `transcriptions/`), et `radar.md`, le journal du radar).

Cycle de vie : idée dans `idees.md` → dossier `projets/<nom>/` (copier une fiche existante) + ligne dans le README et le calendrier → à l'abandon, `git mv` vers `archive/` et une ligne dans `archive/README.md`.

## Radar : à chaque sortie de vidéo

Quand une vidéo sort (l'auteur le dit, ou une vidéo publique apparaît dans `vidiq_user_videos` sans être marquée « Publié » dans le README), fais le radar avant le reste. Il sert à choisir la vidéo du prochain créneau libre, en général celle du lundi N+2 : celle de N+1 est déjà en montage.

1. **Notre chaîne** (`vidiq_channel_stats`, `vidiq_channel_analytics` avec `filters: video==ID`) :
   - la vidéo précédente à J+7 : `engagedViews`, durée moyenne, % regardé, abonnés gagnés, sources de trafic, part de la France ;
   - sa courbe de rétention (`report: audience_retention`) : % de spectateurs à 0:15 (cible 75 %) et à 1:00 (cible 50 %) ;
   - ses 5 premières sources dans les suggestions (`dimensions: insightTrafficSourceDetail`, `filters: insightTrafficSourceType==RELATED_VIDEO;video==ID`, 5 crédits) : qui nous suggère, et combien de temps ces spectateurs restent ;
   - le CTR et les impressions ne passent pas par l'API : demande une capture de Studio.
2. **Concurrents** : la liste de surveillance de `etudes/radar.md`, avec un appel `vidiq_outliers` par langue (`channelIds`, `thisMonth`). Note ce qui fait ×2 ou plus.
3. **Public français** : `vidiq_outliers` en `language: fr` sur les mots-clés listés dans `etudes/radar.md`.
4. **Choix** :
   - candidats : la réserve d'`idees.md`, les idées de `strategie.md` et les signaux du radar ;
   - note sur 40 avec la grille de `strategie.md` (demande × clic × production × niche) ;
   - à note proche, préfère le sujet qui a une grosse vidéo française récente (100 K vues ou plus dans le mois) : sortir dans sa semaine nous place à côté d'elle dans les suggestions ;
   - règles :
     - pas deux fois le même pilier de suite ;
     - au plus 1 vidéo de tendance sur 3 ;
     - une vidéo IA est « testée » seulement si le modèle tourne sur la RTX 5080 (16 Go), sinon elle est « calculée » (voir `strategie.md`, pilier 2) ;
     - on ne copie pas l'angle ni la miniature d'un concurrent.
5. **Écris** :
   - une entrée datée en tête de `etudes/radar.md` (chiffres + décision) ;
   - puis `calendrier.md` (ligne « Mis à jour le … »), `README.md` et le classement de `strategie.md` ;
   - et la fiche si la vidéo choisie n'en a pas.

Budget : une quinzaine d'appels vidIQ (~75 crédits). Regarde `vidiq_balance` avant. Si un sujet chaud n'attend pas deux semaines, propose-le à l'auteur au lieu de bousculer le calendrier tout seul.

## Un dossier projet (`projets/<nom>/`)

Fichiers par ordre de production :

1. `fiche.md` : titres, miniature, contenu, points à vérifier.
2. `brouillon*.md` : premiers jets.
3. `script.md` : script final ; `script-v1.md` garde l'ancienne version.
4. `grill-v1.md` : la critique du script.
5. `sources.md` : les faits vérifiés.
6. `teleprompteur.md` et `.txt` : une ligne = un souffle ; les `[MARQUEURS]`, `⟦à écrire⟧` et `(indications)` ne se lisent pas.
7. `storyboard.md` : timecodes calés sur `voix-off-montee.wav` ; en HyperFrames, `data-start` = le timecode en secondes.
8. `upload.md` : kit d'upload (mots-clés vidIQ, chapitres, description) ; `*.fr.srt` / `*.en.srt` pour les sous-titres. Une fois le kit écrit, ajoute-lui une section « Suggestions » (le pourquoi est dans `etudes/suggestions-2026-10-23.md`) :
   - **les vidéos hôtes** : 4 ou 5 grosses vidéos françaises du même sujet, sorties ce mois-ci (`vidiq_outliers` en `language: fr`, ou `vidiq_youtube_search`) ; note leurs titres et les mots qu'on peut partager dans le nôtre, sans copier leur angle ni leur miniature ;
   - **la planche** : leurs miniatures dans `projets/<nom>/miniature/hotes/` (`curl -o <id>.jpg https://i.ytimg.com/vi/<id>/maxresdefault.jpg`), puis `python3 -I ressources/miniatures/planches.py --suggestions <notre miniature> projets/<nom>/miniature/hotes` ;
   - **la comparaison** : à 168 px, la nôtre se repère-t-elle, et promet-elle autre chose que les leurs ? Sinon, retouche avant de publier ;
   - **l'enchaînement** : l'écran de fin pointe la vidéo suivante de la playlist du pilier, et une fiche tombe pendant le plateau de rétention.
9. `miniature/` : `propositions.md`, maquettes HTML (`propositions/miniature.html?v=a|b|c`), PSD dans `photocraft/`.

**Trois miniatures par vidéo, pour « Tester et comparer »** (décidé le 24/10) :
- **a, noir premium** : la charte `noir.html`, avec le sujet en gros au premier plan, en couleur, sur un décor désaturé ;
- **b, couleurs de Technovore** : ardoise `#34495e` et menthe `#07c095`, la charte `vert.html` ;
- **c, hors niche** : une miniature qui s'inspire d'une autre niche, là où les miniatures ressortent le plus (gaming, vlog, finance, true crime…). Note la chaîne et la vidéo d'origine dans `propositions.md`, et n'en copie pas la miniature.

Pour chacune, dans cet ordre :
0. 10 à 15 références dans `miniature/refs/` : nos vidéos qui ont marché, les concurrents, d'autres niches, des affiches de films, des pochettes d'albums, des publicités ; on ne part jamais d'une page blanche ;
1. le concept et le brief avec `/youtube thumbnail` : la miniature pose une question et fait ressentir une émotion, même sans le titre ;
2. la maquette HTML (`?v=a|b|c`), rendue en PNG ;
3. la critique avec `/coach-miniature-youtube`, puis les corrections, et le test des 50 % (moitié basse cachée, section 5 de `propositions.md`) ;
4. le rendu final et le PSD.

Les trois gardent les règles communes de la section 2 de `ressources/miniatures/propositions.md` (texte, logos, zones interdites, 4K) et la même promesse que le titre, sans répéter son texte.

Règles du test (24/10) :
- **Chaque série garde sa charte** : noir pour « Le génie derrière l'app » et les grandes histoires, vert pour « IA chez moi ». C'est elle qui sert de miniature par défaut, et la vidéo commence sur sa scène.
- **a et b ont exactement la même scène** (objet, texte, cadrage) : seules les couleurs changent. Ainsi, a contre b dit quelle charte gagne.
- **c est le joker** : une autre idée. Si c gagne souvent, on reprend son idée dans la charte de la série.
- **On compte les victoires par série** dans `propositions.md`. Un test « non concluant » ne compte pas, et la charte de la série reste.
- **Après 4 à 6 vidéos par série, on fige** : on arrête les trois miniatures systématiques et on ne teste plus qu'une chose à la fois, avec 2 variantes.

Le montage se fait hors de ce dépôt (projets HyperFrames ou Remotion). `.gitignore` exclut les vidéos et les `.wav` : les fichiers audio versionnés sont les `.m4a`.

**Les 15 premières secondes sont les plus fortes de la vidéo** (règle du 22/10, section 5 de `strategie.md`) :
- on y met le meilleur moment : le résultat, le chiffre le plus fou ou l'image promise par la miniature ;
- on n'y met ni contexte, ni présentation, ni « dans cette vidéo » ;
- à vérifier à chaque brouillon, script, grill et storyboard ;
- origine : ArtCraft perdait 34 % de ses spectateurs en 15 s (`etudes/audit-2026-10-22.md`).

**Les 30 premières secondes n'ont aucune phrase de remplissage, et le script se dit comme à un ami** (23/10, section 5 de `strategie.md`) :
- chaque phrase des 30 s confirme le clic, ouvre une question ou fait monter l'enjeu ; la question centrale est posée avant 30 s, puis un pont ouvre la boucle suivante ;
- les faits arrivent avec des liaisons orales (« donc », « du coup », « en fait », « sauf que », « en effet », « voilà comment… ») et une réaction ; on ne les empile pas comme une fiche. Repère : 1,5 liaison ou plus pour 100 mots (nos téléprompteurs : 0,7 à 0,9) ;
- le contrôle est la variante storytelling du skill `youtube-script-grill` (test des 30 secondes et axe 10) ;
- origine : `etudes/storytelling-2026-10-23.md`.

Les faits comptent : chaque affirmation d'une miniature ou d'un script doit être tenue par la vidéo et sourcée (voir `ressources/miniatures/propositions.md`, section 5, pour les pièges déjà repérés).

## Outils de `ressources/`

Miniatures (`ressources/miniatures/`, détails dans la section 6 de `propositions.md`) :

- Miniatures en 4K (3840×2160) : on dessine en 1280×720 et `rendre.sh` et `psd.py` rendent à ×3 (`--force-device-scale-factor=3`). Import depuis l'ordinateur (50 Mo max ; l'appli mobile plafonne à 2 Mo).
- Deux chartes HTML de 1280×720 : `noir.html` pour « génie derrière l'app » et grandes histoires (`?n=1`, `1b`, `3`, `4`, `6`, `7`, `8`), et `vert.html` pour « IA chez moi » (`?n=2`, `5`, `9`, `10`). Les règles figées des chartes sont dans la section 2 de `propositions.md`, à respecter pendant au moins 5 vidéos.
- Rendu PNG avec Chrome headless : `./ressources/miniatures/rendre.sh noir 3` (sans argument : toutes) → `rendus/`.
- PSD à calques pour PhotoCraft : `python3 -I ressources/miniatures/psd.py noir 3` → `photocraft/`.
  - Le script s'appuie sur `export.js` (`?layer=decor`, `?dump=1`) et `~/.local/bin/photocraft-cli`.
  - Seuls les textes droits des éléments `.t` deviennent des calques de texte ; les textes tournés restent dans le décor.
  - Vérifier un PSD : `photocraft-cli convert <fichier>.psd <sortie>.png`.
- Planches de lisibilité sur le fond sombre de YouTube : `python3 -I ressources/miniatures/planches.py <dossier des concurrents>` (Pillow).
- Si tu ajoutes une variante, mets à jour les listes de variantes en dur dans `rendre.sh` **et** dans `psd.py` (`kept`).
- Polices locales dans `fonts/` (Archivo Black, Inter, JetBrains Mono) ; n'utilise pas SF Pro (licence).

Voix : `ressources/voix/sm7b.sh prise.wav [sortie.wav]` passe une prise dans une chaîne ffmpeg (-16 LUFS). Les réglages se changent à l'oreille, avec les variables en tête du script.

## Outils externes

- vidIQ (MCP) pour les mots-clés, les concurrents et les statistiques. Date toujours les chiffres qui en viennent.
- Le serveur MCP `photocraft` est déclaré dans `.mcp.json`, mais désactivé dans `.claude/settings.local.json`. `psd.py` appelle le CLI directement.
- `claude-youtube/` est une copie locale du skill `/youtube`, ignorée par git. Le skill réellement utilisé est celui de `~/.claude/skills/`. Ne modifie pas cette copie.
