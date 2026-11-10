# Abonnement ou IA locale ? #1 : 16 Go suffisent : script V3

> **08/11 (soir), tes réponses** : la phrase du banc d'essai est retirée (le tampon « calculé, pas testé » suffit) ; ton contexte monté à 64K puis 100K fait du débordement le coupable n° 2, calculé ; ton choix final et l'endroit du réglage de réflexion sont écrits.
>
> **08/11 : corrigé après le [grill de la V3](grill-v3.md)** (hook ramené de 54 à environ 39 s, quatre erreurs de faits, une fausse opposition, Steam déplacé). La V3 d'avant le grill n'est pas gardée : les corrections sont listées dans le grill.

**Titre retenu (05/11)** : *16 Go de VRAM suffisent (si tu prends le bon fichier)*.

**Sortie** : lun. 9 nov. 2026, 18 h. Vidéo **calculée** : aucun banc d'essai, que des mesures publiées (faits `Sx` de [`sources.md`](sources.md) : S1 à S35 vérifiés le 05/11, S36 à S46 ajoutés et revérifiés le 07/11) et une impression à toi, sans chiffre. Versions précédentes : [`script-v1.md`](script-v1.md), [`script-v2.md`](script-v2.md) ; critique de la V1 : [`grill-v1.md`](grill-v1.md).

## Changements depuis la V2 (07/11, tes remarques)

