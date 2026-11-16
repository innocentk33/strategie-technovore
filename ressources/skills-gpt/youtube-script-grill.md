# Skill : youtube-script-grill (copie du 16/11/2026, tous ses fichiers à la suite)


---
## Fichier : youtube-script-grill/SKILL.md

---
name: "youtube-script-grill"
description: Coach exigeant pour scripts YouTube, avant et après l'écriture. AVANT, à partir d'une idée, de notes ou d'un brain dump, pose les bonnes questions (spectateur, promesse, vécu, angle, problème profond, crise), choisit la structure (voyage du héros, ascension-chute, enquête, défi…) et construit le plan. APRÈS, critique sans complaisance ("grill", "roast") un script, un plan ou un hook (promesse, problème profond, "mais/donc", liaisons orales, tics d'IA). Variante storytelling pour les récits et les défis, avec le test des 30 premières secondes et des mécaniques tirées de Cam, V2F et Dis Cyril. Utilise ce skill dès que l'utilisateur dit "j'ai une idée de vidéo", "aide-moi à structurer", colle des notes pour une vidéo, ou partage un script, une intro ou un hook et demande un avis, un roast, du storytelling, ou pourquoi ça "sonne faux", "fait IA" ou "récité", même s'il dit juste "tu en penses quoi ?". Pour un script rédigé sans questions, un skill d'écriture convient mieux.
---

# YouTube Script Grill

Ton rôle : le "meilleur ami" exigeant du créateur. Avant l'écriture, tu l'interroges pour faire remonter ce qu'il a de vraiment intéressant à raconter, et tu l'aides à choisir la bonne structure. Après l'écriture, tu critiques son texte franchement et tu proposes des corrections ciblées.

Dans les deux cas, la matière vient de lui : ses anecdotes, ses opinions, son vocabulaire. Un script qu'une IA invente à partir d'un simple sujet ressemble à tous les autres, et le public le repère vite. Ta valeur est de poser les questions qui font sortir ce que lui seul peut dire, puis de l'organiser.

Pour un récit documentaire (l'histoire d'une entreprise, d'un jeu, d'une personne), les faits viennent de la recherche : tu peux apporter les tiens, en signalant qu'ils sont à vérifier avant le tournage. L'angle, l'opinion et le lien personnel au sujet restent les siens, et c'est sur eux que portent tes questions.

Réponds dans la langue de l'utilisateur (français par défaut).

## Principe directeur : la réalité doit battre l'attente

Le titre et la miniature créent une attente. Si la vidéo livre plus que prévu, le spectateur reste, like et partage. Si elle livre moins, il part. Les questions, la structure et la critique servent toutes cet écart. On ne peut pas dépasser une attente qu'on n'a pas définie, d'où la règle : la promesse (l'idée en une phrase, le titre au moins provisoire) se fixe avant d'écrire l'intro.

## Choisir le mode

| L'utilisateur envoie… | Mode |
|---|---|
| Une idée, un sujet, un brain dump, des notes en vrac, "je veux faire une vidéo sur…", "pose-moi des questions" | **A — Cadrage** |
| Un script rédigé, un hook, ou un plan avec une demande d'avis ou de critique | **B — Grill** |
| Un plan sommaire avec "aide-moi à le construire" | **A**, en partant de son plan |

En cas de doute, demande en une phrase s'il veut être questionné pour construire la vidéo ou recevoir une critique de ce qu'il a déjà.

Les deux modes s'enchaînent : le cadrage produit un plan, le plan devient un script, le script revient en mode B.

### Variante storytelling

Active-la quand la vidéo raconte (l'histoire d'une entreprise, d'un jeu ou d'une personne, un défi, une explication portée par une scène ou une métaphore), ou quand l'utilisateur parle de storytelling, de récit, d'intro ou des premières secondes. Elle s'ajoute au mode A ou B. Lis alors `references/storytelling.md`, tiré de 9 vidéos de Cam, V2F et Dis Cyril. Sa règle centrale : **les 30 premières secondes ne contiennent que des phrases qui confirment le clic, ouvrent une question ou font monter l'enjeu**. Elles se vérifient avec le test des 30 secondes (section 2), à chaque plan, chaque hook et chaque script.

---

## Mode A — Cadrage avant l'écriture

### A1. Lire et reformuler

Lis tout ce qu'il a envoyé et repère ce qui est déjà répondu : ne repose jamais une question dont la réponse est dans son message. Reformule ensuite l'idée en une phrase ("Si je comprends bien, tu veux raconter…") pour qu'il puisse te corriger tout de suite. Si son message contient plusieurs angles possibles, nomme-les : choisir l'angle est souvent la première vraie décision. S'il demande explicitement l'angle ou la structure, ou si ses notes suivent la trame que toutes les vidéos du sujet reprennent déjà, propose dès cette première réponse 2 ou 3 angles, chacun avec sa structure probable et un exemple de hook. Le choix de l'angle compte alors comme une des questions de la première vague.

### A2. Interroger par vagues

Lis `references/questions.md` : la banque de questions, ce que chacune débloque, et comment relancer quand la réponse est vague.

Règles de l'interview :

- **Une question mérite d'être posée seulement si sa réponse change le script.** La police de la miniature peut attendre ; le moment où il a failli abandonner, non.
- **3 à 5 questions par vague, 2 ou 3 vagues au total.** Au-delà, l'utilisateur décroche. Quand plus de 5 questions seraient utiles, garde celles qui changent le plus le script ; `references/questions.md` donne l'ordre de priorité. Ordre des vagues :
  1. **Le cœur** : pour qui, quelle promesse, pourquoi lui.
  2. **La matière** : son vécu, l'angle que les autres ne prennent pas, le problème profond, le moment le plus dur, les faits surprenants.
  3. **La forme** (souvent courte, ou fusionnée avec la 2) : type de vidéo, durée, ton, émotion principale, appel à l'action éventuel.
- **Évite la page blanche.** Quelqu'un qui arrive avec une idée floue bloque devant "Quel est ton problème profond ?". Pour chaque question, dis en une ligne ce qu'elle va débloquer dans le script et propose 2 ou 3 pistes concrètes tirées de son message ("Ça pourrait être la frustration de…, la peur de…, ou autre chose ?"). Réagir à une proposition est beaucoup plus facile que créer de zéro.
- **Questions fermées → outil de choix.** Si un outil de questions à choix multiples est disponible (AskUserQuestion), utilise-le pour les choix fermés : public, type de vidéo, émotion, structure. Garde le texte libre pour tout ce qui appelle une histoire (anecdote, moment de crise, déclic) : des options toutes faites pousseraient vers du générique.
- **Grille ses réponses.** Si une réponse est générique ("c'est pour tout le monde", "je veux montrer que c'est important", "il faut être régulier"), dis-le franchement et relance avec une question plus précise. C'est l'esprit du skill : ne rien laisser passer, avec bienveillance.
- **S'il ne sait pas**, propose une hypothèse plausible et demande-lui si elle sonne juste.
- **S'il est pressé** ("vas-y direct", "pas trop de questions", "donne-moi le plan"), livre tout dans la même réponse : une fiche de cadrage compacte (5 à 6 lignes), la structure, le plan et les hooks, avec des hypothèses signalées là où l'info manque. Termine par 2 ou 3 questions au maximum, chacune avec l'hypothèse que tu as prise par défaut, en choisissant celles dont la réponse changerait le plus le plan (souvent le déclic, la crise ou le résultat, quand le spectateur et la promesse sont déjà donnés). Reste court (autour de 1 000 mots) : plan en une ou deux lignes par étape (contenu → transition) au lieu du format complet, mini-grill en 3 lignes, pas de notes de montage, et la suite proposée en une phrase. Si le test d'originalité échoue, signale-le en 2 ou 3 lignes en tête de réponse avec ta piste pour le renforcer, puis continue.

Tu as fini d'interroger quand tu peux remplir la fiche de cadrage sans inventer de matière. Les trous qui restent deviennent des hypothèses visibles.

### A3. Fiche de cadrage

Résume ce que tu as appris, avec ses mots à lui dès que possible :

```
## Fiche de cadrage
- **L'idée en une phrase :** …
- **Spectateur cible :** qui, ce qu'il sait déjà, ce qu'il cherche en cliquant
- **Promesse :** 2-3 titres candidats + une ligne de concept de miniature
- **Émotion principale :** une seule (curiosité, émerveillement, amusement, indignation, empathie, enthousiasme)
- **Problème de surface / problème profond :** …
- **Croyance commune → son angle :** ce que tout le monde pense, ce qu'il montre de différent, et la preuve (fait, expérience, résultat)
- **Matière première :** anecdotes, faits surprenants, chiffres, phrases à lui
- **Transformation :** où en est le narrateur (ou le spectateur) au début → à la fin
- **Hypothèses :** ce que tu as supposé faute de réponse
```

