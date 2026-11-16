# 32 Go pour Qwen 27B : quelle route coûte vraiment le moins ?

V1 documentaire · diffusion prévue le 30 novembre 2026 · calculs et sources publiques du 16 novembre · cible 11–13 minutes à 145 mots/minute. Les prix encore indisponibles restent entre crochets ; aucun achat ni essai demandé à l'auteur. F1–F79 sont le dossier prévalidé, F80–F90 son complément.

| Partie | Repère de montage |
|---|---|
| Résultat, réserve et question | 0:00 |
| Choisir le contexte avant les cartes | 0:30 |
| Deux cartes de joueur | 2:10 |
| Une carte de 32 Go | 4:00 |
| Un ordinateur à mémoire partagée | 6:00 |
| Le vrai coût de la deuxième carte | 7:40 |
| Garantie et verdict par profil | 9:40 |

## Voix

[VISUEL : deux jauges de 16 Go forment une jauge de 32. Une étiquette « 919,90 € théoriques, rupture » apparaît, puis « 2 799,95 € affichés, stock ». F85/F87.]

Deux cartes de 16 gigas peuvent afficher moins de 1 000 euros à elles deux. Une seule carte de 32 gigas dépasse ici 2 700 euros. Sauf que la première offre est en rupture. Ces chiffres sont les leurs, je n'ai rien testé chez moi. Donc, pour ton Qwen 27B, quelle route donne vraiment de la place sans transformer ton PC en chantier ?

On compare les cartes seules et les paires, on calcule la place de la conversation, puis on ajoute ce que ton PC réclame autour. Et à la fin, tu sauras quelle route regarder selon le matériel que tu as déjà. Avec une mauvaise surprise : avoir 32 gigas ne garantit même pas de remplir tout le contexte.

