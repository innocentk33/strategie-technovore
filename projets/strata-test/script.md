# Le meilleur modèle possible pour 16 Go de VRAM (Strata, testé) : script (V3, 14/11/2026 au soir : nouvelle structure, résultats d'abord ; la V2 est dans [`script-v2.md`](script-v2.md))

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
17. **V3, 14/11 au soir, tes demandes** : (a) **structure à la Red Stapler** (*I ran Qwen3.8 27B on single 8GB Card*, chapitres : intro, benchmark, config et harnais, tests et dépannage, résultats et comparaison, ce qui n'a pas marché), dans ton ordre : résultats → puissance du modèle → d'où vient cette puissance → vitesse → installation → erreurs → Claude → chez les autres → verdict ; (b) **la vidéo ne tourne plus autour des prompts** : ils passent en cartes texte à l'écran, la voix dit ce qu'on voit, le temps et les relances ; les « Niveau un / deux / trois » disparaissent ; (c) le hook ouvre directement sur ta phrase, les résultats défilent dessous ; (d) **le pronostic est retiré** partout (question, pastille, retour en section 5, fin) ; (e) tes phrases : « J'écris mon prompt en anglais pour qu'il soit beaucoup plus efficace, car c'est recommandé dans la doc » (corrigée le 14/11 au soir, à ta demande, en « car sa doc dit qu'il est moins bon dans les autres langues » : la doc ne recommande pas l'anglais, elle dit le Coder plus faible ailleurs, T5) et « Au niveau de la réflexion, par contre, c'est un peu plus tricky » ; (f) **nouvelle section « puissance »** (T47 : Flash-Next avant-goût de Qwen 4, mieux que le 27B en code d'après Qwen ; T6 : le Coder garde 95 % du score) ; (g) les blocages de Chrome, la limite de 32 000 et R15 passent du verdict à la section « erreurs » ; moins de mises en scène (« Pourquoi ? Parce que », « le moment de vérité », « la question qui fâche », « je vais être franc »). 2 107 mots (V2 : 2 340).

## Ce que la vidéo dit (texte et sous-texte)

- **Texte** : la moitié d'un modèle géant, gardée pour le code, tourne sur ma carte de 16 Go et mes 32 Go de RAM. Voilà ce qu'elle écrit (une île en 3D, un site, un mini-Minecraft, un casse-briques), à quelle vitesse, face à Claude, et où ça casse. Et la meilleure formule : un petit abonnement écrit le plan, le modèle local l'exécute.
- **Sous-texte** : ton PC de joueur peut aller plus loin que les fiches ne le disent, mais pas gratuitement : le verrou, c'est la RAM. **Montré, jamais dit** : la RAM libre qui tombe, le premier chargement, l'échec éventuel.
- **À ne pas recadrer** : ce n'est pas une vidéo contre Claude. Tu l'utilises, tu continues, et la comparaison porte sur trois demandes, sans classement.

## Structure

| Temps (≈) | Partie | Ce qui s'y passe | Relance qui la ferme |
|---|---|---|---|
| 0:00-0:28 | 0. Hook | Les quatre résultats défilent sous la voix ; le modèle, la carte, la vitesse, « un seul prompt » ; « la moitié d'un modèle » ; la question ; le plan en 4 livrables et les 2 h perdues | « D'abord, les résultats » |
| 0:28-2:10 | 1. Les résultats | Pi et le compteur, la règle (prompt en anglais, relances comptées), puis l'île, le casse-briques, le site (plan de Claude), le mini-Minecraft (3 relances) ; les prompts à l'écran, pas lus | « D'où vient ce modèle ? » |
| 2:10-3:10 | 2. La puissance du modèle | L'avant-goût de Qwen 4, mieux que le 27B en code (tests de Qwen) ; le Coder, moitié, 95 % du score (ses auteurs) | « Comment il tient ? » |
| 3:10-4:00 | 3. D'où vient cette puissance | Les experts, 6 milliards actifs sur 125 ; Strata range carte / RAM / SSD | — |
| 4:00-6:00 | 4. La vitesse | Le dragon, les tests, les repères (5070 Ti, Radeon), le haut de la fourchette, le contexte et Pi | — |
| 6:00-7:50 | 5. L'installation chez moi | La règle de la RAM, le téléchargement, tout fermer, la RAM pleine, le disque, Pi branché, la réflexion « un peu plus tricky » et la limite à 32 000 | « Voilà ma première erreur » |
| 7:50-10:20 | 6. Les erreurs | La limite trop basse, le site en deux essais (anglais, Chrome, le plan de Claude et ce qu'il a changé), le fichier vide du mini-Minecraft, les 2 h sur Chrome, R15 | — |
| 10:20-10:50 | 7. Et Claude ? | Le site de Claude en une phrase, face à l'essai 1 | — |
| 10:50-11:50 | 8. Chez les autres | Les tickets, Strata jeune, note ta version | « Alors, ça remplace ? » |
| 11:50-13:40 | 9. Verdict et « ce soir » | Le plan à 20 $, abonne-toi, la liste en 4 points, la suite | — |

Timecodes estimés : compte **≈ 13 min 40 à 14 min 30** de voix (V3, 14/11 au soir : 2 107 mots au script, nombres en lettres ; 13 min 35 à 155 mots/min, 14 min 30 à 145). Le hook fait 84 mots ; la question centrale tombe vers 0:18. À recaler sur la voix montée.

**Boucles ouvertes** : « est-ce que ça remplace Claude ? » (0:18 → section 9) ; « les erreurs qui m'ont fait perdre plus de deux heures » (0:25 → section 6) ; « je t'explique pourquoi un peu plus loin », le plan de Claude (section 1 → section 6) ; « comment il tient ? » (fin de 2 → section 3) ; « jeudi, plus vite avec la même carte » (fin → 19/11). **Plus de pronostic** (retiré le 14/11 au soir, ta demande).

**Conventions** : texte normal = voix. `[VISUEL : …]` = plan (V… = plan du storyboard ; TT, INST, CONF, DRAGON, BRICK, T3, VOY, MON0-4 = les rushes et captures, listés en tête du storyboard ; P… et C… = captures à faire). Plus aucun trou ⟦…⟧ depuis le 14/11. Nombres en lettres pour la lecture. **Interdit à l'écran** : clé d'API, onglets du navigateur, dossiers de travail. **Aucun nom de chaîne ni de créateur** dans la voix.

---

## 0. Hook (0:00 – 0:28)

[VISUEL : V01-V05b, les quatre résultats défilent sous toute la voix, un plan toutes les 1 à 3 s : l'île qui tourne (TT 0:06), le casse-briques (TT 2:36), Sillage (TT 1:12), le mini-Minecraft, un bloc posé (TT 2:00) ; la moyenne du moniteur en gros (MON3, « 67.8 tok/s ») sur « soixante-dix ». Pas de titre ni de logo.]
Ces tests ont été réalisés avec Qwen 3.8 Flash Next, qui tourne sur une carte de seize gigas, à près de soixante-dix tokens par seconde. Et tout ça, à partir d'un seul prompt.

[VISUEL : V06, la fiche Hugging Face, « half of its experts removed » surligné (P03) ; un schéma court, la moitié des experts qui s'éteint, « gardée pour le code » écrit à l'écran ; V06c, « ÇA REMPLACE CLAUDE ? ».]
Par contre, ce n'est que la moitié d'un modèle.
Alors, est-ce que ça remplace Claude ?

[VISUEL : V07, le plan en 4 lignes qui s'écrivent avec la voix, sur fond noir, puis « 2 H PERDUES » en rouge.]
Je vais te montrer ce qu'il a réussi, pourquoi il est aussi fort, à quelle vitesse il tourne et comment l'installer. Et à la fin, les erreurs qui m'ont fait perdre plus de deux heures.

---

## 1. Les résultats (0:28 – 2:10)

[VISUEL : V08, Pi devant le moniteur de Strata (BRICK 0:00, plan générique : l'écran de Pi est encore vide) ; le moniteur seul (CONF 0:12-0:40).]
D'abord, les résultats. À gauche, c'est Pi, l'outil qui laisse l'IA écrire les fichiers toute seule. À droite, c'est le compteur de Strata, le programme qui fait tourner le modèle, en tokens par seconde. Un token, c'est à peu près trois quarts de mot.

[VISUEL : V09, les quatre prompts en anglais en cartes texte qui défilent vite, traduction en sous-titre (rien n'est lu) ; GIF pièce d'arcade.]
J'écris mon prompt en anglais pour qu'il soit beaucoup plus efficace, car sa doc dit qu'il est moins bon dans les autres langues. Et je ne touche jamais au code. S'il bloque, je le relance avec une phrase, et je compte chaque relance, comme une pièce de plus à l'arcade.

[VISUEL : V11, l'île ouverte : la rotation à la souris, le zoom, la nuit et les étoiles (TT 0:00-0:40) ; la carte de verdict « ÎLE · 15 MIN 32 · 0 RELANCE ».]
Le premier, c'est une île en 3D. Elle tourne à la souris, elle zoome, et quand j'appuie sur N, la nuit tombe, avec les étoiles. Il l'a écrite en quinze minutes et demie, sans aucune relance.

[VISUEL : V20f-V20g, la partie de casse-briques : les vies, le game over, les bonus « WIDE » et « 3x » (TT 2:28-2:51) ; la carte de verdict « JEU · 8 MIN · 0 RELANCE ».]
Ensuite, un casse-briques. Il y a les vies, l'écran de game over, des bruitages, et des bonus qui élargissent la raquette ou qui triplent la balle. Celui-là, il l'a fait en huit minutes, lui aussi sans relance.

[VISUEL : V18e-V18f, Sillage ouvert (TT 0:41-1:28) ; la carte de verdict « SITE · 17 MIN · PLAN DE CLAUDE ».]
Après, le site d'une agence de voyage qui n'existe pas, avec mes propres photos. Le Kilimandjaro en grand à l'accueil, les destinations avec leurs prix, et des témoignages de voyageurs. Ça a vraiment l'air d'un site d'agence. Il l'a écrit en dix-sept minutes, mais en suivant un plan écrit par Claude, et je t'explique pourquoi un peu plus loin.

[VISUEL : V20c-V20d, le monde, la balade, les blocs posés (TT 1:29-2:27) ; la carte de verdict « 3D · 35 MIN · 3 RELANCES ».]
Et le plus dur, un mini-Minecraft. Tu marches dans un monde en cubes, avec des arbres et du relief, tu sautes, tu casses des blocs, et tu construis avec de la terre, de la pierre, du sable et du bois. Même les textures en pixels, c'est son code qui les dessine, sans jamais voir ce qu'il dessine. Là, il lui a fallu trois relances et trente-cinq minutes.

---

## 2. La puissance du modèle (2:10 – 3:10)

[VISUEL : V12a, la fiche Hugging Face de Flash-Next, « experimental preview of the architecture that will underpin Qwen4 » surligné (P01, à capturer) ; la miniature de la vidéo Qwen 4 du 12/11 (C9, 2 s) ; le tableau de Qwen, la ligne « SWE-bench Multilingual 81.0 / 73.8 » surlignée (P01b, à capturer).]
Pour comprendre ces résultats, il faut savoir d'où vient ce modèle. Qwen 3.8 Flash Next, c'est l'avant-goût de Qwen 4, sorti en août pour montrer sa nouvelle architecture. Et en code, d'après les tests de Qwen, il fait mieux que Qwen 3.8 27B, le modèle dont je te parlais jeudi dernier dans la vidéo sur Qwen 4. Sur un test de code dans plusieurs langages, il monte à quatre-vingt-un, contre soixante-quatorze pour le 27B.

[VISUEL : V13, la doc de Strata (C4), la phrase « a 32 GB PC with a 12 to 16 GB GPU runs the Coder » surlignée ; la fiche du Coder (P03), « experimental » surligné ; son tableau, « SWE-bench Verified 79.2 / 82.8 » surligné.]
Sauf que chez moi, il ne tourne pas en entier. Avec trente-deux gigas de RAM, je ne peux prendre que le Coder, c'est-à-dire le même modèle coupé de moitié et gardé pour le code. Ses auteurs disent eux-mêmes qu'il est expérimental, et plus faible en dehors du code et de l'anglais. Mais sur leur test de code principal, il garde quand même quatre-vingt-quinze pour cent du score du modèle complet. Ça, c'est leur chiffre. Ce qu'il fait vraiment, tu viens de le voir.

[VISUEL : V11e, la miniature de la vidéo du 09/11 (C5), 2 s.]
Et même coupé de moitié, il reste bien plus gros que ma carte. Lundi dernier, je te disais que seize gigas suffisent, si tu prends le bon fichier. Du coup, comment il tient ?

---

## 3. D'où vient cette puissance (3:10 – 4:00)

[VISUEL : V12, un schéma court sur fond noir (la carte / la RAM / le SSD), entre deux vraies images : la page GitHub de Strata (P02), « MIT » en gros plan.]
En fait, le modèle est découpé en centaines de petits spécialistes, qu'on appelle des experts. Et à chaque mot, il n'en réveille que quelques-uns. Sur cent vingt-cinq milliards de paramètres, il n'y en a que six milliards au travail. C'est ce qui lui permet d'être à la fois très gros et rapide.
Et Strata, c'est le programme qui range tout ça. La carte garde les experts les plus utilisés, la RAM garde le reste, et une grosse table reste sur le SSD. En plus, il est gratuit et open source.

---

## 4. La vitesse (4:00 – 6:00)

[VISUEL : V21, l'histoire du dragon qui s'écrit dans Pi (DRAGON 0:21-0:45), puis la ligne « 590 · 50.8 » du moniteur surlignée (MON3) ; V21b, les moyennes « 69.4 » et « 66.1 tok/s » (MON2, MON4), puis les lignes 42.9 (MON4) et 83.6 (MON3).]
Maintenant, la vitesse. Pour la mesurer sans les outils au milieu, je lui ai demandé une petite histoire, celle d'un dragon qui adore les jeux vidéo. Presque pas de réflexion, une réponse courte, et le moniteur affiche cinquante et un tokens par seconde.
Pendant les vrais tests, avec tout le code, c'est même plus rapide, bizarrement. Près de soixante-dix en moyenne, et selon le test, ça va de quarante-trois à quatre-vingt-quatre.

[VISUEL : V22, le ticket GitHub du repère (C1) : « RTX 5070 Ti », « Ryzen 7 9700X », « 70.4 », « thinking off », « Speed only: no correctness check » surlignés.]
Pour te donner un repère, un utilisateur d'une 5070 Ti, avec le même processeur que moi et à peu près la même RAM, mesure environ soixante-dix tokens par seconde avec ce modèle. Lui, il a coupé la réflexion, et il ne vérifie pas si le code marche. Chez moi, c'est du même ordre, mais avec la réflexion allumée, et du code qui doit marcher.

[VISUEL : V22e-V22f, le ticket GitHub de la Radeon (#2250) : « 9600 XT », « 30.3 GiB », « 37.6 » surlignés ; puis deux barres de bande passante : 5080 « 960 Go/s », 5060 Ti « 448 Go/s » (T39, T40).]
Et si ta carte est plus abordable ? Sur une Radeon de seize gigas, avec trente gigas de RAM, un autre utilisateur mesure environ trente-sept tokens par seconde, toujours avec ce modèle. Moi, j'ai une 5080, une carte haut de gamme, et sa mémoire est deux fois plus rapide que celle d'une 5060 Ti. Donc mes chiffres, c'est plutôt le haut de la fourchette. Sur ta carte de seize gigas, ça tourne aussi, juste moins vite.

[VISUEL : V23d, le tableau de vitesses du projet (C4), la ligne du Coder surlignée, « moteur ancien » ; V23e, le moniteur, puis les deux barres « Pi 1 500 / OpenCode 7 400 ».]
Et la vitesse baisse quand la conversation grandit. C'est le projet lui-même qui le publie. Sur une autre machine, avec un ancien moteur, le Coder passe de cinquante-neuf à quarante-trois tokens par seconde entre mille et cent vingt-huit mille tokens de contexte. Donc en gros, plus l'agent lit de code, plus il ralentit. C'est pour ça que j'ai pris Pi : ses instructions font mille cinq cents tokens, contre sept mille quatre cents pour OpenCode. Ça lui fait moins à relire à chaque fois.

---

## 5. L'installation chez moi (6:00 – 7:50)

[VISUEL : V15, le téléchargement, « 58.4 GB to download », l'horloge à 19:30 (INST 1:42-2:24) ; « Hello, I'm Strata » et le premier message à 20:06 (INST 3:00-3:06).]
Pour l'installer, Strata a une règle simple : ta RAM doit contenir les experts, plus une dizaine de gigas pour Windows. C'est pour ça qu'avec trente-deux gigas, sa doc ne me propose que le Coder. Ensuite, il y a une soixantaine de gigas à télécharger. Chez moi, entre le clic sur Télécharger et mon premier message, il s'est passé un peu plus d'une demi-heure.

[VISUEL : V15b, la RAM au moniteur, « 30.8 / 31 GB » en rouge (MON3) ; la case « Disk read » au repos (MON2, 0.1) puis pendant l'histoire du dragon (DRAGON 0:33-0:39, 165 à 183 Mo/s).]
Avant de le lancer, il faut tout fermer, navigateur compris, parce que pendant qu'il écrit, ma RAM est pleine, trente virgule huit gigas sur trente et un. Et regarde cette case du moniteur, c'est la lecture sur le disque. Au repos, elle est à zéro. Dès qu'il écrit, elle monte autour de deux cents mégas par seconde. La RAM est pleine, donc une partie passe par le SSD.

[VISUEL : V23, l'adresse de la page Serving, puis `models.json` de Pi ; une barre « réponse ≤ 16 384 tokens » où la réflexion mange la place du code ; la ligne `"maxTokens": 32000` en gros (CONF 1:24-1:42).]
Ensuite, je branche Pi. L'appli de Strata me donne une adresse, et je la mets dans le fichier de Pi, avec le nom du modèle.
Au niveau de la réflexion, par contre, c'est un peu plus tricky. Ce modèle réfléchit longtemps avant d'écrire, et cette réflexion compte dans la longueur maximale de sa réponse. Par défaut, Pi lui laisse seize mille tokens, et c'est aussi ce que Strata écrirait pour lui chez moi. Un jeu complet plus la réflexion, ça peut déborder, et le fichier s'arrête au milieu. Donc avant le premier test, j'ai monté cette limite à la main, à trente-deux mille. Le fichier est en description.

---

## 6. Les erreurs (7:50 – 10:20)

[VISUEL : V27c, la session coupée en plein site, la réponse qui s'arrête net, « 7 MIN PERDUES » ; puis les écritures par morceaux.]
Et justement, voilà ma première erreur. Trente-deux mille tokens, ce n'était pas assez. Une fois, il a été coupé net en plein milieu du site, sept minutes perdues, et derrière, il a dû écrire le fichier par morceaux. Donc si tu le refais, monte encore plus haut.

[VISUEL : V17a-V17d, le prompt « Sanaka Voyages » en carte texte et les 12 photos ; l'essai 1 en anglais qui défile (TT 3:11-3:57) ; puis l'horloge qui saute de 21:46 à 23:37.]
Le site, lui, ne s'est pas fait du premier coup. Au premier essai, je lui demande un écran d'accueil qui zoome doucement, six destinations, des avis qui défilent tout seuls, une galerie en plein écran, et le tout doit tenir sur un téléphone. Il écrit tout en une demi-heure, mais en anglais, alors que je lui demandais du français. Et à la fin, il veut se tester tout seul. Il ouvre un Chrome invisible, et Chrome ne lui rend jamais la main. Il est resté bloqué presque deux heures, jusqu'à ce que je l'arrête.

[VISUEL : V18a-V18d, le plan de Claude (`AGENTS.md`, puis `i18n.js` et ses textes en français, à capturer) ; la carte « LE PLAN DE CLAUDE : 770 lignes · 228 textes en français · un tiers de la page déjà dedans » ; Pi qui suit le plan (VOY 0:00-0:09, puis 0:57-1:06).]
Pour le deuxième essai, j'ai donné mes photos à Claude, et je lui ai demandé un plan pour ce modèle-là, avec les étapes, des morceaux de code, et tous les textes en français déjà écrits. Le modèle local n'avait plus qu'à le suivre, étape par étape. Ça a donné le site que tu as vu, en dix-sept minutes, avec zéro erreur au contrôle, même s'il s'est encore bloqué deux fois sur Chrome.
Il faut quand même savoir qu'un tiers des lignes de la page étaient déjà dans le plan. Et le plan a changé la commande : plus de galerie en plein écran, et les avis ne défilent plus. À la place, il y a un diaporama dans l'accueil, et une fiche qui s'ouvre pour chaque destination.

[VISUEL : V20a-V20b, la réponse « index.html written and verified » en carte texte, puis « 0 fichier » ; les trois relances et le bug `pos.concat` en cartes texte.]
Pour le mini-Minecraft, l'erreur vient de lui. Au premier essai, il me répond « fichier écrit et vérifié ». Sauf que le dossier est vide, il n'a rien écrit du tout. Il a fallu trois relances, et à la dernière, il a même trouvé un vrai bug dans son propre code.

[VISUEL : V27d, le total « + DE 2 H À ATTENDRE » sur les sessions bloquées ; pour R15, les lignes `write _sim.js`, `write harness.js` de `chrono.mjs`.]
Au total, entre tous les blocages sur Chrome, j'ai passé plus de deux heures à attendre pour rien. Et ce n'est pas son code, c'est l'outil : Pi attendait une réponse que Chrome ne donnait jamais. Donc dis-lui de ne pas ouvrir de navigateur pour se tester, et s'il reste bloqué plus de trois minutes sur une commande, appuie sur Échap.
Mais ce qui m'a le plus surpris, c'est que personne ne le lui demande, et pourtant, il écrit ses propres scripts pour tester ses jeux.
*(R15 : proposition du 14/11, tirée des sessions ; change-la si ce n'est pas ce qui t'a surpris.)*

---

## 7. Et Claude ? (10:20 – 10:50)

[VISUEL : V24, le logo de Claude ; Latitude Sud, le site de Claude, qui défile (TT 2:52-3:10), puis à côté de l'essai 1 en anglais (TT 3:48).]
Et Claude, dans tout ça ? Je ne lui ai pas redonné mes prompts mot pour mot, donc je ne vais pas te faire un faux match. Je lui ai juste demandé un site de voyage avec mes photos, en une phrase. Il l'a fait en moins de deux minutes et demie, en français, et ça tient la route. Mon modèle, lui, avait mis une demi-heure, en anglais, avec une demande bien plus détaillée.

---

## 8. Chez les autres (10:50 – 11:50)

[VISUEL : V26, le moniteur sans erreur, toutes les requêtes « Done » (MON4). Puis les tickets (C2, C3), la page des versions (C6).]
Chez moi, le moteur n'a jamais planté pendant les tests. Chez les autres, ce n'est pas toujours le cas. Sur GitHub, un ticket encore ouvert décrit le moteur qui plante avec ce Coder sur certaines longues demandes. Plusieurs utilisateurs l'ont eu, sur des cartes de huit et de douze gigas, et le message d'erreur accuse la RAM. Sauf qu'en fait, des utilisateurs ont trouvé la vraie cause : c'est un bug du moteur. Un correctif est proposé, mais il n'est pas encore dans la version que j'ai testée.
Un utilisateur de 5080 rapporte aussi une autre erreur, « non-finite logits », avec d'autres fichiers du même modèle. Et un autre testeur a vu ce Coder rater une tâche de code dans Claude Code, là où d'autres versions du modèle l'ont réussie.
Il faut dire que Strata est jeune. Le projet a été créé le vingt-quatre septembre, et il sort une version tous les deux ou trois jours. Donc note bien ta version. Et si ça casse chez toi, copie le message exact, parce que c'est comme ça que la cause de ce bug a été trouvée.

---

## 9. Le verdict, et ce soir (11:50 – 13:40)

[VISUEL : V27a-V27b, les quatre résultats locaux côte à côte (TT), puis la page de prix de Claude, « Pro · 20 $ / mois » surligné (C8).]
Alors, est-ce que ça remplace mon abonnement ? Pas complètement. Mais il n'en faut plus qu'un petit. Avec l'abonnement à vingt dollars par mois, Claude écrit le plan, et le modèle local l'exécute chez moi, sur ma carte. C'est exactement ce qui a sauvé le site. Et même sans plan, il s'en sort bien : l'île et le casse-briques sans relance, et le mini-Minecraft au bout de trois.
Si cette vidéo t'a évité un mauvais achat, abonne-toi.

[VISUEL : V28, la liste qui s'écrit avec la voix, chaque ligne avec sa vraie capture (INST 5:30, INST 1:24, INST 1:48, CONF 1:24-1:42).]
Et si tu veux le refaire ce soir, voilà la liste.
Un, il te faut une carte de douze à seize gigas, au moins trente-deux gigas de RAM, et environ quatre-vingt-dix gigas de disque libres.
Deux, tu installes l'appli Strata, le lien est en description. Dans sa liste de modèles, elle te dit si chacun tient sur ton PC avant même de le télécharger.
Trois, tu prends le Coder, sans les images, et avant de le lancer, tu fermes tout, navigateur compris.
Quatre, tu branches Pi avec l'adresse que te donne l'appli, et tu montes la limite de réponse, plus haut que mes trente-deux mille. Le fichier est en description.
Si tu as plus de RAM, d'après la doc, à quarante-huit gigas, tu passes aux petites tailles du modèle complet, et à soixante-quatre, à toutes.
Et si c'est ta toute première IA en local, commence plutôt par la vidéo sur LM Studio, je te la mets juste là.

[VISUEL : V29, la carte vers la vidéo du jeudi 19/11.]
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
| Flash-Next, « experimental preview of the architecture that will underpin Qwen4 », publié le 24/08 ; en code, d'après Qwen, mieux que le 27B (SWE-bench Multilingual 81,0 contre 73,8) | 2 | T47 | ✅ (fiche Qwen, lue le 12/11) |
| Le Coder garde 95 % du score de code (SWE-bench Verified 79,2 contre 82,8) ; plus faible hors du code et de l'anglais | 2 | T6, T5 | ✅ (DEV, attribué) |
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
