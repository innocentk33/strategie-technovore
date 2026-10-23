# vas-y, viens, on recode Windows de zéro

- Chaîne : v2f · https://www.youtube.com/watch?v=ELTwwTsR5w8
- 1 468 203 vues au 23/10/2026 (vidIQ) · durée 23:41
- Sous-titres manuels récupérés avec yt-dlp le 23/10/2026, dédoublonnés ; un paragraphe ≈ 15 s, horodaté au début.

[00:00] Le projet de code le plus compliqué. C'est ce qui est dit. A chaque fois que je cherche des infos sur comment coder un système d'exploitation, il y a un paragraphe entier pour me dire « Tu vas saigner ! » Et c'est logique. Ton écran, ta souris, ton clavier, ton disque dur, c'est à toi de les gérer. T'as rien, rien à ta disposition.

[00:19] Les fonctions les plus basiques et anodines n'existent plus. Et ça te prend des heures de recherche et des centaines de lignes de code pour recréer leur fonctionnement. Le python, il est parti chercher du lait. Il reviendra plus. Et tes parents adoptifs, c'est le C et l'Assembly. Un scénario digne des orphelins Baudelaire. Mais non, non, pleure pas.

[00:36] La situation pourrait être bien pire. Elle vient tout juste de le devenir. Victor, t'as une semaine pour te rapprocher autant que possible de Windows 11. Pas plus. Tu te démerdes. Pourquoi est-ce que je m'inflige ça ?

[00:54] Tout ça pour des likes. Je serais peut-être temps de stopper YouTube. Je m'appartiens à la campagne. Ferme-la. Le chrono est déjà lancé. Pourquoi tu continues de regarder mon téléphone, là ? Ouais, je suis sur un Wi-Fi public. Et alors ? Eh, dangereux. Comment ça, c'est dangereux ? Y a rien à craindre. Tous les sites utilisent du HTTPS.

[01:11] Mes données sont cryptées. Y a aucun moyen qu'un hacker puisse les voir. Ouais, sauf que le hotspot Burger King Wi-Fi gratuit a été créé par un hacker. Il peut voir tous les sites que tu consultes, combien de temps t'y as passé. Et pire encore, il peut faire une attaque de SSL stripping pour te forcer à utiliser du HTTP. Quand tu communiques.

[01:28] Avec les sites web. Donc, plus de chiffrement et toutes tes données sensibles sont en fait visibles. Pour éviter ça, il suffit d'utiliser CyberGhost VPN, le sponsor de la vidéo. Ce VPN cachera toutes tes infos et gardera tes données chiffrées à tout moment. Plus aucun souci. Grâce à leurs 11 000 serveurs dans 100 pays, tu peux dire adieu au contenu géobloqué et bonjour au catalogue international de 40 services de streaming différents, dont par exemple Netflix, Prime Vidéo ou encore Disney+.

[01:54] CyberGhost VPN est fiable et facile à utiliser sur Windows, MacOS, iOS, Android et même sur des Smart TV ou encore des consoles. Tu peux l'utiliser avec cet appareil en simultané, ce qui est parfait pour toute la famille. Et ouais, c'est pas pour rien que 38 millions d'utilisateurs leur font confiance et que leur note sur Trustpilot est excellente.

[02:12] Utilise le lien en description maintenant pour avoir 83% de réduction sur ton abonnement. Soit 2,03 euros par mois avec 4 mois gratuits, garantie satisfait ou remboursé pendant 45 jours avec un support qui est disponible 24 heures sur 24 si t'as un problème. Alors t'attends quoi ? Allez, ok, maintenant on code. La première étape est forcément un Hello World.

[02:31] Quand t'apprends un nouveau langage de programmation, c'est par ça qu'on te fait commencer. Afficher Hello World sur ton écran. Bah, on va faire la même. Un OS ou système d'exploitation, mais dire OS c'est quand même plus rapide. Désolé les académiciens. Un OS qui affiche juste Hello World. Et c'est tout.

[02:46] Bah ouais c'est tout alors dépêche-toi on a pas... Héhéhé t'as pas écouté la vidéo ou quoi ? C'est déjà beaucoup. D'habitude, faire un Hello World c'est littéralement une ligne de code. Ici c'est 27 lignes de code. Et tu vas dire, je vais devoir lire plusieurs pages de docs pour comprendre exactement ce qui se passe quand ton ordi s'allume. Mais heureusement pour toi, je vais tout te résumer.