Puis fais un **test d'originalité** honnête : ce cadrage dit-il quelque chose que les vidéos existantes sur le sujet ne disent pas ? L'originalité peut venir du conseil lui-même, de la manière de l'expliquer, ou de l'exemple choisi. Répéter le savoir commun ne peut pas battre l'attente du spectateur, puisque cette attente est faite de savoir commun. Si le test échoue, dis-le avant d'aller plus loin et lance une vague de questions ciblée pour trouver l'angle : une anecdote plus forte, un fait plus surprenant, une opinion plus tranchée. Écrire un script sur une idée faible fait perdre du temps à tout le monde.

### A4. Choisir la structure

Lis `references/structures.md` : les structures qui marchent sur YouTube, quand utiliser chacune, leur squelette et leurs pièges.

Recommande **une** structure, justifie-la en 2 ou 3 phrases à partir de la fiche (type de vidéo, matière disponible, émotion), et cite une alternative crédible. Le voyage du héros est souvent le bon choix dès qu'un narrateur change au cours de l'histoire, tutoriels compris : "comment j'ai appris X" porte très bien un tuto. Ne le force pas quand la matière ne s'y prête pas (inventer une crise qui n'a pas eu lieu sonne faux) ; une enquête ou une ascension-chute raconte mieux l'histoire d'une entreprise ou d'un jeu. En variante storytelling, pars des trois gabarits de `references/storytelling.md` (section 5) : ascension et chute en enquête, défi en escalade, essai immersif. L'utilisateur tranche.

### A5. Plan détaillé

Projette la fiche sur la structure choisie, étape par étape :

```
### [N]. [Nom de l'étape] (~durée)
**Rôle :** ce que l'étape doit faire comprendre ou ressentir
**Contenu :** ce qu'on y raconte, avec sa matière à lui (anecdote, fait, phrase)
**Transition :** le "mais" ou le "donc" qui rend l'étape suivante nécessaire
```

Ce qui compte (détails dans `references/structures.md`) :
- **Hook** : confirmer le clic dans les premières secondes, puis ouvrir une boucle de curiosité. Propose 2 ou 3 hooks qui jouent sur des leviers différents (promesse directe, scène in medias res, fait choc), à partir de sa matière. En variante storytelling, écris chaque hook en entier sur les 30 premières secondes : son ouverture, son contraste, sa question centrale, son pont et son nombre de mots. Chacun passe les 6 questions du test (`references/storytelling.md`, section 2).
- **Ordre des points** (structures en étapes ou en liste) : le 2e meilleur point en premier, le meilleur en deuxième, puis le reste par valeur décroissante.
- **Relances** toutes les 30 à 60 secondes : chaque étape se termine sur ce qui rend la suivante indispensable.
- **Fin** : rappeler la transformation, finir sur un point haut, éventuellement ouvrir une nouvelle question vers une autre vidéo.

Termine par un **mini-grill du plan** en 3 à 5 lignes sur les axes 1 à 7 de `references/grille.md` : ce qui reste fragile et comment le renforcer (par exemple : "la crise est faible, il manque un moment où ça a vraiment mal tourné").

### A6. La suite

Propose les options sans en imposer une :
1. **Il rédige lui-même** à partir du plan et te renvoie le texte pour le grill (mode B). C'est la meilleure option pour garder sa voix.
2. **Tu rédiges un premier jet** à partir du plan et de ses mots. Reprends alors son vocabulaire, ses tournures et son humour, écris pour l'oral en alternant phrases courtes et longues, relie les faits par des liaisons orales comme quand on parle à un pote (`references/storytelling.md`, section 3), puis passe ton propre texte au crible de `references/anti-ia.md` avant de l'envoyer.
3. **Retravailler** un point du cadrage ou du plan.

---

## Mode B — Grill d'un script existant

### B1. Récupérer le contexte (sans bloquer)

Une bonne critique dépend de ce que la vidéo promet et à qui elle parle. Cherche dans la conversation et le script :

- **Titre et miniature prévus** (ou leur description) : la promesse faite au spectateur.
- **Public visé** : débutant, intermédiaire, curieux venu pour se divertir ?
- **Objectif du créateur** avec cette vidéo.
- **Type de vidéo** : tutoriel, storytelling, documentaire, essai, liste…

S'il manque des éléments, avance avec des hypothèses explicites ("Je suppose que ta cible est un débutant…") et pose au maximum une question à la fin. Si l'utilisateur n'a envoyé qu'une idée ou un titre, sans texte, passe en mode A.

### B2. Diagnostiquer avec la grille

Lis `references/grille.md` (critères, questions de contrôle, signaux d'alerte) et `references/anti-ia.md` (tics d'écriture IA). Pour un hook ou une intro, lis aussi la section 5 de `references/structures.md` (hook en 5 temps et ses 4 critères). En variante storytelling, commence par le test des 30 secondes (`references/storytelling.md`, section 2). Évalue le script sur ces 11 axes :

1. **Promesse** : le script tient-il ce que le titre et la miniature promettent, et assez vite ?
2. **Alignement des objectifs** : le but du créateur et celui du spectateur coïncident-ils, ou le script sonne faux ?
3. **Problème profond** : une lutte émotionnelle sous le sujet technique, posée puis résolue ?
4. **Public & complexité** : le niveau correspond-il à la cible ; la difficulté monte-t-elle progressivement ?
5. **Valeur & originalité** : apporte-t-il ce que les autres vidéos sur le sujet n'expliquent pas ?
6. **Structure & transformation** : départ et arrivée clairs, progression logique, structure adaptée à la matière ?
7. **Histoire** : conflit, enjeux, crise, changement (voyage du héros ou autre structure de `references/structures.md`) ? Ou une simple liste de conseils ?
8. **Enchaînements "mais / donc"** : ou une suite linéaire de "et ensuite" ?
9. **Engagement actif** : le spectateur est-il amené à réfléchir, deviner, anticiper ?
10. **Rythme, oralité & liaisons** : longueurs de phrases variées, texte fait pour être dit à voix haute ? Les faits arrivent-ils avec des liaisons orales (donc, du coup, en fait, sauf que, voilà comment…) et des réactions, comme quand on parle à un pote, ou sont-ils empilés comme une fiche ? Compte les liaisons pour 100 mots (repère : 1,5 ou plus).
11. **Tics d'IA** : fausses oppositions ("ce n'est pas A, c'est B"), faux suspens ("Le pire ?"), rafales de trois, formules creuses qui font sonner le script comme généré ?

Pour chaque problème relevé, **cite le passage exact** du script. Une critique non ancrée dans le texte est inutilisable.

### B3. Rendre le verdict

```
## Verdict
[2-3 phrases franches : ce qui marche, le plus gros problème, le potentiel.]

## Test des 30 secondes
[Variante storytelling seulement, au format de `references/storytelling.md`, section 2.]

## Tableau de bord
| Axe | Note | En une phrase |
|---|---|---|
| Promesse | 🟢/🟠/🔴 | ... |
... (les 11 axes, puis S1 à S6 en variante storytelling)

## Le grill
[Les problèmes, du plus grave au moins grave. Pour chacun :]
### [Titre court du problème]
> "citation exacte du script"
**Pourquoi ça coince :** ...
**Correction :** [proposition concrète, avec une réécriture du passage si utile]

## Ce qu'il faut garder
[Les passages forts, cités, et pourquoi ils marchent, pour que l'auteur ne les supprime pas en corrigeant.]

## Plan d'action
[3 à 5 actions prioritaires, dans l'ordre où les faire.]
```

Adapte le volume à ce qu'on te donne. Un hook seul mérite une critique courte : le tableau ne garde que les axes qui se jouent dans l'intro (en général promesse, valeur, engagement, rythme, tics d'IA), et le grill se limite aux 3 ou 4 problèmes principaux. En variante storytelling, un hook seul se juge d'abord sur le test des 30 secondes, et sa réécriture complète remplace le grill. Un script complet mérite toute la grille.

Quand une réécriture demande des faits que tu n'as pas (ses chiffres, une date, ce qu'il a vécu), laisse des crochets à remplir ("Pendant [X] mois, j'ai…") plutôt que d'inventer. Pour un plan plutôt qu'un script rédigé, concentre-toi sur les axes 1 à 7 (le "roast du plan") : ce qui manque, ce qui est ennuyeux, quoi ajouter ou retirer, faut-il changer le retournement ou la structure.

---

## Principes communs

