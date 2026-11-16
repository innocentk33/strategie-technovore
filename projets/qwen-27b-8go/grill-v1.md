# Grill de la nouvelle V1 documentaire : Qwen 27B sur 8 Go

Revue indépendante du **16/11/2026**. Texte critiqué : [`script-v1.md`](script-v1.md), nouvelle version documentaire après clarification du format. La première rédaction et son ancien grill sont dans `archive-avant-recentrage/` ; leurs notes ne s'appliquent pas à ce manuscrit.

**Méthode appliquée intégralement :** [`youtube-script-grill.md`](../../ressources/skills-gpt/youtube-script-grill.md), mode B, **variante storytelling** : test des trente secondes, onze axes, S1–S6, anti-IA, passages à conserver et plan d'action. Contraintes supplémentaires : [`prompt-reprise-gpt.md`](../../prompt-reprise-gpt.md), règles de voix, format calculé et clarification de l'auteur. La référence SimplyExplain est désormais assumée pour son rythme d'exposé ; les phrases et le vécu ne sont pas à reprendre.

**Hypothèses de cadrage :** public francophone jeune, souvent joueur ; veut comprendre si son matériel peut rendre un service utile. Promesse du titre : une vitesse supérieure et les concessions qui l'accompagnent. Miniature non définitivement choisie ; le test d'alignement suppose un avant/après accompagné de la limite 8 Go, sans ×5 garanti. Aucune question ni capture à demander pour terminer ce script.

## Verdict : 7,6/10

Cette V1 tient enfin le format demandé : **une explication fondée sur des résultats publiés**, sans ouvrir LM Studio, sans essai personnel à raconter, sans demander au spectateur de mener le test à la place de l'auteur. Le calcul des secondes rend le gain concret ; le contraste **40 / 13 / 36** donne une vraie raison de ne pas choisir uniquement le fichier rapide.

Son principal défaut est maintenant le **double passage sur les limites de preuve**. La partie LM Studio répète près d'une minute de précautions déjà expliquées, juste avant le verdict. L'autre faiblesse est l'engagement : après la question initiale, on écoute un bon exposé, mais on n'est plus invité à anticiper. Les corrections peuvent raccourcir le texte sans sacrifier les informations utiles.

Note globale : moyenne des **onze axes principaux**, 84/110, arrondie à 7,6. Les axes S détaillent le storytelling sans compter une seconde fois les mêmes défauts. Aucune note ne prédit la rétention réelle.

## Test des trente secondes

| Tranche | Ce que dit la V1 | Verdict |
|---|---|---|
| 0–5 s | « Sur une carte limitée à 8 gigas, un testeur change de fichier. » | 🟢 Le sujet, la contrainte et l'action sont présents. L'effet arrive dès la phrase suivante. |
| 5–15 s | « Qwen 27B passe de 3,2 à 18 tokens par seconde pour écrire sa réponse. Ces chiffres sont les leurs, je n'ai rien testé chez moi. » | 🟢 Le meilleur résultat est livré avant 11 s, attribué et séparé de la lecture du prompt. Le bandeau donne la carte, le moteur et la date. |
| 15–30 s | « Sauf que le petit fichier perd aussi des capacités. Du coup, qu'est-ce que tu gagnes vraiment, si tu gardes ta carte de joueur ? » | 🟢 Une seule question centrale, terminée vers 0:25. La perte de capacités fait monter l'enjeu, sans inventer un défaut personnellement observé. |
| Pont, 0:25–0:41 | « On va traduire cette vitesse en temps d'attente, regarder ce que le fichier perd en qualité et combien de conversation il peut garder. À la fin, tu sauras pour quel usage le plus lent reste le meilleur choix. » | 🟢 Trois livrables concrets et une deuxième question : pourquoi choisir le plus lent ? La première partie répond immédiatement par les secondes. |

**Budget : 61 mots jusqu'à la question, soit 25,2 s à 145 mots/min. Plan : 38 mots, environ 15,7 s.** Le mot « capacités » est abstrait, mais évite d'entasser un second benchmark dans l'ouverture ; la preuve arrive ensuite.

Les six contrôles du skill passent : sujet/tension, meilleur moment avant quinze secondes, question unique avant trente secondes, pont qui ouvre une autre attente, utilité de chaque phrase et budget réel. **À couper dans ces trente secondes : rien d'indispensable.** La phrase d'absence d'essai personnel reste, même si elle n'est pas une relance spectaculaire : c'est une règle explicite de l'auteur et une condition de confiance.

