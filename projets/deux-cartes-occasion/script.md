# 32 Go pour Qwen 27B : les prix, les routes et leurs pièges

V3 du 19/11/2026, grill-v3 appliqué ; prix relevés le 16/11, à relire avant la voix

<!-- METRICS -->
**Voix : 1590 mots · 10:57 à 145 mots/min.** Balises [VISUEL], renvois [F…] et titres non lus ; compte fait avec node. Question centrale au 72e mot (0:29). Liaisons strictes (donc, du coup, en fait, sauf que, voilà, par contre, alors, pourtant) : 36, soit 2,26 pour 100 mots. Aucun crochet.

| Partie | Début estimé |
|---|---|
| Le résultat | 0:00 |
| La question et le plan | 0:20 |
| De combien tu as vraiment besoin | 0:57 |
| Route 1 : deux cartes de 16 gigas | 2:34 |
| Route 2 : une seule carte de 32 gigas | 4:46 |
| Route 3 : changer d'ordinateur | 6:53 |
| Avant de payer : les recours | 7:58 |
| La route que je prendrais | 8:59 |
<!-- /METRICS -->

## Voix

### Le résultat

[VISUEL : deux cartes côte à côte, même fond. « ASRock Arc Pro B65 32 Go : 1799,95 € » / « Gigabyte Radeon AI PRO R9700 32 Go : 2799,95 € ». Bandeau : « LDLC, 16/11/2026, prix TTC affichés, les deux en stock ». Un « +1000 € » rouge tombe entre les deux. F85, F91, F95]

Tu peux payer 1000 euros de plus pour la même quantité de mémoire : 32 gigas sur une seule carte, chez le même marchand, le même jour. [F95] Et même avec ces 32 gigas, Qwen 27B en 4 bits, avec sa conversation la plus longue, te laisse moins d'un giga de marge. [F81]

### La question et le plan

