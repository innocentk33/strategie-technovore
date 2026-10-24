# Sans contact : script v2 (version finale)

**Titre** : *Comment ton téléphone paie sans jamais donner ton numéro de carte* (titre 3 de la fiche, à valider)

**Durée** : environ 1 860 mots de voix off. À 145 mots/min (ton débit mesuré sur ArtCraft, pauses comprises) : environ 12 min 50. À 165 mots/min : 11 min 15. Avec des coupes serrées comme pour Uber (175-180 mots/min), compte 10 min 30 plus les pauses de montage. Les timecodes ci-dessous sont calculés à 165 ; à recaler sur la vraie prise.

**Fil rouge** : un seul geste, le bip, regardé trois fois. D'abord avec la carte, qui donne son vrai numéro. Puis avec le téléphone, qui joue trois tours pour ne pas le donner : le faux numéro (le jeton), le coffre (l'élément sécurisé), le code qui ne sert qu'une fois (le cryptogramme). Enfin, on essaie de casser les trois tours avec ce que les chercheurs ont vraiment trouvé, et chaque attaque récolte un détail planté plus tôt.

**Boucles ouvertes** :
- « comment un faux numéro peut-il payer pour de vrai ? » (hook, refermée à la fin de la section 4) ;
- « neuf euros de fraude, avec un numéro qui se balade : comment c'est possible ? » (fin de la section 1, refermée dans la section 4) ;
- « si quelqu'un va chercher ce jeton dans ton téléphone ? » (fin de la section 2, refermée dans la section 3) ;
- « on verra ce qui arrive quand des chercheurs testent ce genre de règle » (section 3, refermée dans la section 5) ;
- « une banque bien faite… et les autres ? » (fin de la section 4, refermée dans la section 5).

