# Balises VoiceStudio et règles d'annotation

## Sommaire
1. Balises disponibles (par onglet et par moteur)
2. Sons non verbaux : `[laughter]` et `[sigh]` uniquement
3. Pauses
4. Emphase sans majuscules
5. Prononciation
6. Dosage
7. Exemples

## 1. Balises disponibles

| Balise | Où | Effet |
|---|---|---|
| `[pause]`, `[pause 500ms]`, `[pause 1.5s]` | partout, tous moteurs | vrai silence inséré (350 ms par défaut, 10 s max) |
| `[laughter]`, `[sigh]` | moteur par défaut (VoiceStudio/OmniVoice) | rire, soupir (voir section 2) |
| `[[…]]` | partout | forcer une prononciation |
| `[slow]…[/slow]` | Audiobook / Stories seulement | ralentit (vitesse ≈ 0,85) |
| `[fast]…[/fast]` | Audiobook / Stories seulement | accélère (≈ 1,15) |
| `[emphasis]…[/emphasis]` | Audiobook / Stories seulement | emphase douce = léger ralentissement (≈ 0,92) |
| `[spell]…` | Audiobook / Stories seulement | épeler |
| `[voice:NOM]` | Audiobook / Stories seulement | changer de voix (multi-voix) |
| `[breath]`, `<strong>mot</strong>` | CosyVoice 3 seulement | respiration audible, emphase |

**Tout le reste est lu à voix haute** : `[excited]`, `[whispers]`, `[happy]`, `[sad]`, `[breath]` sur le moteur par défaut, les balises SSML `<break>` / `<emphasis>`, etc.

Les balises longform découpent la ligne en plusieurs rendus (un par segment de vitesse différente). Une ligne très fragmentée peut donc présenter des micro-ruptures : à écouter.

## 2. Sons non verbaux : `[laughter]` et `[sigh]` uniquement

Le moteur par défaut reconnaît 13 balises non verbales (bouton ⊕ Insert du champ Script), mais **seules deux sont utiles pour une voix off** :
- `[laughter]` : rire
- `[sigh]` : soupir

Les 11 autres (`[confirmation-en]`, `[question-en/ah/oh/ei/yi]`, `[surprise-ah/oh/wa/yo]`, `[dissatisfaction-hnn]`) produisent seulement des onomatopées (« ah », « oh », « wa »…), calibrées pour une diction de type mandarin. Elles n'apportent rien : ne pas les utiliser ni les proposer. Pour exprimer la surprise ou le questionnement, passer par le texte et la ponctuation (« Attends... quoi ? », « Et là, surprise ! »).

Ce qu'il faut savoir :
- **Le rendu dépend de la voix.** Un rire qui passe très bien avec un clip de référence peut sortir atténué avec un autre.
- **Il n'y a pas de réglage d'intensité.**
- **Il n'y a pas de `[breath]`** sur le moteur par défaut. Pour des respirations audibles, voir `parametres.md` (« Faire respirer la voix »).

Placement naturel :
- `[laughter]` juste **après** une chute ou une blague.
- `[sigh]` juste **avant** une phrase déçue ou résignée.

## 3. Pauses

- `[pause 150ms]` à `[pause 300ms]` : isoler un mot, respiration.
- `[pause 500ms]` à `[pause 1s]` : avant une révélation, entre deux idées.
- Plus de `[pause 1.5s]` : effet dramatique, à utiliser rarement.
- `...` : pause courte **et** intonation suspendue ou hésitante. Les deux se combinent : `Et là... [pause 400ms] plus rien.`
- Virgules : micro-pauses et respiration dans une phrase longue.

Si l'utilisateur compte sur des silences **naturels** (non balisés), il doit désactiver `postprocess_output`, qui supprime les longs silences. Les `[pause]` sont insérées comme du silence réel et ne dépendent pas de ce réglage.

## 4. Emphase sans majuscules

Les majuscules étant épelées, voici les techniques, de la plus fiable à la plus subtile :

