# Grill indépendant — RAM, VRAM et mémoire unifiée

Revue du 16/11/2026, V1 et sources F1–F9, recoupement avec `projets/strata-test/sources.md` T6/T7. Méthode `ressources/skills-gpt/youtube-script-grill.md`, mode B, onze axes et variante storytelling. Aucun essai personnel requis.

## Verdict : 7,0/10

Le calcul capacité/débit constitue une bonne colonne vertébrale. Les mesures hétérogènes restent distinctes et le texte ne transforme pas 89,6 ÷ 17 en benchmark. **Le résultat de 70,4 tok/s doit cependant nommer la version Coder allégée** : l'architecture de répartition n'explique pas seule ce qu'un gros modèle peut faire sur 32 Go. La longueur est adaptée ; le milieu manque de décisions et de raccords oraux. Moyenne : 77/110, soit 7,0. Les S ne sont pas comptés une seconde fois.

## Test des trente secondes

| Tranche | Citation | Évaluation |
|---|---|---|
| 0–5 s | « Un utilisateur fait écrire un gros modèle local… » | Sujet concret ; nommer la version allégée avant que l'exemple devienne représentatif du modèle entier. |
| 5–15 s | « … environ 70 tokens… 16 gigas et 32 gigas de RAM » | Meilleur résultat tôt, génération identifiable, configuration visible. |
| 15–30 s | « Ces chiffres sont les leurs… faut-il plus de RAM, plus de VRAM… ? » | Attribution, absence de test et question unique dans le budget. |
| Pont | « … ajouter de la RAM peut laisser ta réponse presque aussi lente » | Boucle utile, mais déjà partiellement résolue au paragraphe suivant. La prolonger par le cas dense puis le cas experts. |

