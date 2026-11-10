# Téléprompteur : 16 Go de VRAM suffisent (si tu prends le bon fichier) (V3, 08/11)

> Une ligne = un souffle. Ligne vide = respiration. Les [MARQUEURS], ⟦à écrire⟧ et (indications) ne se lisent pas.
> Tiré du [script](script.md) V3 du 08/11, avec tes réponses du 08/11 (contexte 64K puis 100K, ton choix final, panneau de droite). Plus aucun ⟦…⟧ : tout est à lire. Prix de la RAM revérifié le 08/11 (560 €).
> Environ 2 000 mots, environ 13 min 50 à 145 mots/min. Le hook vise 35 s au maximum : chronomètre-le.

## Hook

(rapide, sur le chiffre)  
Sur une RTX 5080, seize gigas,  
quelqu'un fait tourner Qwen,  
un vrai modèle de vingt-sept milliards,  
à cent un tokens par seconde.  
Plus vite que tu lis.  

Un autre, même carte, même modèle :  
treize.  
Huit fois moins.  
(plus bas)  
Et chez moi, ce Qwen-là m'a paru super lent.  

Du coup, seize gigas, ça suffit ou pas ?  

Entre cent un et treize,  
la grosse différence, c'est le fichier :  
un qui rentre, un qui déborde.  

Alors on fait les comptes de ta carte,  
et à la fin, je te dis ce qui clochait chez moi.  

## Les comptes de ta carte

(posé)  
Vois ta carte comme un budget.  
Trois choses se le partagent :  
le fichier du modèle,  
la mémoire de la conversation,  
et l'agent, si tu codes avec.  

[LIGNE 1 : LE FICHIER]

Le même modèle existe en plusieurs fichiers.  
En gros, c'est le JPEG de l'IA :  
on garde moins de bits par paramètre,  
le fichier devient plus léger,  
et on perd un peu de qualité.  
On appelle ça la quantization.  

Et là, premier piège : les gigas.  
Ta carte de seize gigas, en vrai,  
c'est dix-sept virgule deux milliards d'octets,  
parce qu'en mémoire, on compte par paquets de mille vingt-quatre.  
Les sites où tu télécharges les modèles, eux,  
comptent en milliards tout ronds.  
Donc un fichier de seize gigas et demi,  
sur le papier, il rentre.  
Sauf que Windows se sert aussi sur ta carte,  
pour afficher ton écran :  
compte environ un giga.  

Résultat : le Q4 K M,  
le quatre bits qu'on te propose le plus souvent,  
fait entre seize et demi et dix-neuf gigas,  
selon qui le publie.  
Il passe pas,  
avant même que t'aies tapé un mot.  

Il existe des quatre bits plus serrés, vers quatorze gigas :  
c'est celui que j'avais pris.  
On en reparle à la fin.  

Et en trois bits, un fichier soigné fait douze gigas,  
petit module d'accélération compris.  
Là, il te reste environ quatre gigas,  
un peu moins une fois que le moteur s'est servi.  
Et ces quatre gigas, il faut les partager.  

[LIGNE 2 : LA CONVERSATION]

Chaque token que le modèle garde en tête  
prend de la place dans ta carte.  
Et pour Qwen, on peut le calculer :  
sur ses soixante-quatre couches,  
seules seize gardent vraiment la mémoire de la conversation.  
Fais la multiplication,  
et ça donne soixante-quatre kilo-octets par token.  

Ça a l'air de rien.  
Sauf que huit mille tokens,  
la valeur par défaut de LM Studio,  
c'est déjà un demi-giga.  
Et cent vingt-huit mille, c'est huit gigas :  
plus que tout ce qui reste.  

Avec nos quatre gigas,  
tu tiens environ soixante mille tokens.  
Et si tu passes cette mémoire en huit bits,  
un réglage du moteur,  
tu tiens presque le double.  