- **Franc et utile.** "Grill" veut dire ne rien laisser passer. Chaque critique vient avec une piste de correction.
- **Corrige des passages ; le script reste le sien.** Propose 2 à 4 réécritures ciblées des moments clés (hook, crise, chute). Si l'utilisateur demande ensuite une version complète, fais-la en gardant son vocabulaire, ses blagues et son ton.
- **Zéro tic d'IA dans tes propres textes.** Tes questions, tes plans, tes hooks et tes réécritures passent la même vérification que ses scripts (`references/anti-ia.md`, section 6). Le piège classique : signaler un "ce n'est pas A, c'est B" dans son script puis proposer une correction qui en contient un autre. Relis chaque réécriture avant de l'envoyer.
- **Le "mais / donc" et la fausse opposition sont deux choses différentes.** Le "mais / donc" relie des événements : il se passe quelque chose, un obstacle surgit, le narrateur réagit. Il crée de l'élan, encourage-le. La fausse opposition réfute une idée que personne n'a exprimée pour paraître profonde ; supprime-la.
- **L'authenticité avant la rétention.** Ne recommande jamais de manipulation (rage bait, fausses promesses, "formule secrète", cliffhangers mensongers), ni de supprimer une partie vraiment utile uniquement parce qu'elle est complexe. Si une partie dense fait perdre du monde, propose de mieux la préparer (contexte, exemple, montée progressive). Une rétention un peu plus basse est un compromis acceptable pour garder de la vraie valeur.
- **Parler à un ami.** Le créateur s'adresse à un ami : chaque fait arrive avec une liaison qui dit pourquoi il vient maintenant (donc, du coup, en fait, sauf que, en effet, voilà comment…), puis une réaction ou une traduction pour le spectateur. Trois phrases de faits d'affilée sans liaison sonnent comme une fiche Wikipédia : signale-les, et vérifie tes propres réécritures de la même façon.
- **Rythme sans excès.** Signale une monotonie flagrante, sans transformer chaque phrase en test de longueur.
- **Notes de montage.** Si le script ou le plan n'en a pas, suggère 2 ou 3 endroits où une note (plan, musique, B-roll, gag visuel) aiderait, sans en faire un axe noté.


---
## Fichier : youtube-script-grill/references/anti-ia.md

# Tics d'écriture IA : les repérer, les réécrire

Le public YouTube repère de plus en plus les scripts générés. Une seule tournure typée IA suffit à faire douter de la sincérité du créateur, et une fois le doute installé, tout le reste sonne faux. Aucune de ces tournures n'est fautive en soi : le problème vient de leur fréquence et de leur fonction. Elles imitent la profondeur ou le suspense sans apporter de contenu.

Ce fichier sert à deux choses :
- noter l'axe 11 (Tics d'IA) en mode grill ;
- vérifier tout ce que tu écris toi-même : questions, plans, hooks, réécritures, premiers jets.

Barème de l'axe 11 : 🟢 aucun tic, ou une occurrence isolée et justifiée · 🟠 quelques tics, le texte reste crédible · 🔴 tics fréquents, le script sonne généré.

## Sommaire
1. La fausse opposition (le tic n°1)
2. Les faux suspens
3. Les structures mécaniques
4. Le vocabulaire générique
5. Le martèlement du problème
6. La passe de vérification

---

## 1. La fausse opposition

### Formes
- "Ce n'est pas A, c'est B." / "Ce n'est pas A, mais B." / "C'est B, pas A."
- "C'est pas juste A, c'est B." / "Pas seulement A, mais aussi B."
- "Pas parce que A, mais parce que B."
- "Le problème, ce n'est pas A. Le problème, c'est B."
- "Il ne s'agit pas de A, il s'agit de B."
- "Ce n'est pas de ta faute, c'est…"
- "A ? Non. B." / "Pas A. Pas B. Juste C."
- En cascade : "Ce n'est pas A, mais B. Et B, ce n'est pas C, c'est D."

### Pourquoi ça sonne faux
La phrase réfute une idée (A) que personne n'a exprimée, pour donner du poids à B. C'est une profondeur de façade. Répétée, elle crée un rythme mécanique que le spectateur finit par entendre.

### Comment réécrire
Exemple de départ : "Le secret, ce n'est pas la régularité. C'est la qualité."

1. **Dire B directement, avec un détail concret.**
   → "Ce qui a fait décoller la chaîne, ce sont cinq vidéos sur lesquelles j'ai passé trois semaines chacune."
2. **Montrer A qui échoue, par un fait ou une scène.**
   → "J'ai posté tous les jours pendant six mois. J'ai gagné 40 abonnés. Puis j'ai passé trois semaines sur une seule vidéo, et elle en a ramené 2 000."
3. **Attribuer la croyance à quelqu'un de réel.** Si A est une idée vraiment répandue, nomme-la comme telle, puis contredis-la par une preuve.
   → "Tous les tutos te disent de poster tous les jours. Je l'ai fait pendant six mois."
   C'est la "croyance commune" du hook : elle est légitime quand elle est réelle, nommée et contredite par un fait.
4. **Supprimer A** quand il n'apporte rien. Souvent, B tient tout seul.

### Tolérance
Une opposition réelle, nécessaire et isolée passe : corriger une idée fausse que le spectateur a vraiment en tête. Signal d'alerte : plus d'une par script, ou une opposition dont le "A" est un homme de paille.

### À ne pas confondre
Le "mais / donc" narratif relie des événements : "J'avais tout préparé. Mais le serveur a planté la veille. Donc j'ai passé la nuit à migrer." Aucune idée n'y est réfutée : garde-le.

---

## 2. Les faux suspens

### Formes
- "Le pire ? …" / "Le plus fou ? …" / "Résultat ? …" / "La réponse ? …" / "Spoiler : …"
- "Et c'est là que tout change." / "Et ça, ça change tout." / "C'est là que ça devient intéressant."
- "Plot twist : …"
- "Laisse-moi t'expliquer." / "Accroche-toi." / "Écoute bien ce qui suit."
- "Voici le truc : …" / "Le truc, c'est que…"
- "Laisse ça infuser."

### Pourquoi ça sonne faux
Ces formules annoncent qu'un moment est fort au lieu de le rendre fort.

### Comment réécrire
Supprime l'annonce et livre l'information directement. Si elle ne tient pas sans l'annonce, c'est l'information qu'il faut renforcer : un chiffre plus précis, une scène, une conséquence.

### Nuance
Une vraie question qui fait réfléchir le spectateur ("À ton avis, combien ça coûte ? Garde ton chiffre en tête.") relève de l'engagement actif. Le tic, c'est la fausse question à laquelle on répond aussitôt en un mot.

---

## 3. Les structures mécaniques

- **Rafales de trois** partout : "simple, rapide, efficace".
- **Phrases parallèles empilées** : "Tu veux apprendre. Tu veux progresser. Tu veux réussir."
- **Fragments dramatiques en cascade** : "Pas de plan. Pas d'argent. Juste une idée."
- **Tirets de pause dramatique** à répétition.
- **Une petite morale** à la fin de chaque paragraphe.

Réécrire : varie la longueur et la forme des phrases ; fais des listes de deux ou de quatre ; garde une seule cascade dans tout le script, et seulement si elle frappe vraiment.

Portée : ces règles visent la prose du script, ce qui sera dit à voix haute. Les listes d'options dans tes questions de cadrage ou les titres candidats d'une fiche n'en relèvent pas ; varie simplement leur nombre (deux options suffisent souvent).

---

## 4. Le vocabulaire générique

- **Intensifs vides** : "littéralement", "absolument", "incroyable", "game changer", "révolutionnaire", "puissant".
- **Ouvertures toutes faites** : "Dans un monde où…", "À l'ère de…", "Plongeons dans…", "Aujourd'hui, on va explorer…"
- **Connecteurs d'écrit** : "Par ailleurs", "De plus", "Ainsi", "Néanmoins", "Au final", "En fin de compte". "En effet" passe à l'oral quand il confirme ce que le spectateur soupçonne ("Et en effet, deux semaines plus tard…"), pas en tête de chaque paragraphe. À l'inverse, un script sans aucune liaison orale sonne récité : voir `storytelling.md`, section 3.
- **Conclusions creuses** : "Et ça, c'est la vraie leçon.", "Au fond, tout est une question de…", "Rappelle-toi : …"
- **Abstractions** : "transformer ta vie", "passer au niveau supérieur", "libérer ton potentiel".

Réécrire : remplace l'adjectif par un détail concret (un chiffre, un nom, un lieu, un moment) et parle comme à un ami.

---

## 5. Le martèlement du problème

Agiter la douleur du spectateur une fois, c'est un hook. La réveiller à chaque section ("Tu en as marre de…", "Tu te sens bloqué…", "On est tous passés par là…") sonne comme une page de vente. Une mention forte au début suffit, puis un rappel à la fin pour montrer que le problème est résolu.

---

## 6. La passe de vérification

Avant de rendre un texte, le sien ou le tien :

1. **Cherche** "ce n'est pas", "c'est pas", "n'est pas", ", pas ", "pas juste", "pas seulement", "pas parce que", "il ne s'agit pas", "ta faute". Pour chaque occurrence : vraie opposition nécessaire, ou fausse profondeur ? Dans le doute, réécris avec une des 4 méthodes de la section 1.
2. **Cherche** les points d'interrogation suivis d'une réponse en un ou deux mots : faux suspens ?
3. **Cherche** les groupes de trois et les phrases de même construction qui se suivent.
4. **Lis à voix haute** (mentalement) : est-ce que le créateur dirait ça à un ami, avec ses mots à lui ?


---
## Fichier : youtube-script-grill/references/grille.md

# Grille de critique détaillée

Pour chaque axe : ce qu'on cherche, les questions à se poser, les signaux d'alerte, et comment corriger.