## Tableau de bord

| Axe | Note /10 | État | Diagnostic ancré dans le texte |
|---|---:|---|---|
| 1. Promesse | 8 | 🟢 | « 3,2 à 18 » au début, puis « 40 %… 13 %… 36 % » : vitesse et prix sont livrés. Le prix n'est pas un montant en euros. |
| 2. Alignement des objectifs | 9 | 🟢 | « Si tu gardes ta carte de joueur » correspond au besoin du public ; aucun achat ou test imposé, CTA bref après un service rendu. |
| 3. Problème profond | 8 | 🟢 | La crainte de devoir remplacer la carte devient un choix d'usage. « Finir d'écrire plus vite… finir le travail plus vite » porte cet enjeu sans faux vécu. |
| 4. Public et complexité | 8 | 🟢 | « Un token, c'est un morceau de texte », puis quantification, puis cache : progression accessible. « Enveloppe précise » est moins oral. |
| 5. Valeur et originalité | 8 | 🟢 | Calcul 500 tokens, comparaison au 4 bits et impossibilité d'additionner les gains donnent une lecture propre des mêmes faits. Le récit ne revendique pas une découverte exclusive. |
| 6. Structure et transformation | 7 | 🟠 | Départ : croire le compteur ; arrivée : choisir un travail. « Ce que ça signifie dans LM Studio » revient toutefois sur deux réserves déjà traitées. |
| 7. Histoire | 7 | 🟠 | Enquête explicative cohérente : gain, mécanisme, coût, verdict. « Une réponse… mauvaise affaire » est le pivot. Pas besoin d'inventer une crise de l'auteur. |
| 8. Mais / donc | 8 | 🟢 | « Même une réponse correcte… manque de place » rend la section mémoire nécessaire. Le raccord vers LM Studio est davantage un changement de rubrique. |
| 9. Engagement actif | 6 | 🟠 | « Qu'est-ce que tu gagnes vraiment ? » est la seule invitation explicite à réfléchir ; le reste révèle tout au spectateur. |
| 10. Rythme, oralité et liaisons | 8 | 🟢 | **21 liaisons strictes / 1 396 mots = 1,50 pour 100**. Bon rythme général, mais « Du coup… Donc… Donc… » ne doit pas remplacer les réactions. |
| 11. Tics d'IA | 7 | 🟠 | « Ce qu'on peut expliquer, en revanche… », « leur autre test raconte une histoire différente », « dans une enveloppe précise » : annonces et abstractions à alléger. |
| S1. Trente premières secondes | 8 | 🟢 | Six contrôles réussis ; question terminée à 0:25. |
| S2. Pont | 8 | 🟢 | « Pour quel usage le plus lent reste le meilleur choix » ouvre une boucle distincte, payée au verdict. |
| S3. Retournements | 6 | 🟠 | Plusieurs bons pivots, mais des plages de 45–67 s entre eux ; le repère 25–35 s n'est pas constamment tenu. |
| S4. Planté / récolté et motif | 9 | 🟢 | Le 18 revient comme débit partiel, comme vitesse à contexte vide, puis comme mauvais critère unique ; les 28 secondes reviennent avec un nouveau coût. |
| S5. Personnages et enjeu | 7 | 🟠 | Le testeur veut faire tenir le modèle et rencontre le manque de place ; le spectateur veut conserver sa carte. Ils existent sans biographie inventée, mais restent peu incarnés. |
| S6. Fin | 8 | 🟢 | « Le plus lent peut être le choix le plus utile » retourne le compteur initial ; le jeudi ouvre la question de ce qu'une mémoire supérieure achète réellement. |

## Le grill, du plus important au plus léger

### 1. LM Studio répète le dossier au lieu de faire avancer la décision

> « Mais les mesures qu'on vient de voir ont été faites avec llama.cpp. On ne peut pas leur coller une étiquette LM Studio et annoncer le même résultat. Le principe aide à comprendre le compromis ; le débit exact reste celui de l'essai publié. »

> « Et couper la réflexion pour économiser du contexte change encore les conditions. Les scores de qualité qu'on a montrés ont été obtenus avec une réflexion élevée. »