**Changements depuis la V1** (détails dans [`grill-v1.md`](grill-v1.md)) :
- **Hook** : Newcastle dit juste (la carte était dans un portefeuille en cuir, pas « au fond d'une poche ») ; la question centrale devient « comment un faux numéro peut-il payer pour de vrai ? », au lieu de répéter la phrase d'avant mot pour mot.
- **Section 1** : EMVCo présenté d'après son propre site ; une phrase sourcée dit que le mécanisme vaut partout où il y a des cartes EMV, juste avant le crochet sur ton public africain ; les neuf euros deviennent une question, refermée au troisième tour ; la fréquence et les 5 mm passent dans le bandeau « Pour les devs ».
- **Section 2** : « le seul moment où ton vrai numéro sert » était faux (c'est ta banque qui sait relier le jeton à ton compte) ; on dit maintenant qu'il sert, une fois, à fabriquer le faux. Le gamertag gagne un « serveur du jeu », ta banque, qui sait qui est derrière. Ton réflexe de dev passe entre crochets. La parenthèse sur ByteMonk et « voilà pourquoi le titre dit téléphone » sont coupées.
- **Section 3** : la Secure Enclave est expliquée en une phrase sourcée ; le « pourquoi » du plafond dépassé est désormais sourcé (c'est le téléphone qui vérifie que c'est toi et qui le dit au terminal : Black Hat 2019), donc « le code, ton téléphone l'a remplacé par ton visage » n'est plus une supposition ; les certifications et l'anecdote du « geste barrière » de 2020 passent en réserve.
- **Section 4** : « souvent, en NFC » devient « selon le réseau de ta carte » (c'est ce que dit Apple) ; la réponse au hook reprend la banque qui relie le jeton à ton compte.
- **Section 5** : le téléphone verrouillé de 2019, c'était Google Pay avec des cartes Visa, pas Apple : le V1 laissait croire que la règle d'Apple était tombée. « Le ticket composté passe » est maintenant chiffré (18 cartes sur 31, avec un terminal trafiqué). Nouvelle attaque, qui récolte la section 3 : la carte qui se fait passer pour un téléphone (10 cartes Visa sur 12).
- **Section 6** : la fin ne dit plus que le système se passe du terminal, puisque toute la section 5 prouve le contraire : elle retourne sur ce maillon. « Ne vaille presque rien » devient « vaut moins » (EMVCo), la rafale « terminal, magasin, réseau » saute, et l'écran de fin ne cite plus ni Google ni « une milliseconde » (non sourcés dans la fiche du pseudo).

**Conventions** : texte normal = voix off. `[VISUEL : …]` = animation Remotion ou HyperFrames. `[SON : …]` = bruitage ou musique. `[CROCHETS EN MAJUSCULES]` = à remplir par toi. Nombres en lettres pour la lecture, sauf les années. Les faits viennent de `sources.md` ; leurs numéros sont en bas, dans « Faits utilisés ».

---

## 0. Hook (0:00 – 0:28) · objectif : 75 % à 0:15, question centrale à 0:27

[VISUEL : gros plan, une main pose une carte bancaire sur un terminal. Pas de titre, pas de logo.]
[SON : le bip, très net.]

Tu poses ta carte sur le terminal. Bip, c'est payé. Et dans ce bip, ta carte vient de donner ton vrai numéro à un terminal que tu ne connais même pas.

[VISUEL : les seize chiffres sortent de la carte et glissent jusque dans le terminal.]

Des chercheurs l'ont lu avec un simple téléphone Android, la carte encore rangée dans un portefeuille.

[VISUEL : un portefeuille en cuir ; un téléphone passe à un centimètre, et les seize chiffres s'affichent sur son écran. En petit : « Newcastle, 2014 ».]

Sauf que ton téléphone, lui, ne donne jamais ce numéro au magasin. Il envoie un faux. Et le paiement passe quand même.

[VISUEL : un téléphone touche le terminal ; un autre numéro s'affiche, puis « ACCEPTÉ » en vert.]

Alors comment un faux numéro peut-il payer pour de vrai ?

---

## 1. Ce que ta carte raconte (0:28 – 2:26)

Pour le comprendre, il faut d'abord écouter ta carte. Parce qu'elle est bavarde.

[VISUEL : la carte en coupe : l'antenne qui fait le tour, la puce au milieu.]

Le sans contact, c'est du NFC : une onde radio qui porte en général jusqu'à deux centimètres. Du coup, tu dois quasiment coller ta carte au terminal.

[VISUEL : une règle entre la carte et le terminal : « 2 cm en général ». Bandeau « Pour les devs » : « 13,56 MHz · 46 kbit/s à 1,7 Mbit/s · ISO/IEC 14443 A et B · portée certifiée par le NFC Forum : 5 mm ».]

Et quand tu la colles, le terminal lui pose une question, et la carte répond. Dans sa réponse, il y a un code calculé pour ce paiement, un compteur… et ton numéro de carte. Le vrai, celui qui est imprimé dessus.

[VISUEL : la réponse de la carte en trois étiquettes : « code », « compteur », « TON NUMÉRO », qui clignote en rouge.]

En fait, c'est documenté depuis des années. En 2014, à l'université de Newcastle, une appli Android récupère les seize chiffres en moins d'une demi-seconde, à travers un portefeuille en cuir. En 2019, à la conférence Black Hat, deux chercheurs en sécurité listent la même chose dans la réponse de la carte : le code, le compteur, et le numéro.

[VISUEL : les deux articles en capture, seuls le titre et l'année restent nets. Texte : « Toutes les sources en description ».]

Et ce numéro, d'après EMVCo, c'est la donnée qui a le plus de valeur pour un fraudeur. EMVCo, c'est l'organisme qui gère les normes des cartes à puce, et il appartient à Visa, Mastercard et quatre autres réseaux.

[VISUEL : le logo-texte « EMV » sur une puce dorée, six petits blasons génériques autour, sans logos de marque.]

Et ces normes, tu les retrouves partout : la carte à puce EMV, c'est le principal système de paiement par carte dans le monde. En Afrique aussi, le sans contact, on l'utilise. Donc ce que je vais te montrer ne s'arrête pas à la France.

Prends la France, parce qu'on y a les chiffres. En 2025, le sans contact, c'est soixante-douze pour cent des paiements par carte en magasin. Et le téléphone, presque un sur cinq.

Normalement, avec un numéro qui se balade comme ça, ce devrait être la fête de la fraude. Et pourtant, regarde. Sur internet, une carte française se fait frauder cent vingt-quatre euros pour cent mille euros payés. En magasin, en sans contact : neuf euros.

[VISUEL : deux barres : « Internet : 124 € », « Sans contact en magasin : 9 € », pour 100 000 € payés. En petit : « Banque de France, OSMP, rapport 2025 ».]

Comment c'est possible ? Garde la question, la réponse arrive au troisième tour. Parce que ton téléphone, lui, va encore plus loin : il garde ton numéro pour lui. Et pour y arriver, il joue trois tours, l'un après l'autre.

[VISUEL : trois cartes à jouer posées face cachée : « Le faux numéro », « Le coffre », « Le code unique ». Elles reviendront au début de chaque chapitre.]


---

## 2. Premier tour : le faux numéro (2:26 – 4:23)

[VISUEL : la première carte à jouer se retourne : « Le faux numéro ».]
[SON : un « flip » de carte.]

Tout commence le jour où tu ajoutes ta carte dans ton téléphone. C'est là que ton vrai numéro sert : une fois, pour fabriquer le faux.

Chez Apple, c'est ta banque qui crée alors un numéro rien que pour cet appareil. Elle le chiffre, et elle l'envoie à Apple. Sauf qu'Apple ne peut pas le déchiffrer. En fait, il file directement dans une puce spéciale du téléphone. Apple l'appelle le numéro de compte de l'appareil, le DAN.

[VISUEL : le vrai numéro part une seule fois du téléphone vers une banque stylisée (flash) ; la banque renvoie un autre numéro, dans un cadenas, qui traverse un nuage « Apple » sans être ouvert et se loge dans le téléphone.]

**Abonnement (≈ 2:50, 25 % de la vidéo, juste après « Apple ne peut pas le déchiffrer »)**

Si tu aimes voir ce qui se cache derrière les gestes que tu fais sans réfléchir, abonne-toi : sur Technovore, j'ouvre les applis du quotidien une par une.

[VISUEL : bouton « S'abonner » animé en bas à droite, 3 secondes, le cadenas reste à l'écran.]

Chez Google, c'est le même principe : à l'ajout de la carte, un numéro unique est stocké sur le téléphone. Et c'est lui qui part au terminal, à la place de ton vrai numéro.

Du coup, au moment du bip, le magasin reçoit ce numéro de remplacement. Ton vrai numéro, ni Apple ni ton téléphone ne le donnent au commerçant. Ce faux numéro, ça s'appelle un jeton. Et le fait de remplacer ton numéro par un jeton, c'est la tokenisation.

[TON RÉFLEXE DE DEV, SEULEMENT SI C'EST VRAI : « MOI, EN DEV, POUR PROTÉGER UNE DONNÉE, MON PREMIER RÉFLEXE, CE SERAIT DE… ». SINON, ON ENCHAÎNE DIRECTEMENT SUR LA PHRASE SUIVANTE.]

Là, ils ont fait plus radical que chiffrer ton numéro : il ne part pas du tout.

[VISUEL : deux colonnes : « chiffré : le vrai numéro voyage, enfermé » ; « jeton : le vrai numéro reste à la maison ».]

Imagine ton pseudo dans un jeu en ligne. Tout le lobby le voit, et personne ne connaît ton vrai nom. Sauf le serveur du jeu. Le jeton, c'est un peu le gamertag de ta carte, et le serveur qui sait qui se cache derrière, c'est ta banque. Chez Apple, c'est même elle qui l'a fabriqué. Avec une règle en plus : d'après EMVCo, un jeton ne doit pas servir en dehors d'un commerçant, d'un appareil ou d'un type de paiement précis. Résultat : si quelqu'un le vole, il vaut moins que ton vrai numéro.

[VISUEL : un écran de lobby façon jeu en ligne, des pseudos ; le pseudo « J3T0N » s'allume, le vrai nom reste flouté ; une petite icône de serveur « BANQUE » voit le vrai nom.]

Mais alors, si quelqu'un met la main sur ton téléphone, et va chercher ce jeton dedans ? Forcément, il faut le cacher quelque part. Et Apple l'a mis dans un coffre.

---

## 3. Deuxième tour : le coffre (4:23 – 6:22)

[VISUEL : la deuxième carte à jouer se retourne : « Le coffre ».]
[SON : un « flip », puis le clac d'une porte de coffre.]

Chez Apple, ce coffre a un nom : l'élément sécurisé, le Secure Element. C'est une puce à part, certifiée, qui fait tourner la plateforme Java Card. Ouais, t'as bien entendu : du Java, dans ton iPhone.

[VISUEL : la puce dans le téléphone, une petite tasse de café fumante posée dessus (clin d'œil dessiné, pas le logo officiel).]

Du coup, c'est là que dort ton DAN : les serveurs d'Apple gèrent ces numéros, mais ils sont stockés dans cette puce. Et pour parler au terminal, le coffre passe par un aiguilleur, le contrôleur NFC.

[VISUEL : schéma : processeur, coffre (élément sécurisé), et au centre le contrôleur NFC qui aiguille vers le terminal.]

Sauf que le coffre ne s'ouvre pas tout seul. Apple l'écrit noir sur blanc : aucune information de paiement ne part sans que tu te sois authentifié. Avec ton visage, ton doigt, ton code, ou un double-clic sur ta montre déverrouillée. Et l'élément sécurisé ne paie qu'après le feu vert de la Secure Enclave : une zone à part dans la puce principale du téléphone, isolée du processeur, qui garde entre autres les données de ton visage.

[VISUEL : coffre fermé ; un visage scanné, un « OK » qui part de la Secure Enclave et voyage jusqu'au coffre ; le coffre s'ouvre une fraction de seconde, puis se referme.]

Donc un téléphone ramassé dans la rue ne devrait rien payer sans toi. En tout cas, c'est la règle d'Apple. Et tout à l'heure, on verra ce qui arrive quand des chercheurs testent ce genre de règle.

D'ailleurs, ce feu vert change même les plafonds. En France, avec une carte, un paiement sans contact, c'est cinquante euros maximum sans code, dans une limite de cumul que fixe ta banque. Mais avec ton téléphone déverrouillé par ton visage ou ton doigt, tu peux dépasser les cinquante euros sans taper ton code sur le terminal.

[VISUEL : deux jauges : la carte bloquée à « 50 € », le téléphone qui dépasse, avec une petite icône de visage.]

Pourquoi ? Service-public ne le dit pas. Les deux chercheurs de Black Hat, eux, l'expliquent : avec un téléphone, c'est le téléphone lui-même qui vérifie que c'est bien toi, et il prévient le terminal que c'est fait. En gros, le code de ta carte, ton téléphone l'a remplacé par ton visage, ou par son propre code.

[VISUEL : une bulle part du téléphone vers le terminal : « Vérifié ✔ ». Le pavé du code, sur le terminal, se grise.]

Chez Google, la doc pour les banques dit que c'est le téléphone qui garde la clé. La clé qui fabrique le code unique de chaque paiement. Et ce code, c'est le troisième tour, le plus malin des trois.

---

## 4. Troisième tour : le code qui ne sert qu'une fois (6:22 – 7:44) · relance à 57 %

[SON : la musique coupe net, une seconde de silence.]
[VISUEL : la troisième carte à jouer se retourne : « Le code unique ».]

Un faux numéro dans un coffre, c'est déjà pas mal. Mais imagine que quelqu'un enregistre tout l'échange entre ton téléphone et le terminal. Et qu'il le rejoue plus tard, dans un autre magasin.

[VISUEL : un pirate en 2D, capuche obligatoire, enregistre l'échange sur un vieux magnétophone, puis appuie sur « play » devant un autre terminal.]
[SON : clic de magnétophone, bande qui rembobine.]

Pour bloquer ça, chaque paiement porte un code à usage unique : le cryptogramme. Le téléphone le calcule avec une clé et un compteur, qui avance à chaque paiement. Et selon le réseau de ta carte, le terminal ajoute son grain de sel : un nombre imprévisible, qu'il tire lui-même.

[VISUEL : trois ingrédients tombent dans un mixeur : « clé », « compteur : 41 → 42 », « nombre du terminal : 8 305 117 » ; il en sort un code, qui s'affiche une seconde et s'efface.]

Du coup, le code change à chaque bip. Rejouer un vieux code, c'est comme tendre un ticket de métro déjà composté. Et en effet, une banque bien faite refuse un compteur qu'elle a déjà vu.

[VISUEL : un portique de métro, un ticket troué ; le portique reste fermé, petit buzzer.]

Et ce tour-là, ta carte le joue aussi. Tu te rappelles les neuf euros de fraude en magasin ? Voilà une partie de la réponse. Ton numéro, quelqu'un peut le lire. Mais le code de chaque paiement, c'est la puce de ta carte qui le fabrique. La différence avec ton téléphone, c'est que ta carte l'envoie avec ton vrai numéro.

[VISUEL : retour des deux barres de la section 1 ; la barre « 9 € » s'allume, un petit cadenas de puce à côté.]

Voilà comment un faux numéro paie pour de vrai. Un jeton que ta banque sait relier à ton compte, rangé dans un coffre qui attend ton visage, et qui part avec un code jetable.

[VISUEL : les trois cartes à jouer retournées côte à côte.]

Sauf que « une banque bien faite », ça laisse une question en suspens. Et les autres ?

---

## 5. On essaie de tout casser (7:44 – 10:26) · deuxième relance à 69 %

[SON : une basse plus sombre, qui tient.]
[VISUEL : les trois cartes à jouer, et une main qui en tire une pour la retourner à nouveau.]

Jusqu'ici, tout a l'air blindé. Donc maintenant, on essaie de tout casser, avec ce que des chercheurs ont vraiment trouvé.

Première attaque, 2012. Cinq chercheurs de Cambridge, dont Ross Anderson, regardent de près ce fameux nombre « imprévisible ». Et là, surprise : sur certains distributeurs et terminaux, il est fabriqué avec un compteur, ou avec l'heure. Donc il se devine.

[VISUEL : un terminal qui « tire » ses nombres ; on voit qu'ils suivent l'horloge : 10:00:01, 10:00:02…]

Et si tu devines le nombre que le terminal va tirer, tu peux préparer des codes valides à l'avance. Ils appellent ça l'attaque de pré-lecture, le « pre-play ». Et pour la banque, ça ressemble à un clonage de carte.

C'est un peu comme un speedrunner qui connaît la seed du jeu : s'il sait ce qui va tomber, il prépare son coup avant même d'appuyer sur start.

[VISUEL : un écran de speedrun, un chrono, une seed affichée en haut ; le personnage esquive un piège avant même qu'il apparaisse.]

Leur étude portait sur les distributeurs et les terminaux à puce, pas spécialement sur le sans contact. Mais en 2019, à Black Hat Europe, Leigh-Anne Galloway et Tim Yunusov refont le coup en sans contact. Ils trafiquent leur propre terminal pour qu'il envoie toujours le même nombre. Et ils arrivent à réutiliser le même code, plusieurs fois. Sur trente et une cartes testées, dix-huit acceptent un compteur égal ou plus bas que le précédent. Le ticket composté, plus d'une carte sur deux le laisse passer. Et d'après eux, ça marche aussi avec des portefeuilles mobiles sur Android.

[VISUEL : le portique de métro s'ouvre devant le ticket troué. Buzzer qui fait « pouet ». Compteur à l'écran : « 18 / 31 ».]

Deuxième attaque, sur les plafonds. Tu te rappelles ? Avec un téléphone, c'est lui qui prévient le terminal que c'est bien toi. Les deux chercheurs glissent un relais entre une carte en plastique et le terminal, et ils réécrivent la réponse de la carte pour qu'elle dise la même chose. Une carte qui prétend avoir vérifié que c'est toi, alors qu'une carte en est incapable. Résultat : sur douze cartes Visa, dix passent au-dessus du plafond sans aucune vérification, jusqu'à cent livres dans leur test.

[VISUEL : une carte en plastique avec une fausse moustache et des lunettes de téléphone ; la bulle « Vérifié ✔ » de la section 3 sort d'elle ; le terminal affiche « ACCEPTÉ : 100 £ ». Compteur : « 10 / 12 ».]

Et le téléphone ramassé dans la rue ? Ils l'ont testé aussi, avec Google Pay et une carte Visa : un paiement de trente et une livres, juste au-dessus du plafond anglais, avec le téléphone verrouillé, l'écran simplement allumé. Sur Apple Pay, leur document ne montre rien de pareil.

[VISUEL : un téléphone Android générique verrouillé, cadenas à l'écran, posé sur un terminal ; « ACCEPTÉ : 31 £ » s'affiche quand même. Bandeau : « Black Hat Europe 2019 · Google Pay + Visa ».]

Bon, c'est un livre blanc de chercheurs en sécurité, pas un article relu par d'autres chercheurs. Mais ça calme.

Alors, est-ce qu'il faut payer avec ton téléphone parce que c'est moins fraudé ? Les chiffres de la Banque de France ne le disent pas. En 2025, en magasin, le téléphone est à neuf euros de fraude pour cent mille, exactement comme l'ensemble du sans contact. Et en 2023 et 2024, il était même plus fraudé : vingt et un euros, puis seize, contre onze.

[VISUEL : un petit graphique sur trois ans : téléphone 21, 16, 9 ; sans contact 11, 11, 9.]

Bref, ce que le téléphone t'apporte se mesure ailleurs : ton vrai numéro ne sort pas.

---

## 6. Ce que ça change pour toi (10:26 – 11:15)

[SON : la musique du début revient.]
[VISUEL : le bip du hook, rejoué au ralenti, deux fois côte à côte : la carte à gauche, le téléphone à droite.]

Donc la prochaine fois que tu entends le bip, regarde ce que tu as posé. Ta carte donne son vrai numéro. Ton téléphone envoie un jeton, sorti d'un coffre, avec un code jetable. En gros, pour quelqu'un d'autre, tout ça vaut moins que ton vrai numéro. Voilà le génie caché derrière ton bip.

Sauf qu'il reste quelqu'un à qui le système doit faire confiance : le terminal. C'est lui qui doit tirer son nombre au hasard, et c'est lui qui croit le téléphone quand il dit « c'est bon, j'ai vérifié ». Et c'est exactement là que les chercheurs ont tapé.

[VISUEL : les trois cartes à jouer retournées ; derrière elles, le terminal s'allume en orange, seul.]

[TON VÉCU : TU PAIES AVEC TA CARTE OU AVEC TON TÉLÉPHONE ? EST-CE QUE ÇA CHANGE QUELQUE CHOSE POUR TOI APRÈS CETTE VIDÉO ? UNE OU DEUX PHRASES.]

Quelle appli je décortique ensuite ? Dis-le en commentaire, et abonne-toi pour la voir.

Et en attendant, la vidéo juste là, c'est un autre tour de magie : comment un site sait tout de suite que ton pseudo est déjà pris.

[VISUEL : écran de fin, 20 s : la vidéo du pseudo à gauche (ou WhatsApp), bouton « S'abonner » à droite.]

---

## Relances d'attention

| Temps | Type | Ce qui se passe |
|---|---|---|
| 0:05 | Révélation | Ta carte donne ton vrai numéro |
| 0:12 | Preuve | Lu par un téléphone, la carte dans un portefeuille (Newcastle 2014) |
| 0:20 | Retournement | Le téléphone envoie un faux, « ACCEPTÉ » |
| 0:27 | Question centrale | « Comment un faux numéro peut-il payer pour de vrai ? » |
| 0:28 | Pont | « Écouter ta carte. Parce qu'elle est bavarde. » |
| ~0:50 | Visuel | La réponse de la carte, « TON NUMÉRO » en rouge |
| ~1:00 | Preuve | Newcastle, moins d'une demi-seconde, à travers un portefeuille en cuir |
| ~1:25 | Élargissement | La carte EMV, partout dans le monde ; ton crochet |
| ~1:55 | Chiffre | 124 € contre 9 € (« Et pourtant, regarde ») |
| ~2:10 | Boucle ouverte | « Comment c'est possible ? Garde la question » |
| 2:26 | Son + visuel | Première carte retournée |
| ~2:50 | Surprise + appel à l'action | Apple ne peut pas déchiffrer le numéro ; abonnement (25 %) |
| ~3:45 | Référence gamer | Le jeton, gamertag de ta carte ; le serveur, ta banque |
| ~4:15 | Boucle ouverte | « Si quelqu'un va chercher ce jeton ? » |
| ~4:35 | Humour | Du Java dans ton iPhone |
| ~5:25 | Boucle ouverte | « On verra ce qui arrive quand des chercheurs testent… » |
| ~5:35 | Lien au vécu | Le plafond de 50 €, dépassé avec ton visage |
| ~6:00 | Graine | « Il prévient le terminal que c'est fait » |
| 6:22 | Coupure musique | Relance : le pirate au magnétophone (57 %) |
| ~6:55 | Image | Le ticket de métro composté |
| ~7:15 | Boucle fermée | Les neuf euros : c'est la puce qui fabrique le code |
| ~7:35 | Boucle fermée | La réponse au hook, les trois tours ensemble |
| ~7:43 | Boucle ouverte | « Et les autres ? » |
| 7:44 | Changement de ton | « On essaie de tout casser » (69 %) |
| ~8:20 | Référence gamer | Le speedrunner et sa seed |
| ~8:50 | Récolte | Le ticket composté passe : 18 cartes sur 31 |
| ~9:15 | Récolte | La carte déguisée en téléphone : 10 cartes Visa sur 12 |
| ~9:35 | Récolte | Le téléphone verrouillé qui paie (Google Pay) |
| ~9:55 | Question du spectateur | « Je paie avec quoi, alors ? » |
| 10:26 | Rappel + retournement | Le bip du hook ; le terminal, maillon de confiance |
| ~10:55 | Appel à l'action | « Quelle appli je décortique ensuite ? » |

**Total** : 31 relances en 11 min 15, environ une toutes les 22 secondes, et jamais plus de 60 s sans changement.

Les timecodes avec « ~ » sont estimés à 165 mots/min ; recale-les sur la prise.

## Points de décrochage

| Moment | Risque | Problème | Parade |
|---|---|---|---|
| Hook, 0:15-0:30 | Moyen | La révélation (la carte donne son numéro) peut faire peur au lieu d'intriguer | Le « ACCEPTÉ » du téléphone suit tout de suite : la question est « comment ? », pas « au secours » |
| Section 1, EMVCo et le monde | Moyen | Un organisme et une norme, du sec | Une phrase chacun, et le crochet de ton public juste après pour parler à 63 % des spectateurs |
| Section 1, la fraude | Moyen | Deux chiffres au milieu d'un chapitre technique | Deux barres seulement, puis une vraie question (« comment c'est possible ? ») refermée au troisième tour |
| Section 3, le coffre | Élevé | Le bloc le plus dense (élément sécurisé, Secure Enclave, contrôleur NFC, plafonds) | Certifications et anecdote de 2020 coupées ; le gag Java ; un seul schéma ; la boucle « on verra… » au milieu |
| Relance (~60 %) | Élevé | Chute classique, et la réponse au hook tombe vers 7:35 | Musique coupée et le pirate au magnétophone ; puis « Et les autres ? » relance aussitôt vers « on essaie de tout casser » |
| Section 5, trois attaques | Moyen | Des chiffres (18/31, 10/12, 31 £) d'affilée | Chaque attaque récolte une image déjà vue (le ticket, la bulle « Vérifié », le téléphone ramassé) et s'affiche avec son compteur |

## Notes de montage

- **Composants à construire une fois** : les trois cartes à jouer (face cachée, retournée), le schéma du coffre (processeur, élément sécurisé, contrôleur NFC), la bulle « Vérifié ✔ » (section 3, reprise en section 5), le mixeur du cryptogramme, le portique de métro.
- **Pas de vraie interface Apple Pay ou Google Wallet à l'écran** : tout est reconstruit en motion design, sans logo de marque (comme pour Uber, `strategie.md`, partie juridique). Le téléphone de la section 5 est un Android générique. Captures autorisées : la doc Apple Platform Security, la doc Google pour les banques, les premières pages des articles (Newcastle 2014, Cambridge 2012, Black Hat 2019), le rapport de la Banque de France.
- **Java** : la tasse de café est un clin d'œil dessiné, pas le logo officiel.
- **Le speedrun et le lobby** : écrans de jeu génériques, en motion design, pas d'extrait d'un jeu précis.
- **Les numéros à l'écran** : des numéros inventés et visiblement faux (par exemple 4000 0000 0000 0000), jamais un vrai numéro de test d'un réseau présenté comme une vraie carte.
- **La carte déguisée** (section 5) : le gag visuel porte toute l'attaque ; garde-le court (2 s).
- **Énergie** : calme, puis une montée à chaque carte retournée, une vraie cassure à la coupure de musique du troisième tour, puis le ton plus sombre de la section 5.
- **Miniature** : piste de la fiche (téléphone sur un terminal, deux numéros, l'un barré), charte noire, à faire après la planche des vidéos hôtes.

## Faits utilisés

| Fait (`sources.md`) | Phrase du script |
|---|---|
| 19, 36 | « ta carte vient de donner ton vrai numéro » ; « la carte encore rangée dans un portefeuille » ; Newcastle 2014, « en moins d'une demi-seconde », « dans un portefeuille en cuir » ; Black Hat 2019 : « le code, le compteur, et le numéro » |
| 11, 15, 31 | « ton téléphone, lui, quand il paie, ne donne jamais ce numéro au magasin » ; « ni Apple ni ton téléphone ne le donnent au commerçant » ; « C'est là que ton vrai numéro sert : une fois, pour fabriquer le faux » |
| 6, 7 | « jusqu'à deux centimètres » ; bandeau devs (13,56 MHz, débit, ISO/IEC 14443, 5 mm certifiés) |
| 14, 33 | « la donnée qui a le plus de valeur pour un fraudeur » ; « un jeton ne doit pas servir en dehors d'un commerçant, d'un appareil ou d'un type de paiement précis » ; « il vaut moins que ton vrai numéro » ; « un jeton que ta banque sait relier à ton compte » |
| 32 | « l'organisme qui gère les normes des cartes à puce, et il appartient à Visa, Mastercard et quatre autres réseaux » |
| 35 | « la carte à puce EMV, c'est le principal système de paiement par carte dans le monde » ; « Cinq chercheurs de Cambridge » |
| 28 | « soixante-douze pour cent des paiements par carte en magasin », « le téléphone, presque un sur cinq » |
| 20, 27 (lignes 25, 26 respectées) | « Sur internet… cent vingt-quatre euros pour cent mille… En magasin, en sans contact : neuf euros » ; section 5 : « neuf euros… exactement comme l'ensemble du sans contact », « vingt et un euros, puis seize, contre onze » |
| 10 | « ta banque crée alors un numéro rien que pour cet appareil. Elle le chiffre… Apple ne peut pas le déchiffrer » ; « le DAN » ; « Chez Apple, c'est même elle qui l'a fabriqué » |
| 15 | « Chez Google… un numéro unique est stocké sur le téléphone » |
| 8 | « une puce à part, certifiée, qui fait tourner la plateforme Java Card » |
| 9 | « les serveurs d'Apple gèrent ces numéros, mais ils sont stockés dans cette puce » ; le contrôleur NFC aiguilleur |
| 12, 34 | « aucune information de paiement ne part sans que tu te sois authentifié » (visage, doigt, code, montre) ; « le feu vert de la Secure Enclave : une zone à part dans la puce principale du téléphone, isolée du processeur, qui garde entre autres les données de ton visage » ; dit comme « la règle d'Apple » |
| 1, 2 | « cinquante euros maximum sans code, dans une limite de cumul que fixe ta banque » |
| 5 | « tu peux dépasser les cinquante euros sans taper ton code sur le terminal » |
| 37 | « Service-public ne le dit pas » ; « c'est le téléphone lui-même qui vérifie que c'est bien toi, et il prévient le terminal que c'est fait » ; « le code de ta carte, ton téléphone l'a remplacé par ton visage, ou par son propre code » |
| 22 (⚠️) | « Chez Google, la doc pour les banques dit que c'est le téléphone qui garde la clé. La clé qui fabrique le code unique » (pas d'HCE, pas d'élément sécurisé chez Google) |
| 13 | « une clé et un compteur, qui avance à chaque paiement » ; « selon le réseau de ta carte, le terminal ajoute… un nombre imprévisible » |
| 16 (⚠️) | « une banque bien faite refuse un compteur qu'elle a déjà vu » |
| 19 (Galloway et Yunusov : la carte « signe la transaction avec un cryptogramme ») | « le code de chaque paiement, c'est la puce de ta carte qui le fabrique » ; « Voilà une partie de la réponse » (lien avec les 9 € donné comme partiel, pas comme cause unique) |
| 17 | Cambridge 2012, « dont Ross Anderson », compteur ou heure, « pre-play », « ressemble à un clonage » ; « portait sur les distributeurs et les terminaux à puce, pas spécialement sur le sans contact » |
| 18, 40 | « Ils trafiquent leur propre terminal pour qu'il envoie toujours le même nombre » ; « réutiliser le même code, plusieurs fois » ; « Sur trente et une cartes testées, dix-huit » ; « ça marche aussi avec des portefeuilles mobiles sur Android » |
| 38 | « ils réécrivent la réponse de la carte » ; « une carte en est incapable, et ils l'écrivent eux-mêmes » ; « sur douze cartes Visa, dix » ; « jusqu'à cent livres » |
| 30, 39 | « avec Google Pay et une carte Visa : un paiement de trente et une livres… avec le téléphone verrouillé, l'écran simplement allumé » ; « Sur Apple Pay, leur document ne montre rien de pareil » ; « un livre blanc… pas un article relu » |

Non utilisés : faits 4 (règlement européen), 21 (fraude par manipulation : surtout des virements), 23 (les deux modes du NFC Forum), 24 (ByteMonk), 3, 29 et 41 (le plafond de 2020, en réserve). Interdits respectés : pas de « téléphone 9, carte 47 », pas de « paie avec le téléphone, c'est moins fraudé », pas de « impossible à rejouer », pas de « 4 cm », pas d'HCE, pas de « Google a besoin du cloud », pas de « le téléphone est inviolable », pas de « le système ne fait confiance à personne ». Aucun conseil de sécurité (étui, désactiver le NFC…) : aucune source n'en mesure l'effet.

## Questions pour l'auteur

1. **Ton public africain** (section 1) : réglé le 23/10. Tu dis que le sans contact s'utilise en Afrique : la phrase est dans la section 1, sans chiffre (fait 42). Si tu as un exemple à toi (ton pays, ta banque), ajoute-le.
2. **Ton réflexe de dev** (section 2) : tu aurais chiffré le numéro, toi ? Si oui, dis-le avec tes mots dans le crochet ; sinon, on enchaîne direct sur « Là, ils ont fait plus radical ».
3. **Ton vécu** (section 6) : tu paies avec ta carte ou ton téléphone ? Est-ce que cette recherche a changé ta façon de payer ?
4. **Le sous-texte** : la fiche proposait « tu n'as pas à faire confiance au terminal ». La section 5 montre l'inverse : le système fait confiance au terminal, et c'est là qu'il casse. La fin le dit maintenant. C'est toujours ce que tu veux que le spectateur retienne ?
5. **L'écran de fin** : le pseudo ou WhatsApp ? Les deux seront sortis le 5 avril. Si c'est le pseudo, la phrase reprend le titre que sa fiche aura gardé (« en une milliseconde » n'y est pas sourcé).
6. **La réserve** : l'anecdote du « geste barrière » de 2020 (30 → 50 €) et la correction de ByteMonk sont coupées, environ 110 mots. Tu en veux une ?

## Bloc en réserve (~45 s)

**Le plafond de 2020** (section 3, après les plafonds ; faits 3, 29, 41) :
> Et ces cinquante euros, c'est récent. Jusqu'au 11 mai 2020, c'était trente. En pleine crise sanitaire, les banques françaises, Visa et Mastercard l'ont relevé, et le ministère de l'Économie présentait le sans contact comme un « geste barrière ».

**La correction de ByteMonk** (section 2, après Google ; faits 15, 24) :
> Si tu regardes des vidéos en anglais sur le sujet, tu vas peut-être entendre que chez Google, ce numéro est dans le cloud. La doc de Google pour les banques dit qu'il est stocké sur le téléphone.

(Ne dis pas qu'elle « dit le contraire » de « l'appli en redemande un à chaque paiement » : la doc lue ne parle pas de ce point.)
