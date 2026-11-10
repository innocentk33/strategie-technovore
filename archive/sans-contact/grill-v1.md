# Grill du script Sans contact v1 (23/10/2026)

> Script grillé : [`script-v1.md`](script-v1.md) (1 787 mots de voix off, 10 min 50 à 165 mots/min). Grille : `youtube-script-grill`, mode B, variante storytelling (test des 30 secondes, axe 10, axes S1 à S6).
> Hypothèses : titre *Comment ton téléphone paie sans jamais donner ton numéro de carte*, miniature de la fiche (un téléphone sur un terminal, deux numéros, l'un barré), public de 18-30 ans curieux de tech, 63 % en Afrique, une bonne part de devs ; objectif : une vidéo « génie derrière l'app » d'accueil et de suggestions, à côté des vidéos « comment ça marche » sur Face ID.
> Faits revérifiés à la source le 23/10 : voir « Vérification des faits » en bas. Dix lignes ajoutées à `sources.md` (faits 32 à 41).
> Version corrigée : [`script.md`](script.md).

## Verdict

**Note globale : 🟠, 13/20.** Le squelette est le meilleur des scripts « génie » à ce stade : un seul geste regardé trois fois, trois cartes à jouer qui servent de carte du trajet, et une section « on essaie de tout casser » qui donne à la vidéo ce que ByteMonk et les vidéos françaises n'ont pas, l'honnêteté sur les limites. Les liaisons sont déjà au niveau de Cam (2,0 pour 100 mots), et les pièges de la 2e vérification sont évités : pas de « téléphone 9, carte 47 », pas de « moins fraudé », pas de « impossible à rejouer ».

Les trois plus gros problèmes :
1. **Le téléphone verrouillé de 2019 était un Google Pay, pas un iPhone.** Le script rappelle « la règle d'Apple » puis enchaîne « Le téléphone ramassé dans la rue, tu te rappelles ? Voilà ce qui arrive quand quelqu'un teste vraiment la règle ». Le livre blanc teste Google Pay avec des cartes Visa et ne montre rien sur Apple Pay. Dans le même livre blanc, « le ticket composté passe » est vrai, mais avec un terminal trafiqué, et ça se chiffre (18 cartes sur 31).
2. **La fin se contredit.** « Le système ne te demande pas de faire confiance au terminal » arrive deux minutes après trois attaques qui passent toutes par le terminal (le nombre qu'il tire, ce qu'il croit). Le sous-texte proposé par la fiche ne tient pas face à la section 5, alors que ce retournement fait une meilleure fin.
3. **La promesse du hook n'est qu'à moitié tenue.** « Et le paiement passe quand même » : le script ne dit jamais pourquoi la banque accepte un faux numéro, et il affirme même que l'ajout de la carte est « le seul moment où ton vrai numéro sert ». Il manque une phrase : c'est ta banque qui fabrique le jeton (chez Apple) et qui sait le relier à ton compte.

Rien de bloquant. Une passe sur le hook, la section 3 (densité), la section 5 (attributions) et la fin suffit. La V2 (`script.md`) l'applique.

## La promesse, le problème profond, la chaîne « mais / donc »

- **Promesse** (titre + miniature) : « ton téléphone paie sans donner ton numéro, et je vais te montrer comment ». La vidéo la tient en trois tours, avec une preuve pour chacun. Ce qui manquait : comment la banque reconnaît le faux numéro (corrigé, section 2 et réponse au hook).
- **Problème de surface** : ce qui part de ton téléphone en une fraction de seconde.
- **Problème profond** (proposé par la fiche, à valider par l'auteur) : « tu n'as pas à faire confiance au terminal ». La section 5 montre l'inverse : le système réduit ce qu'il faut confier au terminal, mais il lui fait toujours confiance sur deux points (tirer un nombre au hasard, croire le téléphone quand il dit « vérifié »). Le sous-texte juste, c'est « la sécurité vient de la conception, et la conception a un maillon de confiance ». Question n° 4 pour l'auteur.
- **La chaîne** : ta carte donne ton numéro (révélation) **mais** la fraude en magasin est basse (9 €) **donc** quelque chose protège déjà la carte ; ton téléphone va plus loin **mais** si on vole le jeton ? **donc** un coffre ; **mais** si on enregistre l'échange ? **donc** un code unique ; **mais** « une banque bien faite »… et les autres ? **donc** on essaie de tout casser. Elle tient partout, sauf au milieu de la section 3 : « D'ailleurs, ce coffre change même les plafonds » puis « Et ces cinquante euros, c'est récent » puis « Chez Google… », trois « et aussi » de suite.

## Le test des 15 premières secondes

Relues seules (≈ 41 mots, 15 s à 165 mots/min) :

> « Tu poses ta carte sur le terminal. Bip, c'est payé. Et dans ce bip, ta carte vient de donner ton vrai numéro à un terminal que tu ne connais même pas. Des chercheurs l'ont lu avec un simple téléphone Android. »

C'est le bon moment. La révélation « ta carte donne ton numéro » est l'image que la miniature prépare, et elle surprend : presque personne ne le sait, et les vidéos françaises qui en parlent font peur sans l'expliquer. Rien de contextuel, ni présentation, ni « dans cette vidéo ». La règle du 22/10 est respectée.

Un seul manque : la preuve reste abstraite. « Un simple téléphone Android » ne montre rien. Le papier de Newcastle a le détail qui rend la scène réelle : la carte était dans un **portefeuille en cuir** (et pas « au fond d'une poche », comme le dit la section 1, voir les faits). Correction : « Des chercheurs l'ont lu avec un simple téléphone Android, la carte encore rangée dans un portefeuille. »

## Test des 30 secondes

| Tranche | Ce que dit le script | Verdict |
|---|---|---|
| 0-5 s | > « Tu poses ta carte sur le terminal. Bip, c'est payé. Et dans ce bip, ta carte vient de donner ton vrai numéro… » | 🟢 Le sujet et une tension dès la troisième phrase ; le geste est celui de tout le monde. |
| 5-15 s | > « Des chercheurs l'ont lu avec un simple téléphone Android. » | 🟠 La preuve est là, mais sans le détail qui la rend visible (le portefeuille). |
| 15-30 s | > « Sauf que ton téléphone, lui, quand il paie, ne donne jamais ce numéro au magasin. Il envoie un faux. Et le paiement passe quand même. » / « Alors comment ton téléphone peut-il payer sans jamais donner ton numéro de carte ? » | 🟠 Le contraste carte / téléphone est parfait. La question centrale, elle, répète mot pour mot la phrase d'avant et le titre : elle n'ajoute rien. « Comment un faux numéro peut-il payer pour de vrai ? » pose la même question avec la tension du « faux ». |
| Pont | > « Pour le comprendre, il faut d'abord écouter ta carte. Parce qu'elle est bavarde. » | 🟢 Il repart d'un endroit inattendu (la carte, pas le téléphone) et ouvre une deuxième question : qu'est-ce qu'elle raconte ? |

**Budget :** 78 mots ≈ 28 s à 165 mots/min, 32 s à 145. La question centrale commence au 65e mot (≈ 24 s à 165) : dans les 90 premiers mots.
**À couper :** « quand il paie » (le spectateur sait de quoi on parle).
**Réécriture des 30 s** (dans `script.md`, 79 mots, question à partir du 69e) :
> Tu poses ta carte sur le terminal. Bip, c'est payé. Et dans ce bip, ta carte vient de donner ton vrai numéro à un terminal que tu ne connais même pas. Des chercheurs l'ont lu avec un simple téléphone Android, la carte encore rangée dans un portefeuille. Sauf que ton téléphone, lui, ne donne jamais ce numéro au magasin. Il envoie un faux. Et le paiement passe quand même. Alors comment un faux numéro peut-il payer pour de vrai ?

## Tableau de bord

| Axe | Note | En une phrase |
|---|---|---|
| 1. Promesse | 🟠 | Tenue en trois tours, mais « le paiement passe quand même » n'est jamais expliqué (comment la banque reconnaît le jeton). |
| 2. Alignement | 🟢 | Aucun conseil vendu, l'appel à l'abonnement est court et bien placé ; pas de conseil de sécurité inventé. |
| 3. Problème profond | 🟠 | Le sous-texte « pas besoin de faire confiance au terminal » est contredit par la section 5. |
| 4. Public & complexité | 🟠 | La section 3 empile élément sécurisé, Java Card, deux certifications, contrôleur NFC, Secure Enclave (jamais expliquée), plafonds, 2020 et Google en 2 min 14. |
| 5. Valeur & originalité | 🟢 | Carte contre téléphone, ce que la carte envoie, et des attaques réelles : rien de tout ça en français au-delà de quelques milliers de vues. |
| 6. Structure & transformation | 🟢 | Début : « je pose ma carte sans y penser ». Fin : « je sais ce que j'ai donné ». Les trois cartes à jouer portent la progression. |
| 7. Histoire | 🟠 | Une enquête sans personnage avant la section 5 ; les chercheurs n'ont pas d'envie avant d'arriver. Acceptable pour un « génie derrière l'app », comme Uber. |
| 8. Mais / donc | 🟢 | Très bon partout, sauf trois « et aussi » au milieu de la section 3. |
| 9. Engagement actif | 🟠 | Aucune question laissée au spectateur : les 9 € de fraude sont un mystère parfait, et le script le résout tout de suite (« Donc le sans contact tient déjà très bien »). |
| 10. Rythme, oralité & liaisons | 🟢 | 2,0 liaisons pour 100 mots, des réactions (« Ouais, t'as bien entendu », « Mais ça calme ») ; une rafale dans la section 3, le hook à 1,3. |
| 11. Tics d'IA | 🟢 | Cinq tics légers, aucun grave (tableau plus bas). |
| S1. Les 30 premières secondes | 🟠 | 5 questions sur 6 : la question centrale répète le titre. |
| S2. Le pont | 🟢 | « Écouter ta carte. Parce qu'elle est bavarde. » |
| S3. Les retournements | 🟢 | Un « sauf que » ou « mais » toutes les 25-35 s, sauf un trou d'environ 50 s dans la section 3 (5:53-6:45). |
| S4. Planté / récolté | 🟠 | Les graines sont là (le téléphone ramassé, le ticket composté, le code dans la réponse de la carte), mais deux récoltes sont fausses ou trop fortes, et la meilleure graine (« le code, ton téléphone l'a remplacé par ton visage ») n'est jamais récoltée. |
| S5. Personnages et enjeu | 🟠 | Des chercheurs nommés seulement en section 5 ; pas de « quelqu'un veut quelque chose ». |
| S6. La fin | 🟠 | Elle résume, puis assène une morale que la section 5 vient de démentir. |

## L'axe 10 : les liaisons

Compte du `controle.py` (liste du skill, texte dit seulement) : **36 liaisons pour 1 787 mots, soit 2,0 pour 100**, au-dessus du repère de 1,5 et du double de nos téléprompteurs (0,7 à 0,9). Le script ne compte pas « sauf qu'» devant une voyelle (« Sauf qu'Apple »), ni « d'ailleurs », « alors », « bon » ou « en tout cas » : le vrai chiffre est un peu plus haut.

| Section | Mots | Liaisons | Pour 100 mots |
|---|---|---|---|
| 0. Hook | 78 | 1 | 1,3 |
| 1. Ce que ta carte raconte | 314 | 7 | 2,2 |
| 2. Le faux numéro | 375 | 6 | 1,6 |
| 3. Le coffre | 366 | 5 | 1,4 |
| 4. Le code unique | 180 | 7 | 3,9 |
| 5. On essaie de tout casser | 334 | 8 | 2,4 |
| 6. Ce que ça change | 140 | 2 | 1,4 |

**La rafale** (section 3, cinq phrases de faits sans liaison ni réaction) :
> « Et ses certificats ne sortent pas d'une boîte de céréales : la puce et sa plateforme sont certifiées selon l'évaluation de sécurité d'EMVCo, et la puce a la certification Critères Communs. / C'est là que dort ton DAN. Les serveurs d'Apple gèrent ces numéros, mais ils sont stockés dans cette puce. Et pour parler au terminal, il y a un aiguilleur : le contrôleur NFC. Lui, il fait passer les échanges entre le processeur du téléphone, l'élément sécurisé et le terminal. »

Correction : les certifications sautent (personne ne retient « Critères Communs », et la puce est déjà dite « certifiée ») ; « Du coup, c'est là que dort ton DAN » rattache le fait au coffre ; le contrôleur NFC tient en une phrase, le schéma fait le reste.

**Une liaison mal employée** (section 1) :
> « Sauf que tout le monde paie comme ça. »

« Sauf que » annonce un retournement ; ici, rien ne se retourne (on passe de « le numéro est précieux » à « tout le monde paie comme ça »). Remplacé par « Prends la France, parce qu'on y a les chiffres », qui sert aussi de transition pour le public africain.

Dans `script.md` : 1 860 mots, **2,0 liaisons pour 100**, la section 3 passe à 1,8, la fin à 1,5.

## Le grill

### 1. Section 5 : deux récoltes qui disent plus que les sources

> « Deuxième attaque, 2019, à Black Hat Europe. Leigh-Anne Galloway et Tim Yunusov s'attaquent aux plafonds. Et ils arrivent à les contourner, y compris sur des portefeuilles mobiles, avec le téléphone verrouillé. Le téléphone ramassé dans la rue, tu te rappelles ? Voilà ce qui arrive quand quelqu'un teste vraiment la règle. »

La graine plantée en section 3, c'est « la règle d'Apple ». Le livre blanc (relu en entier le 23/10) teste le téléphone verrouillé dans une seule section : « Bypassing CDCVM limits on Google Pay with Visa cards », 31 £ payés sans déverrouiller, l'écran allumé. Apple Pay n'apparaît que dans la description des plafonds. Le spectateur entend « la règle d'Apple est tombée » : c'est faux, et un fan d'iPhone le relèvera.

> « Et dans le même document, ils écrivent qu'en pratique, des banques ne refusent pas un compteur plus bas que le dernier. Le ticket composté, certaines le laissent passer. »

Le fait 16 ne dit que la première phrase. Le livre blanc va plus loin, et c'est meilleur : ils ont trafiqué leur propre terminal pour qu'il envoie toujours le même nombre (« aa aa aa aa »), réutilisé le même cryptogramme plusieurs fois, et **18 cartes sur 31** ont accepté un compteur égal ou plus bas. L'image du ticket composté devient vraie, avec son chiffre et sa condition (un terminal trafiqué).

**Correction :** trois attaques dans l'ordre de l'escalade, chacune récolte une graine.
> Mais en 2019, à Black Hat Europe, Leigh-Anne Galloway et Tim Yunusov refont le coup en sans contact. Ils trafiquent leur propre terminal pour qu'il envoie toujours le même nombre. Et ils arrivent à réutiliser le même code, plusieurs fois. Sur trente et une cartes testées, dix-huit acceptent un compteur égal ou plus bas que le précédent. Le ticket composté, plus d'une carte sur deux le laisse passer.
>
> Deuxième attaque, sur les plafonds. Tu te rappelles ? Avec un téléphone, c'est lui qui prévient le terminal que c'est bien toi. Les deux chercheurs glissent un relais entre une carte en plastique et le terminal, et ils réécrivent la réponse de la carte pour qu'elle dise la même chose. […] Résultat : sur douze cartes Visa, dix passent au-dessus du plafond sans aucune vérification, jusqu'à cent livres dans leur test.
>
> Et le téléphone ramassé dans la rue ? Ils l'ont testé aussi, avec Google Pay et une carte Visa : un paiement de trente et une livres, juste au-dessus du plafond anglais, avec le téléphone verrouillé, l'écran simplement allumé. Sur Apple Pay, leur document ne montre rien de pareil.

La deuxième attaque est nouvelle (faits 37 et 38) : c'est la récolte de la meilleure graine du script (point 3 ci-dessous), et le gag visuel (une carte déguisée en téléphone) porte toute l'idée.

### 2. La fin dit le contraire de la section 5

> « En gros, le système ne te demande pas de faire confiance au terminal, ni au magasin, ni à son réseau. Il s'arrange pour que ce qui sort de ton téléphone ne vaille presque rien pour quelqu'un d'autre. Voilà le génie caché derrière ton bip. »

Trois soucis :
- Cambridge 2012 et Black Hat 2019 cassent tous les deux le troisième tour **par le terminal** : un nombre qui se devine, un terminal trafiqué, un terminal qui croit ce qu'on lui dit. Le script l'a même dit : « le troisième tour tient seulement si le terminal tire vraiment au hasard ».
- « Ne vaille presque rien » : EMVCo dit que le jeton « réduit la valeur » des données volées (faits 14, 33). « Presque rien » est à nous.
- « Ni au terminal, ni au magasin, ni à son réseau » : rafale de trois, puis une petite morale.

**Correction :** la fin retourne sur ce maillon, au lieu de le nier. C'est la fin « qui retourne quelque chose » du skill (section 6 de `storytelling.md`).
> Donc la prochaine fois que tu entends le bip, regarde ce que tu as posé. Ta carte donne son vrai numéro. Ton téléphone envoie un jeton, sorti d'un coffre, avec un code jetable. En gros, pour quelqu'un d'autre, tout ça vaut moins que ton vrai numéro. Voilà le génie caché derrière ton bip.
>
> Sauf qu'il reste quelqu'un à qui le système doit faire confiance : le terminal. C'est lui qui doit tirer son nombre au hasard, et c'est lui qui croit le téléphone quand il dit « c'est bon, j'ai vérifié ». Et c'est exactement là que les chercheurs ont tapé.

### 3. « Le code, ton téléphone l'a remplacé par ton visage » : honnête maintenant, et c'est la meilleure graine

> « Mais avec ton téléphone déverrouillé par ton visage ou ton doigt, tu peux dépasser les cinquante euros sans taper ton code sur le terminal. Tu vois le lien : le code, ton téléphone l'a déjà remplacé par ton visage. »

Dans le V1, c'est notre lecture de service-public.gouv.fr, qui ne donne pas la raison. Dite comme une évidence (« Tu vois le lien »), elle présentait une supposition comme un fait. Ce n'était pas honnête, même si c'est vrai.

Le livre blanc de Black Hat donne la raison : « CDCVM is performed entirely by the consumer device. Apple Pay uses Face ID, Touch ID, and passcodes to verify the cardholder », et le téléphone signale au terminal que la vérification est faite (fait 37). C'est le mécanisme que les chercheurs détournent ensuite avec la carte déguisée (fait 38). La phrase devient sourcée et elle plante la récolte de la section 5.

**Correction :**
> Pourquoi ? Service-public ne le dit pas. Les deux chercheurs de Black Hat, eux, l'expliquent : avec un téléphone, c'est le téléphone lui-même qui vérifie que c'est bien toi, et il prévient le terminal que c'est fait. En gros, le code de ta carte, ton téléphone l'a remplacé par ton visage, ou par son propre code.

« Ou par son propre code » : service-public parle d'un téléphone déverrouillé « par biométrie ou code », et Apple liste le code parmi les vérifications.

Au passage, « D'ailleurs, ce coffre change même les plafonds » devient « ce feu vert change même les plafonds » : c'est la vérification qui change le plafond, pas la puce.

### 4. Le hook promet un « comment » que la vidéo ne finit pas

> « Tout commence le jour où tu ajoutes ta carte dans ton téléphone. Et c'est le seul moment où ton vrai numéro sert. »

C'est trop fort. Ton vrai numéro sert à chaque paiement, de l'autre côté : ta banque doit bien savoir quel compte débiter quand le jeton revient. EMVCo écrit que les établissements financiers relient le jeton au numéro de carte (fait 33). Le fait 31 donne la bonne formule : le vrai numéro sert une fois, à l'ajout de la carte, **pour créer le jeton**. Et c'est justement la réponse à « le paiement passe quand même ».

**Correction** (section 2, puis réponse au hook en section 4) :
> Tout commence le jour où tu ajoutes ta carte dans ton téléphone. C'est là que ton vrai numéro sert : une fois, pour fabriquer le faux.
>
> […] Le jeton, c'est un peu le gamertag de ta carte, et le serveur qui sait qui se cache derrière, c'est ta banque. Chez Apple, c'est même elle qui l'a fabriqué.
>
> […] Voilà comment un faux numéro paie pour de vrai. Un jeton que ta banque sait relier à ton compte, rangé dans un coffre qui attend ton visage, et qui part avec un code jetable.

Le gamertag y gagne : un pseudo que tout le lobby voit, et un serveur qui sait qui est derrière, c'est exactement le jeton.

### 5. Les 9 € : un mystère résolu trop vite

> « Normalement, avec un numéro qui se balade comme ça, ce devrait être la fête de la fraude. Et pourtant, regarde. […] Posée sur un terminal sans contact : neuf euros. / Donc le sans contact tient déjà très bien. »

Le « Et pourtant » est excellent, puis « Donc le sans contact tient déjà très bien » ferme la question tout de suite, sans réponse. Or la réponse est dans la vidéo : le troisième tour, que la carte joue aussi (« Tu te rappelles, le code dans sa réponse au terminal ? »). C'est l'engagement actif qui manquait (axe 9).

**Correction :**
> Comment c'est possible ? Garde la question, la réponse arrive au troisième tour.
>
> […] Et ce tour-là, ta carte le joue aussi. Tu te rappelles les neuf euros de fraude en magasin ? Voilà une partie de la réponse. Ton numéro, quelqu'un peut le lire. Mais le code de chaque paiement, c'est la puce de ta carte qui le fabrique.

« Une partie de la réponse » : aucune source ne dit que le cryptogramme explique à lui seul le taux de fraude. Et « Posée sur un terminal sans contact » devient « En magasin, en sans contact » : le chiffre de 9 € compte aussi les téléphones (fait 27).

### 6. La section 3 est trop chargée

De 4:38 à 6:52, le spectateur reçoit : élément sécurisé, Java Card, l'évaluation EMVCo, les Critères Communs, le DAN, le contrôleur NFC, l'authentification, la Secure Enclave (citée sans un mot d'explication), les plafonds, le cumul, l'anecdote de 2020 et Google. Les points de décrochage du V1 la notent déjà « Élevé ».

**Correction :**
- les certifications sautent (voir la rafale, axe 10) ;
- la Secure Enclave reçoit sa phrase, sourcée (fait 34) : « une zone à part dans la puce principale du téléphone, isolée du processeur, qui garde entre autres les données de ton visage » ;
- l'anecdote du « geste barrière » de 2020 passe en réserve. Elle est jolie mais ne sert pas le mécanisme, elle ne parle qu'au public français, et sa source reste de seconde main (faits 3, 29, 41).

La section passe de 366 à 329 mots, avec une explication de plus.

### 7. Ce qui reste au crochet de l'auteur

> « Moi, en dev, mon premier réflexe pour protéger une donnée, ce serait de la chiffrer. »

C'est une opinion de l'auteur qu'il n'a pas donnée, écrite comme si elle était à lui. Même règle que le « j'ai résilié Netflix » d'ArtCraft : elle passe entre crochets, et la phrase suivante (« Là, ils ont fait plus radical que chiffrer ton numéro : il ne part pas du tout ») tient seule.

### 8. Le public africain

> « [TON PUBLIC AFRICAIN PAIE-T-IL EN SANS CONTACT ? À ADAPTER] »

Le crochet est au bon endroit : juste après le seul passage purement français (les chiffres de la Banque de France). Mais le script ne dit nulle part que le mécanisme dépasse la France, alors que c'est sourcé : EMV est « le principal système de paiement par carte dans le monde » (Bond et al., fait 35) et EMVCo gère ces normes pour tout le monde (fait 32). Correction : une phrase juste avant le crochet (« Donc ce que je vais te montrer ne s'arrête pas à la France »), puis « Prends la France, parce qu'on y a les chiffres ». Sans source sur l'usage du NFC en Afrique francophone, la phrase sur ton public doit venir de toi (question n° 1).

### 9. Petits points

- **La parenthèse ByteMonk** : « La doc de Google pour les développeurs dit le contraire : il est stocké sur l'appareil. » La doc dit bien « stocké sur l'appareil », mais elle ne parle pas de « l'appli en redemande un à chaque paiement » : « le contraire » est trop fort. Et elle corrige une vidéo anglaise que le public français n'a sans doute pas vue. Coupée (en réserve, reformulée).
- **« Et voilà pourquoi le titre dit « téléphone » »** : une phrase méta. Le hook a déjà fait ce travail. Coupée.
- **« Et souvent, en NFC, le terminal ajoute son grain de sel »** : Apple écrit que ça dépend du réseau (fait 13). Corrigé : « selon le réseau de ta carte ».
- **« La norme, elle, certifie cinq millimètres »** : c'est la portée certifiée par le NFC Forum (fait 6), pas « la norme ». Passé dans le bandeau des devs avec les 13,56 MHz : une phrase technique de moins dans la section 1.
- **L'écran de fin** : « comment Google sait en une milliseconde que ton pseudo est déjà pris ». La fiche du pseudo a retiré Google et « une milliseconde » le 23/10 (aucune source). Corrigé : « comment un site sait tout de suite que ton pseudo est déjà pris ».
- **Le mode Express d'Apple** (cartes de transport) : Apple propose un mode qui paie sans authentification ; ce n'est ni vérifié ici ni dans `sources.md`. Le script dit bien « c'est la règle d'Apple » : rien à changer, mais n'improvise pas « jamais sans ton visage » à la prise.

## Les tics d'IA

Cinq, tous légers :

| Passage | Tic | Correction |
|---|---|---|
| « ni au terminal, ni au magasin, ni à son réseau » | rafale de trois | supprimée (correction n° 2) |
| « Voilà le génie caché derrière ton bip. » (après une phrase-bilan) | petite morale de fin | gardée, mais suivie d'un vrai retournement (n° 2) |
| « Et voilà pourquoi le titre dit « téléphone » » | phrase méta | coupée |
| « Le téléphone ramassé dans la rue, tu te rappelles ? Voilà ce qui arrive quand quelqu'un teste vraiment la règle. » | annonce qui dramatise | remplacée par le fait (n° 1) |
| « Sauf que tout le monde paie comme ça. » | liaison sans retournement | « Prends la France, parce qu'on y a les chiffres » |

Pas de fausse opposition gratuite. Les deux « pas » qui restent sont de vraies précisions : « pas spécialement sur le sans contact » (la portée de l'étude) et « pas un article relu par d'autres chercheurs » (la valeur de la source). À garder.

## La rétention

- **Relances** : 29 dans le V1, une toutes les 22 s. Le seul trou dépasse un peu 45 s, au milieu de la section 3 (plafonds, 2020, Google) ; la V2 le comble avec la graine « il prévient le terminal » et la coupe de 2020.
- **Ponts** : chaque section finit sur une question (« si quelqu'un va chercher ce jeton ? », « le plus malin des trois », « Et les autres ? »). Rien à changer.
- **Abonnement vers 25 %** : à 2:50 (26 %), juste après la surprise « Apple ne peut pas le déchiffrer », le cadenas à l'écran. Bon placement. La phrase est un peu générique, mais elle reprend la promesse de la chaîne ; on la garde.
- **Relance vers 60 %** : le V1 en a deux, la musique coupée et le pirate au magnétophone (63 %), puis « on essaie de tout casser » (73 %). Elles sont bonnes : la première relance la tension avant la réponse au hook, la seconde change de ton juste après. Dans la V2, avec 1 860 mots, elles tombent à 57 % et 69 %. La réponse au hook arrive vers 7:35 (67 %) et « Et les autres ? » relance aussitôt.
- **Les 15 et 30 premières secondes** : voir plus haut ; la V2 garde la structure et précise la preuve.

## Ce qu'il faut garder

- « Pour le comprendre, il faut d'abord écouter ta carte. Parce qu'elle est bavarde. » Le pont parfait : inattendu, court, il ouvre une question.
- Les trois cartes à jouer face cachée, retournées une par une. C'est la carte du trajet de la vidéo, comme les trois étapes d'Uber.
- « Ouais, t'as bien entendu : du Java, dans ton iPhone. » La réaction après le fait, exactement ce que fait Cam.
- Le ticket de métro composté, et le portique qui fait « pouet » en section 5 : une image qui revient avec un nouveau sens.
- Le speedrunner qui connaît la seed : ton registre gamer, et la meilleure explication du pre-play qu'on puisse faire en une phrase.
- « Bon, c'est un livre blanc de chercheurs en sécurité, pas un article relu par d'autres chercheurs. Mais ça calme. » Dire la valeur de sa source rend tout le reste crédible.
- La question « est-ce qu'il faut payer avec ton téléphone parce que c'est moins fraudé ? » et sa réponse honnête (9 € des deux côtés, plus fraudé en 2023 et 2024). C'est ce que les vidéos américaines font croire, et c'est faux.

## Vérification des faits du script

Chaque affirmation de la voix off du V1, comparée à `sources.md`. ✅ = conforme ; ⚠️ = juste mais à reformuler ; ❌ = faux ou non tenu par la source. Les faits 32 à 41 ont été ajoutés à `sources.md` pendant ce grill (« ajouté au grill, vérifié le 23/10/2026 »).

| Section | Phrase du V1 | Verdict | Fait | Ce que fait la V2 |
|---|---|---|---|---|
| Hook | « ta carte vient de donner ton vrai numéro » | ✅ | 19 | gardée |
| Hook | « Des chercheurs l'ont lu avec un simple téléphone Android » | ✅ | 19, 36 | + « la carte encore rangée dans un portefeuille » |
| Hook | « ton téléphone… ne donne jamais ce numéro au magasin. Il envoie un faux. » | ✅ | 11, 15 | gardée |
| 1 | « treize virgule cinquante-six mégahertz », « jusqu'à deux centimètres » | ✅ | 6, 7 | MHz passés en bandeau |
| 1 | « La norme, elle, certifie cinq millimètres » | ⚠️ c'est la portée certifiée par le NFC Forum | 6 | en bandeau, bien formulée |
| 1 | « un code calculé pour ce paiement, un compteur… et ton numéro de carte » | ✅ | 19 | gardée |
| 1 | « En 2014… Newcastle… la carte au fond d'une poche » | ❌ le papier dit « dans un portefeuille en cuir » | 36 | « à travers un portefeuille en cuir », « en moins d'une demi-seconde » |
| 1 | Black Hat 2019 : « le code, le compteur, et le numéro » | ✅ | 19 | gardée |
| 1 | « la donnée la plus précieuse de ta carte… EMVCo, l'organisme derrière les normes des cartes à puce » | ⚠️ absent de `sources.md` (le fait 14 ne citait pas « most valuable ») ; vérifié | 32, 33 | « la donnée qui a le plus de valeur pour un fraudeur » ; « l'organisme qui gère les normes des cartes à puce, et il appartient à Visa, Mastercard et quatre autres réseaux » |
| 1 | « soixante-douze pour cent… presque un sur cinq » | ✅ | 28 | gardée |
| 1 | « cent vingt-quatre euros… Posée sur un terminal sans contact : neuf euros » | ⚠️ le 9 € compte aussi les téléphones | 27 | « En magasin, en sans contact : neuf euros » |
| 1 | (absent) le mécanisme vaut hors de France | ajouté, vérifié | 32, 35 | « le principal système de paiement par carte dans le monde » |
| 2 | « c'est le seul moment où ton vrai numéro sert » | ⚠️ trop fort : la banque relie le jeton à ton compte | 31, 33 | « C'est là que ton vrai numéro sert : une fois, pour fabriquer le faux » |
| 2 | « ta banque crée… le chiffre… Apple ne peut pas le déchiffrer », « le DAN » | ✅ | 10 | gardée |
| 2 | Google : « un numéro unique est stocké sur le téléphone » | ✅ | 15 | gardée |
| 2 | « La doc de Google… dit le contraire : il est stocké sur l'appareil » | ⚠️ « le contraire » trop fort | 15, 24 | coupée (réserve reformulée) |
| 2 | « ni Apple ni ton téléphone ne le donnent au commerçant » ; « tokenisation » | ✅ | 11, 14 | gardée |
| 2 | « Moi, en dev, mon premier réflexe… » | ⚠️ opinion de l'auteur non donnée | – | crochet |
| 2 | « son usage est limité… un commerçant, un appareil, ou un type de paiement » ; « il vaut moins » | ✅ | 14, 33 | gardée, au plus près d'EMVCo |
| 2 | (absent) qui reconnaît le jeton | ajouté | 10, 33 | « le serveur qui sait qui se cache derrière, c'est ta banque. Chez Apple, c'est même elle qui l'a fabriqué » |
| 3 | « une puce à part, certifiée… Java Card » | ✅ | 8 | gardée |
| 3 | « évaluation de sécurité d'EMVCo… Critères Communs » | ✅ | 8 | coupée (densité) |
| 3 | DAN stockés dans la puce, serveurs, contrôleur NFC | ✅ | 9 | gardée, raccourcie |
| 3 | « aucune information de paiement ne part sans que tu te sois authentifié » (visage, doigt, code, montre) | ✅ | 12 | gardée, dite comme la règle d'Apple |
| 3 | « le feu vert de la Secure Enclave » | ⚠️ juste, mais jamais expliquée ; vérifié | 12, 34 | + « une zone à part dans la puce principale du téléphone, isolée du processeur, qui garde entre autres les données de ton visage » |
| 3 | « cinquante euros maximum, sans code » ; plafond cumulé, nombre de paiements | ✅ | 1, 2 | gardée, raccourcie |
| 3 | « dépasser les cinquante euros sans taper ton code » | ✅ | 5 | gardée |
| 3 | « ce coffre change même les plafonds » | ⚠️ c'est la vérification, pas la puce | 37 | « ce feu vert change même les plafonds » |
| 3 | « le code, ton téléphone l'a déjà remplacé par ton visage » | ⚠️ notre lecture de service-public dans le V1 ; maintenant sourcée | 5, 37 | « Pourquoi ? Service-public ne le dit pas. Les deux chercheurs de Black Hat, eux, l'expliquent… » |
| 3 | « Jusqu'au 11 mai 2020, c'était trente » ; « les banques françaises, Visa et Mastercard » ; « geste barrière » | ⚠️ seconde main (FBF et GCB d'après La finance pour tous ; l'INC confirme la date et le « geste barrière » du ministère) | 3, 29, 41 | en réserve |
| 3 | Google : « c'est le téléphone qui garde la clé » | ✅ | 22 | « la doc pour les banques dit que… » ; plus d'argument d'absence (« ne parle pas d'élément sécurisé ») |
| 4 | « une clé et un compteur, qui avance à chaque paiement » | ✅ | 13, 16 | gardée |
| 4 | « souvent, en NFC… un nombre imprévisible » | ⚠️ Apple dit « selon le réseau » | 13 | « selon le réseau de ta carte » |
| 4 | « une banque bien faite refuse un compteur qu'elle a déjà vu » | ✅ (formulation du fait 16) | 16 | gardée |
| 4 | « ta carte le joue aussi… avec ton vrai numéro » | ✅ | 19 | + « c'est la puce de ta carte qui le fabrique » (la carte « signe la transaction avec un cryptogramme ») |
| 5 | Cambridge 2012, cinq chercheurs, Ross Anderson | ✅ ; affiliation absente de la page arXiv, confirmée par Galloway et Yunusov | 17, 35 | gardée |
| 5 | compteur ou heure, pre-play, clonage, distributeurs et terminaux à puce | ✅ | 17 | gardée |
| 5 | « contourner [les plafonds], y compris sur des portefeuilles mobiles, avec le téléphone verrouillé » + « Le téléphone ramassé dans la rue, tu te rappelles ? » | ❌ dans l'enchaînement : c'était Google Pay avec des cartes Visa, pas la règle d'Apple | 30, 39 | « avec Google Pay et une carte Visa… Sur Apple Pay, leur document ne montre rien de pareil » |
| 5 | « des banques ne refusent pas un compteur plus bas que le dernier » | ✅ | 16 | chiffrée : 18 cartes sur 31, terminal trafiqué (fait 40) |
| 5 | « Le ticket composté, certaines le laissent passer » | ⚠️ vrai avec un terminal trafiqué, non dit | 40 | « Ils trafiquent leur propre terminal… plus d'une carte sur deux le laisse passer » |
| 5 | (absent) la carte déguisée en téléphone | ajouté | 37, 38 | « sur douze cartes Visa, dix passent au-dessus du plafond sans aucune vérification, jusqu'à cent livres » |
| 5 | « un livre blanc… pas un article relu » | ✅ | 18 | gardée |
| 5 | « neuf euros… exactement comme l'ensemble du sans contact » ; « vingt et un… seize, contre onze » | ✅ | 27 | gardée |
| 6 | « ne te demande pas de faire confiance au terminal, ni au magasin, ni à son réseau » | ❌ contredit par la section 5 | 17, 38, 40 | retournement : « il reste quelqu'un à qui le système doit faire confiance : le terminal » |
| 6 | « ne vaille presque rien » | ⚠️ EMVCo : « réduit la valeur » | 14, 33 | « vaut moins » |
| 6 | « comment Google sait en une milliseconde que ton pseudo est déjà pris » | ❌ non sourcé (fiche du pseudo, 23/10) | – | « comment un site sait tout de suite » |

**Ce que j'ai corrigé, en bref** : Newcastle (portefeuille, pas poche) ; EMVCo sourcé ; « le seul moment où ton vrai numéro sert » ; « le contraire » de ByteMonk (coupé) ; la Secure Enclave expliquée ; « ce coffre change les plafonds » ; le visage qui remplace le code, désormais sourcé ; « souvent » → « selon le réseau » ; le téléphone verrouillé attribué à Google Pay ; le ticket composté chiffré et conditionné ; la fin ; « presque rien » ; l'écran de fin. **Retiré** : la correction de ByteMonk, les certifications, l'anecdote de 2020 (en réserve). **Ajouté** : faits 32 à 41 de `sources.md` (EMVCo, Secure Enclave, EMV mondial, Newcastle en détail, CDCVM, les trois résultats de Black Hat 2019, le plafond de 2020 à l'INC).

Aucun conseil de sécurité dans le V1 ni dans la V2 (pas d'étui, pas de « désactive le NFC ») : aucune source n'en mesure l'effet. C'est à garder ainsi.

## Plan d'action (appliqué dans `script.md`)

1. **Section 5** : réattribuer le téléphone verrouillé à Google Pay, chiffrer le ticket composté, ajouter la carte déguisée en téléphone (n° 1).
2. **Section 3** : sourcer le visage qui remplace le code, expliquer la Secure Enclave, couper les certifications et 2020 (n° 3 et 6).
3. **Fin** : retourner sur le terminal comme maillon de confiance (n° 2).
4. **Section 2 et réponse au hook** : la banque qui sait relier le jeton à ton compte (n° 4).
5. **Passe de détail** : la question des 9 € (n° 5), le hook (portefeuille, question centrale), le crochet de ton public et la phrase sur EMV (n° 8), les petits points (n° 9).

## Les questions

Elles sont dans « Questions pour l'auteur », en bas de `script.md`. La plus importante pour le script : **ton public africain paie-t-il en sans contact ?** Ta phrase au crochet de la section 1 décide si la vidéo parle à 63 % de tes spectateurs ou seulement aux 36 % de France.