[03:05] Quand tu allumes ton ordi, le premier programme qui se lance c'est le BIOS ou UEFI sur les machines les plus modernes. Mais moi je vais me concentrer sur le BIOS. Ce petit logiciel se trouve sur une puce de ta carte mère. Tout est déjà codé par son fabricant, y'a rien à faire. Le BIOS va se charger d'identifier et de configurer le matériel de ton ordi. Une fois que c'est fait, il lance le test POST qui consiste à vérifier que tout fonctionne bien et à t'afficher les résultats à l'écran.

[03:27] Si tout est OK, il va alors vouloir donner les commandes à notre OS. Mais comment est-ce qu'il sait où se trouve notre OS ? Quelle taille il fait ? Quelle fonction appeler ? Bah il en sait rien. Tu vois le BIOS, il est un peu débile, un peu archaïque. Bah désolé mais c'est la vérité mon gars. On va devoir l'aider en codant un petit programme intermédiaire entre lui et notre OS, j'ai nommé le bootloader.

[03:49] L'avantage du bootloader c'est qu'on peut le créer en suivant des spécifications très strictes définies par le BIOS, ce qui lui permettra d'être facilement retrouvé par ce dernier. Parce que oui, explorer les 4 Teraoctets de mes SSD à la recherche d'un bootcode, c'est pas viable. Pour éviter ça, on va placer le code de notre bootloader dans le boot sector, une seule adresse que le BIOS va regarder pour voir si notre bootloader s'y trouve ou non.

[04:11] C'est quand même beaucoup plus simple. Mais comment est fait pour savoir qu'il y a bien le code du bootloader qui s'y trouve et que c'est pas juste des données random ? Et bien grâce à deux propriétés. Le code du bootloader doit faire exactement 512 octets et se terminera toujours par cette signature binaire très spécifique. Donc notre BIOS analyse le boot sector de chaque dispositif de stockage que dispose l'ordi, et il y regarde s'il y a un segment de 512 octets qui se termine par notre signature.

[04:36] Si c'est le cas, il sait que c'est le bootloader. Du coup il charge son code en mémoire, plus précisément à l'adresse OX7C00, et il l'exécute depuis le tout premier bit. Ok, codons ça. Mais en quel langage ? Bah tu l'auras deviné... Ouais, je sais.

[04:53] Mais c'est le langage qui se traduit le plus directement en binaire pour notre machine. Et c'est le seul à réunir toutes les caractéristiques requises. Y'a pas le choix. Commençons par la fin, avec la signature binaire. Pour ça, y'a juste à la définir. Et oui, ce nombre c'est bien notre signature, mais on l'a juste écrit en hexadécimal. Assurons-nous à présent que le fichier fasse 512 octets exactement.

[05:14] Cette dernière instruction prend deux octets. Il nous en reste 510 à remplir. On va donc calculer la taille de notre code depuis la position actuelle jusqu'à la première ligne, et voir combien d'octets il nous manque. Et pour ce nombre manquant, on va répéter l'ajout de zéro. Donc si on regarde le fichier binaire créé depuis notre Assembly, on a notre signature, notre code qui sera au début, et entre les deux, on a ajouté plein de zéros pour atteindre les 512 octets.

[05:38] Maintenant, il ne reste plus qu'à écrire quelque chose sur l'écran. Comment ? Tu te rappelles du BIOS ? Le moyen le plus rapide de faire ça, c'est avec son aide. Ouais, peut-être qu'on aurait pas dû l'insulter au final. Je te disais que le BIOS affichait à l'écran les résultats du test POST. Donc ça veut dire qu'il possède une fonction qui affiche un caractère à l'écran. On peut lui demander de l'utiliser pour nous.

[05:58] Cette demande se fait via une interruption. Une interruption, ça consiste à demander à notre CPU de cesser ce qu'il fait, d'exécuter une demande prioritaire, puis de revenir à ce qu'il faisait avant. L'interruption OX10 est celle qui permet de demander au CPU d'utiliser le service d'affichage vidéo du BIOS.

[06:16] Et pour communiquer notre volonté exacte au BIOS, on va lui transmettre des valeurs via les registres du CPU. Un registre, c'est juste un petit endroit où on peut stocker une donnée. Plus précisément, en stockant la valeur 0E dans le registre AH, on demande à afficher un caractère à l'écran. On aurait aussi pu demander d'afficher un pixel ou de changer la position du curseur, par exemple.

