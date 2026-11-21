# AGENTS.md

Consignes pour tout agent qui travaille dans ce dépôt (Claude Code, Codex, GitHub Copilot, Gemini CLI, ou autre). C'est la **source unique** : `CLAUDE.md` n'en est que l'import, et `.gemini/settings.json` demande à Gemini CLI de lire ce fichier.

## Nature du dépôt

Ce dépôt n'est pas une application : c'est la planification de la chaîne YouTube **Technovore** (tech en français, public surtout africain et jeune). Presque tout est du Markdown en français. Le code se limite à quelques outils de production (miniatures, voix, régie). Il n'y a ni build, ni lint, ni tests.

Tout s'écrit en français et s'adresse à l'auteur en le tutoyant, comme le font déjà les documents (« Range-le ici », « Ne te plaît pas »). Ne commite et ne pousse rien sans qu'il le demande.

## Documents pilotes, à garder cohérents

Une décision touche souvent plusieurs fichiers à la fois. Quand une date, un titre ou un statut change, mets à jour **tous** les endroits qui le citent :

- `strategie.md` (v4) : positionnement, les 3 piliers (« Le génie derrière l'app », « IA chez moi », « Les grandes histoires de la tech »), objectifs à 1, 3 et 6 mois, les idées classées. Les fiches renvoient à ses numéros d'idée.
- `calendrier.md` : grille de publication jusqu'au 26/04/2027. **Une vidéo longue chaque lundi à 18 h, aucun Short** (décidé le 21/10). Ses changements sont notés en tête (« Mis à jour le … »).
- `README.md` : tableau de suivi des projets. Statuts : Fiche → Brouillon → Recherche → Script → Voix → Montage → Programmé → Publié (avec le lien YouTube). Si tu changes le format de ce tableau ou de la grille du calendrier, relance `node ressources/regie/verif.mjs`.
- `idees.md` (réserve), `archive/README.md` (abandons, avec date et raison), `etudes/` (concurrents, données vidIQ datées, audits `audit-AAAA-MM-JJ.md`, `suggestions-2026-10-23.md`, `storytelling-2026-10-23.md` et ses `transcriptions/`, `radar.md`).

Cycle de vie : idée dans `idees.md` → dossier `projets/<nom>/` (copier une fiche existante) + ligne dans le README et le calendrier → à l'abandon, `git mv` vers `archive/` et une ligne dans `archive/README.md`.

**À chaque sortie de vidéo** (l'auteur le dit, ou une vidéo publique de `vidiq_user_videos` n'est pas « Publié » dans le README) : applique le skill `radar` (section « Skills ») avant le reste.

## Un dossier projet (`projets/<nom>/`)

Par ordre de production : `fiche.md` → `brouillon*.md` → `script.md` (`script-v1.md` garde l'ancienne) → `grill-v1.md` → `sources.md` (faits vérifiés) → `teleprompteur.md`/`.txt` → `storyboard.md` → `upload.md` (skill `upload`) → `miniature/`.

### Règles détaillées : quel fichier lire selon ce que tu touches

Les règles détaillées sont dans `.claude/rules/`. Claude Code les charge seul quand il ouvre un fichier concerné. **Tout autre agent doit les lire lui-même** avant de travailler sur ces fichiers :

| Si tu lis ou écris… | Lis d'abord |
|---|---|
| `projets/**/fiche.md`, `brouillon*.md`, `script*.md`, `grill*.md`, `storyboard.md`, `teleprompteur*` | `.claude/rules/script.md` (15 et 30 premières secondes, liaisons orales, téléprompteur) |
| `projets/**/miniature/**`, `projets/**/fiche.md`, `ressources/miniatures/**` | `.claude/rules/miniatures.md` (style unique d'OpenCode depuis le 11/11, variantes, logos, outils de rendu) |
| `ressources/voix/**`, `ressources/regie/**` | `.claude/rules/ressources.md` (chaîne de voix, régie) |
| `projets/**/voicestudio*`, ou tout texte préparé pour une voix de synthèse | `.claude/rules/voix-synthese.md` (pas de pause, nombres en lettres, liaisons écrites, conventions de prononciation) |

Une `fiche.md` demande donc deux fichiers de règles (script et miniatures). Ces fichiers commencent par un en-tête `paths:` (propre à Claude Code) : ignore-le, la table ci-dessus dit déjà quand les lire.

Les faits comptent : chaque affirmation d'une miniature ou d'un script doit être tenue par la vidéo et sourcée (voir `ressources/miniatures/propositions.md`, section 5, pour les pièges déjà repérés).

### Règles de l'auteur qui reviennent partout

- **Sources anonymes** : dans la voix d'un script, on ne nomme jamais une chaîne YouTube ni un créateur (« un utilisateur relève », « une vidéo en espagnol ») ; les noms restent dans `sources.md` et, au besoin, dans la description. Pas d'ouverture égocentrée du type « Cette carte, c'est la mienne ».
- **Vendeurs anonymes** : une annonce d'occasion se cite par « sur leboncoin » ou « en occasion », avec son prix, jamais la ville ni le pseudo du vendeur (ni dans le téléprompteur, ni dans les `[VISUEL]`). Pas de petit marchand nommé dans le hook. Les villes restent dans `recherche/` et `sources.md`.
- **Prix** : le meilleur prix du jour, tous marchands confondus (Amazon d'abord), daté ; jamais « même marchand, même jour ». Le marchand se nomme dans la voix.
- **Voix de synthèse (VoiceStudio)** : aucune pause balisée, liaisons écrites comme elles se disent ; règles complètes dans `.claude/rules/voix-synthese.md`, et la façon dont l'auteur dit chaque carte dans `ressources/voix/prononciations.md`.

## Montage

Le montage se fait **hors de ce dépôt** (HyperFrames ou Remotion), dans le dossier `premium-noir` de l'auteur, qui n'est pas versionné. Pour faire, reprendre ou retoucher un montage (voix, captures, mèmes, critiques, rendus), suis le skill `montage` : sa section « Sur une autre machine » dit quoi installer et quels chemins définir. `.gitignore` exclut les vidéos et les `.wav` : les fichiers audio versionnés sont les `.m4a`, sauf la banque de reprises de voix de l'auteur, en FLAC (`ressources/voix/reprises/`, guide `ressources/voix/prononciations.md`).

## Skills

Un skill est un dossier avec un `SKILL.md` (méthode pas à pas) et parfois des fichiers de références. Les skills du projet sont dans `.claude/skills/` (c'est le chemin de Claude Code, mais les fichiers sont du Markdown ordinaire : tout agent peut les lire). Ne déplace pas ces dossiers.

| Skill | Quand l'utiliser | Fichier |
|---|---|---|
| `montage` | Faire, reprendre, corriger ou relancer le montage d'une vidéo : voix reçue ou reprises de voix, captures, mèmes, critiques, rendu 1080p puis 4K. | `.claude/skills/montage/SKILL.md` |
| `upload` | Préparer la publication d'une vidéo : `projets/<nom>/upload.md` (mots-clés, chapitres, description), sous-titres `.fr.srt` / `.en.srt`, section « Suggestions ». | `.claude/skills/upload/SKILL.md` |
| `radar` | À chaque sortie de vidéo : mesurer la précédente, surveiller concurrents et public français, choisir la vidéo du prochain créneau, mettre à jour `etudes/radar.md`, le calendrier, le README et la stratégie. | `.claude/skills/radar/SKILL.md` |
| `miniature-kai` | Les 3 miniatures « à la manière de Kai » (h, i, j) d'une nouvelle vidéo : maquette HTML, portrait illustré, rendu 4K, test à 168 px, test A/B. | `.claude/skills/miniature-kai/SKILL.md` |

**Si ton agent n'a pas de système de skills** : lis le `SKILL.md` du skill qui correspond à la tâche, puis seulement les fichiers de références qu'il désigne (`references/…`, dans le même dossier, selon son tableau « Quand charger quoi »), et suis-le. Ne charge pas tout le dossier d'avance.

Quelques adaptations quand ton agent n'est pas Claude Code :
- les noms d'outils des skills (`vidiq_*`, sous-agents, `Skill`, `WebSearch`) sont ceux de Claude Code : si tu n'as pas l'équivalent, fais l'étape toi-même ou dis ce qui manque ; n'invente jamais un chiffre à la place d'une mesure vidIQ ;
- « Opus » et « Sonnet » veulent dire « ton modèle le plus fort » et « un modèle plus léger » ;
- les chemins `<DEPOT>`, `<PREMIUM>` et `<TMP>` du skill `montage` sont définis dans sa section « Sur une autre machine ».

Copies de skills plus généraux (écriture de script, grill, miniatures, voix off) : `ressources/skills-gpt/` (voir son `README.md`). Ce sont des copies d'une autre source, en lecture seule : ne les modifie pas.

## Outils externes

- vidIQ (MCP) pour les mots-clés, les concurrents et les statistiques. Date toujours les chiffres qui en viennent. Sans vidIQ, utilise les relevés datés déjà présents dans `etudes/` et dis-le.
- `claude-youtube/` (s'il existe sur ta machine) est une copie locale du skill `/youtube`, ignorée par git, donc absente d'un clone. Ne la modifie pas.