Ouverture : **62 mots, 25,7 secondes** à 145 mots/min. Six contrôles : sujet/tension oui ; meilleur moment oui ; question unique oui ; deuxième boucle oui ; chaque phrase utile partiellement (« servir à autre chose qu'attendre » est vague) ; trente secondes oui. Pas d'introduction à ajouter.

## Tableau de bord

| Axe | /10 | État | Diagnostic |
|---|---:|---|---|
| 1. Promesse | 7 | 🟠 | Le titre prudent « aide vraiment » est servi ; « laquelle est la plus rapide » ne serait pas démontré. |
| 2. Alignement | 8 | 🟢 | L'achat utile dépend du fichier et du trajet ; pas de consommation forcée. |
| 3. Problème profond | 8 | 🟢 | Dépenser pour des gigas qui ne raccourcissent pas l'attente. |
| 4. Public/complexité | 7 | 🟠 | Réservoir clair ; experts, cache et table SSD rapprochés demandent une hiérarchie. |
| 5. Valeur/originalité | 8 | 🟢 | Calcul pédagogique, limites explicites et mémoire unifiée sans faux classement. |
| 6. Structure/transformation | 7 | 🟠 | De « davantage de Go » à « capacité et trajet » ; dernier tiers parfois inventaire. |
| 7. Histoire | 7 | 🟠 | Le 70 initial revient ; le modèle Coder doit devenir un personnage précisément identifié. |
| 8. Mais/donc | 7 | 🟠 | Dense → MoE change la décision ; mémoire unifiée → SSD est surtout un ajout de sujet. |
| 9. Engagement actif | 6 | 🟠 | Question d'achat initiale ; peu de prédictions intermédiaires. |
| 10. Oralité/liaisons | 5 | 🟠 | 15 liaisons strictes/1 561 mots = 0,96/100 ; avec quatre « mais », 1,22. |
| 11. Tics d'IA | 7 | 🟠 | Peu de métadiscours ; conseil caricatural « tout ira deux fois plus vite » à couper. |
| S1. Trente secondes | 8 | 🟢 | Budget tenu ; identité du résultat à préciser. |
| S2. Pont | 7 | 🟠 | Deuxième question pertinente, réponse déjà annoncée. |
| S3. Retournements | 6 | 🟠 | Les réserves sur la division et les profils d'achat dépassent parfois une minute sans changement réel. |
| S4. Planté/récolté | 8 | 🟢 | Retour aux 70 tok/s et au réservoir ; payoffs présents. |
| S5. Personnages/enjeu | 7 | 🟠 | Acheteur et testeur réels ; pas d'expérience inventée. |
| S6. Fin | 6 | 🟠 | Trois critères utiles ; renvoi du 18 janvier futur et CTA achat à harmoniser. |

## Le grill et quatre réécritures ciblées

### 1. Identifier le modèle qui rend possible le chiffre initial

> « Ce qu'elle montre, c'est qu'un gros fichier réparti intelligemment peut devenir utilisable avec une carte de joueur. »

La mesure T7 concerne **Coder IQ1_M**, configuration expérimentale, médiane de trois chats courts, réflexion coupée, sans vérification de justesse. T6 décrit une version Coder allégée de moitié. « Utilisable » généralise une vitesse à un usage satisfaisant. Garder le nom exact au visuel et dire l'allégement à la voix.

**Réécriture 1 :**

> Le résultat de 70 tokens vient d'une version Coder allégée, en IQ1_M. Elle répartit ses données entre la carte, la RAM et le disque avec Strata. Donc ces 32 gigas rendent cette configuration possible ; la vitesse publiée ne nous dit pas encore si ses réponses sont assez justes pour ton travail.

À l'ouverture, remplacer simplement « un gros modèle local » par « une version Coder allégée d'un gros modèle local ». Ne pas transformer le gain en propriété de tous les MoE.

### 2. La mémoire stocke ; le processeur calcule

> « La RAM sert alors à faire tenir l'ensemble, tout en participant au calcul. »

La formulation brouille la distinction que la vidéo enseigne. Le paragraphe précédent attribue correctement le calcul au CPU ; maintenir cette précision.

**Réécriture 2 :**

> La RAM garde les experts qui ne sont pas sur la carte, et le processeur calcule leur partie. Le logiciel doit donc organiser deux chemins de calcul, avec des vitesses et des échanges différents.

### 3. Remplacer le faux conseil par une situation qui change l'achat

> « C'est pour ça qu'un conseil comme “ajoute 32 gigas et tout ira deux fois plus vite” est trop court. »

Aucun auteur ne défend ce conseil dans les sources. La situation suffit ; pas besoin d'un adversaire commode.

**Réécriture 3 :**

> Alors, que changent 32 gigas de plus ? Si le système devait relire le disque faute de place, ils peuvent supprimer cette attente. Si les mêmes poids étaient déjà en RAM, tu gardes le même débit de mémoire. Le panier se ressemble, le gain possible change complètement.

Question active, réponse immédiate et aucune demande d'essai au spectateur.

### 4. Raccorder les architectures au besoin avant la liste finale

> « Le SSD mérite aussi sa place dans le schéma. »

Transition de catalogue. Donner une conséquence au changement de chemin avant d'introduire un quatrième composant.

**Réécriture 4 :**

> Il reste un cas où la réserve déborde : le disque entre dans le trajet. En fait, une lecture prévue par le moteur et des pages récupérées faute de RAM peuvent produire de l'activité disque pour deux raisons différentes. C'est cette raison qui détermine si acheter de la mémoire aidera.

Conserver ensuite l'exemple précis de table SSD, sans répéter toute la liste des composants.

## Faits, durée et oralité

- **1 561 mots, 10:46** hors balises et crochet. Repères en tête indicatifs, à recalculer après coupes ; pas de durée mesurée au chronomètre.
- F1 : 5 600 × 8 × 2 = 89,6 Go/s théoriques ; ce n'est pas un débit soutenu mesuré. F2 : 960 Go/s annoncés pour la 5080, pas un débit de génération.
- F4 : 89,6/17 = 5,27, arrondi « environ 5 » correct. Fichier hypothétique, conversation unique, pas de coût supplémentaire : conditions bien dites. Ne pas laisser croire que 17 Go tiennent dans les 16 Go de la 5080.
- F5 : 13 →42 change aussi le fichier et les réglages ; réserve causale bien conservée.
- F6/T7 : afficher Coder IQ1_M, Strata 0.1.55/moteur 0.1.54, 5070 Ti, Ryzen 7 9700X, environ 32 Go, médiane de trois essais et réflexion coupée. Le chiffre n'évalue pas la qualité ; mentionner la version allégée en voix et en source.
- F3 : 307 Go/s concerne M5 Pro ; aucune généralisation à toutes les mémoires unifiées. Les ressources partagées avec l'OS sont bien rappelées.
- Liaisons strictes : donc 7, du coup 3, en fait 1, sauf que 1, par contre 2, voilà pourquoi 1. Ajouter des raccords causaux utiles, pas un « donc » automatique par paragraphe.
- Les vrais déplacements de sens sont capacité → débit, dense → experts, GPU seul → CPU/GPU, mémoire unifiée → réserve partagée, disque prévu → débordement. Les rapprocher à 25–35 s quand le raisonnement le permet ; les réserves successives ne sont pas autant de retournements.
- Le CTA achat demandé peut reprendre « Si cette vidéo t'a évité un mauvais achat, abonne-toi ». Le 18 janvier est postérieur à cette vidéo du 31 décembre : annoncer « dans la vidéo prévue… », pas une vidéo déjà disponible. Le 4 janvier est un Radar sans sujet défini ; ne pas inventer son contenu.

## À garder

> « La capacité, c'est la taille de la réserve. Le débit… »

Deux notions visualisables, sans fausse mesure.

> « Le fichier et les réglages ont aussi changé… »

Une réserve précise qui protège la comparaison 13/42.

> « Une machine annoncée avec 64 gigas ne promet pas 64 gigas entièrement libres… »

Conséquence d'achat réelle, pas une opposition artificielle.

## Plan d'action

1. Nommer Coder allégé et IQ1_M ; remplacer « utilisable » par ce que prouve la vitesse.
2. Attribuer le calcul au CPU et retirer le conseil caricatural sur le doublement.
3. Raccorder SSD et profils au problème de débit ; ajouter une question active au milieu.
4. Améliorer les liaisons, recompter durée et timecodes, harmoniser le CTA achat.
5. Marquer le renvoi au 18 janvier comme futur. Après ces corrections, pas de besoin de nouveau test ni de capture.

## Corrections appliquées par l’agent principal

Coder allégé identifié dès le hook et IQ1_M au visuel ; F10 ajouté par réemploi explicite du dossier Strata T6/T7. La RAM stocke, le CPU calcule. Faux conseil de doublement supprimé ; SSD relié au trajet des données ; question active sur32Go supplémentaires. CTA achat exact demandé rétabli ; renvoi18janvier futur.

Final :1587mots,10:57 à145mots/min ;29liaisons selon la liste du contrôle final (incluant imagine etparceque), soit1,83/100. Timecodes calculés sur la voix et téléprompteur dérivé. La note7,0 demeure celle de laV1.


## Contrôle indépendant ciblé de la version corrigée

Lecture du `script.md` corrigé le16/11 : Coder allégé dès le hook et IQ1_M au visuel ; distinction vitesse/qualité maintenue ; CPU et RAM ont leurs rôles exacts ; faux conseil de doublement retiré ; passage SSD relié au trajet ; renvoi18janvier explicitement futur et CTA conforme au prompt. Aucun nouveau problème matériel repéré sur ces points. Les métriques finales ci-dessus restent celles du calcul de production ; la note7,0 décrit la V1, sans rehaussement automatique.
