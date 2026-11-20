# Claude Code avec une IA locale : connexion, mémoire et tâches réalistes

Script corrigé du 16/11/2026, créneau du 11 janvier 2027. **1537 mots de voix, environ 10:36 à 145 mots/min.** Relevés et recommandations documentaires, aucun essai personnel.

| Partie | Timecodes calculés |
|---|---|
| Résultat et question | 0:00–0:23 |
| Plan concret | 0:23–0:42 |
| Connexion et outils | 0:42–3:44 |
| Contexte utile | 3:44–5:59 |
| Candidats 8/12/16 Go | 5:59–9:14 |
| Verdict | 9:14–10:36 |


## Voix

Claude Code peut envoyer ses demandes à une IA sur ton PC. Sauf que son fichier doit laisser de la place aux instructions, au code et aux résultats des outils. Donc, avec 8, 12 ou 16 gigas, quelle tâche peut-on raisonnablement lui confier ? [F1,F2]

[VISUEL : Claude Code, moteur local, modèle, fichiers du projet ; schéma documentaire.]

On suit le chemin d’une demande, on regarde ce que prennent les instructions et les outils, puis on place un candidat devant chaque palier de mémoire. À la fin, tu auras un verdict selon la taille du projet, sans confondre « connecté » et « autonome ».

Le résultat documenté est concret. Claude Code peut parler à un serveur local qui comprend le format de messages attendu. Ollama propose même une commande de lancement dédiée. LM Studio documente aussi son point d’entrée compatible. Donc l’interface et le modèle peuvent venir de deux endroits différents. [F1,F2]

Imagine un atelier. Claude Code apporte l’organisation du travail : il présente les fichiers, demande des modifications et peut lancer des outils. Le modèle reçoit les informations et choisit ce qu’il propose ensuite. Le moteur local fait tourner ce modèle. Si un de ces éléments change, le résultat peut changer.

[VISUEL : trois blocs distincts, interface, moteur et modèle ; pas de démo personnelle.]

Du coup, quand tu vois « Claude Code gratuit », demande quel élément est gratuit et où tourne le modèle. Si une requête part vers un modèle de cloud, on n’a pas fait disparaître le service distant en changeant simplement la fenêtre. La documentation d’Ollama présente à la fois des possibilités locales et des possibilités cloud. [F1]

Avec un modèle réellement local, le calcul des réponses se fait sur le matériel qui l’héberge. Ça peut éviter une facture de tokens pour ces demandes auprès d’un fournisseur distant. Mais la machine, la mémoire et le temps d’attente restent dans le budget. Donc la dépense de matériel et les conditions des logiciels restent à prendre en compte. [F10]

Il y a aussi une limite de support. Anthropic indique ne pas prendre en charge le routage vers des modèles autres que Claude à travers ces passerelles. Donc une intégration documentée par le moteur local ne vaut pas une garantie de fonctionnement donnée par Anthropic. [F3]

Ce détail compte pour un outil de travail. Si un format de message évolue et que le moteur local ne suit pas encore, certaines fonctions peuvent se casser. Le modèle peut répondre dans un chat simple, tout en rencontrant des difficultés dans l’outil qui organise le projet.

[VISUEL : compatibilité de transport, utilisation des outils et qualité du travail, trois critères séparés.]

Voilà pourquoi la première question utile porte sur les outils. Pour modifier un fichier, le modèle doit choisir l’action, fournir les bons arguments et comprendre le résultat. Donc une réponse correcte dans un chat ne démontre pas encore une action fiable dans le projet.

Du coup, une petite erreur de format peut donc bloquer une opération pourtant simple. À l’inverse, une réponse bien présentée peut donner l’impression que tout marche, alors qu’aucun fichier n’a été modifié. Le texte affiché et l’action réellement accomplie doivent rester deux choses observables.

Pour les usages courts, cette boucle peut être assez modeste : expliquer un fichier, proposer une fonction, commenter une erreur. Pour un gros changement dans un dépôt, elle transporte beaucoup plus d’informations. Donc les besoins de mémoire ne se résument pas à la taille du fichier du modèle.

En fait, le contexte, c’est tout ce qui doit rester disponible pour la demande : les instructions, les extraits du projet, les appels d’outils et leurs réponses. La conversation précédente peut aussi occuper cet espace. Imagine le bureau d’un développeur avec les documents ouverts. Quand il n’y a plus de place, quelque chose doit être écarté.

[VISUEL : contexte rempli par instructions, code et résultats d’outils ; pas de quantité inventée.]

Ollama conseille un contexte d’au moins 64 000 tokens pour les modèles locaux dans cette intégration. LM Studio conseille plus d’environ 25 000. Ce sont leurs recommandations, pas deux preuves qu’un même contexte conviendra à tous les projets. [F1,F2]

Du coup, une carte qui charge le modèle avec une conversation courte ne garantit pas ce volume de travail. Le cache de conversation prend de la mémoire supplémentaire. Il peut demander de réduire le contexte, de changer la compression ou de répartir le travail sur d’autres ressources.

Et réduire le contexte a un prix pratique. Le modèle peut recevoir moins de fichiers à la fois, ou perdre des éléments d’une longue discussion. Un assistant qui répond vite avec très peu d’informations n’est pas forcément celui qui termine correctement la tâche complète.

Du coup, le fichier du modèle ne suffit pas à dimensionner la machine. Il faut aussi loger les instructions et le travail en cours. On peut regarder les trois candidats avec cette réserve en tête. Leur taille est documentée ; leur réussite comme agent reste une autre question. [F5–F9]