[06:37] Et dans le registre AL, on stocke le caractère qu'on veut afficher à l'écran. Donc on file nos variables en modifiant les valeurs des registres du CPU, puis on appelle l'interruption. Le CPU prend la main, regarde à quoi l'interruption correspond et donne le contrôle au BIOS qui s'occupe ensuite de regarder quelles fonctions on souhaite utiliser, en récupérant la valeur du registre AH.

[06:58] Il sait maintenant qu'on veut afficher un caractère. Il cherche la valeur du registre AL pour savoir lequel et il le fait. Et voilà, c'est fait. On va afficher un caractère. Un dernier truc, on va ajouter une boucle infinie, un bout de code que le CPU exécutera en continu sans s'arrêter. Pourquoi ?

[07:14] Parce que le CPU, il a le mindset du grind, mon gars. Il s'arrête jamais de bosser. Il veut exécuter des instructions non-stop. Et s'il arrive à la fin du code de notre bootloader, il va alors exécuter le code qui se trouve juste là. Tout ça après, en mémoire. Sauf que ça, c'est des valeurs random qui veulent rien dire. Donc il exécute n'importe quoi et il va crasher, ce débile.

[07:34] Mais si on le bloque dans notre boucle infinie, il ne crashera pas. Et là, nous y est. On a affiché AH à l'écran. C'est bien, mais il nous manque 10 lettres. On pourrait juste copier-coller et puis basta. Mais faire ça, c'est dégueulasse. 0 sur 10. Mais il y a du potentiel.

[07:50] Et pour l'atteindre, il suffit de faire une fonction qu'on exécute pour chaque caractère de notre phrase. Hello world. 8 minutes. On a mis 8 minutes de vidéo pour expliquer un hello world. Je pense que tu comprends maintenant dans quelle galère on se trouve. Du coup, maintenant, il est temps. On va enfin booter notre OS.

[08:07] Non, on doit d'abord passer en mode protégé. Les fabricants de CPU sont obsédés par la rétro comptabilité. Ils veulent que si tu prends un vieil iOS bien préhistorique et que tu le lances sur ton CPU dernier cri, ça marche nickel. Et pour faire ça, il faut émuler un CPU préhistorique. Attends, je crois que je viens d'insulter une partie de mon audience là.

[08:28] Ouais, non, non, non, mais pas vous. Le temps passe plus vite en technologie, c'est connu, c'est bon. Non, non, non, non, non, non, non. OK, donc quand on boot, notre CPU se comporte comme s'il datait de 1978. C'est ce qu'on appelle le mode réel dans lequel on a par exemple moins de 1 mégaoctet de RAM disponible. 1 mégaoctet.

[08:46] On ne peut pas rester comme ça. C'est à nous d'avancer le temps et à demander à notre CPU d'arrêter son cosplay. On va le faire en passant en mode protégé, ce qui sera amplement suffisant pour nous. Et on aura maintenant, tiens toi bien, jusqu'à 4 gigaoctets de RAM. Et ce mode protégé nous permettra aussi, comme son nom l'indique, de protéger notre OS.

[09:05] Parce qu'en mode réel, il y a zéro protection. Tu installes une appli, elle peut faire tout ce qu'elle veut. Accéder à toute la mémoire, toutes les ressources, utiliser toutes les instructions imaginables. Bref, avec le mode protégé, on va pouvoir restreindre les applications extérieures. Il y a différents niveaux de privilèges qu'on appelle Rings. La Ring 0 est celle qu'utilisera notre OS et qui aura le plus de liberté.

[09:26] Aucune restriction. Une application lambda, elle, sera en Ring 3. Avec très peu d'accès et si jamais l'appli a besoin d'une ressource protégée par exemple, elle sera obligée de demander l'autorisation à notre OS qui décidera ce qu'il en est. On doit donc mettre en place des règles. Et ces règles, ça nous aide de les définir et de les donner au CPU.

[09:45] On fait ça avec la Global Descriptor Table ou GDT. Comme son nom l'indique, c'est une table qui va nous permettre de définir différents segments au sein de notre mémoire. Chaque entrée de la table définit un de ces segments. On donne l'adresse du début du segment, sa taille, puis certaines propriétés qu'on va lui donner comme par exemple est-ce que cette section peut être lue, modifiée, exécutée, quel niveau de privilège ?

