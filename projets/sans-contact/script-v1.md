# Sans contact : script v1

**Titre** : *Comment ton téléphone paie sans jamais donner ton numéro de carte* (titre 3 de la fiche, à valider)

**Durée** : environ 1 790 mots de voix off. À 145 mots/min (ton débit mesuré sur ArtCraft, pauses comprises) : environ 12 min 20. À 165 mots/min : 10 min 50. Avec des coupes serrées comme pour Uber (175-180 mots/min), compte 10 min plus les pauses de montage. Les timecodes ci-dessous sont calculés à 165 ; à recaler sur la vraie prise.

**Fil rouge** : un seul geste, le bip, regardé trois fois. D'abord avec la carte, qui donne son vrai numéro. Puis avec le téléphone, qui joue trois tours pour ne pas le donner : le faux numéro (le jeton), le coffre (l'élément sécurisé), le code qui ne sert qu'une fois (le cryptogramme). Enfin, on essaie de casser les trois tours avec ce que les chercheurs ont vraiment trouvé.

**Boucles ouvertes** :
- « comment ton téléphone paie avec un faux numéro ? » (hook, refermée à la fin de la section 4) ;
- « si quelqu'un récupère ton jeton ? » (fin de la section 2, refermée dans la section 3) ;
- « des chercheurs ont trouvé un moyen de contourner cette règle » (section 3, refermée dans la section 5) ;
- « une banque bien faite… et les autres ? » (fin de la section 4, refermée dans la section 5).

**Conventions** : texte normal = voix off. `[VISUEL : …]` = animation Remotion ou HyperFrames. `[SON : …]` = bruitage ou musique. `[CROCHETS EN MAJUSCULES]` = à remplir par toi. Nombres en lettres pour la lecture, sauf les années. Les faits viennent de `sources.md` (colonne « 2e vérif ») ; leurs numéros sont en bas, dans « Faits utilisés ».

---

## 0. Hook (0:00 – 0:28) · objectif : 75 % à 0:15, question centrale à 0:23

[VISUEL : gros plan, une main pose une carte bancaire sur un terminal. Pas de titre, pas de logo.]
[SON : le bip, très net.]

Tu poses ta carte sur le terminal. Bip, c'est payé. Et dans ce bip, ta carte vient de donner ton vrai numéro à un terminal que tu ne connais même pas.

[VISUEL : les seize chiffres sortent de la carte et glissent jusque dans le terminal.]

Des chercheurs l'ont lu avec un simple téléphone Android. Sauf que ton téléphone, lui, quand il paie, ne donne jamais ce numéro au magasin. Il envoie un faux. Et le paiement passe quand même.

