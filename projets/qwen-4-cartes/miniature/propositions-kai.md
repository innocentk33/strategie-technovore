# Miniatures Kai h/i/j — 19/11/2026

**Accroche : ACHETER / TROP TÔT ?**

Une carte graphique, une horloge et le vrai logo Qwen violet/blanc sur une tuile QWEN 4. L’horloge raconte la décision d’attendre avant l’achat, sans préjuger du lancement ni donner un prix.

Titre utilisateur : Qwen 4 : quelle carte graphique acheter (ou pas) ? La miniature complète le choix de carte par son calendrier : faut-il acheter avant de connaître les fichiers ?

## Fidélité au contenu historique

Le script V2 des 11–12 novembre sépare ce qui était sûr des annonces/rumeurs et conclut qu’on achète pour un fichier et sa conversation, pas pour un nom. Aucun statut de sortie actuel, prix, disponibilité ou mesure de Qwen 4 n’est ajouté. Cette série remet en image une vidéo historique ; elle n’actualise pas son contenu.

## Trois variantes

- h : fond noir calme, Archivo Black blanche et jaune, copie rouge décalée ; portrait illustré Harold, sourire crispé et objets à contours noirs/ombres rouge-bleu.
- i : fond uni #141e27, menthe #07c095 et copie blanche ; sans portrait, objets agrandis sous le titre.
- j : même scène et même portrait que h, peau naturelle, fond Technovore et ombres adaptées ; logo Qwen conserve son violet/blanc officiel.

Le texte se lit à gauche ou en haut. Les regards vont vers la gauche. Aucun logo ne touche l’accroche ni sa copie décalée. Rien d’essentiel dans le coin de la durée. h contre j compare la palette ; i contre j compare deux compositions, pas le visage comme unique variable.

## Sources et fichiers modifiables

- [Maquette HTML](propositions/miniature-kai.html) : `?v=h`, `?v=i`, `?v=j`, objets SVG modifiables et vrais logos composés séparément.
- [Prompt exact et provenance](sources/prompt-kai-19-provenance.md), source générée sur vert puis détourage réel par `portrait.py`. Assets illustrés, pas placeholders.
- PNG 4K : `rendus/h-kai.png`, `i-kai.png`, `j-kai.png`.
- PSD : `photocraft/h-kai.psd`, `i-kai.psd`, `j-kai.psd`. Décor raster + titres/labels droits en calques Type modifiables, Archivo Black installée.
- Reproduire : `./projets/qwen-4-cartes/miniature/rendre-kai.sh`. Options `--png-only`, `--psd-only`, et `h|i|j` pour cibler une variante. Chrome a un profil temporaire distinct.
- Exporteur : `export-kai-psd.py`, réemploie `ressources/miniatures/psd.py` et le CLI PhotoCraft. Aucun ancien script, rendu ou PSD n’est remplacé.
- Contrôles : `apercu/kai/comparaison-168px.png`, `comparaison-50-pourcent.png`, `test-50-et-168px.png`, `comparaison-640px.png`, reconversions PSD et `verification-technique.json`.

La [critique indépendante de cette nouvelle série](critique-kai.md), réalisée par un autre agent après lecture des trois variantes, les approuve sans correction obligatoire. Les empreintes complètes des PNG finaux y sont consignées. Les critiques et propositions historiques restent conservées.

Contrôle technique final : les trois PNG et les trois PSD sont en 3840 × 2160. Les calques Type emploient Archivo Black, sans avertissement PhotoCraft. Les trois PSD ont été réouverts en PNG ; écart moyen maximal par canal : 0.099/255. Le décor reste un calque raster et les objets sont modifiables dans les sources HTML/SVG.