[10:07] Et comme ça, tout est sécurisé. C'est intéressant, hein ? Eh ben on s'en bat les couilles ! Eh ouais, cette histoire de segmentation, elle est plus utilisée de nos jours. Maintenant, on fait du Paging, qu'il faudra setup encore plus tard. Bon, si on a le temps. Mais malgré tout, on doit définir une GDT. C'est obligatoire.

[10:24] Encore une fois, une histoire de réglementation. Une histoire de rétro-comptabilité. On va donc créer une GDT avec en fait... aucune segmentation. C'est ce qu'on appelle le Basic Flat Model, qui est d'ailleurs décrit dans le manuel utilisateur d'Intel. Ça consiste à intégrer trois entrées dans notre table GDT. Les trois entrées qui sont en fait...

[10:41] obligatoires. On commence avec le descriptor nul, avec tous ses bits à zéro. On définit ensuite un segment qui pourra contenir du code, et un segment pour les données. La seule différence, c'est que le code peut être lu, exécuté, mais pas modifié, alors qu'une donnée peut être lue, modifiée, mais pas exécutée. Dans les deux cas, on leur donne un max de privilèges avec le ring 0.

[11:00] Et on fait ensuite en sorte qu'ils prennent tout l'espace disponible de la mémoire. Donc en fait, ils se chevauchent, ils sont superposés. Comme dit plus tôt, on veut pas de segmentation. C'est pour ça. Et voilà, on a notre table. Plus qu'à noter où elle commence, ainsi que sa taille, et de donner ses infos à notre CPU pour qu'il sache où la retrouver. Maintenant qu'on a notre GDT défini, on va pouvoir passer en mode protégé.

[11:21] Pour ça, il suffit de désactiver les interruptions. En effet, les interruptions actuelles sont en mode protégé. Les interruptions actuelles sont gérées par le BIOS. Sauf que le BIOS, il fonctionne qu'en mode réel. On peut plus l'utiliser. Va falloir qu'on s'occupe nous même des interruptions plus tard. Ensuite, on a juste à changer la valeur du registre CR0 de notre CPU. Dès que cette valeur est modifiée, notre CPU sait qu'il est en mode protégé et qu'il ne faut plus fonctionner en mode réel.

[11:43] Et enfin, on a un dernier petit problème à régler. Les CPU sont ultra rapides. Et pour être aussi efficace, ils utilisent ce qu'on appelle le pipelining. En gros, quand le CPU exécute une ligne de temps code, il le fait en plusieurs étapes. D'abord, il charge l'instruction. Ensuite, il décode pour savoir exactement comment la traiter avec ses différents composants et ensuite, il l'exécute.

[12:05] Pour aller aussi vite que possible, il peut faire ces étapes en parallèle sur plusieurs instructions de ton code. Prenons un exemple. Le CPU commence par charger la première ligne de ton code. Quand il a fini, il commence à la décoder et en parallèle, il charge la ligne suivante. Une fois que la première ligne est décodée, le CPU l'exécute et en même temps, il décode la ligne 2, qu'il venait de charger et il en profite pour charger la ligne 3.

[12:28] Le problème qu'on a, c'est que si on passe en mode protégé, il est possible que les instructions suivantes, qui sont censées être exécutées en mode protégé, le soient en fait en mode réel, vu qu'il a pris de l'avance avec le pipelining. Et ça, ça pose problème. Il faut empêcher ce pipelining. Et pour faire ça, on va faire un long jump.

[12:47] On va effectuer un saut lointain dans notre code. Le CPU ne saura donc pas quelle est la prochaine instruction tant qu'il n'aura pas fait ce saut. Il ne pourra pas la charger. Il ne pourra pas faire de pipelining. Il sera obligé d'attendre. Et nous, on sera sûr qu'il sera en mode protégé. Maintenant qu'on est en mode protégé, on va enfin pouvoir charger notre OS. Et cette OS, on va pouvoir le coder en C.

[13:10] Si on m'avait dit un jour que je célébrerais le fait de coder en C... Bon, pour tester notre code, on va faire un OS ultra simple avec juste une boucle infinie. Un peu comme ce qu'on avait fait pour notre OS Hello World en mode réel au début de la vidéo. Ça, c'est notre code C qui permet de le faire. On veut le compiler pour le transformer en code binaire pour pouvoir l'exécuter. Mais il y a un petit problème.

