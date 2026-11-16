# Transcription : Nathan Inline, « Mon IA locale va 11 fois plus vite (même PC) »

> https://www.youtube.com/watch?v=VFC16Tb3lwU · 7 min 27 s · publiée le 14/11/2026 · 7 392 vues au 15/11 (4,43 K abonnés). Sous-titres automatiques français (yt-dlp, 15/11), nettoyés des répétitions : les mots peuvent être mal reconnus.

[00:00:00] Et bien salut à tous, c'est Nathan
[00:00:01] Innight. J'espère que vous allez bien.
[00:00:03] Dans cette vidéo, je vais vous montrer
[00:00:04] comment j'ai fait pour réussir à faire
[00:00:06] tourner un modèle de plus de 177
[00:00:08] milliards de paramètres à plus de 80
[00:00:10] tokens par seconde sur ma petite carte
[00:00:12] graphique de 16 Go. Ce modèle, c'est
[00:00:15] Qwen 3.8 Flash Next. Au début, il me
[00:00:17] répondait à 7 tokens par seconde. Et
[00:00:20] aujourd'hui, il me répond à plus de 80
[00:00:23] tokens par seconde. Mais entre 7 tokens
[00:00:25] et 80 tokens, il y a eu 3 mois de
[00:00:27] galère, d'erreurs et de bonnes
[00:00:29] surprises. Ma machine, [grognement]
[00:00:30] c'est un serveur tout à fait normal, une
[00:00:32] RTX 5060 Ti de 16 Go. C'est elle qui va
[00:00:35] faire presque tout le travail. Une
[00:00:36] deuxième carte graphique, une RTX 3070
[00:00:39] de 8 Go que je pensais au début être
[00:00:41] très utile, mais vous allez voir que
[00:00:43] c'est pas forcément le cas. J'ai
[00:00:44] également un Ryzen 9 3900X et 46 Go de
[00:00:47] RAM DDR4. Retenez bien ce dernier
[00:00:50] chiffre parce que c'est lui qui va tout
[00:00:51] décider. Très vite, je tombe sur un gros
[00:00:54] problème. C'est un modèle MoE, des
[00:00:56] milliers de petits experts, 512 experts
[00:00:59] par couche sur plus de 48 couches. Pour
[00:01:02] chaque token, seuls 10 d'entre
[00:01:04] travaillent, mais on ne sait jamais
[00:01:05] lesquels à l'avance. Et tous ensemble,
[00:01:07] ils pèsent entre 40 et 55 Go. Ils ne
[00:01:10] rentrent pas du tout dans ma carte
[00:01:11] graphique et tout juste dans la VRAM.
[00:01:13] Tout le défi, c'est de mettre les bons
[00:01:15] experts au bon endroit. Fin août,
[00:01:17] [grognement] je me lance avec llama.cpp,
[00:01:19] le moteur que tout le monde utilise, et
[00:01:22] j'ai les premiers résultats. 7,9 tokens
[00:01:24] par seconde. C'est vraiment super lent.
[00:01:26] Du coup, je bricole, je mets quelques
[00:01:27] couches sur la deuxième carte, et là,
[00:01:29] j'atteins 9,5 tokens par seconde. Je
[00:01:32] regarde ce qui se passe, et là, je vois
[00:01:34] que le processeur, il est à fond et que
[00:01:35] mes cartes graphiques, elles font
[00:01:36] presque rien. Le vrai problème, c'est
[00:01:38] pas la puissance, c'est la RAM. Le 10
[00:01:40] septembre, première bonne nouvelle, je
[00:01:43] tombe sur un moteur qui a une idée super
[00:01:45] simple, garder dans la carte les experts
[00:01:47] les plus utilisés. Les experts chauds
[00:01:49] restent en VRAM, les autres attendent à
[00:01:51] côté. Je démarre ce moteur, et là, 24,5
[00:01:54] tokens par seconde. Plus de trois fois
[00:01:56] plus vite sans changer de matériel. Et
[00:01:58] première surprise, ma deuxième carte ne
[00:02:00] sert plus à rien. Du coup, moi je veux
[00:02:02] tout de suite une meilleure qualité. Je
[00:02:04] prends un quant plus gros, le Q4KM, et
[00:02:06] là c'est le piège. Ces experts dépassent
[00:02:09] de ma RAM. Le modèle met une minute à
[00:02:11] lire ma question avant d'écrire le
[00:02:12] premier mot. Mais j'abandonne pas. Je
[00:02:14] bloque le modèle en RAM et je mets neuf
[00:02:16] couches en VRAM. Le pré-fil passe de 31
[00:02:19] à 206 tokens par seconde. Le problème
[00:02:22] est réglé. Mais j'ai compris la règle du
[00:02:23] jeu. Ici, tout doit tenir en RAM.
[00:02:26] [grognement]
[00:02:26] Fin septembre, je prends une décision.
[00:02:28] J'abandonne complètement la llama.cpp et
[00:02:31] je passe à un moteur écrit exprès pour
[00:02:33] ce type de modèle. Son astuce, c'est
[00:02:35] d'activer le MTP. Deviner plusieurs
[00:02:38] tokens d'avance, puis les vérifier d'un
[00:02:40] seul coup. La vitesse double. Je passe à
[00:02:42] 58 tokens par seconde. Je continue
[00:02:44] d'améliorer, j'atteins 64 puis 70 tokens
[00:02:48] par seconde. Et le pré-fil atteint même
[00:02:50] 1000 tokens par seconde. Et puis, un
[00:02:53] soir d'octobre, j'ai eu très peur. Je
[00:02:54] lance un test de trop, la RAM se remplit
[00:02:57] complètement, le serveur se bloque et
[00:02:59] impossible de m'y connecter. Et je ne
[00:03:00] peux pas aller le redémarrer à la main
[00:03:02] parce que je me trouve pas au même
[00:03:03] endroit que le serveur. Depuis ce jour,
[00:03:05] je fais super attention, je lance plus
[00:03:07] aucun test sans protection. J'ai mis en
[00:03:09] place une limite de RAM, une coupure
[00:03:11] automatique en cas de problème et un
[00:03:12] redémarrage automatique. À ce moment-là,
[00:03:14] je me dis "Et si j'écrivais mon propre
[00:03:16] moteur, fait exprès pour cette ?" En une
[00:03:18] journée, il passe de 29 à 63 tokens par
[00:03:22] seconde. C'est super motivant, mais il
[00:03:23] reste quand même moins rapide que celui
[00:03:25] que j'utilisais déjà. Je le mets de
[00:03:26] côté, mais j'ai compris où le temps
[00:03:28] était perdu. Fin octobre, je découvre
[00:03:31] Basalt, un moteur encore plus récent. Il
[00:03:33] promet vraiment beaucoup. Je l'installe,
[00:03:35] je lance et là, 57 tokens par seconde.
[00:03:38] Moins bien qu'avant. J'étais vraiment
[00:03:40] déçu. Mais je peux pas y croire. Je
[00:03:41] pense qu'il y a un problème, alors je
[00:03:43] cherche d'où ça vient. Et là, je trouve,
[00:03:45] 10 Go de RAM occupés pour rien, à cause
[00:03:47] de mes anciens tests. Je nettoie, je
[00:03:49] relance et là, 94 tokens par seconde. Et
[00:03:52] le pré-fil décolle, 2200 tokens par
[00:03:55] seconde.
[00:03:55] [grognement]
[00:03:56] Début novembre, je veux une meilleure
[00:03:57] qualité. J'essaie d'autres quants et là,
[00:04:00] c'est bizarre. Chacun retombe à 63
[00:04:02] tokens par seconde. Je pense d'abord que
[00:04:04] c'est le moteur, puis la machine et je
[00:04:05] me trompe deux fois en fait. Le
[00:04:07] problème, c'est une seule couche sur 48
[00:04:09] dans un format que le mode rapide ne
[00:04:11] connaît pas. À cause d'elle, tous les
[00:04:12] modèles passent en mode lent. Je
[00:04:14] convertis cette couche et là, j'atteins
[00:04:15] 83 tokens par seconde. Reste une grande
[00:04:18] question, quel quant ? J'en ai essayé
[00:04:20] neuf. Les plus gros sont trop lourds,
[00:04:22] leurs experts ne tiennent pas en RAM. La
[00:04:24] surprise vient des plus petits. Celui de
[00:04:26] Unsloth, le UDIQ2XS,
[00:04:29] il garde la précision là où c'est
[00:04:30] important et obtient 99,4 de la qualité
[00:04:33] d'origine. En perplexité, il fait 3,285
[00:04:37] contre 3,273
[00:04:39] pour le modèle d'origine. C'est presque
[00:04:41] pareil. Plus petit et meilleur que des
[00:04:43] quants de plus gros, c'est lui que je
[00:04:44] garde. Bon, je fais le point sur tout
[00:04:46] ça. Voilà tout le chemin parcouru de fin
[00:04:49] août à début novembre. On voit trois
[00:04:51] grands sauts. Et à chaque fois, c'est
[00:04:53] pas le matériel qui a changé, c'est
[00:04:54] simplement le moteur. Et ma deuxième
[00:04:56] carte dans tout ça, la RTX 3070, au
[00:04:59] début, elle m'apportait 20 % de vitesse.
[00:05:01] Avec le cache d'experts, plus rien. Avec
[00:05:03] le moteur spécialisé, 10 à 15 % et avec
[00:05:06] Basalt, elle ralentit tout. La version
[00:05:08] officielle de Basalt le refuse même.
[00:05:10] Basalt est uniquement compatible avec
[00:05:12] les cartes qui commencent par 50. Plus
[00:05:14] le moteur est bon, moins il sert. Au
[00:05:16] final, cette carte, je vais pas
[00:05:17] l'utiliser. Une fois le modèle bien
[00:05:19] réglé, je me pose une : et s'il existait
[00:05:21] ? J'essaie Swift qui réfléchit moins
[00:05:24] longtemps. Un mois plus tard, je reviens
[00:05:25] à l'original. Puis, Edge Zero qui promet
[00:05:28] plus de vitesse avec des experts d'un
[00:05:30] nouveau genre. Converti au format
[00:05:31] classique, il est rapide, mais sa
[00:05:33] qualité baisse beaucoup. Alors, je
[00:05:34] modifie le moteur pour pouvoir le lire
[00:05:36] sans rien perdre. Ça marche, mais il
[00:05:37] dépasse pas 57 tokens par seconde.
[00:05:40] Alors, je supprime tout. Je continue de
[00:05:41] chercher, je fouille sur Hugging Face et
[00:05:43] là, je trouve environ 1600 versions de
[00:05:46] ce modèle. Presque toutes sont de
[00:05:47] simples quants ou des versions
[00:05:49] Uncensored, mais il y a un seul nom qui
[00:05:51] ressort, c'est le Tinfield 1. Un fine
[00:05:53] tune fait pour le code. Lui, c'est un
[00:05:55] vrai concurrent. Je le télécharge, le
[00:05:57] convertis et j'organise un duel entre
[00:05:59] les deux. Premier round, la vitesse.
[00:06:01] Tinfield gagne, 80 tokens par seconde
[00:06:03] contre 68. Deuxième round, je demande à
[00:06:06] chacun une petite application et là
[00:06:08] c'est celle de Tinfield qui est plus
[00:06:09] propre. Du coup, je me dis ça y est,
[00:06:11] j'ai trouvé mieux, mais je veux en avoir
[00:06:12] le cœur net. Alors, je l'ai fait
[00:06:14] travailler comme des agents seuls sur 10
[00:06:16] tâches corrigées automatiquement. Sur
[00:06:18] les six tâches faciles, égalité
[00:06:20] parfaite. Sur les quatre tâches
[00:06:21] difficiles, Flash Next réussit tout et
[00:06:23] Tinfield bloque sur la plus dure. Il
[00:06:25] réécrit son code deux fois sans jamais
[00:06:28] lancer ses tests. Résultat, 9,5 sur 10
[00:06:31] pour Flash Next et 8,95
[00:06:33] pour Tinfield. Plus rapide, mais moins
[00:06:35] fiable. Le champion garde sa place.
[00:06:37] Alors, [grognement] qu'est-ce que j'ai
[00:06:38] appris en 3 ? 1, la limite, c'est pas la
[00:06:41] carte graphique, c'est la RAM. 2, le
[00:06:44] moteur compte plus que le matériel. Il
[00:06:46] multiplie la vitesse par 10. 3, un quant
[00:06:49] bien fait bat un quant plus gros. 4, une
[00:06:51] 2e carte plus lente peut faire perdre du
[00:06:53] temps. 5, les impressions trompent.
[00:06:55] Avant de changer de modèle, il faut
[00:06:57] mesurer. Aujourd'hui, mon modèle tourne
[00:06:59] à 83 token par seconde en décode et 2200
[00:07:02] en préfile sur une machine que beaucoup
[00:07:04] de gens pourraient avoir chez eux. J'ai
[00:07:05] simplement installé dans mon PC deux
[00:07:07] barrettes de 16 Go et deux barrettes de
[00:07:09] 8 Go en DDR4 plus une carte graphique
[00:07:12] 5060 TI, donc l'entrée de gamme au
[00:07:15] niveau de la dernière génération de
[00:07:16] carte graphique. Le même modèle, le même
[00:07:18] équipement et pourtant 11 fois plus vite
[00:07:20] qu'au 1er jour. Et je pense que
[00:07:22] l'histoire n'est pas encore finie.
[00:07:23] C'était Antoine InLine. À la prochaine.