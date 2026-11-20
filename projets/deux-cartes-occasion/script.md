# 32 Go pour Qwen 27B : les prix, les routes et leurs pièges

V4 du 20/11/2026 : hook de l'auteur, meilleurs prix du 20/11 tous marchands confondus (recherche/prix-20-11.md), grill-v4 appliqué ; à relire avant la voix (Black Friday le 27/11)

<!-- METRICS -->
**Voix : 1687 mots au téléprompteur (wc -w) · environ 11:38 à 145 mots/min, 7:14 à 233.** Balises [VISUEL], renvois [F…] et titres non lus. Liaisons strictes (donc, du coup, en fait, sauf que, bref, voilà, par contre, alors, pourtant) : 34, soit 2.02 pour 100 mots. Aucun crochet au téléprompteur.

| Partie | Ordre |
|---|---|
| Le résultat | 1 |
| La question et le plan | 2 |
| De combien tu as vraiment besoin | 3 |
| Route 1 : deux cartes de 16 gigas | 4 |
| Route 2 : une seule carte de 32 gigas | 5 |
| Route 3 : changer d'ordinateur | 6 |
| Avant de payer : les recours | 7 |
| La route que je prendrais | 8 |
<!-- /METRICS -->

## Voix

### Le résultat

[VISUEL : page Hugging Face de Qwen/Qwen3.8-27B, « Downloads last month 6,454,419 » surligné, capture du 20/11. Puis une jauge « 32 GO DE VRAM » qui se change en lingot d'or ; deux étiquettes de prix : « 2799,95 € (R9700, LDLC) » et « dès 1599,98 € la paire (2 × 5060 Ti 16 Go, Amazon) ». « Meilleurs prix relevés le 20/11/2026, TTC affichés ». F120, F100, F118]

Qwen 27B, c'est l'un des meilleurs modèles que tu peux faire tourner sur ta machine : plus de 6 millions de téléchargements en un mois. Sauf que si tu veux faire autre chose que lui demander la météo, il lui faut de la place pour ta conversation. Pour être à l'aise : 32 gigas de VRAM. Et en 2026, la VRAM, c'est de l'or. Ces 32 gigas, tu peux les payer 2800 euros… ou, si t'es malin, beaucoup moins. [F120, F81, F100, F118]

### La question et le plan

[VISUEL : une jauge de 32 gigas qui se remplit presque jusqu'en haut ; il reste un trait fin, « ≈ 0,6 ». « Fichier 4 bits + cache 16 bits complet ». F109]

Du coup, quelle route vers 32 gigas tu prends, et quel piège elle te cache ?

[VISUEL : le plan en quatre lignes qui s'écrivent avec la voix : « COMBIEN IL TE FAUT » · « 3 ROUTES, MEILLEURS PRIX DU 20/11, LEURS PIÈGES » · « MÊME CARTE : +400 € SELON LE SITE » · « LA ROUTE QUE JE PRENDRAIS ».]

Dans cette vidéo, on va voir combien de mémoire Qwen 27B prend vraiment. Ensuite, 3 routes vers 32 gigas, avec les meilleurs prix relevés le 20 novembre, et le piège de chacune. La même carte, 400 euros plus chère selon le site où tu cliques, et un ordinateur entier moins cher qu'une carte de 32 gigas en stock. Et à la fin, la route que je prendrais selon ton PC. [F112, F100, F104, F97]

### De combien tu as vraiment besoin

[VISUEL : jauge de 24 gigas ; le fichier Qwen3.8-27B-UD-Q4_K_M entre dedans, avec une petite conversation par-dessus, coche verte. Étiquette : « fichier 4 bits, conversation courte (32 K) ». Section C de sources.md, conseil 10, F41, F109]

Première réponse, et elle peut déjà t'économiser une carte : pour Qwen 27B en 4 bits, avec une conversation courte, 24 gigas suffisent. Donc les 32, en fait, c'est pour lui laisser une longue mémoire. [F41, F109, section C, conseil 10]

[VISUEL : trois zones dans une même jauge : « le fichier » (fixe), « la conversation » (qui grossit pendant qu'on parle), « le reste du moteur ». F80]

Parce que pendant que tu discutes, le modèle garde des notes sur tout ce qui a été dit. Ton fichier, lui, ne bouge pas. Mais ces notes-là, elles grossissent à chaque message.

[VISUEL : trois barres calculées : 2 / 8 / 16 Gio, pour 32 768, 131 072 et 262 144 tokens. « Calcul à partir de la configuration officielle de Qwen3.8-27B, cache en 16 bits ». F80]

Et on peut les calculer, à partir de la configuration officielle du modèle. Avec un cache en 16 bits, c'est environ 2 gigas pour 32 000 tokens, 8 pour 128 000, et 16 pour la fenêtre complète de 262 000. [F80]

[VISUEL : l'addition qui s'empile dans la jauge de 32 : « 15,4 Gio (16,56 Go sur Hugging Face) + 16 (conversation complète) = 31,4 Gio ». Il reste un trait de 0,6. Vérifier le chiffre affiché par la page avant la capture. F109]

Alors fais l'addition avec moi. Le fichier 4 bits, c'est 16 gigas et demi sur Hugging Face. Mais compté comme ta carte compte, c'est un peu plus de 15. Tu ajoutes 16 pour la conversation complète. Ça fait 31,4. Sur une carte de 32. Et ça, c'est avant les tampons et tout le reste du moteur. Bon, la boîte dit 32 gigas, mais ta marge, elle est déjà partie. [F109]

Du coup, avec 32 gigas, le contexte complet, il faut aller le chercher : en compressant le cache, ou en raccourcissant un peu la conversation. [F81, F109]

Et si t'as qu'une carte de 8 gigas, on a vu dans une vidéo précédente comment Qwen 27B y tourne quand même, juste en changeant de fichier. Là, on parle de ceux qui veulent la place.

### Route 1 : deux cartes de 16 gigas

[VISUEL : tableau, en gros : « 2 × ASUS Dual RTX 5060 Ti OC 16 Go : 2 × 799,99 € = 1599,98 €, Amazon, en stock » ; « même carte chez LDLC : 1079,95 €, 1 PAR CLIENT » ; flèche « +280 € ». 20/11. F101, F117, F118]

Première route, la plus tentante : 2 cartes de 16 gigas, et hop, 32. Prends la RTX 5060 Ti de 16 gigas, la Dual d'ASUS. Le 20 novembre, sur Amazon, elle était à 800 euros, en stock. Donc 1600 la paire, sans limite affichée sur la page. Chez LDLC, le même modèle était à 1080 euros, avec une petite ligne au-dessus du bouton panier : limitée à une par client. 280 euros de plus pour le même modèle, le même jour. En gros, le boss de fin, c'est le site où tu cliques. [F117, F101, F118]

[VISUEL : « 2 × ASUS Prime Radeon RX 9060 XT 16 Go : 2 × 699,99 € = 1399,98 €, Amazon » avec « LIVRAISON 3-5 JANVIER » ; « Intel Arc A770 16 Go : 459,95 €, LDLC » avec « RUPTURE EN LIGNE ». 20/11. F102, F107, F108]

Et chez AMD ? La Radeon RX 9060 XT de 16 gigas d'ASUS était à 700 euros sur Amazon, donc 1400 la paire. Moins cher, mais ce jour-là, la livraison était annoncée du 3 au 5 janvier. Bref : Noël sans cartes. L'Intel Arc A770 ? 460 euros chez LDLC, mais en rupture en ligne. [F107, F108, F102]

[VISUEL : « RTX 5060 Ti 16 Go d'occasion : autour de 600 à 670 €, leboncoin, 20/11 (annonces de particuliers) ». F119]

Et en occasion, le 20 novembre, une 5060 Ti de 16 gigas tournait autour de 600 à 670 euros sur leboncoin. Entre particuliers, par contre : garde ça en tête pour tout à l'heure. [F119]

[VISUEL : schéma de ma carte mère, d'après son manuel (Gigabyte B850M AORUS ELITE WIFI6E ICE) : slot du haut « PCIe 5.0 x16, processeur », slot du bas « PCIe 3.0 x4, chipset », en dernière position. Puis « 5060 Ti Dual : 2,5 slots, 50 mm » et « 9060 XT Prime : 2,5 slots ». F60, F110]

Maintenant, le vrai piège de cette route, c'est ta tour. Prends la mienne : une carte mère micro-ATX, comme beaucoup d'autres. D'après son manuel, le deuxième slot a la même longueur que le premier. Pourtant, il n'a que 4 lignes en PCIe 3.0, et il passe par le chipset. Et en plus, il est tout en bas. Du coup, une carte de 2 slots dedans dépasse sous la carte mère, et il te faut un boîtier à 5 emplacements. Et les 5060 Ti et 9060 XT du relevé sont plus épaisses : 2 slots et demi, donc mesure la place sous ta carte mère. [F60, F110]

[VISUEL : panneau de mon alimentation Corsair RM1000e ; une seule prise 12V-2x6 entourée ; « avec la 5080 branchée : peut-être 2 × 8 broches restantes ». F61]

Ensuite, l'alimentation. La mienne fait 1000 watts. Sauf qu'avec ma RTX 5080 branchée, il ne me resterait peut-être que 2 prises 8 broches. Donc avant d'acheter la deuxième carte, tu regardes ton boîtier, et tu comptes tes câbles. [F61]

[VISUEL : deux bureaux, un modèle coupé en deux tranches de couches ; la flèche de travail passe de l'un à l'autre, jamais les deux en même temps. « llama.cpp, --split-mode layer (défaut) ». F20, F33]

Et le dernier piège, c'est la vitesse. Par défaut, llama.cpp coupe le modèle en tranches de couches, une tranche par carte. Et pour une seule conversation, elles travaillent chacune leur tour. En fait, la mémoire s'additionne, mais la vitesse, elle, ne double pas. [F20, F33]

Bref, 2 cartes, c'est de la place, pas de la vitesse. Si cette vidéo t'a évité un mauvais achat, abonne-toi.

### Route 2 : une seule carte de 32 gigas

[VISUEL : cartes alignées par prix, avec marchand et statut le 20/11 : « Arc Pro B65 ASRock : 1899,95 €, LDLC, en stock » ; « Arc Pro B65 (GUNNIR, vendeur tiers) : 1483 €, Amazon, livrée le 14/12 » ; « Arc Pro B70 ASUS : 2016 €, Amazon, en stock » ; « R9700 Gigabyte : 2399,99 €, Amazon, en stock » ; « même R9700 : 2799,95 €, LDLC ». Offres relevées, pas tout le marché. F97, F100, F112, F113, F114, F115]

Deuxième route : une seule carte de 32 gigas. Plus de deuxième slot, et d'un coup, le PC redevient simple.

Le 20 novembre, la moins chère en stock de mon relevé, c'était l'Intel Arc Pro B65 d'ASRock : 1900 euros chez LDLC. Sur Amazon, des B65 de vendeurs tiers descendaient à 1483 euros, mais livrées en décembre. Sa grande sœur, la B70 d'ASUS, était à 2016 euros sur Amazon, en stock. Côté AMD, la Radeon AI PRO R9700 de Gigabyte : 2400 euros sur Amazon. Et chez LDLC, exactement la même référence : 2800. [F97, F114, F115, F113, F112, F100]

[VISUEL : la même boîte R9700 (GV-R9700AI TOP-32GD) deux fois, « Amazon 2399,99 € » / « LDLC 2799,95 € », « +400 € = ? » ; puis la couverture du guide AMD « Radeon AI PRO : ROCm et PyTorch ». F83, F118]

Alors, ces 400 euros de plus, ils t'achètent quoi ? Rien. C'est la même carte. Donc le vrai match, c'est Intel à 1900 contre AMD à 2400. Et là, 500 euros de plus ne t'achètent pas un giga de plus. Côté AMD, j'ai trouvé un guide officiel pour faire tourner ses outils d'IA sur la R9700. Mais 32 gigas et un guide ne prouvent pas que chaque moteur la prend en charge. Du coup, voilà le vrai piège de cette route : avant de comparer les prix, tu vérifies que ton logiciel gère la carte. [F118, F83]

[VISUEL : « RTX 5090 32 Go : Inno3D X3, 6975,27 €, Amazon, vendeur tiers, livrée du 23 au 28/12 » / « ASUS TUF : 9399,95 €, LDLC, rupture ». 20/11. F103, F116]

Et chez NVIDIA ? La RTX 5090 a aussi 32 gigas. Sur Amazon, elle partait à presque 7000 euros, chez un vendeur tiers, livrée fin décembre. Et chez LDLC, 9400 euros, en rupture. Pour ce prix-là, on change carrément de catégorie. [F116, F103]

[VISUEL : une Tesla V100 32 Go de serveur, sans ventilateur, avec trois étiquettes : « ni ventilateur ni sortie vidéo », « pilote 580 = dernière branche », « CUDA 13 : plus de compilation ». F70, F90, conseil 4]

Reste la Tesla V100 de 32 gigas d'occasion. Pas d'offre vérifiable dans ce relevé, donc pas de prix. Par contre, son piège, on le connaît : NVIDIA a fait du pilote 580 la dernière branche qui la gère, et CUDA 13 ne compile plus pour elle. En plus, comme les autres cartes de serveur, elle n'a ni ventilateur ni sortie vidéo : tout est à refaire autour. En fait, elle peut paraître pas chère, et te coûter tout un week-end. [F90, F70, conseil 4]

### Route 3 : changer d'ordinateur

[VISUEL : « Mac mini M6 32 Go / 512 Go : 1709 €, LDLC, délai + de 15 jours » ; en petit : « Amazon : pas de version 32 Go le 20/11 » ; processeur et puce graphique puisent dans la même réserve de 32 Go ; une part grisée « système et applis ». F89, F104, F122]

Troisième route : changer carrément d'ordinateur. Le Mac mini M6 avec 32 gigas de mémoire unifiée et 512 de stockage était affiché 1709 euros chez LDLC le 20 novembre. Donc un ordinateur complet coûtait moins cher que n'importe quelle carte de 32 gigas en stock de mon relevé. [F104, F122, F97]

Premier hic : lui, il n'était pas en stock : plus de 15 jours. Et en acceptant d'attendre, une B65 de vendeur tiers descendait à 1483. Et surtout, cette mémoire, elle est partagée : le système et tes applis se servent dedans. [F104, F89]

[VISUEL : mini-PC GMKtec EVO-X2, Ryzen AI Max+ 395, versions « 64 Go » et « 128 Go » ; « 2029,99 € affichés (64 Go + 1 To), précommande, code de −80 € affiché à part, inclus ou non : pas clair ; TVA non précisée ». F88, F105]

Côté PC, il y a les mini-PC Ryzen AI Max+, avec 64 ou même 128 gigas de mémoire partagée. Celui que j'ai regardé affichait autour de 2000 euros en 64 gigas, en précommande. Seulement, sa page ne dit pas clairement si la TVA est dedans. Et sa mémoire est fixe, pour toujours. [F105, F88]

Du coup, le piège de cette route, c'est la facture : tu remplaces ton PC entier.

### Avant de payer : les recours

[VISUEL : deux colonnes : « vendeur pro, neuf ou occasion : 2 ans de garantie légale ; défaut présumé 2 ans (neuf), 12 mois (occasion) ; 14 jours de rétractation à distance » / « particulier (leboncoin) : vices cachés seulement, à prouver ». F74, F75, F76, F79]

Et avant de payer, un dernier piège, qui n'est pas technique. En France, chez un vendeur professionnel, neuf ou d'occasion, tu as 2 ans de garantie légale, et il ne peut pas les réduire. Le défaut est présumé exister dès la vente pendant ces 2 ans pour du neuf, et 12 mois pour de l'occasion. Et pour un achat à distance, tu as 14 jours après la réception pour te rétracter. Donc ces 14 jours, c'est ta fenêtre pour tester la carte. [F74, F75, F79]

Par contre, entre particuliers, comme sur leboncoin, pas de rétractation, pas de garantie légale : il te reste seulement les vices cachés, et c'est à toi de les prouver. Donc ta 5060 Ti d'occasion, tu la vois tourner avant de payer. [F76, F119]

[VISUEL : carte de l'Afrique de l'Ouest et centrale, Abidjan, Dakar, Douala, Kinshasa ; deux étiquettes : « valable partout : le calcul de la mémoire, les slots, l'alimentation » / « valable en France seulement : ces prix TTC, ces garanties ».]

Et si tu regardes depuis Abidjan, Dakar ou Kinshasa : ces prix sont des prix français, et ces garanties, c'est le droit français. Donc chez toi, renseigne-toi sur le recours du vendeur avant de payer. Par contre, l'addition de la mémoire, les slots et l'alimentation, ça, c'est valable partout. [F74, F79, F60, F61, F81]

### La route que je prendrais

[VISUEL : cinq profils, chacun avec sa route et son prix du 20/11 : « déjà une 16 Go NVIDIA → + 1 × 5060 Ti 16 Go : 799,99 € (Amazon) ou ≈ 600-670 € d'occasion » ; « pas encore de carte, tour à 2 slots → 2 × 5060 Ti : 1599,98 € (Amazon) » ; « une seule carte → Arc Pro B65 : 1899,95 € (LDLC), en stock, prise 12V-2x6 ; sur Amazon : Arc Pro B70, 2016 € ; si ton logiciel ne gère pas Intel : R9700, 2399,99 € (Amazon) » ; « tout remplacer → Mac mini M6 32 Go : 1709 € (LDLC) ou mini-PC 64 Go ≈ 2030 € en précommande » ; « déjà 24 Go → garde ton argent ». F97, F101, F104, F105, F111, F112, F113, F117, F118, F119]

Alors, quelle route ? Ça dépend de ce que tu as déjà. Et les prix, c'est ceux du 20 novembre.

Si t'as déjà une NVIDIA de 16 gigas, et la place pour une autre, ajoute une 5060 Ti de 16 gigas : 800 euros neuve sur Amazon, ou autour de 600 à 670 d'occasion. La moitié de tes 32 gigas est déjà payée. [F117, F119, F101]

Si t'as pas encore de carte, et que ta tour en accepte 2, la paire de 5060 Ti à 1600 euros était le chemin en stock le moins cher vers 32 gigas. Avec tous les pièges de la route : la place, les câbles, et une vitesse qui ne double pas. La paire de 9060 XT coûtait moins, mais arrivait en janvier. [F118, F108, F20, F33, F60, F61, F110]

Pour une seule carte, je prendrais la moins chère en stock : la B65, à 1900 euros chez LDLC. Regarde juste sa prise d'alimentation, une 12V-2x6 : il te faut ce câble, ou un adaptateur. Si tu préfères Amazon, sa grande sœur, la B70, était à 2016, en stock. Et dans tous les cas, tu vérifies que ton logiciel gère la carte. S'il ne gère pas Intel, regarde la R9700 de Gigabyte : 2400 euros sur Amazon, pas 2800. [F113, F97, F114, F115, F83, F112, F100]

[VISUEL : retour de la jauge du début, 31,4 sur 32, posée sur le Mac mini ; la part « système » la fait déborder. Puis la jauge de 64 du mini-PC, avec de la place. F81, F88, F89, F105, F109]

Si tu veux remplacer tout l'ordinateur, le Mac mini à 1709 euros entre dans la course. Par contre, souviens-toi de l'addition du début : 31,4 gigas pour la conversation complète. Sur un Mac de 32 gigas, dont le système prend sa part, en cache 16 bits, ça ne rentre pas : tu compresses le cache, ou tu raccourcis. Et si c'est vraiment la conversation complète que tu veux, la seule route chiffrée de mon relevé qui dépasse 32 gigas, c'est le mini-PC Ryzen AI Max+ en 64, autour de 2000 euros. [F104, F109, F89, F88, F105]

Et en fait, si tu as déjà 24 gigas et qu'une conversation courte te suffit, garde ton argent. La meilleure carte, parfois, c'est celle que tu n'achètes pas. [section C]

Allez, salut !

## Faits utilisés

F20, F33, F41, F60, F61, F70, F74, F75, F76, F79, F80, F81, F83, F88, F89, F90, F97, F100 à F105, F107 à F122 ; section C et conseils 4 et 10 de sources.md. Meilleurs prix du 20/11, marchand nommé (LDLC, Amazon, GMKtec, leboncoin), exacts dans les [VISUEL], arrondis dans la voix. Taille du fichier 4 bits : F109 (remise en ligne du 11/11), qui remplace F41 et F81 pour la voix.

Écartés : vitesses publiées F28, F29, F31, F32 (⚠️) ; prix d'octobre F1 à F16 ; relevé du 16/11 (F85 à F96) ; écart de 900 € « même marchand » (F106, plus le message principal) ; B70 et R9700 ASRock de LDLC (F98, F99), A770 à 826,99 € sur Amazon (résultat de recherche) ; prix actuels de la V100 et des paires de 3090 ; prix des cartes relevés par l'auteur sans marchand ; gpuprix.com ; « le plus téléchargé », « petit frère Flash-Next », « tout type de modèle » (faux, voir recherche/prix-20-11.md) ; coûts d'import vers l'Afrique.