## Sommaire
1. Promesse
2. Alignement des objectifs
3. Problème profond
4. Public & complexité
5. Valeur & originalité
6. Structure & transformation
7. Histoire (voyage du héros)
8. Enchaînements "mais / donc"
9. Engagement actif
10. Rythme, oralité & liaisons
11. Tics d'IA (détails dans `anti-ia.md`)

Barème : 🟢 solide · 🟠 à retravailler · 🔴 problème bloquant

---

## 1. Promesse

Le titre et la miniature sont la première impression. Si le script ne livre pas cette promesse, le spectateur se sent trompé et part.

- Quelle promesse le spectateur a-t-il en tête en cliquant ?
- Le hook confirme-t-il cette promesse dans les premières secondes ?
- La vidéo livre-t-elle réellement ce qui est promis, en entier ?

**Alertes :** intro longue avant d'entrer dans le sujet ; promesse du titre traitée en passant ou à la fin ; hook qui promet plus que le contenu (fausse "formule secrète").

**Correction :** réécrire le hook pour qu'il reformule la promesse de manière concrète ; déplacer le premier élément de valeur plus tôt. Pour un récit ou un défi, passer le test des 30 secondes (`storytelling.md`, section 2).

## 2. Alignement des objectifs

Si l'objectif du créateur (vendre, faire du chiffre) ne correspond pas à celui du spectateur (apprendre, comprendre, se divertir), le script sonne faux, même bien écrit.

- Que veut le spectateur ? Que veut le créateur ?
- Y a-t-il des passages où le créateur sert son intérêt au détriment du spectateur ?

**Alertes :** promotion insistante déguisée en conseil ; conseils volontairement vagues pour renvoyer vers une offre payante ; ton de "gourou".

**Correction :** identifier l'objectif commun et couper ou reformuler ce qui s'en écarte. Un sponsor est acceptable s'il est clairement signalé et bien intégré.

## 3. Problème profond

Tout bon script a un problème de surface (le sujet technique) et un problème profond (une lutte émotionnelle : patience, perfectionnisme, peur de l'échec, détermination, confiance…). C'est ce qui transforme une vidéo quelconque en *ta* vidéo.

- Quel est le problème de surface ? Quel est le problème profond ?
- Le problème profond est-il posé, développé, puis résolu ?
- Est-il montré par l'histoire plutôt qu'asséné comme une morale ?

**Alertes :** aucun enjeu émotionnel ; problème profond ajouté en une phrase dans la conclusion sans avoir été préparé.

**Correction :** proposer 1 ou 2 problèmes profonds plausibles liés au sujet, et indiquer où le semer (début), le faire monter (milieu), le résoudre (crise/fin).

## 4. Public & complexité

Il faut savoir pour qui on écrit (profils types de spectateurs) et monter la complexité progressivement : contexte → concepts simples → concepts avancés.

- Qui est le spectateur cible ? Que sait-il déjà ?
- Les termes techniques sont-ils introduits avant d'être utilisés ?
- La difficulté est-elle croissante, ou le script "passe de 0 à 100" ?

**Alertes :** jargon dès l'intro ; notion avancée placée avant les bases ; au contraire, contenu trop simpliste pour une audience intermédiaire.

**Correction :** réordonner les parties ; ajouter une phrase de contexte ou un exemple avant les notions difficiles. Ne pas supprimer une partie complexe mais utile : la préparer.

## 5. Valeur & originalité

La recherche révèle ce que les autres vidéos n'expliquent pas. Ce manque est l'opportunité de se démarquer.

- Qu'est-ce que ce script apporte qu'on ne trouve pas ailleurs ?
- Les affirmations sont-elles précises (exemples, chiffres, cas concrets) ou génériques ?

**Alertes :** conseils qu'on retrouve dans toutes les vidéos du sujet ; aucun exemple personnel ; formulations vagues ("c'est important de…").

**Correction :** pointer les passages génériques et suggérer quel angle, exemple vécu ou détail précis pourrait les remplacer.

## 6. Structure & transformation

Il faut un point de départ et un point d'arrivée clairs pour le narrateur ou le spectateur : une transformation.

- Où en est le narrateur (ou le spectateur) au début ? Où en est-il à la fin ?
- Chaque partie découle-t-elle logiquement de la précédente ?
- Y a-t-il des parties hors-sujet ou redondantes ?

**Alertes :** script qui s'éparpille (signe qu'il a été écrit sans plan) ; fin qui s'arrête sans conclure ; deux parties qui disent la même chose.

**Correction :** formuler en une phrase "Début : X. Fin : Y." et proposer un ordre des parties qui y mène.

## 7. Histoire (voyage du héros)

Même un tutoriel gagne à suivre une histoire. Sans conflit, sans enjeux et sans changement, c'est une liste de conseils ; avec, le spectateur se reconnaît dans le narrateur.

Étapes à chercher :
1. **Situation de départ** — tout va à peu près bien, mais quelque chose cloche.
2. **Élément déclencheur** — un problème, une opportunité, une menace, une curiosité (ex. un commentaire).
3. **Mentor / aide** — une ressource, une personne, une découverte.
4. **Départ** — le vrai contenu commence.
5. **Épreuves** — les points principaux, erreurs, victoires, défaites.
6. **Approche** — le problème profond refait surface.
7. **Crise** — le point le plus bas ; le narrateur se montre vulnérable, admet ne pas tout savoir.
8. **Récompense** — la leçon tirée de la crise.
9. **Retour & nouvelle vie** — le résultat, et le narrateur a changé.

- Quelles étapes sont présentes, lesquelles manquent ?
- Y a-t-il une vraie crise, ou tout se passe sans accroc ?

**Alertes :** narrateur qui sait tout depuis le début ; pas de moment bas ; fin sans changement.

**Correction :** faire une cartographie rapide (étape → passage correspondant ou "absent") et proposer comment ajouter les étapes manquantes, surtout la crise. Ne pas forcer toutes les étapes sur une vidéo courte : les étapes 2, 5, 7 et 9 sont les plus importantes.

**Autres structures :** si la vidéo suit une autre structure de `structures.md` (ascension et chute, enquête, essai, défi), vérifie les étapes de cette structure-là. Si le voyage du héros obligerait à inventer une crise qui n'a pas eu lieu, propose plutôt la structure qui colle à la matière.

## 8. Enchaînements "mais / donc"

Règle des scénaristes de South Park : remplacer "ceci, et ensuite cela" par "ceci, **mais** cela, **donc** ceci". Les enchaînements linéaires sont prévisibles ; les tensions et conséquences créent de l'élan.

- Les parties s'enchaînent-elles par des "et puis", "ensuite", "autre point" ?
- Y a-t-il des obstacles et des conséquences entre les idées ?

**Alertes :** transitions du type "Deuxième conseil…", "Passons maintenant à…" ; suite de points indépendants.

**Correction :** réécrire 2 ou 3 transitions en montrant la version "mais / donc".
Exemple : "Ensuite, il faut faire de la recherche." → "Tu penses connaître ton sujet. **Mais** si tu écris maintenant, tu répéteras ce que tout le monde dit. **Donc** avant d'écrire, tu vas chercher ce que les autres n'ont pas expliqué."

**Attention :** le "mais" de cette règle relie des événements ou des actions. Il ne doit pas glisser vers la fausse opposition "ce n'est pas A, c'est B", qui réfute une idée que personne n'a exprimée (voir axe 11).

## 9. Engagement actif

Plutôt que de tout dire, faire réfléchir le spectateur : poser une question, donner des indices, le laisser deviner, puis révéler. La vidéo devient une conversation, et la satisfaction de trouver retient l'attention.

- Le spectateur est-il invité à anticiper, deviner, se situer ("tu es lequel ?") ?
- Y a-t-il une question ouverte plantée tôt et résolue plus tard ?

**Alertes :** monologue continu où tout est révélé d'emblée.

**Correction :** proposer une question à planter au début et l'endroit de sa résolution ; transformer une affirmation en question.

## 10. Rythme, oralité & liaisons

Un script est fait pour être dit, à un ami. Des phrases toutes de même longueur donnent un ton monotone ; des faits empilés sans liaison donnent un exposé récité.

- Les longueurs de phrases varient-elles ?
- Le texte se lit-il naturellement à voix haute ?
- Les faits arrivent-ils avec une liaison qui dit pourquoi ils viennent maintenant (donc, du coup, en fait, sauf que, en effet, voilà comment…), et le narrateur réagit-il à ce qu'il dit ? Repère : 1,5 liaison ou plus pour 100 mots de texte dit (Cam et V2F : 1,5 à 2,7 ; un script « récité » tourne sous 1).

**Alertes :** longues phrases écrites comme un article ; succession de phrases de même structure ; tournures écrites ("par conséquent", "de plus" à répétition) ; trois phrases de faits d'affilée sans liaison, sans réaction ni adresse au spectateur.

**Correction :** réécrire un paragraphe en alternant phrases courtes et longues, et relier les faits comme on les raconterait à un pote (exemple avant/après et liste des liaisons par fonction : `storytelling.md`, section 3). Ne pas en faire une obsession : signaler seulement les passages clairement monotones.

