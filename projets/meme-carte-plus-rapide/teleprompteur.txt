Sur une carte de 16 gigas, tu allumes un seul paramètre,
et ton IA écrit 2 fois plus vite :
de 29 à 64 tokens par seconde.
Même fichier, même carte, rien acheté.

Et c'est ce que trouvent 6 mesures publiées,
sur 5 modèles de cartes de 16 gigas :
entre 1,9 et 2,3 fois plus vite.
Du coup, ta carte, elle serait pas bridée, sans que tu le saches ?

Et attention : ça vaut pour l'écriture, sur Qwen 3.8 27B,
un modèle qui tient en entier dans la carte.

Aujourd'hui, on va voir le réglage qui peut doubler la vitesse de ta carte graphique,
et le moteur qui te permet d'y arriver.
Et surtout, tout ce qu'il faut éviter
pour ne pas perdre ce que tu as gagné :
une conversation trop longue, et c'est déjà un tiers de ta vitesse qui part.
Et reste jusqu'à la fin,
parce qu'on va démystifier un réglage que tu as peut-être allumé pour aller plus vite.

Le réglage qui double, c'est le MTP, un petit module en plus dans le modèle.
En gros, c'est comme les suggestions du clavier de ton téléphone :
le modèle propose plusieurs tokens d'avance, puis il les vérifie tous d'un coup.
Et quand il a deviné juste, il en écrit plusieurs pour le prix d'un.

Par contre, ça ne joue que sur l'écriture.
La lecture de ton prompt, elle,
ralentissait avec le MTP dans les premiers tests de mai.

Sur une 5080, on passe de 53 à 101.
Sur une 4060 Ti, de 17,6 à 40.
Et même chez AMD, sur une RX 9060 XT, de 15 à presque 29.
Donc même la Radeon double presque.

Sauf que 5 de ces 6 mesures viennent du même tableau en ligne,
avec le même script de test.
Du coup, la plus solide, c'est celle du début,
le 29 à 64 : elle a été mesurée à part, 5 fois.
Et elle trouve pareil.

En fait, dans le tableau, ce « 2 fois »,
c'est une moyenne sur du code, du texte et des commandes, avec la réflexion coupée.
Sur du texte seul, ça tombe à 1,8 fois sur la 4060 Ti.
C'est sur du code que ça gagne le plus.
Et sur un modèle à experts, les mesures tombent à 1,5 fois au mieux.

Alors, pourquoi je dis « bridée » ?
Parce que dans llama.cpp, le MTP ne s'allume pas tout seul.
Il faut le demander, et il faut un fichier qui contient le module,
un petit bout de modèle en plus.
LM Studio, lui, le gère depuis la version 0.4.22.
Tu le trouves dans le panneau des réglages
du modèle que tu as sélectionné.
Donc, que tu sois sur l'un ou sur l'autre,
va vérifier qu'il est bien allumé chez toi.

Sauf que le MTP a un prix : il prend de la place.
Selon les mesures, entre 1 et 2,5 gigas de VRAM en plus.
Et sur une carte de 16, c'est justement là que ça coince.

Donc le vrai réglage numéro un,
c'est que le modèle tienne en entier dans la carte.
Sur une 4080 de 16 gigas, avec un Qwen de 27 milliards plus ancien :
un fichier de 15 gigas qui déborde un peu, 20 tokens par seconde.
Un fichier de 11,5 gigas qui tient, 45.
Plus du double, juste en prenant un fichier plus petit.

Et si une partie du modèle sort de la carte, c'est la chute.
Sur une 5060 Ti,
quelqu'un a laissé dehors exprès 8 couches sur 48 d'un modèle plus petit :
on tombe de 43 à 12,5.
En fait, la partie restée en RAM va beaucoup plus lentement, et la carte l'attend.

Par contre, un fichier plus petit est plus compressé,
et aucune de ces mesures ne dit ce que tu perds en qualité.

Sauf que ces 2 gains ne s'additionnent pas.
Si le MTP fait déborder ton fichier, la chute mange ce qu'il te fait gagner.
Du coup, d'abord un fichier qui tient avec la place du MTP, ensuite le MTP.

Bon, rien qu'avec ces 2 réglages, ton modèle peut écrire jusqu'à 2 fois plus vite,
sur la carte que tu as déjà.
Donc avant d'en racheter une plus grosse, essaie ça.
Si cette vidéo t'a évité un mauvais achat, abonne-toi.

Et le moteur qui te permet d'y arriver, le programme qui fait tourner le modèle,
c'est llama.cpp : les 6 mesures du début ont toutes été faites dessus.
Quand tout tient dans la carte,
Ollama a été mesuré 10 % plus lent que llama.cpp, sur une 5060 Ti.
Et jusqu'à 30 % plus lent, sur une 3090.
Et LM Studio était presque à égalité avec llama.cpp : 76,8 contre 77.
Du coup, si tu es sur LM Studio, de ce côté-là, t'es tranquille.

