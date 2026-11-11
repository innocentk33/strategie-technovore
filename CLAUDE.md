# CLAUDE.md

## Nature du dépôt

Ce dépôt n'est pas une application : c'est la planification de la chaîne YouTube **Technovore** (tech en français, public surtout africain et jeune). Presque tout est du Markdown en français. Le code se limite à quelques outils de production (miniatures, voix). Il n'y a ni build, ni lint, ni tests.

Tout s'écrit en français et s'adresse à l'auteur en le tutoyant, comme le font déjà les documents (« Range-le ici », « Ne te plaît pas »).

## Documents pilotes, à garder cohérents

Une décision touche souvent plusieurs fichiers à la fois. Quand une date, un titre ou un statut change, mets à jour **tous** les endroits qui le citent :

- `strategie.md` (v4) : positionnement, les 3 piliers (« Le génie derrière l'app », « IA chez moi », « Les grandes histoires de la tech »), objectifs à 1, 3 et 6 mois, les idées classées. Les fiches renvoient à ses numéros d'idée.
- `calendrier.md` : grille de publication jusqu'au 26/04/2027. **Une vidéo longue chaque lundi à 18 h, aucun Short** (décidé le 21/10). Ses changements sont notés en tête (« Mis à jour le … »).
- `README.md` : tableau de suivi des projets. Statuts : Fiche → Brouillon → Recherche → Script → Voix → Montage → Programmé → Publié (avec le lien YouTube). Si tu changes le format de ce tableau ou de la grille du calendrier, relance `node ressources/regie/verif.mjs`.
- `idees.md` (réserve), `archive/README.md` (abandons, avec date et raison), `etudes/` (concurrents, données vidIQ datées, audits `audit-AAAA-MM-JJ.md`, `suggestions-2026-10-23.md`, `storytelling-2026-10-23.md` et ses `transcriptions/`, `radar.md`).

Cycle de vie : idée dans `idees.md` → dossier `projets/<nom>/` (copier une fiche existante) + ligne dans le README et le calendrier → à l'abandon, `git mv` vers `archive/` et une ligne dans `archive/README.md`.

**À chaque sortie de vidéo** (l'auteur le dit, ou une vidéo publique de `vidiq_user_videos` n'est pas « Publié » dans le README) : lance le skill `radar` avant le reste.

## Un dossier projet (`projets/<nom>/`)

Par ordre de production : `fiche.md` → `brouillon*.md` → `script.md` (`script-v1.md` garde l'ancienne) → `grill-v1.md` → `sources.md` (faits vérifiés) → `teleprompteur.md`/`.txt` → `storyboard.md` → `upload.md` (skill `upload`) → `miniature/`.

Les règles détaillées se chargent seules quand tu ouvres ces fichiers : `.claude/rules/script.md` (15 et 30 premières secondes, liaisons orales), `.claude/rules/miniatures.md` (style unique d'OpenCode depuis le 11/11, variantes, outils de rendu), `.claude/rules/ressources.md` (voix, régie).

Les faits comptent : chaque affirmation d'une miniature ou d'un script doit être tenue par la vidéo et sourcée (voir `ressources/miniatures/propositions.md`, section 5, pour les pièges déjà repérés).

Le montage se fait hors de ce dépôt (HyperFrames ou Remotion). `.gitignore` exclut les vidéos et les `.wav` : les fichiers audio versionnés sont les `.m4a`.

## Outils externes

- vidIQ (MCP) pour les mots-clés, les concurrents et les statistiques. Date toujours les chiffres qui en viennent.
- `claude-youtube/` est une copie locale du skill `/youtube`, ignorée par git. Le skill réellement utilisé est celui de `~/.claude/skills/`. Ne modifie pas cette copie.