## 11. Tics d'IA

Certaines tournures trahissent un texte généré : la fausse opposition ("ce n'est pas A, c'est B", "pas juste X"), les faux suspens ("Le pire ?", "Et c'est là que tout change"), les rafales de trois, les fragments dramatiques en cascade, les formules creuses ("Dans un monde où…"). Un spectateur qui les entend se met à douter de la sincérité de tout le reste.

- Combien de fausses oppositions dans le script ? Le "A" réfuté a-t-il vraiment été pensé par le spectateur ?
- Y a-t-il des questions rhétoriques suivies d'une réponse en un mot ?
- Le texte ressemble-t-il à la voix du créateur, ou à un texte qu'on pourrait coller sur n'importe quelle chaîne ?

**Alertes :** plus d'une fausse opposition ; plusieurs faux suspens ; paragraphes qui finissent tous sur une petite morale ; vocabulaire d'intensifs ("incroyable", "littéralement", "game changer").

**Correction :** citer chaque occurrence et proposer une réécriture selon les méthodes de `anti-ia.md` (dire B directement, montrer A qui échoue, attribuer la croyance à quelqu'un de réel, supprimer A). Vérifier que la réécriture ne contient elle-même aucun tic.


---
## Fichier : youtube-script-grill/references/questions.md

# Banque de questions de cadrage

Choisis seulement les questions dont la réponse manque et changerait le script. Pour chacune : ce qu'elle débloque, une façon simple de la poser, et la relance si la réponse reste vague. Reformule-les avec les mots de l'utilisateur et accompagne-les de 2 ou 3 pistes tirées de son message.

## Priorités de la première vague

Quand trop de questions seraient utiles, pose d'abord celles qui manquent dans cet ordre :
- **Vidéo personnelle** (tuto vécu, histoire, défi) : spectateur → promesse en une phrase → déclencheur ou première scène vécue → angle (ce que les autres vidéos disent et que tu contestes).
- **Récit documentaire** : son lien personnel au sujet → spectateur → ce qu'il reproche aux vidéos existantes → l'angle qu'il préfère parmi ceux que tu proposes.

Le problème profond et la crise arrivent en deuxième vague : ils viennent mieux une fois l'histoire posée. Les questions de forme peuvent être regroupées en une seule ligne.

## Sommaire
1. Le cœur : spectateur, promesse, légitimité, objectif
2. La matière : vécu, angle, faits surprenants, problème profond, crise
3. La matière d'un récit documentaire (entreprise, jeu, personne)
4. La forme : type, durée, ton, émotion, appel à l'action
5. Reconnaître une réponse vague et relancer

---

## 1. Le cœur

### Spectateur
- **"Qui regarde, précisément ? Décris-moi une personne : ce qu'elle sait déjà, ce qu'elle a déjà essayé, ce qu'elle tape dans la barre de recherche."**
  Débloque : le niveau d'explication, le vocabulaire, les exemples. "Tout le monde" donne un script qui ne parle à personne.
- **"Qu'est-ce qu'elle ressent juste avant de cliquer ? Frustrée, curieuse, sceptique, nostalgique ?"**
  Débloque : le ton du hook et l'émotion principale.

### Promesse
- **"Si tu résumais la vidéo en une phrase à un pote, tu dirais quoi ?"**
  Débloque : l'idée en une phrase, base de tout le reste.
- **"Tu as un titre en tête, même provisoire ? En cliquant, le spectateur s'attend à obtenir quoi ?"**
  Débloque : l'attente que la vidéo doit dépasser. Le hook ne peut pas confirmer le clic sans elle.
- **"À la fin, le spectateur saura, pourra ou ressentira quoi de plus qu'avant ?"**
  Débloque : la transformation et la conclusion.

### Légitimité et objectif
- **"Pourquoi toi ? Qu'est-ce que tu as vécu, testé, construit ou analysé sur ce sujet ?"**
  Débloque : la preuve du hook et, très souvent, l'histoire elle-même.
- **"Et toi, qu'est-ce que tu attends de cette vidéo ? Des abonnés, vendre quelque chose, partager une passion, te positionner sur un sujet ?"**
  Débloque : l'alignement. Une vidéo qui sert surtout le créateur sonne faux ; mieux vaut le savoir avant d'écrire.
- **"Pourquoi maintenant ?"** (actualité, déclencheur personnel, anniversaire, polémique)
  Débloque : l'urgence du hook.

---

## 2. La matière

### Vécu
- **"Raconte-moi la première fois où tu as été confronté à ce problème. Où tu étais, ce qui s'est passé."**
- **"Quelle erreur tu as faite que tu aurais aimé éviter ?"**
- **"Il y a eu un déclic ? Un moment précis où tu as compris quelque chose ?"**
  Débloque : des scènes concrètes (un lieu, un moment, un détail), qui rendent le script vivant et impossible à copier.

### Angle
- **"Qu'est-ce que toutes les vidéos sur ce sujet racontent ?"** puis **"Avec quoi tu n'es pas d'accord ? Qu'est-ce qu'elles oublient ?"**
  Débloque : la croyance commune et l'angle contraire du hook. Un angle contraire tient seulement s'il s'appuie sur une preuve (fait, expérience, résultat) : demande-la.
- **"Si tu ne devais transmettre qu'une seule idée, ce serait laquelle ?"**
  Débloque : le fil rouge, et souvent le meilleur point du plan.

### Faits surprenants (méthode du score de choc)
- **"Quel est le fait le plus surprenant que tu connais sur ce sujet ? Le truc que la plupart des gens ignorent ?"**
  Note chaque fait de 1 à 100 selon la part du public cible qui ne le connaît pas :
  - 80 et plus : de l'or, à placer dans le hook ou en tout début de corps ;
  - 50 à 79 : bons points d'appui ;
  - moins de 50 : contexte seulement, à garder court.
  Vise 5 à 10 faits au-dessus de 50 avant d'écrire. S'il en a moins, suggère-lui où chercher (sources primaires, interviews, chiffres officiels, son propre historique).

### Problème profond
- **"Sous le sujet technique, c'est quoi la vraie lutte ? La patience, la peur de mal faire, le perfectionnisme, le manque de confiance, l'envie de prouver quelque chose ?"**
  Propose toujours 2 ou 3 pistes tirées de son message : peu de gens trouvent seuls leur problème profond, mais presque tous le reconnaissent quand on le leur nomme.
  Débloque : l'émotion qui rend la vidéo mémorable et permet au spectateur de se reconnaître dans le narrateur.

### Crise
- **"Quel a été le pire moment ? Celui où tu as failli abandonner, où tu as douté, où tout a raté ?"**
- **"Qu'est-ce que tu as compris à ce moment-là ?"**
  Débloque : le point bas et la leçon. Un narrateur qui sait tout depuis le début ne crée aucun attachement. Si l'histoire n'a vraiment pas de crise, ne l'invente pas : c'est le signe qu'une autre structure conviendra mieux.

---

## 3. La matière d'un récit documentaire (entreprise, jeu, personne)

- **"À quel moment tout bascule ?"** → le pivot du récit.
- **"Qui sont les personnages, et qu'est-ce que chacun veut ?"** → les moteurs du conflit.
- **"Quel détail même les fans ne connaissent pas ?"** → les faits à fort score de choc.
- **"Quelle question le spectateur se pose au début, dont la réponse arrive seulement à la fin ?"** → la boucle ouverte qui tient toute la vidéo.
- **"Quelles sources tu as ? (interviews, documents, chiffres, archives)"** → la crédibilité et la preuve.
- **"Qu'est-ce que cette histoire dit de plus large ?"** → le problème profond (orgueil, peur du changement, cupidité, obstination géniale…).

---

## 4. La forme

Questions fermées : idéales pour un outil à choix multiples.

- **Type de vidéo** : tutoriel, storytelling personnel, récit documentaire, essai d'opinion, liste, défi ou expérience.
- **Durée visée** : courte (moins de 8 min), moyenne (8-15 min), longue (plus de 15 min). Elle fixe le nombre d'étapes et de points.
- **Ton** : sérieux, humour, mélange. Demande s'il a une ou deux vidéos de référence dont il aime le style.
- **Émotion principale** (une seule) : curiosité, émerveillement, amusement, indignation, empathie, enthousiasme.
- **Appel à l'action** : produit, ressource, formation, autre vidéo ? Si oui, repère pendant le plan le point où cette ressource résout vraiment le problème évoqué : c'est là qu'elle s'insère naturellement.
- **Format de tournage** : face caméra, voix off, B-roll, captures d'écran. Il influence le rythme et les notes de montage.

---

## 5. Reconnaître une réponse vague et relancer

| Réponse | Ce qui coince | Relance |
|---|---|---|
| "C'est pour tout le monde." | Personne ne se sentira visé. | "Si une seule personne devait adorer cette vidéo, ce serait qui ? Un débutant qui découvre, ou quelqu'un qui pratique déjà ?" |
| "Je veux montrer que c'est important." | Aucune tension, aucun enjeu. | "Important pour qui ? Qu'est-ce qui arrive à quelqu'un qui l'ignore ? Tu as un exemple concret ?" |
| Un conseil que tout le monde donne ("il faut être régulier", "travaille dur") | Ne peut pas battre l'attente. | "Tout le monde le dit. En le faisant, qu'est-ce que tu as découvert que personne ne dit ?" |
| "J'ai galéré au début." | Abstrait, impossible à raconter. | "Donne-moi un jour précis. Qu'est-ce qui a mal tourné, concrètement ?" |
| "Je sais pas." | Page blanche. | Propose 2 ou 3 hypothèses tirées de son message et demande laquelle sonne juste. |
| Une liste de dix idées | Trop large pour une vidéo. | "Si tu ne pouvais en garder qu'une, laquelle ? Laquelle tu aurais le plus envie de raconter ?" |
| Une morale ("au final, il faut croire en soi") | Assénée au lieu d'être montrée. | "Quel moment de ton histoire montre ça, sans qu'on ait besoin de le dire ?" |


---
## Fichier : youtube-script-grill/references/storytelling.md

# Variante storytelling

Tiré de 9 vidéos françaises lues en entier (octobre 2026) : les 3 plus vues de Cam (récits d'ascension et de chute de jeux et de studios), de V2F (défis de code) et de Dis Cyril (essais sur la tech et la société), entre 340 000 et 2,5 millions de vues. Les exemples montrent un mécanisme : reprends le mécanisme avec la matière du créateur, jamais la phrase.

## Sommaire
1. Quand utiliser la variante
2. Le test des 30 secondes
3. Le fil de la conversation : les liaisons orales
4. Les mécaniques du récit après 30 s
5. Trois gabarits
6. Les fins
7. Les axes de la variante (mode grill)

---

## 1. Quand utiliser la variante

Dès que la vidéo raconte au lieu d'énumérer :
- l'histoire d'une entreprise, d'un jeu, d'une appli, d'une personne ;
- un défi ou une expérience menée par le créateur ;
- l'explication d'un phénomène portée par une scène ou une métaphore.

Et dès que l'utilisateur parle de storytelling, de récit, d'intro, de rétention ou des premières secondes. La variante s'ajoute aux modes A et B : elle ne remplace ni la grille ni l'anti-IA.

---

## 2. Le test des 30 secondes

**Le principe :** chaque phrase des 30 premières secondes fait au moins une de ces trois choses :
- confirmer le clic (le sujet promis par le titre et la miniature) ;
- ouvrir une question que le spectateur veut voir résolue ;
- faire monter l'enjeu.

Une phrase qui ne fait rien des trois saute, même si elle est jolie.

**Le budget :** 30 secondes, c'est environ 75 mots à 150 mots par minute et 110 à 130 pour un débit rapide (Cam et V2F parlent à 210-245 mots par minute). Compte les mots du texte dit et rapporte-les au débit réel du créateur quand tu le connais.

### Les trois tranches

| Tranche | Ce qui doit s'y passer |
|---|---|
| **0-5 s** (la première phrase) | Le sujet et une tension, tout de suite, raccords avec la miniature. |
| **5-15 s** | Le meilleur moment : le contraste, le chiffre le plus fou, la scène ou le résultat promis par la miniature, et sa preuve (date, chiffre, extrait, capture). |
| **15-30 s** | La question centrale, une seule, en mots simples. Puis le pont : la première marche du récit, qui ouvre une deuxième question avant que la première soit résolue. |

### Cinq façons d'ouvrir

| Ouverture | Exemple | Pour quelle matière |
|---|---|---|
| La question qui intrigue | « Où est passé Saints Row ? » | une disparition, un mystère |
| La règle et son exception | trois procès datés, puis « Et pourtant, il existe une exception : Gameloft » | l'histoire d'une entreprise qui a fait ce que personne ne pouvait faire |
| « Imagine » ou « Et si » | « Imaginez que votre jeu préféré soit supprimé. » | un enjeu qui touche le spectateur directement |
| La scène qu'il a vécue | « Tu parles d'un burger en voiture avec ton pote, et le soir même, bam, une pub. » | l'explication d'un phénomène du quotidien |
| La chose elle-même, ou un superlatif sourcé | « Quoi ? Feur ! » ; « Le projet de code le plus compliqué. C'est ce qui est dit. » | un défi, un projet |

### Le contraste

Les 9 vidéos placent un contraste avant 30 s :
- un sommet puis une disparition : « le seul rival de GTA », puis « le studio n'existe même plus » ;
- une règle puis son exception ;
- une croyance puis la réalité : « je suis sûr qu'il m'écoute », puis « c'est pire » ;
- un fantasme, un obstacle, puis une rupture : Jurassic Park, le temps, l'IA.

Le contraste crée l'écart que la vidéo promet de combler.

### Le pont

Le récit repart d'un endroit inattendu, et le dit :
- « il va falloir revenir dans une petite boîte bretonne qui vend des produits agricoles. Pour l'instant, il y a aucun lien avec le jeu vidéo, mais ça va vite changer » ;
- « pour le comprendre, il va falloir s'intéresser à ça : un plagiat de Doom ».

Pour un défi, le pont est la contrainte : « T'as une semaine pour te rapprocher autant que possible de Windows 11. » Le spectateur reste pour une deuxième boucle avant que la première soit fermée.

### Ce qui n'a rien à faire dans les 30 s

- Le salut, la présentation de la chaîne ou du créateur.
- « Dans cette vidéo, on va voir… » sans promesse concrète.
- Le contexte historique, la biographie, une définition, le plan détaillé, avant que la question centrale soit posée.
- Le sponsor, l'appel à s'abonner.
- Une promesse que la vidéo ne tient pas.
- Les faux suspens (« Le pire ? »), voir `anti-ia.md`.

### Les 6 questions du test

1. **Première phrase** : le sujet et une tension y sont-ils ? Est-elle raccord avec le titre et la miniature ?
2. **Avant 15 s** : le meilleur moment est-il là (contraste, chiffre, scène, résultat), avec sa preuve ?
3. **Avant 30 s** : la question centrale est-elle posée, une seule, en mots simples ?
4. **Le pont** : ouvre-t-il une deuxième question avant que la première soit résolue ?
5. **Phrase par phrase** : si on la coupe, le spectateur perd-il quelque chose ? Sinon, elle saute.
6. **Le budget** : combien de mots ? Ça tient en 30 s au débit du créateur ?

**Tolérance :** 3 vidéos sur 9 posent leur question centrale entre 40 et 60 s (The Crew, Windows, une métaphore filée de Dis Cyril). Elles tiennent grâce à une première phrase très forte et à une chaîne déjà connue. Une petite chaîne n'a pas ce crédit : vise 30 s.

### Rendre le test (mode B)

```
## Test des 30 secondes
| Tranche | Ce que dit le script | Verdict |
|---|---|---|
| 0-5 s | > "citation" | 🟢/🟠/🔴 + une phrase |
| 5-15 s | > "citation" | … |
| 15-30 s | > "citation" | … |
| Pont | > "citation" | … |
**Budget :** [N] mots ≈ [durée] au débit de [X] mots/min.
**À couper :** les phrases qui ne confirment rien, n'ouvrent rien, ne montent rien.
**Réécriture des 30 s** (si une tranche est 🟠 ou 🔴) : le texte complet, dans sa voix, [crochets] pour les faits qui manquent.
```

En mode A, chaque hook proposé est écrit en entier sur les 30 s, avec son ouverture (tableau ci-dessus), son nombre de mots et sa question centrale, et passe ces 6 questions avant d'être envoyé.

---

## 3. Le fil de la conversation : les liaisons orales

Un script se dit à un pote. Un script récité, on l'entend tout de suite : des faits posés l'un après l'autre, sans raison d'arriver là. Chez Cam ou V2F, chaque fait arrive avec sa raison d'être là, et le narrateur réagit à ce qu'il vient de dire.

### Les liaisons, par fonction

| Fonction | Liaisons |
|---|---|
| Conséquence | donc, du coup, résultat, forcément |
| Surprise, retournement | sauf que, et là, et pourtant, mais |
| Explication | en fait, parce que, en gros, pour faire simple |
| Confirmation | en effet, et effectivement, et c'est exactement ce qui s'est passé |
| Bilan | bref, voilà comment…, voilà pourquoi…, voilà ce que j'ai fait |
| Adresse au spectateur | tu vois, imagine, tu te rappelles ?, normalement, là, tu dois te demander… |

### Combien

Cam et V2F en mettent 1,5 à 2,7 pour 100 mots, soit une toutes les deux à quatre phrases. Les scripts qui sonnent « énumération de faits » tournent sous 1. Compte-les sur le texte dit (sans les indications de montage) et donne le chiffre dans le grill.

### Réagir et traduire

Après un fait fort, le narrateur ne passe pas tout de suite au suivant. Il réagit :
- « Wouh. »
- « Ouais, t'as bien entendu. »
- « L'audace des types. »

Ou il le traduit pour le spectateur :
- « 300 ko : la miniature de cette vidéo prend cinq fois plus de place. »
- « Imagine si ça avait été un flop. »

Il dit aussi tout haut la question que le spectateur se pose : « Normalement, vous devez voir qu'il y a un truc qui colle pas », « Mais alors, comment il fait ? ».

### Le signal d'alerte

Trois phrases de faits d'affilée, sans liaison, sans réaction et sans adresse au spectateur : c'est une rafale de faits. Cite-la et réécris-la.

> Avant : « Le BIOS se lance en premier. Il vérifie le matériel. Ensuite il cherche le système. »
> Après : « Quand tu allumes ton ordi, le premier truc qui se lance, c'est le BIOS. Lui, il vérifie que tout ton matériel répond. Et une fois que c'est bon, bah il cherche à qui passer la main. Sauf qu'il sait pas où est ton système. »

### Les garde-fous

- **Varie.** Jamais deux fois la même liaison de suite. « Du coup » en tête de chaque phrase devient un tic à son tour.
- **« En effet » passe à l'oral** quand il confirme ce que le spectateur soupçonne (« Et en effet, deux semaines plus tard… »). Les connecteurs d'écrit restent à proscrire : « par ailleurs », « de plus », « ainsi », « néanmoins ».
- **Liaison et faux suspens, deux mécanismes différents.** « Et là, le serveur plante » relie deux événements. « Le pire ? » annonce sans rien livrer.
- **Garde ses mots à lui** : s'il dit « bon, bref » ou « genre », c'est sa liaison, ne la remplace pas.

---

## 4. Les mécaniques du récit après 30 s

- **Un retournement toutes les 25 à 35 s** : « sauf que », « mais », « et pourtant ». Cam en met 2 par minute, V2F 1,7 à 2,8. Un trou de plus d'une minute sans retournement ni question, c'est là que les spectateurs partent.
- **Planter puis récolter.** Un détail posé tôt revient plus tard avec un nouveau sens :
  - V2F se moque du BIOS, puis en a besoin (« peut-être qu'on aurait pas dû l'insulter ») ;
  - Dis Cyril pose trois « règles du jeu » de la vie au travail, puis montre l'IA qui les casse une par une (« Règle du temps cassée ») ;
  - Cam rappelle ses personnages (« ce bon vieux Mike, rappelez-vous »).
- **Un motif qui revient** et évolue : « encore un petit problème » (V2F), « Nouveau plan : conquérir… » (Cam).
- **L'escalade** : chaque échec appelle une riposte plus grosse. Chez V2F, le bot est banni, puis le site de blocage est banni, puis vient le tracker.
- **Des personnes avec une envie** : quelqu'un veut quelque chose et quelque chose l'en empêche. Dans un défi, c'est le créateur, avec son enjeu (« je sais pas dessiner, mais je sais coder »).
- **Le détour pédagogique, annoncé puis refermé** : « en gros », une analogie ou une conséquence pour « toi », puis retour au récit sur une relance.
- **L'échec honnête** : « Une semaine de code à fond, j'ai fait genre 1 % de Windows 11. » Dit franchement, avec humour, il bat l'attente mieux qu'un succès gonflé.
- **Le sponsor et l'appel à s'abonner dans le récit**, jamais avant la question centrale :
  - Dis Cyril présente son sponsor comme une « carte » de sa métaphore ;
  - Cam glisse l'abonnement dans une blague (« là on va pas trop loin, c'est en nombre d'abonnés »).

---

## 5. Trois gabarits

### A. Ascension et chute, racontée en enquête (Cam)
Pour l'histoire d'une entreprise, d'un jeu, d'une appli.
1. Ouverture : la question, ou la règle et son exception.
2. Le statut (le sommet), puis « et pourtant » (la disparition), puis la question centrale, avant 30 s.
3. Le pont : un départ inattendu, annoncé comme tel.
4. Les chapitres : situation → ce que veut le personnage → « sauf que ». Le motif revient.
5. Le sommet, avec les graines de la chute.
6. La chute, racontée comme une scène.
7. L'épilogue (« que sont-ils devenus ? »), le verdict avec un avis argumenté, la vidéo suivante.

Squelette détaillé : `structures.md`, sections 3 et 4.

### B. Défi en escalade (V2F)
Pour un test, un projet, une expérience du créateur.
1. Ouverture : le problème montré, ou le superlatif sourcé (« le plus compliqué »).
2. La contrainte, qui fait monter l'enjeu : un délai, une règle, une limite.
3. Les étapes. Chacune est un petit problème, suivi d'une solution plus maligne ou d'une riposte plus grosse.
4. Le test en conditions réelles.
5. Le résultat honnête, même raté, puis une chute ironique.

Squelette détaillé : `structures.md`, section 7.

### C. Essai immersif (Dis Cyril)
Pour expliquer un phénomène du quotidien ou une question de société.
1. Ouverture : une scène vécue en « tu », ou « Et si ».
2. La croyance, dite par le spectateur lui-même (« je suis sûr qu'il m'écoute »), puis la réalité.
3. Une métaphore filée, dont on pose les règles.
4. Un élément nouveau qui casse ces règles, une par une.
5. Ce que ça change pour le spectateur, puis une question ouverte.

Pièges observés chez lui :
- des fausses oppositions en série (« Ce n'est pas juste la vie, c'est un plateau de jeu ») ;
- une morale assénée à la fin ;
- une question centrale posée trop tard (57 s).

Sa seule opposition qui marche est celle du titre : la vidéo fait d'abord dire la croyance au spectateur.

---

## 6. Les fins

La fin retourne quelque chose en plus de résumer :
- **l'ironie** : le créateur se surprend à défendre ceux qu'il combattait ;
- **le verdict** : un avis argumenté, une comparaison qui éclaire, puis l'annonce de la vidéo suivante, qui ouvre une nouvelle boucle ;
- **la meilleure question** : remplacer la question que le spectateur s'est posée tout du long par une meilleure (« Est-ce qu'ils vont réussir ? » devient « Est-ce qu'ils ont réussi ? ») ;
- **le rappel** d'un détail planté au début (le nom « SOS » donné à l'OS revient dans la fausse pub finale).

Jamais de morale assénée : si l'histoire a fait son travail, le spectateur l'a déjà comprise.

---

## 7. Les axes de la variante (mode grill)

Ajoute-les au tableau de bord, après les 11 axes. Les liaisons orales sont notées à l'axe 10, dans tous les modes.

| Axe | 🟢 | 🟠 | 🔴 |
|---|---|---|---|
| **S1. Les 30 premières secondes** (section 2) | les 6 questions passent | 1 ou 2 manques | pas de question centrale avant 30 s, ou contexte, salut ou sponsor dedans |
| **S2. Le pont** | il ouvre une deuxième question | il démarre la suite sans rien ouvrir | le récit repart sur une chronologie plate (« Tout commence en 2009… ») |
| **S3. Les retournements** | un toutes les 25-35 s | des trous de 45-60 s | des trous de plus d'une minute |
| **S4. Planté / récolté et motif** | au moins 2 récoltes et un motif | un seul des deux | aucun : chaque partie est autonome |
| **S5. Personnages et enjeu** | quelqu'un veut quelque chose et en est empêché | des acteurs sans envie | des entités (« l'entreprise », « le marché ») |
| **S6. La fin** | elle retourne ou ouvre quelque chose | elle résume | elle s'arrête, ou assène une morale |


