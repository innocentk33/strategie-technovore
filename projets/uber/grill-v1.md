# Grill du brouillon Uber v1 (19/10/2026)

> Script grillé : [`brouillon-v1.md`](brouillon-v1.md). Grille : `youtube-script-grill`, mode B.
> Hypothèses : titre *Le génie caché derrière la carte en temps réel d'Uber*, miniature « COMMENT ?! » sur la carte en hexagones (fiche), public de 18-30 ans curieux de tech avec une bonne part de devs (anciens abonnés Flutter/Kotlin), objectif : lancer le pilier « Le génie derrière l'app ».
> Faits revérifiés à la source le 19/10 : voir « Faits vérifiés » en bas.

## Verdict

Le squelette est bon. Le fil rouge (suivre la position d'un chauffeur jusqu'à l'écran du passager) donne une raison d'avancer, les images sont fortes (le stade, le gamin à l'arrière, l'ombre des immeubles), et la vidéo apporte trois choses absentes de celle de Philipp Lackner : le GPS qui se trompe de 50 m, la correction sur Kalman et les pentagones en mer. Les « mais / donc » tiennent presque partout, et il y a bien moins de tics d'IA que dans la v1 d'ArtCraft.

Le plus gros problème : on n'entend pas encore le narrateur. Le texte tutoie alors que tu as dit « vous » tout au long d'ArtCraft, ta seule matière perso est l'anecdote du pote, et le texte te prête un avis que tu n'as pas donné (« c'est la partie que je préfère »). Deuxième problème : à 7:05, au moment le plus fragile, la position suivie change de téléphone sans prévenir.

Rien de bloquant. Une passe sur le hook, la section 4 et la fin suffit, plus ta réponse à la question en bas.

## Tableau de bord

| Axe | Note | En une phrase |
|---|---|---|
| Promesse | 🟠 | Les hexagones arrivent en 5 s, mais le hook leur prête un rôle (« pour les afficher ») et une échelle (570 000 milliards) que les sources ne donnent pas. |
| Alignement | 🟢 | Aucune vente forcée ; les deux appels à l'abonnement sont courts et bien placés. |
| Problème profond | 🟠 | La question « ce que je vois sur ma carte est-il vrai ? » est là ; l'enjeu du narrateur manque. |
| Public & complexité | 🟢 | Chaque terme technique arrive après son explication (polling, k-ring, SSE, Kalman), avec un bandeau pour les devs. |
| Valeur & originalité | 🟢 | GPS et ombres radio, Kalman écarté, pentagones en mer, accusés de réception à 30 s : rien de tout ça chez Lackner ni en français. |
| Structure & transformation | 🟠 | Le trajet trouver/envoyer/afficher est clair, mais la section 4 parle du GPS du passager alors qu'on suivait celui de Karim. |
| Histoire | 🟠 | Le narrateur est convaincu à 0:50 (« Il avait raison. ») et ne traverse aucun moment bas. |
| Mais / donc | 🟢 | Très bien dans les sections 3 et 4 ; un passage « et aussi » entre 3:00 et 4:20. |
| Engagement actif | 🟠 | Une bonne boucle ouverte (voitures fantômes), mais on ne demande jamais au spectateur de deviner. |
| Rythme & oralité | 🟢 | Phrases courtes, écrites pour être dites ; à repasser au « vous ». |
| Tics d'IA | 🟠 | Une dizaine d'occurrences légères (fragments, « le vrai problème », annonces), aucune grave. |

## Le grill

### 1. Le narrateur n'est pas encore toi

> « On tutoie le spectateur, comme dans le hook validé (« Ouvre Uber »). »

Dans ArtCraft, tu dis « vous » du début à la fin : dans ton brouillon, puis dans la prise que tu as enregistrée toi-même (18 « vous », zéro « tu » dans le téléprompteur). Si tu enregistres encore toi-même, un téléprompteur au « tu » va te faire trébucher, ou tu mélangeras les deux en cours de prise. Le « Ouvre Uber » de `strategie.md` est une proposition écrite ; ta voix réelle, c'est la prise d'ArtCraft.
**Correction :** tout passer au « vous » dans la v2 (les réécritures ci-dessous le sont déjà). Si tu préfères le « tu » pour cette série, dis-le et je le garde.

> « Moi, j'ai fait comme tout dev qui se respecte : je ne l'ai pas cru, et je suis allé vérifier. J'ai lu les articles, un par un. / Il avait raison. »

Trois soucis :
- La fiche dit seulement « J'ai vérifié, et j'ai vu tout ce qu'ils ont accompli ». « Je ne l'ai pas cru » et « un par un » sont des ajouts.
- « Il avait raison » ferme à 0:50 la seule question que le narrateur se posait. Il n'a plus rien à découvrir pendant dix minutes.
- Nulle part on ne sait ce que toi, dev, tu aurais fait à la place d'Uber.

> « Et honnêtement, c'est la partie que je préfère. »

Même problème que le « j'ai résilié Netflix » d'ArtCraft, en plus petit : une opinion que tu n'as pas donnée. Garde-la seulement si elle est vraie, avec ta raison.

**Correction :** déplacer le verdict à la fin et laisser une place à ton vécu.

Section 1 :
> Un jour, un pote m'a dit : « Les ingés d'Uber, c'est des génies. » Il avait lu leur blog d'ingénierie. [Ta vraie réaction sur le moment.] Alors j'ai lu les articles. Tout ce que je vais vous montrer vient de là, écrit par les ingénieurs eux-mêmes, et les liens sont en description. À la fin, je vous dirai si mon pote avait raison.

Section 3, juste après « Ça s'appelle le polling » :
> [Si c'est vrai : « Et je ne vais pas faire le malin : dans [ton appli Flutter ou Kotlin], j'ai fait exactement pareil. [Ce qui s'est passé : batterie, serveur, avis sur le store…] »]

Fin, après « Tout ça pour un geste que vous faites en deux secondes » :
> Alors, mon pote avait raison ? [Ton verdict, avec la partie qui t'a le plus surpris et pourquoi.]

### 2. À 7:05, la position change de téléphone

> « Le vrai problème, lui, il est dans ta poche. » … « Le GPS de ton téléphone, en ville, il se trompe. » … « C'est Karim qui t'attend à la mauvaise sortie de la gare. » … [VISUEL : le point bleu saute d'un trottoir à l'autre]

Depuis 0:33, on suit la position de Karim. La section 4 parle soudain du GPS du passager (le point bleu, « ta poche »), puis la fin récapitule « Le téléphone de Karim envoie une position qui peut être fausse de cinquante mètres ». Le spectateur ne sait plus quel téléphone se trompe, et ça tombe à 61 %, le point de décrochage noté dans le brouillon.

Il y a une meilleure idée cachée là. L'erreur GPS se produit au tout début du trajet, avant les hexagones, et le script la raconte en dernier : autant en faire un retournement. La position qu'on a suivie pendant sept minutes était peut-être fausse dès le départ.

**Correction** (fin de section 3, relance, début de section 4) :
> La position de Karim arrive jusqu'à vous, en direct, sans vider votre batterie. Mais depuis le début, je fais comme si elle était juste.
>
> [SON : la musique coupe net, une seconde de silence.]
>
> En ville, elle peut être fausse de cinquante mètres. Ce sont les ingénieurs d'Uber qui le disent, et parfois c'est pire. Cinquante mètres, c'est l'autre côté du boulevard. Sur votre carte, Karim vous attend devant la gare. En vrai, il est garé en face.
>
> Le téléphone de Karim calcule sa position avec le temps que mettent les signaux des satellites à lui arriver. Mais en ville, il y a des immeubles. Un signal tape contre une façade, rebondit, et arrive en retard. Le téléphone croit alors que le satellite est plus loin qu'en réalité, et il se place au mauvais endroit.

Visuel : c'est la voiture de Karim qui saute, plus le point bleu. La réécriture règle aussi « Ton téléphone croit alors que tu es plus loin », qui ne disait pas plus loin de quoi, et elle supprime deux tics (« Un seul problème : » et « Le vrai problème, lui »).

### 3. Le hook en dit plus que les sources

> « Pour les afficher, Uber a dû découper la planète en hexagones. » / « Près de cinq cent soixante-dix mille milliards d'hexagones. »

L'article H3 d'Uber (relu le 19/10) dit que H3 sert à « optimiser les prix et le dispatch » et à analyser le marché ville par ville. Il ne dit nulle part que l'appli s'en sert pour afficher les voitures autour du passager : ce lien vient de Lackner. Et 570 000 milliards, c'est le niveau le plus fin de la grille (0,9 m² la case) ; rien n'indique qu'Uber descende jusque-là. Avec une audience pleine de devs, quelqu'un le relèvera en commentaire, et l'erreur tombe dans les 15 premières secondes.

**Correction :** deux tournures à changer, la promesse reste intacte.
> Ouvrez Uber. Vous voyez ces petites voitures autour de vous ? Pour vous trouver un chauffeur, Uber a découpé la planète en hexagones.
>
> [dézoom]
>
> Une grille qui peut descendre jusqu'à cinq cent soixante-dix mille milliards de cases. Aujourd'hui, on suit une de ces voitures, du téléphone du chauffeur jusqu'au vôtre.
>
> Sur ce trajet, sa position passe par un serveur bombardé de « du nouveau ? » et par un GPS qui se trompe de cinquante mètres en ville. Et en 2015, deux chercheurs ont posé une question gênante : est-ce que toutes ces voitures existent vraiment ?

L'enjeu perd au passage sa rafale de trois fragments (« Un serveur… Un GPS… Et une question… ») et le compte « trois problèmes », qui faisait doublon avec les trois étapes de la carte du trajet 50 secondes plus tard.

### 4. Les voitures fantômes : bonne boucle, chute molle

> « Il y en aurait donc plutôt plus que ce que tu vois. Pas moins. » / « C'était en 2015, et l'appli a beaucoup changé depuis. Mais avoue : une voiture qui glisse sur ta carte, tu ne la regardes plus pareil. »

La question ouverte à 0:30 est la meilleure du script. Mais la réponse se résume à « des chercheurs disent ça, Uber dément », sans rien réutiliser de ce qu'on vient d'apprendre. Or l'article d'origine (Motherboard, relu le 19/10) contient le pont : sur les forums, des chauffeurs expliquaient les fantômes par un décalage de 30 à 60 secondes dans le système. D'autres en voyaient partout où le passager posait son épingle, ce qu'aucun décalage n'explique.

Précision : l'exemple des quatre voitures et des 17 minutes vient d'une chauffeuse, Heather, qui a ouvert l'appli côté passager, et c'est à elle que le support d'Uber a parlé d'« effet visuel ». C'est plus concret que « on peut voir… ».

**Correction** (après le démenti d'Uber) :
> Sur les forums, certains chauffeurs avaient leur explication : un décalage de trente à soixante secondes dans le système. Ce décalage, vous savez maintenant d'où il peut venir : un message qui arrive en retard, une voiture qu'on fait glisser en devinant où elle va. D'autres chauffeurs voyaient des voitures fantômes partout où le passager posait son épingle. Ça, aucun décalage ne l'explique.
>
> Uber a démenti, et l'appli a beaucoup changé depuis 2015. Mais la voiture qui glisse sur votre carte, maintenant, vous savez ce que c'est : au mieux, la position d'un chauffeur d'il y a quelques secondes, en partie devinée.

Supprime du coup « Donc la voiture que tu vois sur ta carte, c'est souvent une estimation. Une bonne estimation. Mais une estimation. » en fin de section 4 : la nouvelle chute dit la même chose, au bon moment.

### 5. Le restaurant : « serveur » veut dire deux choses

> « Fireball, c'est le serveur en salle. » … « Et le serveur RAMEN, c'est le livreur. »

Dans une vidéo sur des serveurs informatiques, un « serveur en salle » suivi d'un « serveur RAMEN » qui joue le livreur, ça se mélange à l'oreille. Et un restaurant avec un livreur, c'est Uber Eats : autant le dire.

**Correction :**
> RAMEN, c'est trois pièces. Pour les comprendre, prenez Uber Eats.
>
> Fireball, c'est le gérant. Il voit passer chaque événement : un passager commande, un chauffeur accepte, une voiture bouge. Et pour chacun, il décide qui doit être prévenu, et quand.
>
> L'API gateway, c'est la cuisine. Elle prépare la commande : toutes les données dont votre appli a besoin, au bon format.
>
> Et RAMEN, c'est le livreur. Il garde une connexion ouverte avec votre téléphone, et il livre avec une promesse : chaque message arrive au moins une fois.

Bonus si ça te fait rire : « Pour livrer ses positions, Uber s'est fait un Uber Eats interne. » À toi de voir si c'est ton humour.

### 6. Entre 3:00 et 4:20, une suite de « et aussi »

> « Maintenant, dézoome. » … « Enfin… presque que des hexagones. » … « Et ces hexagones servent partout. Le prix dynamique, par exemple »

Juste après l'appel à l'abonnement, trois faits s'enchaînent sans que l'un rende l'autre nécessaire : les seize niveaux, les pentagones, le prix dynamique. Chacun est bon ; c'est l'enchaînement qui est plat, à l'endroit où le CTA vient de sortir une partie des spectateurs de la vidéo.

**Correction :** donner une raison aux seize niveaux, enchaîner sur le prix, et garder les pentagones en dernier comme récompense.
> Sept cases, ça suffit pour trouver Karim. Mais pour fixer un prix, Uber doit regarder tout un quartier, parfois toute une ville. Donc H3 a seize niveaux de zoom…

Puis le « ×1,8 », puis les pentagones, puis « Uber sait maintenant quels chauffeurs sont autour de vous ».

### 7. Le spectateur ne devine jamais

> « Le réflexe, c'est de prendre des carrés. Sauf que les carrés ont un défaut. Regarde ta case… »

Le script explique tout d'emblée. Le défaut des carrés se prête bien à une devinette : la grille est à l'écran, la réponse tient en une image.

**Correction :**
> Le réflexe, c'est de prendre des carrés. Regardez la grille deux secondes : vous voyez le défaut ?
>
> [VISUEL : la grille seule, sans flèches, 2 s. Puis les flèches.]

Autre option : « À votre avis, combien d'hexagones au niveau le plus fin ? » avant le compteur de 3:15, à condition de retirer le chiffre du hook. Une seule devinette suffit.

### 8. Les tics d'IA

Une dizaine, tous légers. Les plus audibles :

| Passage | Tic | Réécriture |
|---|---|---|
| « Le vrai problème, lui, il est dans ta poche. » | fausse opposition (les serveurs posaient aussi de vrais problèmes) | supprimé par la correction n° 2 |
| « Un seul problème : elle est peut-être fausse. » | annonce | idem |
| « c'est souvent une estimation. Une bonne estimation. Mais une estimation. » | cascade de fragments | supprimé par la correction n° 4 |
| « publient une idée tordue. Et géniale. » | fragment dramatique | « En 2018, des ingénieurs d'Uber ont une idée tordue : se servir du problème comme d'un indice. » |
| « Il y en aurait donc plutôt plus que ce que tu vois. Pas moins. » | fragment | « Il y aurait donc plus de voitures que ce que vous voyez. » |
| « Uber ne regarde plus le monde entier. Juste ta case… » puis « Uber ne parcourt plus un million de chauffeurs. Seulement ceux… » | même construction deux fois en une minute | garder la seconde ; dire la première au positif : « Quand vous ouvrez l'appli, Uber regarde votre case et celles d'à côté. » |
| « Le plus drôle, c'est ce qu'un employé… » / « Et le meilleur, c'est que H3 est open source. » | annonces | « Le support d'Uber a même répondu à cette chauffeuse… » / « Et H3 est open source. » |
| « Il avait raison. » | phrase-choc isolée | déplacée à la fin (correction n° 1) |
| « de la batterie, du réseau, et du travail pour le serveur » + « trois problèmes », « trois étapes », « trois pièces », « trois lignes » | rafales de trois | les étapes, les pièces et les lignes sont des faits, garde-les ; retire « trois problèmes » (n° 3) et passe la batterie à deux : « de la batterie et du travail pour le serveur » |

### 9. Petits points

- **Kalman.** Bonne correction de Lackner, qui l'affirme. Garde la portée exacte : l'article de 2018 explique pourquoi Kalman ne convient pas à *ce* problème, sans dire qu'Uber n'en utilise nulle part. Ajoute « pour ce problème-là » pour que personne ne l'entende comme un démenti général.
- **Source gRPC.** Le lien `eng.uber.com/blog/...` renvoie une 404. L'article est en ligne sur https://www.uber.com/blog/ubers-next-gen-push-platform-on-grpc/.
- **⚠️ des pentagones.** Il peut sauter : la doc H3 le confirme (voir plus bas).
- **Shorts.** Les notes de montage prévoient un 2e Short le 19/11. Depuis la décision d'aujourd'hui (1 Short par vidéo longue), il ne reste que celui du 12/11 ; le reste passe en réserve.

## Ce qu'il faut garder

- « C'est comme chercher Karim dans un stade en demandant à chaque spectateur : « T'es Karim ? » » La meilleure image du script : on comprend le problème en une seconde.
- Le gamin « On est arrivés ? » pour le polling. Drôle, juste, et il prépare les bulles « Du nouveau ? / Non. ».
- « Non, pas les nouilles. […] Ils ont clairement trouvé le nom avant. » Une respiration juste avant le bloc le plus dense.
- « Quelque part au milieu de l'eau, il y a douze cases à cinq côtés où aucun Uber ne passera jamais. » Désormais sourcé, et c'est le genre de phrase qu'on répète à un pote.
- « Le fameux « ×1,8 » un samedi à deux heures du mat ? C'est ton hexagone qui a décidé. » Le seul moment où la technique touche le portefeuille du spectateur.
- « Ils se repèrent grâce à l'ombre des immeubles. » Une idée contre-intuitive en une phrase.
- « Uber n'a pas détaillé comment l'appli anime ses voitures. Mais les jeux en ligne utilisent… » Dire ce qu'on ne sait pas rend crédible tout le reste.
- Le lag sur Monster Hunter et le Rathalos : ton registre.
- La fin sur trois lignes de Python : un cadeau pour les devs, et une sortie concrète.

## Plan d'action

1. **Répondre à la question** ci-dessous et trancher tu/vous : le reste en dépend.
2. **Section 4** : passer sur le téléphone de Karim et assumer le retournement (n° 2). C'est la plus grosse modification de structure, une dizaine de lignes.
3. **Hook** : « pour vous trouver un chauffeur » et « une grille qui peut descendre jusqu'à » (n° 3).
4. **Fin** : brancher le décalage de 30 à 60 s sur les voitures fantômes (n° 4), puis le verdict du pote en conclusion (n° 1).
5. **Passe de détail** : Uber Eats (n° 5), la transition des seize niveaux (n° 6), la devinette des carrés (n° 7), les tics (n° 8), la source gRPC.

## Faits vérifiés le 19/10

| Fait du script | Verdict | Source |
|---|---|---|
| H3 sert à afficher les voitures autour du passager | ❌ non sourcé : l'article parle de prix, de dispatch et d'analyse du marché | [Uber, H3 (2018)](https://www.uber.com/blog/h3/) |
| 12 pentagones par niveau, tous en mer | ✅ « places all 12 icosahedron vertices in the ocean » (orientation Dymaxion) | [h3geo.org, Overview](https://h3geo.org/docs/core-library/overview) |
| 16 niveaux, open source en 2018 | ✅ | [Uber, H3 (2018)](https://www.uber.com/blog/h3/) |
| Plus de 40 M de courses et livraisons par jour | ✅ 3 867 M au T2 2026 ÷ 91 jours ≈ 42,5 M | [Uber, résultats du T2 2026](https://www.sec.gov/Archives/edgar/data/0001543151/000154315126000027/uberq226earningspressrelea.htm) |
| Accusés de réception toutes les 30 s avec SSE, gRPC pour le bidirectionnel | ✅ article du 16/08/2022 | [Uber, push sur gRPC](https://www.uber.com/blog/ubers-next-gen-push-platform-on-grpc/) |
| 4 voitures, 17 min d'attente | ✅ vu par une chauffeuse (Heather) sur l'appli passager | [Motherboard (Vice)](https://www.vice.com/en/article/ubers-phantom-cabs/) |
| « Effet visuel », « économiseur d'écran », dit à un chauffeur | ✅ e-mail du support d'Uber à Heather | [Motherboard (Vice)](https://www.vice.com/en/article/ubers-phantom-cabs/) |
| Démenti d'Uber, latence, 8 voitures les plus proches | ✅ porte-parole cité par The Guardian, repris par Fortune | [Fortune, 30/07/2015](https://fortune.com/2015/07/30/uber-phantom-cars) |
| Décalage de 30 à 60 s avancé par des chauffeurs | ✅ nouveau, pour la correction n° 4 | [Motherboard (Vice)](https://www.vice.com/en/article/ubers-phantom-cabs/) |

Pas revérifiés aujourd'hui : les 80 % de polling, les 1,5 M de connexions et les 50 m d'erreur GPS. Leurs sources sont dans le brouillon, à relire avant la voix.

## La question

Dans tes applis Flutter ou Kotlin, as-tu déjà fait du polling, ou affiché sur une carte une position qui sautait ? Si oui : quelle appli, et qu'est-ce qui s'est passé ? C'est ce qui manque pour donner un enjeu au narrateur (n° 1). Sinon, dis-moi ce que tu as vraiment pensé quand ton pote t'a parlé du blog, et je partirai de là.
