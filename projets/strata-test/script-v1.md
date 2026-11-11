# Je teste le meilleur modèle possible avec Strata sur ma 5080 : script (V1, 11/11/2026)

**Sortie** : lun. 16/11/2026, 18 h. Tournage et tests : mer. 11/11 ([`plan-tests.md`](plan-tests.md)). Voix enregistrée **après** les tests. Faits : [`sources.md`](sources.md) (T1…). Plans : [`storyboard.md`](storyboard.md). Références : [`references.md`](references.md).

**Ce script n'a aucun résultat.** Tous les résultats sont des trous `⟦résultat : …⟧` à remplir avec ta fiche (section 6 du plan). Tes avis sont des `⟦à écrire : …⟧`. Rien n'est inventé : pas de chiffre, pas d'anecdote, pas de vécu.

**Deux variantes par moment de résultat** : `▶ A (ça marche)` et `▶ B (ça casse)`. Tu gardes celle qui correspond à ce que tu as vu ; `▶ Suite` reprend pour tous les cas. Si c'est mélangé (2 démos sur 3), prends A pour ce qui marche, B pour ce qui casse, et garde la section 6.

## Ce que la vidéo dit (texte et sous-texte)

- **Texte** : un modèle géant, coupé de moitié et fait pour le code, tourne sur ma carte de 16 Go et mes 32 Go de RAM. Voilà ce qu'il écrit (un jeu, un site, un monde en 3D), à quelle vitesse, face à Claude, et où ça casse.
- **Sous-texte** : le matériel que tu as peut aller plus loin que ce que les fiches disent, mais pas gratuitement : le verrou, c'est la RAM, et l'effort de réglage. **Montré, jamais dit** : l'accroc (RAM libre qui tombe, premier chargement) et l'échec éventuel.
- **À ne pas recadrer** : ce n'est pas une vidéo contre Claude. Tu l'utilises, tu continueras, et la comparaison est faite avec ta propre demande (sans classement général).

## Structure (grammaire de la vidéo d'installation, audit du 11/11)

- **0:00-0:15** : les trois démos qui tournent, avec la vitesse affichée. Aucun contexte.
- **~0:30** : la question centrale, le **plan en 4 livrables** et le défi (le pronostic) affiché à l'écran.
- **Section 1 commence par une démo** (le jeu), pas par une définition. La théorie (experts, RAM) vient en section 2, quand on se demande « comment ça tient ».
- **Fil rouge** : le compteur de tok/s et la RAM libre. **Relance toutes les 60 à 90 s** (voir « boucles »).

**Boucles ouvertes**
1. « Jusqu'où ça va ? » (hook) → tenue par les 3 démos, refermée par le verdict (section 7).
2. « Qui gagne ? » (pronostic, 0:30) → tenue par la section 5, refermée à la fin.
3. « Comment un modèle géant rentre sur 16 Go ? » (fin de la section 1) → section 2.
4. « Là où ça casse » (plan, 0:30) → section 6.
5. « Jeudi, plus vite avec la même carte » (fin) → vidéo du 19/11.

**Conventions** : texte normal = voix off. `[VISUEL : …]` = plan (P… = fichier du tournage, V… = plan du storyboard). `⟦résultat : …⟧` = à remplir par la fiche. `⟦à écrire : …⟧` = ton avis. Nombres en lettres pour la lecture, sauf les trous. **Interdit à l'écran** : clé d'API, onglets du navigateur, dossiers de travail. **Aucun nom de chaîne ni de créateur** dans la voix.

---

## 0. Hook (0:00 – 0:40) · objectif : 75 % à 0:15, 50 % à 1:00