[13:28] Ouais, il y a toujours un petit problème quand tu codes en bas niveau. Ça pète les c... Notre compilateur C, il est conçu pour créer un code binaire pour Windows 11 sur ma machine en 64 bits avec toutes les fonctions système et tout le bordel. Sauf que ce code, on va l'exécuter pas sur Windows, mais sur ça. Notre architecture toute pourrie.

[13:46] Il y a un 32 bits qui n'a aucune fonction de la bibliothèque standard C qui n'a rien de défini. Si on compile avec mon compilateur actuel, ça va crasher. On doit donc créer un cross compiler. On va créer un compilateur qui produira un code binaire adapté à notre OS qu'on est en train de coder. Ça a l'air compliqué, mais ça l'est pas.

[14:03] Il faut juste télécharger le code du compilateur C qui se trouve en ligne. Tu lui files en paramètres l'architecture qu'on veut utiliser et qui est adaptée à ce qu'on code. Puis on exécute ça et paf, ça nous crée un compilateur spécial pour notre système avec lequel on compile notre code. OK, bon, c'est top, mais il faut aussi qu'on puisse appeler le code de notre OS depuis notre bootloader.

[14:23] Le problème, c'est que... On ne sait pas où il est le code de notre OS. Réglons ça en liant le code de notre OS avec celui du bootloader et en créant une image disque bootable par un ordi qui combine les deux codes. Ce qui fait que notre OS sera juste après le code de notre bootloader. Bootloader qui se trouve dans le boot sector, comme dit en début de vidéo.

[14:42] On peut donc à présent, dans notre bootloader, charger le code de notre OS depuis notre dispositif de stockage. Et on fait ça en utilisant une fonction du BIOS déjà définie, comme on l'avait fait pour notre Hello World. Ce sera cette fois ci avec l'interruption 13. Une fois que ça s'est exécuté, on a chargé le code à cette adresse dans la RAM qu'on a choisi simplement car on est sûr que ce sera une zone libre.

[15:02] Une fois passé en mode protégé, il n'y a plus qu'à appeler ce code et le tour est joué. On a un écran noir comme prévu dans lequel on peut voir notre reflet et lentement réaliser qu'on a passé des heures de recherche et des heures de code juste pour avoir un foutu écran noir. Ajoutons des features à notre OS maintenant.

[15:19] Il est un peu léger comme ça. Déjà, ce serait bien de pouvoir afficher du texte à l'écran. Ah bah, c'est facile. On a juste à utiliser la fonction du BIOS comme on l'avait fait au début. Bah non, le BIOS, je te l'ai dit, il marche qu'en mode réel et on est en mode protégé. Va falloir se démerder sans. Bon, t'inquiète pas, c'est pas compliqué. L'écran est géré par notre carte graphique et quand on boot, elle est en mode VGA.

[15:39] Un mode graphique ancien avec une résolution dégueulasse. Encore une fois, pour des raisons de rétrocompatibilité. Mais ce mode VGA, il possède un mode texte qui va nous faire gagner beaucoup de temps. Et vu qu'on est à la bourre, ça tombe bien. Le mode texte possède déjà une police d'écriture. Tout ce qu'il faut. Il suffit simplement de dire à notre carte graphique quel caractère afficher et où le mettre.

[15:59] Plus précisément, le mode texte VGA fonctionne avec une grille de 80 x 25 caractères. Chaque caractère de la grille est défini par deux octets. Le premier est son code ASCII et le deuxième les propriétés avec lesquelles il doit être affiché à l'écran. Cette grille est stockée à l'adresse OXB8000. Donc, si je pointe à cette adresse, puis que je définis le premier octet comme la lettre E et le deuxième octet comme la valeur OX0F, j'obtiendrai un code qui va nous donner une liste de l'adresse.

[16:24] Je vais donc afficher un E blanc au tout début de mon écran. Et de là, afficher un caractère n'importe où, c'est facile. C'est deux fois la ligne sur laquelle on veut afficher le caractère, fois le nombre de colonnes par ligne, plus la colonne à laquelle on veut afficher le caractère. Et si on sait imprimer un caractère, on sait imprimer une phrase.