**Pourquoi ça coince :** vers 1:52–2:21, le texte a déjà expliqué la machine unique et l'absence de prédiction pour le PC du spectateur. Vers 5:24–5:46, il a déjà expliqué les conditions des évaluations Unsloth. La section LM Studio dure **54 secondes** et reporte le verdict après 8:26. Son apport propre, utile, tient en deux idées : les contrôles correspondants existent ; leur présence ne valide pas la mesure dans ce logiciel.

**Correction, réécriture ciblée 1 :**

> Si tu utilises LM Studio, les mêmes limites comptent : la place du modèle, celle de la conversation et la réflexion. Sa documentation expose les contrôles correspondants. Mais le testeur a mesuré sa vitesse dans llama.cpp. On sait donc quels compromis regarder ; on n'a toujours pas de débit confirmé dans LM Studio pour cette configuration. Et la qualité dépend elle aussi des conditions choisies.

Cette version conserve le lien demandé au logiciel, sans aucun clic à montrer. L'autre possibilité est de répartir ces deux précisions dans les sections mémoire et qualité et de passer directement au verdict.

### 2. Le calcul de temps est bon, mais son hypothèse centrale reste dans le visuel

> « Pour 500 tokens à écrire, ça donne environ 2 minutes 36 contre 28 secondes. C'est une division des vitesses publiées, pas un chronomètre lancé chez moi. »

**Pourquoi ça coince :** le montage dit bien « vitesse constante », mais quelqu'un qui écoute seulement entend d'abord deux temps de réponse. L'absence de chronomètre personnel est déjà annoncée dans l'ouverture. L'hypothèse de constance apporte davantage que cette deuxième précaution.

**Correction, réécriture ciblée 2 :**

> Pour 500 tokens à écrire, à débit constant, le calcul donne environ 2 minutes 36 contre 28 secondes. Il reste à ajouter la lecture de la demande et le démarrage. Un token, c'est un morceau de texte ; ici, on compare seulement la même quantité à générer.

Les divisions F16 sont correctes : **500 / 3,2 = 156,25 s** et **500 / 18 = 27,78 s**. C'est une illustration calculée, pas un nouvel essai. Ne pas lui ajouter une durée de réflexion supposée : le nombre de tokens générés dépend du travail.

### 3. Le spectateur ne fait plus aucune prédiction après l'ouverture

> « Le modèle complet est autour de 89, le petit fichier autour de 85, en lecture arrondie du graphique. Donc il ne s'effondre pas sur toutes les tâches parce qu'il est plus compressé. Mais dès qu'il faut travailler dans un vrai dépôt de code, leur autre test raconte une histoire différente. »

**Pourquoi ça coince :** les chiffres sont utiles, mais la dernière phrase annonce la surprise juste avant de la donner. Le spectateur n'a pas l'occasion de projeter le petit écart sur un autre usage, puis de voir cette intuition échouer. On peut le faire participer en une phrase, sans quiz artificiel ni question rhétorique en série.

**Correction, réécriture ciblée 3 :**

> Sur ces exercices, on lit autour de 89 contre 85. Garde ce petit écart en tête. Quand le modèle doit travailler dans tout un dépôt, on passe à environ 40 % des tâches réussies pour le modèle complet, contre 13 % pour le petit fichier. Le 4 bits reste autour de 36 %. Donc les quelques points perdus sur les exercices ne racontaient pas ce risque-là.

L'invitation à retenir l'écart permet une anticipation, et le visuel peut laisser une courte respiration avant la seconde comparaison. Pas de faux suspense, pas de nombre inventé, pas de test à mener chez soi.

### 4. Les réactions sont parfois remplacées par des conclusions abstraites

> « C'est le genre de détail qui disparaît derrière un joli “ça tourne sur 8 gigas”. Ça tourne, oui, dans une enveloppe précise. »

> « Le fichier qui rentre apporte une possibilité de plus, mais il ne transforme pas la carte en modèle supérieur. »

**Pourquoi ça coince :** la première phrase suggère que d'autres cachent ce détail alors que la référence SimplyExplain raconte elle-même le plantage. Sans auteur précis à viser, mieux vaut laisser l'incident produire son effet. « Enveloppe précise » est un terme de dossier technique. « Carte en modèle supérieur » mélange la carte et le modèle d'IA au milieu d'une explication où les deux mots reviennent constamment.

**Correction, réécriture ciblée 4 :**

