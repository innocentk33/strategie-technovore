# Grill du brouillon v1 : « Combien coûte Claude en local ? »

> Grill du 22/10/2026 sur [`brouillon-v1.md`](brouillon-v1.md) (premier jet écrit avec `/claude-youtube`). Grille : skill `youtube-script-grill`. Contexte : sortie le lun. 2 nov. ; miniature [`vert-05.png`](../../ressources/miniatures/rendus/vert-05.png) (« Claude chez moi, ?? ??? € ») ; public tech francophone, jeune, 63 % Afrique.

## Verdict

La recherche est solide et honnête : le tableau vert puis rouge face à Opus 5, les euros, OVHcloud et Scaleway, le tarif EDF, la règle des 30 % confrontée à deux mesures. C'est exactement ce qui manque à Kai.

**Le plus gros problème : le chiffre de l'accroche n'est pas un prix « en local ».** 30 660 € par mois, c'est la location d'un serveur chez OVHcloud. Le titre et la miniature promettent « Claude **chez moi** ». Le spectateur attend un prix de machine, et la vraie réponse locale (ta 5080 + 192 Go de RAM, ou le Mac Studio) est noyée au milieu de l'escalier.

Deuxième trou : **le retournement est vide**. Il repose sur un résultat de ta 5080 qui n'existe pas encore, et sur ton avis, qui n'est pas écrit. En l'état, la vidéo finit sur « attends le 16 novembre ».

## Tableau de bord

| Axe | Note | En une phrase |
|---|---|---|
| Promesse | 🔴 | L'accroche donne un prix de location dans le cloud, alors que le titre promet « en local » |
| Alignement des objectifs | 🟢 | Pas de vente, les limites sont dites, le spectateur repart avec un calcul réutilisable |
| Problème profond | 🔴 | Aucun enjeu à toi : pourquoi tu voudrais Claude chez toi n'apparaît qu'en ⟦à écrire⟧ à 11:30 |
| Public & complexité | 🟠 | Le bloc 3:15-5:20 empile bits, Engram, écart 552/763, cache KV et bande passante avant le moindre prix |
| Valeur & originalité | 🟢 | Euros, EDF, clouds européens, Engram sur le SSD, la règle des 30 % : personne ne fait ça en français |
| Structure & transformation | 🟠 | Bon escalier, mais l'étape 4 (Kimi K3) change de modèle, et le vrai « local » n'est pas mis en avant |
| Histoire | 🟠 | Une enquête sans enquêteur : il manque ton point de départ et un moment où ton calcul déraille |
| Mais / donc | 🟢 | Les paliers s'enchaînent par des conséquences (« ne tient pas, donc la RAM… ») |
| Engagement actif | 🟠 | Personne n'est invité à deviner un prix ou à se situer avant le verdict |
| Rythme & oralité | 🟠 | Trop de nombres exacts dits à voix haute (« trente-quatre mille trois cent cinquante-cinq dollars ») |
| Tics d'IA | 🟠 | Peu de tics, mais deux faux suspens et la même réserve répétée 4 fois |

## Le grill

### 1. Le chiffre de l'accroche n'est pas « en local »

> « Trente mille six cent soixante euros. Par mois. C'est ce que coûte, d'après mon calcul, le plus petit serveur que j'ai trouvé en Europe… »