[16:42] Hello World version 2. Mon gars, on l'a fait, mais on n'en a pas fini avec la gestion de l'écran. Avoir un petit curseur qui te dit où tu es actuellement, c'est quand même utile. Surtout quand on voudra que l'utilisateur puisse taper des commandes. Là, t'imagines sûrement qu'on va juste afficher un petit caractère dans notre grille et basta. Eh bah non, à chaque fois, c'est contre intuitif.

[17:00] Pour notre grille de caractères, on communiquait avec la carte graphique via la mémoire RAM. Pour le curseur, on va communiquer directement via le port entrée sortie qui lie le CPU à notre carte graphique. Plus précisément, on veut communiquer la position du curseur. Mais il y a un petit problème.

[17:16] Encore, encore un petit problème. Toujours des petits problèmes. La position fait 16 bits. Sauf que le port entrée sortie ne peut que transmettre 8 bits. A la fois 16 bits, c'est trop. Ça ne rentre pas. Pour résoudre ce problème, on va en fait utiliser deux ports. Avec le port 3D4, on indique à la carte graphique qu'on lui envoie les 8 premiers bits de la position du curseur. Ensuite, via le port 3D5, on envoie ces 8 premiers bits.

[17:41] On indique ensuite via l'autre port qu'on envoie les 8 derniers bits et hop, on les envoie ensuite. Et maintenant, on a un curseur qu'on peut facilement mettre à jour dès qu'on écrit à l'écran. Dernier point important, on aimerait pouvoir scroller quand on arrive à la fin de l'écran. Bah oui, il faut tout faire soi même. Pour ce faire, quand on atteint la dernière ligne, on va juste décaler tous les caractères de notre grille d'une ligne.

[18:01] La gestion de l'écran, c'est fait. On peut même afficher le logo de notre OS lors du boot. Et j'ai choisi SOS comme nom. Je trouvais que ça décrivait parfaitement l'état actuel du créateur de cette atrocité. Faisons à présent en sorte de pouvoir interagir avec notre OS via le clavier. Alors le clavier, tout dépend s'il est en USB, en Bluetooth ou encore en PS2.

[18:22] Un vieux câble bien préhistorique. Dans les deux premiers cas, on gère le clavier en faisant du polling, ce qui consiste à lui demander sans arrêt une touche a été pressée? Non, c'est sûr. Et là? Et maintenant? Il a appuyé? Toujours pas? Alors que dans le cas du clavier PS2, c'est plus tranquille parce que c'est le clavier qui va nous donner l'info qu'une touche a été pressée via une interruption du CPU.

[18:41] Mais ça, le fait que ça pouvait varier, je ne le savais pas. Moi, je pensais que c'était pareil pour tous les claviers. Parce que quand tu recherches des infos sur le net, tu tombes tout le temps sur la méthode utilisée pour le clavier PS2. Du coup, c'est celle que j'ai implémentée alors que j'ai un clavier USB, mais par chance, c'est pas grave parce que Kemu, Kemu, Kemu, Kemu, qui est le programme qui permet de tester mon OS en le simulant, fait en sorte que mon clavier USB se comporte aussi comme un clavier PS2.

[19:07] Donc ça marche nickel alors que ça devrait pas. La chatte. Ce qui se passe quand on appuie sur une touche en version PS2, c'est que le clavier trigger une interruption et le CPU regarde comment notre OS souhaite la gérer. Sauf que pour l'instant, on gère rien du tout. Changeons cela en créant ce qu'on appelle une ID. Téléphone.

[19:24] C'est une table qui décrira toutes les interruptions possibles en indiquant pour chacune si elle est bien prise en charge, quel type d'interruption c'est, quel niveau de privilège est requis pour l'appeler. Mais surtout, on indique quelle fonction de notre OS appelée quand cette interruption a lieu. Une fois la table créée, on la file à notre CPU et le tour est joué. Dans notre cas, il n'y a que l'interruption clavier qui nous intéresse.

[19:43] Le reste, on va les rediriger vers une fonction bidon qui fait rien. Mais quand c'est une interruption clavier, notre CPU saura qu'il faut rediriger le code vers cette fonction de notre OS qui va se charger de récupérer la touche qui a été pressée en communiquant avec le contrôleur clavier via le port entrée sortie 0X60. Le port nous file ce qu'on appelle un scan code, qui est juste un chiffre qui représente une touche du clavier.

