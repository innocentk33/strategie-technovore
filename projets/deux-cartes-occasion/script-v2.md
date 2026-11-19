# 32 Go pour Qwen 27B : les prix, les routes et leurs pièges

Version corrigée après roast indépendant ; relevés du16/11/2026. Prix par référence, classement global non établi.

<!-- METRICS -->
**Voix : 1859 mots · 12:49 à 145 mots/min.** Les balises ne sont pas lues.

| Partie | Début estimé |
|---|---|
| Résultat, question et plan | 0:00 |
| La conversation remplit aussi la carte | 0:36 |
| Les paires et leurs restrictions | 2:31 |
| Les 32 gigas sur une seule carte | 4:19 |
| Acheter la machine complète | 7:02 |
| Ce que la tour doit accueillir | 8:48 |
| Les recours et le choix final | 10:31 |
<!-- /METRICS -->

## Voix
[VISUEL : ASRock Arc Pro B65 32GB1799,95€ etGigabyte R9700 32GB2799,95€, LDLC16/11/2026, toutesdeuxenstock. F85,F91,F95]

1000 euros d’écart entre deux références de 32 gigas chez le même marchand. Pourtant, aucune ne garantit tout le contexte de Qwen 27B. Donc quelle route te donne la mémoire utile sans transformer ton PC en chantier ?

On compare les cartes seules, les paires et les ordinateurs complets. On calcule la place de la conversation, puis on regarde ce que ta tour peut accueillir. Le choix dépend aussi de ce que tu possèdes déjà.

### La conversation remplit aussi la carte

