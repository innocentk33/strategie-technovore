# Ton IA locale est-elle vraiment privée ?

V1 documentaire · 11 janvier 2027 · cible 10–12 min à 145 mots/minute. Rapports et documentations relus le 16/11/2026. Aucun audit personnel ni essai d'intrusion.

| Partie | Repère |
|---|---|
| Des serveurs locaux accessibles en ligne | 0:00 |
| Le trajet réel de ta question | 0:30 |
| Les portes réseau | 2:10 |
| Modèles et outils téléchargés | 4:10 |
| Ce qui reste sur le PC | 6:30 |
| Checklist et verdict | 8:30 |

## Voix

[VISUEL : carte du rapport redessinée, « 175 108 hôtes uniques observés en 293 jours, étude publiée en 2026 ». F1.]

Des chercheurs ont observé plus de 175 mille serveurs Ollama accessibles sur internet, sur une période de 293 jours. Des IA qu'on peut pourtant faire tourner chez soi. Ces chiffres sont les leurs, je n'ai rien testé chez moi. Donc, quand tu écris « c'est local, rien ne sort », qu'est-ce que ta configuration protège vraiment ?

On va suivre le trajet d'une question, repérer les ouvertures réseau, puis regarder les modèles et les outils qu'on installe autour. À la fin, tu auras une checklist pour garder la main sur tes documents. Et le point le plus trompeur arrive avec une fonction qui peut sembler toute simple : la recherche sur le web.