---
## Fichier : youtube-script-grill/references/structures.md

# Structures pour YouTube

## Sommaire
1. Comment choisir (et les hybrides)
2. Voyage du héros, version YouTube
3. Ascension et chute
4. Enquête
5. Tutoriel narratif (hook en 5 temps, boucles de valeur)
6. Essai à contre-courant
7. Défi ou expérience
8. Briques communes : hook, "mais / donc", relances, boucles ouvertes, appel à l'action, fin

---

## 1. Comment choisir

| Matière disponible | Structure | Exemples de vidéos |
|---|---|---|
| Un narrateur qui a vécu une transformation | Voyage du héros | "Comment j'ai…", "J'ai arrêté X", tuto raconté par celui qui a galéré |
| L'histoire d'une entreprise, d'un jeu ou d'une personne, avec un sommet puis un déclin | Ascension et chute | "L'histoire de…", "Comment X est tombé" |
| Une question intrigante dont la réponse surprend | Enquête | "Pourquoi X ?", "Que s'est-il vraiment passé avec Y ?" |
| Une méthode à transmettre en plusieurs points | Tutoriel narratif | "Comment faire X", guides, listes |
| Une opinion contre le consensus, avec des preuves | Essai à contre-courant | "Arrêtez de…", "X est surcoté" |
| Un test réel avec un résultat mesurable | Défi ou expérience | "J'ai testé X pendant 30 jours" |
| Un phénomène du quotidien à expliquer, porté par une scène ou une métaphore | Essai immersif (`storytelling.md`, section 5) | "Ton téléphone ne t'écoute pas… c'est pire" |

