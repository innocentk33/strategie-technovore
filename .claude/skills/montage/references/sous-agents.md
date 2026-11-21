# Pipeline de sous-agents

> **Pour un agent sans sous-agents** (Codex, Gemini CLI, ou tout autre) : fais toi-même chaque étape du tableau, l'une après l'autre. Pour une revue ou une critique « indépendante », lance une **nouvelle session** (ou un nouvel agent) à qui tu ne donnes que le brief rempli, jamais tes propres rapports. « Opus » veut dire « le modèle le plus fort dont tu disposes », « Sonnet » « un modèle plus léger » (recherche, images, rédaction). Les noms d'outils (« notification », `ListAgents`, scratchpad) sont ceux de Claude Code : cherche leur équivalent chez toi.

Tu restes le chef d'orchestre : tu écris `montage.py`, tu regardes les planches, tu tranches. Les tâches longues et indépendantes partent chez des sous-agents, chacun avec un brief écrit dans un dossier de travail temporaire (<TMP>) (copie d'un modèle de `briefs/`, variables remplacées), lancé par « Lis et exécute la consigne complète dans <chemin du brief> ».

| Étape | Agent | Modèle | Modèle de brief | En parallèle de |
|---|---|---|---|---|
| Voix (vraie voix ou clonée) | monteur de voix | Opus | `modele-voix-reelle.md` / `modele-voix-clonee.md` | captures |
| Captures, photos, logos | préparateur d'images | Sonnet | `modele-captures.md` | voix |
| Revue de la voix (2 au plus) | vérificateur indépendant | Opus | `modele-verif-voix.md` | écriture du montage |
| Critique du montage (3 au plus) | monteur critique indépendant | Opus | `modele-critique.md` | rien (tu attends) |
| Kit d'upload et sous-titres | rédacteur | Sonnet | `modele-upload.md` | rendu 4K |
| Retouches de voix de l'auteur | correcteur | Opus (ou toi) | voir `retouches.md` | rien |

Règles :
- **À la fin de chaque étape, vérifie qu'aucun sous-agent ne tourne encore** avant de lancer la suivante (règle de l'auteur du 23/10 ; comment : « Vérifier que rien ne tourne » plus bas), puis relis ce qu'il a écrit : son rapport n'est pas une preuve. Mesure toi-même (durée, LUFS, une planche).
- Un vérificateur ou un critique **n'a pas fait le travail qu'il juge** et ne lit pas les rapports de celui qui l'a fait : son avis doit être indépendant.
- Donne-lui ce qui est déjà décidé (pour qu'il ne le compte pas comme une erreur) et les règles de l'auteur (noms, tampon, bruitages, mèmes muets, rien d'inventé).
- Il ne commite rien et n'écrit que dans le projet et son dossier de travail.
- Les commandes longues (transcription, rendu) tournent en arrière-plan ; on attend la notification, on ne relance pas une seconde copie.
- Le dossier de travail temporaire peut être effacé : les modèles durables sont dans `briefs/`. Les briefs réellement envoyés en novembre 2026 sont dans `briefs/exemples/` : pour « 8 Go » et « 32 Go », voix, captures, vérif, critique et upload ; pour « Même carte » (`mc`), seulement vérif, trois critiques (`mc`, `mc-v2`, `mc-v3`) et upload (ses briefs de voix et de captures étaient écrits directement dans l'appel de l'agent et n'ont pas été gardés).

## D'où viennent les variables des briefs

**Chemins dans les briefs** : les modèles de `briefs/` écrivent `<PREMIUM>`, `<DEPOT>` et `<TMP>` (voir `SKILL.md`, « Sur une autre machine »). Un sous-agent ne sait pas les résoudre : **remplace-les par les chemins absolus réels** de la machine en remplissant le brief (`{{PROJET}}`, `{{DEPOT_PROJET}}` sont déjà des chemins absolus).

| Variable | Où la trouver |
|---|---|
| `{{TITRE}}`, date de sortie | ligne de la vidéo dans `calendrier.md` / `README.md` |
| `{{DEPOT_PROJET}}`, `{{NOM}}` | lien `projets/<nom-depot>/fiche.md` de cette ligne (voir `demarrage.md`) |
| `{{VERSIONS}}` | les fichiers reçus (durée par `ffprobe`), ce que l'auteur en dit dans son message (« la plus fidèle est la voix complet »), et `projets/<nom-depot>/voicestudio.md` (réglages, balises) ; débit et hauteur se mesurent (`voix-clonee.md`) |
| `{{CHUTES}}` | `script.md` : les phrases courtes qui ferment un passage (souvent isolées sur leur ligne, avant un titre `###`, ou notées « chute » dans les indications) ; vérifie qu'elles sont au téléprompteur |
| `{{CHIFFRES}}`, `{{NOMS}}` | tous les nombres, prix, durées et références de cartes de `sources/teleprompteur.txt` (c'est ce qui est dit), recoupés avec `sources.md` (F…) et le relevé de prix daté de `recherche/` |
| `{{PRONONCIATIONS}}` | `ressources/voix/prononciations.md` et les notes de l'auteur dans `voicestudio.md` |
| `{{DATE_RELEVE}}`, `{{PAGES}}`, `{{PRODUITS}}`, `{{LOGOS}}` | le relevé de prix (`recherche/prix-JJ-MM.md`), les indications `[VISUEL]` de `script.md` et `sources.md` |
| `{{DEJA_DECIDE}}` | ce que l'auteur a refusé ou accepté dans la conversation (voix non refaite, captures impossibles, prix disparus…) |

## Critiques successives
La critique n° 1 juge tout. La n° 2 (puis la n° 3) reçoit en plus, dans `{{PRECEDENTE}}`, **la liste des défauts de la précédente avec ce que tu as corrigé** : elle vérifie un par un qu'ils sont réglés (et signale une régression, comme le mème déplacé sur un titre du 32 Go), puis juge **le reste à neuf**, comme une première critique. Elle travaille dans un nouveau dossier (`critique-v2/`, `critique-v3/`).

## Vérifier que rien ne tourne
Avant de lancer l'étape suivante, de copier un projet modèle ou de lancer un rendu :
- chaque sous-agent lancé a renvoyé sa **notification d'achèvement** (son rapport final) ; un agent sans notification tourne encore ou a été arrêté : ne le prends pas pour fini ;
- chaque commande lancée en arrière-plan a renvoyé sa notification ; sa sortie (le fichier de sortie de la tâche, ou le log que tu as choisi, ex. `renders/render-4k.log`) se termine par la dernière ligne attendue, pas par une erreur ;
- aucun rendu, transcription ou montage de voix ne tourne encore sur la machine (sortie vide = rien ne tourne) :
  ```bash
  ps aux | grep -E "hyperframes@0\.9\.47 (render|snapshot|check)|[f]fmpeg |w2v_|scripts/(voix|reprises|prises)\.py" | grep -v grep
  ```
  Les processus `chrome-headless-shell` et `RehyperFrames` qui restent en permanence appartiennent à l'application HyperFrames : ils ne veulent pas dire qu'un rendu tourne.