**Pourquoi ça coince** :
- Un serveur loué chez OVHcloud, c'est le cloud. Le spectateur a cliqué sur « Claude chez moi ». Dès 0:05, la vidéo répond à une autre question.
- Le script le reconnaît lui-même plus loin (« tu paies à l'heure, deux heures de test, quatre-vingt-quatre euros »), ce qui affaiblit le chiffre d'ouverture.
- La vraie réponse locale existe et elle surprend : si tu as déjà un PC gamer, il manque environ **2 500 € de RAM** pour faire tourner la version Q2.

**Correction** : ouvrir sur le prix local et garder les 30 660 € comme contraste. Deux options :

**Option A (le prix « pas cher » d'abord)**
> [VISUEL : la 5080 au pied de la baie. Une étiquette s'allume sur le PC : « + 2 500 € ».]
> Deux mille cinq cents euros. Si tu as déjà un PC gamer comme le mien, c'est ce qu'il te manque, d'après mon calcul, pour faire tourner chez toi un modèle qui joue dans la cour de Claude.
> [VISUEL : un compteur de tokens qui avance au ralenti.]
> À environ six tokens par seconde. Une réponse de code de trois mille tokens, c'est plus de huit minutes à regarder le curseur.
> [VISUEL : la baie s'allume, compteur « 30 660 € / mois ».]
> Pour la version officielle, sans compression, il faut des cartes de datacenter. En location : trente mille euros. Par mois.

**Option B (le contraste en une phrase)**
> Pour avoir chez toi un modèle de la trempe de Claude, il te faut, d'après mon calcul, deux mille cinq cents euros de RAM. Ou trente mille euros. Par mois. Les deux font tourner le même modèle. Il y en a un qui te répond en huit minutes.

Dans les deux cas, l'étiquette de la miniature (« ?? ??? € ») doit afficher **le même chiffre** que la première phrase.

### 2. Le retournement est vide

> « ⟦à écrire : résultat mesuré sur la 5080 (si un essai est fait avant le tournage)…⟧ »
> « Un modèle de seize gigas ne sera probablement pas Claude, mais il pourrait faire le quotidien : compléter du code, résumer, reformuler. »

**Pourquoi ça coince** : la fiche et le titre « (j'ai fait le calcul) » tiennent sans test. Mais la promesse de la fin (« je te dis ce qui tient vraiment chez moi ») ne peut pas être payée avec un conditionnel. C'est une boucle ouverte jamais refermée.

**Correction**, dans l'ordre de préférence :
1. **Un essai, même court, sur ta 5080 avant la voix** (prévu en S1 dans le calendrier) : un modèle de 16 Go ou moins, sa vitesse, une tâche réelle. Une seule mesure suffit pour refermer la boucle. Le détail reste pour le 16 novembre.
2. Sinon, **change la promesse du 0:35** : supprime « je te dis ce qui tient vraiment chez moi », et fais du 16 novembre une boucle ouverte assumée dès le début (« la réponse sur ma carte, je la mesure, et elle sort le 16 »).

### 3. Pas de problème profond

**Pourquoi ça coince** : Kai ouvre sur « je m'étais trompé depuis un an », Morgans sur « j'ai dit 14 000 $, j'avais tort ? » (voir [`etudes/outliers-2026-10-22.md`](../../etudes/outliers-2026-10-22.md)). Ici, le narrateur n'a aucune raison personnelle de faire ce calcul. Le ⟦à écrire⟧ sur ton avis arrive à 11:30, beaucoup trop tard.

**Correction** : une phrase à toi entre 0:25 et 0:40, et sa réponse dans le verdict. Pistes, à toi de dire laquelle est vraie :
- [l'abonnement : tu paies déjà ⟦combien⟧ par mois et tu en as marre] ;
- [une limite d'usage atteinte en plein travail] ;
- [ce que tu ne colles jamais dans Claude : tu as dit le 20/10 que tu ne donnes jamais une clé d'API à un outil tiers] ;
- [la dépendance à une boîte américaine, vue d'Afrique].

### 4. Le bloc technique arrive trop tôt et déborde

> « ⚠️ à vérifier : 552 plus 196 ne font pas 763… »
> « Reste le cache, la mémoire de la conversation. Ici, DeepSeek annonce environ huit cent quatre-vingt-dix octets par token… »

**Pourquoi ça coince** : de 3:15 à 5:20, on enchaîne la quantification, la vérification de la formule, Engram, l'écart de paramètres, le cache et la formule de vitesse. Le spectateur attend un prix depuis 0:35. Le tableau de décrochage le classe lui-même en risque « élevé ».

**Correction** :
- **Garde** : le calcul 16/8/4 bits, le JPEG de l'IA, Engram sur l'étagère (c'est une vraie surprise, et l'analogie bureau/bibliothèque est bonne).
- **Coupe** : l'écart 552/763 (le laisser dans `sources.md`) et la vérification « 316 × 8 ÷ 552 » dite à voix haute (elle peut rester en `[VISUEL]`).
- **Réduis le cache à une phrase** : « la mémoire de la conversation, elle, tient dans moins d'un giga ».
- **Déplace la formule de vitesse** au début de l'étape 1, là où elle sert pour la première fois.

### 5. L'étape 4 change de modèle

> « Le plus gros modèle ouvert du moment est Kimi K3… Chez Scaleway, il faut huit cartes B300… »

**Pourquoi ça coince** : tout le calcul suit DeepSeek, et d'un coup on passe à un autre modèle, sans tableau de niveau face à Claude. La seule chose qu'elle apporte est la phrase « Claude pourrait être plus gros ». Les « 8 × H200 chez toi » dans la partie électricité posent le même problème : personne n'a ça chez soi.

**Correction** : réduis l'étape 4 à deux phrases dans la conclusion de l'escalier (« et si Claude est plus gros que DeepSeek, personne ne le sait, la note grimpe encore »). Coupe la ligne H200 du tableau d'électricité. Ça libère environ 40 s pour ton vécu.

### 6. Le « développeur de la communauté » est antirez

> « Je vérifie la formule sur de vrais fichiers, ceux d'un développeur de la communauté qui fait tourner ce modèle sur Mac. »

**Pourquoi ça coince** : le projet ds4 (S5, S9) est d'antirez, le créateur de Redis (⚠️ à confirmer sur son GitHub). C'est un détail « génie derrière l'app » offert, et le script l'efface.

**Correction** : « Je vérifie sur les fichiers d'antirez, le développeur qui a créé Redis, la base de données qui tourne derrière ⟦un exemple que ton public connaît, à vérifier⟧. Il a écrit son propre moteur pour faire tourner ce modèle sur Mac. »

### 7. Trop de nombres exacts dits à voix haute

> « Trente mille six cent soixante euros, ce sont trente-quatre mille trois cent cinquante-cinq dollars, divisés par vingt : mille sept cent dix-huit millions. »

**Pourquoi ça coince** : à l'oreille, personne ne retient quatre nombres de cinq chiffres d'affilée. Le visuel est là pour la précision.

**Correction** : arrondis dans la voix, précis à l'écran.
> « Avec ce budget, tu achètes chez Anthropic environ un milliard sept cents millions de tokens d'Opus 5.5. Pour faire mieux, ton serveur doit écrire six cent cinquante tokens par seconde, jour et nuit, tout le mois. »

Même traitement pour les étapes 2 et 3 (« trente-neuf », « dix-huit », « cent trente » : garde un nombre par phrase).

### 8. Le spectateur ne participe pas

**Pourquoi ça coince** : le meilleur moment pour le faire réfléchir est sous tes yeux. Le prix du Mac Studio 512 Go n'est pas publié.

**Correction**, juste avant le palier 2 :
> « Apple n'a pas encore donné le prix de la version 512 Go. Tente ton chiffre en commentaire, je l'épinglerai à côté du vrai. »

⚠️ Si Apple publie le prix avant ta prise de voix, remplace par le vrai prix et garde la question pour une autre machine.

### 9. Une comparaison « oubliée » qui ne l'est pas

> « Maintenant, la comparaison que ces vidéos oublient presque toutes. »

**Pourquoi ça coince** : c'est faux, Kai l'a faite (« Can a Mac Mini Replace your $200 AI Subscription? », voir [`etudes/kai.md`](../../etudes/kai.md)). En plus, comparer un serveur à 30 000 € par mois à un abonnement est un homme de paille, puisque personne ne loue ce serveur pour lui seul.

**Correction** : la comparaison utile, c'est ta machine face à l'abonnement. « Les 2 500 € de RAM, c'est ⟦28⟧ mois d'abonnement Max. » (2 500 ÷ 89 ≈ 28 : à recalculer avec le prix final). Garde une phrase sur le seuil de l'API pour les équipes.

⚠️ « Louer, acheter ou s'abonner ? » sort le 4 janvier : reste à une ou deux phrases ici, et annonce cette vidéo plutôt que de la faire en avance.

### 10. Les tics d'IA

| Passage | Problème | Réécriture |
|---|---|---|
| « Ce n'est probablement pas ce que tu crois. » | Faux suspens | Supprimer, ou dire le chiffre : « Et à la fin, ce que deux mille cinq cents euros changent sur ma carte. » |
| « Précision qui change tout : tu paies à l'heure. » | Faux suspens | « Ce serveur se loue à l'heure : deux heures de test, quatre-vingt-quatre euros. » |
| « Un mélange, donc, pas un grand soir. » | Fausse opposition, et le « grand soir » est déjà dit à 0:40 | Supprimer : la phrase d'avant suffit |
| « compléter du code, résumer, reformuler » | Rafale de trois | Remplacer par la tâche que tu auras testée |
| « vaut pour un modèle qui joue dans la même cour que Claude, pas pour Claude » (et les variantes à 2:30, 8:30 et 13:00) | Même réserve martelée 4 fois | Garde-la en 2:30 (tableau) et une fois à la fin ; coupe-la à l'étape 3 |
| « C'est ma règle des trente pour cent » | Formule grandiloquente pour deux mesures | « Deux mesures, c'est peu. Je m'en sers comme d'une règle de pouce : trente pour cent du plafond. » |

## Les faits à reprendre avant la voix

| Point | Pourquoi | Où |
|---|---|---|
| **La 5080 à 2 040 €** | Un seul modèle, chez un seul marchand, et presque le double du prix de lancement (1 169 €). Tu en as une : combien l'as-tu payée, et quand ? | S7 |
| **La RAM à 2 500 €** | Le calcul triple un kit de 2 × 32 Go, mais une carte mère grand public ne prend pas 6 barrettes : il faut un kit de 4 × 48 Go, au prix inconnu. C'est le chiffre de l'accroche si tu prends l'option A ou B : il doit être solide | S8 |
| **Combien de RAM tu as** | Si tu as déjà 64 ou 96 Go, le surcoût n'est pas le même. Et ta carte mère accepte-t-elle 192 Go ? | ⟦à toi⟧ |
| **Les 6 tokens/s** | C'est une estimation (90 Go/s, règle des 30 %) qui ne compte pas les experts gardés sur la carte graphique, ce qui accélère. Une mesure de tiers existe sur un PC avec beaucoup de RAM : Morgans Code cite environ 10 tokens/s sur une station Dell de 2014 avec 256 Go, d'après Digital Spaceport, avec le moteur Maya ([vidéo](https://www.youtube.com/watch?v=mat0oOXVCcU)). Remonte à la source de Digital Spaceport et cite-la comme « mesure d'un tiers », sans reprendre l'angle « station d'occasion » de Morgans | S9 |
| **Le prix du Mac Studio 512 Go** | Annoncé fin octobre, ta voix est prévue en S2 (26/10-1/11) | S10 |
| **ds4 = antirez** | Confirme sur le GitHub avant de le dire | S5 |

## Ce qu'il faut garder

- **« C'est un Rattata qui défie Mewtwo. »** Tu as déjà fait Mewtwo dans Uber : c'est ta signature.
- **Le boss de Monster Hunter** dont une seule patte bouge : l'image des experts est juste, et elle est à toi.
- **Le tableau vert puis rouge** et « au niveau de Claude, c'est vrai sur certains tests et faux sur d'autres » : c'est l'honnêteté qui manque à Kai.
- **« C'est le JPEG de l'IA »** : la meilleure explication de la quantification en une phrase.
- **Engram sur l'étagère** : une vraie découverte de recherche, que les vidéos anglophones ne racontent pas.
- **La règle des 30 % confrontée à deux mesures** : c'est la règle 3 du format calculé, appliquée.
- **« Je te parle de te désabonner de quelque chose, et je te demande de t'abonner à autre chose. »** : la pique contre les abonnements, dans ton style.
- **Le tarif EDF** : la critique que les Européens font à Kai, réglée en une ligne.

## Plan d'action

1. **Choisir l'accroche** (option A ou B), et aligner l'étiquette de la miniature sur le même chiffre.
2. **Écrire tes ⟦à écrire⟧** : ton enjeu (à placer vers 0:30), la vraie question Reddit ou X avec ses trois réponses, et ton avis pour le verdict.
3. **Faire un essai sur la 5080 avant la voix**, ou changer la promesse du 0:35 (grill n° 2).
4. **Alléger** le bloc technique et l'étape 4 (grill n° 4 et 5), arrondir les nombres dits (n° 7), corriger les tics (n° 10).
5. **Revérifier à la source** le prix de la RAM 4 × 48 Go, celui de ta 5080 et la mesure de Digital Spaceport, puis le prix du Mac le jour de la voix.