> Le modèle avait réussi à se charger. Pourtant, il s'arrête quand la conversation déborde. Donc les échanges courts et la longue session avec tous tes documents ne demandent pas le même budget mémoire. Les 8 gigas de la carte restent les mêmes.

La scène vient de l'essai publié, pas d'un incident inventé chez l'auteur. Si cette réécriture remplace le passage entier, retirer les lignes voisines qui répètent la même idée.

## Audit des tics et des répétitions

Toutes les occurrences signalées ci-dessous sont dans la voix. Les indications de montage et titres techniques ne sont pas notés comme prose orale.

| Citation | Diagnostic | Action |
|---|---|---|
| « C'est une division des vitesses publiées, pas un chronomètre lancé chez moi. » | Opposition utile, mais transparence déjà assurée dans l'ouverture ; priorité à l'hypothèse du calcul. | Réécriture 2. |
| « Un token, c'est un morceau de texte, pas forcément un mot entier. » | Correction concrète d'une confusion plausible. Ce n'est pas une fausse profondeur. | Garder ou condenser. |
| « Ce qu'on peut expliquer, en revanche, c'est pourquoi changer de fichier fait un tel écart chez lui. » | Annonce de l'explication au lieu de l'explication. | Enchaîner directement sur ancien fichier partagé / nouveau tout GPU. |
| « Donc la carte n'a pas gagné de mémoire : la copie du modèle prend moins de place. » | Opposition réelle, centrale au sujet. | Garder ; ne pas la multiplier ailleurs. |
| « Leur autre test raconte une histoire différente. » | Formule générique qui annonce le contraste. | Livrer les scores après l'anticipation, réécriture 3. |
| « Là, l'écart se voit même sans sortir la calculatrice. » | Réaction orale acceptable ; moins précise que la conséquence pour le travail. | Garder seulement si elle sonne comme l'auteur. |
| « Finir d'écrire plus vite ne veut pas forcément dire finir le travail plus vite. » | Contraste véritable montré par les données, payé par la section qualité. | Garder. |
| « C'est le genre de détail qui disparaît derrière un joli “ça tourne sur 8 gigas”. » | Critique d'un discours non identifié ; la référence retenue donne justement ce détail. | Raconter le chargement suivi du plantage, réécriture 4. |
| « Ça tourne, oui, dans une enveloppe précise. » | Abstraction technique et petite sentence de fin de paragraphe. | Supprimer. |
| « Le principe aide à comprendre le compromis ; le débit exact reste celui de l'essai publié. » | Reformulation d'une réserve déjà dite. | Condenser avec LM Studio, réécriture 1. |

Pas de « plongeons », « en résumé », intensifs creux, tirets dramatiques dans la voix, cascade de triplets d'adjectifs ou questions suivies d'une réponse en un mot. Les trois profils finaux et les trois scores ne sont pas des rafales d'adjectifs : ils ont une fonction de comparaison. Le texte n'est pas truffé de tics ; son défaut est surtout la répétition des garde-fous.

## Oralité, rythme et retournements : contrôle détaillé

Comptage sur la voix uniquement, crochets et titres retirés : **1 396 mots**, environ **9:38** à 145 mots/min, hors respirations et avis facultatif. Liste stricte : **donc 9, du coup 4, en fait 2, sauf que 4, par contre 1, voilà pourquoi 1**, soit **21 = 1,50 pour 100 mots**. « En effet » et « voilà comment » : zéro. Les huit « mais » supplémentaires font passer le total à **29 = 2,08** avec une liste élargie. Les mots « résultat » employés comme noms ne sont pas comptés comme liaisons ; une recherche brute surestimerait l'oralité.

Le seuil numérique est atteint. Il ne suffit pas à prouver la présence de réactions ou de causalité : la section LM Studio contient assez de connecteurs tout en répétant ce qu'on sait.

| Moment approximatif | Vrai déplacement du sens |
|---|---|
| 0:15 | La copie rapide perd des capacités. |
| 0:41 | Les tokens deviennent un temps d'attente calculé. |
| 1:26 | L'écriture n'est qu'une partie de l'attente. |
| 1:52 | La portée du résultat se réduit à une machine. |
| 2:28 | L'explication vient du placement RAM/GPU. |
| 3:03–3:17 | Le modèle tient grâce à une précision réduite ; ses réponses changent. |
| 3:45 | Le temps économisé peut devenir du travail à corriger. |
| 4:17 | La faible baisse sur les exercices devient une forte baisse en agent. |
| 5:24 | Les conditions du fournisseur limitent la portée des scores. |
| 5:46 | Même une réponse correcte dépend de la place restante. |
| 6:31–6:53 | Plus de contexte compressé, débit différent, puis plantage. |
| 7:49–8:18 | Retour aux limites de transposition vers LM Studio et d'assemblage des chiffres. |
| 9:02 | Le fichier lent peut être le choix utile : récolte de la question du plan. |