[20:05] Si c'est une touche normale, on l'affiche à l'écran pour permettre de taper quelque chose. Si c'est la touche supprimée, on supprime la lettre précédemment tapée. Si c'est la touche entrée, on exécute la commande correspondante à ce qui a été tapé jusque là. Mais pour l'instant, on n'a aucune commande. Je pense que la première qu'on devrait créer, c'est une commande pour créer un fichier texte et le charger. Et pour faire ça, il va falloir gérer la mémoire de notre ordinateur.

[20:27] Alors, tu l'auras compris, c'est toujours un peu la même chose. L'OS s'occupe de gérer la logique, puis communique avec le matériel de notre ordi pour exécuter des actions précises. Jusqu'à maintenant, en utilisant les ports entrées sorties ou encore un espace défini dans la RAM. Pour le stockage, il existe plusieurs façons de gérer la logique, mais celle qu'on va utiliser est une des plus simples.

[20:45] Le FAT, qui, anecdote rigolote, a été inventé par Mark McDonald. Ouais, ça me fait rire. OK. Ça, c'est notre disque dur. Il est divisé en tout un tas de secteurs de 512 octets. Tu te rappelles du Boot Sector et du Bootloader de 512 octets ? Cette taille, ça vient de là.

[21:02] Ces secteurs, c'est la plus petite unité de stockage que notre matériel peut lire ou écrire. Donc, même si tu lui demandes d'écrire un seul octet sur ton disque dur, il va en fait écrire tout un secteur avec ton octet au début. Parce que si on manipulait un octet par un octet, ton disque dur serait beaucoup trop lent. Mais n'empêche que les secteurs, c'est encore trop petit.

[21:22] Sur un teraoctet, il y a 2 milliards de secteurs à gérer. C'est beaucoup trop. Il faut élargir. Et c'est ce que fait le FAT, qui va regrouper ces secteurs dans ce qu'on appelle des clusters. Dans un cluster, par exemple, ça peut être 8 secteurs mis ensemble. Maintenant, on peut facilement noter tous les clusters existants dans la File Allocation Table ou FAT. Quand notre OS voudra créer un nouveau fichier, il va parcourir cette table jusqu'à trouver suffisamment de clusters libres pour pouvoir stocker les données du fichier.

[21:50] Et quand c'est le cas, il va lier ces clusters pour qu'on sache qu'ils représentent tous un seul fichier. Il va ensuite mettre les données de notre fichier dans ces clusters. Et enfin, dans une autre table, la Directory Table, il va noter le nom du fichier, sa taille et l'endroit du premier cluster qui contient les données. Comme ça, quand on voudra charger ce fichier, l'OS pourra parcourir cette Directory Table pour trouver son fichier dedans et regardera où se situe le premier cluster qui a les données.

[22:15] Il ira le chercher ainsi que tous les autres clusters qui lui sont liés et récupérera leurs données. Et voilà, c'est pas bien compliqué. Tu noteras que les clusters sont liés à tous les clusters qui lui sont liés et récupérera leurs données. Et voilà, c'est pas bien compliqué. Tu noteras que les clusters du fichier n'ont pas à être côte à côte. Ils peuvent être n'importe où. Et ça, c'est pratique parce que si tu as un fichier que tu veux modifier et agrandir, mais qu'il est adjacent à un autre, si les clusters étaient obligatoirement adjacents, on devrait écrire par dessus notre autre fichier.

[22:35] Et là, ça casse tout. Alors que dans notre cas, il peut juste créer un nouveau cluster plus loin dans le disque avec les données supplémentaires. Allez, plus qu'à mettre en place la suppression et la modification... Ok, bah non, du coup, on n'a plus le temps. Et je trouve ça hallucinant. Une semaine de code à fond. J'ai fait genre 1% de lui.

[22:52] Windows 11. J'ai vraiment réalisé à quel point c'est un projet titanesque. Mais tu sais quoi ? J'ai quand même réussi à te vendre mon OS. Admire. Dans un monde ultra connecté, il peut être dur de se concentrer sur ce qui est vraiment important.

[23:11] Mais ça, c'était avant. SOS, un design simple, épuré, qui ne réclame pas votre attention. Moins de features, moins de distractions et plus d'herbes touchées. Grâce à S. OS. L'OS qui a entendu votre appel à l'aide. Je suis spécial !

