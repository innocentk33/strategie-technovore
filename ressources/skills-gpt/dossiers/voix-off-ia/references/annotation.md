# Annoter un script pour une voix IA

## Objectif

Transformer un texte « à lire » en texte « à dire ». La ponctuation et la casse sont les seuls leviers de mise en scène dont dispose le moteur de synthèse (hors balises spécifiques à certains modèles) : on s'en sert comme d'indications de jeu pour un acteur.

## Les outils

| Signe | Effet recherché | Quand l'utiliser |
|---|---|---|
| `...` | hésitation, déception, confusion, suspense, pause courte | avant une chute, une révélation, une réplique ironique ; quand le narrateur « cherche ses mots » |
| `!` | énergie, enthousiasme, surprise | accroches, moments forts, réactions ; en ajouter plusieurs (`!!`) si l'effet ne passe pas |
| `,` | micro-pause, respiration | pour casser une phrase trop longue, isoler un mot |
| MAJUSCULES | emphase | le mot porteur de sens de la phrase ; un seul en général |
| `?` | intonation montante | questions rhétoriques adressées au spectateur |

## Règles de dosage

- **Pas d'emphase partout.** Si trois mots sont en majuscules dans une phrase, aucun ne ressort. Vise un mot par phrase au maximum, et pas dans chaque phrase.
- **Varier d'un lot à l'autre.** Alterne lots calmes et lots énergiques : c'est la variation globale qui fait humain, pas l'intensité constante.
- **Majuscules et mots courts** : un mot très court ou ressemblant à un sigle peut être épelé lettre par lettre. Préviens l'utilisateur de tester ces cas.
- **Couper les phrases longues** : une phrase de plus de ~25 mots gagne presque toujours à être scindée ou ponctuée.

## Conseils complémentaires (bonnes pratiques TTS générales)

Ces points ne viennent pas de la méthode de base mais évitent des erreurs de prononciation fréquentes ; présente-les comme des suggestions :
- Écrire les nombres, dates et unités en toutes lettres si la prononciation est ambiguë (« 2,5 Md » → « deux milliards et demi »).
- Écrire phonétiquement les sigles et noms propres difficiles, ou signaler qu'ils sont à vérifier.
- Remplacer les symboles (`%`, `&`, `→`) par des mots.

## Découpage en lots

- 1 à 3 phrases par lot, en coupant là où l'intention change.
- Un moment clé (accroche, chute, révélation) = son propre lot, pour pouvoir le générer plusieurs fois et choisir.
- Donne à chaque lot une intention en quelques mots (« confidentiel », « montée d'énergie », « ironique »).

## Exemples

**Exemple 1 (anglais, tiré de la méthode de référence)**

Avant :
```
Say my name. You're Isaac. You're goddamn right.
```
Après :
```
Say my NAME! You're ISAAC... You're GODDAMN RIGHT!!
```
Même texte, mais la ponctuation crée une montée d'intensité et les majuscules désignent les mots qui portent la réplique.

**Exemple 2 (français)**

Avant :
```
En 2012, l'entreprise valait 3 milliards. Deux ans plus tard, elle ne valait plus rien. Et personne n'avait vu venir la chute.
```
Après :
```
LOT 1 — posé, on installe
En deux mille douze, l'entreprise valait TROIS milliards.

LOT 2 — chute, suspense
Deux ans plus tard... elle ne valait plus RIEN.

LOT 3 — confidentiel
Et personne, absolument personne, n'avait vu venir la chute.
```
Notes : pause longue à ajouter au montage entre les lots 1 et 2 ; générer le lot 2 plusieurs fois, c'est le moment fort.

**Exemple 3 (ce qu'il ne faut pas faire)**
```
C'est VRAIMENT INCROYABLE!!! Personne ne S'ATTENDAIT à ÇA!!!
```
Tout est accentué, donc rien ne l'est, et la voix sature. Préférer :
```
C'est vraiment INCROYABLE ! Personne ne s'attendait à ça...
```
