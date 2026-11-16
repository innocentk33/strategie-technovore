# Grill indépendant — Claude Code et modèle local

Revue du 16/11/2026 par l’agent principal, indépendant de la rédaction GPT-6.1 Sol. [Skill grill complet](../../ressources/skills-gpt/youtube-script-grill.md), mode B, onze axes et S1–S6. Contrôle de V1 contre F1–F10 et leurs journaux ; aucune installation ni mesure de réussite effectuée pour cette revue.

## Verdict : 7,1/10

La distinction importante est bien présente : une connexion documentée par Ollama ou LM Studio ne bénéficie pas du support officiel Anthropic pour les modèles non-Claude. Le texte évite de transformer des tailles de fichiers en preuves d’agent fiable. Cependant, le milieu explique plusieurs fois la même séparation entre répondre, utiliser un outil et réussir une tâche. Les trois paliers arrivent tard, sans que la situation change réellement entre eux. Raccourcir cette répétition permettra de montrer plus tôt le problème de mémoire du contexte.

## Test des trente secondes

| Tranche | Citation | Verdict |
|---|---|---|
| 0–5 s | « Claude Code peut envoyer ses demandes à une IA qui tourne sur ton PC. » | 🟢 Résultat documentaire immédiat, fidèle au sujet. |
| 5–15 s | « Ollama et LM Studio documentent cette connexion… ne transforme pas un petit modèle… » | 🟠 Preuve citée, mais comparaison à Claude introduite avant un avantage concret. |
| 15–30 s | « Ces chiffres sont les leurs… avec 8, 12 ou 16 gigas… qu’est-ce que cette connexion permet vraiment ? » | 🟢 Transparence et question avant trente secondes. |
| Pont | « chemin d’une demande… instructions et outils… candidat devant chaque palier » | 🟢 Livrables précis, trois paliers repris ensuite. |

**65 mots jusqu’à la question,26,9 s à145 mots/min.** Résultat, sujet, transparence, tension et question présents ; pas d’introduction personnelle. Le meilleur obstacle concret apparaît plus tard :64K recommandés alors que le fichier de14GB occupe déjà une grande part d’une carte16Go. Il peut donner plus de force au hook.

**Réécriture1 proposée :**

> Claude Code peut envoyer ses demandes à une IA sur ton PC. Sauf que son fichier doit laisser de la place aux instructions, au code et aux résultats des outils. Ces chiffres sont les leurs, je n’ai rien testé chez moi. Donc, avec8,12 ou16gigas, quelle tâche peut-on raisonnablement lui confier ?

Environ57mots,24s ; afficher les docsF1/F2. La réponse reste conditionnelle puisque aucun taux de réussite comparable n’est disponible. Conserver la question avant30s après toute insertion.

## Tableau de bord

| Axe | /10 | État et diagnostic |
|---|---:|---|
| 1 Promesse |8|🟢 Titre resserré sur connexion et limites ; ne promet plus Claude gratuit équivalent. |
| 2 Alignement |8|🟢 Choisir une tâche réaliste avant un achat ; pas d’installation imposée. |
| 3 Problème profond |8|🟢 Éviter un achat pour un agent dont la fiabilité n’est pas prouvée. |
| 4 Public/complexité |7|🟠 Atelier utile ; « harnais » demande un mot plus simple. |
| 5 Valeur/originalité |8|🟢 Docs des deux outils et absence de support Anthropic rapprochées. |
| 6 Structure/transformation |7|🟠 Le choix final est clair, mais le milieu répète la même limite. |
| 7 Histoire |6|🟠 Enquête de compatibilité ; peu de nouvelles preuves après64K. |
| 8 Mais/donc |7|🟠 Connexion→outils→contexte cohérent ; paliers encore catalogués. |
| 9 Engagement actif |6|🟠 Une question puis longue exposition ; faire anticiper la place restante utile. |
| 10 Oralité/liaisons |6|🟠17liaisons strictes/1492mots=1,14/100 ; phrases généralement lisibles. |
| 11 Anti-IA |7|🟠 Quelques formules de faux adversaire « agentillimité », « record de téléchargement ». |
| S1 Trente secondes |8|🟢 Budget tenu ; rendre le manque de place plus concret. |
| S2 Pont |8|🟢 Trois livrables, puis résultatdocumenté. |
| S3 Retournements |6|🟠 Support absent et recommandations de contexte sont les vrais obstacles ; répétitions entre les deux. |
| S4 Planté/récolté |7|🟢 Connexion du début récoltée comme condition insuffisante à la fin. |
| S5 Personnage/enjeu |8|🟢 Propriétaire de petite carte et développeur de projets plus longs distincts. |
| S6 Fin |7|🟢 Trois usages, limite d’équivalence, renvoi18janvier daté. |

Total onze axes78/110≈7,1/10. Axes S sans double pondération.

## Corrections et réécritures

### Dire directement ce qu’un outil exige

> « Modifier un fichier, ce n’est pas seulement écrire du code dans une réponse. »

La distinction est utile mais la tournure reprend la mécanique que l’auteur veut éviter.

**Réécriture2 :** « Pour modifier un fichier, le modèle doit choisir l’action, fournir les bons arguments et comprendre le résultat. Donc une réponse correcte dans le chat peut encore demander une adaptation avant de devenir une action fiable. » Garder ces trois opérations, sans refaire leur définition dans trois autres paragraphes.

### Trois paragraphes redisent l’absence de preuve d’agent

> « Un assistant qui répond vite… n’est pas forcément celui qui termine… »
> « Un même modèle peut être capable de rédiger une fonction… échouant à choisir… »
> « Si un outil produit beaucoup de code… le débit de texte peut masquer… »

