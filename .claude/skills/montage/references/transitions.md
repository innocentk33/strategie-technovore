# Transitions, caméra et rythme

Tout ce qui bouge est généré par `scripts/kit.py` (classe `Scene` : caméra, entrées, sorties), `scripts/build.py` (chevauchement des plans) et le bas de `scripts/montage.py` (choix automatique par plan). On n'anime jamais à la main dans `compositions/`. Ce qui suit décrit le 32 Go (21/11/2026), lui-même repris de Strata et du v3 de Qwen 4, calés sur la vidéo de référence de l'auteur (https://youtu.be/9hr_zaJuUbM) après son « atroce » du 12/11 : il voulait plus de mouvement de caméra et des plans qui évoluent.

## Le principe

- **Un plan par idée**, ancré sur sa phrase (`new('…')`, `moteur.md`) ; il dure jusqu'au plan suivant.
- **Le mouvement vient de trois couches**, toujours présentes en même temps :
  1. la caméra du plan, une dérive lente et continue ;
  2. la transition d'un plan à l'autre ;
  3. les entrées d'éléments, posées sur les mots.
- **Pas d'effets décoratifs** : pas de glitch, de flash, de volet, de rotation 3D d'un plan entier, ni de transition « au hasard ». La variété vient du cycle automatique ci-dessous.

## 1. La caméra du plan (dérive continue)

Chaque plan dérive pendant toute sa durée (`ease: sine.inOut`). Les mouvements sont dans `Scene.CAM` (`kit.py`) :

| `cam` | Mouvement | Valeurs |
|---|---|---|
| `push` | zoom avant lent | échelle 0,93 → 1 |
| `pull` | zoom arrière lent | 1 → 0,93 |
| `left` | glisse vers la gauche | x 40 → −40, échelle 0,96 |
| `right` | glisse vers la droite | x −40 → 40, échelle 0,96 |
| `rise` | monte | y 28 → −28, échelle 0,97 |
| `tilt` | légère rotation | −1° → 1°, échelle 0,97 |
| `none` | fixe | écran de fin |

- **Attribution** : dans l'assemblage, en cycle, pour que deux plans voisins ne bougent jamais pareil :
  ```python
  MOVES = ['push', 'left', 'pull', 'rise', 'right', 'push', 'tilt', 'pull']
  for i, s in enumerate(SC):
      s.cam = getattr(s, 'fixed_cam', MOVES[i % len(MOVES)])
  ```
- **Forcer un mouvement** : `new('…', cam='push')`. Le 32 Go le fait seulement pour l'introduction (`push`) et l'écran de fin (`none`).
- **Amplitude** : elle a été doublée le 12/11, parce que l'auteur trouvait qu'il n'y avait « très peu de mouvement de caméra ». Elle reste calculée pour qu'un texte posé à 96 px du bord ne sorte jamais de l'image : il reste à environ 50 px, même pendant un punch (règle : 864 × échelle maximale + |x| ≤ 910).
  - Ne l'augmente pas sans refaire ce calcul.
  - Le fond (`#ground`, noir avec un halo en bas) est hors caméra : il ne bouge pas.
- **Punch** : un zoom bref à ×1,04 en 0,42 s (`expo.out`) sur le moment fort.
  - Pose-le avec `sc.punch(T('…'))`.
  - Sans punch posé, le moteur en met un tout seul sur la première entrée qui grossit en `expo.out` (`sc.enter(..., 'pop')`, mais aussi un cadre `frame(..., entry='zoom')`) placée au milieu du plan (plan d'au moins 3 s, entre 0,9 s du début et 1,4 s de la fin).
  - Au plus 2 par plan, en alternance (×1,04 puis retour à ×1). Le moteur ignore ceux qui tombent à moins de 0,75 s du début ou de 0,6 s de la fin.

## 2. Les transitions entre plans

Chaque plan a une **entrée** (`s.entry`) et une **sortie** (`s.exit`) :

| Transition | Sortie du plan A | Entrée du plan B | Durée | Bruitage |
|---|---|---|---|---|
| **Fondu enchaîné** (la base) | `cut` : A s'efface pendant que B entre par-dessus (chevauchement de 0,25 s dans `build.py`) | `settle` : B arrive à ×1,05 et se pose à ×1 | 0,25 s ; pose 0,7 s | aucun |
| **Plan fouetté** | `whip` : A part à gauche (x −300, flou 18 px) | `whip` : B arrive de la droite (x 300 → 0, flou 18 px) | 0,17 s + 0,34 s | un whoosh court ou un souffle (`whoosh-court-a/b/c` ou `air`, volume 0,05), posé au début du plan B par `build.py` ; un seul whoosh par plan |
| **Zoom d'entrée** | `cut` | `zoomin` : B arrive à ×1,14 avec un flou de 10 px | 0,42 s | aucun |
| **Changement de partie** | `fade` : A s'éteint seul (flou 8 px), sans chevauchement | `zoomin`, puis l'écran de chapitre | 0,16 s + 0,42 s | aucun |

Le premier plan de la vidéo n'a pas d'entrée : à l'image 0, tout est déjà visible, car c'est l'image que voient les lecteurs avant de lancer.

**Choix automatique** (bas de `montage.py`, juste après les caméras) :

```python
for i, s in enumerate(SC):
    s.exit = 'cut'                                    # par défaut : fondu enchaîné
for i, s in enumerate(SC[:-1]):
    if SC[i + 1].chap: s.exit = 'fade'; SC[i + 1].entry = 'zoomin'     # nouvelle partie
    elif i % 4 == 1: s.exit = 'whip'; SC[i + 1].entry = 'whip'         # un plan sur quatre : fouetté
    elif i % 4 == 3: SC[i + 1].entry = 'zoomin'                         # un autre sur quatre : zoom d'entrée
```

Sur quatre plans, on a donc un fouetté, un zoom d'entrée et deux fondus enchaînés, plus un fondu et un zoom d'entrée à chaque partie. **Garde ce cycle tel quel d'une vidéo à l'autre** : c'est lui qui donne le rythme.

**Corriger une transition précise** : écris l'exception **après** la boucle, par numéro de plan, avec la raison en commentaire.

```python
SC[41].exit = 'fade'; SC[42].entry = 'settle'   # deux plans de texte : pas de fondu enchaîné (texte sur texte)
```

Défaut connu, encore ouvert sur le 32 Go : entre deux plans **de texte**, le fondu enchaîné de 0,25 s superpose les deux textes pendant 1 à 2 images. Si une planche ou une critique le montre, passe ce raccord en `fade` (exemple ci-dessus).

## 3. Les écrans de partie

- **Déclenchement** : `new('…', chap='Titre')` ouvre une partie ; le plan reçoit `chapter(sc, '01', 'Titre court', sub='précision')` (`blocs2.py`).
- **Animation** :
  - un grand numéro gris (300 px) arrive en 0,8 s (échelle 1,4 → 1, flou 20 px → 0) ;
  - un trait de 520 px se dessine de gauche à droite (0,7 s) ;
  - le titre (112 px) monte mot par mot, à 0,07 s d'écart (0,6 s par mot) ;
  - le sous-titre arrive en surtitre.
- **Son** : `chapter()` pose encore `riser-court` et `impact-doux`, mais `build.py` les retire (liste `BAN`). Un écran de partie est donc **silencieux**, et la musique continue dessous.
- **Combien** : 8 parties dans le 32 Go (8 `new(chap=…)`, donc 8 chapitres YouTube dans `chapitres.txt`), dont 6 avec un écran `chapter()` : l'introduction et « À la prochaine » ont un `chap=` sans écran de titre. Une partie dure au moins 10 s (règle YouTube des chapitres).

## 4. Les entrées d'éléments (dans un plan)

Avec `sc.enter(id, t, how)` :

| `how` | Effet | Durée, courbe | Pour |
|---|---|---|---|
| `blur` (défaut) | apparaît en sortant d'un flou de 10 px | 0,45 s, `power3.out` | texte, surtitre |
| `up` | monte de 34 px | 0,6 s, `power3.out` | pastille, légende sous une image |
| `down` | descend de 30 px | 0,6 s | élément du haut |
| `pop` | grossit de ×0,86 à ×1 | 0,6 s, `expo.out` | prix, chiffre, verdict (déclenche le punch automatique) |
| `left` / `right` | glisse de 220 px avec un flou de 16 px | 0,6 s, `expo.out` | carte qui arrive d'un côté |

Avec les cadres de `frame()` (captures, photos, vidéos), argument `entry=` :
- `rise` (défaut) : monte de 140 px en se redressant (rotationX 14° → 0, échelle 0,94 → 1, flou 12 px), 0,9 s ;
- `left` / `right` : glisse de 300 px en pivotant (rotationY 24°, flou 14 px), 0,85 s, et pose un whoosh court ;
- `zoom` : grossit de ×0,72 à ×1 (flou 14 px), 0,8 s ;
- `cut` : déjà là, pour une vidéo plein écran.

**Le texte de la vidéo de référence** : `ktg()` pose la phrase entière en gris fantôme dès l'ouverture du plan, puis l'allume en blanc mot par mot, au moment où la voix le dit. Le mot clé passe en couleur ; un mot barré passe en rouge.

Pour un changement d'état, utilise `sc.tw(..., kind='move')` (un cadre qui zoome sur la zone surlignée : `F.zoom(t, boîte)` ou `web(..., zoom='auto')`). Pour mettre en retrait : `sc.dim(id, t)`, qui baisse l'opacité à 0,3 avec un flou de 4 px. Pour retirer : `sc.out(id, t)`, en 0,25 s.

**Masquer un élément sans `opacity:0` dans son style**, sinon `check` lève `gsap_cold_seek_hidden_fromto_missing_reveal` : passe par `sc.tw` (`pieges.md`).

## 5. Le rythme

- **Durée d'un plan** : au moins 0,55 s (`new()` refuse en dessous).
- **Changement visible** : jamais plus de 8 s sans qu'un élément entre, s'allume ou zoome.
- **Avance d'une entrée** : au plus 0,4 s sur son mot, jamais un chiffre bien avant la voix (le moteur l'impose).
- **Premier élément** : il arrive dès l'ouverture du plan (à 0,08 s), sinon le plan s'ouvre vide.
- **Les 3 premières secondes de la vidéo** montrent déjà la promesse.
- **Mèmes** : ils s'arrêtent seuls 0,15 s avant le plan suivant (`visuels.md`).
- **Musique** : elle se coupe 0,35 s avant chaque chute et reprend 1,2 s après (`son.md`). Le silence fait partie de la transition.
- **Écran de fin** : `END = voix + 11 s`, caméra `none`, les deux cartes de vidéos entrent avec `zoom`, à 0,2 s d'écart.

## Vérifier

Les transitions ne se jugent pas sur une image fixe :
- **Planches** : extrais 3 images à cheval sur chaque raccord douteux (fin de A, milieu du chevauchement, début de B) et regarde-les (`verifications.md`).
- **`edit-plan/timeline.json`** donne le début, la durée, le chapitre et la caméra de chaque plan.
- **Ce que relèvent les critiques** :
  - texte sur texte pendant un fondu ;
  - une caméra qui pousse un texte trop près du bord ;
  - un fouetté sur un plan qui demande d'être lu (capture dense) ;
  - un plan qui attend sans rien de neuf.