[GRAPHIC] [VISUEL : fichier + conversation + tampons, trois zones d'une même jauge. F80/F81.]

Pour Qwen 27B en 4 bits avec une conversation courte, 24 gigas peuvent déjà suffire. Les 32 deviennent intéressants quand tu veux davantage de contexte, une copie moins compressée ou plus de marge. Du coup, acheter seulement parce qu'un titre affiche « full context », ça peut te coûter une carte pour rien.

La mémoire de conversation grossit pendant que tu discutes. Elle garde des informations utilisées pour la suite. Ton fichier de modèle garde sa taille, mais cette réserve-là se remplit. Donc un modèle qui se charge au début ne promet pas une conversation longue sans débordement.

Dans la configuration officielle de Qwen 3.8 27B, on peut calculer la partie principale de ce cache. En précision 16 bits, c'est environ 2 gigas binaires à 32 mille tokens, 8 à 128 mille, et 16 à la fenêtre native complète. Attention, c'est un calcul théorique, hors autres allocations. On n'a pas lancé ces conversations sur les cartes du tableau.

Et là, tu vois le problème. Les poids du fichier 4 bits retenu ici prennent déjà plus de 15 gigas binaires. Ajoute 16 pour le contexte complet. Il reste une toute petite marge sur 32, avant les tampons et le reste du moteur. Donc il faudra réduire le cache, le contexte, ou choisir une autre copie du modèle. Le chiffre sur la boîte ne fait pas disparaître cette addition.

Par contre, quantifier le cache peut rendre cette route beaucoup plus réaliste. On doit simplement annoncer le réglage avec la capacité. « 32 gigas » tout seul ne décrit pas la conversation que tu pourras garder. Donc le premier achat à comparer doit répondre à cette capacité utile, avec son réglage de cache. [F80,F81]

[VISUEL : tableau de prix daté du 16/11, stock et restrictions écrits en gros. F86/F87.]

### Les paires et leurs restrictions

Deux Intel Arc A770 de 16 gigas donneraient 32 gigas de capacité physique. Chez un marchand français, la référence consultée affiche 459,95 euros TTC. Le calcul donne donc 919,90 euros pour deux. Sauf que la page indique une rupture en ligne. C'est un repère affiché, pas une paire que je te promets de commander ce soir.

En fait, la capacité obtenue explique l’intérêt des paires. Sauf que la facture dépend aussi de leur installation dans ta tour. On y revient avec les contraintes de la tour.

Côté NVIDIA, on peut aussi regarder deux RTX 5060 Ti de 16 gigas. La référence ASUS consultée affiche 1 079,95 euros TTC, en stock. Donc deux fois ce prix donnent 2 159,90 euros, avant tout changement du PC. Et il y a une autre ligne à lire : limitée à une carte par client. Ce total est un calcul de comparaison ; cette fiche ne permet pas de commander la paire telle quelle.

Du coup, on garde le nom complet, les 16 gigas et la restriction. Vérifier la capacité exacte évite de commander une autre version.

Si cette vidéo t'a évité un mauvais achat, abonne-toi.

Deux RTX 3060 de 12 gigas donnent 24 gigas. Elles peuvent répondre à un besoin plus modeste, mais elles n'atteignent pas notre palier de 32. Deux RTX 3090 donnent 48, avec d'autres contraintes de place et d'alimentation. Et deux Radeon de 16 gigas constituent encore une autre route. Les annonces d'occasion françaises ne sont pas assez vérifiables ici pour leur inventer un prix actuel : elles restent hors classement économique. [F90]

[VISUEL : une seule carte prend place dans le boîtier dessiné. F82–F85.]

### Les 32 gigas sur une seule carte

Une seule carte de 32 gigas simplifie une partie du problème physique. La Radeon AI PRO R9700 a bien 32 gigas de mémoire dédiée. La référence Gigabyte consultée affiche 2 799,95 euros TTC, en stock, le 16 novembre. C'est une offre précise chez un marchand, pas le prix minimum de toutes les R9700.

Donc tu paies ici la capacité sur une seule carte, avec un environnement logiciel AMD à vérifier pour ton usage. La présence de 32 gigas ne transforme pas tous les outils CUDA en outils compatibles. Le programme qui lance ton modèle compte aussi dans l'achat.

Par contre, chez le même marchand, l’ASRock Arc Pro B65 de 32 gigas est affichée 1799,95 euros TTC, en stock le 16 novembre. La B70 de 32 gigas est affichée 2299,95 euros, également en stock. Donc on retrouve les 1000 euros de l’ouverture entre la B65 et la Gigabyte R9700. Les deux Intel ont elles-mêmes 500 euros d’écart. [F91,F92,F95]

En fait, le prix le plus bas de ces trois références est celui de la B65. Pour en faire le meilleur achat pour toi, il faudrait aussi comparer ton moteur et ton modèle. Aucun résultat de vitesse commun aux trois cartes n’est établi dans ce relevé. Donc on peut classer ces prix affichés, tout en gardant la question du confort ouverte.

Une autre R9700, l’ASRock Creator, affiche 2349,95 euros TTC. Sauf que son délai dépasse 15 jours. Elle doit garder cette étiquette à côté du prix. [F93]

La RTX 5090 a aussi 32 gigas. L’ASUS TUF consultée affiche 9399,95 euros TTC chez LDLC le 16 novembre, avec un seul exemplaire en stock. Donc elle ajoute une offre NVIDIA à notre comparaison, à un tarif très différent. La V100 d’occasion reste sans prix actuel établi. [F84,F90,F96]

Pour la Tesla V100 de 32 gigas, la version précise change aussi l’installation : une carte prévue pour un serveur ne se transforme pas automatiquement en carte de joueur. Connectique, refroidissement, pilotes, format, il faut un ensemble cohérent. Le dossier rappelle aussi les limites des anciennes générations avec les outils CUDA récents.

En fait, la carte seule peut afficher moins cher et réclamer davantage de travail autour. Si tu débutes et que tu as seulement envie de discuter avec ton IA, ce travail fait partie du coût. On le garde dans le verdict, même s'il n'apparaît pas dans la colonne euros par giga.

[VISUEL : ordinateur compact ; CPU et GPU accèdent à une même réserve. F88/F89.]

### Acheter la machine complète

Mais ton point de départ change encore le calcul si tu remplaces l’ordinateur. Un Ryzen AI Max+ peut employer une grande mémoire partagée avec son GPU intégré. Le mini-PC consulté existe en 64 ou 128 gigas. Et le Mac mini est proposé dans des configurations à 32 ou 64 gigas de mémoire unifiée.

Du coup, on change de comparaison. On achète un ordinateur complet, avec son processeur, son stockage et son système. Si ton PC actuel te sert déjà pour jouer et travailler, son remplacement doit aussi préserver ces usages.

Autre détail : la mémoire partagée sert aussi au système et aux applications. Une configuration à 32 gigas ne promet pas 32 gigas libres pour le GPU. Et avoir une grande réserve ne dit pas à quelle vitesse le modèle écrit. Pour ça, il faut une mesure sur le modèle, le moteur et la configuration concernés.

Pour le Mac mini M6 de 32 gigas avec 512 gigas de stockage, LDLC affiche 1709 euros TTC le 16 novembre, avec un délai supérieur à 15 jours. Du coup, son prix se compare au budget d’un ordinateur complet. Pour le Ryzen, le prix TTC de la configuration exacte reste à établir. [F88,F94]

Voilà pourquoi le comparatif garde deux colonnes : le matériel à ajouter et l'ordinateur à remplacer. Si tu pars de zéro, une machine compacte peut être cohérente. Si tu as déjà une tour adaptée et une carte utile, l'ajout peut demander moins de changements. Le besoin final est le même ; le point de départ change la facture.

[GRAPHIC] [VISUEL : manuel carte mère, dimensions et connecteurs, aucune capture personnelle à produire. F60–F65.]

### Ce que la tour doit accueillir

Reprends la paire d’Intel A770. Même si elle redevient disponible, son prix ne dit toujours pas ce que ta tour peut accueillir. Un deuxième connecteur long sur la carte mère ne signifie pas forcément une liaison aussi rapide que le premier. Dans l'exemple documenté du dossier, le second fonctionne en PCIe 3.0 avec quatre lignes et passe par le chipset. Le manuel donne cette information ; la forme du connecteur ne la donne pas.

Sauf que le connecteur disponible ne règle pas l’espace sous cette carte. Sur une petite carte mère, le port du bas peut mettre le radiateur de la seconde carte tout contre le fond du boîtier. Donc on compare les dimensions réelles et les emplacements disponibles. Une photo avec deux cartes côte à côte ne prouve pas qu'elles rentrent dans ta tour.

Du coup, l’alimentation entre aussi dans la facture. Il faut la puissance, mais aussi les bons câbles et leurs connecteurs. Le dossier distingue les modèles et les prises. On ne transforme pas une prise disponible en branchement compatible à l'aide d'un adaptateur trouvé au hasard.

Par contre, la capacité supplémentaire peut rendre un modèle possible sans accélérer sa réponse. Un moteur peut répartir le modèle entre les cartes. En répartition par couches, pour une seule conversation, les cartes traitent successivement leurs parties. Ajouter la mémoire rend donc certains modèles possibles sans promettre deux fois plus de tokens par seconde. Les détails du partage et des lignes PCIe arrivent dans la suite consacrée aux deux cartes.

[VISUEL : facture vendeur professionnel, calendrier de livraison et étiquette retour. F74–F79.]

### Les recours et le choix final

En fait, une annonce de particulier et une vente professionnelle ne t'offrent pas le même recours. En France, quand un particulier achète à un professionnel, la garantie légale de conformité couvre aussi l'occasion pendant 2 ans à partir de la délivrance. Pour l'occasion, la présomption que le défaut existait déjà dure 12 mois. Ensuite, la question de la preuve change.

Pour un achat à distance auprès d'un professionnel, le droit de rétractation donne en principe 14 jours à partir du lendemain de la réception du bien. Donc une ligne « garantie commerciale 12 mois » ne raconte pas tout. Et ces règles françaises ne deviennent pas automatiquement celles de ton pays si tu regardes depuis Abidjan, Douala ou Kinshasa. Les frais d'importation et les recours locaux doivent être vérifiés séparément.

Alors, quel choix regarder ? Si tu as déjà une carte de 16 gigas et une tour adaptée, compare d'abord le coût de la seconde carte compatible, câbles et place compris. Si tu pars de zéro et que tu veux un ensemble simple, compare aussi une seule carte de 32 gigas. Si tu veux remplacer l'ordinateur, les machines à mémoire unifiée entrent dans la course. Et si ton Qwen en 4 bits avec contexte court tient déjà correctement, garde ton argent tant que tu n'as pas identifié ce qui te manque.

Parmi nos quatre offres immédiatement en stock à une carte de 32 gigas, la B65 affiche le prix le plus bas. Les paires du tableau ont leurs restrictions, et les routes sans prix actuel restent non classées. Donc le choix se fait avec trois lignes devant toi : le fichier, la conversation voulue et le PC que tu possèdes. Le moins cher de ces quatre prix n’établit pas le meilleur achat pour tous les logiciels. [F85–F96]

[CROCHET : ton avis personnel sur le compromis que tu accepterais. Facultatif, sans fait nouveau.]

Jeudi 3 décembre, on regarde une autre route : DeepSeek sans carte graphique, avec 64 gigas de RAM. Le calcul portera sur le coût de cette mémoire et sur ce que la compression fait perdre. Allez, salut !


## Crochets et limites

Avis personnel facultatif. V100, occasion et Ryzen TTC : prix non établis. Pas de performances comparables entre toutes les routes. Aucune manipulation à filmer ; tableaux sources et jauges calculées uniquement.
