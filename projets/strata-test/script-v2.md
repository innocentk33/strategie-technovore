# Le meilleur modèle possible pour 16 Go de VRAM (Strata, testé) : script (V2, 11/11/2026 ; démos réordonnées le 14/11 ; trous remplis le 14/11, prêt pour la voix ; réécrit dans ta voix le 14/11 au soir)

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
12. **Mis à jour le 13/11** : tout passe par l'appli (pas de Terminal) : sa page Monitor donne les tok/s et la lecture disque, Pi se branche à la main sur l'adresse de sa page Serving, le contexte est à 128K. Changés : la phrase du mode (section 2, la case « Disk read » au lieu de l'écran du Terminal), le piège de la limite (section 4, 16 384 au lieu de 8 000), le point quatre de la liste du soir.
13. **Mis à jour le 13/11 (soir), ta décision** : le boss final n'est plus l'île en 3D mais un **mini-Minecraft** (marcher, sauter, casser et poser des blocs ; prompt dans le plan, 6.3). Changés : le hook (« ce mini-Minecraft »), la section 3 (le boss et sa raison d'être le plus dur), R8 à R10.
14. **Mis à jour le 14/11, tes décisions après les tests** : quatre démos, dans ton ordre de montage, **l'île en 3D, le site Sillage, le mini-Minecraft, le casse-briques**. La section 1 devient l'île (Pi, le prompt en anglais, le compteur) ; la section 3 raconte le site **en deux essais** (seul : en anglais et bloqué sur Chrome ; avec un plan de Claude : Sillage), puis le mini-Minecraft et ses trois relances, puis le casse-briques pour finir. La vitesse (section 4) vient de **l'histoire du dragon**, déjà enregistrée. Le verdict (section 7) dit ta conclusion : **un abonnement à 20 $ pour écrire le plan, le modèle local pour l'exécuter** ; même sans plan, il s'en sort bien, et le gros du temps perdu vient de Chrome ; la limite de 32 000 n'a pas suffi une fois. « Une relance par test » est remplacé par « je compte les relances » (le mini-Minecraft en a eu trois). **Encore à revoir** : la section 5 (Claude) et la ligne 3 du plan du hook, qui annoncent les mêmes demandes données à Claude (voir R12).
15. **Mis à jour le 14/11 (après-midi), prêt pour la voix** : le hook nomme **Qwen 3.8 Flash Next** et dit « une seule demande par test, rien d'automatique » (ta demande), suivi tout de suite de « une moitié de modèle » ; la phrase des 32 Go de RAM quitte le hook (elle est en section 2) pour que la question tombe avant 0:30. **Tous les trous sont remplis** avec les sessions de Pi, les captures du moniteur et les rushes (T41, T45) : la vitesse (près de 70 en moyenne, 51 pour le dragon), la demi-heure du premier chargement, la RAM pleine, la lecture disque, les quatre résultats. **R8 coupé** (aucun pronostic écrit avant le test). **Section 5 réécrite** : une seule comparaison honnête, le site de Claude (Latitude Sud). R15 est une **proposition** : change-la si ce n'est pas ce qui t'a surpris. Les plans renvoient aux vrais fichiers (codes TT, INST, CONF, DRAGON… dans le storyboard).
16. **Mis à jour le 14/11 (soir), ta demande : ton style et tes transitions.** Le hook dit ta phrase : « ces tests ont été réalisés avec Qwen 3.8 Flash Next, qui tourne sur une carte de seize gigas […], et tout ça, à partir d'un seul prompt » ; « une seule demande par test, rien d'automatique… » et « deux sur quatre du premier coup » sont retirés (plans V05d et V05c coupés au storyboard). Toute la voix est relissée d'après ce que tu changes toi-même à l'oral (écarts téléprompteur / sous-titres de Qwen 4 et de l'installation) : moins de deux-points et de fragments, des phrases entières, tes liaisons (« par contre », « donc », « du coup », « en gros », « là », « bon, maintenant »), « prompt » au lieu de « demande » quand c'est toi qui parles, les « Bref » retirés, « Allez, salut ! » à la fin. Aucun fait, chiffre, plan ni ordre de section ne change.

## Ce que la vidéo dit (texte et sous-texte)

- **Texte** : la moitié d'un modèle géant, gardée pour le code, tourne sur ma carte de 16 Go et mes 32 Go de RAM. Voilà ce qu'elle écrit (une île en 3D, un site, un mini-Minecraft, un casse-briques), à quelle vitesse, face à Claude, et où ça casse. Et la meilleure formule : un petit abonnement écrit le plan, le modèle local l'exécute.
- **Sous-texte** : ton PC de joueur peut aller plus loin que les fiches ne le disent, mais pas gratuitement : le verrou, c'est la RAM. **Montré, jamais dit** : la RAM libre qui tombe, le premier chargement, l'échec éventuel.
- **À ne pas recadrer** : ce n'est pas une vidéo contre Claude. Tu l'utilises, tu continues, et la comparaison porte sur trois demandes, sans classement.

## Structure

| Temps (≈) | Partie | Ce qui s'y passe | Relance qui la ferme |
|---|---|---|---|
| 0:00-0:40 | 0. Hook | Les quatre résultats, le nom du modèle, la vitesse, « un seul prompt », le contraste « la moitié d'un modèle », la question (≈ 0:22), le plan en 4 livrables, le défi | « Niveau un : une île en 3D » |
| 0:40-2:15 | 1. L'île en 3D | **Une démo d'abord** | « Comment il tient ? » |
| 2:15-4:05 | 2. Comment ça tient | Experts, RAM, le Coder, ce que ça demande | « Une île, on ne fait que la regarder » |
| 4:05-7:15 | 3. Le site en deux essais, le mini-Minecraft, le casse-briques | Trois démos, le plan de Claude, le pronostic | « Bon, maintenant, la vitesse » |
| 7:15-9:30 | 4. La vitesse | L'histoire du dragon, le repère, le piège de la limite | « Ça n'a pas toujours suffi » (récolté en 7) |
| 9:30-10:00 | 5. Et Claude ? | Le site de Claude en une phrase, face à l'essai 1 ; le plan de Sillage | « Où est-ce que ça casse ? » |
| 10:00-11:10 | 6. Où ça casse | Toi, puis les autres | « Alors, ça remplace ? » |
| 11:10-13:50 | 7. Verdict et « ce soir » | Ton verdict (le plan à 20 $), la limite, la liste en 4 points, la suite | — |

Timecodes estimés : compte **≈ 14 min 30 à 15 min 30** de voix (mesure du 14/11 au soir, après la réécriture dans ta voix : 2 340 mots au script, + 140 par rapport à l'après-midi, surtout des liaisons ; 14 min 30 à 155 mots/min, 15 min 30 à 145). Le hook fait 105 mots ; la question centrale tombe vers 0:22. À recaler sur la voix montée.

**Boucles ouvertes** : « est-ce que ça remplace Claude ? » (0:25 → section 7) ; le pronostic du spectateur (0:37 → section 7) ; « comment il tient ? » (2:00 → section 2) ; « là où ça casse » (0:33 → section 6) ; « jeudi, plus vite avec la même carte » (fin → 19/11).

**Conventions** : texte normal = voix. `[VISUEL : …]` = plan (V… = plan du storyboard ; TT, INST, CONF, DRAGON, BRICK, T3, VOY, MON0-4 = les rushes et captures, listés en tête du storyboard ; P… et C… = captures à faire). Plus aucun trou ⟦…⟧ depuis le 14/11. Nombres en lettres pour la lecture. **Interdit à l'écran** : clé d'API, onglets du navigateur, dossiers de travail. **Aucun nom de chaîne ni de créateur** dans la voix.

---

## 0. Hook (0:00 – 0:40)

[VISUEL : V01-V05c, un plan toutes les 1 à 3 s : l'île qui tourne (TT 0:06), Sillage (TT 1:12), le mini-Minecraft, un bloc posé (TT 2:00), le casse-briques (TT 2:36) ; la moyenne du moniteur en gros (MON3, « 67.8 tok/s »). GIF clavier à 0:09. Pas de titre ni de logo. V05d et V05c (« 1 demande par test », « 2 / 4 ») sont coupés le 14/11 (soir) avec leurs phrases.]
Cette île en 3D, ce site, ce mini-Minecraft, ce casse-briques, c'est une IA qui les a écrits, chez moi.
Ces tests ont été réalisés avec Qwen 3.8 Flash Next, qui tourne sur une carte de seize gigas, à près de soixante-dix tokens par seconde. Et tout ça, à partir d'un seul prompt.

[VISUEL : V06, la fiche Hugging Face, « half of its experts removed » surligné (P03) ; un schéma court, la moitié des experts qui s'éteint, « gardée pour le code » écrit à l'écran.]
Par contre, ce n'est que la moitié d'un modèle.
Alors, est-ce que ça remplace Claude ?

[VISUEL : V07, le plan en 4 lignes qui s'écrivent avec la voix, sur fond noir ; la pastille « PRONOSTIC : LOCAL contre CLAUDE » apparaît vers 0:25 et reste en bas jusqu'à la section 5.]
Je te montre la vitesse, ce qu'il faut à ton PC, le site fait par Claude, et là où ça casse.
Et toi, c'est quoi ton pronostic ? Le local tient le coup, ou Claude l'écrase ?

---

## 1. Niveau un : une île en 3D (0:40 – 2:15)

[VISUEL : V08, Pi devant le moniteur de Strata (BRICK 0:00, plan générique : l'écran de Pi est encore vide) ; le moniteur seul (CONF 0:12-0:40).]
Niveau un : une île en 3D.
À gauche, tu as Pi, l'outil qui laisse l'IA écrire les fichiers elle-même, et qui ne touche pas à la config de mon Claude. Et à droite, c'est le compteur de Strata, le programme qui fait tourner le modèle.

[VISUEL : V09, le prompt anglais de l'île en carte texte (le lancement n'a pas été filmé), traduction en sous-titre ; GIF pièce d'arcade.]
Mon prompt, je l'écris en anglais. Pourquoi ? Parce que sa propre doc dit qu'il est moins bon dans les autres langues. Je lui demande une île en cubes, en 3D, dans un seul fichier, avec un relief généré, de l'eau, au moins quinze arbres, la souris pour tourner autour, la touche N pour passer à la nuit, et zéro erreur dans la console.
Et la règle du jeu est simple, je ne touche jamais au code. S'il bloque, je le relance avec une phrase, et chaque relance, je la compte, comme une pièce de plus à l'arcade.

[VISUEL : V10, l'heure de départ (23:42) en incrustation ; la génération en accéléré, recadrée sur le moniteur qui passe en « Generating » (BRICK 0:04-0:21, plan générique, prompt flouté).]
Je lance. Et là, regarde le compteur à droite, ce sont des tokens par seconde. En gros, un token, c'est à peu près trois quarts de mot. La vitesse exacte, on la mesure un peu plus loin.

[VISUEL : V11, l'île ouverte : la rotation à la souris, le zoom, la nuit et les étoiles (TT 0:00-0:40) ; la carte de verdict « ÎLE ».]
Quinze minutes et demie plus tard, il a fini. Une seule demande, aucune relance. Donc je l'ouvre, et là, c'est le moment de vérité. Elle tourne à la souris, elle zoome, et quand j'appuie sur N, la nuit tombe, avec les étoiles.

[VISUEL : V11e, la miniature de la vidéo du 09/11 (C5), 2 s.]
Lundi dernier, je te disais que seize gigas de carte suffisent, si tu prends le bon fichier. Sauf que là, le modèle est bien plus gros que ma carte. Du coup, comment il tient ?

---

## 2. Comment ça tient chez moi (2:15 – 4:05)

[VISUEL : V12, un schéma court sur fond noir (la carte / la RAM / le SSD), entre deux vraies images : la page GitHub de Strata (P02), « MIT » en gros plan.]
En fait, le modèle d'origine est découpé en centaines de petits spécialistes, qu'on appelle des experts. Et à chaque mot, il n'en réveille que quelques-uns. Sur cent vingt-cinq milliards de paramètres, il n'y en a que six milliards au travail.
Et Strata, c'est le programme qui range tout ça. La carte garde les experts les plus utilisés, la RAM garde le reste, et une grosse table reste sur le SSD. En plus, il est gratuit et open source.

[VISUEL : V13, la doc de Strata (C4), la phrase « a 32 GB PC with a 12 to 16 GB GPU runs the Coder » surlignée ; la fiche du Coder (P03), « experimental » surligné ; le tableau des scores.]
Par contre, sa règle, c'est que ta RAM doit contenir les experts, plus une dizaine de gigas pour Windows. Donc avec trente-deux gigas de RAM et une carte de seize, sa doc ne prévoit qu'un seul fichier, le Coder. C'est le même modèle, mais coupé de moitié et gardé pour le code. Et ses auteurs eux-mêmes disent qu'il est expérimental.
D'après eux, il garde quatre-vingt-quinze pour cent du score de code du modèle complet. Ça, c'est leur chiffre. Moi, ce qui m'intéresse, c'est ce qu'il fait.

[VISUEL : V15, le téléchargement, « 58.4 GB to download », l'horloge à 19:30 (INST 1:42-2:24) ; « Hello, I'm Strata » et le premier message à 20:06 (INST 3:00-3:06) ; la RAM au moniteur, « 30.8 / 31 GB » en rouge (MON3) ; la case « Disk read » au repos (MON2, 0.1) puis pendant l'histoire du dragon (DRAGON 0:33-0:39, 165 à 183 Mo/s).]
Maintenant, ce que ça demande en vrai. Déjà, une soixantaine de gigas à télécharger. Chez moi, entre le clic sur Télécharger et mon premier message, il s'est passé un peu plus d'une demi-heure.
Il faut aussi tout fermer, navigateur compris. Parce que pendant qu'il écrit, ma RAM est pleine, trente virgule huit gigas sur trente et un.
Et regarde bien cette case du moniteur, c'est la lecture sur le disque. Au repos, elle est à zéro. Mais dès qu'il écrit, elle monte autour de deux cents mégas par seconde. En gros, la RAM est pleine, donc une partie passe par le SSD.
Bon, ça tient. Par contre, une île, on ne fait que la regarder. Donc maintenant, voyons ce qu'il fait de ce qu'on demande le plus souvent à une IA.

---

## 3. Niveau deux : le site, en deux essais ; puis le plus dur, et le grand classique (4:05 – 7:15)

[VISUEL : V17a-V17b, le prompt « Sanaka Voyages » en carte texte et les 12 photos (non filmé) ; V17c-V17d, l'essai 1 en anglais qui défile (TT 3:11-3:57) ; puis l'horloge qui saute de 21:46 à 23:37.]
Niveau deux : le site. Je lui demande le site d'une agence de voyage qui n'existe pas, avec de vraies photos. Un écran d'accueil qui zoome doucement, six destinations, des avis qui défilent tout seuls, une galerie qui s'ouvre en plein écran, et le tout doit tenir sur un téléphone. Les photos, c'est moi qui les lui ai données.
Premier essai, et là, ça se passe mal. Il écrit tout le site en une demi-heure, sauf qu'il l'écrit en anglais, alors que je lui demande du français. Et à la fin, il veut se tester tout seul. Il ouvre un Chrome invisible, et Chrome ne lui rend jamais la main. Du coup, il est resté bloqué presque deux heures, jusqu'à ce que je l'arrête.

[VISUEL : V18a-V18f, le plan de Claude (`AGENTS.md`, puis `i18n.js` et ses textes en français, à capturer) ; la carte « LE PLAN DE CLAUDE : 770 lignes · 228 textes en français · un tiers de la page déjà dedans » ; Pi qui suit le plan (VOY 0:00-0:09, puis 0:57-1:06) ; Sillage ouvert (TT 0:41-1:28) ; la carte de verdict « SITE ».]
Donc pour le deuxième essai, j'ai fait autrement. Je donne mes photos à Claude, et je lui demande un plan pour ce modèle-là, avec les étapes, des morceaux de code, et tous les textes en français déjà écrits. Le modèle local, lui, n'a plus qu'à suivre le plan, étape par étape.
Et cette fois, il m'écrit un site en français en dix-sept minutes, avec zéro erreur au contrôle. Bon, il s'est encore bloqué deux fois sur Chrome, mais la page, elle, était finie.
Par contre, attention. Un tiers des lignes de la page étaient déjà dans le plan. Et le plan a changé la commande. Il n'y a plus de galerie en plein écran, et les avis ne défilent plus. À la place, on a un diaporama dans l'accueil, et une fiche qui s'ouvre pour chaque destination.
Mais au final, le résultat a vraiment l'air d'un site d'agence. Le Kilimandjaro en grand à l'accueil, les destinations avec leurs prix, et des témoignages de voyageurs.

[VISUEL : V19, GIF « boss » sur fond noir, puis le prompt du mini-Minecraft envoyé dans Pi (T3 0:00-0:14).]
Niveau trois, le plus dur : un mini-Minecraft. Un monde en cubes généré, des textures en pixels dessinées par le code, et je dois pouvoir marcher dedans, sauter, casser et poser des blocs. Et là, c'est vraiment le boss, parce qu'il doit inventer le monde, les textures et les collisions sans jamais voir ce qu'il dessine.
*(R8, ton pronostic, est coupé le 14/11 : il n'a pas été écrit avant le test.)*

[VISUEL : V20a-V20d, la réponse « index.html written and verified » en carte texte, puis « 0 fichier » ; les trois relances et le bug `pos.concat` en cartes texte ; le monde, la balade, les blocs posés (TT 1:29-2:27) ; la carte de verdict « 3D ».]
Premier essai, il me répond « fichier écrit et vérifié ». Sauf que quand j'ouvre le dossier, il est vide. Il n'a rien écrit du tout. Du coup, il a fallu trois relances, trente-cinq minutes en tout, et à la dernière, il a même trouvé un vrai bug dans son propre code. Mais au bout du compte, on se balade dans un vrai petit monde, avec des arbres et du relief, et on peut construire avec de la terre, de la pierre, du sable et du bois.

[VISUEL : V20e-V20g, le prompt du casse-briques collé dans Pi (CONF 4:48-5:08), puis la partie : les vies, le game over, les bonus « WIDE » et « 3x » (TT 2:28-2:51) ; la carte de verdict « JEU ».]
Et pour finir, le grand classique : un casse-briques. Six rangées de briques, la raquette à la souris, trois vies, des bonus qui tombent, des bruitages, des étincelles quand une brique casse, et toujours zéro erreur dans la console.
Celui-là, il l'a fait en huit minutes, avec une seule demande. Et il a même écrit un script pour tester son propre jeu. Et ça se joue vraiment. Tu as les vies, l'écran de game over, et les bonus qui élargissent la raquette ou qui triplent la balle.

---

## 4. La vitesse, en vrai (7:15 – 9:30)

[VISUEL : V21, l'histoire du dragon qui s'écrit dans Pi (DRAGON 0:21-0:45), puis la ligne « 590 · 50.8 » du moniteur surlignée (MON3) ; V21b, les moyennes « 69.4 » et « 66.1 tok/s » (MON2, MON4), puis les lignes 42.9 (MON4) et 83.6 (MON3).]
Bon, maintenant, la vitesse. Pour la mesurer sans les outils au milieu, je lui ai demandé une petite histoire, celle d'un dragon qui adore les jeux vidéo. Presque pas de réflexion, une réponse courte, et là, le moniteur affiche cinquante et un tokens par seconde.
Et pendant les vrais tests, avec tout le code ? Bizarrement, c'est plus rapide. Près de soixante-dix en moyenne, et selon la demande, ça va de quarante-trois à quatre-vingt-quatre.

[VISUEL : V22, le ticket GitHub du repère (C1) : « RTX 5070 Ti », « Ryzen 7 9700X », « 70.4 », « thinking off », « Speed only: no correctness check » surlignés.]
Pour te donner un repère, un utilisateur d'une 5070 Ti, avec le même processeur que moi et à peu près la même RAM, mesure environ soixante-dix tokens par seconde avec ce modèle. Par contre, lui, il a coupé la réflexion, et il ne vérifie pas si le code marche.
Chez moi, c'est du même ordre. Près de soixante-dix pendant les tests, mais avec la réflexion allumée, et du code qui doit marcher.

[VISUEL : V22e-V22f, le ticket GitHub de la Radeon (#2250) : « 9600 XT », « 30.3 GiB », « 37.6 » surlignés ; puis deux barres de bande passante : 5080 « 960 Go/s », 5060 Ti « 448 Go/s » (T39, T40).]
Et si ta carte est plus abordable ? Sur une Radeon de seize gigas, avec trente gigas de RAM, un autre utilisateur mesure environ trente-sept tokens par seconde, toujours avec ce modèle. Et là, je vais être franc avec toi. J'ai une 5080, une carte haut de gamme, et sa mémoire est deux fois plus rapide que celle d'une 5060 Ti. Donc mes chiffres, c'est plutôt le haut de la fourchette. Sur ta carte de seize gigas, ça tourne aussi, juste moins vite.

[VISUEL : V23, une barre « réponse ≤ 16 384 tokens » où la réflexion mange la place du code ; puis `models.json` de Pi, la ligne `"maxTokens": 32000` en gros (CONF 1:42).]
Par contre, il y a un piège, et c'est la réflexion. Par défaut, ce modèle réfléchit longtemps avant d'écrire, et cette réflexion compte dans la longueur maximale de sa réponse. Et par défaut, Pi lui demande au plus seize mille tokens, c'est aussi ce que Strata écrirait pour lui chez moi. Donc un jeu complet plus la réflexion, ça peut déborder, et là, le fichier s'arrête au milieu.
Du coup, avant le premier test, j'ai monté cette limite à la main dans le fichier de Pi, à trente-deux mille. Je te mets le fichier en description. Et tu vas voir à la fin que ça n'a pas toujours suffi.

[VISUEL : V23d, le tableau de vitesses du projet (C4), la ligne du Coder surlignée, « moteur ancien » ; V23e, le moniteur, puis les deux barres « Pi 1 500 / OpenCode 7 400 ».]
Dernière chose, la vitesse baisse quand la conversation grandit. C'est le projet lui-même qui le publie. Sur une autre machine, avec un ancien moteur, le Coder passe de cinquante-neuf à quarante-trois tokens par seconde entre mille et cent vingt-huit mille tokens de contexte. Donc en gros, plus l'agent lit de code, plus il ralentit. Et c'est pour ça que j'ai pris Pi. Ses instructions font mille cinq cents tokens, contre sept mille quatre cents pour OpenCode. Ça lui fait moins à relire à chaque demande.

---

## 5. Et Claude ? (9:30 – 10:00)

[VISUEL : V24, la pastille du pronostic revient ; Latitude Sud, le site de Claude, qui défile (TT 2:52-3:10), puis à côté de l'essai 1 en anglais (TT 3:48) ; `AGENTS.md` en vignette.]
Là, tu vas me dire : et Claude, dans tout ça ? Je ne lui ai pas redonné mes prompts mot pour mot, donc je ne vais pas te faire un faux match.
Je lui ai juste demandé un site de voyage avec mes photos, en une phrase. Il l'a fait en moins de deux minutes et demie, en français, et ça tient la route.
Mon modèle, lui, avait mis une demi-heure, en anglais, avec une demande bien plus détaillée. Et le plan qui a sauvé le deuxième essai, c'est encore Claude qui l'a écrit.
Donc maintenant, la question qui fâche : où est-ce que ça casse ?

---

## 6. Là où ça casse (10:00 – 11:10)

[VISUEL : V26, le moniteur sans erreur, toutes les requêtes « Done » (MON4). Puis les tickets (C2, C3), la page des versions (C6).]
Chez moi, le moteur n'a jamais planté pendant les tests.
Par contre, chez les autres, c'est une autre histoire. Sur GitHub, il y a un ticket encore ouvert où le moteur plante avec ce Coder sur certaines longues demandes. Plusieurs utilisateurs l'ont eu, sur des cartes de huit et de douze gigas, et le message d'erreur accuse la RAM. Sauf qu'en fait, des utilisateurs ont trouvé la vraie cause : c'est un bug du moteur. Un correctif est proposé, mais il n'est pas encore dans la version que j'ai testée.
Un utilisateur de 5080 rapporte aussi une autre erreur, « non-finite logits », avec d'autres fichiers du même modèle. Et un autre testeur a vu ce Coder rater une tâche de code dans Claude Code, là où d'autres versions du modèle l'ont réussie.
Il faut dire que Strata est jeune. Le projet a été créé le vingt-quatre septembre, et il sort une version tous les deux ou trois jours. Donc note bien ta version. Et si ça casse chez toi, copie le message exact, parce que c'est comme ça que la cause de ce bug a été trouvée.

---

## 7. Le verdict, et ce soir (11:10 – 13:50)

[VISUEL : V27a-V27g, les quatre résultats locaux côte à côte (TT), puis la page de prix de Claude, « Pro · 20 $ / mois » surligné (C8) ; pour R15, les lignes `write _sim.js`, `write harness.js` de `chrono.mjs`.]
Alors, est-ce que ça remplace mon abonnement ? Pas complètement. Par contre, il n'en faut plus qu'un petit. Avec l'abonnement à vingt dollars par mois, Claude écrit le plan, et le modèle local l'exécute chez moi, sur ma carte. C'est exactement ce qui a sauvé le site.
Et même sans plan, il s'en sort bien. L'île et le casse-briques en une seule demande, et le mini-Minecraft au bout de trois relances. Ses vraies fautes à lui, tu les as vues, c'est le site en anglais, et ce fichier qu'il disait avoir écrit. Le reste du temps perdu, ce n'est pas son code, c'est l'outil. Quand il lançait Chrome pour se tester, Pi attendait une réponse qui ne venait jamais. Au total, plus de deux heures à attendre pour rien.
Et il y a une erreur qui est la mienne. Trente-deux mille tokens de réponse, ce n'était pas assez. Une fois, il a été coupé net en plein milieu du site, sept minutes perdues, et derrière, il a dû écrire le fichier par morceaux.
Mais ce qui m'a le plus surpris, c'est que personne ne le lui demande, et pourtant, il écrit ses propres scripts pour tester ses jeux.
*(R15 : proposition du 14/11, tirée des sessions ; change-la si ce n'est pas ce qui t'a surpris.)*
Si cette vidéo t'a évité un mauvais achat, abonne-toi.

[VISUEL : V28, la liste qui s'écrit avec la voix, chaque ligne avec sa vraie capture (INST 5:30, INST 1:24, INST 1:48, CONF 1:24-1:42).]
Et si tu veux le refaire ce soir, voilà la liste.
Un, il te faut une carte de douze à seize gigas, au moins trente-deux gigas de RAM, et environ quatre-vingt-dix gigas de disque libres.
Deux, tu installes l'appli Strata, le lien est en description. Dans sa liste de modèles, elle te dit si chacun tient sur ton PC avant même de le télécharger.
Trois, tu prends le Coder, sans les images, et avant de le lancer, tu fermes tout, navigateur compris.
Quatre, tu branches Pi. L'appli te donne une adresse, tu la mets dans le fichier de Pi avec le nom du modèle, et tu montes la limite de réponse, plus haut que mes trente-deux mille. Et dis-lui de ne pas ouvrir de navigateur pour se tester. S'il reste bloqué plus de trois minutes sur une commande, appuie sur Échap. Le fichier est en description.
Par contre, si tu as plus de RAM, d'après la doc, à quarante-huit gigas, tu passes aux petites tailles du modèle complet, et à soixante-quatre, à toutes.
Et si c'est ta toute première IA en local, commence plutôt par la vidéo sur LM Studio, je te la mets juste là.

[VISUEL : V29, la pastille du pronostic revient en grand, « QUI AVAIT RAISON ? », puis la carte vers la vidéo du jeudi 19/11.]
Alors, et ton pronostic du début ? Dis-moi en commentaire si tu avais raison, avec ta carte et ta RAM.
Et jeudi, on cherche comment aller plus vite avec la même carte. La vidéo arrive juste là. Allez, salut !

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
| Limite de réponse, réflexion comprise : 16 384 par défaut dans Pi (T37), et ⅛ du contexte dans la config de Strata, soit 16 384 à 128K (T13) | 4 | T13, T37 | ✅ (code, doc de Pi) |
| La limite montée à la main dans `models.json` de Pi (`maxTokens`) | 4 | T31, T37 | ✅ (code, doc de Pi) ; fait le 13/11 (`"maxTokens": 32000`) |
| Le Coder passe de 59 à 43 tok/s entre 1K et 128K de contexte (autre machine, moteur ancien) | 4 | T30 | ✅ (DEV, ancien) |
| Ticket ouvert : plantage du Coder sur certaines longues demandes, cartes de 8 et 12 Go, le message accuse la RAM, cause trouvée, correctif proposé pas dans la 0.2.13 | 6 | T23 | ✅ (ticket #5104 relu le 11/11) |
| Un utilisateur de 5080 : « non-finite logits » avec d'autres fichiers | 6 | T11 | ⚠️ non confirmé par le développeur |
| Un testeur a vu le Coder rater une tâche dans Claude Code, d'autres versions l'ont réussie | 6 | T27 | ✅ (description revérifiée le 11/11) |
| Projet créé le 24/09 ; une version tous les 2 à 3 jours | 6 | T1 | ✅ |
| 48 Go : les petites tailles ; 64 Go : toutes | 7 | T5 (MODELS.md) | ✅ (DEV) |
| L'appli dit si un modèle tient avant de le télécharger ; Pi se branche à la main sur l'adresse de la page Serving (`http://127.0.0.1:47831/v1`), vu le 13/11 | 7 | T38, T37 | ✅ (DEV) |
| Les vidéos du 09/11 et du 02/11 ; celle du 19/11 | 1, 7 | `calendrier.md` | ✅ |
| Île : 15 min 32 s, une demande ; site, essai 1 : écrit en 31 min, en anglais, bloqué 1 h 50 sur Chrome ; Sillage : écrit en 17 min, deux blocages sur Chrome ; mini-Minecraft : « written and verified » sans fichier, 3 relances, 35 min, un bug trouvé à la dernière ; casse-briques : 8 min, une demande, un script de test ; plus de 2 h bloqué sur Chrome en tout ; une coupure à 32 000 tokens (≈ 7 min perdues) | 1, 3, 7 | T41 | ✅ (sessions de Pi, `chrono.mjs`, 14/11) |
| Le plan de Claude : 770 lignes, 228 textes en français, un tiers des lignes de Sillage recopiées telles quelles ; le plan a retiré la galerie et le défilement des avis | 3 | T42 | ✅ (fichiers du dossier, 14/11) |
| Claude Pro : 20 $ par mois, Claude Code compris | 7 | T43 | ✅ (claude.com, 14/11) ; « ça suffit pour le plan » : ⚠️ ton avis, pas mesuré |
| L'histoire du dragon : presque pas de réflexion | 4 | T41 | ✅ (161 caractères de réflexion) ; le tok/s : ton enregistrement |
| Monter la limite plus haut que 32 000 ; Échap arrête une commande bloquée | 7 | T44 | ✅ (code et doc de Pi 1.5.2) ; une valeur plus haute pas encore essayée avec Strata |
| Près de 70 tok/s en moyenne pendant les tests, de 43 à 84 ; le dragon à 51 ; « du même ordre » que le repère de 70 | 0, 4 | T45 | ✅ (moniteur, 13 et 14/11) |
| « Tout ça, à partir d'un seul prompt » : chaque test part d'un seul prompt, relances à la main ; 2 sur 4 sans relance (l'île, le casse-briques), le site en 2 essais, le mini-Minecraft en 3 relances, dit en sections 1, 3 et 7 | 0, 1, 3, 7 | T41 | ✅ formulation validée par toi (14/11, soir) |
| Un peu plus d'une demi-heure du clic au premier message ; RAM 30,8 / 31 Go ; lecture disque ≈ 200 Mo/s pendant qu'il écrit, 0 au repos | 2 | T45 | ✅ mesures ; « une partie passe par le SSD » : interprétation |
| Ce que montrent l'île, Sillage, le mini-Minecraft et le casse-briques | 1, 3 | T45 | ✅ (`Tous les tests strata.mp4`) |
| Latitude Sud : une phrase, moins de 2 min 30, en français | 5 | T42 | ✅ (2 min 23 s) |
| Le moteur n'a jamais planté pendant les tests | 6 | T41 | ✅ |
| Il écrit ses propres scripts de test sans qu'on le lui demande | 7 | T45 | ✅ (prompt du casse-briques relu) |

**Non dit exprès** : « Flash-Next tourne sur 32 Go » (c'est le Coder ; le nom « Qwen 3.8 Flash Next » est dit dans le hook, à ta demande du 14/11, et suivi tout de suite de « une moitié de modèle »), « 125 milliards » pour le Coder lui-même, tout classement général local contre Claude, tout chiffre de 64 ou 128 Go de RAM comme étant le tien, toute raison inventée à la lenteur du dragon.

## Mesure (11/11, sur la voix seule, sans `[VISUEL]` ni notes en italique)

Mesurée par script, chaque trou compté pour 1 mot (rempli : 3 à 15 mots). Liste « stricte » des liaisons : donc, du coup, en fait, sauf que, en effet, voilà, bref, par contre, justement, bon, alors. Liste « large » : + mais, parce que, maintenant, attention, et là.

| | Mots de voix | Durée à 145 mots/min | Avec les trous remplis (≈ 6 mots chacun) | Liaisons / 100 mots (stricte / large) |
|---|---|---|---|---|
| V1 (variante A) | 1 354 | 9 min 20 | ≈ 9 min 50 | 1,77 / 2,81 |
| **V2** | **1 296** (15 trous, 17 emplacements) | 8 min 56 | ≈ 9 min 30, plutôt **≈ 10 min** avec tes phrases (R3, R7, R9, R12, R13, R15 sont des phrases) | **1,62 / 2,31** |
| **V2 du 14/11** (4 démos, deux essais du site, ton verdict) | **1 954** (17 emplacements) | 13 min 29 | **≈ 14 min** avec tes phrases | non remesuré |

- **Hook** : 92 mots (≈ 95 remplis), soit ≈ 39 s à 145 mots/min et ≈ 34 s à 165. La question centrale tombe vers 0:25 ; le plan en 4 livrables de 0:25 à 0:34 ; le défi à 0:35, affiché dès 0:22.
- **Nombres dans la première minute** : seize gigas, R1, R2 (« sur les trois »), trente-deux gigas : 4. Les chiffres de Pi (1 500 contre 7 400) sont en section 4 pour cette raison.
