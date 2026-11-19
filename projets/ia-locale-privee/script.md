# Ton IA locale est-elle vraiment privée ?

Version finale après revue indépendante du 16 novembre 2026. Publication : 11 janvier 2027. Base : 145 mots/minute, voix seule, hors indications. V1 conservée.

Voix : **1 596 mots** (hors crochets), **11:00 à 145 mots/minute**. Liaisons strictes : **28**, soit **1,75/100 mots**. Question et disclaimer dans les **55 premiers mots**, soit environ **0:23**. Les repères ci-dessous sont calculés sur la voix, sans ajouter de pauses de montage.

| Partie | Début calculé |
|---|---|
| Cumul et question | 0:00 |
| Document et services externes | 0:42 |
| Accès au serveur | 3:00 |
| Téléchargements et permissions | 5:07 |
| Contenu transmis et copies | 7:16 |
| Profils et règles applicables | 8:48 |

## Voix

[VISUEL : carte du rapport redessinée, « 175 108 hôtes uniques observés en 293 jours, étude publiée en 2026 ». F1.]

Des chercheurs ont observé au total plus de 175 000 hôtes Ollama uniques accessibles sur internet, cumulés sur 293 jours. Des IA qu'on peut pourtant faire tourner chez soi. Donc, quand un outil est présenté comme local, qu'est-ce que ta configuration protège vraiment ?

On va suivre un document : son traitement par le modèle, les outils qui peuvent en recevoir un extrait, puis les copies qui restent. À chaque étape, la question est la même : qui peut accéder à quoi ? La recherche web donne le premier exemple.

