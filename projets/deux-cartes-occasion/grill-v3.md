# Grill de la V3 : « 32 Go pour Qwen 27B : les prix, les routes et leurs pièges » (19/11/2026)

> Critiqué : [`script.md`](script.md) (V3 du 19/11, prix du 16/11). Comparé à [`grill-v1.md`](grill-v1.md) (6,5/10). Seule source de chiffres : [`sources.md`](sources.md) (F1…F96). Méthode : skill `youtube-script-grill`, mode B, **variante storytelling** (test des 30 secondes, onze axes) ; règles de `.claude/rules/script.md`.
>
> **Débit** : 1 601 mots dits (compte par espaces, sans titres, [VISUEL] ni [F…] ; l'en-tête du script en annonce 1 571). À 145 mots/min : ≈ 11 min. À ton débit réel une fois monté (≈ 233 mots/min, mesuré dans `../meme-carte-plus-rapide/grill-v3.md`) : **≈ 6 min 50**. Les deux temps sont donnés ci-dessous (le second entre parenthèses).
>
> **Hors script, à noter** : `calendrier.md` et `README.md` décrivent encore une autre V3 (« Script (18/11) : V3 sur ton angle des 600 €… 1 375 mots ; prix relevés le 18/11 »). Le script, lui, est du 19/11, sans angle des 600 €, avec des prix du 16/11. Je n'ai rien modifié : à remettre d'accord.

## 1. Verdict

**V3 : 7/10. Avec les 2 corrections bloquantes et les problèmes 3 à 5 : 8,5/10.**

Le saut depuis la V1 est net. L'ouverture montre un résultat (+1000 € pour la même mémoire), la question tombe à 28 s (17 s), le plan est concret, et la première partie commence par une réponse (« 24 gigas suffisent »). Les liaisons passent de 1,11 à plus de 2 pour 100 mots. Et chaque route a enfin son prix et son piège.

Deux phrases disent plus que les sources : la rupture de l'A770 transposée au soir de la sortie (« ce soir »), et la B65 présentée comme « la moins chère en stock » de LDLC entier. Le plus gros défaut de récit : **les deux promesses du hook ne sont jamais récoltées**. On ne sait toujours pas, à la fin, ce que les 1000 € de plus achètent. Et la marge de « moins d'un giga » disparaît du verdict, alors qu'elle condamne le Mac mini 32 Go pour la conversation complète et qu'une seule route du relevé la règle (le mini-PC en 64). Le verdict est plus net qu'en V1, mais il hésite encore : « une seule carte de 32 gigas », sans dire laquelle, et une paire conseillée juste avant « je ne commencerais pas par une paire ».

### Les onze axes

| Axe | /10 | En une phrase |
|---|---:|---|
| 1. Promesse | 7 | Prix, routes, pièges : tenu. Mais le « +1000 € » du hook n'a pas de réponse (problème 3). |
| 2. Alignement | 9 | « La meilleure carte, parfois, c'est celle que tu n'achètes pas » : l'intérêt du spectateur passe avant tout. |
| 3. Problème profond | 7 | « Ne pas payer pour rien » est posé dès 0:00, puis résolu à moitié. |
| 4. Public & complexité | 8 | Le cache KV est traduit (« le modèle garde des notes »), la jauge porte le calcul. Seule l'unité Go/Gio trébuche (E4). |
| 5. Valeur & originalité | 8 | Prix en euros d'un même jour, slot x4, câbles, garanties françaises, encart Afrique : personne ne fait ça en français. |
| 6. Structure | 7 | Besoin → 3 routes → recours → choix : clair. Le recours « occasion » détonne : toutes les offres chiffrées sont neuves. |
| 7. Histoire | 6 | Un comparatif bien rythmé, mais sans crise ni récolte finale de la marge du début. |
| 8. Mais / donc | 8 | Chaque route s'ouvre sur sa promesse, puis tombe sur un « sauf que ». |
| 9. Engagement | 7 | « Fais l'addition avec moi » est excellent. Il n'y a qu'une interpellation de ce type. |
| 10. Oralité & liaisons | 8 | ≈ 2,3 liaisons pour 100 mots ✅. Mais il y a 12 prix à virgule à dire, et 4 paragraphes se ferment sur « Bref ». |
| 11. Tics d'IA | 7 | 5 « pas A, B » et une morale de fin. Deux sont à garder. |
| **Total** | **82/110** | |

## 2. Test des 30 secondes (V3 telle quelle)

Temps cumulés à 145 mots/min (entre parenthèses : à 233).

| Tranche | Ce que dit la voix | Verdict |
|---|---|---|
| 0-10 s (0-6) | > « Tu peux payer 1000 euros de plus pour la même mémoire : 32 gigas sur une seule carte, chez le même marchand, le même jour. » | 🟢 Le chiffre le plus fort arrive d'abord, avec les deux prix et la date à l'écran. 🟠 « la même mémoire » s'entend comme « la même puce mémoire ». C'est la même **quantité** (E3). |
| 10-18 s (6-11) | > « Et même avec ces 32 gigas, Qwen 27B avec toute sa conversation te laisse moins d'un giga de marge. » | 🟢 Ça fait monter l'enjeu : même la carte chère est juste. 🟠 Sans « en 4 bits », le chiffre n'est vrai que sous conditions (F81 : fichier Q4, cache 16 bits). « Toute sa conversation » est flou à l'oreille. |
| 18-28 s (11-17) | > « Du coup, pour faire tourner Qwen 27B chez toi, quelle route vers 32 gigas tu prends, et quel piège elle te cache ? » | 🟢 Une seule question centrale, avant 30 s à tous les débits, raccord avec le titre. |
| Plan, 28-51 s (17-32) | > « Aujourd'hui, on va voir combien de mémoire Qwen 27B prend vraiment… Et à la fin, la route que je prendrais, selon le PC que tu as déjà. » | 🟢 Quatre livrables concrets, plus la révélation de fin. 🟠 « les prix… Puis le piège de chacune » annonce deux temps, alors que la vidéo les mélange route par route. Et rien ne promet la réponse au « +1000 € ». |
| 51 s (32) | > « Première réponse, et elle peut déjà t'économiser une carte : … 24 gigas suffisent. » | 🟢 La première partie commence par une réponse qui rend service, pas par une définition. |

**Budget** : 67 mots jusqu'à la question (28 s, 17 s) ✅. Aucune phrase de remplissage, aucun salut, aucune présentation ✅. L'abonnement arrive à 5:07 (3:11), juste après la règle « deux cartes, c'est de la place, pas de la vitesse » ✅.
**À changer** : « la même mémoire » → « la même quantité de mémoire » ; ajouter « en 4 bits » ; un plan qui promet la réponse aux 1000 € (problème 3).

**Réécriture des 30 s, prête à coller** (≈ 70 mots jusqu'à la question : 29 s, 18 s) :

> Tu peux payer 1000 euros de plus pour la même quantité de mémoire : 32 gigas sur une seule carte, chez le même marchand, le même jour. Et même avec ces 32 gigas, Qwen 27B en 4 bits, avec sa conversation la plus longue, te laisse moins d'un giga de marge.
>
> Du coup, pour faire tourner Qwen 27B chez toi, quelle route vers 32 gigas tu prends, et quel piège elle te cache ?
>
> Aujourd'hui, on va voir combien de mémoire Qwen 27B prend vraiment, conversation comprise. Ensuite, trois routes vers 32 gigas, avec leurs prix relevés chez LDLC le 16 novembre, et le piège de chacune, celui qui n'est pas écrit sur l'étiquette. Et à la fin, ce que ces 1000 euros de plus t'achètent vraiment, et la route que je prendrais selon le PC que tu as déjà.

## 3. Erreurs de fait

Toutes les affirmations de la voix ont été relues une par une contre `sources.md`. **Le hook est juste** : 2799,95 − 1799,95 = 1000 € (F95), les deux cartes en stock le 16/11 (F85, F91) ; 15,33 + 16 = 31,33 Gio, marge ≈ 0,67 Gio avant le reste du moteur (F81). Sont justes aussi : 2 / 8 / 16 Gio de cache (F80), les prix et les stocks des sept offres (F85-F87, F91-F94, F96), le slot x4 en PCIe 3.0 relié au chipset, tout en bas (F60), les 2 × 8 broches « peut-être » (F61), les tranches de couches et la vitesse qui ne double pas (F20, F33), la FAQ d'Ollama (F24), le pilote 580 et CUDA 13 (F70), et les 2 ans, 12 mois, 14 jours et vices cachés (F74-F76, F79).

### Bloquantes

| # | Citation | Fait | Problème | Correction |
|---|---|---|---|---|
| E1 | « Bref, ta paire à 919 euros, ce soir, tu ne la commandes pas. » | F87 : « **rupture** en ligne », page lue le 16/11, « ⚠️stock et paire » | La vidéo sort le 30/11. « Ce soir » affirme le stock du jour de visionnage, que personne n'a relevé. Si l'A770 revient en stock, la phrase devient fausse à l'écran. | « Sauf que… le 16 novembre, la page affichait une rupture en ligne. Bref, ta paire à 919 euros, ce jour-là, tu ne pouvais pas la commander. » |
| E2 | « Chez LDLC, toujours le 16 novembre, la moins chère en stock, c'est l'Intel Arc Pro B65 d'ASRock » | F91 : « Offre précise, pas minimum du marché » ; complément du 16/11 : « Aucun classement « moins cher du marché » n'est démontré faute de relevé exhaustif » | Dite ainsi, la phrase parle de tout LDLC. Or seules quatre offres à 32 Go ont été lues. Le script le dit d'ailleurs correctement plus loin (« la moins chère des offres en stock du relevé »). | « Chez LDLC, toujours le 16 novembre, la moins chère en stock de mon relevé, c'est l'Intel Arc Pro B65 d'ASRock : 1800 euros, à 5 centimes près. » |

### Non bloquantes (formulation ou renvoi)

| # | Citation | Fait | Correction |
|---|---|---|---|
| E3 | « pour la même mémoire » (hook) et « Donc même mémoire » | F83 : R9700 en GDDR6. Le type de mémoire de la B65 n'est pas dans les sources (F82). F95 : « aucun meilleur achat inféré » | « la même quantité de mémoire » ; « Donc 32 gigas des deux côtés, et jusqu'à 1000 euros d'écart. » |
| E4 | Visuel « Q4_K_M (16,46 Go) », puis dans la voix « Le fichier 4 bits, c'est un peu plus de 15 gigas » | F81 : 16,46 Go = 15,33 Gio (« Corrige confusion unité ») | Le spectateur voit 16,46, puis entend 15. Mets le visuel de la l. 40 en « 15,3 Gio (16,46 Go affichés sur Hugging Face) », ou ajoute dans la voix : « Le fichier 4 bits, c'est 16 gigas et demi sur Hugging Face, mais compté comme la carte compte, un peu plus de 15. » |
| E5 | « 24 gigas suffisent. [F41] » | F41 ne donne que la taille du fichier. C'est le tableau de la section C (Q4_K_M ✅ à 24 Go, avec 32 K de contexte) et le conseil 10 qui tiennent la phrase | Garde la voix. Corrige le renvoi : « [F41, section C, conseil 10] ». |
| E6 | « refroidissement, connectique, tout est à refaire autour » (V100), renvoyée à F70 et F90 | Ni F70 ni F90 ne parlent du refroidissement. Le conseil 4 le dit des cartes de datacentre en général ; F71 vaut pour la P40 | « En plus, comme les autres cartes de serveur, elle n'a ni ventilateur ni sortie vidéo : tout est à refaire autour. » [conseil 4] |
| E7 | « la carte de serveur que les vidéos anglaises adorent » | Une seule vidéo sourcée : celle sur la V100 (386 K vues) | « la carte de serveur qui fait des centaines de milliers de vues en anglais ». |
| E8 | « Par défaut, le moteur coupe le modèle en tranches de couches » | F20 : c'est le défaut de **llama.cpp**. Ollama, lui, charge le modèle sur une seule carte s'il y tient (F24) | « Par défaut, llama.cpp, le moteur le plus courant, coupe le modèle en tranches de couches… » |

## 4. Les problèmes, du plus grave au moins grave

### P1. Les deux phrases bloquantes (E1, E2)

Voir le tableau. Remplace les deux phrases avant la voix.

### P2. La marge du hook n'est jamais récoltée, et elle change le verdict

Le hook plante : « moins d'un giga de marge ». La vidéo le prouve à 1:24, puis le laisse tomber. Or ce chiffre juge deux routes du verdict :

- **le Mac mini 32 Go** : « cette mémoire, elle est partagée : le système et tes applis se servent dedans » (F89). Avec 31,3 gigas à poser (F81), la conversation complète en cache 16 bits n'y tient pas. Le verdict le propose pourtant (« entre dans la course, à condition d'accepter le délai et la mémoire partagée ») sans le dire ;
- **la seule route du relevé qui dépasse 32 gigas**, le mini-PC Ryzen AI Max+ en 64 (F88), n'est pas citée au moment du choix.

En option, pour la paire : la méthode de la section C retire « environ 1 Go de tampons CUDA par carte » (estimation). Avec deux cartes, ça fait environ deux gigas de tampons, soit plus que la marge de 0,67. C'est un argument de plus pour ton avis contre la paire, à dire comme une estimation.

**Réécriture, à coller à la place du paragraphe du Mac mini dans « La route que je prendrais »** :

> Et si tu veux remplacer tout l'ordinateur, le Mac mini à 1709 euros entre dans la course. Par contre, souviens-toi de l'addition du début : 31 virgule 3 gigas pour la conversation complète. Sur un Mac de 32 gigas, dont le système prend sa part, en cache 16 bits, ça ne rentre pas : tu compresses le cache, ou tu raccourcis. Et si c'est vraiment la conversation complète que tu veux, la seule route de mon relevé qui dépasse 32 gigas, c'est le mini-PC Ryzen AI Max+ en 64, affiché 1999,99 euros, TVA pas claire.

### P3. Le « +1000 € » du hook n'a pas de réponse

Le hook dénonce une injustice, avec 1000 € de plus pour la même mémoire. Le spectateur reste pour savoir si ces 1000 € servent à quelque chose. La route 2 répond : « le prix ne te dit rien sur la vitesse ». Le seul élément sourcé qui distingue la R9700, le guide officiel d'AMD (F83), est dit, puis aussitôt dilué. Résultat : la boucle ouverte à 0:00 se ferme sur « on ne sait pas ». Il faut transformer ce « on ne sait pas » en réponse, grâce à ce que les sources tiennent.

**Réécriture, à la place de « Donc même mémoire… pas forcément le plus de confort pour toi. »** :

> Donc 32 gigas des deux côtés, et jusqu'à 1000 euros d'écart. Alors, ces 1000 euros, ils t'achètent quoi ? Pas un giga de plus, en tout cas. Et la vitesse, le prix ne te la dit pas. Ce que la R9700 a en plus sur le papier, c'est un guide officiel d'AMD pour faire tourner tes outils dessus. Sauf que, même là, 32 gigas et un guide ne prouvent pas que chaque moteur la prend en charge. Du coup, voilà le vrai piège de cette route : avant de comparer les prix, tu vérifies que ton logiciel gère la carte.

### P4. Le verdict hésite encore, et il se contredit sur la paire

- « je regarderais d'abord une seule carte de 32 gigas, en vérifiant mon logiciel » : laquelle ? Le titre promet un choix. Le grill V1 reprochait déjà l'absence de verdict.
- Profil 1 : « + 1 × 5060 Ti », c'est une **paire**. Trois phrases plus loin : « je ne commencerais pas par une paire de cartes », avec la liste de ses pièges. À l'oreille, ça se contredit. En fait, le profil 1 est le seul cas où la paire se défend, puisque la moitié est déjà payée : dis-le.

**Réécriture complète de « La route que je prendrais »** (avec P2 inclus) :

> Alors, quelle route ? Ça dépend de ce que tu as déjà.
>
> Si tu as déjà une carte NVIDIA de 16 gigas, et une tour qui accueille une deuxième carte, c'est le seul cas où je prendrais une paire : la moitié est déjà payée. Regarde la 5060 Ti de 16 gigas, à 1080 euros. Et du coup, la limite d'une par client ne te gêne plus, puisque t'en achètes qu'une. Mais vérifie d'abord ton slot, ton boîtier et tes câbles.
>
> Si tu pars de zéro, moi, je ne commencerais pas par une paire. Sur le papier, c'est la route la moins chère, mais en vrai, c'est celle qui a le plus de pièges : le stock, la règle du magasin, la tour, les câbles, et une vitesse qui ne double pas. Donc je prendrais la B65, à 1800 euros : la moins chère des offres en stock du relevé, avec la même quantité de mémoire que la R9700 à 2800. Sauf que, avant de cliquer, tu vérifies que ton logiciel la gère. S'il ne la gère pas, là, les 1000 euros de la R9700 et son guide officiel peuvent avoir un sens.
>
> Et si tu veux remplacer tout l'ordinateur, le Mac mini à 1709 euros entre dans la course. Par contre, souviens-toi de l'addition du début : 31 virgule 3 gigas pour la conversation complète. Sur un Mac de 32 gigas, dont le système prend sa part, en cache 16 bits, ça ne rentre pas : tu compresses le cache, ou tu raccourcis. Et si c'est vraiment la conversation complète que tu veux, la seule route de mon relevé qui dépasse 32 gigas, c'est le mini-PC Ryzen AI Max+ en 64, affiché 1999,99 euros, TVA pas claire.
>
> Et en fait, si tu as déjà 24 gigas et qu'une conversation courte te suffit, garde ton argent. La meilleure carte, parfois, c'est celle que tu n'achètes pas.
>
> Allez, salut !

(Vérifié : 1080 ≈ 1079,95 F86 ; 1800 ≈ 1799,95 F91 ; 2800 ≈ 2799,95 F85 ; 24 gigas avec une conversation courte, section C ; Mac F89, F94 ; mini-PC F88 ; pièges F20, F33, F60, F61, F86, F87 ; guide F83. L'ancienne phrase « si ton Qwen en 4 bits avec une conversation courte te suffit déjà » ne disait pas qu'il faut déjà 24 gigas : quelqu'un qui n'a que 16 gigas l'aurait mal comprise.)

### P5. La 5080 et « notre exemple » tombent du ciel

> « Prends une carte mère micro-ATX courante, celle de notre exemple. » … « Sur l'exemple documenté, une alimentation de 1000 watts, il ne resterait peut-être que deux prises 8 broches une fois une RTX 5080 branchée. »

Aucun exemple n'a été présenté avant. « L'exemple documenté » sent la note de recherche. Et une RTX 5080 apparaît sans qu'on sache à qui elle est. C'est ta machine (section D de `sources.md`). Le dire est plus clair et plus humain, et ce n'est pas une ouverture « cette carte, c'est la mienne ». Lire un manuel, ce n'est pas non plus prétendre avoir testé.

**Réécriture** :

> Maintenant, le vrai piège de cette route, c'est ta tour. Prends la mienne : une carte mère micro-ATX, comme beaucoup d'autres. D'après son manuel, le deuxième slot a la même longueur que le premier. Pourtant, il n'a que quatre lignes en PCIe 3.0, et il passe par le chipset. Et en plus, il est tout en bas. Du coup, une carte de deux slots dedans dépasse sous la carte mère, et il te faut un boîtier à cinq emplacements.
>
> Ensuite, l'alimentation. La mienne fait 1000 watts. Sauf qu'avec ma RTX 5080 branchée, il ne me resterait peut-être que deux prises 8 broches. Donc avant d'acheter la deuxième carte, tu regardes ton boîtier, et tu comptes tes câbles.

(Si tu préfères garder l'exemple anonyme : « un PC avec une RTX 5080 et une carte mère micro-ATX », mais présente-le dans la phrase.)

### P6. 12 prix à virgule à dire

« 1799,95 », « 2299,95 », « 2349,95 », « 2799,95 », « 9399,95 », « 1079,95 », « 459,95 »… Dit à voix haute, « mille sept cent quatre-vingt-dix-neuf virgule quatre-vingt-quinze » fait 9 mots et casse le rythme. L'œil a déjà le prix exact à l'écran. **Règle proposée** : le prix exact reste dans les [VISUEL] et dans le téléprompteur la première fois (« 1799,95 euros, donc 1800 »), puis on arrondit dans la voix : 1800, 2300, 2350, 2800, 9400, 1080, 460, 920 la paire, 2160 la paire. Les 1000 € du hook restent exacts. Avec les arrondis, ce sont environ 40 mots de moins.

### P7. Le recours ne parle que d'occasion, alors que toutes les offres chiffrées sont neuves

> « Et si tu pars sur de l'occasion, un dernier piège, qui n'est pas technique. … Pendant douze mois, le défaut est présumé exister dès la vente. »

Les sept prix de la vidéo sont des cartes neuves chez LDLC. Le spectateur qui achète la B65 se demande ce qui vaut pour lui : 24 mois de présomption pour le neuf (F75). Le titre du dossier dit « occasion », mais le script n'en chiffre aucune : élargis la phrase.

**Réécriture** :

> Et avant de payer, un dernier piège, qui n'est pas technique. En France, chez un vendeur professionnel, neuf ou d'occasion, tu as deux ans de garantie légale, et il ne peut pas les réduire. Le défaut est présumé exister dès la vente pendant ces deux ans pour du neuf, et douze mois pour de l'occasion. Et pour un achat à distance, tu as quatorze jours après la réception pour te rétracter. Donc ces quatorze jours, c'est ta fenêtre pour tester la carte.

(F74, F75, F79. Le paragraphe « entre particuliers » reste tel quel.)

### P8. Tics : quatre « Bref » en conclusion, cinq « pas A, B »

- « Bref » ferme 4 paragraphes (l. 54, 64, 84, 118). À la troisième fois, on entend la recette.
- « pas A, B » : « le boss de fin, c'est pas le prix, c'est la règle du magasin » ; « deux cartes, c'est de la place, pas de la vitesse » ; « ça ne fait pas 32 gigas libres » ; « tu ne compares plus une carte à une carte. En fait, tu remplaces ton PC entier » ; « Donc 32, c'est pas pour lancer le modèle. En fait, c'est pour lui laisser une longue mémoire ».
  - **À garder** : « de la place, pas de la vitesse » (c'est la thèse, avant l'abonnement) et « le boss de fin » (ton humour de gamer).
  - **À réécrire** : l. 118 → « Du coup, le piège de cette route, c'est la facture : tu remplaces ton PC entier, celui qui te sert aussi à jouer et à bosser. » ; l. 54 → « Bon, la boîte dit 32 gigas, mais ta marge, elle est déjà partie. »
- « Ouais. » (l. 100) : bien, ça sonne vrai.

### P9. Le mini-PC parle comme une note de recherche

> « Le modèle consulté affiche 1999,99 euros pour la version 64 gigas, mais la page ne dit pas clairement si la TVA est comprise. »

« Le modèle consulté » est du vocabulaire de rapport. **Réécriture** :

> Côté PC, il y a les mini-PC Ryzen AI Max+, avec 64 ou même 128 gigas de mémoire partagée. Celui que j'ai regardé affiche 1999,99 euros en 64 gigas, sauf que sa page ne dit pas clairement si la TVA est dedans. Et là encore, la mémoire est fixe : tu choisis à l'achat, et c'est pour toujours.

### P10. Le plan annonce « les prix, puis les pièges », mais la vidéo les mélange

Corrigé dans la réécriture des 30 s (section 2) : « trois routes… avec leurs prix… et le piège de chacune », plus la promesse sur les 1000 €, que P3 tient.

## 5. Ce qui marche, à garder

- **Le hook** : un résultat chiffré, deux prix du même jour à l'écran, puis l'enjeu monte (même la chère est juste). C'est le contraire de l'intro passive qui a perdu 52 % des spectateurs.
- **« Première réponse, et elle peut déjà t'économiser une carte »** : la première partie rend service avant d'expliquer.
- **« Alors fais l'addition avec moi »** et la jauge 15,3 + 16 = 31,3 : le meilleur moment pédagogique de la vidéo.
- **« le modèle garde des notes sur tout ce qui a été dit »** : le cache KV expliqué sans jargon.
- **Le slot « même longueur… Pourtant, il n'a que quatre lignes »** : un vrai piège d'achat, concret et sourcé.
- **« En gros, le boss de fin, c'est pas le prix, c'est la règle du magasin »** : ta voix.
- **« Bref, deux cartes, c'est de la place, pas de la vitesse. Si cette vidéo t'a évité un mauvais achat, abonne-toi. »** : l'abonnement est au bon endroit, juste après le service rendu.
- **« Ouais. Pour ce prix-là, on change carrément de catégorie »** (5090) : une réaction, pas une fiche.
- **L'encart Abidjan, Dakar, Kinshasa** : il sépare ce qui vaut partout (mémoire, slots, alimentation) de ce qui ne vaut qu'en France. C'est exactement ton public.
- **Les interdits** : aucun crochet ✅, aucun « je n'ai rien testé » ✅, aucun nom de chaîne ✅ (LDLC, Ollama, AMD sont des marques, pas des chaînes), un seul renvoi (« on a vu lundi dernier », raccord avec la vidéo du 23/11) ✅, pas de teaser final (« Allez, salut ! ») ✅, l'abonnement après 30 s et après le service rendu ✅.
- **La fin** : « La meilleure carte, parfois, c'est celle que tu n'achètes pas » est une morale, mais elle découle de la première réponse (24 gigas suffisent) : garde-la.
