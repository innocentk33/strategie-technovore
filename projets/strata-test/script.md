# Le meilleur modèle possible pour 16 Go de VRAM (Strata, testé) : script (V2, 11/11/2026)

**Sortie** : lun. 16/11/2026, 18 h. Tests et tournage : mer. 11/11 ([`plan-tests.md`](plan-tests.md)). Voix enregistrée **après** les tests. Faits : [`sources.md`](sources.md) (T1…). Plans : [`storyboard.md`](storyboard.md). Critique de la V1 : [`grill-v1.md`](grill-v1.md) ; ancienne version : [`script-v1.md`](script-v1.md).

## Angle 16 Go (11/11, ta demande)

La vidéo parle à toute carte de 16 Go, pas à ta 5080, une carte chère que peu de gens ont : le hook dit « une carte graphique de seize gigas » ; la section 4 ajoute un repère sur une carte abordable (une Radeon de 16 Go, ≈ 37 tok/s, T39) et dit franchement que ta 5080 est le haut de la fourchette (mémoire deux fois plus rapide que celle d'une 5060 Ti, T40) ; la liste du soir commence par « une carte de douze à seize gigas » (T5). Le nom de ta carte n'apparaît plus qu'une fois, en section 4.

## Changements depuis la V1

1. **15 trous au lieu de 43**, numérotés **R1 à R15**, les mêmes dans le plan de tests (section 11), le storyboard et le téléprompteur. Un résultat = une phrase que tu dis avec tes mots ; les chiffres détaillés vont sur les cartes de verdict à l'écran.
2. **Plus de variantes A / B** : chaque phrase marche que le test réussisse ou non. Il n'y a plus qu'un texte à lire.
3. **Hook** : la question centrale est celle de la fin (« est-ce que ça remplace Claude ? »), posée vers 0:25 ; la moitié de modèle est le contraste ; « le vrai modèle, celui dont il vient » (flou) disparaît. Les trois fragments « Un jeu qui se joue. Un site complet. Un monde en 3D. » deviennent une phrase.
4. **Section 2 raccourcie** (342 → 238 mots, 2 min 30 → 1 min 45) : les trois commandes d'installation passent dans la liste « ce soir » de la fin, qui faisait doublon. On arrive au site vers 3:50 au lieu de 4:29, avec une relance à la fin de la section.
5. **« Niveau deux : le site… donc c'est la plus facile »** retiré : il cassait la montée de difficulté et n'était pas sourcé.
6. **La réflexion** : tu ne la règles plus (`--set reasoning-effort` non confirmé). La section 4 dit à la place le vrai piège, la limite de réponse, et ce que tu as fait (la limite montée à la main).
7. **Faits corrigés** : « cinquante-huit gigas à télécharger » → « une soixantaine » (la couche de prédiction s'ajoute, T33) ; « resident experts, tout est en RAM » → « tout ce que la carte ne garde pas est copié en RAM » (T8) ; le ticket du plantage touche des cartes de 8 **et** 12 Go, sa cause est trouvée et un correctif proposé (T23) ; l'échec du Coder dans Claude Code est revérifié (T27).
8. **Liaisons** : quatre « Du coup » et un « En effet » en tête de paragraphe ressemblaient à un quota. Varié : « sauf que », « en fait », « bon », « bref », « et justement », « parce que ».
9. **« Un token »** est expliqué dès la première apparition du compteur (section 1), plus à 5:36.
10. **Plantés et récoltés** : le message qui « accuse la RAM » (section 6) se referme sur « c'est comme ça que la cause de ce bug a été trouvée » ; le pronostic de 0:35 revient à la fin ; « monter la limite » (section 4) revient dans la liste du soir.
11. **Tes décisions du 11/11** : Pi remplace OpenCode (section 4 : « ses instructions font mille cinq cents tokens, contre sept mille quatre cents », T14, placé là pour ne pas charger la première minute en chiffres) ; l'installation passe par l'appli, et la liste du soir ajoute le Terminal (points deux et quatre).

## Ce que la vidéo dit (texte et sous-texte)

- **Texte** : la moitié d'un modèle géant, gardée pour le code, tourne sur ma carte de 16 Go et mes 32 Go de RAM. Voilà ce qu'elle écrit (un jeu, un site, une île en 3D), à quelle vitesse, face à Claude, et où ça casse.
- **Sous-texte** : ton PC de joueur peut aller plus loin que les fiches ne le disent, mais pas gratuitement : le verrou, c'est la RAM. **Montré, jamais dit** : la RAM libre qui tombe, le premier chargement, l'échec éventuel.
- **À ne pas recadrer** : ce n'est pas une vidéo contre Claude. Tu l'utilises, tu continues, et la comparaison porte sur trois demandes, sans classement.

## Structure

| Temps (≈) | Partie | Ce qui s'y passe | Relance qui la ferme |
|---|---|---|---|
| 0:00-0:42 | 0. Hook | Les trois résultats, la vitesse, le contraste « une moitié de modèle », la question, le plan en 4 livrables, le défi | « Niveau un : le jeu » |
| 0:42-2:03 | 1. Le jeu | **Une démo d'abord** | « Comment il tient ? » |
| 2:03-3:49 | 2. Comment ça tient | Experts, RAM, le Coder, ce que ça demande | « Un casse-briques, c'est le grand classique » |
| 3:49-4:42 | 3. Le site, puis l'île | Deux démos, le pronostic | « Et la vitesse ? » |
| 4:42-6:24 | 4. La vitesse | Les chiffres, le repère, le piège de la limite | « Maintenant, le vrai test » |
| 6:24-7:04 | 5. Claude | Les mêmes demandes | « Et là où ça casse ? » |
| 7:04-8:11 | 6. Où ça casse | Toi, puis les autres | « Alors, ça remplace ? » |
| 8:11-9:31 | 7. Verdict et « ce soir » | Ton verdict, la liste en 4 points, la suite | — |

Timecodes estimés à 145 mots/min, chaque trou compté pour 6 mots : c'est optimiste pour les trous qui sont des phrases, compte ≈ 10 min au total. À recaler sur la voix montée.

**Boucles ouvertes** : « est-ce que ça remplace Claude ? » (0:25 → section 7) ; le pronostic du spectateur (0:37 → section 7) ; « comment il tient ? » (2:00 → section 2) ; « là où ça casse » (0:33 → section 6) ; « jeudi, plus vite avec la même carte » (fin → 19/11).

**Conventions** : texte normal = voix. `[VISUEL : …]` = plan (P… = fichier du tournage, V… = plan du storyboard). `⟦Rn résultat : …⟧` = à remplir avec la fiche du plan (section 11), dans tes mots ; `⟦Rn à écrire : …⟧` = ton avis. Nombres en lettres pour la lecture. **Interdit à l'écran** : clé d'API, onglets du navigateur, dossiers de travail. **Aucun nom de chaîne ni de créateur** dans la voix.

---

## 0. Hook (0:00 – 0:42)

[VISUEL : V01-V05, un plan toutes les 1 à 3 s : le jeu qui tourne (P20), le site qui défile (P21), l'île qui tourne (P22), chaque fois avec le compteur de tok/s incrusté (P12-P14). GIF clavier à 0:07. Pas de titre ni de logo.]
Ce casse-briques, ce site, cette île en 3D : une IA les a écrits chez moi, sur une carte graphique de seize gigas, à ⟦R1 résultat : tok/s typique du jeu⟧ tokens par seconde.
⟦R2 résultat : combien ont marché du premier coup⟧ sur trois ont marché du premier coup.

[VISUEL : V06, le Gestionnaire des tâches (P04), « 32 Go » entouré ; la fiche Hugging Face, « half of its experts removed » surligné (P03).]
Sauf que le modèle complet ne rentre pas dans mes trente-deux gigas de RAM : j'ai pris sa moitié, gardée pour le code.
Alors, une moitié de modèle, est-ce que ça remplace Claude ?

[VISUEL : V07, le plan en 4 lignes qui s'écrivent avec la voix, sur fond noir ; la pastille « PRONOSTIC : LOCAL contre CLAUDE » apparaît à 0:22 et reste en bas jusqu'à la section 5.]
Au programme : la vitesse, ce qu'il faut à ton PC, le même test donné à Claude, et là où ça casse.
Ton pronostic : le local tient, ou Claude écrase ?

---

## 1. Niveau un : le jeu (0:42 – 2:03)

[VISUEL : V08, le terminal en deux volets (P12) : Pi à gauche, le moniteur de Strata à droite.]
Niveau un : le jeu.
À gauche, Pi, l'outil qui laisse l'IA écrire les fichiers elle-même, et qui ne touche pas à la config de mon Claude. À droite, le compteur de Strata, le programme qui fait tourner le modèle.
*(Si tu as dû passer à OpenCode, plan B 9.10 : remplace « Pi » par « OpenCode » ici et en section 5, et coupe la dernière phrase de la section 4.)*

[VISUEL : V09, le prompt anglais collé (P12), traduction en sous-titre ; GIF pièce d'arcade.]
Ma demande, je l'écris en anglais, parce que sa propre doc dit qu'il est plus faible dans les autres langues. Un casse-briques complet, dans un seul fichier : six rangées de briques, la raquette à la souris, trois vies, des bonus qui tombent, des bruitages, des étincelles quand une brique casse, et zéro erreur dans la console.
Règle du jeu : un seul essai. Et s'il plante, je lui renvoie l'erreur une fois, sans toucher au code, comme une dernière pièce à l'arcade.

[VISUEL : V10, l'accéléré de la génération, l'horloge visible, le compteur en gros (P12).]
Je lance. Et regarde le compteur à droite : ⟦R1⟧ tokens par seconde. Un token, c'est à peu près trois quarts de mot.

[VISUEL : V11, le jeu ouvert, la partie, la console F12 (P20) ; la carte de verdict « JEU ».]
Il a fini. Je l'ouvre, et c'est le moment de vérité : ⟦R3 résultat : le jeu en une phrase⟧.

[VISUEL : V11e, la miniature de la vidéo du 09/11 (C5), 2 s.]
Bon. Lundi dernier, je te disais que seize gigas de carte suffisent, si tu prends le bon fichier. Sauf que là, le modèle est bien plus gros que ma carte. Comment il tient ?

---

## 2. Comment ça tient chez moi (2:03 – 3:49)

[VISUEL : V12, un schéma court sur fond noir (la carte / la RAM / le SSD), entre deux vraies images : la page GitHub de Strata (P02), « MIT » en gros plan.]
En fait, le modèle d'origine est découpé en centaines de petits spécialistes, les experts. Et à chaque mot, il n'en réveille que quelques-uns : six milliards de paramètres au travail, sur cent vingt-cinq.
Strata, c'est le programme qui range tout ça. La carte garde les experts les plus utilisés, la RAM garde le reste, et une grosse table reste sur le SSD. Il est gratuit, et open source.

[VISUEL : V13, la doc de Strata (C4), la phrase « a 32 GB PC with a 12 to 16 GB GPU runs the Coder » surlignée ; la fiche du Coder (P03), « experimental » surligné ; le tableau des scores.]
Sauf que sa règle, c'est : ta RAM doit contenir les experts, plus une dizaine de gigas pour Windows. Et avec trente-deux gigas de RAM et une carte de seize, sa doc ne prévoit qu'un seul fichier : le Coder. Le même modèle, coupé de moitié, gardé pour le code, et ses auteurs le disent eux-mêmes expérimental.
Ils annoncent quatre-vingt-quinze pour cent du score de code du modèle complet. Ça, c'est leur chiffre. Moi, je regarde ce qu'il fait.

[VISUEL : V15, le téléchargement accéléré, « Preparing your model », la RAM qui monte (P07), la RAM au plus bas (P15), la ligne du mode (P06).]
Et ce que ça demande, en vrai : une soixantaine de gigas à télécharger, et un premier chargement de ⟦R4 résultat : durée, et si le PC s'est figé⟧.
Il faut aussi tout fermer, navigateur compris, parce que pendant qu'il écrit, la RAM libre descend à ⟦R5 résultat : RAM libre au plus bas⟧.
Et sur l'écran de lancement du Terminal, regarde cette ligne. Si tu lis « resident experts », tout ce que la carte ne garde pas est copié en RAM, et il ne va plus rien chercher sur le SSD pendant qu'il répond. Chez moi : ⟦R6 résultat : resident ou mmap⟧.
Bon, ça tient. Mais un casse-briques, c'est le grand classique. Voyons s'il tient sur autre chose.

---

## 3. Niveau deux, puis le boss (3:49 – 4:42)

[VISUEL : V17, le prompt du site (P13), l'accéléré avec le compteur ; V18, le site ouvert, la FAQ, la version téléphone (P21), la carte de verdict « SITE ».]
Niveau deux : le site, ce qu'on demande le plus souvent à une IA. Une page de présentation pour une appli de paiement qui n'existe pas : un grand titre avec un téléphone dessiné, trois cartes, trois tarifs, une FAQ qui s'ouvre et se ferme, et ça doit tenir sur un téléphone.
⟦R7 résultat : le site en une phrase⟧.

[VISUEL : V19, GIF « boss » sur fond noir, puis le prompt de l'île (P14) ; V19c, ton pronostic écrit à l'écran.]
Et maintenant, le boss final : une île en cubes, en 3D. Un relief généré, de l'eau, au moins quinze arbres, la souris pour tourner autour, et la touche N pour passer à la nuit.
Là, c'est le plus dur, parce qu'il doit calculer le relief et la lumière sans jamais voir ce qu'il dessine.
Mon pronostic avant de lancer : ⟦R8 à écrire : ton pronostic⟧.

[VISUEL : V20, l'île qui s'affiche (ou pas), la rotation, le zoom, la touche N (P22), la carte de verdict « 3D ».]
Et là : ⟦R9 résultat : l'île en une phrase⟧.

---

## 4. La vitesse, en vrai (4:42 – 6:24)

[VISUEL : V21, le moniteur en plein écran (P10, P12-P14), les trois valeurs en gros.]
Bref, et la vitesse ? Le compteur affichait ⟦R1⟧ tokens par seconde pour le jeu, et ⟦R10 résultat : tok/s du site et de l'île⟧ pour le site et l'île.

[VISUEL : V22, le ticket GitHub du repère (C1) : « RTX 5070 Ti », « Ryzen 7 9700X », « 70.4 », « thinking off », « Speed only: no correctness check » surlignés.]
Du coup, pour te donner un repère : un utilisateur d'une 5070 Ti, avec le même processeur que moi et à peu près la même RAM, mesure environ soixante-dix tokens par seconde avec ce modèle. Mais avec la réflexion coupée, et sans vérifier si le code marche.
Chez moi : ⟦R11 résultat : face au repère, et pourquoi⟧.

[VISUEL : V22e-V22f, le ticket GitHub de la Radeon (#2250) : « 9600 XT », « 30.3 GiB », « 37.6 » surlignés ; puis deux barres de bande passante : 5080 « 960 Go/s », 5060 Ti « 448 Go/s » (T39, T40).]
Et si ta carte est plus abordable ? Sur une Radeon de seize gigas, avec trente gigas de RAM, un autre utilisateur mesure environ trente-sept tokens par seconde, toujours avec ce modèle. Parce que moi, je te le dis franchement : j'ai une 5080, une carte haut de gamme, et sa mémoire est deux fois plus rapide que celle d'une 5060 Ti. Donc mes chiffres, c'est plutôt le haut de la fourchette. Sur ta carte de seize gigas, ça tourne aussi, juste moins vite.

[VISUEL : V23, une barre « réponse = 1/8 du contexte » où la réflexion mange la place du code ; puis `models.json` de Pi, la ligne `"maxTokens": 32000` surlignée (P09).]
Et justement, la réflexion, c'est le piège. Par défaut, ce modèle réfléchit longtemps avant d'écrire, et cette réflexion compte dans la longueur maximale de sa réponse. Avec la config que Strata écrit pour Pi, cette limite, c'est un huitième du contexte : huit mille tokens chez moi. Un jeu complet plus la réflexion, ça peut déborder, et le fichier s'arrête au milieu.
Du coup, avant le premier test, j'ai monté cette limite à la main dans le fichier de Pi. La ligne est en description.
*(Si tu ne l'as pas fait, coupe ces deux phrases.)*

[VISUEL : V23d, le tableau de vitesses du projet (C4), la ligne du Coder surlignée, « moteur ancien » ; V23e, le moniteur, puis les deux barres « Pi 1 500 / OpenCode 7 400 ».]
Dernière chose : la vitesse baisse quand la conversation grandit. Le projet le publie lui-même : sur une autre machine, avec un ancien moteur, le Coder passe de cinquante-neuf à quarante-trois tokens par seconde entre mille et cent vingt-huit mille tokens de contexte. Donc plus l'agent lit de code, plus il ralentit. C'est pour ça que j'ai pris Pi : ses instructions font mille cinq cents tokens, contre sept mille quatre cents pour OpenCode. Moins à relire à chaque demande.

---

## 5. Le même test, donné à Claude (6:24 – 7:04)

[VISUEL : V24, l'écran partagé : à gauche les trois résultats locaux (P20-P22), à droite ceux de Claude (P30-P32) ; la pastille du pronostic revient.]
Maintenant, le vrai test : les trois mêmes demandes, mot pour mot, données à Claude avec mon abonnement. Un seul essai chacune, aucune relance.
Ce n'est pas le même outil : Pi d'un côté, Claude Code de l'autre. Par contre, la demande est la même, et je note la même chose : la durée, et ce qui marche sur les cinq points.
⟦R12 résultat : Claude, une phrase par test⟧.
Donc, sur ces trois demandes : ⟦R13 à écrire : la comparaison, et ce qui sépare les deux⟧.
Attention quand même : trois essais, une tentative chacun. Ça dit ce qui s'est passé chez moi ce jour-là, rien de plus.

---

## 6. Là où ça casse (7:04 – 8:11)

[VISUEL : V26, ton incident s'il y en a eu (P16), le message exact ; sinon l'écran sans erreur. Puis les tickets (C2, C3), la page des versions (C6).]
Chez moi : ⟦R14 résultat : ce qui a cassé, ou « rien n'a planté »⟧.
Et chez les autres ? Sur GitHub, un ticket encore ouvert décrit le moteur qui plante avec ce Coder sur certaines longues demandes. Plusieurs utilisateurs l'ont eu, sur des cartes de huit et de douze gigas. Le message accuse la RAM. Sauf que des utilisateurs ont trouvé la vraie cause : un bug du moteur, avec un correctif proposé, pas encore dans la version que j'ai testée.
Un utilisateur de 5080 rapporte une autre erreur, « non-finite logits », avec d'autres fichiers du même modèle. Et un autre testeur a vu ce Coder rater une tâche de code dans Claude Code, là où d'autres versions du modèle l'ont réussie.
Strata est jeune : le projet a été créé le vingt-quatre septembre, et il sort une version tous les deux ou trois jours. Donc note ta version. Et si ça casse chez toi, copie le message exact : c'est comme ça que la cause de ce bug a été trouvée.

---

## 7. Le verdict, et ce soir (8:11 – 9:31)

[VISUEL : V27, les trois résultats locaux côte à côte, puis la RAM et la VRAM qui reviennent quand on arrête Strata (P41).]
Alors, est-ce que ça remplace mon abonnement ? ⟦R15 à écrire : ton verdict, et ce qui t'a le plus surpris⟧.

[VISUEL : V28, la liste qui s'écrit avec la voix, chaque ligne avec sa vraie capture (P04, P05, P07, P09).]
Si tu veux le refaire ce soir, voilà la liste.
Un : il te faut une carte de douze à seize gigas, au moins trente-deux gigas de RAM, et environ quatre-vingt-dix gigas de disque libres.
Deux : tu installes l'appli Strata, le lien est en description. Dans sa liste de modèles, elle te dit si chacun tient sur ton PC avant de le télécharger.
Trois : tu prends le Coder, sans les images, et tu fermes tout, navigateur compris, avant de le lancer.
Quatre : tu installes aussi le Terminal de Strata, une ligne en description, tu branches Pi avec « strata connect pi », et tu montes la limite de réponse.
Par contre, si tu as plus de RAM, d'après la doc, à quarante-huit gigas tu passes aux petites tailles du modèle complet, et à soixante-quatre, à toutes.
Si c'est ta toute première IA en local, commence plutôt par la vidéo sur LM Studio : je te la mets là.

[VISUEL : V29, la pastille du pronostic revient en grand, « QUI AVAIT RAISON ? », puis la carte vers la vidéo du jeudi 19/11.]
Bref, et ton pronostic du début ? Dis-moi en commentaire si tu avais raison, avec ta carte et ta RAM.
Jeudi, on cherche comment aller plus vite avec la même carte. Elle arrive juste là.

---

## Faits utilisés

| Ce que dit le script | Section | Source | Statut (11/11) |
|---|---|---|---|
| La version complète ne rentre pas dans 32 Go de RAM ; le Coder, moitié des experts, gardée pour le code | 0, 2 | T5, T6, T15 | ✅ (DEV) |
| Pi : prompt et outils ≈ 1 500 tokens, OpenCode ≈ 7 400 ; Pi a son propre dossier (`~/.pi/agent`) ; `strata connect claude-code --write` écrirait dans `~/.claude/settings.json` | 1, 4 | T14 | ✅ (code de Strata, DEV) |
| Le Coder plus faible hors de l'anglais | 1 | T5 | ✅ (DEV) |
| Un token ≈ trois quarts de mot | 1 | T36 | ✅ (DEV) |
| 125 milliards de paramètres, 6 milliards actifs (modèle d'origine) | 2 | T25 | ✅ (fiche Qwen) |
| La carte garde les plus utilisés, la RAM le reste, une table sur le SSD ; gratuit, open source (MIT) | 2 | T25, T24, T8 | ✅ |
| RAM ≥ experts + ≈ 10 Go ; 32 Go + carte de 12 à 16 Go = le Coder | 2 | T5, T15 | ✅ (DEV) |
| « expérimental » ; 95 % du score de code, d'après ses auteurs | 2 | T6 | ✅ (DEV, attribué) |
| Une soixantaine de gigas à télécharger | 2 | T6, T33 | ✅ (58,4 + ≈ 5,2 Go) |
| « resident experts » : ce que la carte ne garde pas est copié en RAM, rien lu sur le SSD | 2 | T8 | ✅ (DEV) |
| Repère : 5070 Ti, même processeur, ≈ 70 tok/s, réflexion coupée, sans test de justesse | 4 | T7 | ✅ (une mesure) |
| Limite de réponse = ⅛ du contexte, réflexion comprise ; 8 192 à 64K | 4 | T13 | ✅ (code) |
| La limite montée à la main dans `models.json` de Pi (`maxTokens`) | 4 | T31, T37 | ✅ (code, doc de Pi) ; à dire seulement si tu l'as fait |
| Le Coder passe de 59 à 43 tok/s entre 1K et 128K de contexte (autre machine, moteur ancien) | 4 | T30 | ✅ (DEV, ancien) |
| Ticket ouvert : plantage du Coder sur certaines longues demandes, cartes de 8 et 12 Go, le message accuse la RAM, cause trouvée, correctif proposé pas dans la 0.2.13 | 6 | T23 | ✅ (ticket #5104 relu le 11/11) |
| Un utilisateur de 5080 : « non-finite logits » avec d'autres fichiers | 6 | T11 | ⚠️ non confirmé par le développeur |
| Un testeur a vu le Coder rater une tâche dans Claude Code, d'autres versions l'ont réussie | 6 | T27 | ✅ (description revérifiée le 11/11) |
| Projet créé le 24/09 ; une version tous les 2 à 3 jours | 6 | T1 | ✅ |
| 48 Go : les petites tailles ; 64 Go : toutes | 7 | T5 (MODELS.md) | ✅ (DEV) |
| L'appli dit si un modèle tient avant de le télécharger ; Pi se branche avec `strata connect pi` | 7 | T38, T14 | ✅ (DEV) |
| Les vidéos du 09/11 et du 02/11 ; celle du 19/11 | 1, 7 | `calendrier.md` | ✅ |

**Non dit exprès** : « Flash-Next tourne sur 32 Go » (c'est le Coder), « 125 milliards » pour le Coder lui-même, tout classement général local contre Claude, tout chiffre de 64 ou 128 Go de RAM comme étant le tien, tout tok/s avant ta mesure.

## Mesure (11/11, sur la voix seule, sans `[VISUEL]` ni notes en italique)

Mesurée par script, chaque trou compté pour 1 mot (rempli : 3 à 15 mots). Liste « stricte » des liaisons : donc, du coup, en fait, sauf que, en effet, voilà, bref, par contre, justement, bon, alors. Liste « large » : + mais, parce que, maintenant, attention, et là.

| | Mots de voix | Durée à 145 mots/min | Avec les trous remplis (≈ 6 mots chacun) | Liaisons / 100 mots (stricte / large) |
|---|---|---|---|---|
| V1 (variante A) | 1 354 | 9 min 20 | ≈ 9 min 50 | 1,77 / 2,81 |
| **V2** | **1 296** (15 trous, 17 emplacements) | 8 min 56 | ≈ 9 min 30, plutôt **≈ 10 min** avec tes phrases (R3, R7, R9, R12, R13, R15 sont des phrases) | **1,62 / 2,31** |

- **Hook** : 92 mots (≈ 95 remplis), soit ≈ 39 s à 145 mots/min et ≈ 34 s à 165. La question centrale tombe vers 0:25 ; le plan en 4 livrables de 0:25 à 0:34 ; le défi à 0:35, affiché dès 0:22.
- **Nombres dans la première minute** : seize gigas, R1, R2 (« sur les trois »), trente-deux gigas : 4. Les chiffres de Pi (1 500 contre 7 400) sont en section 4 pour cette raison.
