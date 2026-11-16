# Skill : voix-off-ia (copie du 16/11/2026, tous ses fichiers à la suite)


---
## Fichier : voix-off-ia/SKILL.md

---
name: voix-off-ia
description: Coach pour rendre une voix off IA (ElevenLabs ou équivalent) naturelle et humaine. Prépare et annote un script pour la génération (ponctuation, MAJUSCULES d'emphase, pauses, découpage en lots), aide à choisir, cloner ou concevoir une voix (prompt de Voice Design), recommande les réglages, et guide l'assemblage des prises, le montage audio, l'égalisation et le doublage multilingue. Utilise ce skill dès que l'utilisateur parle de voix off, voiceover, voix IA, text-to-speech, TTS, ElevenLabs, clonage de voix, doublage ou traduction audio de vidéo, ou dit que sa voix IA « sonne robotique », « fait faux », « manque de vie », même s'il ne demande pas explicitement de l'aide sur la voix — par exemple s'il colle un script en demandant de le « préparer pour ElevenLabs » ou veut savoir « quelle voix utiliser ».
---

# Voix off IA — rendre une voix synthétique humaine

Ce skill aide à produire une voix off IA qui ne trahit pas son origine. L'idée centrale : une voix IA sonne fausse surtout parce qu'elle est **trop régulière** (même ton, même rythme, même intensité, du début à la fin). Tout le travail consiste à réintroduire de la variation humaine — dans le texte, dans la génération, puis au montage.

## Les 4 piliers du réalisme

Garde-les en tête pour tout conseil et toute annotation, et explique-les à l'utilisateur quand c'est utile :

1. **Variation du ton et du débit** — une voix monocorde sonne robotique ; des montées d'énergie, des passages plus calmes, des accélérations et ralentissements sonnent humains.
2. **Pauses** — supprimer tous les silences rend la voix mécanique. Garder des pauses volontaires avant ou après les idées importantes renforce l'impact.
3. **Emphase** — accentuer quelques mots clés donne du relief.
4. **Un script écrit comme on parle** — un texte générique ou rédigé entièrement par IA finit par sonner robotique, quelle que soit la qualité de la voix. Si le script a ce ton (phrases trop lisses, transitions artificielles, listes déguisées en phrases), signale-le et propose de le réécrire plus oralement avant de l'annoter.

## Identifier le besoin

Les demandes tombent dans une ou plusieurs de ces catégories. Repère laquelle, puis va à la section correspondante :

- **A. Préparer / annoter un script** pour la génération → section « Annoter un script »
- **B. Choisir ou créer une voix** → section « Choisir la voix »
- **C. Réglages de génération** → section « Réglages »
- **D. Générer et assembler** (workflow, montage, EQ) → `references/montage-et-doublage.md`
- **E. Doubler une vidéo** dans d'autres langues → `references/montage-et-doublage.md`
- **F. Diagnostic** (« ma voix sonne robotique ») → pose au besoin une question sur son workflow actuel, puis passe en revue les 4 piliers et les étapes A à D pour trouver ce qui manque.

## A. Annoter un script

C'est le cas le plus fréquent. Lis `references/annotation.md` pour les règles détaillées et les exemples avant d'annoter.

Principes rapides :
- **`...`** → hésitation, déception, confusion, suspense ; aussi pour une pause courte.
- **`!`** → enthousiasme, énergie (en ajouter plusieurs si l'effet ne passe pas).
- **Virgules** → micro-pauses, respiration.
- **MAJUSCULES** → emphase sur un mot clé. Avec parcimonie : un mot par phrase au maximum en général, sinon plus rien ne ressort.
- **Découper en lots de 1 à 3 phrases** : chaque lot sera généré séparément (voir pourquoi dans la section génération).

### Format de sortie pour un script annoté

Présente le résultat ainsi :

```
LOT 1 — [intention en quelques mots : ex. « accroche, curieux »]
<texte annoté>

LOT 2 — [intention]
<texte annoté>
...
```

Puis, après les lots, une courte section **Notes** : les passages où une pause longue doit être ajoutée au montage, les lots qui méritent plusieurs générations (moments clés), et les éventuelles phrases du script trop « écrites » que tu as reformulées (dis-le clairement, ne réécris pas le fond en silence).

Si l'utilisateur veut un fichier, exporte en **.txt** par défaut (sauf s'il demande un autre format), parce que c'est prêt à copier-coller dans ElevenLabs sans balises Markdown parasites.

## B. Choisir la voix

Rappelle que c'est un choix à long terme : la voix devient l'identité sonore de la chaîne. Trois options :

1. **Cloner sa propre voix** — clonage instantané (court échantillon) ou professionnel (au moins ~30 min d'audio propre). Utile même si on peut enregistrer soi-même : ça permet ensuite de doubler ses vidéos dans d'autres langues avec sa propre voix.
2. **Voix de la bibliothèque** — rapide, mais d'autres créateurs peuvent utiliser la même.
3. **Voice Design (voix créée sur mesure)** — on décrit la voix en texte ; elle est unique, donc bonne pour une identité de marque.

**Légal / éthique** : ne jamais aider à cloner la voix d'une personne réelle sans son consentement. C'est contraire aux conditions d'utilisation et potentiellement illégal. Si la demande vise la voix de quelqu'un d'autre, propose plutôt un Voice Design inspiré d'un *style* (énergie, âge, accent) sans imiter la personne.

### Rédiger un prompt de Voice Design

Quand on te demande de créer une voix, rédige un prompt descriptif qui couvre : âge approximatif, genre, accent / langue, timbre (grave, clair, légèrement éraillé…), style de parole (posé, énergique, décalé, charismatique), et surtout **la variabilité** (« beaucoup d'émotion, change souvent de ton et de rythme »). Exemple :

> Homme d'une vingtaine d'années, accent français standard, voix claire et légèrement grave, style décalé mais charismatique, parle avec beaucoup d'émotion, varie constamment le ton et la vitesse, alterne passages posés et moments très enthousiastes.

Conseille de baisser un peu le paramètre de « guidance » pour laisser plus de liberté au générateur, et de générer plusieurs propositions avant de choisir.

## C. Réglages

Réglages recommandés dans la méthode de référence (ElevenLabs, modèle multilingue v2) :
- **Vitesse** : légèrement augmentée
- **Stabilité** : réduite (plus de variation expressive)
- **Similarité** : ~70 %
- **Exagération du style** : augmentée

Sur le choix du modèle : la méthode d'origine recommandait v2 plutôt que v3, car v3 (alors en alpha) modifiait parfois le timbre de la voix, surtout avec une voix clonée. Les modèles évoluent vite — si tu as accès à la recherche web, vérifie l'état actuel avant de trancher, et sinon présente ce conseil comme daté. Si l'utilisateur utilise v3, il peut employer les balises d'émotion du modèle (du type `[excited]`, `[whispers]`) en complément de la ponctuation ; conseille de vérifier que le timbre reste stable sur plusieurs générations.

Ces réglages sont un point de départ : invite l'utilisateur à ajuster à l'oreille sur un lot test avant de lancer tout le script.

## D. Génération et assemblage — le « secret »

Le point qui fait la plus grande différence, à toujours transmettre :

- **Générer lot par lot**, jamais tout le script d'un coup. Une mauvaise prise se régénère sans gaspiller de crédits.
- **Chaque génération varie légèrement** en ton et en rythme, même avec le même texte. On exploite ça : garder et télécharger plusieurs versions de chaque lot (les régénérations gratuites si l'outil en propose).
- **Au montage**, choisir la meilleure prise par phrase, voire **combiner des morceaux de plusieurs versions** d'une même phrase. L'assemblage de ces légères variations imite la manière dont un humain parle et fait disparaître l'impression d'« uncanny valley ».
- **Nommer et ranger** les fichiers systématiquement (ex. `lot01_v1.mp3`, `lot01_v2.mp3`…) pour s'y retrouver.

Pour le détail du montage (pauses, vitesse, égalisation) et le doublage, lis `references/montage-et-doublage.md`.

## Ton à adopter

Sois concret et direct. Quand tu annotes, montre le résultat plutôt que de réexpliquer toutes les règles. Réponds dans la langue de l'utilisateur ; annote le script dans la langue du script.


---
## Fichier : voix-off-ia/references/annotation.md

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


---
## Fichier : voix-off-ia/references/montage-et-doublage.md

# Montage de la voix off et doublage

Les étapes sont décrites avec Premiere Pro, mais tout logiciel avec une timeline convient (DaVinci Resolve, CapCut, Audacity pour l'audio seul…). Adapte les noms de menus au logiciel de l'utilisateur.

## 1. Assembler les prises

1. Importer toutes les générations dans le projet.
2. Poser les lots dans l'ordre du script sur une seule piste, sans se soucier du timing pour l'instant.
3. Pour chaque phrase avec plusieurs versions : écouter toutes les prises, garder celle qui colle le mieux au contexte.
4. Pour les phrases importantes : **combiner des morceaux de plusieurs versions** (début de la v1, milieu de la v3…). C'est là que le résultat devient le plus humain.

## 2. Rythme et pauses

- Une fois la ligne complète, couper les silences superflus. Astuce : utiliser une deuxième piste pour démarrer la phrase suivante juste à la fin de la précédente, puis ramener sur une piste.
- **Garder ou ajouter des pauses volontaires** sur les moments importants. Couper tous les silences améliore peut-être la rétention, mais rend la voix mécanique.

## 3. Vitesse

- Mieux vaut régler la vitesse **à la génération** (curseur de vitesse de l'outil TTS).
- Si la voix est trop lente ou trop rapide après coup : l'étirement temporel des logiciels de montage déforme souvent la voix (effet « chipmunk » sans conservation de la hauteur, artefacts avec). Solutions : régénérer avec une autre vitesse, ou ajuster le rythme manuellement en raccourcissant/allongeant les pauses plutôt que la voix elle-même.

## 4. Égalisation (rendre la voix plus « pro »)

Avec un égaliseur paramétrique :
1. **Filtre passe-haut** pour couper les basses inutiles (grondements) — souvent autour de 80–100 Hz pour une voix, à ajuster à l'oreille.
2. **Chercher les fréquences qui résonnent** : augmenter fortement une bande étroite, la balayer jusqu'à entendre une résonance désagréable ou un effet « boîte / écho », puis l'atténuer.
3. Ajuster à l'oreille, par petites touches, en comparant avec/sans effet.

Une fois le réglage trouvé, **l'enregistrer en preset** pour l'appliquer à toutes les vidéos et garder un son cohérent.

## 5. Doublage multilingue

L'intérêt : l'essentiel des utilisateurs de YouTube ne parle pas la langue d'origine de la vidéo. Doubler dans quelques grandes langues peut multiplier l'audience potentielle.

### Préparer les pistes
1. Dans la timeline finale, couper tout sauf la voix off → exporter en MP3 (**piste voix**).
2. Faire l'inverse : couper la voix off → exporter la musique et les effets (**piste ambiance**).

### Générer le doublage
3. Dans l'outil de doublage (ex. onglet Dubbing d'ElevenLabs) : langue d'origine, langue cible, envoyer la **piste voix seule**. Envoyer la voix isolée évite que la musique perturbe la transcription et la synthèse.

### Remonter
4. Dans le logiciel de montage, trois pistes :
   - en haut : voix originale (**guide de timing**, sera coupée ensuite)
   - au milieu : voix doublée
   - en bas : piste ambiance
5. Caler la voix doublée sur les visuels en s'aidant de la voix originale.
6. Couper la voix originale, appliquer le même preset d'égalisation à la voix doublée, exporter **l'audio seul**.

### Publier sur YouTube
7. YouTube Studio → **Langues** → choisir la vidéo.
8. Vérifier que YouTube n'a pas déjà créé un doublage automatique dans cette langue ; si oui, le supprimer.
9. Ajouter la langue et envoyer le fichier audio doublé.
10. Traduire aussi **titre et description** dans chaque langue.

### Mesurer
Dans les statistiques YouTube, regarder les vues **par piste audio** plutôt que le total : c'est là que l'effet du doublage devient visible.

Rappelle que les fonctions de YouTube Studio évoluent : si un menu ne correspond pas, vérifie l'interface actuelle (recherche web si disponible).

