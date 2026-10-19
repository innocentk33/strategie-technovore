# Storyboard : ArtCraft

> **Voix off montée** : [`voix-off-montee.wav`](voix-off-montee.wav). Durée **12 min 14 s**, 48 kHz, normalisée à −16 LUFS, crête à −1,5 dBFS. Elle est tirée de `artcraft.m4a` (21 min 25 s de prises).
> **Rush du test** : `Test photocraft.mp4` (1 min 37, 2560×1440, 60 i/s, sans son). Son index est en bas de page.
> Script d'origine : [`script.md`](script.md). Fiche : [`fiche.md`](fiche.md).
>
> Les timecodes (TC) de ce document sont ceux de `voix-off-montee.wav`, à poser à 0:00 sur la timeline. En Remotion, à 60 i/s : image = TC en secondes × 60.

## Fiche d'identité

| Axe | Position |
|---|---|
| Cible | Curieux de tech de 18 à 30 ans, entre débutant et intermédiaire |
| But | Surtout théorique (le récit), avec une vraie part pratique (le test) |
| Ambiance | Divertissant d'abord : ton humour, les vannes et les mèmes portent le récit |
| Complexité | Simple : un seul test, des chiffres simples |
| Outil | Remotion (motion design), avec le rush du test importé en vidéo. Déduit de ton cap v3 |

Le style visé est un montage « fancy » mais lisible. Ce sont les captures réelles qui prouvent, et les animations servent les chiffres. Ne mets pas d'effet partout : réserve-les aux temps forts listés plus bas.

## Comment la voix off a été montée

- **Les prises** : 21 min 25 de rushes donnent 12 min 14 de voix, en 98 morceaux.
- **La règle de choix** : je garde la dernière prise complète, sauf quand une prise plus ancienne est plus juste. Une vingtaine de faux départs et de bruits sont supprimés, par exemple « Le lendemain ? », « Il dit, je cite, le logiciel c'est fini. Mais… » ×2, « Avec une règle. » ×2 ou « Ça se compte… ».
- **Les blancs** : à l'intérieur d'une phrase, tout silence de plus de 0,6 s est ramené à 0,4 s. Les respirations sont gardées.
- **Les pauses posées** (🟫 dans les tableaux) :
  - 0,1 à 0,3 s entre deux phrases d'une même idée ;
  - 0,5 à 0,6 s quand on change d'idée ;
  - 1 s en fin de partie, pour la transition et la musique ;
  - 1,2 à 1,5 s sur les cinq temps forts : « Ambiance » (1:00.7), les pronostics (5:16.6), Claude aux commandes (7:47.3), « …avec des abonnements » (8:26.9) et la compatibilité (11:36.5).
- **Les meilleures parties d'une prise** :
  - Hook : « le buzz **vide** de l'année » vient de la 2e prise. La 1re disait « le buzz de l'année », ce qui inverse le sens.
  - Gag de l'agent : j'ai coupé le doublon « c'est-à-dire je peux décrire le style ».
  - Rust : j'ai coupé le faux départ « Rust est un langage pour… ».
  - L'usine : j'ai coupé le doublon « avec Opus… ».
  - Le chiffre de 45 % : j'ai gardé la prise « Mais prêt pour un vrai travail de pro ? Environ 45 % ». L'autre disait « 45 % des fonctionnalités qui sont faites », ce qui est inexact : 45 %, c'est la part prête pour un travail de pro.
  - Fin : j'ai pris la 4e prise de « Pour vous, tout dépend… », la seule complète.

### Erreurs factuelles dans l'enregistrement