[VISUEL : une jauge de 32 gigas qui se remplit presque jusqu'en haut ; il reste un trait fin, « ≈ 0,7 ». « Fichier 4 bits + cache 16 bits complet ». F81]

Du coup, pour faire tourner Qwen 27B chez toi, quelle route vers 32 gigas tu prends, et quel piège elle te cache ?

[VISUEL : le plan en quatre lignes qui s'écrivent avec la voix : « COMBIEN IL TE FAUT » · « 3 ROUTES, LEURS PRIX DU 16/11, LEURS PIÈGES » · « CE QUE TE PAIENT LES 1000 € » · « LA ROUTE QUE JE PRENDRAIS ».]

Aujourd'hui, on va voir combien de mémoire Qwen 27B prend vraiment, conversation comprise. Ensuite, trois routes vers 32 gigas, avec leurs prix relevés chez LDLC le 16 novembre, et le piège de chacune, celui qui n'est pas écrit sur l'étiquette. Et à la fin, ce que ces 1000 euros de plus t'achètent vraiment, et la route que je prendrais selon le PC que tu as déjà.

### De combien tu as vraiment besoin

[VISUEL : jauge de 24 gigas ; le fichier Qwen3.8-27B Q4_K_M entre dedans, avec une petite conversation par-dessus, coche verte. Étiquette : « fichier 4 bits, conversation courte (32 K) ». Section C de sources.md, conseil 10, F41]

Première réponse, et elle peut déjà t'économiser une carte : pour Qwen 27B en 4 bits, avec une conversation courte, 24 gigas suffisent. [F41, section C, conseil 10] Donc les 32, en fait, c'est pour lui laisser une longue mémoire.

[VISUEL : trois zones dans une même jauge : « le fichier » (fixe), « la conversation » (qui grossit pendant qu'on parle), « le reste du moteur ». F80]

Parce que voilà le truc : pendant que tu discutes, le modèle garde des notes sur tout ce qui a été dit. Ton fichier, lui, ne bouge pas. Sauf que cette réserve-là grossit à chaque message.

[VISUEL : trois barres calculées : 2 / 8 / 16 Gio, pour 32 768, 131 072 et 262 144 tokens. « Calcul à partir de la configuration officielle de Qwen3.8-27B, cache en 16 bits ». F80]

Et on peut la calculer, à partir de la configuration officielle du modèle. Avec un cache en 16 bits, c'est environ 2 gigas pour 32 000 tokens, 8 pour 128 000, et 16 pour la fenêtre complète de 262 000. [F80]

[VISUEL : l'addition qui s'empile dans la jauge de 32 : « 15,3 Gio (16,46 Go affichés sur Hugging Face) + 16 (conversation complète) = 31,3 Gio ». Il reste un trait de 0,7. F81]

Alors fais l'addition avec moi. Le fichier 4 bits, c'est 16 gigas et demi sur Hugging Face. Mais compté comme ta carte compte, c'est un peu plus de 15. Tu ajoutes 16 pour la conversation complète. Ça fait 31,3. Sur une carte de 32. [F81] Et ça, c'est avant les tampons et tout le reste du moteur. Bon, la boîte dit 32 gigas, mais ta marge, elle est déjà partie.

Du coup, avec 32 gigas, le contexte complet, il faut aller le chercher : en compressant le cache, ou en raccourcissant un peu la conversation. [F81]

Et si t'as qu'une carte de 8 gigas, on a vu lundi dernier comment Qwen 27B y tourne quand même, juste en changeant de fichier. Là, on parle de ceux qui veulent la place.

### Route 1 : deux cartes de 16 gigas

[VISUEL : tableau, en gros : « 2 × Intel Arc A770 16 Go : 2 × 459,95 € = 919,90 € » avec un tampon « RUPTURE EN LIGNE LE 16/11 » ; « 2 × ASUS Dual RTX 5060 Ti OC 16 Go : 2 × 1079,95 € = 2159,90 € » avec « 1 PAR CLIENT ». LDLC, 16/11. F86, F87]

Première route, la plus tentante : deux cartes de 16 gigas, et hop, 32. La moins chère du relevé, c'est l'Intel Arc A770 : 460 euros chez LDLC le 16 novembre. Donc deux, ça fait 920 euros. Moins de 1000 euros pour 32 gigas ! Sauf que… ce jour-là, la page affichait une rupture en ligne. [F87] Bref, ta paire à 920 euros, le 16 novembre, tu ne pouvais pas la commander.

Côté NVIDIA, la RTX 5060 Ti de 16 gigas d'ASUS est bien en stock : 1080 euros. Ça ferait 2160 la paire. Sauf qu'il y a une petite ligne sous le prix : limitée à une par client. [F86] En gros, le boss de fin, c'est pas le prix, c'est la règle du magasin.

[VISUEL : « 2 × RTX 3090 : 2 × 24 = 48 Go », « prix actuel non établi » ; en petit, « 2 × RTX 3060 = 24 Go : sous le palier ». F90]

Et deux RTX 3090 ? Ça fait 48, mais aucune offre d'occasion vérifiable ce jour-là pour te donner un vrai prix. [F90]

[VISUEL : schéma de ma carte mère, d'après son manuel (Gigabyte B850M AORUS ELITE WIFI6E ICE) : slot du haut « PCIe 5.0 x16, processeur », slot du bas « PCIe 3.0 x4, chipset », en dernière position. F60]

Maintenant, le vrai piège de cette route, c'est ta tour. Prends la mienne : une carte mère micro-ATX, comme beaucoup d'autres. D'après son manuel, le deuxième slot a la même longueur que le premier. Pourtant, il n'a que 4 lignes en PCIe 3.0, et il passe par le chipset. [F60] Et en plus, il est tout en bas. Du coup, une carte de 2 slots dedans dépasse sous la carte mère, et il te faut un boîtier à 5 emplacements. [F60]

[VISUEL : panneau de mon alimentation Corsair RM1000e ; une seule prise 12V-2x6 entourée ; « avec la 5080 branchée : peut-être 2 × 8 broches restantes ». F61]

Ensuite, l'alimentation. La mienne fait 1000 watts. Sauf qu'avec ma RTX 5080 branchée, il ne me resterait peut-être que 2 prises 8 broches. [F61] Donc avant d'acheter la deuxième carte, tu regardes ton boîtier, et tu comptes tes câbles.

[VISUEL : deux bureaux, un modèle coupé en deux tranches de couches ; la flèche de travail passe de l'un à l'autre, jamais les deux en même temps. « llama.cpp, --split-mode layer (défaut) ». F20, F33]

Et le dernier piège, c'est la vitesse. Par défaut, llama.cpp coupe le modèle en tranches de couches, une tranche par carte. [F20] Et pour une seule conversation, elles travaillent chacune leur tour. En fait, la mémoire s'additionne, mais la vitesse, elle, ne double pas. [F33]

Bref, deux cartes, c'est de la place, pas de la vitesse. Si cette vidéo t'a évité un mauvais achat, abonne-toi.

### Route 2 : une seule carte de 32 gigas

[VISUEL : quatre cartes alignées par prix, avec leur statut : « Arc Pro B65 : 1799,95 €, en stock » ; « Arc Pro B70 : 2299,95 €, en stock » ; « Radeon AI PRO R9700 ASRock : 2349,95 €, + de 15 jours » ; « Radeon AI PRO R9700 Gigabyte : 2799,95 €, en stock ». LDLC, 16/11, offres relevées (pas tout le marché). F85, F91, F92, F93]

Deuxième route : une seule carte de 32 gigas. Plus de deuxième slot, plus de câbles en double, et là, d'un coup, le PC redevient simple. Et c'est là qu'on retrouve nos 1000 euros du début.

Chez LDLC, toujours le 16 novembre, la moins chère en stock de mon relevé, c'est l'Intel Arc Pro B65 d'ASRock : 1800 euros, à 5 centimes près. [F91] Sa grande sœur, la B70, est à 2300. [F92] Côté AMD, la Radeon AI PRO R9700 de Gigabyte est à 2800, en stock. [F85]

[VISUEL : la même jauge « 32 GO » sur la B65 et la R9700 ; « +1000 € = ? » ; puis la couverture du guide AMD « Radeon AI PRO : ROCm et PyTorch » qui s'ajoute côté R9700. F83, F95]

Donc 32 gigas des deux côtés, et jusqu'à 1000 euros d'écart. [F95] Alors, ces 1000 euros, ils t'achètent quoi ? Pas un giga de plus, en tout cas. Et la vitesse, le prix ne te la dit pas. Ce que la R9700 a en plus sur le papier, c'est un guide officiel d'AMD pour y faire tourner ses outils d'IA. [F83] Sauf que, même là, 32 gigas et un guide ne prouvent pas que chaque moteur la prend en charge. [F83] Du coup, voilà le vrai piège de cette route : avant de comparer les prix, tu vérifies que ton logiciel gère la carte.

[VISUEL : « ASUS TUF RTX 5090 32 Go : 9399,95 € — 1 en stock », LDLC, 16/11. F96]

Et chez NVIDIA ? La RTX 5090 a aussi 32 gigas. Sauf que la TUF d'ASUS s'affichait à 9400 euros, avec un seul exemplaire en stock. [F96] Ouais. Pour ce prix-là, on change carrément de catégorie.

[VISUEL : une Tesla V100 32 Go de serveur, sans ventilateur, avec trois étiquettes : « ni ventilateur ni sortie vidéo », « pilote 580 = dernière branche », « CUDA 13 : plus de compilation ». F70, F90, conseil 4]

Reste la Tesla V100 de 32 gigas d'occasion, la carte de serveur qui fait des centaines de milliers de vues en anglais. [vidIQ, 24/10] Pas d'offre vérifiable dans ce relevé, donc pas de prix. [F90] Par contre, son piège, on le connaît : NVIDIA a fait du pilote 580 la dernière branche qui la gère, et CUDA 13 ne compile plus pour elle. [F70] En plus, comme les autres cartes de serveur, elle n'a ni ventilateur ni sortie vidéo : tout est à refaire autour. [conseil 4] En fait, elle peut paraître pas chère, et te coûter tout un week-end.

### Route 3 : changer d'ordinateur

[VISUEL : « Mac mini M6 32 Go / 512 Go : 1709 € — délai + de 15 jours », LDLC, 16/11 ; processeur et puce graphique puisent dans la même réserve de 32 Go ; une part grisée « système et applis ». F89, F94]

Troisième route, et c'est là que ça devient bizarre. Le Mac mini M6 avec 32 gigas de mémoire unifiée et 512 de stockage est affiché 1709 euros chez LDLC le 16 novembre. [F94] Donc un ordinateur complet coûte moins cher que la carte de 32 gigas la moins chère du relevé.

Sauf que, déjà, le délai dépasse 15 jours. [F94] Et surtout, cette mémoire, elle est partagée : le système et tes applis se servent dedans. [F89]

[VISUEL : mini-PC GMKtec EVO-X2, Ryzen AI Max+ 395, deux versions « 64 Go » et « 128 Go » ; « 1999,99 € affichés (64 Go + 1 To), TVA non précisée ». F88]

Côté PC, il y a les mini-PC Ryzen AI Max+, avec 64 ou même 128 gigas de mémoire partagée. Celui que j'ai regardé affiche presque 2000 euros en 64 gigas, sauf que sa page ne dit pas clairement si la TVA est dedans. [F88] Et là encore, la mémoire est fixe : tu choisis à l'achat, et c'est pour toujours. [F88]

Du coup, le piège de cette route, c'est la facture : tu remplaces ton PC entier, celui qui te sert aussi à jouer et à bosser.

### Avant de payer : les recours

[VISUEL : deux colonnes : « vendeur pro, neuf ou occasion : 2 ans de garantie légale ; défaut présumé 2 ans (neuf), 12 mois (occasion) ; 14 jours de rétractation à distance » / « particulier : vices cachés seulement, à prouver ». F74, F75, F76, F79]

Et avant de payer, un dernier piège, qui n'est pas technique. En France, chez un vendeur professionnel, neuf ou d'occasion, tu as 2 ans de garantie légale, et il ne peut pas les réduire. [F74, F75] Le défaut est présumé exister dès la vente pendant ces 2 ans pour du neuf, et 12 mois pour de l'occasion. [F75] Et pour un achat à distance, tu as 14 jours après la réception pour te rétracter. [F79] Donc ces 14 jours, c'est ta fenêtre pour tester la carte.

Par contre, entre particuliers, il te reste seulement les vices cachés, et c'est à toi de les prouver. [F76]

[VISUEL : carte de l'Afrique de l'Ouest et centrale, Abidjan, Dakar, Douala, Kinshasa ; deux étiquettes : « valable partout : le calcul de la mémoire, les slots, l'alimentation » / « valable en France seulement : ces prix TTC, ces garanties ».]

Et si tu regardes depuis Abidjan, Dakar ou Kinshasa : ces prix sont des prix français, et ces garanties, c'est le droit français. [F74, F79] Donc chez toi, renseigne-toi sur le recours du vendeur avant de payer. Par contre, l'addition de la mémoire, les slots et l'alimentation, ça, c'est valable partout. [F60, F61, F81]

### La route que je prendrais

[VISUEL : trois profils, chacun avec sa route et son prix du 16/11 : « tu as déjà une 16 Go NVIDIA → + 1 × 5060 Ti 16 Go : 1079,95 € » ; « tu pars de zéro → Arc Pro B65 : 1799,95 € » ; « tu remplaces tout → Mac mini M6 32 Go : 1709 €, ou mini-PC Ryzen AI Max+ 64 Go : 1999,99 € affichés ». F85, F86, F88, F91, F94]

Alors, quelle route ? Ça dépend de ce que tu as déjà.

Si tu as déjà une carte NVIDIA de 16 gigas, et une tour qui accueille une deuxième carte, c'est le seul cas où je prendrais une paire : la moitié est déjà payée. Regarde la 5060 Ti de 16 gigas, à 1080 euros. [F86] Et du coup, la limite d'une par client ne te gêne plus, puisque t'en achètes qu'une. Mais vérifie d'abord ton slot, ton boîtier et tes câbles. [F60, F61]

Si tu pars de zéro, moi, je ne commencerais pas par une paire. Sur le papier, c'est la moins chère, mais en vrai, c'est elle qui a le plus de pièges. [F20, F33, F60, F61, F86, F87] Donc je prendrais la B65, à 1800 euros : la moins chère des offres en stock du relevé, avec la même quantité de mémoire que la R9700 à 2800. [F85, F91] Sauf que, avant de cliquer, tu vérifies que ton logiciel la gère. S'il ne la gère pas, là, les 1000 euros de la R9700 et son guide officiel peuvent avoir un sens. [F83, F95]

[VISUEL : retour de la jauge du début, 31,3 sur 32, posée sur le Mac mini ; la part « système » la fait déborder. Puis la jauge de 64 du mini-PC, avec de la place. F81, F88, F89]

Et si tu veux remplacer tout l'ordinateur, le Mac mini à 1709 euros entre dans la course. Par contre, souviens-toi de l'addition du début : 31,3 gigas pour la conversation complète. Sur un Mac de 32 gigas, dont le système prend sa part, en cache 16 bits, ça ne rentre pas : tu compresses le cache, ou tu raccourcis. [F81, F89] Et si c'est vraiment la conversation complète que tu veux, la seule route chiffrée de mon relevé qui dépasse 32 gigas, c'est le mini-PC Ryzen AI Max+ en 64. [F88]

Et en fait, si tu as déjà 24 gigas et qu'une conversation courte te suffit, garde ton argent. [section C] La meilleure carte, parfois, c'est celle que tu n'achètes pas.

Allez, salut !

## Faits utilisés

F20, F33, F41, F60, F61, F70, F74, F75, F76, F79, F80, F81, F83, F85, F86, F87, F88, F89, F90, F91, F92, F93, F94, F95, F96 ; section C et conseils 4 et 10 de sources.md ; vues de la vidéo V100 (vidIQ, 24/10). Prix du 16/11 chez LDLC, exacts dans les [VISUEL], arrondis dans la voix (sauf les 1000 € du hook et les 1709 € du Mac).

Écartés faute de source ou de fiabilité : vitesses publiées F28, F29, F31, F32 (marquées ⚠️) ; prix d'occasion d'octobre F1 à F16 (pas des prix du 16/11) ; prix actuels de la V100, des paires de 3090 et de Radeon 16 Go d'occasion ; prix TTC certifié du Ryzen AI Max+ (seul le 1999,99 € affiché, TVA non claire, est dit) ; coûts d'import vers l'Afrique.
