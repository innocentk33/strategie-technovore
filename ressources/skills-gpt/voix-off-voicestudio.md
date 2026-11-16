# Skill : voix-off-voicestudio (copie du 16/11/2026, tous ses fichiers à la suite)


---
## Fichier : voix-off-voicestudio/SKILL.md

---
name: voix-off-voicestudio
description: Coach pour rendre naturelle une voix off générée avec VoiceStudio (ex-OmniVoice Studio, alternative locale et open source à ElevenLabs, moteur OmniVoice par défaut). Prépare et annote un script avec les balises propres à VoiceStudio ([pause 500ms], [laughter], [sigh]), remplace les techniques ElevenLabs qui ne marchent pas ici (MAJUSCULES épelées, balises [excited]/[whispers] lues à voix haute), recommande les paramètres (class_temperature, num_step, guidance_scale, seed, speed, postprocess_output), aide au clonage et au Voice Design par attributs, et guide la génération par prises, le montage et le doublage intégré. Utilise ce skill dès que l'utilisateur mentionne VoiceStudio, OmniVoice, OmniVoice Studio, voicestudio.sh, ou veut adapter un script ou des réglages ElevenLabs à VoiceStudio, même s'il demande simplement de « préparer ce script », « améliorer la voix » ou « pourquoi ça sonne robotique » dans un contexte VoiceStudio.
---

# Voix off naturelle avec VoiceStudio

Une voix IA sonne fausse surtout parce qu'elle est **trop régulière** : même ton, même rythme, même intensité. Le travail consiste à réintroduire de la variation humaine — dans le texte, dans le clip de référence, dans la génération, puis au montage.

VoiceStudio n'est pas ElevenLabs : plusieurs réflexes ElevenLabs y **dégradent** le résultat. Ce skill adapte la méthode au moteur par défaut de VoiceStudio (OmniVoice). Si l'utilisateur a activé un autre moteur (CosyVoice 3, IndexTTS2, VoxCPM2…), consulte `references/parametres.md`, section « Autres moteurs ».

## Les 3 pièges à ne jamais oublier

1. **Les MAJUSCULES sont épelées.** Un mot écrit en capitales est lu lettre par lettre. Ne jamais utiliser les majuscules pour l'emphase. Les réserver aux sigles qui *doivent* être épelés (SNCF, PDG). Un sigle qui se prononce comme un mot s'écrit en minuscules avec une capitale initiale (Nasa, Otan, Unesco).
2. **Une balise inconnue est lue à voix haute.** VoiceStudio transmet le texte tel quel au moteur et ne supprime pas les balises qu'il ne connaît pas. `[excited]`, `[whispers]`, `[happy]`, `<break>` (ElevenLabs / SSML) seront prononcés. N'utiliser que les balises listées dans `references/balises-et-annotation.md`.
3. **Les balises longform ne marchent que dans les onglets Audiobook et Stories.** `[slow]…[/slow]`, `[fast]…[/fast]`, `[emphasis]…[/emphasis]`, `[spell]`, `[voice:NOM]` ne sont pas interprétées sur la page Voice (génération simple). Demande ou déduis dans quel onglet l'utilisateur génère avant de les utiliser.

## Les 4 piliers du réalisme (et leur traduction VoiceStudio)

