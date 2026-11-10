# Abonnement ou IA locale ? #1 : 16 Go suffisent : script V1

**Sortie** : lun. 9 nov. 2026, 18 h. Vidéo **calculée** : aucun essai, que des mesures publiées (faits `Sx` de [`sources.md`](sources.md), vérifiés le 05/11/2026). Durée visée 10-12 min.

## Titres (3 propositions)

1. **16 Go de VRAM suffisent (mais pas la RAM)** : verdict + tension, recommandé
2. **Abonnement ou IA locale ? 16 Go suffisent, à une condition**
3. **Ma carte de 16 Go fait tourner un vrai Qwen : le piège, c'est la RAM**

**Miniature** : explainer façon OpenCode, la carte graphique en gros plan, couleurs vives, fond très contrasté, « 16 Go » en gros. L'ouverture de la vidéo montre cette scène.

**Conventions** : texte normal = voix off ; `[VISUEL]`, `[SON]` = montage ; `(Sx)` = fait de `sources.md`, ne se lit pas. Timecodes à ~145 mots/min, à recaler sur la voix.

---

## 0. Hook (0:00 - 0:30)

[VISUEL : plan fixe sur ta RTX 5080, gros plan, fond noir, « 16 Go » en vert menthe sur la carte. Pas de logo, pas de visage, aucun titre. 0:08 : le chiffre « 101 tok/s » s'écrit à côté, avec « mesuré par un utilisateur de 5080 » en petit (S18).]
[SON : un seul coup de basse, puis le souffle des ventilateurs.]

Cette carte a seize gigas. Et sur une carte comme elle, un utilisateur a mesuré cent un tokens par seconde avec un vrai Qwen de vingt-sept milliards de paramètres. Donc oui : seize gigas suffisent.

[VISUEL : le « 16 Go » reste, une cassure rouge apparaît sur une barre « RAM 32 Go ».]

Sauf que le vrai verrou, c'est pas la carte, c'est la RAM. Et c'est pas Claude.

[VISUEL : retour sur toi ou sur le schéma carte + RAM. Petit tampon « calculé, pas testé » en bas à droite.]

Alors, jusqu'où ces seize gigas te mènent vraiment, et à partir de quand ton abonnement redevient la bonne réponse ? Je n'ai rien testé moi-même : j'ai rassemblé les mesures de ceux qui l'ont fait, et il y en a une qui change tout.

---

## 1. Le 27B tient en entier dans la carte (0:30 - 3:00)

[VISUEL : jauge VRAM de 16 Go ; un bloc « Qwen3.8-27B » s'y glisse et la remplit presque.]

Commençons par le plus simple. Qwen3.8-27B, vingt-sept milliards de paramètres. En quantization trois bits, son fichier fait onze virgule huit gigas chez ISTA (S33). Il rentre donc en entier dans ta carte, avec un peu de marge.

[VISUEL : capture du README sudoingX/qwen38-mtp, la ligne « RTX 5080 16GB », 53,4 → 101,3 surlignés. Légende : « une seule mesure, Q3_K_M, llama.cpp, 05/11/2026 » (S18).]

Et en vrai, ça va vite. Sur une RTX 5080, une contributrice ou un contributeur du dépôt sudoingX mesure cinquante-trois tokens par seconde. Avec la prédiction multi-tokens, le MTP, ça monte à cent un. Cent un ! C'est plus vite que ce que tu lis. Par contre, attention : c'est une seule mesure.

[VISUEL : trois petites cartes qui s'empilent : Kai 5060 Ti « 45 tok/s » (S20), laptop RTX 3080 « 20-30 tok/s » (S22), 5060 Ti « 26 → 59 » (S19).]

Du coup, je regarde ailleurs. Le YouTubeur Kai trouve quarante-cinq tokens par seconde sur une 5060 Ti. Sur un portable avec une 3080 de seize gigas, un autre mesure vingt à trente. Ce ne sont pas les mêmes cartes ni les mêmes fichiers, mais ça raconte la même chose : un 27B en trois bits, sur seize gigas, ça tourne bien. Et ça, c'est la première bonne nouvelle.

[VISUEL : barre « Q4_K_M : 17 Go » qui déborde de la jauge, rouge, puis « 13 tok/s » (S21).]

Mais attention au piège. Le Q4, celui qu'on te propose souvent par défaut, fait dix-sept gigas. Il ne rentre pas. Et quand ça déborde, la vitesse s'effondre : Hardware IA mesure treize tokens par seconde sur une 5080, avec le Q4. Alors oui, ce n'est pas exactement le même réglage que les cent un, donc je ne te fais pas une soustraction. Mais l'idée est là : un fichier de trop, et ta carte de mille cinq cents euros rame comme une vieille tour.

[VISUEL : un fichier de 11,8 Go à gauche, 17 Go à droite, avec un panneau « tient / ne tient pas ».]

Du coup, la règle pour le 27B, c'est : prends le fichier qui rentre, pas celui qui est « meilleur sur le papier ».

[VISUEL : la ligne « 64 Ko par token » ; « 128 000 tokens = 8 Go » grossit (S20).]

Et il reste un détail. Chaque mot que le modèle garde en mémoire coûte de la place : soixante-quatre kilo-octets par token, d'après Kai. Pour cent vingt-huit mille tokens, ça fait huit gigas de plus. Donc ton vrai plafond, c'est le contexte, pas la taille du modèle. Kai passe de quarante-sept mille à cent dix mille tokens avec deux réglages : la vision coupée et un cache en huit bits.

[VISUEL : schéma RAM 32 Go en gris, barré d'un « presque inutile ici ».]

Et ta RAM là-dedans ? En fait, pour ce modèle, presque rien : tout vit dans la carte. Retiens cette phrase, parce qu'elle va s'inverser tout de suite.

---

## 2. Le modèle de 125 milliards, et le vrai verrou (3:00 - 6:30)

[VISUEL : l'icône Strata, puis « 125 milliards de paramètres, dont 6 travaillent à chaque mot » (S4).]

Car il y a un autre Qwen, bien plus gros : Qwen3.8 Flash-Next. Cent vingt-cinq milliards de paramètres, mais seulement six qui travaillent à chaque mot. Un projet récent, Strata, le fait tourner sur un PC de joueur. Comment ? Il garde les experts les plus utilisés dans la carte, le reste dans la RAM, et la grosse table sur le SSD (S2).

[VISUEL : schéma en trois étages : GPU 16 Go / RAM / SSD. Les experts descendent en cascade.]

Sauf que, du coup, tout bascule. Le verrou n'est plus ta carte, c'est ta RAM. La doc de Strata donne la règle : la RAM doit couvrir les experts, plus environ dix gigas pour Windows et le reste (S2).

[VISUEL : tableau qui s'écrit ligne par ligne : Q2_0 = 34 + 10 = 44 Go ; IQ3_S = 50 + 10 = 60 Go. Barres rouges au-dessus de « 32 Go ».]

Fais le calcul avec moi. Le plus petit fichier du modèle complet, c'est trente-quatre gigas d'experts, plus dix : quarante-quatre. Le plus qualitatif, cinquante plus dix : soixante. Et toi, tu as trente-deux gigas de RAM. Donc le modèle complet, c'est non. Et une plus grosse carte n'y change rien : la doc le dit noir sur blanc.

[VISUEL : ligne « Avec 32 Go, prends le Coder » encadrée, source MODELS.md (S3).]

Par contre, la doc dit autre chose : avec trente-deux gigas, prends le Coder. C'est une version réduite, entraînée pour le code, qui garde deux cent cinquante-six experts sur cinq cent douze (S6). Vingt-trois gigas d'experts, donc vingt-trois plus dix : trente-trois.

[VISUEL : jauge RAM : 33,5 Go visibles sous Windows, le bloc « Coder 23 Go » + « Windows 10 Go » la remplit à ras. « calcul, pas une mesure » (S8).]

Et là, en vrai, c'est serré. Trente-deux gigas de DDR5, Windows t'en laisse voir environ trente-trois virgule cinq. Moins vingt-trois, il reste dix et demi pour tout le reste. C'est pile la marge demandée, à un giga près. Donc ça passe, mais à ras, navigateur fermé. Et c'est un calcul, pas un test.

[VISUEL : la capture du ticket #4997, « Ryzen 7 9700X, 5070 Ti 16 Gio, 31,2 Gio de RAM », puis 70,4 tok/s. En petit : « Speed only: no correctness check was run » (S9).]

Heureusement, quelqu'un l'a mesuré. Sur GitHub, un gars avec presque ma config : le même Ryzen 7 9700X, une RTX 5070 Ti de seize gigas, trente et un gigas de RAM. Avec le Coder, il mesure soixante-dix tokens par seconde en chat court. Et presque soixante-dix-neuf dans une session d'agent. Soixante-dix !

[VISUEL : zoom sur la ligne « Speed only: no correctness check was run ».]

Sauf que lui-même l'écrit en tête du ticket : vitesse seulement, aucun test de justesse. Donc ça tourne vite, mais il ne dit pas si c'est bon. Et c'est une 5070 Ti, pas une 5080. La mienne devrait faire au moins aussi bien, mais ce n'est pas mesuré.

[VISUEL : deux tickets #5115 et #5237, avec « 64 Go » et « 96 Go » entourés en rouge (S11, S12).]

Attention, ne te fais pas piéger par les chiffres de 5080 sous Strata : cent quatorze tokens par seconde ici, cent six là. Leurs auteurs ont soixante-quatre, voire quatre-vingt-seize gigas de RAM. Pas trente-deux. Ce n'est pas ta situation, donc je ne les mélange pas avec la tienne.

---

## 3. Le prix à payer (6:30 - 9:00)

[VISUEL : panneau « Prix du Coder », trois lignes qui se remplissent.]

Alors, quel est le coût de ce « ça passe » ? D'abord, la qualité. Le Coder compresse le modèle à un virgule quatre-vingt-neuf bit par paramètre. Ses auteurs annoncent quatre-vingt-quinze pour cent du score de code du modèle complet (S6, S7). Sauf que ce sont leurs chiffres, sur du code en anglais.

[VISUEL : trois citations qui défilent : HN « noticable loss » (S17) ; Samayas « The Coder variant failed » (S35) ; « le français est hors du domaine optimisé » (S6).]

Du coup, je regarde les autres. Sur Hacker News, un commentateur écrit que le Coder est moins bon et qu'il a une perte notable. Dans le test de Samayas avec Claude Code, le Coder a échoué à finir la tâche, sur une RTX 5090. Ce n'est pas un test universel, il le dit lui-même, mais ça compte. Et pour toi, une chose en plus : le français est hors du domaine optimisé du Coder. Donc pour écrire ou répondre en français, ce n'est pas lui qu'il te faut.

[VISUEL : la liste « 1 536 Mio de VRAM réservés », « souris figée quelques minutes au premier lancement » (S15).]

Ensuite, le confort. Au premier lancement, Strata charge trente-cinq à cinquante-cinq gigas dans ta RAM, et la souris peut se figer plusieurs minutes. Un projet de six semaines, avec plus de mille trois cents tickets ouverts. Entre deux versions, un utilisateur de 5080 perd vingt-cinq pour cent de vitesse (S11). Donc c'est impressionnant, mais ce n'est pas encore stable.

[VISUEL : retour aux deux fichiers : « 27B, 11,8 Go, tout dans la carte » / « Coder, 33 Go, RAM à ras ».]

Ce qui nous donne, honnêtement, deux réponses à « seize gigas suffisent ». Pour le 27B, oui, sans réserve, parce qu'il tient dans la carte. Pour le gros modèle, oui, mais en version réduite, avec trente-deux gigas de RAM à ras. Et le gros modèle complet, il lui faut quarante-huit à soixante-quatre gigas de RAM.

---

## 4. Et Claude, dans tout ça ? (9:00 - 10:45)

[VISUEL : tableau Qwen3.8-27B contre Opus 4.6 : Terminal Bench 2.1 73,0 / 78,2 ; SWE-bench Pro 61,7 / 53,4 ; source « fiche de Qwen, 05/08/2026 » (S29).]

Reste la grosse question : est-ce que ça remplace ton abonnement ? D'après les tableaux de Qwen, le 27B bat l'ancien Opus 4.6 en code sur SWE-bench Pro : soixante et un virgule sept contre cinquante-trois virgule quatre. Mais c'est le modèle complet, avec leurs réglages, pas le fichier de douze gigas dans ta carte.

[VISUEL : le benchmark indépendant : « Terminal-Bench 4.0 : 6 % vs 46 % » en gros, Artificial Analysis, indice v5.0.1 (S31).]

Alors je regarde une mesure indépendante. Artificial Analysis compare le même 27B à Claude Opus 5. En agent de terminal : six pour cent contre quarante-six. Six contre quarante-six ! Donc pour coder en agent, sur les gros projets, Claude reste très loin devant.

[VISUEL : deux colonnes « Local » / « Abonnement » avec trois lignes chacune.]

Du coup, voilà comment je le lis. Ton modèle de seize gigas, c'est un très bon plan B : tes données restent chez toi, ça marche sans internet, ça ne coûte rien de plus. Mais ce n'est pas Claude. Et le coût caché, c'est la RAM : la mienne m'a coûté quatre-vingt-treize euros en 2025, et la même est à cinq cent soixante euros aujourd'hui.

---

## 5. Verdict et suite (10:45 - 11:30)

[VISUEL : récap en trois lignes sur fond sombre : « Le 27B : tient en 16 Go. Le Coder : 32 Go de RAM, à ras. Le gros : 48-64 Go. »]

Donc, résumons. Seize gigas suffisent pour un vrai Qwen de vingt-sept milliards. Le verrou, c'est la RAM, pas la carte. Et même quand ça tourne, ça ne vaut pas encore ton abonnement pour le code sérieux.

[VISUEL : carte YouTube vers la vidéo d'installation (2 nov.).]

Si tu n'as jamais installé d'IA chez toi, j'ai une vidéo qui le fait pas à pas : je te la mets là.

[VISUEL : carte YouTube vers « comment lire le nom d'un modèle » (16 nov.), ajoutée à la sortie. Écran de fin, vidéo suivante de la playlist.]

Et si tu te demandes ce que veulent dire tous ces noms, Q3, IQ3_S, A3B… la semaine prochaine, je t'apprends à lire le nom d'un modèle. Dis-moi en commentaire ta carte et ta RAM, et je te dirai ce qui tient chez toi.

---

## Faits utilisés

| Dit dans le script | Faits |
|---|---|
| 27B en 3 bits, 11,8 Go ; 53 → 101 tok/s sur 5080 (une seule mesure) | S18, S33 |
| 5060 Ti 45, laptop 3080 20-30, 5060 Ti 26 → 59 | S20, S22, S19 |
| Q4 17 Go ne tient pas ; 13 tok/s (réglages différents) | S19, S20, S21 |
| 64 Ko/token, 128K = 8 Go ; 47 000 → 110 000 | S20 |
| 125 B dont 6 actifs ; GPU/RAM/SSD ; experts + 10 Go | S2, S4 |
| Q2_0 44 Go, IQ3_S 60 Go ; « avec 32 Go, le Coder » | S3, S5, S8 |
| Coder 256/512 experts, 23 Go ; 33,5 Go visibles (calcul) | S6, S8 |
| Mesure 5070 Ti / 9700X / 31,2 Gio : 70,4 et 78,7 tok/s, sans test de justesse | S9 |
| 5080 à 114 / 106 tok/s avec 64-96 Go de RAM | S11, S12 |
| 95 % annoncé ; HN, Samayas ; français hors domaine | S6, S7, S17, S35 |
| Souris figée, 25 % de baisse, 1 300 tickets | S15, S11, S1 |
| Qwen vs Opus 4.6 ; 6 % vs 46 % | S29, S31 |
| RAM 92,95 € → 560 € | fiche.md (relevé 24/10, à revérifier avant la voix) |

**Interdits respectés** : aucun « j'ai testé », aucun tok/s à toi, le Coder n'est jamais « équivalent » au complet ni à Claude, la 5070 Ti n'est pas une 5080.