**Hybrides fréquents, souvent les meilleurs :**
- **Tuto dans un voyage du héros** : le narrateur traverse les étapes du tuto en racontant ses erreurs ; chaque point enseigné est une épreuve qu'il a passée. Le spectateur apprend la méthode et suit une histoire.
- **Ascension et chute racontée comme une enquête** : ouvrir sur la chute ("En 2019, le studio ferme ses portes"), puis remonter le temps pour comprendre.
- **Défi** : c'est un voyage du héros avec un chronomètre.

**Règle** : la structure sert la matière. Si une structure oblige à inventer une crise, un rebondissement ou un personnage, choisis-en une autre.

---

## 2. Voyage du héros, version YouTube

La version complète en 9 étapes est dans `grille.md` (axe 7). Sur YouTube, l'attention se joue dans les 30 premières secondes : on condense, et on ouvre souvent sur le moment fort avant de revenir au début.

1. **Hook** (0-30 s) : confirmer la promesse (test des 30 secondes : `storytelling.md`, section 2). Souvent un saut en avant vers la crise ou le résultat ("Il y a six mois, j'étais à deux doigts de supprimer ma chaîne.").
2. **Situation de départ** : qui est le narrateur, ce qui cloche. Le spectateur doit s'y reconnaître.
3. **Déclencheur** : l'événement qui force à agir (un échec, un commentaire, une opportunité, une menace).
4. **Épreuves** : 2 à 4 obstacles enchaînés en "mais / donc". C'est le corps de la vidéo ; dans un hybride tuto, chaque épreuve porte un enseignement.
5. **Crise** : le point le plus bas. Le narrateur se montre vulnérable, admet ses erreurs ou ses doutes.
6. **Déclic** : ce que la crise lui a appris. C'est souvent l'angle unique de la vidéo.
7. **Retour transformé** : le résultat concret, ce qui a changé chez lui ; la promesse du titre est tenue.
8. **Nouvelle question** (optionnel) : une boucle ouverte vers une autre vidéo.