Ils sont plausibles, mais n’apportent aucune nouvelle observation du dossier. Après les recommandations64K et25K, aller directement aux fichiers candidats. Garder une seule conséquence sur le résultat attendu.

**Réécriture3 :** « Du coup, le fichier de modèle ne suffit pas à dimensionner la machine. Il faut aussi loger les instructions et le travail en cours. On peut regarder nos trois candidats avec cette réserve en tête, sans leur attribuer un taux de réussite qu’on n’a pas. » F5–F9.

### Le palier16Go est le meilleur retour à la question initiale

> « La fiche d’Ollama affiche un fichier d’environ14gigas… »
> « Donc16gigas ne garantissent pas que64000tokens resteront entièrement sur leGPU… »

Conserver ce rapprochement et le montrer avant de conclure. Ne jamais afficher16−14=2Go de cache garanti : unités, allocations et partage importent.

**Réécriture4 :** « Le candidat16gigas a un fichier annoncé autour de14gigas. Sauf que le contexte conseillé reste à ajouter. Voilà pourquoi “le modèle se charge” ne décrit pas encore une longue session de code. La jauge doit aussi réserver de la place aux informations du projet. » F7/F8 ; fichier surdisque distinct de consommationtotale.

### Éviter les promesses absurdes qu’aucun exemple n’a faites

> « agent “illimité” » ; « record de téléchargement » ; « tout le système ne coûte rien ».

Le titre initial contenait gratuit, donc expliquer les coûts reste nécessaire. Dire « le calcul local peut éviter une facturation distante pour ces demandes ; matériel et logiciels gardent leurs conditions » suffit. Ne pas introduire un argument juridique absent : F4 dit conditions propriétaires, pas interdiction de toute intégration.

## Contrôle des faits

- F1/F2 : connexion documentée par les outils, contexte64K+ et>~25K recommandés ; aucun minimum universel déduit de leur différence.
- F3 : absence de support officiel Anthropic pour le routage non-Claude, explicitement conservée. « Peut se casser si évolution » reste un risque conditionnel, pas un incident observé.
- F4 : licence propriétaire ; ne pas qualifier Claude Code de logiciel open source. La V1 ne le fait pas.
- F5/F6/F7 : tailles2,74GB,8,99GB et14GB, formats précis. Ces valeurs sont celles des fichiers et n’établissent ni taux de réussite ni confort sur8/12/16Go.
- Qwen2.5-Coder n’est pas certifié pour les outils de Claude Code ; la voix le précise. Un modèle cité dans un exemple de connexion n’est pas validé sur tous les projets.
- Pas de débits comparables : aucune fausse table de vitesse. La voix distingue génération, lecture et échangesoutils.
- F10 est un raisonnement de coût, pas un tarifclient Claude Code ou une gratuitécontractuelle démontrée. Ne pas ajouter « aucun abonnement requis » sans preuve adaptée.
- Version de janvier future : garder date documentaire16/11 et besoin d’actualisation ; ne pas inventer les modèles recommandés de janvier.
- Aucun nomdecréateur envoix, aucun dépôt personnel prétendument modifié, aucun test demandé.

## Oralité et anti-IA

1492mots≈10:17, horsbalises/titres/notes.17liaisons strictes :donc11,ducoup3,enfait2,voilàpourquoi1, soit1,14/100. Des connecteurs ajoutés mécaniquement ne répareront pas les répétitions : couper celles-ci puis relier les conséquences réelles. Viser≥1,5 sans deux débuts identiques successifs.

Remplacer « harnais » par « outil qui organise le travail ». Dans « Connected et autonomous », aucune traduction anglaise n’est nécessaire : la V1 utilise déjà les termesfrançais. Nettoyer les balises « palier8Go », « candidatgpt-oss20B », « àdimensionner » pour des documents lisibles.

## À garder

« Anthropic indique ne pas prendre en charge… » : fait décisif pour la promesse.

« Le nom “Coder” ne certifie pas la réussite des appels d’outils » : limite précise du candidat12Go.

« La génération de texte, la lecture des fichiers et les allers-retours d’outils sont des temps différents » : distinction utile, sans fauxbenchmark.

## Plan d’action

1. Conserver le résultat de connexion immédiat ; hook plus concret sur le contexte et question avant30s.
2. Couper les répétitions après64K ; avancer les paliers et donner la place restante comme question, sans chiffre de cache fictif.
3. Reformuler directement les fausses oppositions et les adversaires imaginaires ; conserver les limites support/licence/coût.
4. Améliorer les raccords et lisibilité, recalculer voix/timecodes et produireTP concordant.
5. Maintenir tous les candidats comme pistes conditionnelles, sans les transformer en recommandations d’achat validées par un agent testé.

## Corrections appliquées après revue

Claude Code : hook centré sur mémoire utile, répétitions après64K condensées, outils expliqués directement, harnais remplacé, candidats conditionnels et absence de support non-Claude conservés ; aucune gratuité contractuelle globale ajoutée.

Final : 1548 mots, durée10:41, ouverture55 mots≈22.8s, 28 liaisons strictes soit 1.81/100. Timecodes calculés sur voix, TP concordant avec chiffres et souffles. Limites factuelles maintenues.

Dernier contrôle ciblé : raccord répété ou phrase répétée retirés, voix directe conservée ; 1536 mots, 10:36, 1.82 liaisons/100 ; timecodes et TP actualisés.

Dernier contrôle ciblé : raccord répété ou phrase répétée retirés, voix directe conservée ; 1536 mots, 10:36, 1.82 liaisons/100 ; timecodes et TP actualisés.

Cohérence calendrier : renvoi vers la publication suivante corrigé. Compte final actualisé : 1537 mots, 10:36, 1.82 liaisons/100 ; fin du tableau et téléprompteur régénérés.
