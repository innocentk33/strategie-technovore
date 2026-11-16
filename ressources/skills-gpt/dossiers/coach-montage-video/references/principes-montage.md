# Principes de montage – méthode indépendante de l'outil

Synthèse de la méthode du tutoriel et de son guide de référence. Ce fichier décrit *quoi* faire et *pourquoi*. La mise en œuvre dans chaque logiciel est dans `outils/`. Les chiffres sont ceux de l'auteur : des points de départ, pas des règles absolues.

## Sommaire
1. Identité de la vidéo
2. Fondations : idée, miniature, script
3. Voix off
4. Inspiration
5. Ressources
6. Script coloré et collecte
7. Configuration du projet
8. Montage brut
9. Animations
10. Deuxième passe et gestion de l'espace
11. Zooms et point d'attention
12. Texte à l'écran
13. Personnage / mascotte
14. Overlays, transitions, effets
15. Sound design
16. Étalonnage
17. Progresser et publier

---

## 1. Identité de la vidéo
Avant tout, situer la vidéo sur quatre axes :

| Question | Spectre |
|---|---|
| Qui est la cible ? | débutant ↔ avancé |
| Quel est le but principal ? | théorique ↔ pratique |
| Quelle ambiance ? | éducatif ↔ divertissant |
| Quelle complexité ? | simple ↔ complexe |

Ces réponses décident du style de montage. Un montage ultra-rapide façon MrBeast ne convient pas à une vidéo calme et posée. Cette méthode enseigne un style précis : le montage « fancy » (animations, textes animés, overlays, effets lumineux, sound design dense).

## 2. Fondations : idée, miniature, script
Un excellent montage ne sauve ni une idée faible ni un script ennuyeux.

- **Idée** : intéressante pour la cible ? Un inconnu cliquerait-il ?
- **Miniature** : partir d'un concept éprouvé (ce qui marche déjà dans la niche), pas d'une idée sortie de nulle part.
- **Script** :
  1. **Plan** : lister tous les points à couvrir, écrire tout ce qui vient en tête.
  2. **Recherche** : s'appuyer sur des faits, exemples et sources solides.
  3. **Problème profond** : identifier la vraie difficulté ou la vraie question sous le sujet apparent.
  4. **Voyage du héros** : construire une histoire secondaire qui porte la vidéo (voir `voyage-du-heros.md`). Le contenu principal se loge dans l'étape « épreuves ».
  5. **Affiner** : couper l'inutile, simplifier (une IA peut aider), construire une progression du début à la fin.
  6. **Code couleur** : voir section 6.

## 3. Voix off
- Micro, ou voix IA (ex. ElevenLabs) ; les voix IA rendent désormais des émotions.
- Générer par petits morceaux plutôt qu'en un seul bloc.
- Terminer la voix off avant de monter : elle sert de colonne vertébrale au montage.

## 4. Inspiration
- Regarder d'autres vidéastes, mais surtout **un bon film** avec un regard de monteur : transitions, narration, montages, angles de caméra. Beaucoup de ces techniques n'ont presque jamais été utilisées sur YouTube : c'est la meilleure source d'originalité.
- Ne pas en faire une excuse pour procrastiner.

## 5. Ressources
- Quatre familles : musique, effets sonores, overlays, presets (ou, en montage par code, composants et blocs réutilisables).
- Se constituer une bibliothèque réutilisable. Sources dans `ressources.md`.

## 6. Script coloré et collecte
- Attribuer à chaque passage du script une catégorie selon ce qu'on voit à l'écran. L'auteur utilise 6 catégories, à adapter. Code couleur proposé (couleurs de surlignage Notion) :

| Catégorie | Étiquette | Couleur | Fond | Texte |
|---|---|---|---|---|
| Vidéo / B-roll | [VID] | Bleu | `#E7F3F8` | `#337EA9` |
| Image | [IMG] | Vert | `#EDF3EC` | `#448361` |
| Capture d'écran | [ECR] | Violet | `#F6F3F9` | `#9065B0` |
| Animation | [ANI] | Orange | `#FBECDD` | `#D9730D` |
| Texte sur fond noir | [TXT] | Gris | `#F1F1EF` | `#787774` |
| Mème / blague visuelle | [MEM] | Rose | `#FAF1F5` | `#C14C8A` |

  Couleurs libres pour le suivi : jaune (`#FBF3DB` / `#CB912F`) = à retravailler ; rouge (`#FDEBEC` / `#D44C47`) = élément manquant ; marron (`#F4EEEE` / `#9F6B53`) = pause ou respiration voulue. L'orange est réservé aux animations parce que ce sont les éléments les plus longs à produire : ils doivent sauter aux yeux.
- Une fois tout le script coloré, rassembler **tous** les éléments de chaque catégorie avant de monter. Les animations sont seulement repérées (et esquissées) à ce stade.

## 7. Configuration du projet
- 1920×1080 (4K seulement si la machine suit), 60 images/s.
- Espace de travail organisé à sa main.