[GRAPHIC] [VISUEL : question→modèle téléchargé→réponse, entièrement à l'intérieur du PC. F4/F6.]

Une conversation avec un modèle téléchargé peut rester entièrement sur ton ordinateur. LM Studio le documente pour le chat et les documents traités localement. Ollama indique aussi ne pas voir les prompts quand tu utilises un modèle local. Donc oui, il y a un vrai bénéfice à garder le calcul et les données chez toi.

Sauf que le programme qui calcule la réponse n'est qu'une partie de l'ensemble. Autour, tu peux avoir une interface, une recherche web, des extensions, un serveur et des sauvegardes. Chacun de ces éléments peut changer le trajet d'une information.

Imagine ton document comme une sauvegarde de jeu. Tu peux la garder sur ton disque. Si tu actives ensuite une synchronisation, elle obtient un autre trajet. Le fichier est toujours sur ta machine, mais cette seule phrase ne décrit plus toutes ses copies. Avec ton IA, il faut regarder la même chose pour les questions, les pièces jointes et les outils.

Du coup, avant de coller un document sensible, la première question est très concrète : quel modèle traite cette demande ? Une interface capable de lancer un modèle local peut aussi proposer un modèle distant. Le bouton et le nom affichés comptent davantage que la couleur du logo de l'application.

La politique de LM Studio distingue ces cas. Pour les modèles locaux, l'éditeur dit que les conversations et documents restent sur l'appareil. Pour des services cloud facultatifs, comme un modèle distant ou la recherche web, les requêtes choisies passent par un traitement externe. L'éditeur annonce des conditions de non-conservation. Cela décrit ce qui arrive après le traitement ; l'information a quand même dû être transmise pour que le service fonctionne.

Donc un outil peut être respectueux de certaines règles de conservation sans fonctionner hors ligne. Et il peut se connecter pour chercher un modèle ou vérifier une mise à jour sans envoyer le contenu de tous tes chats. On doit distinguer ces trajets pour juger ce qu'il fait réellement.

[VISUEL : PC seul,puis porte vers réseau local,puis internet ;aucune commande d'ouverture montrée. F1–F3.]

La deuxième question, c'est qui peut parler à ton serveur. Ollama écoute par défaut sur l'adresse locale de la machine. Son API locale ne demande pas d'authentification. Ces deux choix vont ensemble : l'accès est prévu pour les programmes de ton ordinateur.

Par contre, si une configuration rend ce service accessible plus largement, le périmètre change. Le réseau de la maison, un hébergement et une adresse publique ne représentent pas le même accès. Il faut alors une protection adaptée, avec des utilisateurs autorisés et un accès réseau maîtrisé.

C'est le contexte des rapports d'exposition. Le chiffre du début compte des hôtes observés au fil des jours. Il ne signifie pas que tous étaient accessibles simultanément, ni que chacun a subi une intrusion. Et il ne permet pas d'affirmer que 175 mille personnes ont perdu leurs conversations.

Une étude antérieure de Censys avait déjà identifié des milliers de services accessibles. Mais elle employait une autre période et une autre méthode. Donc on ne divise pas les deux nombres pour annoncer une explosion précise du risque. Ce qu'on retient, c'est l'existence répétée de configurations publiquement accessibles.

Et on ne déduit pas non plus qu'un modèle sachant produire un appel d'outil contrôle forcément le terminal du serveur. Il faut qu'une application lui donne réellement cet outil et les permissions associées. La capacité du modèle et les droits d'un agent sont deux lignes distinctes de la configuration.

En fait, le problème pratique est simple : une porte qu'on ajoute pour le confort doit correspondre au public qu'on veut laisser entrer. Si tu utilises ton IA uniquement sur ton PC, tu n'as pas besoin d'une ouverture sur internet. Si tu veux y accéder à distance, l'authentification et le contrôle d'accès font partie de cette décision.

[GRAPHIC] [VISUEL : boîte«poids»,boîte«logiciel»,boîte«outils»,séparées. F7/F8.]

La troisième question arrive au téléchargement. Un fichier de modèle peut contenir des poids dans différents formats. Certains formats de sérialisation, comme Pickle, peuvent faire exécuter du code lors du chargement. Hugging Face documente ce risque et recommande des sources de confiance.

Safetensors a été conçu pour stocker les tenseurs sans ces mécanismes de Pickle. C'est un avantage précis. Mais un format ne certifie pas tout ce que tu installes autour : le moteur, un script d'installation ou un outil ajouté restent du logiciel.

Donc regarde la provenance du dépôt et les fichiers réellement nécessaires. Une page connue pour publier les poids du modèle n'est pas la même chose qu'un lien raccourci vers un installateur inconnu. Et le nombre de téléchargements ne te donne pas à lui seul l'identité de la personne qui a préparé le paquet.

La même logique vaut pour les extensions. LM Studio permet d'ajouter des serveurs MCP, c'est-à-dire des outils que le modèle peut utiliser. Sa documentation précise que certains peuvent accéder aux fichiers, utiliser le réseau ou exécuter du code. Du coup, installer un outil mérite la même attention qu'installer une autre application.

Imagine que tu donnes à ton assistant la clé d'un dossier de travail. Il peut maintenant lire ce dossier pour t'aider. Si tu lui donnes l'accès à tout le disque alors qu'il doit résumer un seul fichier, tu as élargi le périmètre sans ajouter forcément de service utile.

On peut donc limiter les dossiers accessibles et garder une validation pour les actions importantes. Ce sont des choix d'organisation, pas une accusation contre tous les outils. Le but est que les permissions correspondent à la tâche : résumer, écrire un fichier ou publier quelque chose ne demandent pas les mêmes accès.

[VISUEL : documentconfidentiel→outilrechercheweb→serviceexterne ;F5/F7.]

Et voilà le cas de la recherche web. Ton modèle peut être calculé sur la carte graphique du PC pendant qu'un outil envoie une requête à un moteur distant. Si la requête contient des éléments de ton document, ces éléments ont quitté l'ordinateur, même si la réponse finale est écrite localement.

Donc, pour une tâche sensible, il faut savoir ce que l'outil reçoit. Le titre d'un dossier client, une phrase entière du document ou une recherche générale ne transmettent pas la même information. La promesse de confidentialité se juge aussi sur cette étape, pas seulement sur le chargement du modèle.

Par contre, travailler hors ligne ne supprime pas les fichiers produits. L'historique peut rester enregistré sur le PC. Une exportation peut se retrouver dans un dossier synchronisé. Un journal peut contenir du contexte ajouté pour diagnostiquer un problème. La bonne question devient : qui peut lire ces copies et combien de temps tu souhaites les garder ?

Un ordinateur partagé demande aussi de penser aux comptes utilisateurs et à l'accès aux documents. La confidentialité vis-à-vis d'un fournisseur cloud et celle vis-à-vis de quelqu'un qui utilise ton ordinateur ne se règlent pas avec le même bouton.

Si ces trajets de données t'ont évité un partage que tu ne voulais pas, abonne-toi.

[GRAPHIC] [VISUEL : checklist àcocher,deuxprofils«personnel»/«organisation». F9/F10.]

Pour une organisation qui traite des données personnelles, le fait de rester sur site ne donne pas automatiquement une conformité au RGPD. La CNIL explique que ce déploiement peut limiter l'exposition à un tiers. Elle rappelle aussi les responsabilités de sécurité et d'encadrement des usages.

Donc une petite entreprise peut bénéficier du local sans considérer que tout devient autorisé. Il faut encore savoir quelles données on utilise, pour quel besoin, avec quels accès et quelles règles de conservation. Les obligations dépendent du traitement ; le mot local ne les efface pas.

Pour ton usage personnel, garde une checklist plus courte. D'abord, le modèle sélectionné est bien téléchargé et calculé sur ta machine. Ensuite, tu connais les fonctions qui utilisent un service externe. Puis tu sais à qui ton serveur est accessible. Enfin, tu choisis les dépôts et les outils auxquels tu fais confiance, avec des permissions limitées à leur travail.

Ajoute la maîtrise des historiques et des sauvegardes. Si tu n'as plus besoin d'un document dans une conversation, décide de ce que tu conserves. Et maintiens le logiciel à jour : garder les données chez toi implique aussi d'entretenir les programmes qui les manipulent.

Tu veux simplement poser des questions personnelles hors ligne ? Un modèle téléchargé, sans outil externe nécessaire, peut répondre à ce besoin. Tu veux un agent qui navigue, lit et modifie tes fichiers ? Son intérêt peut être grand, et ses permissions méritent d'être définies. Tu gères des documents professionnels ? Ajoute les règles de ton organisation et le cadre applicable.

[CROCHET : ton avis sur les données que tu préfères garder chez toi. Facultatif.]

L'IA locale te donne davantage de contrôle sur le trajet de tes données. Pour en profiter, suis ce trajet jusqu'au bout : le modèle, l'interface, les outils et les copies. C'est comme ça que « chez moi » devient une configuration que tu comprends. Allez, salut !

## Hors voix

Visuels : schémas et rapports cités. Aucun scan,serveurtiers,requêted'attaque ni auditpersonnel à effectuer. Risques : conserver293joursdans le hook ;distingueréditeur/auditindépendant ;pasd'affirmation deconformitéjuridiquegénérale. La checklist est défensive et ne décrit aucune méthode d'exploitation.