Et même une mise à jour peut te ralentir.
Sur une 5080 avec Strata, un autre moteur,
un utilisateur a perdu 25 % en passant à une version plus récente.
Et sa version 0.2.14, sortie le 15 novembre, lit ton prompt plus vite,
mais écrit environ 10 % moins vite sur une 5070 Ti, d'après le projet lui-même.
Voilà pourquoi il faut noter ta version, pour savoir d'où vient un ralentissement.
Celles du 15 novembre sont à l'écran.

Et si ton modèle est trop gros pour la carte ?
Dans la vidéo précédente, je te l'ai montré :
la RAM pleine, et le disque qui se met à lire.

Sur un modèle à experts, dans llama.cpp, il y a un réglage à toi :
où vont les experts, ces petits spécialistes du modèle.
Lesquels restent sur la carte, et lesquels partent en RAM.
Le bon réglage, c'est d'en garder sur la carte autant que possible,
juste avant que ça plante.
Sur une 3060 de 12 gigas, ça a fait gagner 12 %.
Sur une 5060 Ti de 16,
avec le cache d'experts arrivé dans llama.cpp en octobre, 29 %.
Une seule mesure chacune, donc à prendre avec des pincettes.
Et leurs PC avaient 32 et 64 gigas de RAM.

Maintenant, le piège.
Plus ta conversation est longue, plus ça ralentit.
Tu te rappelles la mesure du début, à 29 tokens par seconde ?
À 64 000 tokens de conversation, elle tombe à 20.
Donc un tiers de vitesse en moins.
Et avec le MTP, les 64 deviennent 39.
Le MTP double toujours, mais tout descend.

Et ça peut être bien pire.
En fait, la mémoire de la conversation se range aussi dans la carte.
Et la 4080 qui montait à 45 avec le petit fichier ?
À 128 000 tokens de conversation, cette mémoire pousse le modèle dehors,
et la carte tombe sous les 10 tokens par seconde.
La falaise, encore.

Bref, 2 gestes tout bêtes : une nouvelle conversation dès que tu changes de sujet,
et une taille de conversation réglée au plus juste dans ton moteur.
Et si tu as vraiment besoin d'une longue conversation, il reste un dernier réglage.

Ce réglage, c'est compresser le cache KV, la mémoire de la conversation.
À ton avis, est-ce que ça fait écrire plus vite ?
Garde ta réponse.

Sur une 5060 Ti, avec un petit modèle de 7 milliards,
l'écriture est 6,6 % plus lente en 8 bits,
et 1,8 % plus lente en 4 bits.
Et sur une machine de Nvidia faite pour l'IA,
en 4 bits, à 64 000 tokens, elle perd même 35 %.
Donc pour la vitesse, il ne sert à rien.

Sauf qu'il fait de la place.
Sur une 3080 de PC portable de 16 gigas, avec Qwen 3.8 27B,
on passe de 32 000 à plus de 128 000 tokens de conversation.
Du coup, il fait tenir beaucoup plus de conversation dans la carte,
avant que le modèle soit poussé dehors.
Il ne t'évite pas le tiers de vitesse en moins,
puisque la mesure du début avait déjà le cache compressé.
Par contre, il peut t'éviter la falaise.

Attention au 4 bits, quand même.
Sur le petit modèle de 7 milliards de tout à l'heure,
la réponse en 8 bits ressemble à 82 % à celle d'origine.
En 4 bits, à 8 % seulement.
Et au moins 3 des 6 mesures du début étaient en 4 bits,
sur un modèle bien plus gros :
ce que ça leur a coûté en qualité, aucune ne le dit.
Du coup, si tout tient en 8 bits chez toi, reste en 8 bits.
Voilà le réglage démystifié : lui, il sert à tenir plus longtemps.

Donc, dans l'ordre : un fichier qui tient dans ta carte,
avec la place du MTP.
Le MTP allumé, surtout pour du code.
Llama.cpp ou LM Studio, plutôt qu'Ollama.
Si ton modèle déborde, règle où vont les experts.
Une conversation neuve quand elle s'allonge.
Le cache en 8 bits si tu manques de place.
Et note ta version.

Alors, ta carte, bridée ?
Si le MTP est éteint, ou si ton fichier déborde, oui.
Et ça se répare ce soir, sans rien acheter.

Et si ta carte n'a que 8 gigas, lundi,
on regarde le nouveau fichier qui fait tenir Qwen 27B en entier dedans.
Allez, salut !
