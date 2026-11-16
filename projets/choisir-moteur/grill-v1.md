# Grill indépendant — Choisir son moteur local

Revue du 16/11/2026 par l’agent principal, indépendant du rédacteur GPT-6.1 Sol. Application du [skill complet](../../ressources/skills-gpt/youtube-script-grill.md), mode B, onze axes et variante storytelling. V1 rapprochée de F1–F10 et du journal de double lecture ; aucun benchmark exécuté pour la revue.

## Verdict : 7,2/10

Le guide évite trois erreurs utiles à corriger : LM Studio dispose d’un serveur, llama.cpp dispose d’une interface web, et une application ne détermine pas seule les performances. Les trois profils finaux tiennent la promesse. Le point faible est le hook : son63% vient d’un Steam Deck et d’une préparation Vulkan, puis la question vise unPC et trois applications. La portée est bien limitée, mais le lien narratif demande une formulation plus directe. Le milieu répète trop souvent l’absence de podiumWindows.

## Test des trente secondes

| Tranche | Citation | Verdict |
|---|---|---|
|0–5s|« Une étude publiée gagne jusqu’à63%… »|🟠 Chiffre fort ; une étude ne “gagne” pas, c’est le débit de lecture mesuré qui progresse.|
|5–15s|« …préparation de Vulkan sur un Steam Deck. Le choix du logiciel ne suffit donc pas… »|🟠 Matériel identifié ; vocabulaire technique avant le service rendu.|
|15–30s|« Ces chiffres sont les leurs… qu’est-ce qui doit décider entre… ? »|🟢 Transparence et question avant30s.|
|Pont|« trois questions… discuter… contrôler… brancher… »|🟢 Livrables concrets ; la suite répond dans cet ordre.|

**59mots,24,4s à145mots/min jusqu’à la question.** Sujet et question présents ; résultat avant15s mais indirectement lié à la promesse. Aucun historique ni présentation. Le nombre ne doit jamais être affiché comme gain de génération ou résultat surPCWindows.

**Réécriture1, conserver le fait en clarifiant son rôle :**

> Sur un Steam Deck, une préparation de Vulkan améliore jusqu’à63% la lecture du prompt dans une étude publiée. Donc les réglages peuvent changer le résultat sans changer d’application. Ces chiffres sont les leurs, je n’ai rien testé chez moi. Alors, pour choisir Ollama, LM Studio ou llama.cpp sur tonPC, quelle différence compte vraiment ?

Environ60mots. Le fait “sans changer d’application” doit correspondre exactement à la comparaisonF4 ; si le protocole ne l’établit pas, dire « les réglages font partie du résultat ». Éviter de renforcer un chiffre au-delà de sa source. Autre option : ouvrir directement sur les fonctions croisées plutôt qu’un gainSteamDeck.

## Tableau de bord

| Axe | /10 | État et diagnostic |
|---|---:|---|
|1 Promesse|8|🟢 Choix parusage tenu ; pas de vainqueur de vitesse inventé.|
|2 Alignement|8|🟢 Garder l’outil actuel si besoin satisfait ; choix concret sans achat requis.|
|3 Problème profond|7|🟢 Éviter un changement d’application qui n’améliore pas le travail.|
|4 Public/complexité|7|🟠 Vulkan enouverture ; API etserveur expliqués ensuite, sansmode d’emploi.|
|5 Valeur/originalité|8|🟢 Chevauchement des fonctions etversions documentés ; contreparties réelles.|
|6 Structure/transformation|8|🟢 Trois questions, trois réponses etbonusStrata borné.|
|7 Histoire|6|🟠 Parcours de choix cohérent, peu d’évolution dans le long passagebenchmark.|
|8 Mais/donc|7|🟠 Fichier/version→performance causal ; certains “autres points” restent listés.|
|9 Engagement actif|7|🟢 Choix selon besoin identifiable ; peut inviter à choisir une des troisquestions dès leplan.|
|10 Oralité/liaisons|5|🔴15liaisons strictes/1461mots=1,03/100, risque de récitation.|
|11 Anti-IA|8|🟢 Peu de clichés ; plusieurs phrases négatives répétées sur le podium.|
|S1 Trente secondes|7|🟠 Temps tenu ; lienDeck/PC à clarifier.|
|S2 Pont|9|🟢 Très concret, avecbonus annoncé etlivré.|
|S3 Retournements|6|🟠 Interfaces etAPI croisées surprennent ; milieu méthodologique ralentit.|
|S4 Planté/récolté|8|🟢63%réexpliqué, troisquestions récoltées auverdict.|
|S5 Personnage/enjeu|7|🟢 Débutant, intégrateur, utilisateur technique reconnaissables.|
|S6 Fin|8|🟢 Verdictparprofil etguideVRAM18janvier déjà publié le25, cohérent.|

