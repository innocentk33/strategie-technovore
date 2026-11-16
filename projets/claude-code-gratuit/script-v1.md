# Claude Code avec une IA locale : ce qui marche, et la limite des petites cartes

V1 documentaire du 16/11/2026. Créneau provisoire du 7/01/2027. Cible 10–12 min à 145 mots/min. Les noms de modèles sont des candidats documentés ; aucun dépôt n’a été codé par l’auteur pour cette vidéo.

| Partie | Repère |
|---|---|
| Résultat et question |0:00–0:30|
| Le chemin d’une demande locale |0:30–2:30|
| Contexte et outils |2:30–5:10|
|8,12,16Go : candidats et limites |5:10–8:20|
| Verdict et coût |8:20–fin|

## Voix

Claude Code peut envoyer ses demandes à une IA qui tourne sur ton PC. Ollama et LM Studio documentent cette connexion. Mais la fenêtre de Claude Code ne transforme pas un petit modèle local en modèle Claude. [F1,F2]

Ces chiffres sont les leurs, je n’ai rien testé chez moi. Alors, avec 8, 12 ou 16 gigas de mémoire vidéo, qu’est-ce que cette connexion permet vraiment ?

[VISUEL : Claude Code, moteur local, modèle, fichiers du projet ; schéma documentaire.]

On suit le chemin d’une demande, on regarde ce que prennent les instructions et les outils, puis on place un candidat devant chaque palier de mémoire. À la fin, tu auras un verdict selon la taille du projet, sans confondre « connecté » et « autonome ».

Le résultat documenté est concret. Claude Code peut parler à un serveur local qui comprend le format de messages attendu. Ollama propose même une commande de lancement dédiée. LM Studio documente aussi son point d’entrée compatible. Donc l’interface et le modèle peuvent venir de deux endroits différents. [F1,F2]

Imagine un atelier. Claude Code apporte l’organisation du travail : il présente les fichiers, demande des modifications et peut lancer des outils. Le modèle reçoit les informations et choisit ce qu’il propose ensuite. Le moteur local fait tourner ce modèle. Si un de ces éléments change, le résultat peut changer.

[VISUEL : trois blocs distincts, interface, moteur et modèle ; pas de démo personnelle.]

Du coup, quand tu vois « Claude Code gratuit », demande quel élément est gratuit et où tourne le modèle. Si une requête part vers un modèle de cloud, on n’a pas fait disparaître le service distant en changeant simplement la fenêtre. La documentation d’Ollama présente à la fois des possibilités locales et des possibilités cloud. [F1]

Avec un modèle réellement local, le calcul des réponses se fait sur le matériel qui l’héberge. Ça peut éviter une facture de tokens pour ces demandes auprès d’un fournisseur distant. Mais la machine, la mémoire et le temps d’attente restent dans le budget. « Pas de facture pour cette requête » ne signifie pas « tout le système ne coûte rien ». [F10]

Il y a aussi une limite de support. Anthropic indique ne pas prendre en charge le routage vers des modèles autres que Claude à travers ces passerelles. Donc une intégration documentée par le moteur local ne vaut pas une garantie de fonctionnement donnée par Anthropic. [F3]

Ce détail compte pour un outil de travail. Si un format de message évolue et que le moteur local ne suit pas encore, certaines fonctions peuvent se casser. Le modèle peut répondre dans un chat simple, tout en rencontrant des difficultés dans le harnais qui organise le projet.

[VISUEL : compatibilité de transport, utilisation des outils et qualité du travail, trois critères séparés.]

Voilà pourquoi la première question utile porte sur les outils. Modifier un fichier, ce n’est pas seulement écrire du code dans une réponse. Le modèle doit demander la bonne action, avec les bons arguments, puis comprendre le résultat renvoyé. Ensuite, il doit poursuivre le travail sans oublier la consigne.

Une petite erreur de format peut donc bloquer une opération pourtant simple. À l’inverse, une réponse bien présentée peut donner l’impression que tout marche, alors qu’aucun fichier n’a été modifié. Le texte affiché et l’action réellement accomplie doivent rester deux choses observables.

Pour les usages courts, cette boucle peut être assez modeste : expliquer un fichier, proposer une fonction, commenter une erreur. Pour un gros changement dans un dépôt, elle transporte beaucoup plus d’informations. Donc les besoins de mémoire ne se résument pas à la taille du fichier du modèle.

Le contexte, c’est tout ce qui doit rester disponible pour la demande : les instructions, les extraits du projet, les appels d’outils et leurs réponses. La conversation précédente peut aussi occuper cet espace. Imagine le bureau d’un développeur avec les documents ouverts. Quand il n’y a plus de place, quelque chose doit être écarté.

[VISUEL : contexte rempli par instructions, code et résultats d’outils ; pas de quantité inventée.]

Ollama conseille un contexte d’au moins 64 000 tokens pour les modèles locaux dans cette intégration. LM Studio conseille plus d’environ 25 000. Ce sont leurs recommandations, pas deux preuves qu’un même contexte conviendra à tous les projets. [F1,F2]

Du coup, une carte qui charge le modèle avec une conversation courte ne garantit pas ce volume de travail. Le cache de conversation prend de la mémoire supplémentaire. Il peut demander de réduire le contexte, de changer la compression ou de répartir le travail sur d’autres ressources.

Et réduire le contexte a un prix pratique. Le modèle peut recevoir moins de fichiers à la fois, ou perdre des éléments d’une longue discussion. Un assistant qui répond vite avec très peu d’informations n’est pas forcément celui qui termine correctement la tâche complète.