[LIGNE 3 : L'AGENT]

Et la troisième ligne,  
c'est celle que tout le monde oublie : l'agent.  
Un agent de code comme Claude Code,  
avant même ta première question,  
il envoie ses consignes et la liste de tous ses outils.  
Un utilisateur a relevé  
plus de cinquante mille tokens au compteur,  
avant d'avoir tapé quoi que ce soit.  
Sur notre Qwen, ça fait plus de trois gigas.  
(sourire)  
En fait, c'est le jeu qui te réclame un patch de trois gigas  
avant même l'écran titre.  

Donc si tu branches un agent sur ta carte,  
voilà les comptes :  
avec la mémoire en version normale,  
il te reste à peine dix mille tokens pour ton vrai travail.  
Avec la mémoire en huit bits,  
plus de soixante-dix mille.  
Ça passe,  
mais seulement si tu règles ta carte.  

## Ça va vite comment ?

Bon, ça rentre.  
Mais ça va vite comment ?  

Pour écrire un seul token,  
la carte doit relire tout le modèle.  
Donc la vitesse max, c'est simple :  
la vitesse de la mémoire,  
divisée par la taille du fichier.  
Une 5080, c'est neuf cent soixante gigas par seconde.  
Avec un fichier de douze gigas,  
ton plafond tourne autour de quatre-vingts tokens par seconde.  

En vrai, on l'atteint jamais tout à fait.  
Quelqu'un avec une 5060 Ti  
a pris un fichier quatre bits de quatorze gigas,  
exactement celui que j'avais chez moi,  
et il mesure vingt-cinq tokens par seconde,  
pour un plafond de trente et un.  
Environ quatre-vingts pour cent.  
(appuyé)  
Garde ce chiffre dans un coin, il va servir.  

Et le cent un du début ?  
Sans réglage,  
la personne qui l'a publié mesure cinquante-trois.  
Puis elle active le MTP,  
le petit module d'accélération dont je te parlais :  
le modèle devine plusieurs mots d'avance,  
et la carte les vérifie d'un seul coup.  
Résultat : cent un.  
Par contre, c'est une seule mesure.  

Et maintenant, le treize.  
Quand le fichier rentre pas,  
une partie part dans ta RAM.  
Et la RAM, même en DDR5 six mille comme la mienne,  
c'est environ quatre-vingt-seize gigas par seconde :  
dix fois moins que la carte.  
Et là, la règle est brutale :  
c'est la mémoire la plus lente qui donne le rythme.  

Dans une vidéo espagnole,  
un utilisateur charge un modèle quatre bits dans LM Studio,  
sur sa 5080.  
Ça rentre pas,  
il laisse une partie des couches en RAM,  
et il le dit lui-même :  
treize tokens par seconde,  
parce qu'une partie du modèle est dans la RAM.  
Ce sont pas les mêmes réglages que pour le cent un,  
donc je compare pas au chiffre près.  

Sur une seule carte, une 5060 Ti,  
quelqu'un a vécu les deux.  
Avec la version précédente de Qwen,  
son fichier débordait de trois gigas :  
huit ou neuf tokens par seconde.  
Avec un fichier du Qwen actuel qui tient dans la carte :  
vingt-six.  
Trois fois plus vite.  
Et sa conclusion, en gros :  
un fichier qui tient vaut plus que le MTP.  

Au passage, ça vaut aussi pour AMD.  
Regarde la vitesse de la mémoire,  
pas seulement les gigas sur la boîte.  
Avec le même fichier,  
une RX 9070 XT a un plafond deux fois plus haut  
qu'une 9060 XT.  
Seize gigas toutes les deux.  
Et la 5080, encore au-dessus.  

Et si t'as pas seize gigas ?  
T'es loin d'être seul :  
sur Steam, en octobre,  
plus d'un joueur sur quatre a une carte de huit gigas,  
et un sur huit en a douze.  
En douze, le vingt-sept B rentre en trois bits,  
avec un fichier de dix gigas,  
mais il te reste à peine vingt-sept mille tokens :  
une conversation, oui ;  
un agent de code lourd, non.  
En huit, il rentre pas :  
tu tombes dans le cas du treize, en pire.  

Et ta RAM, dans tout ça ?  
Pour ce modèle, elle sert presque à rien :  
tout se joue dans la carte.  
(appuyé)  
Retiens ça,  
parce qu'avec le modèle suivant, ça s'inverse.  

## Plus gros : là, c'est ta RAM qui décide

Parce qu'il existe un autre Qwen, bien plus gros :  
Flash-Next,  
cent vingt-cinq milliards de paramètres.  
En fait, il est découpé en centaines de petits spécialistes,  
des experts,  
et à chaque mot, il n'en réveille que quelques-uns :  
environ six milliards au travail.  
Et un projet open source sorti fin septembre, Strata,  
le fait tourner sur un PC de joueur.  

Son astuce :  
les experts qui servent le plus restent dans la carte,  
les autres vont dans la RAM,  
et une grosse table reste sur le SSD.  
Sauf que du coup, tout s'inverse :  
la doc de Strata le dit,  
ta RAM doit contenir les experts,  
plus environ dix gigas pour Windows et le reste.  

Fais le calcul avec moi.  
Le plus petit fichier du modèle complet,  
c'est trente-quatre gigas d'experts.  
Plus dix : quarante-quatre.  
Et moi, j'ai trente-deux gigas de RAM :  
c'est non.  

Mais la doc a une réponse pour trente-deux gigas :  
prends le Coder,  
une version réduite pour le code,  
qui garde la moitié des experts.  
Vingt-trois gigas, plus dix : trente-trois.  
Et Windows t'en laisse voir environ trente-trois et demi.  
Ça passe, mais à ras, navigateur fermé.  
Et ça, c'est un calcul.  

Sauf qu'un utilisateur l'a mesuré,  
avec presque ma config :  
le même processeur,  
une 5070 Ti de seize gigas,  
trente et un gigas de RAM visibles.  
Soixante-dix tokens par seconde.  
Un modèle de cent vingt-cinq milliards,  
à cette vitesse,  
sur un PC de joueur.  
(plus bas)  
Mais en tête de son rapport, la personne l'écrit elle-même :  
vitesse seulement, aucun test de justesse.  

Et il y a un prix.  
Ses auteurs annoncent quatre-vingt-quinze pour cent  
du score de code du modèle complet,  
mais c'est leur chiffre.  
Sur un forum de développeurs,  
quelqu'un sent, en substance, une vraie perte.  
Dans un test publié en vidéo, sur une 5090,  
le Coder a pas réussi à finir sa tâche avec Claude Code.  
Et d'après la doc, il est plus faible  
hors de l'anglais, du chinois, du japonais et du coréen.  
Le français en fait partie.  

Et si tu te dis « bah, je rajoute de la RAM » :  
mes trente-deux gigas,  
je les ai payés quatre-vingt-treize euros  
en deux mille vingt-cinq.  
Le même kit, aujourd'hui :  
cinq cent soixante euros.  
Six fois le prix, pour les mêmes barrettes.  

Bref, sur le papier, le Coder tient chez moi.  
Alors la semaine prochaine,  
je le lance pour de vrai sur ma 5080,  
et on regarde ce qu'il vaut.  

Mais admettons que ça tourne chez toi.  
Est-ce que ça vaut ton abonnement ?  

## Et Claude, dans tout ça ?

Sur les tableaux publiés par Qwen,  
le vingt-sept B bat l'ancien Opus quatre point six  
en code sur un test,  
et il perd sur un autre.  
Mais c'est leur tableau, avec le modèle complet :  
c'est pas le fichier trois bits qui tient dans ta carte.  

Un classement indépendant, lui,  
compare ce même vingt-sept B à Claude Opus cinq,  
en agent dans un terminal :  
six pour cent de réussite,  
contre quarante-six.  
(pause)  
Ouais, t'as bien entendu.  
Six.  
Donc pour coder en agent sur un vrai projet,  
Claude est loin devant.  

Du coup, voilà comment je le lis.  
Ton modèle de seize gigas, c'est un très bon plan B :  
tes données restent chez toi,  
il marche sans internet,  
et t'as rien à payer chaque mois.  
Pour le code sérieux en agent,  
l'abonnement garde l'avantage.  
(sourire)  
Et en plus, chez Claude,  
le patch de trois gigas, c'est pas ta carte qui le paie.  

## Ce qui clochait chez moi, et le verdict

(on ralentit, ton d'enquête)  
Et mon Qwen qui me paraissait super lent, alors ?  
J'avais pris le fichier quatre bits de quatorze gigas.  
Souviens-toi :  
la 5060 Ti en tire vingt-cinq tokens par seconde,  
et ma carte a deux fois plus de bande passante.  
D'après le calcul,  
le mien aurait dû tourner autour de cinquante.  
Donc c'était pas la carte.  
Il reste deux suspects.  

Le premier, je suis sûr qu'il était là :  
par défaut, ce Qwen réfléchit au niveau maximum  
avant de répondre.  
Un développeur a compté  
plus de vingt-deux mille tokens de réflexion  
pour une seule demande :  
dessiner un pélican.  
Même à cinquante tokens par seconde,  
ça fait plus de sept minutes  
avant la première ligne utile.  
Ce niveau de réflexion,  
tu peux le baisser dans le panneau de droite de LM Studio.  

(un temps)  
Le deuxième suspect, c'est moi.  
Avec quatorze gigas de fichier,  
une fois l'écran servi,  
il me restait moins de deux gigas pour la conversation.  
Et j'avais monté la conversation à soixante-quatre mille tokens,  
puis à cent mille.  
Reprends la ligne deux de la facture :  
soixante-quatre mille tokens, c'est plus de quatre gigas.  
Cent mille, plus de six.  
Il me manquait donc entre deux et quatre gigas et demi.  

Et quand ta carte est pleine,  
le pilote NVIDIA déborde en silence dans ta RAM,  
au lieu de planter.  
Ça marche, mais beaucoup plus lentement :  
NVIDIA le dit lui-même, et LM Studio aussi.  
En gros, d'après le calcul,  
j'avais recréé le treize du début,  
tout seul.  

Pour le savoir chez toi :  
Gestionnaire des tâches, Performances, GPU,  
et tu regardes la mémoire GPU partagée  
pendant que le modèle écrit.  
Si elle grimpe, t'as ton coupable.  
Et dans le panneau NVIDIA,  
un réglage interdit ce débordement :  
le modèle plante au lieu de ramer,  
mais au moins, tu sais.  

Bref, ma carte était pas en cause :  
c'était ce que je lui demandais.  

(net)  
Donc oui, seize gigas suffisent :  
pour un vrai modèle de vingt-sept milliards,  
si tu prends le fichier qui rentre,  
et que tu laisses de la place à la conversation et à l'agent.  
Pour aller plus gros,  
c'est ta RAM qui décide, plus la carte.  
Et pour le code en agent,  
Claude reste devant.  

Moi, je garde ma config :  
les moteurs sont de plus en plus performants.  
Par contre, je vais passer de LM Studio  
à llama point cpp, ou à Strata.  

Si t'as jamais installé d'IA chez toi,  
j'ai une vidéo qui le fait pas à pas :  
je te la mets là.  

Et la semaine prochaine,  
Strata, en vrai, sur ma carte.  
En attendant, dis-moi en commentaire ta carte et ta RAM,  
et je te dis ce qui tient chez toi.  