Total onzeaxes79/110≈7,2/10. AxesS sans doublepondération.

## Corrections avec réécritures

### La preuve du hook doit garder son opération exacte

> « gagne jusqu’à63% en lecture de prompt »

Il s’agit d’un débit de préremplissage, sur9B/SteamDeck/Vulkan selonF4. Préparationlogicielle etchangementd’application sont des opérations différentes. Garder cette distinction dans legraphique etla voix, une fois clairement.

**Réécriture2 :** « Le63% concerne le débit de lecture du prompt sur leSteamDeck. Pour la vitesse d’écriture surWindows, cette étude ne donne pas le même résultat. Donc on conserve le matériel etl’opération à côté du chiffre. » Pas de raccourci «63%plusrapide » isolé.

### Le milieu démontre quatre fois qu’il n’y a pas de gagnant universel

> « Mais ça ne prouve pas que llama.cpp sera toujours le plus rapide… »
> « aucun duel contrôlé… un vainqueur général »
> « elle ne suffit pas à fabriquer ce podium »
> « le changement vise cette fonction ».

Toutes sont justes, mais l’idée n’évolue plus. Regrouper les limites du comparatif, puis revenir au choix. La meilleure conséquence est le besoin d’une fonction précise, pas une nouvelle dénégation de podium.

**Réécriture3 :** « Du coup, une comparaison utile garde le même fichier, le contexte et le matériel. Les sourcesWindows retenues n’alignent pas ces conditions pour les troisoutils. On peut cependant choisir une fonction : retrouver ses modèles, accéder directement aux paramètres, ou connecter uneapplication déjàcompatible. » F1–F5/F10.

### L’API doit répondre à un usage avant de devenir une liste

> « Ollama documente des API compatibles… LMStudio propose aussi… llama.cpp fournit lui-même… »

Le recoupement est utile, mais ressemble à un tableau lu. Partir de l’application déjàutilisée, puis révéler que les trois peuvent offrir un serveur.

**Réécriture4 :** « Ton outil de code attend un serveur local ? Les trois projets en proposent un. Donc la différence utile devient le format attendu, les fonctions dont ton outil a besoin et le modèle qui doit les exécuter. Si tonapplication est déjà configurée pourOllama, conserver cette connexion peut simplifier le choix. » F1–F3. Ne pas prétendre que les trois implémentent chaque protocoleàl’identique.

### Strata ne doit pas devenir une quatrième promesse vague

> « Il peut donc devenir une autre piste quand le type de modèle et la répartition du travail motivent ce choix. »

L’idée est prudente mais abstraite. Dire directement que la compatibilité du modèle et la quantité deRAM sont les deuxconditions àconserver, puis renvoyer au dossierStrata. Aucun débit ajouté sanslesconditions duCoder allégé.

## Faits et limites conservés

