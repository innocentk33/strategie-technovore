---
paths:
  - "projets/**/miniature/**"
  - "projets/**/fiche.md"
  - "ressources/miniatures/**"
---

# Miniatures

## Style unique : celui d'OpenCode piraté (décidé le 11/11)

**Toutes les miniatures prennent le style d'OpenCode piraté** (4,2 % de CTR, la meilleure de la chaîne), y compris celles d'« IA chez moi ». La charte verte (`vert.html`) n'est plus utilisée. La référence est [`ressources/miniatures/images/reference-style-opencode.jpg`](../../ressources/miniatures/images/reference-style-opencode.jpg) :
- fond noir, texturé (code, grille sombre), jamais une couleur pleine ;
- à gauche, le logo ou l'objet du sujet, petit, au-dessus du texte ;
- 2 lignes de texte en capitales très grasses : le sujet en blanc, puis le mot choc en rouge (« OPENCODE / HACKÉ ») ; ensemble, elles se comprennent sans le titre ;
- à droite, un visage expressif ou un meme (acteur ou réaction : voir la mémoire « visages et memes »), détouré, qui sort du cadre en bas.

Contre-exemple : « 16 Go de VRAM » (09/11), avec un fond rouge plein, une carte graphique grise et le texte « ÇA RENTRE ? », a fait 1,5 % de CTR à J+2 (test A/B encore en cours) : pas d'émotion, et un texte qui ne dit pas le sujet (voir [`etudes/audit-2026-11-11.md`](../../etudes/audit-2026-11-11.md), § 4).

**Texte « PEAK », en essai depuis le 12/11** (demande de l'auteur, référence [`reference-texte-peak.jpg`](../../ressources/miniatures/images/reference-texte-peak.jpg)) :
- les deux lignes passent en blanc, en Anton (`fonts/anton-latin-400.woff2`), avec des lettres serrées ;
- derrière chaque ligne, une copie rouge pleine, sans flou, un peu plus grande (×1,06) et décalée vers le bas (0,075 em) ;
- le texte est bien plus gros qu'en Inter : à 168 px, il prend presque toute la moitié gauche ;
- on l'obtient avec `?txt=peak` dans les maquettes de Strata et de Qwen 4. La copie rouge est un vrai élément `.t`, pour devenir un calque dans le PSD. Rendus : `rendus/a-peak.png` ; PSD : `photocraft/a-peak.psd` ; avant/après : `apercu/essai-peak.png` ;
- pour PhotoCraft, Anton doit être installé (`~/Library/Fonts/Anton-Regular.ttf`, fait le 12/11). Sans lui, le PSD prend une police fine.

Ce n'est pas encore la règle. Le mot choc n'est plus écrit en rouge, puisque le rouge passe à l'ombre. **Test A/B décidé le 12/11** : `a` (ancien texte) contre `a-peak`, avec le même texte et le même meme, sur Qwen 4 (si le test Harold contre Jackie n'est pas déjà lancé) et sur Strata. On tranche avec les résultats ; si PEAK gagne les deux, il devient le texte de toutes les miniatures.

**Seule la miniature est concernée.** Le montage de la vidéo garde sa propre DA : la règle « la vidéo commence sur la scène de la miniature » tombe.

Le reste de ce fichier (3 variantes, chartes `noir`/`vert`) date d'avant cette décision. Ce qui en reste valable :
- les règles communes de la section 2 de `ressources/miniatures/propositions.md` (moitié haute, zones interdites, 4K, jamais la même info que le titre) ;
- les étapes (refs → `/youtube thumbnail` → maquette → `/coach-miniature-youtube` → test des 50 %) ;
- les tests A/B, mais toutes les variantes sont dans le style OpenCode et ne changent qu'une seule chose (le meme, le mot choc ou l'objet). La base de départ est `noir.html`.

---

**Ancien style de toutes les miniatures** (décidé le 03/11, d'après OpenCode piraté) : un visage ou un objet fort, net et en couleur, sur un fond très contrasté. Détails dans la section 2 de `ressources/miniatures/propositions.md`.

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
  - Le script s'appuie sur `export.js` (`?layer=decor`, `?dump=1`) et `photocraft-cli` (`~/.local/bin` sur Mac, `C:\Program Files\PhotoCraft` sur Windows).
  - Pour une miniature de projet : `python3 -I ressources/miniatures/psd.py --page <miniature.html> <dossier> [a b c]`, ou `--page <miniature.html> v=b <sortie.psd>` pour une seule.
  - Seuls les textes droits des éléments `.t` deviennent des calques de texte ; les textes tournés restent dans le décor.
  - Vérifier un PSD : `photocraft-cli convert <fichier>.psd <sortie>.png`.
- Planches de lisibilité sur le fond sombre de YouTube : `python3 -I ressources/miniatures/planches.py <dossier des concurrents>` (Pillow).
- Si tu ajoutes une variante, mets à jour les listes de variantes en dur dans `rendre.sh` **et** dans `psd.py` (`kept`).
- Polices locales dans `fonts/` (Archivo Black, Inter, JetBrains Mono) ; n'utilise pas SF Pro (licence).
- Le serveur MCP `photocraft` est déclaré dans `.mcp.json` et activé dans `.claude/settings.local.json` (`enabledMcpjsonServers`). `psd.py`, lui, appelle le CLI directement.
