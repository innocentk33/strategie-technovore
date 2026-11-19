# Miniatures Kai h/i/j — 19/11/2026

**Accroche : TON FICHIER / DÉBORDE ?**

Une carte 16 Go et un fichier .GGUF marqué du vrai symbole Qwen. La différence de formes interroge la place du fichier. i agrandit ce duel, h/j ajoutent la confusion reconnaissable du meme.

Titre utilisateur : 16 Go de VRAM suffisent (si tu prends le bon fichier). L’image interroge le mauvais fichier et le débordement qui pénalise une carte pourtant suffisante.

## Fidélité au contenu historique

Le script V3 et les sources S18–S21 / S38 expliquent les fichiers qui débordent, le contexte et le moteur. Le visuel ne transforme pas deux mesures de tiers en test contrôlé : aucun 101, 13 ou ×8 n’est affiché. Le fichier est une métaphore de mémoire, pas une mesure supplémentaire. La carte est générique : elle n’est pas présentée comme la 5080 personnelle de l’auteur.

## Trois variantes

- h : fond noir calme, Archivo Black blanche et jaune, copie rouge décalée ; portrait illustré Jackie Chan, meme WTF et objets à contours noirs/ombres rouge-bleu.
- i : fond uni #141e27, menthe #07c095 et copie blanche ; sans portrait, objets agrandis sous le titre.
- j : même scène et même portrait que h, peau naturelle, fond Technovore et ombres adaptées ; logo Qwen conserve son violet/blanc officiel.

Le texte se lit à gauche ou en haut. Les regards vont vers la gauche. Aucun logo ne touche l’accroche ni sa copie décalée. Rien d’essentiel dans le coin de la durée. h contre j compare la palette ; i contre j compare deux compositions, pas le visage comme unique variable.

## Sources et fichiers modifiables

- [Maquette HTML](propositions/miniature-kai.html) : `?v=h`, `?v=i`, `?v=j`, objets SVG modifiables et vrais logos composés séparément.
- [Prompt exact et provenance](sources/prompt-kai-19-provenance.md), source générée sur vert puis détourage réel par `portrait.py`. Assets illustrés, pas placeholders.
- PNG 4K : `rendus/h-kai.png`, `i-kai.png`, `j-kai.png`.
- PSD : `photocraft/h-kai.psd`, `i-kai.psd`, `j-kai.psd`. Décor raster + titres/labels droits en calques Type modifiables, Archivo Black installée.
- Reproduire : `./projets/claude-ou-mon-pc-1/miniature/rendre-kai.sh`. Options `--png-only`, `--psd-only`, et `h|i|j` pour cibler une variante. Chrome a un profil temporaire distinct.
- Exporteur : `export-kai-psd.py`, réemploie `ressources/miniatures/psd.py` et le CLI PhotoCraft. Aucun ancien script, rendu ou PSD n’est remplacé.
- Contrôles : `apercu/kai/comparaison-168px.png`, `comparaison-50-pourcent.png`, `test-50-et-168px.png`, `comparaison-640px.png`, reconversions PSD et `verification-technique.json`.

La [critique indépendante de cette nouvelle série](critique-kai.md), réalisée par un autre agent après lecture des trois variantes, les approuve sans correction obligatoire. Les empreintes complètes des PNG finaux y sont consignées. Les critiques et propositions historiques restent conservées.

Contrôle technique final : les trois PNG et les trois PSD sont en 3840 × 2160. Les calques Type emploient Archivo Black, sans avertissement PhotoCraft. Les trois PSD ont été réouverts en PNG ; écart moyen maximal par canal : 0.126/255. Le décor reste un calque raster et les objets sont modifiables dans les sources HTML/SVG.
