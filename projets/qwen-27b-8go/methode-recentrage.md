# Cadrage et méthode de la reprise calculée

16/11/2026. Méthodes appliquées : [écriture et hook](../../ressources/skills-gpt/youtube-script-et-hook.md) ; [grill, variante storytelling](../../ressources/skills-gpt/youtube-script-grill.md). Références d'écriture absentes de la copie, mais retrouvées et lues : `/Users/innocent/.claude/skills/claude-youtube/references/retention-scripting-guide.md` et `algorithm-guide.md`. Leurs statistiques de rétention ne sont pas reprises comme faits ni comme promesses.

## Ce que la clarification change

Le spectateur regarde une explication, il ne suit pas un exercice. L'auteur raconte des mesures publiées ; aucune mise en scène ne lui attribue ces essais. La référence SimplyExplain fournit le rythme d'un exposé avec chiffres et conséquences. Son résultat reste attribué à un testeur, sans dire « on a testé ».

- **Public :** utilisateur de LM Studio avec carte de joueur, données démographiques du prompt.
- **Promesse :** comprendre le gain d'écriture et ce qu'il coûte en conversation et en qualité.
- **Enjeu :** savoir quel service peut encore rendre sa carte, sans confondre vitesse affichée et travail réussi.
- **Émotion :** curiosité, puis soulagement conditionnel selon le travail demandé.
- **Matière :** F1–F15 déjà documentés ; F16 est une division explicite, pas une expérience.
- **Transformation :** « le chiffre de vitesse suffit à choisir » → « le choix dépend aussi du travail et du contexte ».
- **Avis de l'auteur :** crochet facultatif, aucune préférence personnelle inventée dans la voix.

## Structure retenue

Explication documentaire avec une enquête sur le bénéfice réel. Débit traduit en temps d'attente → raison du gain → objection majeure sur qualité → limite de contexte → portée pour LM Studio → décision par usage. Le résultat arrive immédiatement ; le contraste qualité arrive avant la section mémoire, pour éviter le déroulé fichier/réglages/contexte/qualité d'un tutoriel.

Alternative écartée : tutoriel narratif. Elle obligerait à guider des manipulations, précisément la dérive signalée par l'auteur. Aucun voyage du héros ni crise personnelle inventée.

## Cinq ouvertures étudiées

Ce sont des options de travail, pas cinq introductions à enregistrer. Risques éditoriaux qualitatifs, aucune prédiction mesurée de rétention. Les règles du prompt priment sur le gabarit : 145 mots/minute, résultat avant15s, disclaimer avant30s, question avant plan. La variante curiosité révèle le chiffre immédiatement pour respecter cette priorité.

### 1. Preuve publiée, retenue

Sur une carte limitée à 8 gigas, un testeur change de fichier. Qwen 27B passe de 3,2 à 18 tokens par seconde pour écrire sa réponse. Ces chiffres sont les leurs, je n'ai rien testé chez moi. Sauf que le petit fichier perd aussi des capacités. Du coup, qu'est-ce que tu gagnes vraiment, si tu gardes ta carte de joueur ?

Mécanisme : un résultat attribué donne une raison d'écouter, son coût ouvre la question. Risque modéré : préciser « limitée » et conserver l'attribution. Adaptée recherche et suggestions, car modèle/capacité/gain sont compris immédiatement.

### 2. Contraste vitesse/qualité

Qwen 27B écrit à 18 tokens par seconde sur une carte limitée à 8 gigas, dans une mesure publiée. Avant, le testeur était à 3,2. Ces chiffres sont les leurs, je n'ai rien testé chez moi. Mais le fichier plus petit réussit moins bien certains travaux. Donc le gain de vitesse vaut quoi, si l'IA te laisse davantage de choses à corriger ?

Mécanisme : la promesse de vitesse rencontre son coût. Risque modéré : ne pas laisser croire que vitesse et qualité viennent du même banc d'essai ; attribution séparée dans le corps. Adaptée accueil et suggestions.

### 3. Problème d'attente

Pour écrire 500 tokens, les vitesses publiées donnent environ 2 minutes 36, puis 28 secondes. C'est Qwen 27B sur une carte limitée à 8 gigas. Ces chiffres sont les leurs, je n'ai rien testé chez moi ; les durées viennent d'un calcul. Sauf que le fichier plus petit change aussi les réponses. Donc ce temps gagné, tu le récupères vraiment sur ton travail ?

Mécanisme : rendre l'attente concrète. Risque plus élevé : trop d'hypothèses à préciser avant30s, chronométrage apparent. Adaptée suggestions si le montage rend le calcul évident. Écartée au profit du débit primaire dans le hook.

### 4. Scène documentaire

Une carte limitée à 8 gigas, un fichier remplacé : le testeur publie 18 tokens par seconde pour Qwen 27B, contre 3,2 auparavant. Ces chiffres sont les leurs, je n'ai rien testé chez moi. Le modèle tient maintenant entièrement sur la carte. Mais ce fichier a été davantage compressé. Du coup, est-ce qu'il peut encore faire le travail que tu veux lui confier ?

Mécanisme : entrer dans l'événement publié, sans scène personnelle. Risque modéré : le visuel doit être un schéma attribué, jamais une fausse capture. Adaptée suggestions ; résultat direct et enjeu simple.

### 5. Curiosité sur le compromis

De 3,2 à 18 tokens par seconde pour Qwen 27B : c'est le résultat publié d'un changement de fichier sur une carte limitée à 8 gigas. Ces chiffres sont les leurs, je n'ai rien testé chez moi. Mais le plus lent peut encore gagner pour certains travaux. Donc qu'est-ce que le petit fichier sacrifie pour accélérer autant ? C'est ce qui va décider de son intérêt pour toi.

Mécanisme : ouvrir une question sur le choix final en livrant tout de suite le résultat promis. Risque modéré : dernière phrase dispensable ; risque d'annonce artificielle. Adaptée accueil, moins directe que la variante1.

## Choix du hook

La variante1 convient au trafic visé et à la matière : elle livre une preuve identifiable, puis une question d'usage. La variante2 est le repli si le contraste qualité devient la miniature. Aucun mécanisme ne dépend de la notoriété de l'auteur ; pas d'autorité personnelle fabriquée. Le guide générique par tailles de chaîne n'apporte rien au choix de cette vidéo : priorité aux sources et au public déjà définis.

## Changements par rapport au texte précédent

- Retrait de tous les « ouvre », « réduis », « compare chez toi », de la proposition4096 et des captures avant tournage.
- Aucun protocole de test à accomplir par le spectateur comme condition du verdict.
- LM Studio conservé comme contexte et limite de transposition, sans menu ni instruction.
- Révélation qualité appuyée sur le graphique primaire ; calcul de temps clairement identifié.
- Motif récurrent : le débit18 devient temps d'attente, puis vitesse qui ne garantit ni réussite ni longue conversation.
- Production suffisante : voix/face caméra, sources publiques, barres chiffrées, schémas et tableau final.