- F1 : LMStudio interface, serveurlocal etCLI ; GGUF/llama.cpp etMLXsurAppleSilicon distincts. Pas deMLXWindows suggéré.
- F2/F3 : Ollama possède des intégrations, llama.cpp serveur etinterfaceweb ; ne pas figer les outils dans un clichéGUI/terminal.
- F4 : étude17/09, jusqu’à63%préremplissage9B surDeck ; configurationsfixées par le protocole, pas versions dujour. Une seulecampagne, aucune secondeéquipe reproduisant le gain.
- F5 : meilleurescellules7,62/6,12 dans des conditionsdifférentes, nonutiliséescommeclassement : bonchoix.
- F6 : versionsobservées16/11 danssources ; ne pas les présenter commeversionsjanvier. L’interfacewrapper peut employer uneversionmoteur distincte.
- F7 : connexionClaudeCode documentée côtéoutils, supportAnthropicnonClaude absent. Ne pas rendre ce point pluslarge qu’il n’est.
- F9 : fichiersprésents etfonctionslocales pourhorsligne ; fonctionnalitéscloud/recherche séparées.
- F8 : Strata compatible avec certainsmodèles etmatériels, jamaisuniversel surpetitecarte.
- F10 : absence de comparatifcontrôlé reconnue ; cette recherche bornée n’affirme pas qu’aucunbenchmark de ce genre n’existe au monde.

## Oralité et anti-IA

1461mots≈10:05, horsbalises/titres/notes.15liaisons strictes :donc10,enfait2,ducoup2,parcontre1, soit1,03/100. Ajouter des raccords où l’obstacle oula conséquence change réellement, après coupes. Éviter une accumulation artificielle en tête de chaque paragraphe.

Aucune fausseanecdote ni nomdechaîne envoix. Les limites “pas surWindows”, “pas en génération” sont indispensables. Les fausses oppositions “ce n’estpasA,c’estB” ne sont pas nécessaires pour expliquer les fonctions. Nettoyer les balisesetnotes concaténées, et conserver desespaces autourdes unités.

## À garder

« llama.cpp… une interface web intégrée » : petite surprise directementutile.

« le contexte réellement conservé » : critère plusutile qu’une simplecapture de tokens/s.

Les troisprofils finaux : ils répondent précisément au titre sansvendre de performanceinventée.

## Plan d’action

1. Clarifier le sujet du63% etson lienavec lechoix ; garder question<30s.
2. Réduire les répétitions de limitesbenchmark, revenirplusvite aux fonctions concrètes.
3. Réécrire le passageAPI depuis l’applicationàbrancher ; Strata conditionnéàsesmodèles etRAM.
4. Raccords orauxvariés, nettoyage, compte ettimecodes recalculés, TPconcordant.
5. Maintenir versionsdatées, pas de classementWindows nonétabli, aucun nouveau test niinstallation demandé.

## Corrections appliquées par le rédacteur

Traçabilité : les 1 461 mots et 15 liaisons de l’audit correspondent à la version lue par le reviewer avant le nettoyage réalisé en parallèle. La V1 sur disque à la fin de ce nettoyage comptait 1 472 mots et 24 liaisons. Elle est désormais conservée ; les changements suivants figurent seulement dans script.md.

Hook centré sur le débit de lecture du 9B sur Steam Deck et la préparation Vulkan ; aucune comparaison implicite de génération Windows. Réserves de classement condensées, usage du serveur expliqué depuis l’application à brancher, Strata conditionné au modèle et à la RAM. Visuels et notes espacés, aucun test demandé.

Contrôle final : 1502 mots, 10:22 à 145 mots/min ; hook 59 mots, 24.4 secondes ; 27 liaisons strictes, 1.80/100. Timecodes calculés et téléprompteur concordants.

Cohérence calendrier : renvoi vers la publication suivante corrigé. Compte final actualisé : 1511 mots, 10:25, 1.79 liaisons/100 ; fin du tableau et téléprompteur régénérés.

Dernier contrôle ciblé : renvoi petits modèles spécialisés et raccords variés pour moteur ; CTA exact après prévention d’achat pour VRAM. 1507 mots, 10:24, 1.66 liaisons/100. Tableau et téléprompteur recalculés.

Dernier contrôle ciblé : renvoi petits modèles spécialisés et raccords variés pour moteur ; CTA exact après prévention d’achat pour VRAM. 1507 mots, 10:24, 1.66 liaisons/100. Tableau et téléprompteur recalculés.

Dernier contrôle ciblé : renvoi petits modèles spécialisés et raccords variés pour moteur ; CTA exact après prévention d’achat pour VRAM. 1507 mots, 10:24, 1.66 liaisons/100. Tableau et téléprompteur recalculés.