| Passage enregistré | Problème | Ce que j'ai fait |
|---|---|---|
| « Adobe, qu'on sait qui est sorti dans les années 1900 » | Photoshop 1.0 date de 1990 | **Coupé**. Le bilan s'arrête sur « c'est bluffant », ce qui évite aussi un 2e « bluffant » |
| « Plus de la moitié des modifications de PhotoCraft sont **corrigées** par Claude » | Les commits sont **cosignés** par Claude, donc écrits par lui, pas corrigés | **Coupé**. Pour la récupérer, enregistre : « Plus de la moitié des modifications de PhotoCraft sont cosignées par Claude. » Je la replace à 6:23 |
| « Quand j'ai regardé le live de Basti UI, on ne peut pas breveter ou attaquer en justice une interface graphique » | Faux en l'état. Une interface peut être protégée : dessins et modèles, brevets de design aux États-Unis, droit d'auteur en Europe si elle est originale. Seule la hiérarchie de menus a été jugée non protégeable aux États-Unis (Lotus c. Borland, 1995) | **Coupé**. Ta phrase suivante (« à mon avis… à peu près protégés ») garde ton opinion |
| « Je vous donne rendez-vous **la semaine prochaine** » | La prochaine longue vidéo (Uber) sort le 9/11, soit deux semaines après | **Coupé** proprement : « je vous donne rendez-vous pour une grosse vidéo qui arrive sur la chaîne » |
| « Une petite équipe **de plus de 300 contributeurs** » | L'équipe est petite. Les 300+ sont des contributeurs open source | **Gardé**, car la coupe aurait été audible. **Corrigé à l'écran** (#45) |
| « Pas de distraction, on contrôle les vibrations » | Hors sujet, entre « pas de piège » et les 13 applis | **Retiré**. Dis-moi si c'était voulu |
| « Zone grise **judiciaire** » (citation de Brandon) | Brandon parle de *legal grey area* | Gardé à l'oral. **La citation affichée à l'écran dit « juridique »** |

**Pas enregistrés** (le storyboard compense) :
- « Ambiance. » est remplacé par un texte sur fond noir (#9) ;
- le teaser Uber est remplacé par une carte d'écran de fin (#58) ;
- la RAM mesurée et l'aparté OMG Ubuntu sont abandonnés, la vidéo n'en a pas besoin.

## Rythme et rétention

| Repère | TC | Part de la vidéo |
|---|---|---|
| Fin du hook | 0:29 | 4 % |
| Appel à l'abonnement | 2:40 | 22 % |
| Début du test | 2:55 | 24 % |
| **Révélation du PSD** | 5:18 | 43 % |
| Relance (« qui paie ? ») | 7:48 | 64 % |
| **Twist de l'abonnement** | 8:19 | 68 % |
| Fin de la voix | 12:14 | 100 % |

Le passage le plus fragile est **9:03 à 10:07** : le juridique, une minute sans image forte. Il faut donc un changement de plan au moins toutes les 4 à 5 s : citation, FakeYou, article, question centrale, écran partagé, puis la parodie.

## Musique par partie

| Partie | TC | Ambiance | Coupe |
|---|---|---|---|
| Hook | 0:00 – 0:29 | Pulsation tendue, basse | Coupe sèche dans la pause de 1 s |
| Intro | 0:30 – 1:41 | Tech curieuse, lo-fi | **Silence pendant « Ambiance »** (1:00.7 – 1:02.0) |
| La vengeance | 1:41 – 2:40 | Ironique, ambiance de casse | Baisse sous l'appel à l'abonnement |
| Le test | 2:55 – 6:07 | Enjouée, rythmée : coupes sur le temps fort | **Coupée à 5:16.6** (riser), retour en force sur « parfaitement » |
| L'usine | 6:07 – 7:48 | Électronique, mécanique | Coupe à 7:47 |
| Relance + qui paie | 7:48 – 9:03 | Enquête, mystère | **Silence total à 8:26.9** pendant 1,2 s |
| Le juridique | 9:03 – 10:07 | Même morceau, plus bas et plus posé | Coupe à 10:07 |
| La promesse | 10:08 – 11:37 | Réflexive (piano, ambient) | Remonte légèrement sur le verdict |
| Outro + écran de fin | 11:38 – ~12:30 | Chaleureuse, enjouée | **Ajouter environ 15 s de musique après la voix** pour l'écran de fin (YouTube accepte 5 à 20 s) |

## Légende

🟦 VID vidéo, B-roll · 🟩 IMG image · 🟪 ECR capture d'écran · 🟧 ANI animation · ⬜ TXT texte sur fond noir · 🩷 MEM mème, blague visuelle · 🟫 pause voulue · 🟥 élément manquant · 🟨 à vérifier à l'oreille

« Test 0:24 » renvoie au timecode du rush `Test photocraft.mp4`.

---

## HOOK (0:00 – 0:29)

| # | TC | Voix off (telle que dite) | Visuel | Texte · Son |
|---|---|---|---|---|
| 1 | 0:00.0 | « Ce mec en avait tellement marre de payer des frais de résiliation chez Adobe… qu'il a complètement recréé. » | 🟩 sa photo de profil GitHub (publique) 🟥 → 🟧 facture qui défile, ligne « frais de résiliation » surlignée en rouge | Aucun intro ni logo. **Tampon** sur « recréé » |
| 2 | 0:06.8 | « Photoshop, Premiere Pro, Lightroom : sept logiciels gratuits, sortis en même pas trois jours, et c'est une IA qui a écrit le code. » | 🟧 **ANI-01** : les 7 icônes des clones en rafale, compteur « 3 jours » | Petit whoosh par icône, volume bas |
| 3 | 0:14.6 | « Moi, j'ai essayé de faire la miniature de cette vidéo avec son Photoshop. Si ça marche, franchement, adieu l'abonnement Adobe. » | 🟪 Test 0:39 – 0:45 accéléré ×3 (le logo Claude posé sur la miniature). Ne montre pas le résultat final : garde la surprise pour 5:18 | — |
| 4 | 0:22.2 | « Sinon, ça sera le buzz vide de l'année. » | 🩷 une bulle qui éclate | Son « pop » |
| 5 | 0:25.2 | « Et dans cette histoire, le Robin des Bois a lui aussi un abonnement à nous vendre. » | 🟩 Robin des Bois (gravure du domaine public), tampon « ABONNEMENT » | Impact sur « abonnement ». 🟫 1 s, la musique coupe |

## INTRO (0:30 – 1:41)

| # | TC | Voix off | Visuel | Texte · Son |
|---|---|---|---|---|
| 6 | 0:30.3 | « On vit quand même une époque de dingue. Depuis l'arrivée de Claude Opus 5.5, des gens sortent des trucs de plus en plus fous. » | 🟦 enchaînement rapide de démos IA, puis 🟪 l'annonce d'Opus 5.5 | La musique entre |
| 7 | 0:38.4 | « Le 30 septembre, un développeur d'Atlanta, Brandon Thomas, ouvre un nouveau projet sur GitHub : PhotoCraft. Le lendemain soir, il poste ça sur Hacker News, le forum préféré des développeurs. » | 🟪 le dépôt GitHub (date de création), puis la page Hacker News | ⬜ texte intégré « 30 septembre 2026 » |
| 8 | 0:49.2 | « Il dit, je cite : "Le logiciel, c'est fini. Mais pour de vrai. Je viens de faire Photoshop d'un seul coup, et en entier." Et il ajoute à cela : "Notre métier ne vaudra bientôt plus rien." » | 🟪 le post HN, citation surlignée au fil de la voix (zoom lissé) | Sous-titre FR de la citation anglaise |
| 9 | 1:00.7 | 🟫 *(1,3 s sans voix)* | ⬜ **« Ambiance. »** sur fond noir | Musique coupée, **criquets** |
| 10 | 1:02.0 | « Franchement, moi, je suis un développeur, et ma première pensée a été pour les petits SaaS : ces services en ligne qui font une seule chose à la fois, comme générer un QR code par exemple, ou je sais pas… peut-être iLovePDF. » | 🟪 un générateur de QR code, puis iLovePDF | — |
| 11 | 1:17.9 | « Si une IA recrée Photoshop en trois jours, est-ce que tout ça va disparaître ? Adobe compris. On y revient à la fin. » | 🟪 zoom arrière du QR code vers l'interface de Photoshop (**plan repris en #55**) | ⬜ petit texte « On y revient à la fin » |
| 12 | 1:25.7 | « En moins de trois semaines, son projet a récolté près de 67 000 étoiles sur GitHub. Les étoiles, c'est les likes des développeurs. » | 🟧 **ANI-02** : compteur jusqu'à 67 000, puis 🩷 ⭐ = 👍 | Ticks du compteur, impact sur le chiffre final |
| 13 | 1:33.3 | « Alors, est-ce qu'on peut vraiment s'en servir, ou est-ce que c'est une coquille vide ? Pour répondre à ça, il faut remonter à une facture. » | 🟩 une coquille vide, puis la facture qui tombe à l'écran | Whoosh et bruit de papier. 🟫 1 s |

## BLOC 1 : La vengeance (1:41 – 2:40)

| # | TC | Voix off | Visuel | Texte · Son |
|---|---|---|---|---|
| 14 | 1:41.5 | « Si vous avez déjà un abonnement Adobe, vous connaissez peut-être le piège. Vous prenez l'offre annuelle, payée tous les mois : ça a l'air souple. Sauf que si vous partez pendant la première année, Adobe facture des frais de résiliation : la moitié de ce qu'il vous reste à payer. » | 🟧 **ANI-03** : frise de 12 mois, résiliation au mois 4, les 8 mois restants coupés en deux | ⬜ « 50 % du reste » en pop. Son de caisse enregistreuse |
| 15 | 1:58.1 | « En 2024, la justice américaine attaque Adobe pour ces pratiques. En mars 2026, Adobe accepte de payer 150 millions de dollars, sans reconnaître de faute. » | 🟪 deux titres de presse, sans logo Adobe | ⬜ « 150 M$ ». Impact |
| 16 | 2:10.1 | « Brandon Thomas fait partie de ceux qui ont payé. Il l'a écrit sur Reddit, je cite : "Ils m'ont fait payer des frais de résiliation à plusieurs reprises, et je les déteste depuis." » | 🟪 son commentaire Reddit, « à plusieurs reprises » surligné | — |
| 17 | 2:20.9 | « À plusieurs reprises, il a dit. Alors il a décidé de farmer de l'aura sur le dos d'Adobe, en construisant toute la boîte. » | 🩷 compteur « +1000 aura » | Son de jeu vidéo (level up) |
| 18 | 2:28.6 | « On a tous voulu se venger d'Adobe. Moi, je paie 33 euros juste pour créer des miniatures. Lui, il a cloné carrément Photoshop. » | 🟪 ta page d'abonnement Adobe, infos perso floutées 🟥 → 🟪 écran d'accueil de PhotoCraft (Test 0:02) | 🟫 1 s |

## APPEL À L'ABONNEMENT (2:40 – 2:55)

| # | TC | Voix off | Visuel | Texte · Son |
|---|---|---|---|---|
| 19 | 2:40.1 | « Mais bon, petite pause : sur Technovore, on décortique le génie caché derrière certaines applications que vous utilisez tous les jours. Si c'est un truc qui vous intéresse, alors abonnez-vous, c'est gratuit. Et contrairement à Adobe… vous pouvez partir quand vous voulez. » | 🟧 bouton S'abonner animé | ⬜ « Résiliable à tout moment 😉 » sur la chute. Clic |

## BLOC 2 : Le test (2:55 – 6:07)

| # | TC | Voix off | Visuel | Texte · Son |
|---|---|---|---|---|
| 20 | 2:55.0 | « Sur Reddit, où ses posts s'enflamment, il promet : "On atteindra 100 % de parité d'ici un mois." Traduction : tout Photoshop dans un mois. » | 🟪 le post Reddit | ⬜ jauge « 100 % · 1 mois » |
| 21 | 3:04.8 | « Franchement, sept logiciels en trois jours, tout Photoshop promis en un mois : sur le papier, c'est intéressant. Mais le papier, ça ne fait pas des miniatures, et ça ne fait pas tout. Alors j'ai fait un test. » | ⬜ « 7 logiciels · 3 jours · 100 % en 1 mois » qui s'empilent, puis 🟦 Test 0:00 (ton bureau) | **Riser** qui finit sur « un test ». La musique repart |
| 22 | 3:19.1 | « Un seul, un tout petit test. Le défi pour moi, c'était de faire la miniature de cette vidéo avec PhotoCraft. En gros, mon vrai travail, celui que je fais pour chaque vidéo. » | 🟪 la grille de tes anciennes miniatures | — |
| 23 | 3:30.8 | « Mais je pourrais faire aussi mieux : vu que ce logiciel a été fait pour les IA, je peux décrire le style de ce que je veux, donner des références, et laisser mon IA faire le tout tout seul. Mais bon, là, faut pas abuser. » | 🟪 un faux prompt tapé dans Claude, « Fais ma miniature », puis arrêt sur image sur « Mais bon » | 🩷 **disque qui raye**. 🟫 0,9 s |
| 24 | 3:44.9 | « Déjà, au niveau de l'installation, il y a une version pour Windows, Mac et Linux. Linux, frère ! Franchement, quel logiciel a une compatibilité pour Linux ? C'est super rare. Même Adobe n'y est pas. » | 🟪 la page Releases GitHub avec ses 3 installeurs 🟥, puis 🩷 Tux | — |
| 25 | 3:56.9 | « Normal pour eux : ce qui intéresse Adobe, c'est l'argent. Et quand tu regardes Linux, pour dix personnes seulement qui sont sous Linux, le marché n'est pas du tout rentable pour eux. Mais imaginez si vous avez un Steam Deck que vous utilisez comme PC principal, vu qu'il tourne sous Linux : avec PhotoCraft, vous pouvez utiliser littéralement votre console de jeu comme un vrai PC de bureau. » | 🩷 « 10 personnes » (une salle vide), puis 🟩 Steam Deck branché à un écran (image presse Valve) 🟥 | — |
| 26 | 4:21.7 | « En plus de ça, le fichier fait moins de 100 mégas, et le logiciel démarre franchement en deux secondes. » | 🟪 **Test 0:00 – 0:03 en temps réel** (bureau, puis PhotoCraft ouvert) | ⬜ chrono « 2 s » et « installeur : 66 à 92 Mo ». Tic-tac |
| 27 | 4:28.0 | « La force d'Adobe aussi, c'est son interface. Les gens y sont habitués, et changer ses habitudes, c'est terriblement difficile. Sauf que là, le mec débarque avec quasiment la même interface, les mêmes raccourcis, et il ouvre des fichiers PSD en plus. Des fichiers Photoshop. Des fichiers Photoshop ! Mais en fait, que demande le peuple de plus ? » | 🟪 Test 0:03 – 0:07 (menu Fichier) en **écran partagé avec le même menu dans Photoshop** 🟥, puis Test 0:12 – 0:15 (ouverture de `miniature-1920x1080.psd`) | ⬜ « .PSD ✔ » en pop sur la répétition |
| 28 | 4:47.7 | « Franchement, pour ma miniature, je n'utilise pas d'effets artistiques compliqués : des calques, un détourage, du texte, et pour moi tout y est, en fait. » | 🟪 trois coupes calées sur les mots : **calques** = Test 0:15 – 0:16 (panneau Calques) ; **détourage** = Test 0:24 – 0:33 ; **texte** = Test 0:15 (propriétés : Montserrat 104 pt) | Un clic par mot |
| 29 | 4:58.0 | « Maintenant, le vrai juge de paix : si j'ouvre un ancien fichier Photoshop d'une miniature de la chaîne, un fichier PSD… le projet le reconnaît lui-même : sur les fichiers créés par Photoshop, il n'en affiche correctement qu'environ la moitié. » | 🟪 la page d'évaluation de compatibilité du projet 🟥 | ⬜ « ≈ 1 PSD sur 2 » |
| 30 | 5:13.3 | « Alors, le mien ? Qu'en pensez-vous ? Franchement, faites vos pronostics. » | ⬜ « ✅ ou ❌ ? » et une horloge | 🟫 **1,5 s** : musique coupée, **riser** qui finit pile à 5:18.1 |
| 31 | 5:18.1 | « Pour moi, il a ouvert parfaitement mon fichier PSD. J'ai même pu faire quelques modifications : j'ai ajouté le logo de Claude pour faire la miniature de cette vidéo. Et honnêtement, même au lancement du logiciel, c'était super rapide. » | 🟪 **Test 0:08 – 0:16** (le PSD ouvert, avec ses calques et effets intacts), puis Test 0:36 – 1:06 accéléré ×4 (copier, coller, placer le logo), puis 1:15 – 1:24 (export), puis 1:30 (le PNG final dans la visionneuse) | **Impact** sur « parfaitement », ⬜ « ✅ ». La musique repart en force. **Technique du jour : voir en bas** |
| 32 | 5:36.2 | « En fait, comme tout est écrit en Rust, Rust qui est un langage réputé pour être ultra rapide et ne pas consommer beaucoup de choses, PhotoCraft est super super rapide, et démarre en un quart de tour. » | 🟩 Ferris, la mascotte de Rust, puis 🟪 Test 0:00 – 0:03 en boucle courte | 🟨 écoute la collure « en Rust, Rust qui est » (deux prises raccordées) |
| 33 | 5:51.3 | « Et franchement, pour mes miniatures, ça fait largement le job. Et pour un logiciel qui est sorti il y a moins de trois semaines, c'est bluffant. » | 🟩 **la miniature finale en plein écran**, tampon « Faite avec PhotoCraft » | 🟨 « c'est bluffant » est dit bas : remonte-le de 2 à 3 dB si besoin |
| 34 | 5:59.4 | « Mais comment est-ce qu'un seul développeur sort sept logiciels de cette taille en trois jours ? » | ⬜ la question au centre | Whoosh de transition. 🟫 1 s |

## BLOC 3 : L'usine (6:07 – 7:48)

| # | TC | Voix off | Visuel | Texte · Son |
|---|---|---|---|---|
| 35 | 6:07.9 | « En réalité, Brandon, il a quinze ans de métier, dont une dizaine sur Rust. Mais en février, il a fait le choix radical. Je cite : "J'ai complètement arrêté d'écrire du code en février." Depuis, c'est l'IA qui écrit : Claude Code tel quel, avec Opus 5.5. » | 🟩 carte-citation, puis 🟪 un terminal Claude Code | Machine à écrire sur la citation |
| 36 | 6:23.5 | « Et sur les sept applis, ça fait presque 2,9 millions de lignes de code. Lui, il joue au chef de chantier : il découpe le travail, lance des agents en parallèle, relit, redresse la barre, avec une règle répétée dans chaque projet : on ne regarde jamais le code d'Adobe. » | 🟧 **ANI-02** jusqu'à 2,9 M, puis 🟧 schéma (Brandon au centre, agents en parallèle), puis 🟪 la règle dans le dépôt 🟥 | ⬜ « Règle n° 1 » |
| 37 | 6:41.7 | « On appelle ça une réimplémentation en salle blanche. En gros, imaginez un chef qui goûte un plat au restaurant, puis qui le refait chez lui. Il a le droit de goûter le plat ; il n'a pas le droit de voler le cahier de recettes. Ici, le cahier de recettes, c'est le code d'Adobe. » | 🟧 un chef, une assiette, un cahier barré (formes simples) | — |
| 38 | 6:58.4 | « Le projet interdit même la décompilation, et s'appuie sur la documentation publique, comme celle des formats PSD et PDF. Le PDF, d'ailleurs, il faut qu'on en parle : c'est Adobe qui l'a inventé, et avec Acrobat, il l'a presque privatisé. Pourtant, c'est une norme ouverte depuis 2008 : même votre navigateur sait lire un PDF. ArtCraft en a profité pour sortir son PdfCraft. » | 🟪 la spécification PSD publique, un PDF ouvert dans le navigateur, puis PdfCraft | ⬜ « ISO 32000 · 2008 » |
| 39 | 7:26.7 | « Autre détail : chaque action de ces logiciels est une commande. Du coup, une IA peut les piloter. Vous dites à votre Claude, ou à votre GPT, "détoure ce personnage", et c'est lui qui clique dans PhotoCraft. Je l'ai essayé personnellement pour monter ma miniature, et il a réussi à faire tout ce que je lui ai demandé. » | 🟪 **ta conversation avec Claude qui pilote PhotoCraft** 🟥, en écran partagé avec Test 0:17 – 0:33 (le détourage du logo) | 🟫 1,2 s, puis la musique coupe |

## RELANCE (7:48 – 7:59)

| # | TC | Voix off | Visuel | Texte · Son |
|---|---|---|---|---|
| 40 | 7:48.5 | « Sauf que des agents IA qui codent jour et nuit, ça coûte quand même cher. Alors j'ai cherché qui paie tout ça, en réalité. Et je suis tombé sur la page des tarifs. » | 🩷 un compteur de jetons qui s'emballe, puis 🟪 la page des tarifs | **Nouveau morceau** (enquête) sur « page des tarifs » |

## BLOC 4 : Qui paie ? (7:59 – 10:08)

| # | TC | Voix off | Visuel | Texte · Son |
|---|---|---|---|---|
| 41 | 7:59.5 | « Les applications sont gratuites pour de vrai, et sans compte à créer. Mais elles sont publiées par une entreprise qui s'appelle… ArtCraft. Et ArtCraft, à la base, c'est un studio de création d'images et de vidéos générées par IA. Payant. Avec des crédits, et des formules entre 8 et 60 $ par mois. » | 🟪 le site PhotoCraft (« gratuit »), puis les mentions légales, puis 🟪 le site du studio ArtCraft, puis sa grille tarifaire 🟥 | Impact sur « ArtCraft » |
| 42 | 8:19.2 | « Eh bien oui : l'homme qui a cloné Adobe par haine des abonnements finance ses logiciels gratuits… avec des abonnements. » | ⬜ **texte central** qui pop sur « avec des abonnements » | 🟫 **1,2 s de silence total**, sans musique : laisse la chute respirer |
| 43 | 8:28.1 | « Bon, pour être juste : son abonnement à lui est résiliable à tout moment. Pas de frais de sortie, pas de piège. » | 🟪 la mention « résiliable à tout moment » sur la page des tarifs | La musique revient doucement |
| 44 | 8:34.9 | « Et ArtCraft ne s'arrête pas à Adobe : treize applications, avec des clones de Word, d'Excel, de PowerPoint, et même de Figma. Franchement, comme Thanos avec les pierres d'infinité : il les veut toutes. » | 🟧 la grille des 13 applis (icônes des clones, pas des originaux), puis 🩷 le gant de Thanos avec les icônes en guise de pierres | Claquement de doigts |
| 45 | 8:48.6 | « Derrière ça, on a un cofondateur et une petite équipe, de plus de 300 contributeurs. On est loin de la légende du mec seul dans sa chambre, qui est en train de développer, ou en train de combattre Adobe à lui seul, genre un David contre Goliath. » | 🟪 la page Contributors du dépôt 🟥, puis 🟩 David et Goliath | ⬜ **deux étiquettes séparées** : « 1 cofondateur + petite équipe » et « 300+ contributeurs sur GitHub » (elles corrigent le raccourci de la voix) |
| 46 | 9:03.2 | « En 2020, Brandon disait déjà : "Je ne suis pas avocat, mais je pense qu'on entre dans une zone grise judiciaire." C'était à propos de Vocodes, son site qui faisait parler des voix de célébrités avec l'IA, devenu aujourd'hui FakeYou. En 2022, le gendarme italien de la vie privée a ouvert une enquête sur FakeYou. Aujourd'hui, la même question revient avec Photoshop : cloner un logiciel avec une IA, est-ce que c'est légal ? » | 🟪 la citation de 2020, puis le site FakeYou, puis 🟩 l'article sur l'enquête italienne, puis ⬜ **la question au centre** | Citation affichée : « zone grise **juridique** ». La musique baisse |
| 47 | 9:33.2 | « Côté code, la salle blanche le protège. Mais les menus, les raccourcis sont volontairement les mêmes, et c'est justement ce qui fait sa force. Au moment où j'enregistre, Adobe n'a fait aucune déclaration publique, aucune plainte connue. » | 🟧 écran partagé : à gauche le code 🔒, à droite les menus identiques | ⬜ « Aucune plainte connue (au [date]) » 🟨 à revérifier la veille de la sortie |
| 48 | 9:46.9 | « Moi non plus, je suis pas avocat. Mais à mon avis, ces copies restent open source et gratuites, sans rien à revendre dedans. Et ça, ça les protège à peu près de toutes les attaques juridiques. » | ⬜ fond sobre | Sous-titre « Avis perso, pas un conseil juridique » |
| 49 | 9:57.9 | « D'ailleurs, si vous avez vu passer une vidéo "Adobe réagit", méfiez-vous : c'est une parodie, jouée par un acteur. Reste à savoir si la promesse de Brandon tient. » | 🟪 la miniature de la parodie, tampon « PARODIE » 🟥 | 🟫 1 s, puis transition |

## BLOC 5 : La promesse (10:08 – 11:37)

| # | TC | Voix off | Visuel | Texte · Son |
|---|---|---|---|---|
| 50 | 10:08.1 | « 100 % de Photoshop en un mois. Deux jours plus tard, sur Hacker News, la promesse avait déjà rétréci : "Ça se comptera en mois, pas en années." » | ⬜ la jauge de #20 qui **rétrécit**, puis 🟪 le commentaire HN | Son qui se dégonfle |
| 51 | 10:17.4 | « Et le projet publie sa propre évaluation, plutôt honnête d'ailleurs : environ 76 % des fonctions de Photoshop existent dans PhotoCraft. Mais prêt pour un vrai travail de pro ? Environ 45 %. Et pour aller au bout du Photoshop, ils estiment qu'il faut encore entre 2 300 et 4 100 heures de travail d'agents IA. » | 🟧 **ANI-04** : barres 76 %, puis 45 %, puis compteur d'heures | Impact léger sur « 45 % » |
| 52 | 10:38.6 | « La première moitié de ces applications, l'IA l'a écrite en quelques jours. La seconde, ce sont des détails : un fichier qui s'ouvre exactement pareil, une couleur qui ne bouge pas à l'impression, un pinceau qui réagit comme votre main l'attend. » | 🟦 trois plans de détail (fichier, impression couleur, coup de pinceau), tirés d'une banque d'images | 🟨 écoute le départ « La première moitié » (faux départ coupé juste avant) |
| 53 | 10:51.8 | « Alors, coquille vide ou pas ? Franchement, non. Pour un usage comme le mien, ça suffit largement. Ou pour quelqu'un qui utilisait par exemple Photopea en ligne, ça suffit. Mais pour un professionnel, il manque encore des fonctions : sur Reddit et Hacker News, des utilisateurs les listent une par une. » | 🟩 ta miniature, puis 🟪 Photopea, puis 🟪 les fils Reddit et HN qui défilent | Rappel de la coquille de #13 |
| 54 | 11:09.2 | « Mais plus de 300 contributeurs en trois semaines, ça montre que le projet intéresse vraiment. » | 🟧 la courbe des contributeurs (ANI-02 en version courbe) | 🟫 1 s |
| 55 | 11:15.5 | « Bon, et mon métier, alors ? Je reviens à mes petits SaaS. Un service qui fait une seule chose, comme générer un code QR, je pense qu'il va disparaître : une IA peut recréer cela trop facilement. Mais une grosse boîte comme Adobe ne vend pas que le produit : elle vend aussi du support, et la compatibilité avec des années de projets. » | 🟪 **le plan du QR code de #11**, qui se dissout, puis 🟧 un bouclier « support + compatibilité » | ⬜ rappel « ≈ 1 PSD sur 2 mal affiché ». Sans lui, l'argument contredit ton test réussi. 🟫 1,2 s |

## OUTRO (11:38 – fin)

| # | TC | Voix off | Visuel | Texte · Son |
|---|---|---|---|---|
| 56 | 11:37.7 | « En tout cas, moi, je vais continuer d'utiliser pour mes miniatures. Un logiciel de moins de 100 mégas qui démarre en deux secondes… franchement, c'est pas cher payé. Juste pour gérer des minias, ça va : c'est le must have pour moi. » | 🟪 Test 0:00 – 0:03, puis la miniature finale | Musique d'outro |
| 57 | 11:51.4 | « Pour vous, tout dépend de ce qu'il vous faut. Alors dites-moi en commentaire : il vous manquerait quoi pour lâcher Adobe ? Ou "j'utilise déjà GIMP" ? À vous de voir, on ne juge personne ici. Et si vous voulez la suite, abonnez-vous. » | ⬜ la question au centre (à **épingler en commentaire**), puis le bouton S'abonner | — |
| 58 | 12:04.6 | « Si vous aimez comprendre comment les applications marchent sous le capot, je vous donne rendez-vous pour une grosse vidéo qui arrive sur la chaîne. Allez, salut, c'était Inno. » | **Écran de fin** : carte « Prochaine vidéo : Uber, 9 novembre », bouton S'abonner. **Environ 15 s de musique après la voix** | 🟨 collure « rendez-vous / pour » (« la semaine prochaine » est coupé) |

---

## Index du rush `Test photocraft.mp4`

Le rush fait 2560×1440 : en 1080p, tu peux zoomer jusqu'à 133 % sans perte. Il contient déjà des zooms automatiques ; ne zoome pas par-dessus sur les mêmes plans.

| TC du rush | Contenu | Utilisé en |
|---|---|---|
| 0:00 – 0:02 | Bureau, puis PhotoCraft ouvert en environ 2 s | #21, #26, #32, #56 |
| 0:02 – 0:03 | Écran d'accueil de PhotoCraft | #18 |
| 0:03 – 0:07 | Fichier > Ouvrir un fichier récent ; `logo_claude.png` | #27 |
| 0:08 – 0:14 | La miniature PSD ; menu des fichiers récents | #27, #31 |
| 0:15 – 0:16 | PSD ouvert : calques (Titre avec effets et ombre, ArtCraft A, liseré, extrusion, lueur), Montserrat Extra-gras 104 pt | #28, #31 |
| 0:17 – 0:23 | Le logo Claude, avec les actions rapides « Supprimer l'arrière-plan » et « Sélectionner le sujet » | #39 |
| 0:24 – 0:33 | Outil Sélection d'objet, détourage, fond transparent | #28, #39 |
| 0:36 – 0:39 | Copier, puis coller dans la miniature | #31 |
| 0:39 – 1:06 | Placement et redimensionnement du logo | #3, #31 |
| 1:09 – 1:14 | Calque > Convertir en objet dynamique | (facultatif) |
| 1:15 – 1:24 | Fichier > Exporter, enregistrement, alerte d'écrasement | #31 |
| 1:30 | Le PNG exporté dans la visionneuse Windows | #31 |
| 1:33 – 1:37 | Résultat final | #33 |

## Éléments à collecter 🟥

1. La photo de profil GitHub de Brandon (#1).
2. Ta page d'abonnement Adobe à 33 €, floutée (#18).
3. La page Releases du dépôt : les 3 installeurs et leurs tailles (#24, #26).
4. Le même menu Fichier dans Photoshop, pour l'écran partagé (#27).
5. La page d'évaluation de compatibilité PSD du projet (#29).
6. La règle « on ne regarde jamais le code d'Adobe » dans le dépôt (#36).
7. **La conversation avec Claude qui pilote PhotoCraft (#39)**. Le rush montre l'application, pas l'IA. Si tu n'as pas filmé la conversation, refais une commande courte (2 min) : la phrase « il a réussi à faire tout ce que je lui ai demandé » mérite sa preuve.
8. Les pages ArtCraft : le studio, les tarifs, la mention « résiliable » (#41 – #43).
9. Les captures Reddit et HN citées (#8, #16, #20, #50, #53).
10. La page Contributors du dépôt (#45).
11. Une image presse du Steam Deck (#25).
12. La miniature de la parodie « Adobe Reacts » (#49).
13. Photopea (#53).

**Attention, miniature** : celle du test montre un « A » rouge barré. La fiche prévoyait « pas de logo Adobe ». Si c'est bien leur logo, remplace-le par un carré rouge générique, ce qui suffit à l'idée.

## Fiches d'animation (Remotion, 60 i/s)

**ANI-01 · Les 7 clones (#2, 0:06.8)**
- **Éléments** : les 7 icônes des clones, une ligne de 7 sur fond sombre, et un compteur « 0 → 3 jours » sous la ligne.
- **Déroulé** :
  - t = 0 : écran vide ;
  - une icône toutes les 0,25 s, en pop 70 → 110 → 100 % (7 puis 5 images) ;
  - t = 1,9 s : le compteur défile jusqu'à « 3 jours », puis légère lueur.
- **Easing** : sortie lissée (`Easing.out(Easing.quad)`).
- **Point d'attention** : le centre de l'écran, là où tombe le compteur.
- **Son** : whoosh très court par icône (volume 0,2), impact sur « 3 jours ».

**ANI-02 · Compteur réutilisable (#12, #36, #54)**
- **Principe** : un seul composant `<Compteur de={0} a={67000} duree={1.5} />`, réutilisé pour 67 000 étoiles, 2,9 M de lignes, puis la courbe des contributeurs.
- **Déroulé** :
  - de 0 à 1,5 s, le chiffre monte avec `Easing.out(Easing.cubic)` (rapide puis lent) ;
  - à la fin, pop à 110 % puis 100 %.
- **Placement** : sur le tiers gauche à chaque fois, pour que le regard retrouve les chiffres au même endroit.
- **Son** : des ticks qui ralentissent avec le compteur, puis un impact.

**ANI-03 · La facture (#14, 1:41.5)**
- **Éléments** : une frise de 12 cases (les mois), une case « résiliation » au mois 4, puis les 8 mois restants coupés en deux.
- **Déroulé** :
  - les cases se remplissent au fil de « payée tous les mois » ;
  - sur « Sauf que », la case du mois 4 devient rouge ;
  - sur « la moitié de ce qu'il vous reste », les 8 cases restantes se scindent et la moitié se colore, avec le texte « 50 % du reste ».
- **Son** : une caisse enregistreuse sur « frais de résiliation ».

**ANI-04 · 76 % / 45 % (#51, 10:17.4)**
- **Éléments** : deux barres horizontales, « Fonctions présentes » et « Prêt pour un travail de pro ».
- **Déroulé** :
  - la barre 1 monte à 76 % sur « 76 % » ;
  - la barre 2 monte à 45 % sur « Environ 45 % » ;
  - puis le compteur « 2 300 – 4 100 h » apparaît.
- **Remarque** : garde les couleurs de la jauge de #20, pour que la promesse de « 100 % » et la réalité se lisent avec le même code.

## Une chose nouvelle à essayer : garder le point d'attention

La technique à essayer cette fois, c'est **la révélation du PSD (#31, 5:18)**.
- **Le principe** : à la sortie du silence de 1,5 s, le PSD ouvert apparaît, puis on zoome doucement vers le panneau Calques.
- **La règle** : le plan suivant (le placement du logo) garde le sujet **au même endroit de l'écran**, sur le tiers droit. Le regard du spectateur n'a alors jamais à chercher.
- **En Remotion** : un même `transformOrigin` (par exemple `"66% 40%"`) sur les deux plans, et un zoom `interpolate(frame, [0, 45], [1, 1.25], { easing: Easing.inOut(Easing.cubic) })`.

**À vérifier à l'oreille** (🟨) : ces collures ont été validées par retranscription, pas par écoute. Ce sont #32, #33, #52 et #58.
