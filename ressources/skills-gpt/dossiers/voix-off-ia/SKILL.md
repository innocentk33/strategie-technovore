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