[GRAPHIC] [VISUEL : question→modèle téléchargé→réponse, entièrement à l'intérieur du PC. F4/F6.]

Une conversation avec un modèle téléchargé peut rester entièrement sur ton ordinateur. LM Studio le documente pour le chat et les documents traités localement. Ollama indique aussi ne pas voir les prompts quand tu utilises un modèle local. Donc oui, il y a un vrai bénéfice à garder le calcul et les données chez toi.

Sauf que le programme qui calcule la réponse n'est qu'une partie de l'ensemble. Autour, tu peux avoir une interface, une recherche web, des extensions, un serveur et des sauvegardes. Chacun de ces éléments peut changer le trajet d'une information.

Prenons un document de travail que tu veux résumer. Le modèle peut lire son contenu sur le PC et y écrire sa réponse. Par contre, si un outil transmet ensuite un extrait, la copie locale reste sur le disque et une information a obtenu un autre trajet. La présence du fichier chez toi ne décrit donc plus toutes ses copies.

Du coup, avant de coller un document sensible, la première question est très concrète : quel modèle traite cette demande ? Une interface capable de lancer un modèle local peut aussi proposer un modèle distant. Le bouton et le nom affichés comptent davantage que la couleur du logo de l'application.

En fait, la politique de LM Studio distingue ces cas. Pour les modèles locaux, l'éditeur dit que les conversations et documents restent sur l'appareil. Pour des services cloud facultatifs, comme un modèle distant ou la recherche web, les requêtes choisies passent par un traitement externe. L'éditeur annonce des conditions de non-conservation. Cela décrit ce qui arrive après le traitement ; l'information a quand même dû être transmise pour que le service fonctionne.

Donc une règle de non-conservation décrit ce qui reste chez le service après l'opération. Elle ne supprime pas le trajet nécessaire à cette opération. Et le logiciel peut se connecter pour chercher un modèle ou vérifier une mise à jour sans envoyer le contenu de tous tes chats. On doit distinguer ces trajets pour juger ce qu'il fait réellement.

[VISUEL : PC seul, puis porte vers réseau local, puis internet ; aucune commande d'ouverture montrée. F1–F3.]

Sauf qu'une autre question se pose : qui peut envoyer des demandes à ton serveur ? Ollama écoute par défaut sur l'adresse locale de la machine. Son API locale ne demande pas d'authentification. Ces deux choix vont ensemble : l'accès est prévu pour les programmes de ton ordinateur.

Par contre, si une configuration rend ce service accessible plus largement, le périmètre change. Le réseau de la maison, un hébergement et une adresse publique ne représentent pas le même accès. Il faut alors une protection adaptée, avec des utilisateurs autorisés et un accès réseau maîtrisé.

C'est le contexte des rapports d'exposition. Le chiffre du début compte des hôtes observés au fil des jours. Il ne signifie pas que tous étaient accessibles simultanément, ni que chacun a subi une intrusion. Et il ne permet pas d'affirmer que 175 mille personnes ont perdu leurs conversations.

Une étude antérieure de Censys avait déjà identifié des milliers de services accessibles. Par contre, elle employait une autre période et une autre méthode. Donc on ne divise pas les deux nombres pour annoncer une explosion précise du risque. Ce qu'on retient, c'est l'existence répétée de configurations publiquement accessibles.

Du coup, l'exposition du service et les capacités du modèle doivent rester distinctes. Un modèle sachant produire un appel d'outil ne contrôle pas forcément le terminal du serveur. Il faut qu'une application lui donne réellement cet outil et les permissions associées. La capacité du modèle et les droits d'un agent sont deux lignes distinctes de la configuration.

En fait, le problème pratique est simple : une porte qu'on ajoute pour le confort doit correspondre au public qu'on veut laisser entrer. Si tu utilises ton IA uniquement sur ton PC, tu n'as pas besoin d'une ouverture sur internet. Si tu veux y accéder à distance, l'authentification et le contrôle d'accès font partie de cette décision.

[GRAPHIC] [VISUEL : boîtes « poids », « logiciel », « outils », séparées. F7/F8.]

Ton document peut rester sur le PC, avec un serveur fermé à l'extérieur. Sauf que le logiciel téléchargé pour le traiter demande encore de l'attention. Un fichier de modèle peut contenir des poids dans différents formats. Certains formats de sérialisation, comme Pickle, peuvent faire exécuter du code lors du chargement. Hugging Face documente ce risque et recommande des sources de confiance.

Safetensors a été conçu pour stocker les tenseurs sans ces mécanismes de Pickle. C'est un avantage précis. Par contre, un format ne certifie pas tout ce que tu installes autour : le moteur, un script d'installation ou un outil ajouté restent du logiciel.

Donc regarde la provenance du dépôt et les fichiers réellement nécessaires. Une page connue pour publier les poids du modèle n'est pas la même chose qu'un lien raccourci vers un installateur inconnu. Et le nombre de téléchargements ne te donne pas à lui seul l'identité de la personne qui a préparé le paquet.

En fait, la même logique vaut pour les extensions qui pourront recevoir ton document. LM Studio permet d'ajouter des serveurs MCP, c'est-à-dire des outils que le modèle peut utiliser. Sa documentation précise que certains peuvent accéder aux fichiers, utiliser le réseau ou exécuter du code. Du coup, installer un outil mérite la même attention qu'installer une autre application.

Imagine que tu donnes à ton assistant la clé d'un dossier de travail. Il peut maintenant lire ce dossier pour t'aider. Si tu lui donnes l'accès à tout le disque alors qu'il doit résumer un seul fichier, tu as élargi le périmètre sans ajouter forcément de service utile.

L'assistant a donc besoin du dossier utile à sa tâche. Pour résumer un fichier, cet accès peut suffire ; pour en modifier un autre, il lui faudra une permission supplémentaire. Chaque droit ajouté élargit ce qu'il peut lire ou changer. Une validation des actions importantes peut compléter ces limites.

[VISUEL : document confidentiel → requête web → service externe ; extrait transmis clairement marqué. F5/F7.]

Reste le contenu exact de la recherche web évoquée au début. Un mot général, le nom d'un client ou une phrase du document ne transmettent pas la même information. Du coup, le choix de l'outil et les éléments qu'il reçoit changent la confidentialité de cette étape, même si le modèle qui écrit la réponse reste local.

Imagine que la demande porte sur une règle générale mentionnée dans le document. Le service distant peut recevoir seulement le thème de cette règle, ou bien un extrait accompagné du nom du client. Donc deux recherches utiles pour la même réponse peuvent exposer des informations très différentes. Le schéma doit montrer l'extrait qui voyage.

Par contre, travailler hors ligne ne supprime pas les fichiers produits. L'historique peut rester enregistré sur le PC. Une exportation peut se retrouver dans un dossier synchronisé. Un journal peut contenir du contexte ajouté pour diagnostiquer un problème. La bonne question devient : qui peut lire ces copies et combien de temps tu souhaites les garder ?

En fait, un ordinateur partagé demande aussi de penser aux comptes utilisateurs et à l'accès aux documents. La confidentialité vis-à-vis d'un fournisseur cloud et celle vis-à-vis de quelqu'un qui utilise ton ordinateur ne se règlent pas avec le même bouton.

Si ces trajets de données t'ont évité un partage que tu ne voulais pas, abonne-toi.

[GRAPHIC] [VISUEL : trajet du document, 2 profils « personnel » / « organisation ». F9/F10.]

Par contre, pour une organisation qui traite des données personnelles, le fait de rester sur site ne donne pas automatiquement une conformité au RGPD. La CNIL explique que ce déploiement peut limiter l'exposition à un tiers. Elle rappelle aussi les responsabilités de sécurité et d'encadrement des usages.

Donc une petite entreprise peut bénéficier du local sans considérer que tout devient autorisé. Il faut encore savoir quelles données on utilise, pour quel besoin, avec quels accès et quelles règles de conservation. Les obligations dépendent du traitement ; le mot local ne les efface pas.

Pour ton usage personnel, le schéma garde donc quatre questions : quel modèle reçoit le document, quels outils peuvent en transmettre un extrait, qui accède au serveur et qui retrouve les copies ? Les mises à jour, les dépôts et les permissions complètent ce trajet. On peut les relier au même fichier au lieu de traiter chaque réglage comme une garantie générale.

Sauf que la décision ne s'arrête pas à la réponse affichée. Un document dont tu n'as plus besoin peut rester dans un historique ou une sauvegarde, selon l'application. La durée de conservation et l'accès à ces copies font donc partie de la confidentialité. Garder les données chez toi implique aussi d'entretenir les programmes qui les manipulent.

Tu veux simplement poser des questions personnelles hors ligne ? Un modèle téléchargé, sans outil externe nécessaire, peut répondre à ce besoin. Tu veux un agent qui navigue, lit et modifie tes fichiers ? Son intérêt peut être grand, et ses permissions méritent d'être définies. Tu gères des documents professionnels ? Ajoute les règles de ton organisation et le cadre applicable.

[CROCHET : ton avis sur les données que tu préfères garder chez toi. Facultatif.]

Ton document peut rester sur ton PC, et tu sais maintenant quelles fonctions peuvent lui donner un autre trajet. Dans la prochaine vidéo, on regarde ce qu'une IA locale peut réellement construire dans un jeu : le résultat produit, avec les limites de ce qu'il prouve. Allez, salut !

## Hors voix

Sources F1–F10. Un document sert de fil aux trajets : traitement, outil, réseau, copies. Le cumul ne compte pas des conversations volées. Documentation d’éditeur distincte d’un audit indépendant. Aucun scan, intrusion, ouverture de port ou audit personnel requis. Le renvoi final mène au jeu vidéo du 14 janvier.
