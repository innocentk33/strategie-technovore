# Grill de la V1 : « 16 Go suffisent » (05/11/2026)

> Script critiqué : [`script-v1.md`](script-v1.md). Version corrigée : [`script.md`](script.md). Faits : [`sources.md`](sources.md) (S1 à S35, vérifiés le 05/11). Skill : `youtube-script-grill`, mode B, variante storytelling (test des 30 s, axe 10 des liaisons). Débit de référence : 145 mots/min.

## Verdict

**V1 : 6/10. V2 : 8/10 (estimation).** La matière est solide et honnête : les mesures sont croisées, chaque limite est dite (« une seule mesure », « calcul, pas une mesure »), et la section Strata a un vrai calcul fait avec le spectateur. Le plus gros problème est au début : le hook livre le verdict à 0:08 (« Donc oui : seize gigas suffisent »), puis le corrige par une fausse opposition, ce qui tue la question centrale. Avec une chute de 85 % à 45 % pendant la première minute sur Uber, c'est le passage qui coûte le plus. Deuxième chantier : quatre faits mal recollés à `sources.md` et trois genres supposés.

## Test des 30 secondes (V1)

| Tranche | Ce que dit le script | Verdict |
|---|---|---|
| 0-5 s | > « Cette carte a seize gigas. » | 🟢 Raccord avec la miniature, mais aucune tension : c'est une fiche technique. |
| 5-15 s | > « un utilisateur a mesuré cent un tokens par seconde avec un vrai Qwen de vingt-sept milliards de paramètres. Donc oui : seize gigas suffisent. » | 🔴 Le meilleur chiffre est là, mais le verdict tombe aussitôt : le spectateur a sa réponse à 0:10, il n'a plus de raison de rester. Le contraste le plus fort des sources (101 contre 13 sur la même carte, `fiche.md`, contenu 1) n'est pas utilisé. |
| 15-30 s | > « Sauf que le vrai verrou, c'est pas la carte, c'est la RAM. Et c'est pas Claude. » | 🔴 Double fausse opposition. Elle est aussi fausse pour le 27B : la section 1 dit elle-même que la RAM « presque rien ». « Et c'est pas Claude » ne s'explique pas. |
| Question + pont | > « Alors, jusqu'où ces seize gigas te mènent vraiment, et à partir de quand ton abonnement redevient la bonne réponse ? Je n'ai rien testé moi-même [...] et il y en a une qui change tout. » | 🟠 Deux questions d'un coup au lieu d'une, posées à ~0:25. « Il y en a une qui change tout » annonce sans rien livrer (faux suspens). « Je n'ai rien testé » contredit ton vécu (tu as lancé Qwen, il t'a paru lent) : « aucun banc d'essai » est plus juste. |

**Budget V1** : 92 mots, environ 38 s.
**À couper** : « Donc oui : seize gigas suffisent », « Et c'est pas Claude », « il y en a une qui change tout ».
**À ajouter** : une tension dans la première phrase, ton impression à toi (seule matière qu'aucun concurrent n'a), le contraste 101 / 13.

**Réécriture (V2, 88 mots, environ 36 s)** :

> Cette carte, c'est la mienne : seize gigas. Et dessus, Qwen, un vrai modèle de vingt-sept milliards, m'a paru super lent. Sauf que quelqu'un, avec la même carte et le même modèle, a publié cent un tokens par seconde. Une autre mesure, sur une 5080 aussi : treize. Du coup, seize gigas, ça suffit ou pas ? J'ai fait aucun banc d'essai, j'ai rassemblé les mesures publiées. Et entre cent un et treize, il y a un fichier qui rentre, et un qui déborde. Et au-delà, c'est ta RAM qui décide.