1. **Position finale.** En français, l'accent tombe en fin de groupe. Déplace le mot fort à la fin : « Il a tout perdu en deux ans » → « En deux ans, il a tout perdu. »
2. **Isoler par une pause.** `Et tout ça pour... [pause 250ms] rien.`
3. **Phrase ultra-courte ou fragment.** « Rien. Absolument rien. »
4. **Tournure emphatique.** « C'est ce détail qui a tout changé. »
5. **Répétition.** « Personne. Personne n'avait vu venir ça. »
6. **Point d'exclamation** pour l'énergie (sans en abuser).
7. **Longform** : `[emphasis]mot[/emphasis]`. Effet doux (léger ralentissement), donc à combiner avec les techniques ci-dessus.

Sigles :
- Sigle épelé (SNCF, PDG, IA) : garder les majuscules, c'est voulu.
- Sigle prononcé comme un mot : minuscules avec capitale initiale (Nasa, Otan, Unesco, Covid).
- Nom de marque stylisé en capitales (ex. « IKEA ») : l'écrire comme il se prononce (« Ikea »).

## 5. Prononciation

- `[[…]]` en ligne force une prononciation. Il existe aussi un dictionnaire de prononciation dans l'application pour les mots récurrents (nom de la chaîne, noms propres).
- Anglais : phonèmes CMU entre crochets (ex. `[B EY1 S]`).
- Nombres, dates, symboles : les écrire en toutes lettres quand la lecture est ambiguë (« 2,5 Md€ » → « deux milliards et demi d'euros »). C'est plus sûr que de compter sur la normalisation automatique.
- Anglicismes dans un texte français : les tester. Si la prononciation est mauvaise, écrire une graphie phonétique à la française ou utiliser `[[…]]`.

## 6. Dosage

- Un `[laughter]` ou `[sigh]` par lot au maximum, et pas dans chaque lot. Sinon l'effet devient mécanique, c'est-à-dire exactement ce qu'on cherche à éviter.
- Alterner lots posés et lots énergiques : c'est la variation globale qui fait humain.
- 1 à 3 phrases par lot. Un moment clé forme un lot à lui seul, pour pouvoir farmer les prises.
- Phrases de plus de ~25 mots : les couper ou les ponctuer.

## 7. Exemples

**Conversion d'une ligne ElevenLabs**

Avant (ElevenLabs) :
```
Say my NAME! You're ISAAC... You're GODDAMN RIGHT!!
```
Après (VoiceStudio) :
```
Say my name! [pause 300ms] You're Isaac... [pause 400ms] You're goddamn right!!
```
Les majuscules auraient été épelées (« N-A-M-E »). L'emphase passe ici par les pauses qui isolent chaque réplique et par la ponctuation.

**Script français**

Avant :
```
En 2012, l'entreprise valait 3 milliards. Deux ans plus tard, elle ne valait plus rien. Et personne n'avait vu venir la chute.
```
Après :
```
LOT 1 — posé, on installe
En deux mille douze, l'entreprise valait trois milliards.

LOT 2 — chute, suspense
[pause 600ms] Deux ans plus tard... [pause 300ms] plus rien.

LOT 3 — confidentiel
[sigh] Et personne, absolument personne, n'avait vu venir la chute.
```
Notes :
- Lot 2 : générer 3 à 4 prises, c'est le moment fort. « Plus rien » en fin de phrase, isolé par une pause, remplace l'emphase.
- Lot 3 : si l'utilisateur a un profil « posé / confidentiel », l'utiliser ici.

**À ne pas faire**
```
C'est VRAIMENT INCROYABLE [excited] !!! [laughter] [surprise-wa]
```
Problèmes :
- « VRAIMENT INCROYABLE » sera épelé.
- `[excited]` sera prononcé.
- `[surprise-wa]` ne produit qu'une onomatopée « wa ».
- Deux sons non verbaux à la suite sonnent artificiel.

Mieux :
```
Attends... [pause 300ms] c'est vraiment incroyable !
```
