TÉLÉPROMPTEUR — Même carte, 2 fois plus rapide (V2, 15/11 : un testeur dès la première phrase, le plan avant les conditions)
Une ligne = un souffle. Ligne vide = respiration. Les [MARQUEURS] et les (indications) ne se lisent pas.
Les nombres sont écrits en chiffres pour la lecture, mais tu les dis en entier.
4 crochets sont à toi : remplis-les avec tes mots, ou saute-les. Le texte tient sans eux.
Aucun chiffre n'est à toi : ce sont les mesures d'autres testeurs.

[ HOOK ]

(le compteur de la miniature : l'aiguille file de 29 à 64)

Sur une carte de 16 gigas, un testeur allume un seul réglage,
et son IA écrit 2 fois plus vite :
de 29 à 64 tokens par seconde.
Même fichier, et rien acheté.

Et ils sont 6 testeurs, sur 5 modèles de cartes de 16 gigas,
à trouver entre 1,9 et 2,3 fois plus vite.
Du coup, ta carte, elle serait pas bridée,
sans que tu le saches ?

[ LE PLAN ]

Je vais te montrer ce réglage, celui à faire avant lui,
le moteur qui peut te coûter jusqu'à 30 %,
et le piège qui te vole un tiers de ta vitesse.
Et à la fin, le réglage qui ne fait rien pour la vitesse,
et pourquoi le connaître quand même.

Ces chiffres sont les leurs : je n'ai rien testé chez moi.
Et c'est l'écriture, sur Qwen 3.8 27B,
un modèle qui tient en entier dans la carte.

[ LE MTP ]

Ce réglage, c'est le MTP,
le petit module dont je te parlais dans la vidéo sur les 16 gigas.
En gros, c'est comme les suggestions du clavier de ton téléphone :
le modèle propose plusieurs tokens d'avance,
puis il les vérifie tous d'un coup.
Et quand il a deviné juste, il en écrit plusieurs pour le prix d'un.

Par contre, ça ne joue que sur l'écriture.
La lecture de ton prompt, elle,
ralentissait avec le MTP dans les premiers tests de mai.

Et le 101 tokens par seconde de cette vidéo-là, c'était déjà lui :
sur une 5080, 53 sans le MTP, 101 avec.
Je te disais alors : une seule mesure.
Depuis, j'en ai trouvé 5 autres.
Sur une 4060 Ti, de 17,6 à 40.
Et même chez AMD, sur une RX 9060 XT, de 15 à presque 29.
Donc même la Radeon double presque.

Sauf que 5 de ces 6 mesures viennent du même tableau en ligne,
avec le même script de test.
Du coup, la plus solide, c'est celle du début :
le testeur à 29 et 64 a tout mesuré de son côté, 5 fois.
Et il trouve pareil.

En fait, ce « 2 fois », c'est une moyenne,
sur du code, du texte et des commandes, avec la réflexion coupée.
Sur du texte seul, ça tombe à 1,8 fois sur la 4060 Ti.
C'est sur du code que ça gagne le plus.
Et sur un modèle à experts, un testeur ne mesure que 1,5 fois.

Alors, pourquoi je dis « bridée » ?
Parce que dans llama.cpp, le MTP ne s'allume pas tout seul.
Il faut le demander,
et il faut un fichier qui contient le module, un petit bout de modèle en plus.
LM Studio, lui, le gère depuis la version 0.4.22.

[CROCHET : dans LM Studio 0.4.28, où s'allume le MTP, et s'il est allumé par défaut. Avec tes mots. Si tu n'as pas vérifié, saute.]

Donc va vérifier qu'il est bien allumé chez toi.

[ LE FICHIER QUI TIENT ]

Sauf que le MTP a un prix : il prend de la place.
Selon les testeurs, entre 1 et 2,5 gigas de VRAM en plus.
Et sur une carte de 16, c'est justement là que ça coince.

Donc le vrai réglage numéro un,
c'est que le modèle tienne en entier dans la carte.
Sur une 4080 de 16 gigas, avec un Qwen de 27 milliards plus ancien :
un fichier de 15 gigas qui déborde un peu, 20 tokens par seconde.
Un fichier de 11,5 gigas qui tient, 45.
Plus du double, juste en prenant un fichier plus petit.

Et si une partie du modèle sort de la carte, c'est la chute.
Sur une 5060 Ti, un testeur a laissé dehors exprès
8 couches sur 48 d'un modèle plus petit :
on tombe de 43 à 12,5.
En fait, la partie restée en RAM va beaucoup plus lentement,
et la carte l'attend.

C'est ce que je te disais dans la vidéo sur les 16 gigas :
prends le bon fichier.
Par contre, un fichier plus petit est plus compressé,
et aucun de ces testeurs ne mesure ce que tu perds en qualité.

Sauf que ces 2 gains ne s'additionnent pas.
Si le MTP fait déborder ton fichier,
la chute mange ce qu'il te fait gagner.
Du coup, d'abord un fichier qui tient avec la place du MTP,
ensuite le MTP.

Bon, rien qu'avec ces 2 réglages,
ton modèle peut écrire jusqu'à 2 fois plus vite,
sur la carte que tu as déjà.
Donc avant d'en racheter une plus grosse, essaie ça.
Si cette vidéo t'a évité un mauvais achat, abonne-toi.

[CROCHET : si tu veux, une phrase à toi sur ces 2 premiers réglages, ou celui que tu essaierais en premier.]

[ LE MOTEUR ]

Mais tout ça dépend aussi du moteur,
le programme qui fait tourner le modèle.
Quand tout tient dans la carte,
un testeur a mesuré Ollama 10 % plus lent que llama.cpp,
sur une 5060 Ti.
Un autre, jusqu'à 30 % plus lent, sur une 3090.
Et LM Studio était presque à égalité avec llama.cpp :
76,8 contre 77.
Du coup, si tu l'as installé avec ma vidéo sur LM Studio,
de ce côté-là, t'es tranquille.

Et même une mise à jour peut te ralentir.
Sur une 5080 avec Strata, le moteur de ma vidéo de lundi,
un utilisateur a perdu 25 % en passant à une version plus récente du moteur.
Et la 0.2.14, celle d'après la mienne, sortie le 15 novembre,
lit ton prompt plus vite,
mais écrit environ 10 % moins vite sur une 5070 Ti,
d'après le projet lui-même.
Voilà pourquoi je te disais lundi de bien noter ta version.
Celles du 15 novembre sont à l'écran.

[ LE MODÈLE QUI DÉBORDE ]

Et si ton modèle est trop gros pour la carte, comme celui de lundi ?
Lundi, tu as vu ma RAM pleine, et le disque qui se met à lire.
Sur ce modèle-là, en entier,
une chaîne française vient de passer de 8 à 83 tokens par seconde
sur une 5060 Ti, surtout en changeant de moteur.

Sauf que son dernier moteur ne marche que sur les cartes RTX 50, sous Linux,
et il ne donne ni ses versions ni ses réglages exacts.
Donc ça a marché sur sa machine,
et je ne peux pas te le promettre sur la tienne.

Mais dans llama.cpp, il y a un réglage à toi :
où vont les experts, ces petits spécialistes du modèle.
Lesquels restent sur la carte, et lesquels partent en RAM.
Le bon réglage, c'est d'en garder sur la carte autant que possible,
juste avant que ça plante.
Sur une 3060 de 12 gigas, ça a fait gagner 12 %.
Sur une 5060 Ti de 16, avec le cache d'experts arrivé dans llama.cpp en octobre,
29 %.
Une seule mesure chacune, donc à prendre avec des pincettes.
Et leurs PC avaient 32 et 64 gigas de RAM.

[ LE PIÈGE ]

Maintenant, le piège.
Plus ta conversation est longue, plus ça ralentit.
Tu te rappelles le testeur du début, à 29 tokens par seconde ?
À 64 000 tokens de conversation, il tombe à 20.
Donc un tiers de vitesse en moins.
Et avec le MTP, ses 64 deviennent 39.
Le MTP double toujours, mais tout descend.
C'est ce que je te disais lundi :
la vitesse baisse quand la conversation grandit.

Et ça peut être bien pire.
En fait, la mémoire de la conversation se range aussi dans la carte.
Tu te rappelles la 4080 qui montait à 45 avec le petit fichier ?
À 128 000 tokens de conversation,
cette mémoire pousse le modèle dehors,
et la carte tombe sous les 10 tokens par seconde.
La falaise, encore.

Bref, 2 gestes tout bêtes :
une nouvelle conversation dès que tu changes de sujet,
et une taille de conversation réglée au plus juste dans ton moteur.
Et si tu as vraiment besoin d'une longue conversation,
il reste un dernier réglage.

[ LE RÉGLAGE QUI NE SERT À RIEN POUR LA VITESSE ]

Ce réglage, c'est compresser le cache KV,
la mémoire de la conversation.
À ton avis, est-ce que ça fait écrire plus vite ?
Garde ta réponse.

(1 seconde de silence)

Sur une 5060 Ti, avec un petit modèle de 7 milliards,
l'écriture est 6,6 % plus lente en 8 bits,
et 1,8 % plus lente en 4 bits.
Et sur une machine de Nvidia faite pour l'IA,
en 4 bits, à 64 000 tokens, elle perd même 35 %.
Donc pour la vitesse, il ne sert à rien.

Sauf qu'il fait de la place.
Un testeur passe de 32 000 à plus de 128 000 tokens de conversation,
sur la même carte.
Du coup, il fait tenir beaucoup plus de conversation dans la carte,
avant que le modèle soit poussé dehors.
Il ne t'évite pas le tiers de vitesse en moins,
puisque le testeur du début avait déjà son cache compressé.
Par contre, il peut t'éviter la falaise.

Attention au 4 bits, quand même.
Dans le même test, la réponse en 8 bits ressemble à 82 % à celle d'origine.
En 4 bits, à 8 % seulement.
Et au moins 3 des 6 testeurs du début étaient en 4 bits.
Du coup, si tout tient en 8 bits chez toi, reste en 8 bits.

[CROCHET : ta réaction à ce retournement, avec tes mots. Tu ne l'as pas testé : ne raconte pas d'essai.]

[ LA LISTE, ET LA RÉPONSE ]

Donc, dans l'ordre :
un fichier qui tient dans ta carte, avec la place du MTP.
Le MTP allumé, surtout pour du code.
Llama.cpp ou LM Studio, plutôt qu'Ollama.
Si ton modèle déborde, règle où vont les experts.
Une conversation neuve quand elle s'allonge.
Le cache en 8 bits si tu manques de place.
Et note ta version.

Alors, ta carte, bridée ?
Si le MTP est éteint, ou si ton fichier déborde, oui.
Et ça se répare ce soir, sans rien acheter.

[CROCHET : ton verdict en 1 ou 2 phrases : ce que tu retiens, ou ce que tu vas régler toi-même.]

Et si ta carte n'a que 8 gigas,
lundi, on regarde le nouveau fichier
qui fait tenir Qwen 27B en entier dedans.
Allez, salut !
