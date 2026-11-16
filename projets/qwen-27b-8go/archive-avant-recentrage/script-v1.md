# Qwen 27B sur 8 Go : le fichier à essayer, et le compromis à connaître

V1 du 16/11/2026. Sortie prévue le 23/11. Vidéo calculée. Références F1–F15 dans `sources.md`. Durée mesurée : 1423 mots, soit 9 min 49 s à 145 mots/min. Timecodes ci-dessous provisoires, corrigés dans la version finale.

| Partie | Timecode provisoire |
|---|---|
| Résultat et enjeu | 0:00 |
| Plan | 0:30 |
| Le bon fichier, sans jeter l'ancien | 0:45 |
| Les réglages LM Studio | 2:00 |
| Ce que la mesure prouve | 3:30 |
| Le prix de la conversation | 4:35 |
| Le prix de la qualité | 5:45 |
| Verdict par usage | 7:15 |

## Voix

### Résultat et enjeu

[VISUEL : 3,2 → 18 tokens/s. Bandeau permanent : mesure publiée, GTX 1080 Ti limitée à 8 Go, llama.cpp. F2]

Un testeur fait passer Qwen 27B de 3,2 à 18 tokens par seconde en écriture, sur une carte limitée à 8 gigas.
Il change le fichier du modèle.
Ces chiffres sont les leurs, je n'ai rien testé chez moi.
Sauf que le fichier plus petit perd aussi des capacités.
Donc, sur ta carte, tu gagnes un assistant utile ou juste un compteur qui monte ?

### Plan

On va choisir le fichier, repérer les réglages dans LM Studio et décider combien de conversation lui laisser.
Et à la fin, tu sauras pour quel travail je garderais l'ancien, même plus lent.

### Le bon fichier, sans jeter l'ancien

