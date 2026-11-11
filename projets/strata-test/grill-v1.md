# Grill de la V1 : « Je teste le meilleur modèle possible avec Strata sur ma 5080 » (11/11/2026)

> Critiqués : [`script-v1.md`](script-v1.md) et [`plan-tests-v1.md`](plan-tests-v1.md) (copies à l'identique de la V1 du rédacteur), avec le storyboard et le téléprompteur de la V1. Corrigés dans la V2 : [`plan-tests.md`](plan-tests.md), [`script.md`](script.md), [`storyboard.md`](storyboard.md), [`teleprompteur.txt`](teleprompteur.txt). Faits revérifiés : [`sources.md`](sources.md), section G. Méthode : skill `youtube-script-grill`, mode B, variante storytelling ; règles de `.claude/rules/script.md` et de l'audit du 11/11 (§ 2, 2 bis, 3, 5). Débit de référence : 145 mots/min.

## Verdict

**Script V1 : 6/10. Plan de tests V1 : 5/10.** V2 estimées : script 7,5/10 (il dépend de tes 15 phrases), plan 8/10.

Le script V1 a la bonne colonne vertébrale : les résultats d'abord, trois démos en niveaux de jeu vidéo, un défi affiché tôt, aucun résultat inventé. Mais il est **injouable tel quel** : 43 trous et deux variantes par moment, à remplir le soir d'une journée de tests, avec des contradictions entre branches. Le plan V1 est sérieux et presque toutes ses commandes existent, mais **la seule correction prévue pour les fichiers coupés ne marchait pas**, il sous-estimait le bug qui fait planter le Coder sur une longue demande, et il demandait 41 plans et deux relances par test : trop pour une après-midi.

## Test des 30 secondes (V1, variante A)

| Tranche | Ce que dit le script | Verdict |
|---|---|---|
| 0-5 s | > « Un jeu qui se joue. Un site complet. Un monde en 3D. » | 🟠 Les images portent, et c'est raccord avec le titre. Mais c'est la cascade de trois fragments que `anti-ia.md` signale, en ouverture. |
| 5-15 s | > « Une IA a écrit les trois, chez moi, sur ma RTX 5080, à ⟦tok/s typique⟧ tokens par seconde. » | 🟢 Le résultat et sa preuve (le compteur incrusté). « Tokens par seconde » n'est expliqué qu'à 5:36. |
| 15-30 s | > « Sauf que le vrai modèle, celui dont il vient, demande bien plus de RAM que mes trente-deux gigas. Du coup, jusqu'où ça va, une IA qui tourne chez toi ? » | 🟠 Contraste flou : quel « vrai modèle » ? Le spectateur ne sait pas encore qu'il y a une version coupée. Et « jusqu'où ça va » est vague, alors que la vraie question de la vidéo arrive à la fin : « est-ce que ça remplace mon abonnement ? ». |
| Pont | > « Au programme : ce que j'ai fait tourner et comment le refaire, la vitesse, le même test donné à Claude, et là où ça casse. Ton pronostic en commentaire : le local tient, ou Claude écrase ? » | 🟢 Quatre livrables concrets et un défi, comme le demande l'audit (§ 2 bis). |

**Budget V1** : 92 mots (variante A) ≈ 38 s ; la question tombe vers 0:22, le plan finit vers 0:38.
**Coupé en V2** : la cascade de fragments, « le vrai modèle, celui dont il vient », « jusqu'où ça va, une IA qui tourne chez toi ».

**Réécriture appliquée (V2, 92 mots ≈ 38 s, 34 s à un débit vif)** :

> Ce casse-briques, ce site, cette île en 3D : une IA les a écrits chez moi, sur ma 5080, à ⟦R1⟧ tokens par seconde. ⟦R2⟧ sur trois ont marché du premier coup. Sauf que le modèle complet ne rentre pas dans mes trente-deux gigas de RAM : j'ai pris sa moitié, gardée pour le code. Alors, une moitié de modèle, est-ce que ça remplace Claude ? Au programme : la vitesse, ce qu'il faut à ton PC, le même test donné à Claude, et là où ça casse. Ton pronostic : le local tient, ou Claude écrase ?

- Le contraste devient concret (« la moitié »), et c'est le cœur de la vidéo.
- La question centrale (≈ 0:25) est **celle de la fin** : la boucle se referme en section 7.
- R2 (« combien sur trois ») monte l'enjeu dans les deux cas : trois sur trois, c'est fort ; zéro sur trois aussi.

## Tableau de bord

| Axe | V1 | V2 | En une phrase |
|---|---|---|---|
| 1. Promesse | 🟢 | 🟢 | « Le meilleur modèle possible sur ma 5080 » est montré dès 0:00. |
| 2. Alignement | 🟢 | 🟢 | Pas une vidéo contre Claude, pas de rêve vendu : « trois essais, ce n'est pas un classement ». |
| 3. Problème profond | 🟠 | 🟠 | « Mon PC de joueur vaut-il un abonnement ? » : posé en V2 dès 0:25, résolu par ton verdict (R15). Il reste à ta phrase de le porter. |
| 4. Public & complexité | 🟠 | 🟢 | V1 : « tokens par seconde » expliqué à 5:36, « resident experts » expliqué faux. V2 : expliqué à la première apparition. |
| 5. Valeur & originalité | 🟢 | 🟢 | Personne en français ne fait ce test avec du vrai code (références du 11/11). |
| 6. Structure | 🟠 | 🟢 | V1 : deux listes « comment le refaire » (section 2 et 7) ; 2 min 30 sans démo en section 2. V2 : une seule liste, à la fin. |
| 7. Histoire | 🟠 | 🟢 | Défi en escalade (niveau 1, niveau 2, boss). V1 cassait l'escalade (« le site… la plus facile »). |
| 8. Mais / donc | 🟢 | 🟢 | « Sauf que sa règle… », « Le message accuse la RAM. Sauf que… ». |
| 9. Engagement actif | 🟢 | 🟢 | Le pronostic du spectateur (0:35 → fin), le tien avant la 3D. |
| 10. Oralité & liaisons | 🟠 | 🟢 | V1 : 2,0 pour 100 mots, mais quatre « Du coup » et deux « En effet », dont un en tête de paragraphe : un quota. V2 : 1,62, variées. |
| 11. Tics d'IA | 🟠 | 🟢 | V1 : cascade de fragments en ouverture ; « Bon, c'est joli » après la variante « ça casse ». |
| S1. 30 premières secondes | 🟠 | 🟢 | Question centrale précise avant 30 s, plan et défi juste après. |
| S2. Le pont | 🟢 | 🟢 | Le plan en 4 livrables, puis une démo tout de suite. |
| S3. Retournements | 🟠 | 🟢 | V1 : la section 2 tenait 2 min 30 sans démo ni relance (la fuite de « 16 Go », audit § 2). V2 : 1 min 45, avec « 29,6 Go > 16 Go » et « Bon, ça tient. Mais… ». |
| S4. Planté / récolté | 🟠 | 🟢 | V2 : le message « qui accuse la RAM » → « c'est comme ça que la cause a été trouvée » ; « monter la limite » → la liste du soir ; les deux pronostics. |
| S5. Personnages | 🟠 | 🟠 | Toi et des utilisateurs sans nom (ta règle). |
| S6. La fin | 🟢 | 🟢 | Ton verdict, un geste à faire ce soir, la vidéo de jeudi. |

## Les 5 problèmes les plus graves

### 1. La correction des fichiers coupés ne marchait pas, et le risque était sous-estimé (plan)
> « relance Strata avec un contexte plus grand […] `--context 98304` […] Puis `strata connect opencode --write` **de nouveau** (il met le contexte à jour dans OpenCode). […] La réponse maximale passe à 12 288 tokens »

**Pourquoi ça coince** : dans le code de `strata connect` (`_keep_output_cap`), une limite déjà écrite et différente de 4 096 est **gardée** quand on réécrit le fichier : après la relance, la limite reste à 8 192 (T31). Tu aurais perdu une relance du moteur, de la RAM (plus de contexte sur un PC à ras) et gardé des fichiers coupés. Et le risque est plus grand que le plan ne le disait : le serveur n'arrête la réflexion qu'au dernier quart de la limite, soit ≈ 2 000 tokens pour écrire un jeu entier (T13, T31). Les trois démos étaient exposées.
**Correction (faite)** : la limite est montée **à la main** à 32 000 avant le premier test (`maxTokens` de Pi, ou `limit.output` d'OpenCode), et le calibrage le vérifie (plan 4.3 et 5).

### 2. Le bug du plantage était présenté comme un cas de petite carte (plan et script)
> « chez un utilisateur avec une petite carte » (script) ; « sur une carte de 8 Go ; sur la tienne ça reste à mesurer » (plan)

**Pourquoi ça coince** : les commentaires du ticket #5104 le montrent sur des cartes de 8 **et 12 Go**, sous Windows, et sur une **RTX 5070 (la famille de ta 5080)** ; la cause est trouvée (un compte de 512 experts en dur, le Coder en a 256) et la source de la 0.2.13 plante encore (T23). Le prompt système d'OpenCode (≈ 7 400 tokens) dépasse le seuil où les plantages ont été vus (≈ 3 300).
**Correction (faite)** : le plan cherche la ligne « layer-major walk » au démarrage et applique le contournement avant de filmer ; le calibrage sert de détecteur ; le harnais passe à Pi (≈ 1 500 tokens). Le script dit « plusieurs utilisateurs, des cartes de huit et douze gigas » et que la cause est trouvée.

### 3. 43 trous et deux variantes par moment (script)
> « ▶ A (ça marche) : […] ▶ B (ça casse) : […] ▶ Suite : Bon, c'est joli. »

**Pourquoi ça coince** : 43 trous à remplir le soir d'une journée de tests, dont la moitié se recoupent (« a marché du premier coup ? », « points sur 5 », « verdict final », « relances »…). Les branches se contredisent : « Bon, c'est joli » suit aussi la variante où le jeu plante. Le téléprompteur devient un jeu de piste.
**Correction (faite)** : **15 trous** (R1 à R15), un seul texte, une phrase par résultat dans tes mots ; les chiffres détaillés vont sur les cartes de verdict du storyboard.

### 4. La question centrale était vague, et la section 2 refaisait la fuite de « 16 Go » (script)
> « Du coup, jusqu'où ça va, une IA qui tourne chez toi ? » […] section 2 : 342 mots, de 1:58 à 4:29, sans démo

**Pourquoi ça coince** : la question n'est pas celle à laquelle la fin répond (« est-ce que ça remplace mon abonnement ? »). Puis, après le premier résultat, 2 min 30 de théorie, d'installation et de commandes, sans relance : exactement le creux de 0:30 → 1:15 de « 16 Go » (audit § 2). Les trois étapes d'installation faisaient aussi doublon avec la liste de la fin.
**Correction (faite)** : la question de la fin est posée à 0:25 ; la section 2 passe à 238 mots (≈ 1 min 45) et finit sur une relance ; les commandes vont dans la liste du soir.

### 5. Le plan ne tenait pas dans une après-midi (plan)
> « 41 plans à filmer » ; « Relances : **2 au maximum** par test » ; la comparaison avec Claude **après** les tests locaux

**Pourquoi ça coince** : chaque relance demande d'arrêter le navigateur, de relancer le moteur (plusieurs minutes) et d'attendre une génération ; deux par test, c'est jusqu'à six cycles. Claude passait en dernier, alors qu'il n'a besoin ni de Strata ni de la RAM libre. Et l'étape du réglage de la réflexion reposait sur une commande non confirmée.
**Correction (faite)** : Claude et les captures web **pendant le téléchargement** (la moitié de la vidéo existe même si Strata casse) ; une relance par test, toutes ensemble ; 18 plans indispensables ; la réflexion n'est plus réglée.

**Aussi corrigé** : « cinquante-huit gigas à télécharger » (la couche de prédiction s'ajoute : « une soixantaine », T33) ; « si tu vois resident experts, tout est en RAM » (en fait : ce que la carte ne garde pas est copié en RAM, T8) ; « Niveau deux : le site… donc c'est la plus facile » (casse l'escalade, non sourcé) ; l'échec du Coder dans Claude Code, revérifié dans la description de la vidéo (T27).

## Les commandes et réglages du plan V1, un par un

Vérifiés le 11/11 dans `docs/TERMINAL_LAUNCH.md`, `MODELS.md`, `DETAILS.md`, `INSTALL.md`, `TROUBLESHOOTING.md`, `SETTINGS.md`, `strata_cli/launch/harness.py`, les notes de la v0.2.13 et les tickets (T31 à T38).

| Commande ou réglage de la V1 | Statut | Ce qu'en fait la V2 |
|---|---|---|
| `strata launch --plan --family coder --model IQ1_M --context 64k --vision off --parallel 1 --data-dir D:\Strata` | ✅ toutes les options existent | Gardée (pour vérifier que le Terminal reprend le modèle de l'appli) |
| Le plan affiche « fits / tight / does not fit » | ⚠️ depuis la 0.2.13 : « fits » ou « may run slower » ; `--plan` ne promet pas de libellé | Formulation corrigée |
| `strata launch` guidé, ses écrans, l'écran Advanced qui montre la commande | ✅ | Gardé (P06) |
| `--resident-experts` / `--mmap-experts`, « pas d'option `--low-ram` » | ✅ | Gardé, explication corrigée |
| `strata launch --status` « doit répondre serving » | ✅ la commande ; ⚠️ le mot | « doit montrer le modèle servi » |
| `--stop`, `--restart`, `--preset "Coder 64K"`, `--save-preset` | ✅ | Gardés |
| `strata connect opencode`, `--write`, `--check` ; `--write` écrit `~/.config/opencode/opencode.json` | ✅ | Plan B (Pi devient le harnais) |
| `strata connect claude-code --write` écrirait dans `~/.claude/settings.json` | ✅ (code, `FileSpec("~/.claude/settings.json", merge=True)`) | La règle reste : jamais cette commande |
| Plafond de réponse = max(4 096, contexte ÷ 8) = **8 192 à 64K**, réflexion comprise | ✅ (code) | Gardé, et corrigé à la main |
| `--context 98304` + `--write` → 12 288 | ❌ la limite déjà écrite est gardée (8 192) | Retiré ; correction à la main |
| `--set STRATA_PREFILL_LAYER_MAJOR=0` (#5104) | ✅ (ticket, confirmé par deux utilisateurs ; listé dans SETTINGS.md) ; portée sous-estimée | Gardé, appliqué dès la ligne « layer-major walk » |
| Version 0.2.13 (09/11), « le Terminal reste en 0.2.12 après `strata update` » | ✅ ; la note ne vaut que pour une mise à jour depuis la 0.2.12 | Gardé |
| `--set reasoning-effort=medium` | ⚠️ non confirmé (la clé `reasoning_effort` existe dans la config du modèle, pas cette option de lancement) | Retiré |
| « Les Chat settings de la page web ne servent pas ici » | ❌ contredit : « the web page's shared Chat settings win » (DETAILS.md, deux fois) | Retiré |
| `--mtp off` comme remède | ❌ pour le Coder : un fichier IQ natif refuse de démarrer sans (rapporteur de #5046) | Retiré |
| `--set STRATA_RESIDENT_PIN=0` (#649) | ✅ existe, mais pour `--resident-budget-gib` | Retiré (simplification) |
| `strata monitor --url http://127.0.0.1:8080`, vue 1 Overview | ✅ | Gardé |
| « La vue 6 (Logs) garde la vitesse par requête » | ⚠️ la doc met les requêtes récentes en vue 1 et Requests en vue 3 | Vue 1 ou 3 ; la vue 6 sert aux lignes du moteur |
| `strata status --json` | ⚠️ documenté seulement avec `--url` | Remplacé par `strata launch --status` |
| `strata doctor`, `strata --version`, ligne `install.ps1`, pilote 580 | ✅ | Gardés (le Terminal seulement si l'installeur ne le met pas) |
| `npm i -g opencode-ai`, premier lancement qui télécharge un plug-in | ✅ (code de Strata) | Plan B |
| `opencode --continue` | ⚠️ non vérifié | Remplacé par `pi --continue` ✅ (doc de Pi) |
| « VRAM libre à 0 : de 100 à 14 tok/s » | ⚠️ c'est le cas d'une `--expert-cache N` mise à la main | Reformulé |
| L'adresse three.js r128 | ✅ HTTP 200 le 11/11 | Gardée |

## Tes décisions du 11/11, intégrées

- **L'installeur Windows** (`Strata-0.2.13-windows-x64-setup.exe`) : il installe l'appli, sans le moteur, que l'appli télécharge au premier démarrage avec le modèle choisi ; le mode RAM réduite est choisi par la même installation que le Terminal. L'appli contient un harnais à elle (« DeepSeek Harness »), mais la doc ne le présente qu'avec DeepSeek : pas utilisé. Le Terminal reste pour ce que la doc de l'appli ne montre pas (`strata connect`, un compteur hors navigateur, `--set` pour #5104) ; il reprend le modèle que l'appli a téléchargé (T38). Non trouvé dans la doc : si l'installeur ajoute la commande `strata` (le plan le vérifie en 2.3).
- **Pi plutôt qu'OpenCode : recommandé.** Strata le dit lui-même : « pi has the smallest prompt of the eight (1.5K tokens) », contre ≈ 7 400 pour OpenCode (T14, T37). **≈ 5 900 tokens de moins par requête**, 9 % d'un contexte de 64K. Sa première requête (≈ 1 850 tokens) passe sous le seuil où #5104 a été vu ; celle d'OpenCode non. Il tourne sous Windows natif (Node 22.19+, Git Bash pour ses commandes, Windows Terminal recommandé). Dans le script, ces chiffres sont en section 4 (« moins à relire à chaque demande »), pas dans la première minute. **Ce qu'il ne change pas** : la limite de réponse (8 192 pour les deux) ; et `strata connect pi --write` remet `maxTokens` à 8 192 à chaque fois. OpenCode est le plan B 9.10.

## Ce qui marche, à garder

- **Les résultats d'abord** et l'escalade en niveaux de jeu vidéo (« Niveau un », « Boss final ») : le bon cadre pour ton public.
- > « Règle du jeu : un essai […] comme des pièces à l'arcade » : une contrainte claire, avec ton humour.
- > « Mais avec la réflexion coupée, et sans vérifier si le code marche » : le repère de 70 tok/s donné avec ses limites. C'est ce qui rend la vidéo crédible.
- > « Ils annoncent quatre-vingt-quinze pour cent du score de code […] C'est leur chiffre » : l'attribution.
- Le pronostic affiché tôt et rappelé à la fin ; ton pronostic écrit **avant** le test 3D (« ce qu'on écrit après coup est toujours trop malin »).
- Dans le plan : la règle « le premier essai compte », la limite de 25 minutes, le navigateur fermé pendant les générations, le score sur 5 exigences numérotées, un plan B par symptôme, « décale la vidéo plutôt que de changer de modèle », l'adresse de three.js imposée, le faux nom vérifié (« Tikaya », « Kora » écarté).
- La discipline des sources : aucun nom de chaîne dans la voix, « un utilisateur rapporte », chaque chiffre relié à un T.

## Mesure (11/11, même script de comptage pour les deux versions)

Voix seule (sections 0 à 7, sans `[VISUEL]` ni notes), chaque trou compté pour 1 mot. Liaisons strictes : donc, du coup, en fait, sauf que, en effet, voilà, bref, par contre, justement, bon, alors ; larges : + mais, parce que, maintenant, attention, et là.

| | Mots | Durée à 145 mots/min | Trous (emplacements) | Hook | Liaisons / 100 (stricte / large) |
|---|---|---|---|---|---|
| V1, variante A | 1 294 | 8 min 55 (≈ 10 min remplie) | 43 distincts (32 dans A) | 92 mots ≈ 38 s | 2,01 / 2,70, dont 4 « du coup » |
| **V2** | **1 296** | **8 min 56 (≈ 9 min 30 remplie, ≈ 10 min avec tes phrases)** | **15 (17)** | **92 mots ≈ 38 s** | **1,62 / 2,31**, 2 « du coup », 0 « en effet » |

Les chiffres de la V1 diffèrent un peu de ceux du rédacteur (1 354 mots, 1,77) : ce n'est pas le même découpage des mots, ni la même liste.

## Plan d'action

1. **Aujourd'hui** : suis [`plan-tests.md`](plan-tests.md) V2, dans l'ordre. Le calibrage (section 5) n'est pas optionnel.
2. Remplis la fiche R1 à R15 en tournant, une phrase chacune, dans tes mots.
3. Remplace les ⟦R…⟧ dans [`teleprompteur.txt`](teleprompteur.txt) ; coupe les deux phrases de la limite si tu ne l'as pas montée, et la phrase sur Pi si tu es passé à OpenCode.
4. Repasse le hook rempli au test des 30 secondes : si R2 vaut zéro, garde la phrase, elle monte l'enjeu.
5. Avant le montage : recale le storyboard sur la voix, et vérifie que la version du jour de Strata n'a pas corrigé #5104 (la phrase « pas encore dans la version que j'ai testée » reste vraie dans tous les cas).
