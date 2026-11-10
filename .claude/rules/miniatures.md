---
paths:
  - "projets/**/miniature/**"
  - "projets/**/fiche.md"
  - "ressources/miniatures/**"
---

# Miniatures

**Style de toutes les miniatures** (décidé le 03/11, d'après OpenCode piraté) : un visage ou un objet fort, net et en couleur, sur un fond très contrasté. Détails dans la section 2 de `ressources/miniatures/propositions.md`.

`projets/<nom>/miniature/` contient `propositions.md`, les maquettes HTML (`propositions/miniature.html?v=a|b|c`) et les PSD dans `photocraft/`.

## Trois miniatures par vidéo, pour « Tester et comparer » (décidé le 24/10)

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

## Outils (`ressources/miniatures/`, détails dans la section 6 de `propositions.md`)

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
- Le serveur MCP `photocraft` est déclaré dans `.mcp.json` et activé dans `.claude/settings.local.json` (`enabledMcpjsonServers`). `psd.py`, lui, appelle le CLI directement.