- **0-5 s** : la carte de la miniature et une tension (ta carte, ton modèle, et ça rame).
- **5-15 s** : le contraste 101 → 13, avec sa preuve à l'écran (S18, S21).
- **Vers 0:18** : une seule question, celle du titre.
- **Le pont** : il ouvre deux boucles avant de fermer la première : « un fichier qui rentre, un qui déborde » (section 1) et « ta RAM qui décide » (section 2, et le titre 2 s'il gagne).
- **Ce qui reste fragile** : 36 s, un peu au-dessus de la cible. Si ta prise est lente, coupe « J'ai fait aucun banc d'essai, j'ai rassemblé les mesures publiées » et garde le tampon « calculé, pas testé » à l'écran ; la phrase revient alors en section 1.

## Tableau de bord

| Axe | V1 | V2 | En une phrase |
|---|---|---|---|
| 1. Promesse | 🟠 | 🟢 | V1 donne la réponse à 0:08 ; V2 garde « ça suffit ou pas ? » jusqu'au verdict, et chaque section en tranche un morceau. |
| 2. Alignement | 🟢 | 🟢 | Tu cherches la même chose que le spectateur : savoir ce que ta carte vaut, sans vendre de rêve. |
| 3. Problème profond | 🟠 | 🟢 | V1 : « est-ce que ma carte de 1 500 € vaut le coup ? » reste implicite. V2 : ton Qwen lent le rend concret. |
| 4. Public & complexité | 🟠 | 🟢 | V1 parle de « quantization trois bits », de MTP et d'experts sans les expliquer. V2 : le JPEG de l'IA, « devine plusieurs mots d'avance », « des spécialistes ». |
| 5. Valeur & originalité | 🟢 | 🟢 | Les mesures croisées et le calcul de RAM à ras, Kai ne les a pas. |
| 6. Structure & transformation | 🟢 | 🟢 | Du simple (27B) au compliqué (Strata), puis le prix, puis Claude : la progression tient. |
| 7. Histoire | 🔴 | 🟠 | V1 n'a personne qui veut quelque chose. V2 : toi, avec ta carte et ton modèle lent, au début et à la fin. Ça reste un essai, pas un récit. |
| 8. Mais / donc | 🟢 | 🟢 | Les « sauf que » relient de vrais faits (le Q4 qui déborde, le « speed only »). |
| 9. Engagement actif | 🟠 | 🟢 | « Fais le calcul avec moi » est très bien. V2 ajoute « tu dois te demander si c'est ce qui est arrivé à mon Qwen ». |
| 10. Oralité & liaisons | 🟠 | 🟢 | Assez de liaisons, mais 13 « donc », dont 6 qui ouvrent une conclusion. Détail plus bas. |
| 11. Tics d'IA | 🔴 | 🟢 | 9 « ce n'est pas / c'est pas », 3 « attention », un « Comment ? », la même réaction (« Cent un ! ») répétée trois fois. |
| S1. 30 premières secondes | 🔴 | 🟢 | Voir le test. |
| S2. Le pont | 🟠 | 🟢 | V1 démarre par « Commençons par le plus simple ». V2 ouvre deux boucles. |
| S3. Retournements | 🟠 | 🟢 | V1 : environ 75 s sans retournement entre 0:30 et 1:45 (le 101 redit). V2 : « Et le treize, alors ? » vers 1:55, « tu dois te demander » vers 2:40. |
| S4. Planté / récolté | 🟠 | 🟢 | V1 : une seule récolte (« Retiens cette phrase »). V2 : la RAM qui s'inverse, et ton Qwen lent (hook → section 1 → fin). |
| S5. Personnages | 🔴 | 🟠 | Des « utilisateurs » sans visage. V2 : toi. Les autres restent des mesures, c'est normal pour une vidéo calculée. |
| S6. La fin | 🔴 | 🟢 | V1 : « Donc, résumons », la fin résume. V2 : elle explique pourquoi ton Qwen était lent (« j'avais exactement le problème de cette vidéo ») et ouvre sur la vidéo du 16 nov. |

## Les liaisons orales

Comptées sur le texte dit, sans les indications de montage, avec les liaisons du skill (donc, du coup, en fait, sauf que, en effet, voilà, et là, et pourtant, parce que, en gros, bref, résultat, tu vois, mais…).

| Section | V1 : mots / liaisons / pour 100 | V2 : mots / liaisons / pour 100 |
|---|---|---|
| Hook | 92 / 2 / 2,2 | 88 / 2 / 2,3 |
| 1. Le 27B | 353 / 9 / 2,6 | 445 / 14 / 3,1 |
| 2. Strata | 392 / 13 / 3,3 | 429 / 12 / 2,8 |
| 3. Le prix | 249 / 7 / 2,8 | 338 / 8 / 2,4 |
| 4. Claude | 158 / 5 / 3,2 | 146 / 4 / 2,7 |
| 5. Verdict | 101 / 1 / **1,0** | 211 / 3 / 1,4 |
| **Total** | **1 345 / 37 / 2,75** (9 min 16) | **1 657 / 43 / 2,6** (11 min 25) |

Le chiffre de la V1 dépasse déjà le repère de 1,5, mais sa variété est faible :
- **« donc » 13 fois**, souvent en tête d'une conclusion (« Donc oui », « Donc le modèle complet, c'est non », « Donc ça tourne vite, mais », « Donc c'est impressionnant, mais », « Donc pour coder en agent », « Donc, résumons ») : à force, chaque paragraphe finit par une petite morale ;
- **« en fait » 1 fois, « en gros » 0, « bref » 0, « tu vois » 0** ;
- **la même réaction trois fois** : « Cent un ! », « Soixante-dix ! », « Six contre quarante-six ! ». Répétée, elle devient un tic de montage.

V2 : « donc » 8, « du coup » 5, « sauf que » 5, « en fait » 3, « en gros » 2, « bref » 2, « voilà » 2, « et là » 2, « en effet », « résultat », « tu vois », « parce que » 1 chacun. Les réactions changent à chaque fois (« En gros, il écrit bien plus vite que tu ne lis », « Sur le papier, c'est dingue », « Ouais, t'as bien entendu. Six. », « Ouais, six fois le prix »). Le verdict reste sous 2 : il est fait pour être net.

## Le grill (du plus grave au moins grave)

### 1. Le verdict à 0:08 tue la question
> « Donc oui : seize gigas suffisent. »

**Pourquoi ça coince :** le titre pose une affirmation, le hook la confirme tout de suite, puis la phrase suivante la nuance. Le spectateur a sa réponse avant 15 s, et la nuance arrive sous forme de slogan.
**Correction :** le contraste d'abord (101 contre 13), la question ensuite, le verdict à la fin (V2, hook et section 5).

### 2. Le 101 tok/s et le fichier de 11,8 Go ne sont pas le même fichier
> « En quantization trois bits, son fichier fait onze virgule huit gigas chez ISTA (S33). [...] Sur une RTX 5080, une contributrice ou un contributeur du dépôt sudoingX mesure cinquante-trois tokens par seconde. »

**Pourquoi ça coince :** S18 mesure un **Q3_K_M d'Unsloth** (VRAM 14 445 → 15 359 Mio), pas le fichier ISTA de 11,8 Go. Enchaînés, les deux chiffres laissent croire que le 101 tourne avec 4 Go de marge.
**Correction :** « sur une 5080, avec un fichier trois bits, la carte remplie à quinze gigas sur seize » ; le 11,8 Go d'ISTA ne reste qu'à l'écran, comme exemple de fichier qui rentre.

### 3. Trois genres supposés, et une formule lourde
> « une contributrice ou un contributeur du dépôt sudoingX » ; « un gars avec presque ma config » ; « Ce n'est pas un test universel, il le dit lui-même » ; « un commentateur écrit » ; « le YouTubeur Kai » ; « un autre mesure »

**Correction :** « la personne qui l'a publiée », « quelqu'un l'a mesuré », « la personne l'écrit elle-même », « Samayas précise », « Kai, sur YouTube », « Autodidacts mesure ».

### 4. La fausse opposition en série (9 occurrences)
> « le vrai verrou, c'est pas la carte, c'est la RAM. Et c'est pas Claude. » ; « ton vrai plafond, c'est le contexte, pas la taille du modèle » ; « Le verrou n'est plus ta carte, c'est ta RAM » ; « prends le fichier qui rentre, pas celui qui est "meilleur sur le papier" » ; « Mais ce n'est pas Claude. »

**Pourquoi ça coince :** c'est le tic n° 1. Trois fois la même idée (carte → RAM) en opposition, et elle est fausse pour le 27B.
**Correction :** dire B directement. « Donc ton vrai plafond, sur seize gigas, c'est la longueur de la conversation » ; « Sauf que du coup, tout s'inverse » ; « le fichier qui rentre, avec de la place pour la conversation ». V2 n'en garde qu'une, vraie : « c'était pas la carte » à la fin, parce que le spectateur soupçonne la carte depuis le hook.

### 5. Les 45 tok/s de Kai ne sont pas les siens
> « Le YouTubeur Kai trouve quarante-cinq tokens par seconde sur une 5060 Ti. »

**Pourquoi ça coince :** S20 : « Speeds are self-reported by the owners ». Kai relaie, il ne mesure pas.
**Correction :** « Kai, sur YouTube, relaie des possesseurs de 5060 Ti qui annoncent quarante-cinq tokens par seconde. »

### 6. Le tableau de Qwen, dit à moitié
> « D'après les tableaux de Qwen, le 27B bat l'ancien Opus 4.6 en code sur SWE-bench Pro »

**Pourquoi ça coince :** le visuel montre Terminal Bench 2.1 (73,0 contre 78,2, Opus devant), la voix ne garde que la ligne où Qwen gagne. Un spectateur qui met pause le voit.
**Correction :** « Mais sur Terminal Bench, Opus reste devant. »

### 7. Les citations HN et Samayas présentées comme des citations
> « Sur Hacker News, un commentateur écrit que le Coder est moins bon et qu'il a une perte notable. »

**Pourquoi ça coince :** la voix reformule, le visuel affiche le texte anglais : il faut que la reformulation se dise comme telle.
**Correction :** « quelqu'un le trouve, en substance, moins bon, avec une perte qui se sent » ; bulles marquées « en substance » à l'écran ; la phrase de Samayas reste en anglais, en petit, puisqu'elle est exacte (S35).

### 8. « Commençons par le plus simple » et le 101 redit
> « Commençons par le plus simple. Qwen3.8-27B, vingt-sept milliards de paramètres. »

**Pourquoi ça coince :** à 0:30, au moment où Uber perdait le plus, la section 1 rouvre sur une phrase de remplissage et redit le chiffre du hook.
**Correction :** ouvrir sur ce que le hook a promis (« pourquoi un même modèle peut avoir plusieurs fichiers »), et garder le 101 pour l'expliquer, pas pour le répéter.

### 9. La fin résume
> « Donc, résumons. »

**Correction :** la récolte de ton Qwen lent (fichier de 14,25 Go à ras, réflexion activée par défaut, `fiche.md`), puis le verdict en deux phrases, puis ton choix ⟦à écrire⟧.

### 10. Les petits tics
- « Comment ? » (section 2) : faux suspens, remplacé par « Son astuce : ».
- « Car il y a un autre Qwen » : connecteur d'écrit, remplacé par « Parce qu'il existe ».
- « Par contre, attention », « Mais attention au piège », « Attention, ne te fais pas piéger » : un seul « par contre » reste.
- « il y en a une qui change tout » : annonce vide, coupée.
- « ça ne coûte rien de plus » : l'électricité est exclue par décision, mais la formule promet trop ; remplacée par « t'as rien à payer chaque mois ».
- « ta carte de mille cinq cents euros » : la tienne a coûté 1 100 € ; 1 500 € est le prix de Hardware IA. V2 : « une carte à mille cinq cents euros ».

## Ce qu'il faut garder

- **« Fais le calcul avec moi »** et le tableau 34 + 10 / 50 + 10 : le spectateur fait le calcul avec toi et retient la règle.
- **« Retiens cette phrase, parce qu'elle va s'inverser »** : la meilleure relance de la V1, gardée.
- **« Vitesse seulement, aucun test de justesse »** : l'honnêteté qui manque à Kai et à Luke's Dev Lab.
- **« Ce n'est pas exactement le même réglage que les cent un, donc je ne te fais pas une soustraction »** : la nuance est dite à l'oral, sans alourdir. Gardée, raccourcie.
- **« Un fichier de trop, et ta carte de mille cinq cents euros rame comme une vieille tour »** : la phrase la plus « toi » du script.
- **« Pile la marge demandée, à un giga près »**.

## Ce que l'auteur doit trancher

1. **Le titre.** 1 : *16 Go de VRAM suffisent (si tu prends le bon fichier)*, que le hook confirme dès 0:10 (recommandé) ; 2 : *(mais pas la RAM)*, celui de la V1, tenu seulement à partir de la section 2.
2. **Strata ici, ou le 7 déc. ?** La nouvelle vidéo *L'IA locale sans grosse carte graphique* (7 déc., `petit-budget-ia/`) prend aussi Strata comme exemple, et `fiche.md` disait encore le 24/10 que Strata irait dans *Combien coûte Claude en local ?*. Si les sections 2 et 3 restent ici (elles portent le titre 2 et la moitié de la valeur), le 7 déc. doit prendre un autre angle (le PC que tu as déjà, les petits modèles sur processeur).
3. **Le calcul en quatre cas et les conseils d'achat**, annoncés dans le calendrier (« + conseils d'achat (neuf et occasion) + le calcul en quatre cas ») et dans la fiche (contenus 5 et 6), ne sont ni dans la V1 ni dans la V2. Les ajouter fait +2 à 3 min et demande le relevé des prix ; sinon, il faut les déplacer (Coût Claude le 30 nov., Louer, acheter le 28 déc.) et corriger le calendrier.
4. **Ton vécu dans le hook** : confirme que c'était bien `UD-IQ4_XS` (14,25 Go) et que tu es d'accord pour dire « il m'a paru super lent » dès la première phrase. Ça reste une impression : pas de chiffre, pas de « j'ai testé ».
5. **Tes mots** : le crochet de la fin (ce que tu gardes, ce que tu fais tourner sur ta carte) ; le prix de la RAM (92,95 € → 560 €) à revérifier le jour de la voix.
6. **La miniature** : le script ouvre sur la carte seule, avec « 16 Go » ; le gabarit de la série dans la fiche (`vert-02`) met Claude à gauche et la carte à droite. Si c'est ce gabarit qui sort, ouvre la vidéo sur la même scène.

## Plan d'action

1. Trancher le titre et le point 2 (Strata), qui changent la longueur.
2. Écrire le crochet de la fin, revérifier le prix de la RAM.
3. Lire le hook à voix haute et le chronométrer : sous 36 s, sinon couper la phrase « aucun banc d'essai » (le tampon reste à l'écran).
4. Téléprompteur, puis storyboard calé sur la voix.