## 8. Montage brut
1. Poser la voix off, la découper selon le script, supprimer les pauses gênantes.
2. **Poser la musique juste après la voix off** (et non à la fin) : elle fixe l'ambiance, permet de couper sur le rythme, rend le travail plus agréable. Régler son volume sous la voix.
3. Placer vidéos, images et captures selon les couleurs du script.
4. Expérimenter des coupes sur les temps forts de la musique (facultatif pour un débutant).
5. Un simple texte sur fond noir est une option visuelle valable.

## 9. Animations
- **Esquisser sur papier d'abord.** Exemple : des cases reliées par des flèches comme un organigramme, titres floutés, zoom sur la première case qui révèle son texte.
- **Rédiger une fiche d'animation** (voir le modèle de script) : éléments, état de départ, mouvements, durées, easing, son associé. Indispensable si l'animation est réalisée en code ou par un agent IA, utile dans tous les cas.
- **Choisir l'outil selon la complexité et le pipeline** :
  - *Simple, sans code* : Canva.
  - *Complexe, à la main, avec un rendu très fin* : After Effects (ou équivalent).
  - *Basée sur des données, répétée, à modifier souvent, ou générée par un agent IA* : Remotion (React) ou HyperFrames (HTML).
- **Briques de base**, quel que soit l'outil : formes, textes, tracés ; texte qui s'écrit (machine à écrire) ; tracé qui se dessine progressivement ; lueur (glow) pour faire ressortir.
- Méthode : esquisser, spécifier, créer, animer, caler sur la voix off. Si l'animation sera zoomée au montage, l'exporter en haute résolution.

## 10. Deuxième passe et gestion de l'espace
- Le premier montage brut n'est jamais parfait : le revoir en entier.
- **Ajouter** : animations, captures, mèmes ; réécrire des passages si une meilleure idée apparaît.
- **Couper** : lignes ennuyeuses, images inutiles, mauvaises blagues.
- **L'espace** : couper chaque milliseconde vide peut détruire l'histoire. Le public n'a pas une attention plus courte, il a des exigences plus hautes. Une pause est permise si ce qui suit la vaut.

## 11. Zooms et point d'attention
- Règle générale : un effet doit compléter ce qui est dit.
- Zoom = animation d'échelle et de position entre deux instants, **avec une courbe lissée** (ease) ; un mouvement linéaire paraît saccadé.
- Niveau supérieur : **garder le point d'attention au même endroit d'une coupe à l'autre**. Repères : point central, ligne des yeux, et surtout **règle des tiers**. Le sujet de chaque zoom et de chaque plan reste au même endroit de l'écran.

## 12. Texte à l'écran
Trois usages :
1. **Sous-titre** – seulement quand on dit quelque chose d'important.
2. **Texte central** – quand un sous-titre ne suffit pas : couleur propre, lueur, tout ce qui le fait ressortir.
3. **Texte intégré à la scène** – attaché à un écran, un mur, un élément du décor.

Animation « pop » de référence (à 60 i/s) :
- échelle 70 % au départ ;
- 110 % environ 7 images plus tard (≈ 0,12 s) ;
- 100 % environ 5 images après (≈ 0,08 s) ;
- lissage léger ; lueur, glitch ou autre selon le style.

Rendre l'animation réutilisable : preset, composant ou fonction selon l'outil.

## 13. Personnage / mascotte (facultatif)
- Générer une tête ou un logo avec un générateur d'images IA, la poser sur une image de stock, intégrer à la vidéo.
- Animer avec des mouvements lissés ; rendre réutilisable.

## 14. Overlays, transitions, effets
- **Overlays** : vidéos sur fond noir (électricité, poussière, light leaks, textures). Mode de fusion **Écran** (screen) pour rendre le noir transparent. Usages : surligner, faire une transition, habiller.
- **Transitions** : light leaks principalement ; glissements, secousses, zooms, rotations.
- **Effets favoris** (avec parcimonie) : lueur, 3D, transformation, flou, mosaïque.
- Pouvoir utiliser un effet ne veut pas dire devoir l'utiliser.

## 15. Sound design
- Sans bruitages, même un beau montage paraît plat : le son représente la moitié de la vidéo.
- Trois bases : **whoosh** (mouvements, transitions), **riser** (montée de tension), **impact** (moment fort). Puis tout ce qui colle au sujet : clavier, engrenages, mèmes, clics, explosion, horloge…
- Méthode : **couper la voix off et la musique**, regarder la vidéo et placer les bruitages. Oser combiner plusieurs sons. Enfin, **baisser le volume** des bruitages pour qu'ils ne deviennent pas agaçants.

## 16. Étalonnage
- Plan par plan : exposition, contraste, saturation.

## 17. Progresser et publier
- Une seule technique nouvelle par vidéo, pratiquée jusqu'à l'aisance, puis la suivante (feuille de route dans `ressources.md`).
- Les chaînes qui stagnent sont celles où chaque vidéo copie les dix précédentes.
- Investir 3 h pour 5 secondes de vidéo est rentable : la fois suivante ça prend 1 h, puis quelques minutes.
- **Perfectionnisme** : un travail créatif n'est jamais « fini ». Décider que c'est suffisant et publier.
- Pas de technique secrète : continuer d'apprendre, mélanger les styles, s'inspirer, casser les règles, et mettre de soi dans ses montages.