[VISUEL : V01-V05, plans de 1 à 3 s : le jeu qui tourne (P20), le site qui défile (P21), l'île qui tourne (P22), à chaque fois le compteur de tok/s du moniteur en incrustation (P12-P14). GIF « taper sur un clavier » avant 0:12. Pas de titre ni de logo.]

▶ A (ça marche) :
Un jeu qui se joue.
Un site complet.
Un monde en 3D.
Une IA a écrit les trois, chez moi, sur ma RTX 5080, à ⟦résultat : tok/s typique⟧ tokens par seconde.

▶ B (ça casse) :
Trois demandes à une IA qui tourne chez moi : un jeu, un site, un monde en 3D.
⟦résultat : combien sur trois ont marché⟧ sur trois ont marché.
Et le reste, ça donne ça : ⟦résultat : ce qui a cassé, en une phrase⟧.

▶ Suite :
[VISUEL : V06, la carte de la RAM dans le Gestionnaire des tâches (P04) : « 32 Go » entouré.]
Sauf que le vrai modèle, celui dont il vient, demande bien plus de RAM que mes trente-deux gigas.
Du coup, jusqu'où ça va, une IA qui tourne chez toi ?

[VISUEL : V07, le plan en 4 lignes qui s'écrivent avec la voix, sur fond noir : « 1. Ce que j'ai fait tourner, et comment le refaire » / « 2. La vitesse, en vrai » / « 3. Le même test, donné à Claude » / « 4. Là où ça casse ». Puis, en bas, le défi : « Ton pronostic : le local tient / Claude écrase ».]
Au programme : ce que j'ai fait tourner et comment le refaire, la vitesse, le même test donné à Claude, et là où ça casse.
Ton pronostic en commentaire : le local tient, ou Claude écrase ?

---

## 1. Niveau un : le jeu (0:40 – 1:58)

[VISUEL : V08, capture du terminal en deux volets : OpenCode à gauche, le moniteur de Strata à droite (P11). La carte de la vidéo du 09/11 apparaît 2 s (« 16 Go de VRAM suffisent »).]
Niveau un : le jeu.
Lundi dernier, je te disais que seize gigas suffisent, si tu prends le bon fichier. Là, on passe au niveau d'après : un modèle bien plus gros, et du vrai code, pas juste une discussion.

[VISUEL : V09, le prompt en anglais collé (P12), traduction en sous-titre : « un casse-briques complet, un seul fichier, raquette à la souris, 3 vies, bonus, bruitages, zéro erreur ».]
Ma demande : un casse-briques complet, dans un seul fichier. La raquette à la souris, trois vies, des bonus, des bruitages, et zéro erreur dans la console.
Je l'écris en anglais, parce que ce modèle est plus faible dans les autres langues : c'est sa propre doc qui le dit. Règle du jeu : un essai, et deux relances au maximum, comme des pièces à l'arcade.

[VISUEL : V10, accéléré de la génération, l'horloge de la barre des tâches visible, le compteur de tok/s en gros (P12).]
Du coup, je lance. Et regarde le compteur à droite : ⟦résultat : tok/s du jeu, bas / typique / haut⟧.

▶ A (ça marche) :
[VISUEL : V11, le jeu ouvert, 20 s de partie (P20), la console F12 vide.]
Au bout de ⟦résultat : durée du jeu⟧, il a fini. Et là, le moment de vérité : ⟦résultat : a marché du premier coup ? oui/non⟧.
Les briques cassent, la raquette suit la souris, un bonus tombe, et ça fait du bruit. ⟦résultat : points du jeu qui marchent, sur 5⟧ points sur cinq marchent.

▶ B (ça casse) :
[VISUEL : V11, le jeu ouvert qui plante ou reste vide (P20), la console F12 en rouge.]
Au bout de ⟦résultat : durée du jeu⟧, il a fini. Premier essai : ⟦résultat : ce qui ne marche pas dans le jeu⟧.
Je lui renvoie l'erreur, telle quelle, sans toucher au code. ⟦résultat : nombre de relances⟧ relance plus tard : ⟦résultat : verdict final du jeu⟧.

▶ Suite :
Bon, c'est joli. Mais en fait, tu te demandes sûrement la même chose que moi : comment un modèle géant tient sur une carte de seize gigas ?
Voilà comment.

---

## 2. Comment ça tient chez moi (1:58 – 4:29)

[VISUEL : V12, schéma très court sur fond noir, trois blocs qui s'allument avec la voix : « la carte » / « la RAM » / « le SSD ». Une capture de la page GitHub de Strata (P02) en incrustation, « gratuit, open source (MIT) ».]
Le modèle d'origine est découpé en centaines de petits spécialistes, les experts. Et à chaque mot, il n'en réveille que quelques-uns : six milliards de paramètres au travail, sur cent vingt-cinq.
Strata, c'est le programme qui range tout ça. La carte garde les experts les plus utilisés, la RAM garde le reste, et une grosse table reste sur le SSD. Il est gratuit, et open source.

[VISUEL : V13, l'écran du plan de Strata (P05) : « fits / tight », puis la fiche Hugging Face du Coder (P03), le mot « experimental » surligné en jaune.]
Sauf que sa règle, c'est : ta RAM doit contenir les experts, plus environ dix gigas pour Windows. Du coup, le modèle complet en demande bien plus que mes trente-deux. Et selon la doc, avec trente-deux gigas de RAM et une carte de seize, un seul fichier est prévu : le Coder. En fait, c'est le même modèle, coupé de moitié, fait pour le code, et ses auteurs le disent expérimental. Ils annoncent quatre-vingt-quinze pour cent du score de code du modèle complet. C'est leur chiffre, pas le mien.
Et retiens ces dix gigas de marge : on y revient, avec la vraie mesure.

[VISUEL : V14, trois étapes à l'écran, chacune avec la vraie commande (P05, P06, P09) : « 1. install.ps1 » / « 2. strata launch » / « 3. strata connect opencode ».]
Pour le refaire chez toi, trois étapes.
Un : tu installes le Terminal de Strata, une seule ligne dans PowerShell. La page est en description.
Deux : tu regardes d'abord le plan, « strata launch --plan », qui te dit si ça rentre avant de télécharger quoi que ce soit. Ensuite tu lances « strata launch », tu choisis le Coder, tu laisses le reste par défaut, et tu lis la commande : si tu vois « resident experts », tout est en RAM, c'est le bon mode.
Trois : tu branches ton outil de code avec « strata connect ». Moi, j'ai pris OpenCode : il a son propre fichier de config, donc je ne touche pas à mon Claude. ⟦à écrire : ta vraie raison d'avoir pris OpenCode, si ce n'est pas celle-là⟧

[VISUEL : V15, ce que ça demande, montré : le premier chargement accéléré, le curseur qui saccade (P07), la RAM libre dans le Gestionnaire des tâches (P15). Meme « This is fine » (chien dans la pièce en feu) sur la RAM qui tombe, si c'est le cas.]
Et ce que ça demande, vraiment. Ça fait environ cinquante-huit gigas à télécharger. Le premier chargement a pris ⟦résultat : durée du premier chargement⟧, et ⟦résultat : le PC s'est-il figé ? combien de temps⟧.
Il faut aussi tout fermer, navigateur compris : en effet, la RAM libre est descendue à ⟦résultat : RAM libre au plus bas⟧. Et la commande disait ⟦résultat : resident ou mmap⟧.

[VISUEL : V16, la carte de la vidéo d'installation du 02/11 (capture de LM Studio qui répond hors ligne), 3 s.]
Si c'est ta toute première IA en local, regarde d'abord la vidéo d'installation de LM Studio : je te la mets là. Strata, c'est l'étage au-dessus.

---

## 3. Niveau deux, boss final (4:29 – 5:36)

[VISUEL : V17, le site : prompt (P13), accéléré (P13) avec le compteur.]
Niveau deux : le site. C'est la demande que tout le monde fait à une IA, donc c'est la plus facile. Une page de présentation pour une appli de paiement mobile qui n'existe pas : un bouton, trois étapes, six cartes, trois tarifs, une FAQ qui s'ouvre, et ça doit tenir sur un téléphone.

▶ A (ça marche) :
[VISUEL : V18, le site ouvert, défilement lent, FAQ, version 375 px (P21).]
⟦résultat : durée du site⟧ plus tard : ⟦résultat : a marché du premier coup ? oui/non⟧. Je fais défiler, j'ouvre la FAQ, je passe en version téléphone : ⟦résultat : points du site qui marchent, sur 5⟧ points sur cinq.

▶ B (ça casse) :
[VISUEL : V18, le site cassé ou tronqué (P21), la console en rouge.]
⟦résultat : durée du site⟧ plus tard : ⟦résultat : ce qui ne va pas dans le site, y compris s'il est coupé⟧. ⟦résultat : relances du site et résultat⟧.

▶ Suite :
[VISUEL : V19, l'île voxel : le prompt (P14), sous-titre « une île en cubes, relief généré, eau, 15 arbres, souris pour tourner, touche N = nuit ».]
Boss final : une île en cubes, en 3D. Du relief généré, de l'eau, au moins quinze arbres, la souris pour tourner autour, et la touche N pour passer à la nuit.
Avant de lancer, mon pronostic : ⟦à écrire : ton pronostic avant le test 3D⟧.

▶ A (ça marche) :
[VISUEL : V20, l'île qui tourne, zoom, touche N (P22).]
Et là : ⟦résultat : l'île s'affiche ? premier coup oui/non, durée⟧. Le relief est ⟦résultat : le relief est-il crédible ?⟧, l'eau et les arbres ⟦résultat : eau et arbres ok ?⟧, et ça tourne ⟦résultat : fluide ou pas⟧. Pour moi, ⟦à écrire : ton avis sur la 3D⟧.

▶ B (ça casse) :
[VISUEL : V20, l'écran noir ou l'île incomplète (P22), la console.]
Et là : ⟦résultat : ce qui s'affiche à la place de l'île, premier coup oui/non⟧. ⟦résultat : relances et verdict final de la 3D⟧.

▶ Suite :
Bref, voilà pour ce qu'il écrit. Reste la question que tu vas poser : à quelle vitesse ?

---

## 4. La vitesse, en vrai (5:36 – 6:56)

[VISUEL : V21, le moniteur de Strata en plein écran (P10, P12-P14), les trois valeurs en gros : « jeu », « site », « 3D ».]
Pendant les trois tests, le compteur de Strata affichait ⟦résultat : tok/s du jeu⟧ pour le jeu, ⟦résultat : tok/s du site⟧ pour le site, et ⟦résultat : tok/s de la 3D⟧ pour la 3D, en tokens par seconde. Un token, c'est un morceau de mot.

[VISUEL : V22, une carte de repère sourcée sur fond noir : « RTX 5070 Ti, même processeur, 31 Go de RAM : ≈ 70 tok/s, réflexion coupée, sans test de justesse » (capture de la page GitHub du rapport, la phrase surlignée).]
Du coup, pour te donner un repère : un utilisateur d'une 5070 Ti, avec le même processeur que moi et à peu près la même RAM, mesure environ soixante-dix tokens par seconde avec ce modèle. Mais avec la réflexion coupée, et sans vérifier si le code marche.

▶ A (proche ou au-dessus du repère) :
Chez moi, c'est ⟦résultat : plus rapide ou plus lent que le repère, et de combien⟧.

▶ B (en dessous du repère) :
Chez moi, c'est ⟦résultat : plus lent que le repère, et de combien⟧, et je pense que c'est à cause de ⟦résultat : cause probable, d'après ton diagnostic⟧.

▶ Suite :
[VISUEL : V23, le réglage de réflexion à l'écran (la commande de lancement ou la config), le temps de réflexion visible dans OpenCode et dans le moniteur.]
Et la réflexion, justement. Par défaut, ce modèle réfléchit beaucoup avant de répondre, et ça mange les tokens de la réponse : avec la config que Strata écrit pour OpenCode, une réponse est limitée à un huitième du contexte, réflexion comprise. J'ai réglé la mienne sur ⟦résultat : réglage de réflexion⟧.
Dernière chose : la vitesse baisse quand la conversation grandit. Le projet le publie lui-même : le Coder passe de cinquante-neuf à quarante-trois tokens par seconde entre mille et cent vingt-huit mille tokens de contexte, sur une 5070 avec soixante-quatre gigas et un ancien moteur. Donc plus l'agent lit de code, plus ça ralentit, d'après leurs mesures.

---

## 5. Le même test, donné à Claude (6:56 – 7:43)

[VISUEL : V24, écran partagé : à gauche les trois résultats locaux, à droite les trois résultats de Claude (P33). Le pronostic de la section 0 revient en bas, 3 s.]
Maintenant, le vrai test : les trois mêmes demandes, mot pour mot, données à Claude avec mon abonnement. Donc une seule tentative, aucune relance.
Ce n'est pas le même outil : OpenCode d'un côté, Claude Code de l'autre. Par contre, c'est la même demande, et je note les mêmes choses : la durée, et les cinq points du prompt qui marchent.

[VISUEL : V25, les trois plans de Claude (P30, P31, P32) avec l'horloge : la durée de chacun s'affiche.]
Le jeu : ⟦résultat : Claude, durée et verdict du jeu⟧. Le site : ⟦résultat : Claude, durée et verdict du site⟧. La 3D : ⟦résultat : Claude, durée et verdict de la 3D⟧.

▶ A (le local tient la comparaison) :
Donc, sur ces trois demandes, ⟦résultat : verdict de la comparaison, en une phrase⟧. Et la différence que je vois : ⟦à écrire : ton avis sur ce qui sépare les deux⟧.

▶ B (Claude devant) :
Donc, sur ces trois demandes, Claude est devant : ⟦résultat : verdict de la comparaison, en une phrase⟧. Et ce qui fait la différence : ⟦à écrire : ton avis sur ce qui sépare les deux⟧.

▶ Suite :
Attention : trois essais, une tentative chacun, ce n'est pas un classement. C'est ce que j'ai vu, sur ma machine, aujourd'hui.

---

## 6. Là où ça casse (7:43 – 8:38)

[VISUEL : V26, les captures des incidents s'il y en a (P16) : le message exact à l'écran. Sinon, la page du ticket GitHub sur le plantage du Coder (capture, ticket surligné).]

▶ A (rien n'a planté chez moi) :
Chez moi, rien n'a planté. Mais d'autres ont eu des surprises, et tu dois les connaître.

▶ B (quelque chose a cassé chez moi) :
Chez moi, ça a cassé ici : ⟦résultat : ce qui a cassé, message exact, version de Strata⟧. Et ce n'est pas que moi.

▶ Suite :
En effet, un ticket ouvert sur GitHub décrit le moteur qui plante avec le Coder sur certains longs prompts, chez un utilisateur avec une petite carte, et avec un message qui parle, à tort, de manque de RAM. Un utilisateur de 5080 rapporte une autre erreur, « non-finite logits », avec d'autres fichiers du même modèle. Et un autre testeur a vu ce Coder échouer à une tâche dans Claude Code.
Strata est jeune : le projet date du vingt-quatre septembre, et il sort une version tous les deux ou trois jours. Donc note ta version, avant de te plaindre. Et si ça casse chez toi, copie le message exact : c'est ce qui sert au projet pour comprendre.

---

## 7. Le verdict, et ce soir (8:38 – 9:36)

[VISUEL : V27, les trois résultats locaux côte à côte, puis la RAM et la VRAM qui reviennent à zéro quand on arrête Strata (P41).]
Alors, est-ce que ça remplace mon abonnement ? ⟦à écrire : ton verdict, en une ou deux phrases⟧.
Ce que je retiens : ⟦à écrire : la chose qui t'a le plus surpris⟧. Et ce qui m'a manqué : ⟦à écrire : ce qui t'a manqué⟧.

[VISUEL : V28, la checklist qui s'écrit avec la voix : « 1. Ferme tout » / « 2. 32 Go de RAM, 90 Go de disque libres » / « 3. Le Coder » / « 4. Une demande à la fois, et tu notes ».]
Et selon ta RAM, la doc de Strata dit : trente-deux gigas, le Coder ; quarante-huit, les petites tailles du modèle complet ; soixante-quatre, toutes les tailles.
Si tu veux le refaire ce soir : un, ferme tout. Deux, vérifie que tu as au moins trente-deux gigas de RAM et environ quatre-vingt-dix gigas de disque libres. Trois, prends le Coder, pas un autre fichier. Quatre, une demande à la fois, et note ce que tu mesures.

[VISUEL : V29, le pronostic de la section 0 revient avec « Qui avait raison ? », carte YouTube vers la vidéo du jeudi 19/11.]
Bref, et ton pronostic, au début ? Dis-moi en commentaire si tu avais raison, avec ta carte et ta RAM.
Jeudi, on cherche comment aller plus vite avec la même carte. Je te mets la vidéo là.

---

## Faits utilisés

| Ce que dit le script | Section | Source | Statut |
|---|---|---|---|
| Modèle découpé en experts ; 6 milliards actifs sur 125 | 2 | T25 | ✅ (DEV) |
| La carte garde les experts les plus utilisés, la RAM le reste, une table sur le SSD ; gratuit, open source | 2 | T25, T24 | ✅ (DEV) |
| Règle : RAM ≥ experts + ≈ 10 Go ; le modèle complet en demande plus que 32 Go | 0, 2 | T15, T5 (S8) | ⚠️ à ras ; « bien plus » vaut pour ≥ 44 Go (Q2_0) |
| Le Coder : seul fichier annoncé pour 32 Go ; coupé de moitié, pour le code, expérimental | 2 | T5, T6 | ✅ (DEV) |
| « 95 % du score de code du modèle complet, d'après ses auteurs » | 2 | T6 | ✅ (DEV, attribué) |
| « plus faible dans les autres langues » | 1 | T5, T6 | ✅ (DEV) |
| La page GitHub, la commande `strata launch`, `strata connect`, « resident experts » | 2 | T2, T8, T14 | ✅ |
| ≈ 58 Go à télécharger | 2 | T6 (29,61 + 28,8), T4 | ✅ |
| OpenCode a son propre fichier de config (≠ Claude Code) | 2 | T14 | ✅ |
| Repère : une 5070 Ti, même processeur, ≈ 70 tok/s, réflexion coupée, sans test de justesse | 4 | T7 | ✅ (MESURE, une seule) |
| La limite d'une réponse = ⅛ du contexte, réflexion comprise | 4 | T13 | ✅ (DEV) |
| Un ticket : plantage du moteur avec le Coder sur certains longs prompts, chez un utilisateur de carte de 8 Go ; message « manque de RAM » à tort | 6 | T23 | ✅ (ticket ouvert ; ne se reproduit pas par défaut sur 12 Go, dit « certains ») |
| Un utilisateur de 5080 rapporte « non-finite logits » avec d'autres fichiers | 6 | T11 | ⚠️ non confirmé par le développeur |
| Un autre testeur a vu le Coder échouer à une tâche dans Claude Code | 6 | T27 | ⏳ description seule, non revérifiée le 11/11 |
| Projet du 24/09 ; une version tous les 2 à 3 jours (0.2.9 le 31/10, 0.2.10 le 02/11, 0.2.11 le 05/11, 0.2.12 le 07/11, 0.2.13 le 09/11) | 6 | T1 | ✅ |
| La vitesse baisse avec le contexte : le Coder passe de 59 à 43 tok/s entre 1 000 et 128 000 tokens (RTX 5070, 64 Go, moteur ancien) | 4 | T30 | ✅ (DEV, ancien moteur, dit « ancien moteur ») |
| OpenCode : son propre fichier ; `strata connect claude-code --write` écrit dans `~/.claude/settings.json` | 2 | T14 | ✅ ; la raison de ton choix est un `⟦à écrire⟧` |
| La doc : 32 Go → le Coder ; 48 Go → Q2_0 et IQ2_XS ; 64 Go → toutes les tailles | 7 | T5, DETAILS.md | ✅ (DEV) |
| Les liens vers 02/11 et 09/11 ; la vidéo du 19/11 | 1, 2, 7 | `calendrier.md` | ✅ |

**Non dit exprès** : « Flash-Next tourne sur 32 Go » (c'est le Coder), « 125 milliards » pour le Coder lui-même, tout classement général local contre Claude, tout chiffre de RAM de 64 ou 128 Go comme étant le tien.

## Mesure (11/11/2026, à relancer après avoir choisi les variantes et rempli les trous)

Comptée sur la voix seule (sections 0 à 7, sans titres, sans `[VISUEL]`, sans tableaux), à l'espace près ; **chaque trou `⟦…⟧` compté pour 1 mot** (rempli, il en vaudra 1 à 4 de plus). Variante A = « ça marche » partout ; variante B = « ça casse » partout. La liste de liaisons « stricte » : donc, du coup, en fait, sauf que, en effet, voilà, bref, par contre, justement, bon, alors.

| Variante | Mots de voix | Durée à 145 / 165 mots/min | Liaisons / 100 mots (stricte) | Liaisons / 100 mots (large : + mais, parce que, maintenant, attention…) |
|---|---|---|---|---|
| **A** (ça marche) | **1 354** | 9 min 20 / 8 min 12 (≈ 9 min 36 avec les trous remplis) | **1,77** (24) | 2,81 (38) |
| **B** (ça casse) | 1 328 | 9 min 10 / 8 min 03 | 1,81 (24) | 2,71 (36) |

- **Dans la cible** : 1 200 à 1 500 mots. Avec les trous remplis (≈ 45 trous, 1 à 3 mots de plus chacun), A passe à environ 1 430 mots (43 trous distincts, une cinquantaine d'emplacements) : toujours sous 1 500.
- **Hook** : 96 mots (A). Les trois démos et la vitesse sont dits dans les **28 premiers mots (≈ 12 s)** ; la question centrale (« jusqu'où ça va ») vers **0:22** ; le plan en 4 livrables de **0:24 à 0:34** ; le pronostic (le défi) à **0:34**, affiché dès 0:26.
- **Nombres dans la première minute** (voix) : RTX 5080, le tok/s du hook (un trou), « trente-deux gigas », « seize gigas » : **4**, plus « trois » (démos). Max 2 par phrase.
- **Aucun nom de chaîne ni de créateur** dans la voix (contrôlé mot à mot : « un utilisateur », « un autre testeur », jamais un nom). Les noms de produits cités sont Strata, OpenCode, Claude, GitHub, PowerShell, LM Studio, Windows.
- **Aucun résultat inventé** : tous les chiffres de résultat sont des `⟦…⟧` ; les seuls chiffres de la voix sont des faits sourcés (T5, T6, T7, T14, T15, T25, T30, T1) ou des constantes de tes prompts (trois vies, six rangées, quinze arbres…).
- **Pas d'anecdote ni de vécu inventé** : les actions décrites sont celles du plan de tests (tu lances, tu mesures, tu relances) ; tes avis sont des `⟦à écrire⟧` (pronostic, avis sur la 3D, sur l'écart avec Claude, verdict, ce qui t'a surpris, ce qui t'a manqué, la raison d'OpenCode).