1. **Variation du ton et du débit.** Se règle par la ponctuation, le paramètre `speed`, les balises `[slow]`/`[fast]` en longform, et surtout **le clip de référence** : le clonage reproduit la *manière de parler* du clip, pas seulement le timbre. Un clip plat donne une voix plate, un clip animé donne une voix animée. C'est le levier expressif le plus fiable du moteur par défaut.
2. **Pauses.** Utiliser `[pause]` (350 ms), `[pause 500ms]`, `[pause 1.5s]` (jusqu'à 10 s). Ces balises insèrent un vrai silence et fonctionnent sur tous les moteurs. Les `...` et les virgules restent utiles pour les micro-pauses et l'intonation.
3. **Emphase, sans majuscules.** Placer le mot fort en fin de phrase (l'accent tonique du français tombe en fin de groupe), l'isoler par une pause courte, écrire une phrase très courte, utiliser une tournure emphatique (« c'est … qui »), la répétition, ou `!`. En longform : `[emphasis]mot[/emphasis]`. Détails et exemples dans la référence.
4. **Un script écrit comme on parle.** Si le texte sonne rédigé ou généré par IA, signale-le et propose de le réécrire plus oralement avant d'annoter.

Sons non verbaux : n'utiliser que **`[laughter]`** (rire) et **`[sigh]`** (soupir). Les autres balises du moteur (`[question-ah]`, `[surprise-wa]`, `[confirmation-en]`, `[dissatisfaction-hnn]`…) ne produisent que des onomatopées (« ah », « oh », « wa ») sans intérêt pour une voix off : ne jamais les proposer.

Le moteur par défaut n'a **pas de contrôle d'émotion** (`[happy]`, `[sad]` ne sont pas reconnus). Le seul style de diction accepté est `whisper`, à régler via le champ de style / Voice Design, pas dans le texte.

## Identifier le besoin

- **A. Annoter un script** → lis `references/balises-et-annotation.md`, puis section A ci-dessous
- **B. Convertir un script ou des réglages ElevenLabs** → section B
- **C. Choisir / cloner / concevoir une voix** → section C
- **D. Paramètres de génération** → `references/parametres.md`
- **E. Générer, assembler, monter, doubler** → `references/montage-et-doublage.md`
- **F. Diagnostic** (« ça sonne robotique ») → vérifie d'abord les 3 pièges, puis le clip de référence, puis les paramètres (`class_temperature` à 0, clip plat, `postprocess_output` qui a supprimé des pauses voulues…), puis le montage.

## A. Annoter un script

Format de sortie :

```
LOT 1 — [intention : ex. « accroche, curieux »]
<texte annoté, prêt à coller>

LOT 2 — [intention]
<texte annoté>
```

Les lignes `LOT …` sont des repères de lecture : précise à l'utilisateur de ne coller que le texte sous chaque en-tête, sinon l'en-tête sera prononcé.

Après les lots, une section **Notes** courte :
- lots à générer plusieurs fois (moments clés) ;
- lots qui gagneraient à utiliser un autre profil de référence (plus énergique, plus posé), si l'utilisateur en a plusieurs ;
- mots à risque de prononciation (sigles, anglicismes, noms propres) avec une correction proposée (voir « Prononciation » dans la référence) ;
- phrases reformulées pour l'oral : dis-le clairement, ne change pas le fond en silence.

Avant de rendre un script annoté, vérifie-le avec le script fourni (voir plus bas). Si l'utilisateur veut un fichier, exporte en **.txt** par défaut.

## B. Convertir depuis ElevenLabs

Applique cette table, puis vérifie avec le script :

| ElevenLabs | VoiceStudio (moteur par défaut) |
|---|---|
| MOT EN MAJUSCULES (emphase) | minuscules + position finale / pause courte / phrase courte ; `[emphasis]…[/emphasis]` en longform |
| `[excited]`, `[whispers]`, `[sad]`… (v3) | supprimer. Énergie : ponctuation + clip de référence animé. Chuchotement : style `whisper` |
| `<break time="1s"/>` | `[pause 1s]` |
| `...` et `!` | inchangés, fonctionnent aussi |
| Rire, soupir implicites | `[laughter]`, `[sigh]` |

Pour la correspondance des réglages (stabilité, similarité, exagération du style, vitesse), vois `references/parametres.md`.

## C. Voix : cloner ou concevoir

**Clonage (recommandé pour le français).**
- Clip de référence de **3 à 10 s** (20 s max si on fournit la transcription).
- Enregistré **sec et près du micro** : l'écho du clip se retrouve dans la voix clonée.
- Fournir la transcription exacte du clip améliore le résultat.
- Choisir un clip dont la diction correspond au ton voulu.

Astuce clé pour la variation : enregistrer **2 ou 3 clips de sa propre voix avec des énergies différentes** (posé, enthousiaste, confidentiel), en faire des profils distincts, puis choisir le profil selon l'intention de chaque lot. Vérifie à l'écoute que le timbre reste cohérent d'un profil à l'autre.

**Consentement.** Ne cloner que sa propre voix ou une voix pour laquelle on a l'autorisation. Si la demande vise la voix de quelqu'un d'autre, propose un Voice Design ou un clip de l'utilisateur lui-même.

**Voice Design (sans clip).** Le moteur par défaut ne comprend qu'un vocabulaire fixe d'attributs. Il ignore les descriptions libres.
- **Genre** : male / female
- **Âge** : child / teenager / young adult / middle-aged / elderly
- **Hauteur** : very low / low / moderate / high / very high pitch
- **Style** : whisper
- **Accent anglais** : american, british, australian, canadian, indian, chinese, korean, japanese, portuguese, russian — seulement si le texte est en anglais
- **Dialectes chinois** : seulement si le texte est en chinois

Traduis toujours une description (« homme jeune, voix grave et charismatique ») en chaîne d'attributs : `male, young adult, low pitch`. Précise ce qui sera ignoré (« charismatique »).

Le Voice Design est entraîné sur l'anglais et le chinois et peut être instable dans d'autres langues. Pour une voix off en français, préfère le clonage. Pour une description libre, le moteur VoxCPM2 l'accepte.

Une fois une prise réussie, **épingler la seed** (« Keep this seed » ou verrouiller le profil depuis l'historique) pour retrouver exactement la même voix.

## Le « secret » : générer par petits lots et multiplier les prises

- Générer lot par lot (1 à 3 phrases), pas tout le script d'un coup.
- La seed n'est pas épinglée par défaut, donc **chaque rendu diffère légèrement**. En local, les prises ne coûtent rien : en générer 2 à 4 par lot important.
- Au montage, choisir la meilleure prise par phrase et **combiner des morceaux de plusieurs prises**. L'assemblage de ces variations imite la parole humaine.
- Nommer les fichiers systématiquement : `lot01_v1.wav`, `lot01_v2.wav`…

Alternative pour les longs scripts : l'onglet **Stories / Audiobook** rend tout le texte d'un coup. Il gère des silences maîtrisés entre lignes et paragraphes, la vitesse par ligne, les balises longform, et l'option **Vary repeated lines**. Détails dans `references/montage-et-doublage.md`.

## Script de vérification

`scripts/verifier_script.py` repère dans un script annoté :
- les mots en majuscules (qui seront épelés) ;
- les balises inconnues (qui seront lues à voix haute) ;
- les balises longform utilisées en mode Voice ;
- les pauses de plus de 10 s ;
- les lots de plus de 4 096 caractères.

```bash
python scripts/verifier_script.py script.txt --mode voice      # page Voice
python scripts/verifier_script.py script.txt --mode longform   # Audiobook / Stories
```

Lance-le sur ta propre sortie avant de la rendre. Corrige ce qu'il signale, ou explique pourquoi un sigle en majuscules est voulu.

## Documentation à jour

VoiceStudio évolue vite (renommé depuis OmniVoice Studio, interface Electron). Si un paramètre ou un menu ne correspond pas à ce que voit l'utilisateur, consulte :
- https://voicestudio.sh/docs
- `docs/expressive-speech.md`, `docs/generation-parameters.md` et `docs/voice-design.md` sur https://github.com/debpalash/VoiceStudio

Ne promets jamais un effet qu'un moteur ne supporte pas.

Réponds dans la langue de l'utilisateur ; annote le script dans la langue du script.


---
## Fichier : voix-off-voicestudio/references/balises-et-annotation.md

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


---
## Fichier : voix-off-voicestudio/references/montage-et-doublage.md

# Génération, montage et doublage avec VoiceStudio

## 1. Deux façons de générer

**Page Voice (lot par lot).** Idéale pour la méthode des prises multiples.
- Coller un lot, générer 2 à 4 fois (la seed non épinglée donne une prise différente à chaque fois), télécharger chaque prise, passer au lot suivant.
- Changer de profil de référence selon l'intention du lot si l'utilisateur en a plusieurs.
- Les balises longform ne fonctionnent pas ici.

**Onglet Stories / Audiobook (script entier).** Pratique pour une première version complète ou un long script.
- Accepte `[slow]`, `[fast]`, `[emphasis]`, `[voice:NOM]`, une vitesse globale et une vitesse par ligne.
- Gère les jointures :
  - « Trim engine silence » coupe le silence ajouté par le moteur ;
  - « Gap between lines » ajoute un silence entre les lignes (250 ms par défaut) ;
  - « Gap between paragraphs » ajoute un silence aux lignes vides (350 ms).
- Une `[pause]` explicite remplace l'écart entre lignes au lieu de s'y ajouter.
- « Vary repeated lines » donne une prise différente aux lignes identiques.
- Chaque chapitre peut être pré-écouté.

Approche mixte conseillée :
1. Rendre tout le script dans Stories pour avoir une base.
2. Régénérer les moments clés sur la page Voice avec plusieurs prises.
3. Remplacer ces passages au montage.

## 2. Assembler les prises (Premiere Pro, DaVinci, CapCut…)

1. Importer toutes les prises et les poser dans l'ordre du script sur une piste.
2. Pour chaque phrase, écouter les versions et garder celle qui colle au contexte.
3. Pour les phrases importantes, **combiner des morceaux de plusieurs prises**. C'est là que le résultat devient le plus humain.
4. Couper les blancs superflus, en **gardant des pauses volontaires** sur les moments importants.

## 3. Vitesse

- Régler `speed` à la génération plutôt qu'au montage : l'étirement temporel des logiciels de montage déforme souvent la voix.
- Pour caler une phrase sur une durée précise, utiliser le paramètre `duration`.
- En dernier recours, ajuster le rythme en jouant sur les pauses plutôt que sur la voix.

## 4. Égalisation

VoiceStudio applique déjà un **filtre passe-haut et un compresseur** à chaque rendu (24 kHz mono). Au montage :
- Pas de gros passe-haut supplémentaire : vérifier d'abord à l'oreille.
- Chercher les résonances désagréables : augmenter fortement une bande étroite, la balayer, puis atténuer la fréquence gênante.
- Éviter les préréglages d'effet qui ajoutent de la réverbération (Cinematic, Warm) pour une voix off, sauf si c'est voulu.
- Un clip de référence enregistré dans une pièce qui résonne donne une voix clonée qui résonne. Il vaut mieux réenregistrer le clip que corriger au montage.
- Enregistrer le réglage final en preset pour garder un son cohérent d'une vidéo à l'autre.

## 5. Doublage (espace « Dub » intégré)

VoiceStudio a son propre atelier de doublage : pas besoin de passer par ElevenLabs.

**Préparer**
1. Ouvrir Dub, importer la vidéo, l'audio, ou une URL.
2. La transcription se fait automatiquement.
3. Choisir le fournisseur de traduction dans Settings > Models > Translation.

**Traduire et relire**
4. Choisir une ou plusieurs langues cibles et traduire.
5. **Relire la traduction** segment par segment : c'est le point le plus important pour un rendu naturel.

**Régler les voix et le timing**
6. Attribuer une voix par locuteur. L'attribution automatique est active par défaut. Pour garder sa propre voix, choisir son profil cloné.
7. Chaque segment peut avoir son volume, sa vitesse et une note de direction.
8. La timeline permet de déplacer et redimensionner les segments, et signale les chevauchements.

**Générer et contrôler**
9. Générer. Vérifier les segments manquants ou en échec, et les dépassements de timing, avant d'exporter.
10. Si une traduction est trop longue, le mode de calage (Strict Slot) l'accélère en conservant la hauteur, ce qui peut sonner précipité. Dans ce cas, **raccourcir la traduction** plutôt que d'accélérer la voix.

**Exporter**
11. Choisir la piste, le format et le mixage avec la musique et les effets d'origine.
12. Pour YouTube, exporter l'**audio seul** de la piste doublée.

Variante pour plus de contrôle : exporter soi-même, depuis le logiciel de montage, une piste voix seule et une piste musique/effets. Doubler la piste voix, puis remonter trois pistes (voix originale comme guide de timing, voix doublée, ambiance) avant d'exporter.

**Publier sur YouTube**
1. YouTube Studio → **Langues** → choisir la vidéo.
2. Supprimer le doublage automatique de YouTube s'il existe pour cette langue.
3. Ajouter la langue et envoyer le fichier audio.
4. Traduire le titre et la description.
5. Dans les statistiques, regarder les vues **par piste audio** pour mesurer l'effet du doublage.

Les menus de VoiceStudio et de YouTube Studio évoluent. En cas d'écart avec l'interface, vérifier la documentation actuelle.


---
## Fichier : voix-off-voicestudio/references/parametres.md

# Paramètres de génération VoiceStudio

Ces réglages se trouvent dans le panneau **Production Overrides**, disponible sur la page Voice et dans l'onglet Audiobook. Par l'API locale (`http://localhost:3900`), ce sont les mêmes noms de champs.

## Sommaire
1. Correspondance ElevenLabs → VoiceStudio
2. Tous les paramètres utiles
3. Préréglage de départ pour une voix off
4. Faire respirer la voix
5. Autres moteurs

## 1. Correspondance ElevenLabs → VoiceStudio

| Réglage ElevenLabs (méthode d'origine) | Équivalent VoiceStudio | Commentaire |
|---|---|---|
| Stabilité basse | `class_temperature` ↑ (défaut 0, essayer 0,3 à 0,7) ; `position_temperature` (défaut 5,0) | Plus de variation expressive, mais aussi plus d'artefacts (mots mâchés, dérive du timbre). Monter par petites touches. |
| Similarité ~70 % | Qualité du clip de référence + `guidance_scale` (défaut 2,0) | La fidélité au timbre dépend surtout du clip : 3 à 10 s, sec, proche du micro, avec sa transcription. Garder 2,0 et n'ajuster qu'en comparant à l'oreille. |
| Exagération du style ↑ | Aucun paramètre équivalent | Utiliser un clip de référence plus animé : le clonage copie la diction. |
| Vitesse | `speed` (1,0 = normal, >1 plus rapide) ; `[slow]`/`[fast]` en longform ; vitesse par ligne dans Stories | Régler à la génération plutôt qu'au montage. |
| Choix du modèle v2 / v3 | Choix du moteur (Model Catalogue) | Par défaut : OmniVoice. Voir « Autres moteurs ». |
| Régénérations gratuites | Seed non épinglée | Chaque rendu diffère, et en local c'est illimité. |
| — | `num_step` | 16 = rapide (défaut de la page Voice), 32 = plus propre (défaut Audiobook). |
| — | `postprocess_output` | Actif par défaut, supprime les longs silences. |
| — | Seed | Épingler une prise réussie pour la reproduire à l'identique. |

## 2. Paramètres utiles

- **`num_step`**
  - 16 pour tester vite.
  - 32 pour le rendu final.
  - Moins d'étapes donne un son plus rugueux, parfois un peu plus « humain » : à tester, sans en faire une règle.
- **`guidance_scale`** (2,0) : guidage du conditionnement. Rester proche de la valeur par défaut.
- **`class_temperature`** (0 = déterministe) : le principal levier de variation.
- **`position_temperature`** (5,0) : aléatoire sur l'ordre de génération. Rarement besoin d'y toucher.
- **`speed`** : facteur de vitesse. `duration` (durée fixe en secondes) est prioritaire sur `speed` s'il est défini, ce qui est utile pour caler une phrase sur un plan.
- **`postprocess_output`** : le désactiver quand les silences naturels font partie de la performance. Les `[pause]` balisées ne sont pas concernées.
- **Seed** : non épinglée par défaut. L'historique affiche la seed de chaque prise ; « Keep this seed » ou le verrouillage du profil la fixe. L'onglet Audiobook accepte une seed globale.
- **Style / instruct** : sur le moteur par défaut, seulement les attributs du Voice Design. Le seul style de diction est `whisper`. Si le style et le clip se contredisent, c'est le clip qui gagne.

Le moteur produit du 24 kHz mono, avec une chaîne de mastering automatique (filtre passe-haut + compresseur).

## 3. Préréglage de départ pour une voix off

À présenter comme un point de départ à tester sur un lot, pas comme une vérité :

- **Moteur** : OmniVoice par défaut, avec un profil cloné à partir d'un clip animé.
- **`num_step`** : 32
- **`guidance_scale`** : 2,0
- **`class_temperature`** : générer le même lot à 0, 0,3 et 0,5, puis choisir à l'oreille.
- **`speed`** : 1,0 à 1,1 selon le débit naturel de la voix.
- **`postprocess_output`** : actif, sauf si le script repose sur des silences non balisés.
- **Seed** : non épinglée pendant la phase de prises multiples ; épinglée pour refaire une prise précise.

## 4. Faire respirer la voix (moteur par défaut)

Il n'y a pas de balise `[breath]` sur le moteur par défaut. Voici la méthode de contournement, dans l'ordre d'efficacité :

1. **Mettre les respirations dans le clip de référence** : 8 à 15 s avec des inspirations audibles entre les phrases. Le clone reprend cette diction.
2. **Écrire des fragments courts avec des pauses** : `Je peux pas... [pause 300ms] je peux plus...`
3. **Désactiver `postprocess_output`**, pour ne pas couper les silences où se trouvent les respirations.
4. **Monter `class_temperature` à 0,3–0,7** et générer plusieurs prises.
5. **Garder la meilleure** et épingler sa seed.

C'est un contournement : l'aléatoire qui produit une belle respiration produit aussi des mots mal articulés. Pour des respirations placées précisément, utiliser CosyVoice 3.

## 5. Autres moteurs (à installer, optionnels)

- **CosyVoice 3**
  - Balises `[breath]` et `[laughter]`, emphase `<strong>mot</strong>`.
  - Instructions en langage naturel (« parle comme quelqu'un d'épuisé »), actuellement seulement via l'API.
  - Installation non triviale.
- **IndexTTS2**
  - Seul moteur avec des émotions graduées : 8 émotions (joyeux, en colère, triste, effrayé, dégoûté, mélancolique, surpris, calme), un clip d'émotion de référence, ou une description d'émotion avec un curseur d'intensité.
  - Réglable dans l'onglet Audiobook ou via l'API `/ws/tts`.
- **VoxCPM2**
  - Instruction en préfixe dans le texte : `(parle vite, essoufflé) Je peux pas m'arrêter.`
  - Accepte aussi une description libre en Voice Design.
  - L'adhérence varie selon la voix et la langue.
- **OmniVoice GGUF** : même modèle, quantifié, pour les petites cartes graphiques (moins de 6 Go de VRAM) ou le CPU.

Les balises non verbales `[laughter]` et `[sigh]` sont propres au moteur par défaut (CosyVoice 3 a aussi `[laughter]`) : ne pas les supposer disponibles sur les autres moteurs.


---
## Fichier : voix-off-voicestudio/scripts/verifier_script.py

#!/usr/bin/env python3
"""Vérifie un script annoté pour VoiceStudio (moteur par défaut OmniVoice).

Usage:
    python verifier_script.py script.txt [--mode voice|longform]
    cat script.txt | python verifier_script.py - --mode voice

Signale :
  - mots en MAJUSCULES (épelés lettre par lettre par VoiceStudio)
  - onomatopées non voulues ([question-*], [surprise-*]…), seuls [laughter]/[sigh] sont gardés
  - balises inconnues (lues à voix haute), dont les balises ElevenLabs/SSML
  - balises longform ([slow], [fast], [emphasis], [spell], [voice:]) en mode voice
  - pauses > 10 s ou mal formées
  - lots > 4096 caractères
Les lignes d'en-tête "LOT …" et la section "Notes" sont ignorées.
"""
import argparse
import re
import sys

USEFUL_NONVERBAL = {"laughter", "sigh"}
NONVERBAL = {
    "laughter", "sigh", "confirmation-en", "question-en", "question-ah",
    "question-oh", "question-ei", "question-yi", "surprise-ah", "surprise-oh",
    "surprise-wa", "surprise-yo", "dissatisfaction-hnn",
}
LONGFORM = {"slow", "/slow", "fast", "/fast", "emphasis", "/emphasis", "spell", "/spell"}
ELEVENLABS_HINT = {
    "excited", "whispers", "whisper", "happy", "sad", "angry", "sarcastic",
    "curious", "laughs", "laughing", "sighs", "breath", "breathes", "shouts",
    "crying", "giggles", "exhales", "inhales",
}
MAX_CHARS = 4096
PAUSE_RE = re.compile(r"^pause(?:\s+(\d+(?:[.,]\d+)?)\s*(ms|s))?$", re.I)
TAG_RE = re.compile(r"\[\[.*?\]\]|\[[^\[\]]*\]|<[^<>]+>")
CAPS_RE = re.compile(r"\b[A-ZÀÂÄÇÉÈÊËÎÏÔÖÙÛÜŸÆŒ]{2,}\b")
HEADER_RE = re.compile(r"^\s*LOT\s+\d+", re.I)
NOTES_RE = re.compile(r"^\s*\**\s*Notes?\s*\**\s*:?\s*$", re.I)


def split_lots(text):
    lots, current, in_notes = [], [], False
    for line in text.splitlines():
        if NOTES_RE.match(line):
            in_notes = True
            continue
        if HEADER_RE.match(line):
            in_notes = False
            if current:
                lots.append(current)
            current = [(None, line)]
            continue
        if not in_notes:
            current.append((True, line))
    if current:
        lots.append(current)
    return lots


def check_tag(tag, mode):
    if tag.startswith("[["):
        return None  # prononciation forcée
    if tag.startswith("<"):
        name = tag.strip("<>/").split()[0].lower()
        if name == "strong":
            return f"{tag} : emphase CosyVoice 3 seulement, lue à voix haute sur le moteur par défaut"
        return f"{tag} : balise SSML/HTML non reconnue, sera lue à voix haute (pause → [pause 1s])"
    inner = tag[1:-1].strip()
    low = inner.lower()
    if low in USEFUL_NONVERBAL:
        return None
    if low in NONVERBAL:
        return f"{tag} : simple onomatopée (ah/oh/wa…), à retirer ; exprimer l'idée par le texte et la ponctuation"
    m = PAUSE_RE.match(inner)
    if m:
        if m.group(1):
            val = float(m.group(1).replace(",", "."))
            secs = val / 1000 if m.group(2).lower() == "ms" else val
            if secs > 10:
                return f"{tag} : pause > 10 s (maximum 10 s)"
        return None
    if low.startswith("pause"):
        return f"{tag} : pause mal formée (formats : [pause], [pause 500ms], [pause 1.5s])"
    if low in LONGFORM or low.startswith("voice:"):
        if mode == "voice":
            return f"{tag} : balise longform, ignorée/lue sur la page Voice (Audiobook/Stories seulement)"
        return None
    if low in ELEVENLABS_HINT:
        return f"{tag} : balise de type ElevenLabs, non reconnue, sera lue à voix haute"
    return f"{tag} : balise inconnue, sera lue à voix haute"


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("path")
    ap.add_argument("--mode", choices=["voice", "longform"], default="voice")
    args = ap.parse_args()
    text = sys.stdin.read() if args.path == "-" else open(args.path, encoding="utf-8").read()

    issues = 0
    for i, lot in enumerate(split_lots(text), 1):
        header = next((l for k, l in lot if k is None), f"(bloc {i})").strip()
        body_lines = [l for k, l in lot if k]
        body = "\n".join(body_lines).strip()
        if not body:
            continue
        problems = []
        if len(body) > MAX_CHARS:
            problems.append(f"lot de {len(body)} caractères (> {MAX_CHARS}) : le découper")
        for tag in TAG_RE.findall(body):
            msg = check_tag(tag, args.mode)
            if msg:
                problems.append(msg)
        without_tags = TAG_RE.sub(" ", body)
        for word in sorted(set(CAPS_RE.findall(without_tags))):
            problems.append(
                f"« {word} » en majuscules : sera épelé. OK si sigle à épeler, "
                f"sinon l'écrire en minuscules (emphase par position/pause)"
            )
        tags_nv = [t for t in TAG_RE.findall(body) if t[1:-1].lower() in USEFUL_NONVERBAL]
        if len(tags_nv) > 1:
            problems.append(f"{len(tags_nv)} sons non verbaux ([laughter]/[sigh]) dans ce lot : en garder un au plus")
        if problems:
            print(header)
            for p in problems:
                print(f"  - {p}")
            issues += len(problems)

    if issues == 0:
        print(f"Aucun problème détecté (mode {args.mode}).")
    else:
        print(f"\n{issues} point(s) à vérifier (mode {args.mode}).")
    return 0


if __name__ == "__main__":
    sys.exit(main())