Un résultat utile peut être très modeste : une fonction correctement expliquée, une proposition de modification lisible ou un diagnostic qui cite le bon passage. Ces tâches offrent un périmètre plus précis qu’une demande de transformer tout le projet. Le choix du modèle peut donc commencer avec la quantité d’informations nécessaire.

Par contre, si l’agent doit coordonner des fichiers et relire des résultats d’outils, chaque étape ajoute du travail. Le temps total comprend ces échanges et la relecture humaine. Une réponse rapide devient utile quand elle mène à une modification correcte et vérifiable.

Avec cette réserve, on peut commencer par les cartes de 8 gigas. Un candidat léger est Qwen3.5-4B en Q4_K_M, dont les poids occupent environ 2,74 gigas sur le disque. Donc il laisse davantage de place qu’un gros modèle fortement compressé. Ça en fait une piste pour de petites demandes, pas une preuve qu’il saura piloter un projet entier. [F5]

[VISUEL : palier 8 Go ; fichier2,74Go ; cache et bureau avec marge non chiffrée.]

Sur ce palier, un usage raisonnable serait l’explication d’un bout de code ou la rédaction d’une fonction bien délimitée. Le résultat doit être relu. Si la demande suppose de coordonner beaucoup de fichiers, la limite peut venir des capacités du modèle avant même que la mémoire soit pleine.

Donc, pour quelqu’un qui possède déjà cette carte, la connexion locale peut avoir un intérêt. Acheter une nouvelle carte pour des projets plus longs demanderait des résultats solides sur les tâches qui motivent l’achat.

Par contre, avec 12 gigas, on peut examiner un candidat plus spécialisé en code, Qwen2.5-Coder-14B. Son fichier Q4_K_M est affiché autour de 9 gigas. La différence avec la capacité de la carte doit encore accueillir le contexte et les allocations du logiciel. [F6]

[VISUEL : palier 12 Go ; poids9Go ; ne pas afficher3Go comme cache garanti.]

C’est une piste pour produire ou expliquer du code. En revanche, son nom « Coder » ne certifie pas la réussite des appels d’outils dans Claude Code. L’intégration technique et la qualité de l’agent demandent des preuves distinctes. Un bon spécialiste d’une fonction peut être moins solide quand il faut gérer toute une série d’actions.

Du coup, sur ce budget mémoire, garder un périmètre court peut donc être plus utile que de chercher le maximum de paramètres. Une consigne claire, un petit ensemble de fichiers et un résultat vérifiable donnent un objectif plus concret qu’une promesse d’autonomie sans limite.

Avec 16 gigas, gpt-oss-20B devient un autre candidat à regarder. La fiche d’Ollama affiche un fichier d’environ 14 gigas en MXFP4 et documente des fonctions d’outils. LM Studio cite aussi ce modèle dans son exemple de connexion à Claude Code. [F2,F7]

Mais le fichier ne remplit pas à lui seul le tableau de compatibilité. Il reste la mémoire nécessaire au contexte, au logiciel et aux autres usages de la carte. Sauf que le contexte conseillé reste à ajouter au fichier de 14 gigas. Voilà pourquoi 16 gigas ne garantissent pas que 64 000 tokens resteront entièrement sur le GPU dans toutes les conditions. [F8]

[VISUEL : palier 16 Go ; candidat gpt-oss-20B ; contexte64K marqué à dimensionner.]

En fait, le palier supérieur donne surtout plus de choix. Tu peux préférer un modèle plus petit avec davantage de conversation, ou un modèle plus gros avec un périmètre serré. Le bon compromis dépend de l’opération que tu veux réussir.

Par contre, pour la vitesse, aucun tableau de ces candidats n’est présenté comme un duel identique dans Claude Code sur ces trois cartes. La génération de texte, la lecture des fichiers et les allers-retours d’outils sont des temps différents. Additionner des chiffres pris dans trois démonstrations produirait un faux classement. [F9]

Donc le verdict par profil est donc assez simple. Tu veux comprendre de petits fichiers et obtenir des propositions que tu relis : un modèle léger peut rendre la connexion locale intéressante. Tu veux modifier un projet de taille moyenne : le contexte, les outils et la fiabilité du modèle deviennent les critères décisifs.

Tu veux remplacer un modèle Claude sur de longues tâches autonomes : la connexion seule ne suffit pas à établir cette équivalence. Il faut que les résultats sur tes types de projets la soutiennent. Ici, cette promesse n’est pas démontrée. [F3,F9]

Le moteur déjà utilisé peut aussi simplifier ce choix. Si tes modèles sont déjà dans LM Studio, sa connexion documentée évite de supposer qu’un changement d’application améliorera les compétences du modèle. Si tu travailles déjà avec Ollama, son lancement dédié propose un autre chemin. Dans les deux cas, le modèle local conserve ses capacités et ses limites. [F1,F2]

[CROCHET : ton avis sur le compromis petit assistant local ou agent plus autonome, sans résultat personnel inventé.]

Le 14 janvier, on regardera ce que le local change pour ta vie privée, avec les données qui restent sur la machine et les fonctions connectées. Et le 21 janvier, le guide de 4 à 16 gigas donnera les candidats pour ta carte.

Allez, salut !


## Notes de production

Documentation publique et schémas uniquement. Aucune installation, aucun test ni capture demandés à l’auteur. Candidats conditionnels, aucun taux de réussite sur dépôt inventé. Le routage non-Claude n’est pas pris en charge par Anthropic. La connexion locale ne démontre pas une gratuité contractuelle globale. Actualisation documentaire nécessaire pour janvier. Avis facultatif.