Le passage **4:17–5:24** fait environ **67 secondes** entre deux nouvelles contraintes : les explications intermédiaires sont utiles, mais presque toutes développent le même contraste. La plage **6:53–7:49** approche une minute. D'où S3 orange : la version ne respecte pas partout le repère 25–35 secondes. Les coupes de répétitions et l'anticipation de la réécriture 3 améliorent ce point sans ajouter de faux rebondissements.

### Motifs plantés et récoltés

- **18 tokens/s** : résultat initial → insuffisant pour juger le travail vers 5:03 → valeur à contexte vide vers 6:45 → mauvais critère unique vers 9:07. Au moins deux vraies récoltes.
- **28 secondes** : gain calculé vers 0:41 → un débit unique vers 2:15 → mauvaise affaire si davantage de corrections vers 3:49.
- **La carte conservée** : question initiale → elle n'a pas gagné de mémoire vers 3:03 → achat pertinent seulement si mémoire ou qualité bloquent, dans la fin.

Cette progression suffit pour une enquête documentaire. Ne pas lui ajouter un voyage du héros ou une émotion personnelle que l'auteur n'a pas fournie.

## Faits, sources et format calculé

- **Format : conforme.** Aucun passage ne demande d'ouvrir LM Studio, de télécharger le modèle, de remplir le contexte, de mesurer un débit ou de produire une capture personnelle. Les tableaux et documents publics suffisent aux visuels.
- **Mesure principale : conforme.** F2 et F11 rendent visible le caractère unique de l'essai, sa carte bridée et son moteur. Trois passes ne sont pas trois mesures indépendantes. Le titre ne promet pas ×5 pour toutes les cartes.
- **Temps calculés : calcul juste**, hypothèse de débit constant à renforcer dans la voix, réécriture 2. F16 doit figurer dans la version consolidée des sources.
- **Qualité : conforme aux graphiques déjà contrôlés directement.** LiveCodeBench BF16 annoté 88,62, petit fichier lu autour de 84,5 ; DeepSWE BF16 annoté 40,40, IQ2_XS autour de 12,8 et IQ4_XS autour de 36,2. Les valeurs arrondies de la voix sont cohérentes, attribuées et non présentées comme des taux de réussite personnels.
- **Contexte : conforme à F3.** 14 000, 22 500 et environ 12 sont des ordres de grandeur du même testeur ; le visuel distingue bien les conditions 8 bits / 4 bits et contexte vide / plein. Ne pas transformer les barres en une courbe prétendant mesurer un seul réglage.
- **MTP : conforme.** Il est désactivé dans cet essai pour le budget mémoire. Le script n'affirme pas qu'il serait impossible sur toute carte de 8 Go.
- **Réflexion : réserve pertinente.** Les grands contextes et la réflexion élevée des benchmarks ne valident pas le mode à contexte réduit ; cela doit rester dit une fois clairement.
- **Aucune anecdote, aucun résultat personnel inventé, aucun nom de chaîne dans la voix.** Le seul avis personnel est dans un crochet facultatif.
- **Limite de formulation :** « Tu finis par préparer un gros message » décrit un comportement comme automatique. « Tu peux finir par préparer… » ou une formulation impersonnelle suffit ; ce n'est pas un fait mesuré.

**Aucun problème matériel bloquant identifié dans cette V1.** Les réserves restantes concernent la présentation du calcul et la répétition de la méthode, pas un chiffre à retirer faute de source.

## Ce qu'il faut garder

> « Sur une carte limitée à 8 gigas, un testeur change de fichier. »

La limitation mémoire est conservée dès le début, sans donner l'impression d'une véritable 4060 mesurée.

> « Pour 500 tokens à écrire, ça donne environ 2 minutes 36 contre 28 secondes. »

La traduction du débit en attente parle au public. Garder le calcul en renforçant son hypothèse, sans le remplacer par une nouvelle explication technique.