1. **Plus aucun nom de chaîne ni de créateur dans la voix** (ta règle : il faudrait leur autorisation). On dit « un utilisateur relève », « quelqu'un qui a la même carte », « une vidéo espagnole », « un forum de développeurs », « un classement indépendant ». Les noms restent dans `sources.md` et dans la description. À l'écran, la légende dit « source en description ».
2. **Plus d'ouverture « Cette carte, c'est la mienne »** : le hook part des deux mesures, ton impression arrive en troisième phrase.
3. **« Hardware IA » n'était pas une chaîne** : c'est un hashtag. La vidéo du 13 tok/s vient de la chaîne espagnole Globalcobots (1 730 abonnés), et le présentateur dit lui-même qu'une partie du modèle est en RAM (S21 corrigé).
4. **Inspiré de la vidéo de référence** ([kKdhK2zRtto](https://www.youtube.com/watch?v=kKdhK2zRtto), 03/11) : la carte vue comme **un budget en trois lignes** (le fichier, la conversation, l'agent), le piège des gigas (16 Go de carte = 17,18 milliards d'octets), la vitesse = bande passante ÷ taille du fichier, « la mémoire la plus lente donne le rythme ». Les calculs sont refaits avec nos chiffres, sans reprendre ses exemples ni ses phrases.
5. **Ton Qwen lent devient une vraie enquête, avec un indice que tu peux vérifier** : une 5060 Ti fait 25 tok/s avec ton fichier exact (S40), donc ta carte n'était pas en cause. Les deux suspects sont documentés : la réflexion au maximum par défaut (S45) et le pilote NVIDIA qui déborde en silence dans la RAM (S43, S44).
6. **Strata est raccourci** (2 min au lieu de 5) et devient la boucle vers le **16 nov.**, le test filmé de Strata sur ta 5080 : la V2 annonçait encore « le nom d'un modèle » la semaine suivante, ce qui n'est plus vrai depuis le 05/11.
7. **Ajouts tirés des commentaires des vidéos concurrentes** : le contexte (leur question n° 1), « et AMD ? », « et si j'ai 8 ou 12 Go ? » (Steam d'octobre : 8 Go = 26,92 % des joueurs, 16 Go = 26,35 %, 12 Go = 12,91 %).

**Texte et sous-texte** :
- **Texte** : 16 Go suffisent pour un vrai modèle de 27 milliards, à condition de prendre le fichier qui rentre et de compter la conversation et l'agent ; au-delà, c'est la RAM qui décide.
- **Sous-texte** : le chiffre sur la boîte compte moins que ce que tu mets dedans. Montré par ton Qwen lent, jamais dit avant la fin.

**Boucles ouvertes** :
1. « Seize gigas, ça suffit ou pas ? » (0:20) → tenue section par section, verdict à la fin.
2. « À la fin, je te dis ce qui clochait chez moi » (0:30) → récoltée en section 5, avec l'indice de la 5060 Ti planté en section 2.
3. « Ta RAM sert presque à rien… ça va s'inverser » (fin de section 2) → section 3.
4. « Je le lance chez moi la semaine prochaine » (section 3) → vidéo du 16 nov.
5. « Est-ce que ça vaut ton abonnement ? » (fin de section 3) → section 4.

**Conventions** : texte normal = voix off ; `[VISUEL]`, `[SON]` = montage ; `(Sx)` = fait de `sources.md`, ne se lit pas ; `⟦à écrire⟧` = tes mots ; `⟦à vérifier⟧` = une question pour toi avant la voix ; `[À REVÉRIFIER]` = à relever le jour de la voix. Nombres en lettres pour la lecture. Environ 2 000 mots dits, soit 13 min 50 à 145 mots/min (2,2 liaisons pour 100 mots), à recaler sur la voix. Si c'est trop long, coupe d'abord le paragraphe AMD et celui des 8 et 12 Go de la section 2 (environ 40 s).

---

## 0. Hook (0:00 - 0:39) · objectif : 75 % à 0:15, 50 % à 1:00

[VISUEL : une RTX 5080 en gros plan, fond noir, « 16 Go » en vert menthe : la scène de la miniature. Un compteur « tok/s » grimpe à toute vitesse jusqu'à 101. En petit : « RTX 5080, mesure publiée, source en description » (S18).]
[SON : un seul coup de basse, puis le souffle des ventilateurs.]

Sur une RTX 5080, seize gigas, quelqu'un fait tourner Qwen, un vrai modèle de vingt-sept milliards, à cent un tokens par seconde. Plus vite que tu lis.

[VISUEL : le compteur dégringole jusqu'à 13, en rouge (S21).]
[SON : un « bip » qui descend.]

Un autre, même carte, même modèle : treize. Huit fois moins. Et chez moi, ce Qwen-là m'a paru super lent.

[VISUEL : petit tampon « calculé, pas testé » en bas à droite.]

Du coup, seize gigas, ça suffit ou pas ? Entre cent un et treize, la grosse différence, c'est le fichier : un qui rentre, un qui déborde.

[VISUEL : une facture vierge s'imprime à côté de la carte : « 16 Go », trois lignes vides.]

Alors on fait les comptes de ta carte, et à la fin, je te dis ce qui clochait chez moi.

---

## 1. Les comptes de ta carte (0:32 - 4:00)

[VISUEL : la facture se remplit, trois lignes : « le fichier », « la conversation », « l'agent ». Total en bas : « 16 Go ».]

Vois ta carte comme un budget. Trois choses se le partagent : le fichier du modèle, la mémoire de la conversation, et l'agent, si tu codes avec.

### Ligne 1 : le fichier

[VISUEL : une photo nette qui devient un JPEG de plus en plus compressé ; en dessous, « 16 bits → 4 bits → 3 bits » et la taille du fichier qui fond.]

Le même modèle existe en plusieurs fichiers. En gros, c'est le JPEG de l'IA : on garde moins de bits par paramètre, le fichier devient plus léger, et on perd un peu de qualité. On appelle ça la quantization.

[VISUEL : « 16 Go sur la boîte = 17,18 milliards d'octets » ; à côté, « les sites de modèles comptent en milliards tout ronds ». Puis une barre « Windows + écran : ~1 Go » qui mord sur le budget.]

Et là, premier piège : les gigas. Ta carte de seize gigas, en vrai, c'est dix-sept virgule deux milliards d'octets, parce qu'en mémoire on compte par paquets de mille vingt-quatre. Les sites où tu télécharges les modèles, eux, comptent en milliards tout ronds. Donc un fichier de seize gigas et demi, sur le papier, il rentre. Sauf que Windows se sert aussi sur ta carte pour afficher ton écran : compte environ un giga.

[VISUEL : quatre étiquettes « Q4_K_M » de 16,5 à 19 Go qui débordent toutes de la barre rouge (S38). Puis un fichier « 3 bits, 12,1 Go » qui se glisse dedans, avec un filet vert de 4 Go au-dessus.]

Résultat : le Q4_K_M, le quatre bits qu'on te propose le plus souvent, fait entre seize et demi et dix-neuf gigas selon qui le publie. Il passe pas, avant même que t'aies tapé un mot. Il existe des quatre bits plus serrés, vers quatorze gigas : c'est celui que j'avais pris, on en reparle à la fin. Et en trois bits, un fichier soigné fait douze gigas, petit module d'accélération compris. Là, il te reste environ quatre gigas, un peu moins une fois que le moteur s'est servi. Et ces quatre gigas, il faut les partager.

### Ligne 2 : la conversation

[VISUEL : 64 couches empilées ; 16 s'allument (S37). Puis « 16 × 4 × 256 × 2 × 2 = 64 Ko par token ».]

Chaque token que le modèle garde en tête prend de la place dans ta carte. Et pour Qwen, on peut le calculer : sur ses soixante-quatre couches, seules seize gardent vraiment la mémoire de la conversation. Fais la multiplication, et ça donne soixante-quatre kilo-octets par token.

[VISUEL : la ligne « conversation » de la facture : « 8 000 tokens = 0,5 Go » ; « 128 000 tokens = 8 Go », qui explose le budget en rouge ; « 4 Go restants ≈ 60 000 tokens » en vert (S37, S44).]

Ça a l'air de rien. Sauf que huit mille tokens, la valeur par défaut de LM Studio, c'est déjà un demi-giga. Et cent vingt-huit mille, c'est huit gigas : plus que tout ce qui reste. Avec nos quatre gigas, tu tiens environ soixante mille tokens. Et si tu passes cette mémoire en huit bits, un réglage du moteur, tu tiens presque le double.

### Ligne 3 : l'agent

[VISUEL : un terminal de Claude Code ; un compteur « tokens envoyés avant ta question » grimpe jusqu'à « 51 400 » (S46). Puis « ≈ 3,4 Go » qui s'ajoute à la facture.]

Et la troisième ligne, c'est celle que tout le monde oublie : l'agent. Un agent de code comme Claude Code, avant même ta première question, il envoie ses consignes et la liste de tous ses outils. Un utilisateur a relevé plus de cinquante mille tokens au compteur, avant d'avoir tapé quoi que ce soit. Sur notre Qwen, ça fait plus de trois gigas. En fait, c'est le jeu qui te réclame un patch de trois gigas avant même l'écran titre.

[VISUEL : total de la facture, version normale : « 4 Go − 3,4 Go = de quoi tenir 10 000 tokens » en orange ; version cache en 8 bits : « 70 000 tokens » en vert.]

Donc si tu branches un agent sur ta carte, voilà les comptes : avec la mémoire en version normale, il te reste à peine dix mille tokens pour ton vrai travail. Avec la mémoire en huit bits, plus de soixante-dix mille. Ça passe, mais seulement si tu règles ta carte.

---

## 2. Ça va vite comment ? (4:00 - 6:50)

[VISUEL : animation : pour écrire un token, la carte balaie tout le fichier, de haut en bas. Formule : « vitesse max = vitesse de la mémoire ÷ taille du fichier ».]

Bon, ça rentre. Mais ça va vite comment ? Pour écrire un seul token, la carte doit relire tout le modèle. Donc la vitesse max, c'est simple : la vitesse de la mémoire, divisée par la taille du fichier. Une 5080, c'est neuf cent soixante gigas par seconde (S39). Avec un fichier de douze gigas, ton plafond tourne autour de quatre-vingts tokens par seconde.

[VISUEL : une 5060 Ti, le fichier « UD-IQ4_XS, 14,25 Go » ; jauge « plafond 31 » et aiguille « mesuré 24,9 » (S40). Ta carte en vignette dans un coin, un point d'interrogation dessus.]

En vrai, on l'atteint jamais tout à fait. Quelqu'un avec une 5060 Ti a pris un fichier quatre bits de quatorze gigas, exactement celui que j'avais chez moi, et il mesure vingt-cinq tokens par seconde, pour un plafond de trente et un. Environ quatre-vingts pour cent. Garde ce chiffre dans un coin, il va servir.

[VISUEL : la ligne « RTX 5080 16GB » d'un dépôt GitHub, 53,4 → 101,3 surlignés, légende « une seule mesure, fichier 3 bits, source en description » (S18).]

Et le cent un du début ? Sans réglage, la personne qui l'a publié mesure cinquante-trois. Puis elle active le MTP, le petit module d'accélération dont je te parlais : le modèle devine plusieurs mots d'avance, et la carte les vérifie d'un seul coup. Résultat : cent un. Par contre, c'est une seule mesure.

[VISUEL : deux tuyaux : « carte : 960 Go/s », large ; « RAM DDR5 : 96 Go/s », dix fois plus fin (S39). Le flux se bouche au tuyau fin.]

Et maintenant, le treize. Quand le fichier rentre pas, une partie part dans ta RAM. Et la RAM, même en DDR5-6000 comme la mienne, c'est environ quatre-vingt-seize gigas par seconde : dix fois moins que la carte. Et là, la règle est brutale : c'est la mémoire la plus lente qui donne le rythme.

[VISUEL : extrait de la vidéo espagnole, sous-titré, au moment où il commente le « 13 » ; légende « vidéo en espagnol, source en description » (S21).]

Dans une vidéo espagnole, un utilisateur charge un modèle quatre bits dans LM Studio sur sa 5080. Ça rentre pas, il laisse une partie des couches en RAM, et il le dit lui-même : treize tokens par seconde, parce qu'une partie du modèle est dans la RAM. Ce sont pas les mêmes réglages que pour le cent un, donc je compare pas au chiffre près.

[VISUEL : même carte, 5060 Ti : « Qwen3.6, 3 Go qui débordent : 7,7 à 9,2 tok/s » → « Qwen3.8, fichier qui tient : 26,3 tok/s » (S41).]

Sur une seule carte, une 5060 Ti, quelqu'un a vécu les deux. Avec la version précédente de Qwen, son fichier débordait de trois gigas : huit ou neuf tokens par seconde. Avec un fichier du Qwen actuel qui tient dans la carte : vingt-six. Trois fois plus vite. Et sa conclusion, en gros : un fichier qui tient vaut plus que le MTP.

[VISUEL : quatre cartes de 16 Go côte à côte, même fichier, plafond calculé : RX 9060 XT 320 Go/s ≈ 26 ; RTX 5060 Ti 448 ≈ 37 ; RX 9070 XT 640 ≈ 53 ; RTX 5080 960 ≈ 79 (S38, S39).]

Au passage, ça vaut aussi pour AMD. Regarde la vitesse de la mémoire, pas seulement les gigas sur la boîte. Avec le même fichier, une RX 9070 XT a un plafond deux fois plus haut qu'une 9060 XT. Seize gigas toutes les deux. Et la 5080, encore au-dessus.

[VISUEL : histogramme Steam d'octobre 2026 : « 8 Go : 26,9 % », « 16 Go : 26,4 % », « 12 Go : 12,9 % » (S36). Puis deux petites cartes : « 12 Go : le 27B en 3 bits, 10 Go de fichier, ~27 000 tokens » / « 8 Go : ne tient pas » (S38).]

Et si t'as pas seize gigas ? T'es loin d'être seul : sur Steam, en octobre, plus d'un joueur sur quatre a une carte de huit gigas, et un sur huit en a douze. En douze, le 27B rentre en trois bits, avec un fichier de dix gigas, mais il te reste à peine vingt-sept mille tokens : une conversation, oui ; un agent de code lourd, non. En huit, il rentre pas : tu tombes dans le cas du treize, en pire.

[VISUEL : la barre « RAM 32 Go » en gris, avec « presque inutile ici ».]

Et ta RAM, dans tout ça ? Pour ce modèle, elle sert presque à rien : tout se joue dans la carte. Retiens ça, parce qu'avec le modèle suivant, ça s'inverse.

---

## 3. Plus gros : là, c'est ta RAM qui décide (6:50 - 9:00)

[VISUEL : l'icône Strata, puis « 125 milliards de paramètres, dont 6 travaillent à chaque mot » (S4).]

Parce qu'il existe un autre Qwen, bien plus gros : Flash-Next, cent vingt-cinq milliards de paramètres. En fait, il est découpé en centaines de petits spécialistes, des experts, et à chaque mot, il n'en réveille que quelques-uns : environ six milliards au travail. Et un projet open source sorti fin septembre, Strata, le fait tourner sur un PC de joueur.

[VISUEL : schéma en trois étages : GPU 16 Go / RAM / SSD. Les experts descendent en cascade (S2).]

Son astuce : les experts qui servent le plus restent dans la carte, les autres vont dans la RAM, et une grosse table reste sur le SSD. Sauf que du coup, tout s'inverse : la doc de Strata le dit, ta RAM doit contenir les experts, plus environ dix gigas pour Windows et le reste.

[VISUEL : tableau qui s'écrit ligne par ligne : « complet, plus petit fichier : 34 + 10 = 44 Go » ; « Coder : 23 + 10 = 33 Go » ; à côté, « 32 Go de DDR5 = ~33,5 Go visibles sous Windows ». Barres rouge / orange (S3, S6, S8).]

Fais le calcul avec moi. Le plus petit fichier du modèle complet, c'est trente-quatre gigas d'experts. Plus dix : quarante-quatre. Et moi, j'ai trente-deux gigas de RAM : c'est non. Mais la doc a une réponse pour trente-deux gigas : prends le Coder, une version réduite pour le code, qui garde la moitié des experts. Vingt-trois gigas, plus dix : trente-trois. Et Windows t'en laisse voir environ trente-trois et demi. Ça passe, mais à ras, navigateur fermé. Et ça, c'est un calcul.

[VISUEL : capture d'un ticket GitHub, « Ryzen 7 9700X, 5070 Ti 16 Gio, 31,2 Gio de RAM », 70,4 tok/s ; zoom sur « Speed only: no correctness check was run », traduit (S9).]

Sauf qu'un utilisateur l'a mesuré, avec presque ma config : le même processeur, une 5070 Ti de seize gigas, trente et un gigas de RAM visibles. Soixante-dix tokens par seconde. Un modèle de cent vingt-cinq milliards, à cette vitesse, sur un PC de joueur. Mais en tête de son rapport, la personne l'écrit elle-même : vitesse seulement, aucun test de justesse.

[VISUEL : trois étiquettes de prix accrochées au « 70 » : « 95 % du score de code… d'après ses auteurs » ; « échec documenté sur une tâche Claude Code » ; « plus faible hors de l'anglais, du chinois, du japonais et du coréen » (S6, S7, S17, S35).]

Et il y a un prix. Ses auteurs annoncent quatre-vingt-quinze pour cent du score de code du modèle complet, mais c'est leur chiffre. Sur un forum de développeurs, quelqu'un sent, en substance, une vraie perte. Dans un test publié en vidéo, sur une 5090, le Coder a pas réussi à finir sa tâche avec Claude Code. Et d'après la doc, il est plus faible hors de l'anglais, du chinois, du japonais et du coréen. Le français en fait partie.

[VISUEL : capture du kit de 32 Go à 92,95 € (2025), puis la même référence à 560 € sur Amazon. En petit : « relevé du 08/11/2026 ».]

Et si tu te dis « bah, je rajoute de la RAM » : mes trente-deux gigas, je les ai payés quatre-vingt-treize euros en 2025. Le même kit, aujourd'hui : cinq cent soixante euros. Six fois le prix, pour les mêmes barrettes.

[VISUEL : carte YouTube vers la vidéo du 16 nov. (ajoutée à sa sortie). Un écran « à suivre : Strata sur la 5080, en vrai ».]

Bref, sur le papier, le Coder tient chez moi. Alors la semaine prochaine, je le lance pour de vrai sur ma 5080, et on regarde ce qu'il vaut.

[VISUEL : la carte d'un côté, le logo de Claude de l'autre, un « ? » au centre.]

Mais admettons que ça tourne chez toi. Est-ce que ça vaut ton abonnement ?

---

## 4. Et Claude, dans tout ça ? (9:00 - 10:05)

[VISUEL : tableau Qwen3.8-27B contre Opus 4.6 : SWE-bench Pro 61,7 / 53,4 en vert ; Terminal Bench 2.1 73,0 / 78,2 en rouge ; légende « chiffres de Qwen, modèle complet » (S29).]

Sur les tableaux publiés par Qwen, le 27B bat l'ancien Opus 4.6 en code sur un test, et il perd sur un autre. Mais c'est leur tableau, avec le modèle complet : c'est pas le fichier trois bits qui tient dans ta carte.

[VISUEL : « Terminal-Bench 4.0 : 6 % contre 46 % » en gros, « classement indépendant, source en description » (S31).]

Un classement indépendant, lui, compare ce même 27B à Claude Opus 5, en agent dans un terminal : six pour cent de réussite contre quarante-six. Ouais, t'as bien entendu. Six. Donc pour coder en agent sur un vrai projet, Claude est loin devant.

[VISUEL : deux colonnes « Local » / « Abonnement ». Local : « tes données restent chez toi », « marche sans internet », « rien à payer chaque mois ». Abonnement : « le meilleur modèle », « rien à installer », « pas de patch de 3 Go à caser ».]

Du coup, voilà comment je le lis. Ton modèle de seize gigas, c'est un très bon plan B : tes données restent chez toi, il marche sans internet, et t'as rien à payer chaque mois. Pour le code sérieux en agent, l'abonnement garde l'avantage. Et en plus, chez Claude, le patch de trois gigas, c'est pas ta carte qui le paie.

---

## 5. Ce qui clochait chez moi, et le verdict (10:05 - 13:00)

[VISUEL : retour sur la 5080, comme au début. Le fichier « 14,25 Go, 4 bits » se glisse dans la jauge, puis « Windows ~1 Go ». Il reste un mince filet vert : « moins de 2 Go pour la conversation ».]

Et mon Qwen qui me paraissait super lent, alors ? J'avais pris le fichier quatre bits de quatorze gigas. Souviens-toi : la 5060 Ti en tire vingt-cinq tokens par seconde, et ma carte a deux fois plus de bande passante. D'après le calcul, le mien aurait dû tourner autour de cinquante. Donc c'était pas la carte. Il reste deux suspects.

[VISUEL : un compteur « tokens de réflexion » qui défile ; « 22 276 tokens pour un seul dessin » ; « à 50 tok/s ≈ 7 min avant la première ligne » (S45). Puis ta capture du panneau de droite de LM Studio, le réglage de réflexion entouré.]

Le premier, je suis sûr qu'il était là : par défaut, ce Qwen réfléchit au niveau maximum avant de répondre. Un développeur a compté plus de vingt-deux mille tokens de réflexion pour une seule demande : dessiner un pélican. Même à cinquante tokens par seconde, ça fait plus de sept minutes avant la première ligne utile. Ce niveau de réflexion, tu peux le baisser dans le panneau de droite de LM Studio.

[VISUEL : la facture de la section 1 revient, ligne « conversation » : « 64 000 tokens = 4,3 Go », puis « 100 000 tokens = 6,6 Go », face au filet vert de « 1,9 Go ». Le surplus coule en rouge vers une barre « RAM ». Puis capture du Gestionnaire des tâches, Performances, GPU : « Mémoire GPU dédiée » pleine, « Mémoire GPU partagée » qui grimpe ; et le panneau NVIDIA, ligne « CUDA – Sysmem Fallback Policy » (S37, S43, S44).]

Le deuxième suspect, c'est moi. Avec quatorze gigas de fichier, une fois l'écran servi, il me restait moins de deux gigas pour la conversation. Et j'avais monté la conversation à soixante-quatre mille tokens, puis à cent mille. Reprends la ligne deux de la facture : soixante-quatre mille tokens, c'est plus de quatre gigas. Cent mille, plus de six. Il me manquait donc entre deux et quatre gigas et demi. Et quand ta carte est pleine, le pilote NVIDIA déborde en silence dans ta RAM au lieu de planter. Ça marche, mais beaucoup plus lentement : NVIDIA le dit lui-même, et LM Studio aussi. En gros, d'après le calcul, j'avais recréé le treize du début, tout seul. Pour le savoir chez toi : Gestionnaire des tâches, Performances, GPU, et tu regardes la mémoire GPU partagée pendant que le modèle écrit. Si elle grimpe, t'as ton coupable. Et dans le panneau NVIDIA, un réglage interdit ce débordement : le modèle plante au lieu de ramer, mais au moins, tu sais.

[VISUEL : récap en trois lignes sur fond sombre : « le fichier qui rentre, avec 4 Go de marge » / « la conversation et l'agent comptent » / « au-delà : c'est la RAM qui décide ».]

Bref, ma carte était pas en cause : c'était ce que je lui demandais. Donc oui, seize gigas suffisent : pour un vrai modèle de vingt-sept milliards, si tu prends le fichier qui rentre et que tu laisses de la place à la conversation et à l'agent. Pour aller plus gros, c'est ta RAM qui décide, plus la carte. Et pour le code en agent, Claude reste devant.

[VISUEL : plan sur toi ou sur ton bureau.]

Moi, je garde ma config : les moteurs sont de plus en plus performants. Par contre, je vais passer de LM Studio à llama.cpp, ou à Strata.

[VISUEL : carte YouTube vers la vidéo d'installation (2 nov.).]

Si t'as jamais installé d'IA chez toi, j'ai une vidéo qui le fait pas à pas : je te la mets là.

[VISUEL : écran de fin : la vidéo suivante de la playlist « Abonnement ou IA locale ? ».]

Et la semaine prochaine, Strata, en vrai, sur ma carte. En attendant, dis-moi en commentaire ta carte et ta RAM, et je te dis ce qui tient chez toi.

---

## Faits utilisés

| Dit dans le script | Faits |
|---|---|
| 101 tok/s sur 5080 (53 sans MTP), fichier 3 bits, une seule mesure | S18 |
| 13 tok/s sur 5080, LM Studio, Q4, une partie des couches en RAM (dit par le présentateur) | S21 (corrigé le 07/11) |
| Ton Qwen « super lent », fichier 4 bits de 14,25 Go | `fiche.md` (impression sans chiffre) |
| Steam d'octobre 2026 : 8 Go 26,92 %, 16 Go 26,35 %, 12 Go 12,91 % | S36 |
| 16 Gio = 17,18 milliards d'octets ; Windows ~1 Go (hypothèse, comme la marge de 1 536 Mio de Strata, S15) | calcul ; S15 |
| Q4 de 16,46 à 18,97 Go selon l'éditeur ; 3 bits ISTA avec MTP 12,12 Go ; IQ3_XXS 10,09 Go | S38 |
| 64 Ko par token (16 couches à attention complète sur 64) ; 8 000 tokens par défaut dans LM Studio | S37, S44 |
| ~60 000 tokens avec 4 Go ; presque le double en 8 bits | calcul (4,06 Go ÷ 64 Kio ≈ 62 000) |
| Claude Code : 51 400 tokens avant la première question (un relevé, ça dépend de la config) ≈ 3,4 Go | S46, calcul |
| Plafond = bande passante ÷ taille ; 5080 960 Go/s ; DDR5-6000 double canal ~96 Go/s | S39 |
| 5060 Ti, même fichier UD-IQ4_XS : 24,9 tok/s, plafond 31 | S40, S39 |
| Même carte, version précédente de Qwen : 26,3 tok/s qui tient, 7,7-9,2 qui déborde de 3 Go | S41 |
| Plafonds AMD / NVIDIA avec le même fichier | S38, S39, calcul |
| 12 Go : 10,09 Go de fichier, ~27 000 tokens ; 8 Go ne tient pas | S38, calcul |
| Strata, 125 B dont ~6 actifs ; experts + ~10 Go ; 44 Go ; Coder 23 + 10 ; 33,5 Go visibles | S2, S3, S4, S6, S8 |
| 5070 Ti / 9700X / 31,2 Gio : 70,4 tok/s, « speed only » | S9 |
| 95 % d'après ses auteurs ; forum de développeurs ; échec en vidéo sur 5090 ; plus faible hors anglais et CJK | S6, S7, S17, S35 |
| RAM 92,95 € → 560 € | `fiche.md` (relevé du 24/10, revérifié par toi le 08/11 : 560 €) |
| Tableaux de Qwen contre Opus 4.6 ; 6 % contre 46 % contre Opus 5 | S29, S31 |
| Réflexion au maximum par défaut ; 22 276 tokens pour un pélican | S45 |
| Le pilote déborde en silence dans la RAM ; LM Studio le confirme ; réglage pour l'interdire | S43, S44 |
| Ton contexte monté à 64K puis 100K : 4,3 Go et 6,6 Go de conversation pour ~1,9 Go libres, soit 2,4 à 4,6 Go de trop | `fiche.md` (ton vécu, 08/11) ; S37, S38 (calcul, cache en version normale) |
| Le réglage de réflexion est dans le panneau de droite de LM Studio ; ton choix final (garder ta config, passer à llama.cpp ou Strata) | tes mots du 08/11 |

**Interdits respectés** : aucun nom de chaîne ni de créateur dans la voix ; aucun « j'ai testé » ni « sur ma 5080 » avec un chiffre ; ton Qwen lent reste une impression, et ses causes sont « d'après le calcul » ; la 5060 Ti et la 5070 Ti ne sont pas des 5080 ; le Coder n'est jamais « équivalent » au complet ni à Claude ; « 16 Go suffisent » est toujours précisé ; pas de « /no_think » (non documenté pour Qwen3.8).