Et le choix du moteur ne supprime pas cette différence. Un même modèle peut être capable de rédiger une fonction dans un message, tout en échouant à choisir correctement les outils qui l’insèrent dans le projet. Du coup, un résultat impressionnant dans une fenêtre de discussion ne prouve pas encore un bon agent.

Il faut aussi compter la relecture. Si un outil produit beaucoup de code mais demande longtemps pour corriger ses erreurs, le débit de texte peut masquer le temps total de travail. Donc le critère utile reste une modification correcte et compréhensible. C’est ce résultat qui apporte de la valeur, même quand la réponse arrive moins vite.

Le vrai confort se juge donc sur un périmètre précis. Est-ce qu’on veut comprendre un fichier, écrire une petite modification, ou suivre une opération longue ? Ces trois tâches n’ont pas le même besoin de mémoire ni le même risque d’erreur.

Passons aux cartes de 8 gigas. Un candidat léger est Qwen3.5-4B en Q4_K_M, dont les poids occupent environ 2,74 gigas sur le disque. Donc il laisse davantage de place qu’un gros modèle fortement compressé. Ça en fait une piste pour de petites demandes, pas une preuve qu’il saura piloter un projet entier. [F5]

[VISUEL : palier8Go ; fichier2,74Go ; cache et bureau avec marge non chiffrée.]

Sur ce palier, un usage raisonnable serait l’explication d’un bout de code ou la rédaction d’une fonction bien délimitée. Le résultat doit être relu. Si la demande suppose de coordonner beaucoup de fichiers, la limite peut venir des capacités du modèle avant même que la mémoire soit pleine.

Donc, pour quelqu’un qui possède déjà cette carte, la connexion locale peut avoir un intérêt. Acheter une nouvelle carte uniquement pour reproduire la promesse d’un agent « illimité » serait une autre décision. Il faudrait des résultats solides sur les tâches qui motivent l’achat.

Avec 12 gigas, on peut examiner un candidat plus spécialisé en code, Qwen2.5-Coder-14B. Son fichier Q4_K_M est affiché autour de 9 gigas. La différence avec la capacité de la carte doit encore accueillir le contexte et les allocations du logiciel. [F6]

[VISUEL : palier12Go ; poids9Go ; ne pas afficher3Go comme cache garanti.]

C’est une piste pour produire ou expliquer du code. En revanche, son nom « Coder » ne certifie pas la réussite des appels d’outils dans Claude Code. L’intégration technique et la qualité de l’agent demandent des preuves distinctes. Un bon spécialiste d’une fonction peut être moins solide quand il faut gérer toute une série d’actions.

Sur ce budget mémoire, garder un périmètre court peut donc être plus utile que de chercher le maximum de paramètres. Une consigne claire, un petit ensemble de fichiers et un résultat vérifiable donnent un objectif plus concret qu’une promesse d’autonomie sans limite.

Avec 16 gigas, gpt-oss-20B devient un autre candidat à regarder. La fiche d’Ollama affiche un fichier d’environ 14 gigas en MXFP4 et documente des fonctions d’outils. LM Studio cite aussi ce modèle dans son exemple de connexion à Claude Code. [F2,F7]

Mais le fichier ne remplit pas à lui seul le tableau de compatibilité. Il reste la mémoire nécessaire au contexte, au logiciel et aux autres usages de la carte. Donc 16 gigas ne garantissent pas que 64 000 tokens resteront entièrement sur le GPU dans toutes les conditions. [F8]

[VISUEL : palier16Go ; candidatgpt-oss20B ; contexte64K marqué àdimensionner.]

En fait, le palier supérieur donne surtout plus de choix. Tu peux préférer un modèle plus petit avec davantage de conversation, ou un modèle plus gros avec un périmètre serré. Le bon compromis dépend de l’opération que tu veux réussir, pas du record de téléchargement.

Pour la vitesse, aucun tableau de ces candidats n’est présenté comme un duel identique dans Claude Code sur ces trois cartes. La génération de texte, la lecture des fichiers et les allers-retours d’outils sont des temps différents. Additionner des chiffres pris dans trois démonstrations produirait un faux classement. [F9]

Le verdict par profil est donc assez simple. Tu veux comprendre de petits fichiers et obtenir des propositions que tu relis : un modèle léger peut rendre la connexion locale intéressante. Tu veux modifier un projet de taille moyenne : le contexte, les outils et la fiabilité du modèle deviennent les critères décisifs.

Tu veux remplacer un modèle Claude sur de longues tâches autonomes : la connexion seule ne suffit pas à établir cette équivalence. Il faut que les résultats sur tes types de projets la soutiennent. Ici, cette promesse n’est pas démontrée. [F3,F9]

[CROCHET : ton avis sur le compromis petit assistant local ou agent plus autonome, sans résultat personnel inventé.]

Et si ton objectif est d’abord de savoir quel modèle tient sur ta carte, le comparatif de 4 à 16 gigas est prévu le 18 janvier. Il part de la mémoire disponible et distingue le fichier, la conversation et la vitesse publiée.

Allez, salut !

## Notes

Visuels : documentation publique et schémas. Aucune installation, aucun test ni capture demandés à l’auteur. Risques : gratuité totale non établie, support non-Claude absent côté Anthropic, paliers théoriques confondus avec agent fiable. Les candidats ne sont pas des vainqueurs universels. Janvier demande une actualisation documentaire.