[VISUEL : page du dépôt, nom exact surligné ; aucune simulation présentée comme capture d'essai. F1]

Le fichier à regarder, c'est celui-ci : UD-IQ2_XS, dans le dépôt Unsloth de Qwen 3.8 27B.
La page affiche 7,63 gigas.
Donc vérifie bien le nom complet, pas seulement « Qwen » dans la recherche.
Entre deux fichiers du même modèle, la taille et le résultat peuvent changer.

Mais garde l'ancien téléchargement si tu as la place.
L'idée, c'est de pouvoir revenir en arrière.
Pas de remplacer ton assistant habituel avant de savoir si le nouveau comprend encore ton travail.
Tu lui confies une tâche dont tu connais la réponse, puis tu compares.
Par exemple, expliquer une erreur dans un bout de code que tu as déjà corrigé.
C'est une proposition pour ton essai, pas un résultat que j'aurais obtenu.

En fait, le gros changement, c'est où le modèle travaille.
Dans la mesure publiée, l'ancien fichier reste en partie dans la RAM du PC.
Le nouveau tient entièrement sur la carte. [F2]
Imagine ton inventaire dans un jeu : les objets dont tu as besoin sont enfin à portée de main.
Tu arrêtes les allers-retours au coffre.
L'image explique le principe, elle ne prédit pas la vitesse de ta machine.

Et ça parle à beaucoup de joueurs.
Dans l'enquête Steam d'octobre, plus d'un quart des configurations participantes ont 8 gigas de VRAM. [F8]
Donc avant de condamner ta carte, ça mérite de regarder ce qu'un autre fichier permet.
Sauf que sa taille sur le disque ne suffit pas à savoir si tout va tenir.

### Les réglages LM Studio

[VISUEL : schéma annoté des contrôles documentés. Mention « paramètres documentés ; aucune mesure LM Studio de notre part ». F5–F7]

Dans LM Studio, ouvre la liste de tes modèles, puis la roue dentée du modèle.
On y trouve les réglages de chargement : la part envoyée sur la carte, la longueur de contexte et Flash Attention. [F5]
Le contexte, c'est la place accordée à la conversation en cours.

Le but ici, c'est de charger toutes les couches sur la carte.
Mais si ça ne tient pas, ne force pas pour avoir un joli chiffre dans le menu.
Réduis la place réservée à la conversation et regarde ce que le logiciel annonce au chargement.
Si une partie reste en RAM, tu n'es plus dans la configuration qui produit le résultat du début. [F2, F9]

Du coup, pour démarrer, je propose une conversation courte.
Par exemple un contexte de 4096 tokens, pas un plafond à battre. [F10]
C'est un point de départ prudent, pas une capacité mesurée sur ta carte.
Un token, c'est un morceau de texte : pas forcément un mot entier.
Ta question et la réponse se partagent cette place.

Il y a aussi les réglages de compression du cache K et du cache V.
C'est la mémoire de travail de cette conversation.
Leurs contrôles existent dans LM Studio, et la compression du cache V demande Flash Attention. [F6]
Si ton moteur propose le cache en 8 bits, c'est celui que je regarderais d'abord ; le 4 bits est une concession supplémentaire, pas un bouton magique. [F3, F6, F10]
Les intitulés sont à l'écran, pas besoin de les apprendre comme une combinaison de Monster Hunter.

Enfin, regarde le contrôle de réflexion.
S'il est disponible et relié au modèle, tu peux la désactiver pour commencer avec des demandes simples. [F7, F10]
Par contre, ce bouton dépend de la configuration du modèle.
Je ne vais pas te promettre qu'il apparaît sur tous les fichiers importés.
Et réflexion coupée ne veut pas dire qualité identique.
On revient là-dessus juste après.

### Ce que la mesure prouve

[VISUEL : fiche du protocole ; ancien IQ4_XS partiellement en RAM, nouveau UD-IQ2_XS tout GPU. F2]

Le testeur du début utilise une GTX 1080 Ti.
Il lui bloque une partie de sa mémoire pour se rapprocher du budget d'une carte de 8 gigas.
Donc ce n'est pas une mesure sur une 4060.
Et ce n'est pas non plus une mesure dans LM Studio.

Nous avons retrouvé ses notes, mais pas de deuxième reproduction du nouveau fichier sur une vraie carte de 8 gigas. [F11]
Son résultat est intéressant ; il ne te donne pas ta future vitesse.
La carte, le moteur et la place réellement libre comptent.

Il faut aussi séparer deux attentes.
Lire ta demande, puis écrire la réponse.
Le gain annoncé porte sur l'écriture.
La lecture du prompt reste du même ordre dans son essai. [F2]
Donc ne prends pas une barre qui avance vite pendant le chargement de ton texte pour la vitesse de réponse.
Ce sont deux compteurs différents.

Et quand tu compares chez toi, garde la même demande et une conversation neuve.
Sinon, tu compares aussi deux historiques différents.
C'est comme comparer deux armes avec un bonus actif d'un seul côté : le compteur peut être vrai, la conclusion reste bancale.

### Le prix de la conversation

[VISUEL : jauge conceptuelle « modèle / conversation / travail du moteur / autres applications », sans proportions prétendument mesurées. F3, F9]

Sauf que le modèle ne vit pas seul dans la carte.
Il lui faut aussi de la place pour travailler et pour conserver la conversation.
Le bureau et les autres applications peuvent en prendre.
Donc 7,63 gigas de fichier ne signifie pas que tout le reste rentre automatiquement. [F1, F9]

Dans son essai, le testeur rapporte environ 14000 tokens avec le cache en 8 bits. [F3]
Ne recopie pas ce plafond comme une garantie.
Chez toi, si la place disponible change, la limite peut changer aussi.
Voilà pourquoi je partirais plus bas avant d'allonger la conversation.

Et charger le modèle n'est que le début.
Il faut encore qu'il puisse terminer ta demande quand la conversation se remplit.
Le testeur rapporte justement un plantage en poussant son contexte trop haut. [F3]
Un menu qui accepte un nombre ne te promet pas que toute la session tiendra.

Du coup, si tu changes de sujet, repars dans une conversation neuve.
Garde ailleurs ce que tu veux conserver.
Tu n'as pas besoin de transporter toute l'histoire du royaume pour demander comment réparer une boucle.
Et si ton travail exige un gros historique, ce compromis devient beaucoup moins intéressant.

### Le prix de la qualité

[VISUEL : résultats Unsloth, attribution et conditions visibles ; aucune étiquette « qualité conservée ». F4]

Le plus petit fichier change aussi les réponses.
On réduit la précision des nombres du modèle pour économiser de la place.
Sauf que les conséquences ne sont pas les mêmes selon le travail.

Unsloth publie ses propres évaluations.
Sur certains exercices de code, le petit fichier reste proche du modèle complet.
Sur leur test de travail autonome dans un dépôt de code, il décroche beaucoup plus. [F4]
Donc un assistant qui t'aide à réparer une fonction et un agent qui modifie tout un projet, ce n'est pas la même promesse.

Mais attention à ce que ces scores ne disent pas.
Leurs tests utilisent de grands contextes et des réglages de réflexion qui ne sont pas notre proposition de départ. [F4]
Ils ne prouvent pas que ton petit contexte, réflexion coupée, garde la même qualité.
Et ce sont les mesures de ceux qui produisent le fichier, pas une confirmation indépendante.

Du coup, pour expliquer un passage ou proposer une correction que tu peux relire, je le mettrais dans la liste des fichiers à essayer.
Pas dans celle des assistants auxquels tout déléguer les yeux fermés.
Une réponse rapide que tu dois réparer peut te coûter plus de temps que l'ancienne réponse lente.
Ton objectif, c'est de finir ton travail, pas de farmer les tokens.

### Verdict par usage

Donc, pour discuter ou comprendre un petit morceau de code : essaie le fichier sur une tâche familière, avec une conversation courte.
S'il répond assez bien pour toi et tient sur la carte, le compromis peut valoir le coup.

Pour corriger un fichier : compare avec ton ancien modèle et vérifie le résultat.
La vitesse seule ne tranche pas.

Pour un agent qui doit travailler longtemps dans tout un projet : je garderais un fichier moins compressé, quitte à attendre davantage. [F4, F10]
Ce n'est pas une garantie qu'il réussira ; c'est le compromis que les résultats publiés me donnent envie d'éviter.

[CROCHET : ton avis personnel sur le compromis vitesse/fiabilité, sans raconter un essai que tu n'as pas fait.]

Ta carte de 8 gigas n'est donc pas automatiquement bonne à remplacer.
Mais le fichier ne lui ajoute pas de mémoire.
Tu échanges de la précision et de la place pour la conversation contre une chance de tout faire tenir dessus.
Voilà le choix réel.

Et si ce choix est trop serré pour ton usage, jeudi on regarde quelle carte acheter selon ton budget, avec les prix affichés en France.
Là, on pourra décider si payer davantage t'apporte vraiment la mémoire qu'il te manque. [F15]
Allez, salut !

## Crochets et questions

- Un crochet facultatif d'avis ; le texte tient sans lui.
- Aucun récit personnel inventé.
- Question éditoriale facultative : privilégies-tu une miniature « 8 GO : ÇA RENTRE ? » ou « PLUS VITE, MAIS… » ? Pas de ×5 garanti.
- Avant tournage : capturer les contrôles réellement visibles dans ta version de LM Studio si tu veux des images d'interface plutôt que les schémas documentaires prévus.