[VISUEL : un téléphone touche le terminal ; un autre numéro s'affiche, puis « ACCEPTÉ » en vert.]

Alors comment ton téléphone peut-il payer sans jamais donner ton numéro de carte ?

---

## 1. Ce que ta carte raconte (0:28 – 2:22)

Pour le comprendre, il faut d'abord écouter ta carte. Parce qu'elle est bavarde.

[VISUEL : la carte en coupe : l'antenne qui fait le tour, la puce au milieu.]

Le sans contact, c'est du NFC : une onde radio à treize virgule cinquante-six mégahertz, qui porte en général jusqu'à deux centimètres. La norme, elle, certifie cinq millimètres. Du coup, tu dois quasiment coller ta carte au terminal.

[VISUEL : une règle entre la carte et le terminal : « 5 mm certifiés », « 2 cm en général ». Bandeau « Pour les devs » : « 13,56 MHz · 46 kbit/s à 1,7 Mbit/s · ISO/IEC 14443 A et B ».]

Et quand tu la colles, le terminal lui pose une question, et la carte répond. Dans sa réponse, il y a un code calculé pour ce paiement, un compteur… et ton numéro de carte. Le vrai, celui qui est imprimé dessus.

[VISUEL : la réponse de la carte en trois étiquettes : « code », « compteur », « TON NUMÉRO », qui clignote en rouge.]

En fait, ça fait des années que c'est documenté. En 2014, des chercheurs de l'université de Newcastle font tourner une appli sur un téléphone Android, et elle lit les seize chiffres de la carte, la carte au fond d'une poche. En 2019, à la conférence Black Hat, deux autres chercheurs listent la même chose dans la réponse de la carte : le code, le compteur, et le numéro.

[VISUEL : les deux articles en capture, seuls le titre et l'année restent nets. Texte : « Toutes les sources en description ».]

Et ce numéro, c'est justement la donnée la plus précieuse de ta carte. C'est EMVCo, l'organisme derrière les normes des cartes à puce, qui le dit.

Sauf que tout le monde paie comme ça. En France, en 2025, le sans contact, c'est soixante-douze pour cent des paiements par carte en magasin. Et le téléphone, presque un sur cinq.

[TON PUBLIC AFRICAIN PAIE-T-IL EN SANS CONTACT ? À ADAPTER]

Normalement, avec un numéro qui se balade comme ça, ce devrait être la fête de la fraude. Et pourtant, regarde. Sur internet, une carte française se fait frauder cent vingt-quatre euros pour cent mille euros payés. Posée sur un terminal sans contact : neuf euros.

[VISUEL : deux barres : « Internet : 124 € », « Sans contact : 9 € », pour 100 000 € payés. En petit : « Banque de France, OSMP, rapport 2025 ».]

Donc le sans contact tient déjà très bien. Mais ton téléphone fait un truc de plus : il garde ton numéro pour lui. Et pour y arriver, il joue trois tours, l'un après l'autre.

[VISUEL : trois cartes à jouer posées face cachée : « Le faux numéro », « Le coffre », « Le code unique ». Elles reviendront au début de chaque chapitre.]

Tout ce qui suit vient des docs d'Apple et de Google, et des articles des chercheurs. Les liens sont en description.

---

## 2. Premier tour : le faux numéro (2:22 – 4:38)

[VISUEL : la première carte à jouer se retourne : « Le faux numéro ».]
[SON : un « flip » de carte.]

Tout commence le jour où tu ajoutes ta carte dans ton téléphone. Et c'est le seul moment où ton vrai numéro sert.

Chez Apple, ta banque crée alors un numéro rien que pour cet appareil. Elle le chiffre, et elle l'envoie à Apple. Sauf qu'Apple ne peut pas le déchiffrer. Ce numéro file directement dans une puce spéciale du téléphone, et on en reparle juste après. Apple l'appelle le numéro de compte de l'appareil, le DAN.

[VISUEL : le vrai numéro part une seule fois du téléphone vers une banque stylisée (flash) ; la banque renvoie un autre numéro, dans un cadenas, qui traverse un nuage « Apple » sans être ouvert et se loge dans le téléphone.]

**Abonnement (≈ 2:50, 26 % de la vidéo, juste après « Apple ne peut pas le déchiffrer »)**

Si tu aimes voir ce qui se cache derrière les gestes que tu fais sans réfléchir, abonne-toi : sur Technovore, j'ouvre les applis du quotidien une par une.

[VISUEL : bouton « S'abonner » animé en bas à droite, 3 secondes, le cadenas reste à l'écran.]

Chez Google, c'est le même principe : à l'ajout de la carte, un numéro unique est stocké sur le téléphone. Et c'est lui qui part au terminal, à la place de ton vrai numéro.

Petite parenthèse. Si tu regardes des vidéos en anglais sur le sujet, tu vas peut-être entendre que chez Google, ce numéro est dans le cloud, et que l'appli en redemande un à chaque paiement. La doc de Google pour les développeurs dit le contraire : il est stocké sur l'appareil.

[VISUEL : un nuage barré ; bandeau « Doc Google, mise à jour du 27/11/2025 : stocké sur l'appareil ».]

Du coup, au moment du bip, le magasin reçoit ce numéro de remplacement. Ton vrai numéro, ni Apple ni ton téléphone ne le donnent au commerçant. Ce faux numéro, ça s'appelle un jeton. Et le fait de remplacer ton numéro par un jeton, c'est la tokenisation.

Moi, en dev, mon premier réflexe pour protéger une donnée, ce serait de la chiffrer. Là, ils ont trouvé plus radical : la donnée ne part pas du tout.

[VISUEL : deux colonnes : « chiffré : le vrai numéro voyage, enfermé » ; « jeton : le vrai numéro reste à la maison ».]

Imagine ton pseudo dans un jeu en ligne. Tout le lobby le voit, et personne ne connaît ton vrai nom. Le jeton, c'est un peu le gamertag de ta carte. Avec une règle en plus : d'après EMVCo, son usage est limité. Il peut être lié à un commerçant, à un appareil, ou à un type de paiement. Résultat : si quelqu'un le vole, il vaut moins que ton vrai numéro.

[VISUEL : un écran de lobby façon jeu en ligne, des pseudos ; le pseudo « J3T0N » s'allume, le vrai nom reste flouté.]

Et voilà pourquoi le titre dit « téléphone » : ta carte, elle, donne son vrai numéro à chaque bip.

Mais alors, si quelqu'un met la main sur ton téléphone, et va chercher ce jeton dedans ? Forcément, il faut le cacher quelque part. Et Apple l'a mis dans un coffre.

---

## 3. Deuxième tour : le coffre (4:38 – 6:52)

[VISUEL : la deuxième carte à jouer se retourne : « Le coffre ».]
[SON : un « flip », puis le clac d'une porte de coffre.]

Chez Apple, ce coffre a un nom : l'élément sécurisé, le Secure Element. C'est une puce à part, certifiée, qui fait tourner la plateforme Java Card. Ouais, t'as bien entendu : du Java, dans ton iPhone.

[VISUEL : la puce dans le téléphone, une petite tasse de café fumante posée dessus (le logo Java en clin d'œil, en motion design).]

Et ses certificats ne sortent pas d'une boîte de céréales : la puce et sa plateforme sont certifiées selon l'évaluation de sécurité d'EMVCo, et la puce a la certification Critères Communs.

C'est là que dort ton DAN. Les serveurs d'Apple gèrent ces numéros, mais ils sont stockés dans cette puce. Et pour parler au terminal, il y a un aiguilleur : le contrôleur NFC. Lui, il fait passer les échanges entre le processeur du téléphone, l'élément sécurisé et le terminal.

[VISUEL : schéma : processeur, coffre (élément sécurisé), et au centre le contrôleur NFC qui aiguille vers le terminal.]

Sauf que le coffre ne s'ouvre pas tout seul. Apple l'écrit noir sur blanc : aucune information de paiement ne part sans que tu te sois authentifié. Avec ton visage, ton doigt, ton code, ou un double-clic sur ta montre déverrouillée. Et l'élément sécurisé ne paie qu'après le feu vert de la Secure Enclave.

[VISUEL : coffre fermé ; un visage scanné, un « OK » qui voyage jusqu'au coffre ; le coffre s'ouvre une fraction de seconde, puis se referme.]

Donc un téléphone ramassé dans la rue ne devrait rien payer sans toi. En tout cas, c'est la règle d'Apple. Et tout à l'heure, on verra que des chercheurs ont trouvé un moyen de contourner ce genre de règle.

D'ailleurs, ce coffre change même les plafonds. En France, avec une carte, un paiement sans contact, c'est cinquante euros maximum, sans code. Et au-delà, ta banque fixe un plafond cumulé, et un nombre de paiements à la suite avant de te redemander ton code. Mais avec ton téléphone déverrouillé par ton visage ou ton doigt, tu peux dépasser les cinquante euros sans taper ton code sur le terminal. Tu vois le lien : le code, ton téléphone l'a déjà remplacé par ton visage.

[VISUEL : deux jauges : la carte bloquée à « 50 € », le téléphone qui dépasse, avec une petite icône de visage.]

Et ces cinquante euros, c'est récent. Jusqu'au 11 mai 2020, c'était trente. En pleine crise sanitaire, les banques françaises, Visa et Mastercard l'ont relevé, et le ministre de l'Économie parlait du sans contact comme d'un « geste barrière ».

[VISUEL : un calendrier qui tourne jusqu'au « 11 mai 2020 », la jauge qui passe de 30 à 50.]

Chez Google, la doc ne parle pas d'élément sécurisé. Ce qu'elle dit, c'est que c'est le téléphone qui garde la clé. La clé qui fabrique le code unique de chaque paiement. Et ce code, c'est le troisième tour, le plus malin des trois.

---

## 4. Troisième tour : le code qui ne sert qu'une fois (6:52 – 7:57) · relance à 63 %

[SON : la musique coupe net, une seconde de silence.]
[VISUEL : la troisième carte à jouer se retourne : « Le code unique ».]

Un faux numéro dans un coffre, c'est déjà pas mal. Mais imagine que quelqu'un enregistre tout l'échange entre ton téléphone et le terminal. Et qu'il le rejoue plus tard, dans un autre magasin.

[VISUEL : un pirate en 2D, capuche obligatoire, enregistre l'échange sur un vieux magnétophone, puis appuie sur « play » devant un autre terminal.]
[SON : clic de magnétophone, bande qui rembobine.]

Pour bloquer ça, chaque paiement porte un code à usage unique : le cryptogramme. Le téléphone le calcule avec une clé et un compteur, qui avance à chaque paiement. Et souvent, en NFC, le terminal ajoute son grain de sel : un nombre imprévisible, qu'il tire lui-même.

[VISUEL : trois ingrédients tombent dans un mixeur : « clé », « compteur : 41 → 42 », « nombre du terminal : 8 305 117 » ; il en sort un code, qui s'affiche une seconde et s'efface.]

Du coup, le code change à chaque bip. Rejouer un vieux code, c'est comme tendre un ticket de métro déjà composté. Et en effet, une banque bien faite refuse un compteur qu'elle a déjà vu.

[VISUEL : un portique de métro, un ticket troué ; le portique reste fermé, petit buzzer.]

Et ce tour-là, ta carte le joue aussi. Tu te rappelles, le code dans sa réponse au terminal ? La différence, c'est qu'elle l'envoie avec ton vrai numéro.

Voilà comment ton téléphone paie sans jamais donner ton numéro au magasin. Un faux numéro, rangé dans un coffre, qui part avec un code jetable.

[VISUEL : les trois cartes à jouer retournées côte à côte.]

Sauf que « une banque bien faite », ça laisse une question en suspens. Et les autres ?

---

## 5. On essaie de tout casser (7:57 – 10:00) · deuxième relance à 73 %

[SON : une basse plus sombre, qui tient.]
[VISUEL : les trois cartes à jouer, et une main qui en tire une pour la retourner à nouveau.]

Jusqu'ici, tout a l'air blindé. Donc maintenant, on essaie de tout casser, avec ce que des chercheurs ont vraiment trouvé.

Première attaque, 2012. Cinq chercheurs de Cambridge, dont Ross Anderson, regardent de près ce fameux nombre « imprévisible ». Et là, surprise : sur certains distributeurs et terminaux, il est fabriqué avec un compteur, ou avec l'heure. Donc il se devine.

[VISUEL : un terminal qui « tire » ses nombres ; on voit qu'ils suivent l'horloge : 10:00:01, 10:00:02…]

Et si tu devines le nombre que le terminal va tirer, tu peux préparer des codes valides à l'avance. Ils appellent ça l'attaque de pré-lecture, le « pre-play ». Et pour la banque, ça ressemble à un clonage de carte.

C'est un peu comme un speedrunner qui connaît la seed du jeu : s'il sait ce qui va tomber, il prépare son coup avant même d'appuyer sur start.

[VISUEL : un écran de speedrun, un chrono, une seed affichée en haut ; le personnage esquive un piège avant même qu'il apparaisse.]

Petite précision : leur étude portait sur les distributeurs et les terminaux à puce, pas spécialement sur le sans contact. Mais elle montre une chose : le troisième tour tient seulement si le terminal tire vraiment au hasard.

Deuxième attaque, 2019, à Black Hat Europe. Leigh-Anne Galloway et Tim Yunusov s'attaquent aux plafonds. Et ils arrivent à les contourner, y compris sur des portefeuilles mobiles, avec le téléphone verrouillé. Le téléphone ramassé dans la rue, tu te rappelles ? Voilà ce qui arrive quand quelqu'un teste vraiment la règle.

[VISUEL : un téléphone verrouillé, cadenas à l'écran, posé sur un terminal ; « ACCEPTÉ » s'affiche quand même. Bandeau : « Black Hat Europe 2019 ».]

Et dans le même document, ils écrivent qu'en pratique, des banques ne refusent pas un compteur plus bas que le dernier. Le ticket composté, certaines le laissent passer. Bon, c'est un livre blanc de chercheurs en sécurité, pas un article relu par d'autres chercheurs. Mais ça calme.

[VISUEL : le portique de métro s'ouvre devant le ticket troué. Buzzer qui fait « pouet ».]

Alors, est-ce qu'il faut payer avec ton téléphone parce que c'est moins fraudé ? Les chiffres de la Banque de France ne le disent pas. En 2025, en magasin, le téléphone est à neuf euros de fraude pour cent mille, exactement comme l'ensemble du sans contact. Et en 2023 et 2024, il était même plus fraudé : vingt et un euros, puis seize, contre onze.

[VISUEL : un petit graphique sur trois ans : téléphone 21, 16, 9 ; sans contact 11, 11, 9.]

Bref, ce que le téléphone t'apporte se mesure ailleurs : ton vrai numéro ne sort pas.

---

## 6. Ce que ça change pour toi (10:00 – 10:51)

[SON : la musique du début revient.]
[VISUEL : le bip du hook, rejoué au ralenti, deux fois côte à côte : la carte à gauche, le téléphone à droite.]

Donc la prochaine fois que tu entends le bip, regarde ce que tu as posé. Ta carte donne son vrai numéro, avec un code unique. Ton téléphone envoie un jeton, sorti d'un coffre qui attend ton visage, avec un code qui ne sert qu'une fois.

En gros, le système ne te demande pas de faire confiance au terminal, ni au magasin, ni à son réseau. Il s'arrange pour que ce qui sort de ton téléphone ne vaille presque rien pour quelqu'un d'autre. Voilà le génie caché derrière ton bip.

[TON VÉCU : TU PAIES AVEC TA CARTE OU AVEC TON TÉLÉPHONE ? EST-CE QUE ÇA CHANGE QUELQUE CHOSE POUR TOI APRÈS CETTE VIDÉO ? UNE OU DEUX PHRASES.]

Sur Technovore, j'ouvre comme ça les applis que tu as dans la poche. Quelle appli je décortique ensuite ? Dis-le en commentaire, et abonne-toi pour la voir.

Et en attendant, la vidéo juste là, c'est un autre tour de magie : comment Google sait en une milliseconde que ton pseudo est déjà pris.

[VISUEL : écran de fin, 20 s : la vidéo du pseudo à gauche (ou WhatsApp), bouton « S'abonner » à droite.]

---

## Relances d'attention

| Temps | Type | Ce qui se passe |
|---|---|---|
| 0:05 | Révélation | Ta carte donne ton vrai numéro |
| 0:15 | Retournement | Le téléphone envoie un faux, « ACCEPTÉ » |
| 0:23 | Question centrale | « Comment ton téléphone peut-il payer sans jamais donner ton numéro ? » |
| 0:28 | Pont | « Écouter ta carte. Parce qu'elle est bavarde. » |
| 0:50 | Visuel | La réponse de la carte, « TON NUMÉRO » en rouge |
| 1:04 | Preuve | Newcastle 2014, la carte au fond d'une poche |
| 1:53 | Chiffre | 124 € contre 9 € (« Et pourtant, regarde ») |
| 2:13 | Visuel récurrent | Les trois cartes à jouer, face cachée |
| 2:22 | Son + visuel | Première carte retournée |
| 2:40 | Surprise | Apple ne peut pas déchiffrer le numéro |
| 2:50 | Appel à l'action | Abonnement (26 %) |
| 3:12 | Correction | La légende du jeton « dans le cloud » |
| 3:56 | Référence gamer | Le jeton, gamertag de ta carte |
| 4:28 | Boucle ouverte | « Si quelqu'un va chercher ce jeton ? » |
| 4:48 | Humour | Du Java dans ton iPhone |
| 5:46 | Boucle ouverte | « On verra que des chercheurs… » (refermée à 8:56) |
| 5:53 | Lien au vécu | Le plafond de 50 €, dépassé avec ton visage |
| 6:25 | Anecdote | 30 € → 50 € en 2020, « geste barrière » |
| 6:52 | Coupure musique | Relance : le pirate au magnétophone (63 %) |
| 7:20 | Image | Le ticket de métro composté |
| 7:42 | Boucle fermée | La réponse au hook, les trois tours ensemble |
| 7:56 | Boucle ouverte | « Et les autres ? » |
| 7:57 | Changement de ton | « On essaie de tout casser » (73 %) |
| 8:35 | Référence gamer | Le speedrunner et sa seed |
| 8:56 | Boucle fermée | Le téléphone verrouillé qui paie quand même |
| 9:22 | Retournement | Le ticket composté passe |
| 9:32 | Question du spectateur | « Je paie avec quoi, alors ? » |
| 10:00 | Rappel | Le bip du hook, rejoué |
| 10:37 | Appel à l'action | « Quelle appli je décortique ensuite ? » |

**Total** : 29 relances en 10 min 51, environ une toutes les 22 secondes, et jamais plus de 60 s sans changement.

## Points de décrochage

| Moment | Risque | Problème | Parade |
|---|---|---|---|
| Hook, 0:15-0:30 | Moyen | La révélation (la carte donne son numéro) peut faire peur au lieu d'intriguer | Le « ACCEPTÉ » du téléphone suit tout de suite : la question est « comment ? », pas « au secours » |
| Section 1, le NFC | Moyen | Mégahertz et millimètres, de la fiche technique | Une seule phrase, la règle à l'écran, et le reste en bandeau « Pour les devs » |
| Section 1, la fraude | Moyen | Deux chiffres au milieu d'un chapitre technique | Deux barres seulement, et le retournement « Et pourtant, regarde » |
| Section 3, le coffre | Élevé | Le bloc le plus dense (élément sécurisé, Secure Enclave, contrôleur NFC, plafonds) | Le gag Java, un seul schéma, et la boucle « on verra que des chercheurs… » ouverte au milieu |
| Relance (~60 %) | Élevé | Chute classique, et la réponse au hook tombe à 7:42 | Musique coupée et le pirate au magnétophone à 6:52 ; puis « Et les autres ? » à 7:56 relance aussitôt vers « on essaie de tout casser » |
| Section 5, la fraude | Moyen | Des chiffres de nouveau, en fin de vidéo | Un seul graphique ; il répond à la question que le spectateur se pose (« donc je paie avec quoi ? ») |

## Notes de montage

- **Composants à construire une fois** : les trois cartes à jouer (face cachée, retournée), le schéma du coffre (processeur, élément sécurisé, contrôleur NFC), le mixeur du cryptogramme, le portique de métro. Les cartes à jouer servent de carte du trajet, comme les trois étapes d'Uber.
- **Pas de vraie interface Apple Pay ou Google Wallet à l'écran** : tout est reconstruit en motion design, sans logo de marque (comme pour Uber, `strategie.md`, partie juridique). Captures autorisées : la doc Apple Platform Security, la doc Google pour les développeurs, les premières pages des articles (Newcastle 2014, Cambridge 2012, Black Hat 2019), le rapport de la Banque de France.
- **Java** : la tasse de café est un clin d'œil dessiné, pas le logo officiel.
- **Le speedrun et le lobby** : écrans de jeu génériques, en motion design, pas d'extrait d'un jeu précis.
- **Les numéros à l'écran** : des numéros inventés et visiblement faux (par exemple 4000 0000 0000 0000), jamais un vrai numéro de test d'un réseau présenté comme une vraie carte.
- **Énergie** : calme, puis une montée à chaque carte retournée, et une vraie cassure à 6:52 (musique coupée), puis le ton plus sombre de 7:57.
- **Miniature** : piste de la fiche (téléphone sur un terminal, deux numéros, l'un barré), charte noire, à faire après la planche des vidéos hôtes.

## Faits utilisés

| Fait (`sources.md`) | Phrase du script |
|---|---|
| 19 | « ta carte vient de donner ton vrai numéro » ; « Des chercheurs l'ont lu avec un simple téléphone Android » ; Newcastle 2014, « la carte au fond d'une poche » ; Black Hat 2019 : « le code, le compteur, et le numéro » |
| 11, 15, 31 | « ton téléphone, lui, quand il paie, ne donne jamais ce numéro au magasin » ; « ni Apple ni ton téléphone ne le donnent au commerçant » ; « le seul moment où ton vrai numéro sert » (l'ajout de la carte) |
| 6, 7 | « treize virgule cinquante-six mégahertz », « jusqu'à deux centimètres », « certifie cinq millimètres » ; bandeau devs (débit, ISO/IEC 14443) |
| 14 | « la donnée la plus précieuse de ta carte » ; « son usage est limité… un commerçant, un appareil, ou un type de paiement » ; « il vaut moins que ton vrai numéro » |
| 28 | « soixante-douze pour cent des paiements par carte en magasin », « le téléphone, presque un sur cinq » |
| 20, 27 (lignes 25, 26 respectées) | « Sur internet… cent vingt-quatre euros pour cent mille… sans contact : neuf euros » ; section 5 : « neuf euros… exactement comme l'ensemble du sans contact », « vingt et un euros, puis seize, contre onze » |
| 10 | « ta banque crée alors un numéro rien que pour cet appareil. Elle le chiffre… Apple ne peut pas le déchiffrer » ; « le DAN » |
| 15, 24 | « La doc de Google… dit le contraire : il est stocké sur l'appareil » (correction de ByteMonk, sans le nommer) |
| 8 | « une puce à part, certifiée, qui fait tourner la plateforme Java Card » ; « évaluation de sécurité d'EMVCo », « Critères Communs » |
| 9 | « Les serveurs d'Apple gèrent ces numéros, mais ils sont stockés dans cette puce » ; le contrôleur NFC aiguilleur |
| 12 | « aucune information de paiement ne part sans que tu te sois authentifié » (visage, doigt, code, montre) ; « le feu vert de la Secure Enclave » ; dit comme « la règle d'Apple » |
| 1, 2 | « cinquante euros maximum, sans code » ; « plafond cumulé, et un nombre de paiements à la suite » |
| 5 | « tu peux dépasser les cinquante euros sans taper ton code sur le terminal » |
| 3 (⚠️), 29 (⚠️) | « Jusqu'au 11 mai 2020, c'était trente » ; « les banques françaises, Visa et Mastercard » ; « le ministre de l'Économie parlait… de “geste barrière” » |
| 22 (⚠️) | « c'est le téléphone qui garde la clé. La clé qui fabrique le code unique » (pas d'HCE, pas d'élément sécurisé chez Google) |
| 13 | « une clé et un compteur, qui avance à chaque paiement » ; « souvent, en NFC… un nombre imprévisible, qu'il tire lui-même » |
| 16 (⚠️) | « une banque bien faite refuse un compteur qu'elle a déjà vu » ; section 5 : « en pratique, des banques ne refusent pas un compteur plus bas que le dernier » |
| 17 | Cambridge 2012, « dont Ross Anderson », compteur ou heure, « pre-play », « ressemble à un clonage » ; « portait sur les distributeurs et les terminaux à puce, pas spécialement sur le sans contact » |
| 18, 30 | Galloway et Yunusov, Black Hat Europe 2019 : plafonds contournés « y compris sur des portefeuilles mobiles, avec le téléphone verrouillé » ; « un livre blanc… pas un article relu » |

Non utilisés : faits 4 (règlement européen), 21 (fraude par manipulation : surtout des virements), 23 (les deux modes du NFC Forum), 24 (sauf comme légende corrigée). Interdits respectés : pas de « téléphone 9, carte 47 », pas de « paie avec le téléphone, c'est moins fraudé », pas de « impossible à rejouer », pas de « 4 cm », pas d'HCE, pas de « Google a besoin du cloud », pas de « le téléphone est inviolable ».

## Questions pour l'auteur

1. **Ton public africain** : est-ce qu'il paie en sans contact (carte ou téléphone), ou surtout en mobile money ? Selon ta réponse, on adapte le passage `[TON PUBLIC AFRICAIN…]` de la section 1. Je n'ai rien écrit sur l'Afrique faute de source.
2. **« Moi, en dev, mon premier réflexe… ce serait de la chiffrer »** (section 2) : garde cette phrase seulement si c'est vrai pour toi ; sinon, dis-moi ton vrai réflexe ou on la coupe.
3. **Ton vécu** (section 6) : tu paies avec ta carte ou ton téléphone ? Est-ce que cette recherche a changé ta façon de payer ?
4. **Le sous-texte** proposé dans la fiche, dit à la fin (« le système ne te demande pas de faire confiance au terminal… ») : c'est bien ce que tu veux que le spectateur retienne ?
5. **À sourcer** avant la v2 (absents de `sources.md`) : que EMVCo est « l'organisme derrière les normes des cartes à puce » ; ce qu'est la Secure Enclave, si tu veux l'expliquer en une phrase ; que « les banques françaises » de l'annonce de 2020 sont bien la FBF et le Groupement des cartes bancaires (c'est la formulation du fait 3, mais de seconde main).
6. **« Tu vois le lien : le code, ton téléphone l'a déjà remplacé par ton visage »** (section 3) : c'est notre lecture de service-public.gouv.fr, qui ne donne pas la raison. On la garde comme image, ou tu préfères la couper ?
7. **L'écran de fin** : le pseudo ou WhatsApp ? Les deux seront sorties le 5 avril ; le pseudo colle mieux (« un autre tour de magie »).