> « On ne peut pas empiler les gains des deux vidéos comme des bonus d'équipement. »

Le pont avec la vidéo précédente explique une limite réelle avec le vocabulaire du public.

> « Le modèle complet réussit environ 40 % des tâches. Le petit fichier, environ 13 %. Et le fichier 4 bits de leur graphique reste autour de 36 %. »

C'est la preuve qui rend le verdict crédible. Le 4 bits est particulièrement utile : il soutient la comparaison finale avec un fichier moins compressé.

> « Finir d'écrire plus vite ne veut pas forcément dire finir le travail plus vite. »

Le problème profond tient dans cette phrase et dans la preuve qui la précède.

> « Donc le plus lent peut être le choix le plus utile. »

La fin répond à la question du plan et retourne le sens du chiffre initial. Garder le conditionnel.

## Plan d'action

1. **Raccourcir la section LM Studio**, en gardant son apport propre et une seule réserve claire sur la transposition des mesures.
2. **Dire “à débit constant” dans le calcul des secondes**, et conserver ses exclusions à l'écran.
3. **Faire anticiper le changement de qualité** avec « garde cet écart en tête », puis montrer les trois scores ; retirer l'annonce générique de surprise.
4. **Nettoyer les abstractions et la cible implicite** autour du plantage : raconter l'incident, retirer « enveloppe précise » et « carte en modèle supérieur ».
5. **Finaliser l'en-tête** : nombre de mots, durée, tableau des parties et timecodes, demandés par le prompt. Ils étaient absents de la V1 lors de la première lecture et ont depuis été ajoutés sans modifier sa voix. Recompter après coupes ; ne pas réutiliser les métriques du premier script archivé.

### Base de timecodes pour la correction

| Partie V1 | Début calculé | Mots |
|---|---:|---:|
| Résultat et prix caché | 0:00 | 61 |
| Plan | 0:25 | 38 |
| Secondes | 0:41 | 261 |
| Modèle qui rentre | 2:29 | 215 |
| Qualité | 3:58 | 279 |
| Conversation | 5:53 | 239 |
| LM Studio | 7:32 | 131 |
| Verdict | 8:26 | 172 |
| Fin | 9:38 | **1 396** |

Ces durées sont des estimations au débit demandé. Le crochet d'avis, les respirations et les temps laissés aux graphiques s'ajoutent ; les coupes proposées créent une marge utile sous les dix minutes.

## Contrôle de la version corrigée

[`script.md`](script.md) relu après les premières corrections, le 16/11/2026. Ce contrôle ne remplace pas le grill de la V1 et n'ajoute pas une note artificiellement supérieure.

- **Format documentaire conservé :** aucune manipulation ou capture personnelle requise, ni appel au spectateur à reproduire un test.
- **Ouverture :** résultat attribué, limite de 8 Go et déclaration d'absence d'essai personnel conservés avant trente secondes.
- **Calcul :** « à débit constant, hors lecture de la demande et démarrage » est désormais dit dans la voix. F16 documente les divisions.
- **Qualité :** les arrondis 89/85 et 40/13/36 correspondent au graphique primaire déjà inspecté ; l'attribution et les limites des conditions restent explicites. Une question d'anticipation, suivie d'une pause visuelle, a été ajoutée avant DeepSWE.
- **LM Studio :** section ramenée à **92 mots, environ 38 secondes**, sans refaire le paragraphe sur les conditions des benchmarks de qualité. Le lien au logiciel reste informatif.
- **MTP :** le texte parle toujours de cet essai précis et ne déclare pas le mécanisme impossible sur toutes les cartes de 8 Go.
- **Structure et voix :** le motif du compteur et le verdict par profil sont conservés. Comptage indépendant de cette version : **1 382 mots, environ 9:32**, **26 liaisons strictes, 1,88 pour 100 mots**. Métadonnées et tableau sont cohérents avec ce relevé.
- **Dernière amélioration éditoriale transmise :** retirer les deux phrases autour du « joli ça tourne sur 8 gigas » et de l'« enveloppe précise ». La référence raconte le plantage ; mieux vaut laisser l'incident parler que suggérer sa dissimulation.

**Aucun problème matériel bloquant identifié.** Si les dernières lignes sont coupées, les compteurs et timecodes doivent simplement suivre cette coupe. L'estimation de durée reste hors pauses et avis facultatif.