[GRAPHIC] [VISUEL : fichier + conversation + tampons, trois zones d'une même jauge. F80/F81.]

Pour Qwen 27B en 4 bits avec une conversation courte, 24 gigas peuvent déjà suffire. Les 32 deviennent intéressants quand tu veux davantage de contexte, une copie moins compressée ou plus de marge. Du coup, acheter seulement parce qu'un titre affiche « full context », ça peut te coûter une carte pour rien.

La mémoire de conversation grossit pendant que tu discutes. Elle garde des informations utilisées pour la suite. Ton fichier de modèle garde sa taille, mais cette réserve-là se remplit. Donc un modèle qui se charge au début ne promet pas une conversation longue sans débordement.

Dans la configuration officielle de Qwen 3.8 27B, on peut calculer la partie principale de ce cache. En précision 16 bits, c'est environ 2 gigas binaires à 32 mille tokens, 8 à 128 mille, et 16 à la fenêtre native complète. Attention, c'est un calcul théorique, hors autres allocations. On n'a pas lancé ces conversations sur les cartes du tableau.

Et là, tu vois le problème. Les poids du Q4 historique du dossier prennent déjà plus de 15 gigas binaires. Ajoute 16 pour le contexte complet. Il reste une toute petite marge sur 32, avant les tampons et le reste du moteur. Donc il faudra réduire le cache, le contexte, ou choisir une autre copie du modèle. Le chiffre sur la boîte ne fait pas disparaître cette addition.

Par contre, quantifier le cache peut rendre cette route beaucoup plus réaliste. On doit simplement annoncer le réglage avec la capacité. « 32 gigas » tout seul ne décrit pas la conversation que tu pourras garder. Voilà le besoin fixé. Maintenant, on peut regarder les cartes.

[VISUEL : tableau de prix daté du 16/11, stock et restrictions écrits en gros. F86/F87.]

Deux Intel Arc A770 de 16 gigas donneraient 32 gigas de capacité physique. Chez un marchand français, la référence consultée affiche 459,95 euros TTC. Le calcul donne donc 919,90 euros pour deux. Sauf que la page indique une rupture en ligne. C'est un repère affiché, pas une paire que je te promets de commander ce soir.

La comparaison reste utile : elle montre pourquoi on regarde les paires. Mais tu dois pouvoir acheter les deux cartes, les faire rentrer et employer un moteur qui les utilise. Un prix barré ou une fiche encore présente sur Google ne remplit aucun de ces critères.

Côté NVIDIA, on peut aussi regarder deux RTX 5060 Ti de 16 gigas. La référence ASUS consultée affiche 1 079,95 euros TTC, en stock. Donc deux fois ce prix donnent 2 159,90 euros, avant tout changement du PC. Et il y a une autre ligne à lire : limitée à une carte par client. Ce total est un calcul de comparaison ; cette fiche ne permet pas de commander la paire telle quelle.

Du coup, on garde le nom complet, les 16 gigas et la restriction. Il existe des cartes portant des noms proches avec une autre capacité. Refaire toute une machine et découvrir que tu as acheté la mauvaise version, c'est le boss de fin dont personne ne veut.

Si cette vidéo t'a évité un mauvais achat, abonne-toi.

Deux RTX 3060 de 12 gigas donnent 24 gigas. Elles peuvent répondre à un besoin plus modeste, mais elles n'atteignent pas notre palier de 32. Deux RTX 3090 donnent 48, avec d'autres contraintes de place et d'alimentation. Et deux Radeon de 16 gigas constituent encore une autre route. Les annonces d'occasion françaises ne sont pas assez vérifiables ici pour leur inventer un prix actuel : elles gardent leur mention prix à relever.

[VISUEL : une seule carte prend place dans le boîtier dessiné. F82–F85.]

Une seule carte de 32 gigas simplifie une partie du problème physique. La Radeon AI PRO R9700 a bien 32 gigas de mémoire dédiée. La référence Gigabyte consultée affiche 2 799,95 euros TTC, en stock, le 16 novembre. C'est une offre précise chez un marchand, pas le prix minimum de toutes les R9700.

Donc tu paies ici la capacité sur une seule carte, avec un environnement logiciel AMD à vérifier pour ton usage. La présence de 32 gigas ne transforme pas tous les outils CUDA en outils compatibles. Le programme qui lance ton modèle compte aussi dans l'achat.

Chez Intel, les Arc Pro B65 et B70 proposent également 32 gigas chacune. Elles méritent donc une ligne dans le comparatif. Mais leur prix français exact reste à relever. Et une promesse de TOPS ou de multi-GPU sur une fiche constructeur ne donne pas une vitesse d'écriture de Qwen sur ton bureau.

La RTX 5090 propose elle aussi 32 gigas, cette fois chez NVIDIA. Son intérêt dépend de ton budget et des logiciels que tu veux conserver. Son prix français reste à relever pour une référence réellement disponible. Je ne vais pas la déclarer rentable en divisant un prix américain par une mémoire française.

Reste la Tesla V100 de 32 gigas d'occasion. C'est séduisant sur une annonce. Sauf que la version précise change tout : une carte prévue pour un serveur ne se transforme pas automatiquement en carte de joueur. Connectique, refroidissement, pilotes, format, il faut un ensemble cohérent. Le dossier rappelle aussi les limites des anciennes générations avec les outils CUDA récents.

En fait, la carte seule peut afficher moins cher et réclamer davantage de travail autour. Si tu débutes et que tu as seulement envie de discuter avec ton IA, ce travail fait partie du coût. On le garde dans le verdict, même s'il n'apparaît pas dans la colonne euros par giga.

[VISUEL : ordinateur compact ; CPU et GPU accèdent à une même réserve. F88/F89.]

Il y a aussi la route où tu remplaces l'ordinateur. Un Ryzen AI Max+ peut employer une grande mémoire partagée avec son GPU intégré. Le mini-PC consulté existe en 64 ou 128 gigas. Et le Mac mini est proposé dans des configurations à 32 ou 64 gigas de mémoire unifiée.

Du coup, on change de comparaison. On achète un ordinateur complet, avec son processeur, son stockage et son système. Si ton PC actuel te sert déjà pour jouer et travailler, son remplacement ne se justifie pas seulement avec une division par 32.

Autre détail : la mémoire partagée sert aussi au système et aux applications. Une configuration à 32 gigas ne promet pas 32 gigas libres pour le GPU. Et avoir une grande réserve ne dit pas à quelle vitesse le modèle écrit. Pour ça, il faut une mesure sur le modèle, le moteur et la configuration concernés.

Le prix TTC de la configuration exacte reste à relever. La page du mini-PC présente plusieurs variantes et un prix par défaut. Attribuer ce prix au modèle de 128 gigas aurait l'air d'une bonne affaire. Ce serait surtout la mauvaise ligne du catalogue.

Voilà pourquoi le comparatif garde deux colonnes : le matériel à ajouter et l'ordinateur à remplacer. Si tu pars de zéro, une machine compacte peut être cohérente. Si tu as déjà une tour adaptée et une carte utile, l'ajout peut demander moins de changements. Le besoin final est le même ; le point de départ change la facture.

[GRAPHIC] [VISUEL : manuel carte mère, dimensions et connecteurs, aucune capture personnelle à produire. F60–F65.]

Regarde maintenant ce que le prix des cartes laisse de côté. Un deuxième connecteur long sur la carte mère ne signifie pas forcément une liaison aussi rapide que le premier. Dans l'exemple documenté du dossier, le second fonctionne en PCIe 3.0 avec quatre lignes et passe par le chipset. Le manuel donne cette information ; la forme du connecteur ne la donne pas.

Ensuite, il faut de la place sous cette carte. Sur une petite carte mère, le port du bas peut mettre le radiateur de la seconde carte tout contre le fond du boîtier. Donc on compare les dimensions réelles et les emplacements disponibles. Une photo avec deux cartes côte à côte ne prouve pas qu'elles rentrent dans ta tour.

L'alimentation pose la même question. Il faut la puissance, mais aussi les bons câbles et leurs connecteurs. Le dossier distingue les modèles et les prises. On ne transforme pas une prise disponible en branchement compatible à l'aide d'un adaptateur trouvé au hasard.

Et pour la vitesse, on garde les pieds au sol. Un moteur peut répartir le modèle entre les cartes. En répartition par couches, pour une seule conversation, les cartes traitent successivement leurs parties. Ajouter la mémoire rend donc certains modèles possibles sans promettre deux fois plus de tokens par seconde. Les détails du partage et des lignes PCIe arrivent dans la suite consacrée aux deux cartes.

[VISUEL : facture vendeur professionnel, calendrier de livraison et étiquette retour. F74–F79.]

Enfin, une annonce de particulier et une vente professionnelle ne t'offrent pas le même recours. En France, quand un particulier achète à un professionnel, la garantie légale de conformité couvre aussi l'occasion pendant 2 ans à partir de la délivrance. Pour l'occasion, la présomption que le défaut existait déjà dure 12 mois. Ensuite, la question de la preuve change.

Pour un achat à distance auprès d'un professionnel, le droit de rétractation donne en principe 14 jours à partir du lendemain de la réception du bien. Donc une ligne « garantie commerciale 12 mois » ne raconte pas tout. Et ces règles françaises ne deviennent pas automatiquement celles de ton pays si tu regardes depuis Abidjan, Douala ou Kinshasa. Les frais d'importation et les recours locaux doivent être vérifiés séparément.

Alors, quel choix regarder ? Si tu as déjà une carte de 16 gigas et une tour adaptée, compare d'abord le coût de la seconde carte compatible, câbles et place compris. Si tu pars de zéro et que tu veux un ensemble simple, compare aussi une seule carte de 32 gigas. Si tu veux remplacer l'ordinateur, les machines à mémoire unifiée entrent dans la course. Et si ton Qwen en 4 bits avec contexte court tient déjà correctement, garde ton argent tant que tu n'as pas identifié ce qui te manque.

Le classement du moins cher reste ouvert pour les offres sans prix actuel vérifiable. Avec les pages disponibles, on a des repères, des ruptures et des restrictions ; on n'a pas une paire miracle valable pour tout le monde. Donc ton verdict commence par trois lignes : le fichier, la conversation voulue et le PC que tu possèdes.

[CROCHET : ton avis personnel sur le compromis que tu accepterais. Facultatif, sans fait nouveau.]

La prochaine étape, c'est la deuxième carte avant l'achat : comment elle communique avec la première, ce que les ports changent, et pourquoi la mémoire supplémentaire peut te rendre service sans accélérer la réponse. Allez, salut !

## Notes hors voix

- Prix manquants : occasion, V100, Arc Pro, 5090, Mac et configuration Ryzen TTC. Aucun relevé personnel imposé ; conserver les crochets tant que non sourcé.
- Risque de rétention au calcul KV : montrer la jauge avant de nommer le cache. Aux prix : afficher stock/restriction au même instant que le total. Aux routes pro : ne pas lire un catalogue de TOPS.
- Visuels : uniquement tableaux originaux, schémas et documents cités, avec date. Aucun achat, lancement LM Studio ou enregistrement de démonstration requis.
- Comptage hors titres et balises : 1 801 mots, soit 12 min 25 s à 145 mots/minute. Les repères restent indicatifs avant montage. Pas de conclusion « le moins cher est X » avec prix manquants.
