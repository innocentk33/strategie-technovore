# Abonnement ou IA locale ? #1 : 16 Go suffisent : script V2

**Titre retenu (05/11)** : *16 Go de VRAM suffisent (si tu prends le bon fichier)*.

**Sortie** : lun. 9 nov. 2026, 18 h. Vidéo **calculée** : aucun banc d'essai, que des mesures publiées (faits `Sx` de [`sources.md`](sources.md), vérifiés le 05/11/2026) et une impression à toi, sans chiffre (`fiche.md`, essais rapides d'avant le 25/10). V1 : [`script-v1.md`](script-v1.md) ; critique : [`grill-v1.md`](grill-v1.md).

## Changements depuis la V1 (05/11)

1. **Le hook montre le contraste au lieu de livrer le verdict** : ta carte, ton impression (« il m'a paru super lent »), puis 101 contre 13 sur la même carte. La question centrale arrive à 0:15, le verdict seulement à la fin.
2. **Ton Qwen lent devient le fil rouge** : planté dans le hook, rappelé en section 1, récolté à la fin.
3. **Les faits recollés à sources.md** : le 101 vient d'un fichier Q3 d'Unsloth (carte remplie à 15 Go sur 16), plus du fichier ISTA de 11,8 Go ; les 45 tok/s de Kai sont des chiffres de possesseurs de 5060 Ti qu'il relaie ; Terminal Bench 2.1, où Opus 4.6 reste devant, est dit à voix haute ; HN et Samayas sont des paraphrases annoncées comme telles.
4. **Plus aucun genre supposé** : « quelqu'un », « la personne qui a publié la mesure ».
5. **Les tics coupés** : 3 « attention », 13 « donc » (dont 6 en tête de conclusion), 9 « ce n'est pas / c'est pas » ramenés à 2, le « Cent un ! / Soixante-dix ! / Six contre quarante-six ! » répété trois fois.
6. **Nouveau** : la quantization en deux phrases (le JPEG de l'IA, contenu 3 de la fiche) ; ton choix final en crochet, rien n'est écrit à ta place.

**Titre** (garde l'idée « 16 Go suffisent ») :
1. **16 Go de VRAM suffisent (si tu prends le bon fichier)** : la promesse que le hook confirme tout de suite (101 contre 13), recommandé.
2. **16 Go de VRAM suffisent (mais pas la RAM)** : le titre de la V1. Tenu par la section 2, et le hook le pose dans sa dernière phrase. Moins juste pour le 27B, où la RAM ne joue presque aucun rôle.

**Miniature** : la carte en gros plan, « 16 Go » en gros. La vidéo commence sur cette scène.

**Texte et sous-texte** :
- **Texte** : 16 Go suffisent pour un vrai modèle, à condition de choisir le fichier qui rentre ; au-delà, c'est la RAM qui décide.
- **Sous-texte** : le chiffre affiché sur la boîte compte moins que ce que tu mets dedans. Montré par ton Qwen lent, jamais dit.

**Boucles ouvertes** :
1. « Seize gigas, ça suffit ou pas ? » (0:15) → tenue section par section, verdict à la fin.
2. « Mon Qwen m'a paru super lent » (0:05) → rappelée en section 1, récoltée à la fin.
3. « Au-delà, c'est ta RAM qui décide » (0:30) → tenue en section 2.
4. « Ça a l'air trop beau » (fin de section 2) → le prix, section 3.
5. « Est-ce que ça vaut ton abonnement ? » (fin de section 3) → section 4.

**Conventions** : texte normal = voix off ; `[VISUEL]`, `[SON]` = montage ; `(Sx)` = fait de `sources.md`, ne se lit pas ; `⟦à écrire⟧` = tes mots, rien n'est écrit à ta place ; `[À REVÉRIFIER]` = à relever le jour de la voix. Nombres en lettres pour la lecture. Timecodes à ~145 mots/min (1 657 mots dits, environ 11 min 25), à recaler sur la voix.

---

## 0. Hook (0:00 - 0:36) · objectif : 75 % à 0:15, 50 % à 1:00

[VISUEL : plan fixe sur ta RTX 5080, gros plan, fond noir, « 16 Go » en vert menthe sur la carte : la scène de la miniature. Pas de logo, pas de visage, aucun titre.]
[SON : un seul coup de basse, puis le souffle des ventilateurs.]

Cette carte, c'est la mienne : seize gigas. Et dessus, Qwen, un vrai modèle de vingt-sept milliards, m'a paru super lent.

[VISUEL : « 101 tok/s » s'écrit à côté de la carte, en vert. En petit : « RTX 5080, sudoingX, relevé le 05/11/2026 » (S18).]

Sauf que quelqu'un, avec la même carte et le même modèle, a publié cent un tokens par seconde.

[VISUEL : le « 101 » tombe et devient « 13 » en rouge. En petit : « RTX 5080, Hardware IA, 01/09/2026 » (S21).]
[SON : un « bip » qui descend.]

Une autre mesure, sur une 5080 aussi : treize.

[VISUEL : retour sur la carte. Petit tampon « calculé, pas testé » en bas à droite.]

Du coup, seize gigas, ça suffit ou pas ? J'ai fait aucun banc d'essai, j'ai rassemblé les mesures publiées. Et entre cent un et treize, il y a un fichier qui rentre, et un qui déborde.

[VISUEL : derrière la carte, une barre « RAM 32 Go » s'allume en gris.]

Et au-delà, c'est ta RAM qui décide.

---

## 1. Un fichier qui rentre, un fichier qui déborde (0:36 - 3:40)

[VISUEL : une photo nette qui devient un JPEG de plus en plus compressé ; en dessous, « 16 bits → 4 bits → 3 bits » et la taille du fichier qui fond.]

Bon, d'abord, pourquoi un même modèle peut avoir plusieurs fichiers. En gros, c'est le JPEG de l'IA : on garde moins de bits par paramètre, le fichier devient plus léger, et on perd un peu de qualité. On appelle ça la quantization.

[VISUEL : jauge VRAM de 16 Go ; un bloc « Qwen3.8-27B, 3 bits » s'y glisse. Puis la capture du README sudoingX/qwen38-mtp, la ligne « RTX 5080 16GB », 53,4 → 101,3 surlignés. Légende : « une seule mesure, Q3_K_M d'Unsloth, llama.cpp, 15 Go de VRAM utilisés sur 16 » (S18).]

Et en trois bits, notre Qwen de vingt-sept milliards rentre en entier dans seize gigas. La mesure à cent un, elle vient de là : sur une 5080, avec un fichier trois bits, la carte remplie à quinze gigas sur seize. Sans réglage, la personne qui l'a publiée mesure cinquante-trois tokens par seconde. Et avec la prédiction multi-tokens, le MTP, le modèle devine plusieurs mots d'avance, et ça monte à cent un. En gros, il écrit bien plus vite que tu ne lis. Par contre, c'est une seule mesure.

[VISUEL : deux petites cartes qui s'empilent : « 5060 Ti 16 Go : 45 tok/s, chiffres de possesseurs relayés par Kai » (S20) ; « portable RTX 3080 16 Go : 20-30 tok/s, Autodidacts » (S22).]

Donc je suis allé voir ailleurs. Kai, sur YouTube, relaie des possesseurs de 5060 Ti qui annoncent quarante-cinq tokens par seconde. Et sur un portable avec une 3080 de seize gigas, Autodidacts mesure vingt à trente. Pas les mêmes cartes, pas les mêmes fichiers, mais tout le monde raconte la même histoire : un 27B en trois bits, sur seize gigas, ça tourne bien.

[VISUEL : barre « Q4_K_M : 17 Go » qui déborde de la jauge, rouge (S19, S20), puis « 13 tok/s » (S21).]

Et le treize, alors ? Là, on passe en quatre bits. Le Q4, celui qu'on te propose souvent par défaut, fait dix-sept gigas. Il rentre pas dans la carte. Du coup, une partie du modèle part dans la RAM, et la vitesse s'effondre : Hardware IA mesure treize tokens par seconde sur une 5080, dans LM Studio, avec un Q4 d'après ses chapitres. Ce sont pas les mêmes réglages que pour le cent un, donc je fais pas de soustraction. Mais tu vois le problème : un fichier de trop, et une carte à mille cinq cents euros rame comme une vieille tour.

[VISUEL : un fichier de 11,8 Go à gauche (S33), 17 Go à droite, avec un panneau « tient / ne tient pas ». Ta carte en vignette dans un coin, avec un point d'interrogation.]

Et là, tu dois te demander si c'est ce qui est arrivé à mon Qwen. On y revient à la fin, parce qu'il manque encore une pièce.

[VISUEL : la ligne « 64 Ko par token » ; « 128 000 tokens = 8 Go » grossit dans la jauge, par-dessus le modèle (S20).]

Cette pièce, c'est la mémoire de la conversation. Chaque token que le modèle garde en tête prend de la place dans ta carte : soixante-quatre kilo-octets, d'après Kai. Ça a l'air de rien. Sauf que pour cent vingt-huit mille tokens, ça fait huit gigas de plus. Donc ton vrai plafond, sur seize gigas, c'est la longueur de la conversation. Kai passe quand même de quarante-sept mille à cent dix mille tokens avec deux réglages : la vision coupée, et ce cache en huit bits.

[VISUEL : la jauge se remplit : modèle + contexte. Puis schéma RAM 32 Go en gris, « presque inutile ici ».]

La règle pour le 27B, c'est donc : le fichier qui rentre, avec de la place pour la conversation. Et ta RAM, là-dedans ? En fait, pour ce modèle, elle sert presque à rien : tout vit dans la carte. Retiens ça, parce que ça va s'inverser.

---

## 2. Le modèle de 125 milliards, et le vrai verrou (3:40 - 6:40)

[VISUEL : l'icône Strata, puis « 125 milliards de paramètres, dont 6 travaillent à chaque mot » (S4).]

Parce qu'il existe un autre Qwen, bien plus gros : Qwen3.8 Flash-Next. Cent vingt-cinq milliards de paramètres. En fait, il est découpé en centaines de petits spécialistes, des experts, et à chaque mot, il n'en réveille que quelques-uns : environ six milliards de paramètres au travail. Et un projet sorti fin septembre, Strata, le fait tourner sur un PC de joueur.

[VISUEL : schéma en trois étages : GPU 16 Go / RAM / SSD. Les experts descendent en cascade (S2).]

Son astuce : les experts qui servent le plus restent dans la carte, les autres vont dans la RAM, et une grosse table reste sur le SSD. Sauf que du coup, tout s'inverse. La doc de Strata donne la règle : ta RAM doit contenir les experts, plus environ dix gigas pour Windows et le reste (S2).

[VISUEL : tableau qui s'écrit ligne par ligne : Q2_0 = 34 + 10 = 44 Go ; IQ3_S = 50 + 10 = 60 Go. Barres rouges au-dessus de « 32 Go ».]

Fais le calcul avec moi. Le plus petit fichier du modèle complet, c'est trente-quatre gigas d'experts. Plus dix : quarante-quatre. Le plus soigné, cinquante plus dix : soixante. Et moi, j'ai trente-deux gigas de RAM. Donc le modèle complet, chez moi, c'est non. Et une plus grosse carte le rendrait plus rapide, mais d'après la doc, elle baisse pas la RAM qu'il faut (S3).

[VISUEL : ligne « With 32 GB, take the Coder » encadrée, source MODELS.md (S3), traduite en dessous.]

Par contre, la doc a une réponse pour trente-deux gigas : prends le Coder. C'est une version réduite, choisie pour le code, qui garde deux cent cinquante-six experts sur cinq cent douze (S6). Vingt-trois gigas d'experts, plus dix : trente-trois.

[VISUEL : jauge RAM : « 33,5 Go visibles sous Windows », le bloc « Coder 23 Go » + « Windows 10 Go » la remplit à ras. En gros : « calcul, pas une mesure » (S8).]

Et là, c'est serré. Trente-deux gigas de DDR5, Windows t'en laisse voir environ trente-trois virgule cinq. Moins vingt-trois, il reste dix et demi. Pile la marge demandée, à un giga près. Résultat : ça passe, mais à ras, navigateur fermé. Et ça, c'est un calcul.

[VISUEL : la capture du ticket #4997, « Ryzen 7 9700X, 5070 Ti 16 Gio, 31,2 Gio de RAM », puis 70,4 et 78,7 tok/s (S9).]

Sauf que quelqu'un l'a mesuré, sur GitHub, avec presque ma config : le même Ryzen 7 9700X, une RTX 5070 Ti de seize gigas, trente et un gigas de RAM visibles. Avec le Coder : soixante-dix tokens par seconde en chat court, et presque soixante-dix-neuf dans une session d'agent. Un modèle de cent vingt-cinq milliards, à cette vitesse, sur un PC de joueur. Sur le papier, c'est dingue.

[VISUEL : zoom sur la ligne « Speed only: no correctness check was run », traduite : « vitesse seulement, aucun test de justesse ».]

Mais en tête du ticket, la personne l'écrit elle-même : vitesse seulement, aucun test de justesse. On sait que ça va vite, on sait pas si c'est bon. Et c'est une 5070 Ti. La 5080 devrait faire au moins aussi bien, mais personne l'a mesurée avec trente-deux gigas de RAM.

[VISUEL : deux tickets #5115 et #5237, « RTX 5080 », avec « 64 Go » et « 96 Go » entourés en rouge (S11, S12).]

D'ailleurs, si tu tombes sur des 5080 à cent quatorze ou cent six tokens par seconde sous Strata, regarde la RAM : soixante-quatre gigas chez l'un, quatre-vingt-seize chez l'autre. C'est une autre machine que la tienne.

[VISUEL : retour sur « 70 tok/s », qui clignote, puis une étiquette de prix vide accrochée dessus.]

Soixante-dix tokens par seconde, avec trente-deux gigas. Ça a l'air trop beau. Et en effet, il y a un prix.

---

## 3. Le prix à payer (6:40 - 9:00)

[VISUEL : panneau « Le prix du Coder », trois lignes qui se remplissent : qualité, langue, confort.]

D'abord, la qualité. Pour tenir dans ta RAM, le Coder descend à un virgule quatre-vingt-neuf bit par paramètre. Ses auteurs annoncent quatre-vingt-quinze pour cent du score de code du modèle complet (S6, S7). Sauf que c'est leur chiffre, mesuré par eux, sur du code en anglais.

[VISUEL : deux bulles, chacune marquée « en substance » : HN (S17) ; Samayas, RTX 5090, « The Coder variant failed to complete the task » en petit (S35).]

Du coup, je suis allé voir ce qu'en disent les autres. Sur Hacker News, quelqu'un le trouve, en substance, moins bon, avec une perte qui se sent, et conseille le modèle normal. Et dans un test de la chaîne Samayas, avec Claude Code sur une RTX 5090, le Coder n'a pas réussi à finir la tâche. Samayas précise que c'est pas un test universel. Mais ça fait un échec documenté, et aucune vérification indépendante de ces quatre-vingt-quinze pour cent.

[VISUEL : une ligne de MODELS.md, « weaker outside code and in languages other than English and CJK », traduite (S6).]

Et pour toi, il y a un détail en plus : d'après la doc de Strata, il est plus faible hors du code et dans les langues autres que l'anglais, le chinois, le japonais et le coréen. Le français en fait partie. Donc pour écrire ou discuter en français, c'est pas lui qu'il te faut.

[VISUEL : « souris figée quelques minutes au premier lancement » (S15) ; « créé le 24/09/2026, plus de 1 300 tickets et demandes ouverts » (S1) ; « −25 % entre deux moteurs, RTX 5080 » (S11).]

Ensuite, le confort. D'après sa doc, au premier lancement, Strata charge trente-cinq à cinquante-cinq gigas dans ta RAM, et ta souris peut se figer quelques minutes. Le projet a six semaines, avec plus de mille trois cents tickets et demandes ouverts. Et entre deux versions du moteur, une personne avec une 5080 a perdu vingt-cinq pour cent de vitesse. Bref, c'est impressionnant, mais ça bouge encore beaucoup.

[VISUEL : retour aux deux fichiers : « 27B, 3 bits, tout dans la carte » / « Coder, 33 Go, RAM à ras » / « Flash-Next complet : 48-64 Go de RAM » (S3).]

Voilà où on en est. Le 27B, oui, dans la carte, sans rien demander à ta RAM. Le Coder, oui, avec trente-deux gigas à ras, et ce prix-là. Le modèle complet, lui, veut quarante-huit à soixante-quatre gigas de RAM.

[VISUEL : capture du kit de 32 Go à 92,95 € (2025), puis la même référence à 560 € sur Amazon. Date du relevé en petit. [À REVÉRIFIER LE JOUR DE LA VOIX]]

Et si tu te dis « bah, je rajoute de la RAM » : mes trente-deux gigas, je les ai payés quatre-vingt-treize euros en 2025. Le même kit, aujourd'hui, il est à cinq cent soixante euros sur Amazon. Ouais, six fois le prix.

[VISUEL : la carte d'un côté, le logo de Claude de l'autre, un « ? » au centre.]

Bon. Admettons que ça tourne chez toi. Est-ce que ça vaut ton abonnement ?

---

## 4. Et Claude, dans tout ça ? (9:00 - 10:00)

[VISUEL : tableau Qwen3.8-27B contre Opus 4.6 : SWE-bench Pro 61,7 / 53,4 en vert ; Terminal Bench 2.1 73,0 / 78,2 en rouge ; source « fiche de Qwen, 05/08/2026, modèle complet » (S29).]

Sur les tableaux de Qwen, le 27B bat l'ancien Opus 4.6 en code sur SWE-bench Pro : soixante et un virgule sept contre cinquante-trois virgule quatre. Mais sur Terminal Bench, Opus reste devant. Et surtout, c'est le modèle complet, avec les réglages de Qwen : c'est pas le fichier trois bits qui tient dans ta carte.

[VISUEL : le benchmark indépendant, « Terminal-Bench 4.0 : 6 % contre 46 % » en gros, Artificial Analysis, indice v5.0.1 (S31).]

Alors je suis allé chercher une mesure indépendante. Artificial Analysis compare ce même 27B à Claude Opus 5, en agent dans un terminal : six pour cent de réussite contre quarante-six. Ouais, t'as bien entendu. Six. Donc pour coder en agent sur un vrai projet, Claude est loin devant.

[VISUEL : deux colonnes « Local » / « Abonnement ». Local : « tes données restent chez toi », « marche sans internet », « rien à payer chaque mois ». Abonnement : « le meilleur modèle », « rien à installer ».]

Du coup, voilà comment je le lis. Ton modèle de seize gigas, c'est un très bon plan B : tes données restent chez toi, il marche sans internet, et t'as rien à payer chaque mois. Pour le code sérieux en agent, l'abonnement garde l'avantage.

---

## 5. Verdict et suite (10:00 - 11:25)

[VISUEL : ta carte en gros plan, comme au début. Le fichier « 14,25 Go, 4 bits » se glisse dans la jauge de 16 Go et la remplit presque. Il reste un mince filet vert : « moins de 2 Go pour la conversation et l'écran ».]

Et mon Qwen qui me paraissait super lent, alors ? J'avais pris un fichier quatre bits de quatorze gigas. Il rentre dans la carte, mais à ras : il reste moins de deux gigas pour la conversation, et pour l'écran si ton écran est branché sur la carte. D'après le calcul, il était sûrement trop juste. Et en plus, par défaut, ce Qwen réfléchit longtemps avant d'écrire sa réponse. Bref, j'avais exactement le problème de cette vidéo, et c'était pas la carte.

[VISUEL : récap en trois lignes sur fond sombre : « 27B en 3 bits : tient en 16 Go » / « Coder : 32 Go de RAM, à ras » / « Flash-Next complet : 48-64 Go de RAM ».]

Donc oui, seize gigas suffisent. Pour un vrai modèle de vingt-sept milliards, si tu prends le fichier qui rentre et que tu lui laisses de la place. Pour aller plus gros, c'est ta RAM qui décide, plus la carte. Et pour le code en agent, Claude reste devant.

[VISUEL : plan sur toi ou sur ton bureau.]

Moi, ⟦à écrire : ce que tu gardes, ce que tu fais tourner sur ta carte, avec tes mots⟧.

[VISUEL : carte YouTube vers la vidéo d'installation (2 nov.).]

Si t'as jamais installé d'IA chez toi, j'ai une vidéo qui le fait pas à pas : je te la mets là.

[VISUEL : carte YouTube vers « comment lire le nom d'un modèle » (16 nov.), ajoutée à la sortie. Écran de fin : la vidéo suivante de la playlist « Abonnement ou IA locale ? ».]

Et si tous ces noms, Q4, IQ3_S, Coder, te donnent mal à la tête : la semaine prochaine, je t'apprends à lire le nom d'un modèle. En attendant, dis-moi en commentaire ta carte et ta RAM, et je te dis ce qui tient chez toi.

---

## Faits utilisés

| Dit dans le script | Faits |
|---|---|
| Ton Qwen « super lent » ; fichier 4 bits de 14,25 Go ; moins de 2 Go restants ; réflexion activée par défaut | `fiche.md` (essais d'avant le 25/10, impression sans chiffre ; causes « possibles », d'où « sûrement ») |
| 101 tok/s sur 5080 (53 sans MTP), Q3_K_M d'Unsloth, 15 Go de VRAM utilisés, une seule mesure | S18 |
| 13 tok/s sur 5080, LM Studio, Q4 d'après les chapitres, 1 500 € | S21 |
| 27B en 3 bits : 11,8 Go chez ISTA | S33 |
| 45 tok/s sur 5060 Ti (chiffres de possesseurs, relayés par Kai) ; portable 3080 16 Go 20-30 | S20, S22 |
| Q4_K_M 17 Go ne tient pas | S19, S20 |
| 64 Ko/token, 128K = 8 Go ; 47 000 → 110 000 | S20 |
| 125 B dont ~6 actifs ; GPU / RAM / SSD ; experts + ~10 Go | S2, S4 |
| Q2_0 44 Go, IQ3_S 60 Go ; une plus grosse carte ne baisse pas la RAM ; « avec 32 Go, prends le Coder » ; complet 48-64 Go | S3, S8 |
| Coder 256/512 experts, 23 Go ; 33,5 Go visibles, 10,5 restants (calcul) | S6, S8 |
| 5070 Ti / 9700X / 31,2 Gio : 70,4 et 78,7 tok/s, « speed only » | S9 |
| 5080 à 114 / 106 tok/s avec 64 / 96 Go de RAM | S11, S12 |
| 1,89 bit ; 95 % d'après ses auteurs ; HN et Samayas en paraphrase ; plus faible hors anglais et CJK | S6, S7, S17, S35 |
| Souris figée, 35-55 Go chargés ; 6 semaines, 1 300+ tickets et demandes ; −25 % | S15, S1, S11 |
| SWE-bench Pro 61,7 / 53,4 ; Terminal Bench 2.1 73,0 / 78,2 ; 6 % contre 46 % | S29, S31 |
| RAM 92,95 € → 560 € | `fiche.md` (relevé du 24/10, à revérifier avant la voix) |

**Interdits respectés** : aucun « j'ai testé » ni « sur ma 5080 » avec un chiffre ; ton Qwen lent est une impression, sans tok/s ; le Coder n'est jamais « équivalent » au complet ni à Claude ; le 27B n'est pas « au niveau de Claude » ; la 5070 Ti n'est pas une 5080 ; les 114 tok/s à 64-96 Go ne sont pas mélangés avec ta config ; « 16 Go suffisent » est toujours précisé (fichier qui rentre, ou le Coder avec 32 Go à ras).