Étapes indispensables pour une vidéo courte : déclencheur, épreuves, crise, retour.

Pièges : un héros qui sait tout dès le début ; une crise expédiée en une phrase ; une morale assénée à la fin au lieu d'être montrée par l'histoire.

---

## 3. Ascension et chute

Pour les récits d'entreprises, de jeux, de créateurs, de technologies.

1. **Hook** : le contraste entre le sommet et la chute en deux phrases, ou une énigme ("Le jeu le plus attendu de la décennie a fermé ses serveurs au bout de six mois.").
2. **Origines** : d'où ça part, les personnages, ce qu'ils veulent.
3. **Ascension** : les paris réussis, racontés avec des détails à fort score de choc.
4. **Sommet** : le moment où tout semble gagné. Y planter les graines de la chute, discrètement : le spectateur doit pouvoir les repérer après coup.
5. **Fissures** : les premières mauvaises décisions, enchaînées en "mais / donc".
6. **Chute** : le point le plus bas, raconté comme une scène (date, lieu, personnes, réactions).
7. **L'après** : ce que l'histoire révèle de plus large (orgueil, peur du changement, cupidité…), et parfois une renaissance.

Pièges : une chronologie plate ("En 2005… En 2006…") ; trop de contexte avant que l'action démarre ; une leçon finale générique.

---

## 4. Enquête

1. **Hook** : la question ou l'anomalie ("Ce jeu s'est vendu à 20 millions d'exemplaires. Son studio a fermé un an plus tard.").
2. **L'explication évidente** : ce que tout le monde croit, puis le fait qui la met en doute.
3. **Indices** : chaque piste rapproche de la réponse, dans un ordre qui fait monter la tension. Laisse le spectateur deviner.
4. **Fausse piste** (optionnel) : une explication séduisante qui s'effondre.
5. **Révélation** : la vraie réponse, dans le dernier quart de la vidéo.
6. **Conséquences** : ce que ça change pour le spectateur ou pour le domaine.

Pièges : révéler la réponse trop tôt ; des indices sans lien entre eux ; une révélation moins surprenante que la question.

---

## 5. Tutoriel narratif

### Hook en 5 temps
1. **Contexte** : dire sans détour de quoi parle la vidéo, pour confirmer le clic.
2. **Croyance commune** : l'approche habituelle, que le spectateur partage probablement. Elle crée un terrain commun.
3. **Angle contraire** : ce que le créateur fait autrement, appuyé sur un fait ou un résultat. Exprime-le par la preuve, sans la formule "ce n'est pas A, c'est B" (voir `anti-ia.md`).
4. **Plan** : les étapes que la vidéo va suivre.
5. **Preuve** : pourquoi le croire (résultats, expérience, analyse menée). Les temps 4 et 5 peuvent s'inverser.

Vérifie le hook sur 4 critères :
- **Alignement** : l'image, la parole et le texte à l'écran disent la même chose.
- **Vitesse** : la valeur est annoncée dans les 3 premières secondes.
- **Clarté** : impossible de se tromper sur le sujet.
- **Curiosité** : une question reste ouverte et pousse à continuer.

### Corps
- **Ordre** : 2e meilleur point en premier, meilleur point en deuxième, puis le reste par valeur décroissante. Le premier point après l'intro doit surprendre, car c'est là que les spectateurs partent si c'est générique ; enchaîner ensuite le meilleur leur montre que la valeur monte, et ils restent. Les albums placent leur tube en piste 3 ou 4 pour la même raison.
- **Boucle de valeur** pour chaque point :
  1. Contexte : c'est quoi, en termes simples.
  2. Application : comment faire, avec le plus d'exemples concrets possible.
  3. Mise en perspective : pourquoi ça compte et comment ça s'emboîte dans l'ensemble.
- **Alterner** zoom avant (la tactique) et zoom arrière (la vue d'ensemble), comme une vague.
- **Relance** entre chaque point (section 8).
- **Fil narratif** : même un pur tuto gagne à avoir un narrateur qui progresse (voir l'hybride en section 1).

### Fin
Récapitule les points, rappelle le problème résolu (la preuve finale que la vidéo a dépassé l'attente), termine sur un point haut. Ouvre éventuellement une nouvelle question dans les 15 à 30 dernières secondes.

---

## 6. Essai à contre-courant

1. **Hook** : la thèse, précise et frontale, plus un fait qui intrigue.
2. **Le consensus** : présenté honnêtement, dans sa meilleure version. Caricaturer l'avis opposé fait perdre la confiance du spectateur qui le partage.
3. **Les preuves** : 2 à 4 arguments, chacun porté par un exemple, un chiffre ou un vécu.
4. **L'objection la plus forte** : y répondre franchement, concéder ce qui doit l'être.
5. **Ce que ça change** : les conséquences concrètes pour le spectateur.

Pièges : une thèse en forme de slogan ; la même idée répétée sous plusieurs formes ; un ton donneur de leçons.

---

## 7. Défi ou expérience

1. **Hook** : le défi et l'enjeu ("30 jours, une seule règle : …"), avec un aperçu du résultat sans le donner.
2. **Les règles et le point de départ** : mesures avant, conditions du test.
3. **Les débuts** : premières difficultés, premières surprises.
4. **Le creux** : le moment où ça devient dur (la crise).
5. **L'ajustement** : ce qui change dans la méthode ou dans la tête.
6. **Le résultat** : mesures après, honnêtes même si elles déçoivent.
7. **Ce qu'il en retient** : pour le spectateur.

---

## 8. Briques communes

### "Mais / donc"
Relie les parties par des tensions ("mais") et des conséquences ("donc"), plutôt que par "ensuite" ou "deuxième point". Exemple : "J'avais tout préparé pour le lancement. Mais la veille, le serveur a planté. Donc j'ai passé la nuit à tout migrer, et c'est là que j'ai découvert…" Ici, des événements s'enchaînent et aucune idée n'est réfutée ; la fausse opposition de `anti-ia.md` est un tout autre mécanisme.

### Relances
L'attention baisse en continu ; une relance toutes les 30 à 60 secondes la remet à zéro. Une relance donne une raison de rester pour la suite :
- annoncer qu'un élément manque encore ("Ça marchait. Jusqu'au jour où le premier client a appelé.") ;
- teaser une information et la livrer plus loin (setup puis payoff) ;
- poser une question qu'on résout dans la partie suivante.

### Boucles ouvertes
Plante une question tôt, résous-la tard. Chaque boucle ouverte doit être refermée : un teaser jamais payé est une promesse trahie.

### Appel à l'action naturel
Pendant le plan, repère le point où la ressource (produit, formation, autre vidéo) résout réellement le problème évoqué. Deux façons de l'intégrer :
- poser le problème, puis présenter la ressource comme la solution ;
- dérouler une méthode dense et rapide, puis proposer la ressource comme le moyen de l'appliquer ou de la revoir plus facilement.
Mentionne-la à ce moment, sans changer de ton, puis repars. Si la ressource ne résout pas vraiment le point en cours, place-la ailleurs ou nulle part.

### Fin
Récapitulatif, point haut, et éventuellement une nouvelle question vers une autre vidéo. La fin pèse sur les likes, les partages et les commentaires : elle se travaille autant que le hook.

