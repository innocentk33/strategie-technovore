# Grill V3 · Setup Black Friday IA locale

Critique indépendante du téléprompteur V3 du 21/11 (`teleprompteur.txt`, identique à `teleprompteur.md`, vérifié par `diff`) et de `script.md`. Méthode : skill `youtube-script-grill`, variante storytelling, test des 30 secondes, axe des liaisons orales, règles de `.claude/rules/script.md`. Faits recoupés avec `recherche/prix-21-11.md` (qui fait foi pour les prix), `sources.md` (F1 à F21) et `verification.md`. Le renvoi est comparé à `projets/qwen-27b-8go/teleprompteur.txt`.

Les numéros de ligne (L…) sont ceux de `teleprompteur.txt` V3. Les mots sont comptés comme dans `script.md` (chaque groupe de chiffres compte pour un mot, « 1 499 » = 2, guillemets exclus).

## Note : 6,5 / 10

**Verdict.** Côté chiffres, c'est très propre : j'ai refait chaque soustraction et chaque total du tableau de la section 3, et aucun prix prononcé n'est faux. Les pièges (RAM affichée comme VRAM, la 3060 en 8 ou 12 gigas, la 3090 de 34 cm) rendent un vrai service. Le plus gros problème, c'est la logique : chaque palier de mémoire est expliqué un budget trop tard (on vise 16 gigas à 1 000 euros sans savoir pourquoi, et 24 gigas à 1 500 sans le fichier de 22 gigas), et le verdict oublie la route la moins chère pour 16 gigas, celle que tu as toi-même montrée à 1 000 euros. Avec un hook remis dans l'ordre, une intro qui finit à 1:07 au lieu de 1:17, et des fiches techniques moins récitées, la vidéo passe à 8.

---

## 1. Test des 30 secondes

Deux décomptes, parce qu'à l'oral les chiffres s'allongent : « 1 799 » fait 2 mots écrits, mais « mille sept cent quatre-vingt-dix-neuf » en fait 7. **La règle de la chaîne compte les mots écrits à 145 mots/min (72,5 mots en 30 s) : c'est ce décompte qui tranche.** Le décompte oral sert de contrôle : il dit ce que la voix va vraiment durer.

| Tranche | Ce que dit le script | Mots écrits (cumul) | Seconde (écrit / oral) | Verdict |
|---|---|---|---|---|
| 0-5 s | « Le 21 novembre, cette tour à 1 499 euros » | 9 | 3,7 s / 6,6 s | 🟠 Ça s'ouvre sur une date, donc du contexte, et pas en « tu ». La tension n'arrive qu'à la ligne 2. |
| 5-15 s | « avait 16 gigas de mémoire vidéo. Sur le même site, celle à 2 049 euros n'en a que 12. » | 28 | 11,6 s / 15,3 s | 🟢 Bon contraste (la moins chère a plus de mémoire vidéo). Mais ce n'est pas le chiffre le plus fort. |
| 15-30 s | « Et la veille, ces 2 tours affichaient 1 299 et 1 799 euros. Plus 200 et plus 250 euros en un jour, avec un badge « moins 50 euros » Black Friday. Du coup, avec ton budget, quelle carte te laisse de quoi finir la tour ? » | 72 | **question à 29,8 s** / 38,9 s | 🟠 Le meilleur moment du hook (+200 en un jour, sous un badge promo) tombe entre 17 et 21 s à l'écrit, vers 30 s à l'oral, donc après les 15 s. La question passe juste à l'écrit, pas à l'oral. Et le « Du coup » ne découle de rien : le prix qui bouge n'amène pas la question « quelle carte te laisse de quoi finir ». |
| Pont | « Bon, la tour à 16 gigas a aussi changé quelques pièces entre les 2 relevés. Et le site prévient que ses prix bougent d'un jour à l'autre. Donc avant le Black Friday, note le prix que tu vois. » | 110 | 45,5 s / ≈ 52 s | 🔴 C'est une précaution loyale envers OXIUM, mais elle n'ouvre aucune question. Elle dégonfle même le hook, et le conseil final revient mot pour mot à L211-212. Ces 38 mots repoussent le plan à 46 s. |

**Budget :** 72 mots jusqu'à la question (29,8 s à l'écrit, environ 39 s à l'oral). Le plan démarre à 46 s et finit à **1:17**. La règle du 11/11 veut le plan « vers la fin des 30 premières secondes ».

**À couper :** L10-13, à fondre dans le hook (la précaution) et dans la fin (le conseil, déjà présent).

**Réécriture des 30 s :** bloc R1, section 5. Question à 71 mots écrits (29,4 s ; environ 36 s à l'oral), le « +200 euros en un jour » à 27 mots (11,2 s ; environ 16 s à l'oral), plan fini à 1:07.

---

## 2. Les 14 règles de l'auteur

| # | Règle | Verdict | Où |
|---|---|---|---|
| 1 | Script complet, aucun crochet, aucune anecdote inventée | **Tenue** | Aucun `[`, `(` ni `⟦` dans le .txt. Yvetot et les recherches sont réelles (relevé § 4). « Sur ton téléphone… » (L63) est une mise en situation, pas une anecdote. |
| 2 | Lignes à lire seulement, 14 mots max, chiffres, .txt = .md | **Tenue** | Max 14 mots (L17, L19, L24, L30…). Aucun nombre en lettres. `diff` : fichiers identiques. |
| 3 | Hook direct en « tu », chiffre le plus fort avant 15 s, sans contexte | **Enfreinte (partielle)** | L1 commence par une date. Le premier « tu » arrive à L7 (vers 26 s). Le « +200 / +250 en un jour » tombe à L5 (17-21 s à l'écrit). |
| 4 | Question avant 30 s, puis zéro remplissage avant le plan | **Enfreinte** | Question à 29,8 s à l'écrit (38,9 s à l'oral), puis L10-13 : 38 mots de précaution et de conseil avant le plan. |
| 5 | Plan « Aujourd'hui, on va voir… », livrables concrets, « Et reste jusqu'à la fin : … » tenu | **Tenue, avec réserve** | La forme est bonne (L15-22). Le plan arrive tard (46-77 s). La promesse est tenue à L195-205, mais en partie seulement : la route « 14,4 gigas » oublie la 4060 Ti d'occasion de L103-111, et le fichier de 22 gigas n'est pas repris. |
| 6 | Après le plan, une réponse ou un cas concret | **Tenue** | L24-27 : la RX 6600 d'Issy, et ce qu'il reste. |
| 7 | Jamais « je n'ai rien testé », jamais l'impression d'un test | **Tenue, deux vigilances** | Aucune phrase de désaveu. À surveiller : le [VISUEL] « Démo : mail à raccourcir » (script.md, avant L50), qui laisse croire que tu as fait tourner le modèle, et le [VISUEL] « Carte à côté d'un mètre » (avant L145), qui ferait croire que tu as la carte s'il s'agit d'une photo. Voir E17. |
| 8 | Un seul renvoi, « dans une vidéo précédente », sans jour ni titre | **Tenue** | L56, une seule fois. « Tu te souviens de la tour… » (L113) renvoie au début de cette vidéo, pas à une autre. Ce que dit le renvoi est à corriger : voir E6. |
| 9 | Pas d'annonce de la prochaine vidéo ; fin = verdict puis « Allez, salut ! » | **Enfreinte (partielle)** | Aucune annonce. Mais après le verdict (L195-205) viennent 6 lignes (L207-212) : garantie, date, autre pays, rappel du prix. |
| 10 | Aucun nom de chaîne ni de site de tests ; pas de pseudo de vendeur | **Tenue** | Seulement des marchands et des constructeurs (OXIUM, CSL, Top Achat, Amazon, Carrefour, Cybertek, Memory PC, MSI, Palit, Intel, NVIDIA) et un logiciel (LM Studio). Aucun pseudo leboncoin. Leboncoin lui-même n'est jamais nommé (E13). |
| 11 | « Si cette vidéo t'a évité un mauvais achat, abonne-toi. », une fois, après un service | **Tenue** | L73, juste après le piège du Cintra, vers 3:50. |
| 12 | Au moins 1,5 liaison pour 100 mots, réactions, pas de fiche récitée | **Tenue en chiffre, enfreinte dans l'esprit** | 42 liaisons pour 1 813 mots = **2,3 pour 100** (comptées à la main ; sont exclus « même résultat » L59, « d'imaginer » L145, « que tu vois » L13 et L63, et « mais bon » compte pour une). Sauf que « Donc » revient 11 fois, dont 6 « Donc + ordre » en fin de paragraphe (L72, L80, L148, L163…). Les paires « Sauf que / Donc » sont mécaniques (L47-48, L58-59, L79-80). Et on entend 10 fiches techniques récitées (section 4). |
| 13 | Meilleur prix quel que soit le marchand, marchand nommé ; jamais « même marchand » comme méthode | **Enfreinte (partielle)** | L104 : Créteil à 450 €, alors que Talence était à 325 € (relevé § 4). L167 : Palit à 1 200 € sans dire pourquoi pas la MSI à 750. L186 « la vraie bonne affaire » et L193 « Amazon passait devant » : la tour 16 Go la moins chère était à 1 269,54 €, et le vendeur est Memory PC, pas Amazon. Aucun « même marchand » comme méthode : tenu. |
| 14 | Une seule date de relevé, tout au passé daté | **Enfreinte (partielle)** | La date est bien une seule (le 21). Mais « entre les 2 relevés » (L11) en révèle deux. Et 8 verbes au présent : L3 « n'en a que », L12 « prévient », L79 « dit », L98 « il y a », L126 « Pour l'avoir avant décembre », L142 « est », L180 « dit », L183 « a ». |

---

## 3. Erreurs de faits, de calcul et de loyauté (de la plus grave à la moins grave)

Aucun prix prononcé n'est faux. Les problèmes sont des oublis, des comparaisons et des phrases qui laissent croire plus que les sources.

**E1 · Le verdict oublie la route la moins chère pour 16 gigas (grave, logique)**
> L201-203 « Pour le fichier de 14,4 gigas, je prendrais une carte de 16. La tour Amazon à 1 270 euros si décembre ne te gêne pas, sinon la 5060 Ti à 799,99 et une base autour. »

À L103-111, tu as montré 16 gigas pour environ 1 000 € : la 4060 Ti de Créteil à 451,99 €, plus une base dans 548 € (plafonds F8 : 544 €). C'est un scénario, pas un prix relevé : la correction le dit au conditionnel. Le spectateur à 1 000 € entend ensuite qu'il lui faut 1 270 €. Correction : R16.

**E2 · Le piège du Cintra repose sur une mise en page non vérifiée (grave, c'est le pivot de la vidéo)**
> L18 « Le kit à 800 euros qui cache 6 gigas derrière un 16 » · L63-64 « Sur ton téléphone, tu vois une RTX 3050 et, un peu plus bas, 16 gigas. »

F3 dit seulement que la fiche « indique explicitement la version 6 Go ». Le relevé du 21/11 écrit « RTX 3050 6 Go, 16 Go ». Rien ne dit que le titre ou le haut de la page montre « 16 Go » sans le « 6 Go » à côté, ni à quoi ressemble la page sur téléphone. Le plan, l'abonnement (L73) et l'écho de L184 tiennent tous sur ce piège. **Avant d'enregistrer, fais une capture de la fiche, sur ordinateur et sur téléphone.** Et « cache » prête une intention à Top Achat, alors que l'info est sur la fiche. Correction : R1 (plan) et R6.

Si la capture montre « RTX 3050 6 Go » écrit en entier, le piège devient la RAM affichée à côté de la carte. Lignes de secours, qui remplacent L63-68 :
```
Sur la fiche, tu lis 16 gigas de RAM et une RTX 3050.
À ton avis, lequel compte pour l'IA ?
En fait, c'est la mémoire de la carte : 6 gigas sur la 3050.
```
Dans ce cas, L184 tient toujours : sur la Wyvern aussi, le 16 est la RAM.

**E3 · « La vraie bonne affaire » à 2 000 € ne tient pas (moyenne-grave)**
> L186 « La vraie bonne affaire était aussi sur Amazon, chez Memory PC. » · L193 « Donc à carte égale, Amazon passait devant. »

- La tour 16 Go la moins chère du relevé, c'est la TopConfig à 1 269,54 € (§ 3). Memory PC est moins chère seulement en RTX 5060 Ti 16 Go.
- Une autre 5060 Ti 16 Go (SYSTEMTREFF, 1 709,90 €) est sortie dans la recherche, sans que sa fiche soit ouverte. Ouvre-la au relevé du 25-26/11 : si elle a bien 16 gigas, elle passe 9,10 € devant.
- Le vendeur est Memory PC GmbH, un vendeur tiers sur Amazon. « Amazon passait devant » se trompe de marchand.
- Le spectateur n'entend jamais qu'en neuf, à 2 000 €, il n'a pas plus de mémoire vidéo qu'à 1 270 €. C'est pourtant la leçon de ton hook.

Correction : R13.

**E4 · Le hook est exact, mais à la limite de la loyauté (moyenne)**
> L1-6, puis L10-12.

- Les chiffres tiennent : 1 299 → 1 499 et 1 799 → 2 049 (+200, +250), barrés 1 549 et 2 099 avec un badge « −50 € ».
- Mais « ces 2 tours affichaient » laisse croire au même produit. Or l'Air avait changé 5 pièces, et le relevé ne dit pas si la Vice a changé.
- La précaution n'arrive qu'après la question (L10), et elle ne couvre que l'Air.
- « n'en a que 12 » présente la Vice comme moins bonne, sans dire que c'est une autre machine : RTX 5070, Ryzen 7 8700F, DDR5. F17 note bien « configurations différentes ».
- La phrase du site (« selon le prix des composants ») est l'explication du marchand : elle doit rester dans la voix, pas seulement à l'écran.

Correction : R1. La précaution passe dans le hook, la RTX 5070 est nommée et le +250 disparaît.

**E5 · Créteil retenue alors que Talence était moins chère (moyenne, règle 13)**
> L104 « À Créteil, une RTX 4060 Ti de 16 gigas était à 450 euros demandés. »

Relevé § 4 : ASUS Dual OC RTX 4060 Ti 16 Go à Talence, 325 € (326,99 € avec les frais), vendeur sans avis, en main propre. Soit 125 € de moins. Tu as retenu une tour en main propre à 800 € et une 3090 en main propre à 1 500 €, donc la remise en main propre n'explique pas le choix. Dis-le en une ligne. Correction : R10.

**E6 · Le renvoi dit vrai, mais il oublie ce qui compte (moyenne)**
> L56-58 « Dans une vidéo précédente, on a vu Qwen 27B tenir sur 8 gigas, juste en changeant de fichier. Sauf que cette mesure venait d'une carte NVIDIA. »

La vidéo du 23/11 parle bien d'une seule mesure publiée, sur une GTX 1080 Ti limitée à 8 gigas (NVIDIA : exact). Sauf qu'elle concluait que ce fichier (UD-IQ2_XS, 7,63 Go) rate « presque 9 fois sur 10 » les tâches d'agent (13 % contre 40 %) et ne laisse qu'environ 14 000 tokens de conversation. Le spectateur à 500 € qui a une Radeon de 8 gigas retient « 27B sur ma carte ». La vraie limite, c'est la qualité, pas seulement la marque. Correction : R5. Elle sert aussi de pont vers 800 €.

**E7 · À 2 000 €, la Palit à 1 200 € n'est pas justifiée, et la comparaison est laissée au spectateur (moyenne)**
> L167-171 « Une Palit 3090 était à 1 200 euros demandés. […] Additionne tes vrais prix, et compare avec la tour déjà montée. »

La MSI à 750 € (L140) reste le meilleur prix d'une 3090. Si tu prends la Palit, c'est parce que 750 € est un prix isolé : dis-le. Et fais le calcul à sa place : 1 201,99 + 785 (plafonds F8 : 150 + 105 + 140 + 140 + 165 + 85) = **1 986,99 €**, plus cher que la tour de Pontchâteau (1 851,99 €). Correction : R14.

**E8 · Le fichier de 22 gigas sur 24 gigas, sans mise en garde (moyenne)**
> L174-175 « il y a un fichier moins compressé qui pèse environ 22 gigas. »

24 − 22 = 2 gigas pour le moteur et la conversation. Tu l'expliques toi-même à L133-134 (le fichier, ce sont seulement les poids). Il faut le redire ici. Correction : R11.

**E9 · Une disponibilité dite au présent (mineure)**
> L126 « Pour l'avoir avant décembre, une autre était à 1 489,90 livrée. »

La livraison du 26 au 30/11 vaut pour une commande passée le 21/11. Un spectateur qui commande le 26 n'a aucune garantie. Correction : R12 (« annoncée avant décembre »).

**E10 · Les listes de pièces sont incomplètes (mineure)**
> L108-110 (pas de boîtier ni de refroidissement) · L169-170 (pas de carte mère)

Les plafonds F8 comptent ces pièces, et L30-31 annonçait 6 pièces. Corrections : R10 et R14.

**E11 · Huit verbes au présent et une deuxième date (mineure, règle 14)**
L3, L12, L79, L98, L126, L142, L180, L183, plus L11 « entre les 2 relevés ». Corrections : L3, L11 et L12 dans R1 ; L79 dans R7 ; L98 dans R9 ; L126 dans R12 ; L142 dans R11 ; L180 et L183 dans R13.

**E12 · Le mauvais marchand nommé deux fois (mineure)**
L98 « Chez Carrefour » : c'est la place de marché de Carrefour, vendeur DSGate. « Sur Carrefour » suffit. L193 « Amazon » au lieu de Memory PC (voir E3).

**E13 · « avec les frais » sans dire de quels frais (mineure)**
L26, L35, L91, L105, L141, L168 : leboncoin n'est jamais nommé, donc « avec les frais » ne dit rien à celui qui écoute. Nomme-le une fois, à la première annonce. Correction : R2.

**E14 · « cette même RX 6600 » (mineure)**
L33 : c'est le même modèle, pas la même carte, et la marque de celle de Tarbes n'est pas connue. Correction : R3.

**E15 · Comparer à la tour du début, oui, mais à configuration égale (mineure, à ne pas introduire)**
Tentation à éviter en corrigeant : « la TopConfig coûte 254 € de moins que l'OXIUM ». Elle n'a ni le même processeur, ni le même Windows, ni la même RAM. La comparaison loyale est la SYSTEMTREFF : même carte, même processeur, 1 489,90 € contre 1 523,99 € (34,09 € de moins). Correction : R12.

**E16 · Un trou de recherche, hors voix (à traiter au relevé du 25-26/11)**
Les recherches du 21/11 ne couvrent que les tours 5060 Ti, 9060 XT et 3060. Aucune recherche sur les tours neuves en RX 7900 XT (20 Go) ou 7900 XTX (24 Go) sous 2 000 €. Tant que cette recherche n'est pas faite, ne dis jamais « en neuf, tu ne dépasses pas 16 gigas ». R13 compare donc seulement les tours relevées.

**E17 · Des visuels qui font croire à un test (vigilance, règle 7)**
Dans script.md, remplace « Démo : mail à raccourcir » par « Exemple d'usage (texte à l'écran) ». Pour la 3090 « à côté d'un mètre », utilise le schéma à l'échelle (336 mm, fiche MSI), pas une photo.

### Vérification chiffre par chiffre

| Ligne | Chiffre dit | Source | Recalcul | État |
|---|---|---|---|---|
| L1-2 | 1 499 €, 16 Go | relevé § 1 (OXIUM Air, RX 9060 XT 16 Go) | — | ✅ |
| L3 | 2 049 €, 12 Go | relevé § 1, F17 (RTX 5070) | — | ✅ (présent, config différente : E4) |
| L4 | 1 299 et 1 799 € la veille | F9, F17 (20/11) | — | ✅ |
| L5 | +200, +250 | relevé § 1 | 1 499 − 1 299 = 200 ; 2 049 − 1 799 = 250 | ✅ |
| L6 | badge −50 € | relevé § 1 (barrés 1 549 / 2 099) | 1 549 − 1 499 = 50 | ✅ |
| L15 | 5 budgets, 500 à 2 000 | sources.md | — | ✅ |
| L18 | 6 Go derrière un 16 | F3, relevé § 2 | — | ⚠️ mise en page non sourcée (E2) |
| L19 | 3090, 24 Go | F10, F17 | — | ✅ |
| L25-26 | RX 6600 8 Go, Issy, 208 / 209,99 € | relevé § 4, F21 | — | ✅ |
| L27 | il reste au mieux 290 € | — | 500 − 209,99 = 290,01 | ✅ |
| L33-35 | Tarbes, Ryzen 7, 32 Go, 450 / 451,99 € | relevé § 4, F2 (5700X) | — | ✅ |
| L37 | 48 € | — | 500 − 451,99 = 48,01 | ✅ |
| L44 | environ 494 € livrée | relevé § 2, F1 | 469 + 24,99 = 493,99 | ✅ |
| L45-46 | Ryzen 5 à puce intégrée, 16 Go, SSD 500 Go | F1 (5655G) | — | ✅ |
| L50-51 | 7B en 4 bits, environ 4,7 Go | F13 | 3,99 + 0,69 = 4,68 | ✅ |
| L54 | 8 Go dédiés | F2 (fiche AMD) | — | ✅ |
| L56-58 | 27B sur 8 Go, carte NVIDIA | qwen-27b-8go (GTX 1080 Ti limitée à 8 Go, 7,63 Go) | — | ✅ mais incomplet (E6) |
| L61 | Cintra 799,99 € | relevé § 2, F3 | — | ✅ |
| L68 | 6 Go | F3 | — | ✅ |
| L69-70 | 14B en 4 bits, environ 9 Go | F13 | 3,99 + 3,99 + 1,01 = 8,99 | ✅ |
| L76-78 | Amazon 799,99 €, livraison gratuite, 3060 12 Go, 16 Go, SSD 512 | relevé § 3 (B0GQGW4278) | — | ✅ |
| L79 | « Core i7 », sans génération | relevé § 3 | — | ✅ (présent) |
| L82-83 | CSL 3060 12 Go, Ryzen 5, environ 824 € | relevé § 2, F6 | 799 + 24,99 = 823,99 | ✅ |
| L84 | 24 € au-dessus | — | 823,99 − 800 = 23,99 | ✅ |
| L87-90 | Châteauneuf, 550 €, 5600, 3060 12 Go, 32 Go, SSD 500 | relevé § 4, verification.md | — | ✅ |
| L91 | il reste environ 248 € | — | 800 − 551,99 = 248,01 | ✅ |
| L94 | 3060 de 8 Go | F4, F17 | — | ✅ |
| L98-99 | Arc B580, 999 €, 12 Go | relevé § 2, F5 | — | ✅ (vendeur DSGate : E12) |
| L101 | ReBAR recommandé par Intel | F5 | — | ✅ |
| L104-105 | Créteil 4060 Ti 16 Go, 450 / 451,99 € | relevé § 4, F7 | — | ✅ mais Talence à 325 € (E5) |
| L106 | 548 € | — | 1 000 − 451,99 = 548,01 | ✅ |
| L108-110 | 5600, B550, 32 Go DDR4, 1 To, 650 W | F8 (plafonds, 544 € avec boîtier) | 544 ≤ 548 | ✅ (boîtier oublié : E10) |
| L114 | 27B, 14,4 Go | F14 (UD-IQ4_XS) | — | ✅ |
| L117-118 | OXIUM avec le port > 1 500 € | relevé § 1 | 1 499 + 24,99 = 1 523,99 | ✅ |
| L121-123 | TopConfig, RX 9060 XT 16 Go, 5600X, 32 Go, 1 To, environ 1 270 € | relevé § 3 | 1 256,55 + 12,99 = 1 269,54 | ✅ |
| L124 | vendeur tiers, décembre, Windows 10 | relevé § 3 (5 au 16/12, W10 Pro) | — | ✅ |
| L126-127 | 1 489,90 €, 5700X, 16 Go, 1 To | relevé § 3 (SYSTEMTREFF) | — | ✅ (livraison au présent : E9) |
| L130-131 | 5060 Ti 16 Go 799,99 €, reste 700 € | relevé § 3 | 1 500 − 799,99 = 700,01 | ✅ |
| L135 | estimation LM Studio | F15 | — | ✅ |
| L140-141 | MSI 3090 750 €, en main propre, reste environ 748 € | relevé § 4, F10 | 1 500 − 751,99 = 748,01 | ✅ |
| L143 | la plupart entre 1 200 et 1 500 € | relevé § 4 | — | ✅ |
| L146 | presque 34 cm, 3 × 8 broches | F10 (336 mm) | — | ✅ |
| L149-150 | 850 W recommandés, bloc de 1 000 W | F10, F8 | — | ✅ |
| L152-155 | Yvetot, 3090, Ryzen 7, 32 Go, 1 300 €, 1,3/5 | relevé § 4, F20 (5800X3D, 16 avis) | — | ✅ |
| L160-162 | Pontchâteau, 1 850 €, 3090, 5800X3D, 32 Go, 1 To | relevé § 4, F20 | — | ✅ |
| L167-168 | Palit 1 200 / 1 201,99 €, reste 798 € | relevé § 4, F12 | 2 000 − 1 201,99 = 798,01 | ✅ |
| L169-170 | 5700X, 32 Go, 2 To, alimentation, grand boîtier | F8 (785 €) | 785 ≤ 798 | ✅ (carte mère oubliée : E10) |
| L174-175 | 22 Go | F14 (UD-Q6_K) | — | ✅ (marge : E8) |
| L179-183 | Wyvern 1 309 €, « 16GB » = RAM, carte 8 Go | relevé § 3 | — | ✅ (présent) |
| L184 | 500 € plus cher | — | 1 309 − 799,99 = 509,01 | ✅ (arrondi honnête) |
| L187-189 | Memory PC 1 719 €, livraison gratuite, 5060 Ti 16 Go, 5700X, 32 Go, 1 To | relevé § 3 | — | ✅ (le superlatif ne tient pas : E3) |
| L190-191 | CLAW 1 779,99 € hors port, Ryzen 5 | relevé § 2, F11 | — | ✅ |
| L192 | Sparkle environ 1 965 € livré | relevé § 2, F11 | 1 949,99 + 14,99 = 1 964,98 | ✅ |
| L197 | CSL 494 € | — | voir L44 | ✅ |
| L199 | 550 € d'occasion, 799,99 € neuve | relevé § 3, § 4 | — | ✅ |
| L202 | 1 270 € | — | voir L123 | ✅ |
| L207-208 | garantie légale de 2 ans chez un pro, aucune entre particuliers | F18 | — | ✅ |
| L209 | relevé du 21 novembre, France métropolitaine | relevé | — | ✅ |

---

## 4. Là où le spectateur décroche

1. **De 0:30 à 1:17 : la précaution, puis le plan.** L10-13 n'ouvre rien, et le plan finit à 77 s. C'est le défaut que vise la règle du 11/11 : la vidéo 16 Go a perdu un tiers de ses spectateurs juste après un plan trop vague. Correction : R1.
2. **L50-59 : du 7B au processeur, à la Radeon, au renvoi, à la précaution NVIDIA, puis le saut à 800 €.** Quatre idées en 30 s, et la partie finit sur « ne compte pas sur le même résultat ». Rien ne rend le palier suivant nécessaire. Correction : R5, avec le pont « 9 gigas, tes 8 ne suffisent plus ».
3. **L96-101 : la B580.** CUDA, Intel, Resizable BAR, sans jamais dire s'il faut la prendre. Le spectateur décroche sur le jargon. Le verdict tient en une ligne : même mémoire que la 3060, 175 € de plus. Correction : R9.
4. **L103-111 : 16 gigas sans dire pourquoi.** Le fichier de 14,4 gigas qui justifie ces 16 gigas n'arrive que 40 s plus tard (L114). Correction : R10.
5. **L120-131 : une rafale.** Environ 18 chiffres en 12 lignes et trois options de suite, sans choix entre elles. Correction : R12.
6. **L133-136 : LM Studio coincé entre la 5060 Ti et la 3090.** Le « Sauf que » arrive après « Ça te laisse 700 euros pour la base », sans lien. Correction : déplacé dans R10.
7. **L138-143 : 24 gigas sans dire pourquoi.** Même défaut qu'à 1 000 €, et le fichier de 22 gigas n'arrive qu'à L174 (1:20 plus tard). Correction : R11.
8. **Le palier de 1 500 € (L113-157) : 400 mots, environ 2:46.** C'est le palier le plus long. Les autres font de 1:04 à 2:13.
9. **L159-171 : « le piège revient »… sauf qu'il ne revient qu'à L179.** Le pont de L157 promet le piège, et la section commence par Pontchâteau puis par une liste de pièces. Paie la promesse tout de suite. Correction : R13.
10. **L186-193 : trois marchands et six chiffres à la suite.** Correction : R13.
11. **L207-212 : la traîne après le verdict.** La garantie sert au moment du premier achat entre particuliers (Tarbes), pas après le verdict. Correction : R4 et R16.

**Les fiches récitées :** « Ryzen X, Y gigas de RAM, SSD de Z » revient 10 fois (L33-34, L45-46, L77-78, L89-90, L121-122, L127, L153, L161-162, L170, L189). Dis la carte, le prix et la seule chose qui compte pour ce cas. Le reste va à l'écran.

---

## 5. Réécritures prêtes à coller

Les blocs ne se recoupent pas. Chaque bloc dit les lignes V3 qu'il remplace. Les lignes non citées restent telles quelles. Tout a été vérifié : 14 mots au plus par ligne, nombres en chiffres, pas de crochet, et une passe anti-IA (pas de « ce n'est pas A, c'est B » ajouté, pas de faux suspens).

### R1 · Hook et plan · remplace L1-22 (E2, E4, règles 3, 4, 5, 14)

```
Regarde cette tour : 1 499 euros le 21 novembre, badge « moins 50 » Black Friday.
La veille, la fiche affichait 1 299. Plus 200 euros en un jour.
Bon, des pièces avaient changé, et le site prévenait : ses prix suivent les composants.
Et pourtant, 16 gigas sur sa carte.
Celle à 2 049 euros, même site, RTX 5070 : seulement 12.
Avec ton budget, quelle carte te laisse de quoi finir la tour ?

Aujourd'hui, on va voir 5 budgets, de 500 à 2 000 euros,
en neuf et en occasion, avec des prix relevés en France.
À chaque fois, la carte d'abord, puis ce qu'il reste pour finir la tour.
Tu vas voir le kit à 800 euros
qui affiche 16 gigas, mais 6 sur la carte,
et la 3090 de 24 gigas qui ne rentre pas dans tous les boîtiers.
Et reste jusqu'à la fin :
je te dis quelle route je prendrais,
selon la taille du fichier d'IA que tu veux ouvrir.
```

- **Décompte :** question à 71 mots (29,4 s à l'écrit, environ 36 s à l'oral). « +200 euros en un jour » à 27 mots (11,2 s ; environ 16 s à l'oral). Plan fini à 1:07 au lieu de 1:17.
- **Pourquoi c'est plus loyal :** la précaution (les pièces, la phrase du site) arrive avant la question, et la RTX 5070 est nommée. Le +250 de la Vice saute, parce que le relevé ne dit pas si ses pièces ont changé.
- **Pour la règle 14 :** une seule date, le 21 novembre, dite dès la ligne 1 ; « la veille » s'y accroche. « Même site » garde le contraste de la V3 (deux tours chez OXIUM). C'est un fait du hook, pas une méthode de choix : la règle 13 n'est pas touchée.
- **Ligne 3 :** « suivent » reste au présent, parce que c'est la règle du site, pas un prix. [VISUEL] : la capture de la phrase d'OXIUM pendant cette ligne.
- **Ligne « qui affiche 16 gigas » :** à garder seulement si la capture du Cintra le confirme (E2). Sinon, mets : `avec 16 gigas de RAM, mais 6 sur la carte,`

### R2 · 500 € : nommer leboncoin · remplace L25-27 (E13)

```
Une RX 6600 de 8 gigas, seule, sur leboncoin à Issy-les-Moulineaux,
était à 208 euros demandés, 209,99 avec les frais du site.
Du coup, il te reste au mieux 290 euros pour les autres pièces.
```

Ça retire aussi le « soit » écrit et la répétition « reste… reste ».

### R3 · 500 € : répondre à « Tu mets quoi là-dedans ? » · remplace L32-33 (E14)

```
Avec 290 euros, c'est très serré.
Alors avant de commander la Radeon, ouvre aussi les annonces de PC entiers.
À Tarbes, il y en avait un avec une RX 6600 aussi,
```

Les lignes L30-31 (la liste des 6 pièces) et L34-35 restent.

### R4 · La garantie, au moment du premier achat entre particuliers · insère après L41, supprime L207-208

```
Entre particuliers, la garantie légale ne s'applique pas.
Chez un vendeur pro en France, elle dure 2 ans, même en occasion.
```

### R5 · Coupe chez CSL, renvoi juste, pont vers 800 € · remplace L45-46, L53 et L56-59 (E6, transition molle)

L45-46 devient :
```
Dedans, un Ryzen 5 avec sa puce graphique intégrée, et 16 gigas de RAM.
```
L53 devient :
```
Par contre, sur la RX 6600 de Tarbes, vérifie que ton logiciel la gère.
```
L56-59 devient :
```
Dans une vidéo précédente, on a vu une mesure
où Qwen 27B tenait sur 8 gigas, avec un fichier très compressé.
Sauf que ce fichier ratait bien plus de tâches d'agent,
et la mesure venait d'une carte NVIDIA.
Alors sur la Radeon, ne compte pas dessus sans vérifier.
Et le Qwen suivant, celui de 14 milliards en 4 bits,
pèse environ 9 gigas. Là, tes 8 gigas ne suffisent plus.
```

Le renvoi reste unique et sans date. Il ne promet plus « 27B sur ta carte ». Et le 9 gigas, posé ici, rend le palier de 800 € nécessaire.

### R6 · 800 € : le piège, sans doublon · remplace L63 et L69-71 (E2, phrases écrites)

L63 devient (seulement si la capture le confirme) :
```
Sur la fiche, tu vois une RTX 3050
```
L69-71 devient :
```
Et le Qwen de 9 gigas, rien que ses poids, ne rentre pas dedans.
```

Ça retire le « Or » et la phrase écrite « Ses poids dépassent déjà la mémoire de la 3050 ». Le 9 gigas est déjà posé dans R5.

### R7 · 800 € : une fiche de moins à réciter · remplace L77-79 (règle 14, coupe)

```
Dedans, une RTX 3060 de 12 gigas,
sauf que sa fiche disait juste « Core i7 », sans génération ni référence.
```

### R8 · 800 € en occasion : coupe · remplace L89-90

```
Un Ryzen 5 5600, la même 3060 de 12 gigas, 32 gigas de RAM.
```

### R9 · 1 000 € : la B580 tranchée · remplace L98-101 (E12, décrochage 3)

```
Sur Carrefour, une tour avec une Intel Arc B580 était à 999 euros.
Même 12 gigas sur la carte, 175 euros plus cher que la tour CSL.
Et ton logiciel doit savoir utiliser l'Intel.
```

Calcul : 999 − 823,99 = 175,01. Le Resizable BAR saute de la voix : il ne sert que si on achète la tour, et la phrase dit maintenant de ne pas la prendre. Garde-le à l'écran si tu veux.

### R10 · 1 000 € : pourquoi 16 gigas, Talence, la base complète · remplace L103-111, supprime L133-136 (E5, E10, décrochages 4 et 6)

```
Sauf qu'avec 1 000 euros, tu peux viser 16 gigas dédiés.
Avec 16 gigas, tu peux ouvrir un fichier de 14,4 gigas,
celui d'un Qwen de 27 milliards, toujours compressé.
Sur une carte de 16, il peut tenir en entier.
Par contre, ce fichier, c'est seulement les poids du modèle.
Ta conversation prend aussi de la place sur la carte.
Dans LM Studio, tu peux estimer la mémoire selon la longueur de conversation.
Commence court, puis refais l'estimation avec ton vrai document.

À Créteil, une RTX 4060 Ti de 16 gigas était à 450 euros demandés.
Avec les frais, 451,99. Ça laisse au mieux 548 euros pour la tour.
Une autre était à 325 euros à Talence, mais son vendeur n'avait aucun avis.
Avec tes 548 euros, je chercherais un Ryzen 5 5600 d'occasion,
une carte mère B550 et 32 gigas de DDR4,
puis un SSD d'un téra, un bloc neuf de 650 watts et un boîtier.
J'ai mis à l'écran le maximum que je mettrais dans chaque pièce.
```

Si tu préfères retenir Talence, inverse les deux annonces : 1 000 − 326,99 = 673,01 € pour la base.

### R11 · 1 500 € : à quoi servent 24 gigas, dit tout de suite · remplace L138-143, supprime L173-177 (E8, E11, décrochage 7)

```
Mais à ce budget, on voit aussi des RTX 3090 d'occasion.
Et là, on passe à 24 gigas.
Sur le même Qwen de 27 milliards, il y a un fichier moins compressé
qui pèse environ 22 gigas, mais il laisse peu de place à ta conversation.
Sinon, tu gardes celui de 14,4, et ton document a de la marge.
Une MSI était à 750 euros demandés, en main propre.
Avec les frais, il te reste environ 748 euros pour la base.
Sauf que ce prix-là était très bas, et le vendeur n'avait qu'un avis.
La plupart des autres étaient entre 1 200 et 1 500 euros.
```

Le vendeur avec un seul avis vient du relevé § 4 (Raj, 5/5, 1 avis). « En main propre » remplace « en retrait », qu'on peut comprendre comme « annonce retirée ».

### R12 · 1 500 € neuf : moins de fiche, une comparaison juste · remplace L113-131 (E9, E15, décrochage 5)

```
Tu te souviens de la tour à 16 gigas du début ?
Chez OXIUM, avec le port, elle dépassait les 1 500 euros.
Alors à 1 500 euros, regarde Amazon.
Une tour avec une Radeon RX 9060 XT de 16 gigas
et 32 gigas de RAM revenait à environ 1 270 euros livrée.
Par contre, vendeur tiers, livraison en décembre, et Windows 10.
Une autre avait la même carte et le même processeur qu'au début.
Elle était à 1 489,90 livrée, 34 euros de moins, annoncée avant décembre.
Mais son tableau technique se contredisait : relis la fiche avant de payer.
Et sinon, tu montes autour de la carte, en restant chez NVIDIA.
La RTX 5060 Ti de 16 gigas neuve était à 799,99 sur Amazon.
Ça te laisse 700 euros pour la base.
```

Calcul : 1 523,99 − 1 489,90 = 34,09, et l'OXIUM est un prix « dès », donc l'écart est au moins de 34 €. Le fichier de 14,4 gigas et le paragraphe LM Studio sont partis dans R10 : L114-116 disparaissent avec ce bloc, et L133-136 sont à supprimer (R10) pour ne pas les avoir en double.

**R12 bis · coupe à la 3090 · remplace L145** : `Regarde-la à côté d'un mètre.`

**R12 ter · Yvetot, la config entière, pour la récolter à Pontchâteau · remplace L152-156**

```
J'ai aussi trouvé une tour entière à Yvetot,
avec une 3090, un Ryzen 7 5800X3D et 32 gigas de RAM.
Elle était à 1 300 euros demandés.
Sauf que le vendeur affichait 1,3 sur 5, sur 16 avis.
Donc je garde le prix pour comparer, et je passe mon tour.
```

L157 reste (« Et tu vas voir, à 2 000 euros, le piège des 16 gigas revient. »).

### R13 · 2 000 € : le piège d'abord, puis la leçon du hook · remplace L159-193 (avec R14) (E3, E16, décrochages 9 et 10)

```
À 2 000 euros, méfie-toi de cette tour à 1 309 euros sur Amazon.
Son titre disait « RTX 5060 Ti » et « 16GB ».
Tu le sens venir ?
En fait, les 16, c'est encore la RAM.
Dans le tableau de la fiche, la carte avait 8 gigas.
Même piège que le kit à 800 euros, juste 500 euros plus cher.

Côté NVIDIA, avec une RTX 5060 Ti de 16 gigas,
la moins chère vérifiée était chez Memory PC, sur Amazon.
1 719 euros, livraison gratuite.
Moins chère que le CLAW de Top Achat et le Sparkle de Cybertek.
Sauf que la tour Radeon à 1 270 euros avait déjà 16 gigas.
Ces 450 euros t'achètent NVIDIA, un Ryzen 7, Windows 11, une livraison plus tôt.
La mémoire vidéo, elle, reste à 16.
```

- **Calculs :** 1 719 − 1 269,54 = 449,46. La livraison est plus tôt : du 28/11 au 1/12, contre du 5 au 16/12. Ryzen 7 5700X contre Ryzen 5 5600X, Windows 11 Pro contre Windows 10 Pro.
- **« vérifiée » :** ce mot tient tant que la fiche SYSTEMTREFF à 1 709,90 € n'est pas ouverte (E3).
- **À l'écran :** les prix du CLAW et du Sparkle (1 779,99 € hors port ; 1 949,99 + 14,99 = 1 964,98 €).

### R14 · 2 000 € : les 3090, avec le calcul fait · suite de R13, dans le même remplacement de L159-193

```
Pour 24 gigas, regarde cette annonce à Pontchâteau : 1 850 euros pour la tour.
Sur le papier, la même config qu'à Yvetot.
Remise en main propre, donc demande la référence du bloc
et une démonstration avant de te déplacer.

Et si tu la montes toi-même ?
Si la MSI à 750 est partie, compte plutôt 1 200, comme cette Palit.
Avec les frais, 1 201,99, donc il te reste au mieux 798 euros.
Aux plafonds à l'écran, ton montage pourrait monter jusqu'à 1 987 euros.
Au pire, plus cher que la tour de Pontchâteau, mais tu choisis chaque pièce.
```

- **Calcul :** 1 201,99 + 785 = 1 986,99. « Pourrait monter jusqu'à » et « au pire », parce que ce sont des plafonds, des enveloppes de calcul (F8), pas des prix relevés.
- **La même config qu'à Yvetot :** relevé § 4 (3090, 5800X3D, 32 Go, 1 To dans les deux annonces). « Sur le papier », parce que le bloc et la carte mère ne sont pas connus (F20).
- **Ce qui part :** les lignes du 22 gigas (L173-177) sont dans R11.

### R16 · Verdict et fin · remplace L195-213 (E1, règle 9)

```
Alors, la route que je prendrais, selon ton fichier.
Avec le Qwen de 4,7 gigas, commence par ton PC actuel.
Si tu pars de zéro, la tour CSL à 494 euros suffit pour démarrer.
Pour le Qwen de 9 gigas, je chercherais la 3060 de 12 gigas.
D'occasion à 550 euros,
ou la tour neuve à 799,99, si le vendeur nomme le processeur.

Pour le fichier de 14,4 gigas, je prendrais une carte de 16.
Le moins cher : la 4060 Ti d'occasion, si ta base tient dans 548 euros.
En neuf, la tour Radeon à 1 270, si décembre ne te gêne pas.
Je passerais aux 24 si l'estimation de mon document le justifie,
et seulement si je peux vérifier la 3090 et son alimentation.
Si tu n'es pas en France, refais le total livré chez toi.
Et note le prix avant le Black Friday :
tu as vu qu'il peut bouger en un jour.
Allez, salut !
```

- **Calcul :** 1 000 − 451,99 = 548,01, et les plafonds F8 de la base font 544 €. Le conditionnel « si ta base tient dans 548 euros » suit `verification.md` (garder le conditionnel pour les paniers calculés).
- **Ce qui part :** la garantie (dans R4) et la date (dans R1).
- **La fin :** le verdict, une ligne pratique pour le public hors de France, le rappel du hook, puis le salut. « si le processeur tient » devient « si le vendeur nomme le processeur », ce qui dit ce que tu veux vraiment.

---

## 6. Longueur et coupes

La V3 fait **1 813 mots** (le décompte de script.md donne environ 1 805), soit 12:30 à 145 mots/min. Compte plutôt 13 min et plus avec les chiffres dits en entier. On est au-dessus des 1 800 mots.

| Coupe | Lignes V3 | Mots gagnés |
|---|---|---|
| Précaution et conseil avant le plan (fondus dans le hook) | L10-13 | −38 (+14 réinjectés dans R1) |
| Le +250 et les 1 799 € de la Vice | L4-5 | −8 |
| SSD du CSL | L45-46 | −6 |
| « Or… Ses poids dépassent… » | L69-71 | −9 |
| RAM et SSD de la tour Amazon à 799,99 € | L77-78 | −8 |
| SSD de Châteauneuf | L89-90 | −3 |
| Resizable BAR | L101 | −11 |
| « Avant d'imaginer la carte sur ton bureau » | L145 | −8 |
| « En cherchant directement » | L152 | −4 |
| Fiche de Pontchâteau (récoltée par « la même config qu'à Yvetot ») | L161-162 | −10 |
| Fiche de Memory PC | L189 | −10 |
| Date et France en fin de vidéo (passées dans le plan) | L209 | −9 |

Avec les ajouts (pont vers 800 €, pourquoi 16 et 24 gigas, Talence, leçon du hook à 2 000 €, calcul de Pontchâteau, route à 1 000 €), **la V4 assemblée fait 1 755 mots**, soit 12:06 à 145 mots/min. Aucune ligne ne dépasse 14 mots, et il y a 45 liaisons, soit 2,6 pour 100 mots. Elle est en annexe.

**Coupes en option, si tu veux passer sous 1 700 mots (environ −55) :**
- la B580 entière (R9, 3 lignes, −31) : elle n'apporte rien de plus que la 3060 ;
- la ligne CLAW et Sparkle de R13 (−12) : les prix restent à l'écran, et la règle 13 est tenue par le visuel ;
- « Dans mon calcul, j'ai réservé un bloc neuf de 1 000 watts. » (L150, −11) : le chiffre est déjà dans les plafonds à l'écran.

---

## 7. Tableau de bord

| Axe | Note | En une phrase |
|---|---|---|
| 1. Promesse | 🟢 | Les 5 budgets, en neuf et en occasion, sont tous traités, et la route finale est donnée. |
| 2. Alignement | 🟢 | Pas de sponsor, les marchands sont nommés et souvent défendus. Seul « cache » (L18) prête une intention. |
| 3. Problème profond | 🟠 | La peur de se faire avoir au Black Friday est posée (hook) et rappelée (fin), mais les pièges ne la relient pas assez (« tu te souviens du badge ? »). |
| 4. Public et complexité | 🟠 | Tout est en France, avec des remises en main propre à Tarbes ou à Pontchâteau, pour un public à 63 % africain. La méthode (la carte d'abord, la RAM qui n'est pas la VRAM, 8 ou 12 gigas) voyage : mets-la en avant. Jargon : ReBAR, « poids ». |
| 5. Valeur et originalité | 🟢 | Les pièges de fiches (Cintra, Wyvern) et le calcul de ce qu'il reste après la carte : c'est ce que le spectateur ne trouve pas sur une fiche produit. |
| 6. Structure et transformation | 🟠 | Chaque palier de mémoire est justifié un budget trop tard, et le verdict oublie la route à 1 000 €. |
| 7. Histoire | 🟠 | Une enquête par budgets, sans crise. Pour un guide, ça suffit, mais la leçon du hook (payer plus ≠ plus de mémoire) pouvait servir de fil. |
| 8. Mais / donc | 🟢 | Il y en a partout, mais ils sont trop souvent appariés (« Sauf que… Donc… »). |
| 9. Engagement actif | 🟢 | « Tu mets quoi là-dedans ? », « Tu repères où ils sont ? », « Tu le sens venir ? », « Tu te souviens… ». |
| 10. Rythme et liaisons | 🟠 | 2,3 liaisons pour 100 mots, mais 10 fiches récitées et 6 « Donc + ordre ». |
| 11. Tics d'IA | 🟢 | Une seule fausse opposition (« C'est pas une carte graphique, c'est une planche à repasser »), tolérée parce que c'est une blague. « La vraie bonne affaire » et « c'est encore mieux » annoncent au lieu de montrer. |
| S1. Les 30 premières secondes | 🟠 | La question passe à l'écrit (29,8 s), pas à l'oral. Le chiffre fort arrive après 15 s. Le remplissage suit la question. |
| S2. Le pont | 🔴 | C'est une précaution, qui n'ouvre aucune question. |
| S3. Les retournements | 🟢 | Un « sauf que » toutes les 20 à 30 s. |
| S4. Planté / récolté | 🟢 | La tour à 16 gigas (L113), le piège des 16 gigas (Cintra puis Wyvern), le prix qui bouge (du hook à la fin). R12 ter et R14 ajoutent Yvetot / Pontchâteau. |
| S5. Personnages et enjeu | 🟠 | Seul « tu », avec ton budget. Les vendeurs restent des silhouettes, et c'est voulu (pas de pseudo). |
| S6. La fin | 🟠 | Le verdict et le rappel du hook sont bons, mais il y a une traîne avant (garantie, date). R16 la retire. |

---

## 8. Ce qu'il faut garder

- « Tu repères où ils sont, ces 16 gigas ? » (L65) : le spectateur cherche lui-même, et c'est le meilleur moment de la vidéo.
- « Si le vendeur reste vague, garde tes 500 euros. » (L41) : un conseil d'ami, en 8 mots.
- « 24 euros au-dessus du budget, mais tu sais ce que tu achètes. » (L84) : tu choisis, avec la raison.
- « C'est pas une carte graphique, c'est une planche à repasser. » (L147) et « je passe mon tour » (L156) : ton humour. Garde-les, ils sont rares dans le script.
- « Même piège que le kit à 800 euros, juste 500 euros plus cher. » (L184) : une vraie récolte.
- « Tu te souviens de la tour à 16 gigas du début ? » (L113) et « tu as vu qu'il peut bouger en un jour » (L212) : les deux rappels du hook.
- La discipline des chiffres : chaque montant donne le prix demandé, puis les frais, puis ce qu'il reste. Ne la casse pas en corrigeant.

## 9. Plan d'action

1. Fais la capture de la fiche Cintra, sur ordinateur et sur téléphone (E2). Si le « 16 Go » n'apparaît pas seul, adapte R1, R6 et L184.
2. Colle R1 (hook et plan), R5 (renvoi et pont) et R16 (verdict) : ce sont les trois corrections qui changent la rétention et la logique.
3. Colle R10, R11 et R12, avec leurs suppressions (L133-136 ; L173-177 si tu ne prends pas R13), pour que chaque palier de mémoire arrive avec son fichier.
4. Colle R13 et R14 (2 000 €), puis les petits blocs (R2, R3, R4, R6 à R9, R12 bis et ter).
5. Au relevé du 25-26/11 : rouvre l'OXIUM, toutes les annonces leboncoin (surtout la MSI à 750 €, Talence et Châteauneuf), la fiche SYSTEMTREFF à 1 709,90 €, et cherche des tours neuves en RX 7900 XT ou XTX sous 2 000 € (E16).

---

## Annexe · V4 assemblée (tous les blocs R appliqués)

À coller dans `teleprompteur.txt` et `teleprompteur.md` seulement si tu prends tous les blocs. Sinon, applique-les un par un. Version avec la ligne de plan « qui affiche 16 gigas » : à adapter si la capture du Cintra dit autre chose (E2).

```
Regarde cette tour : 1 499 euros le 21 novembre, badge « moins 50 » Black Friday.
La veille, la fiche affichait 1 299. Plus 200 euros en un jour.
Bon, des pièces avaient changé, et le site prévenait : ses prix suivent les composants.
Et pourtant, 16 gigas sur sa carte.
Celle à 2 049 euros, même site, RTX 5070 : seulement 12.
Avec ton budget, quelle carte te laisse de quoi finir la tour ?

Aujourd'hui, on va voir 5 budgets, de 500 à 2 000 euros,
en neuf et en occasion, avec des prix relevés en France.
À chaque fois, la carte d'abord, puis ce qu'il reste pour finir la tour.
Tu vas voir le kit à 800 euros
qui affiche 16 gigas, mais 6 sur la carte,
et la 3090 de 24 gigas qui ne rentre pas dans tous les boîtiers.
Et reste jusqu'à la fin :
je te dis quelle route je prendrais,
selon la taille du fichier d'IA que tu veux ouvrir.

À 500 euros, regarde ce qui se passe si tu commences par la carte.
Une RX 6600 de 8 gigas, seule, sur leboncoin à Issy-les-Moulineaux,
était à 208 euros demandés, 209,99 avec les frais du site.
Du coup, il te reste au mieux 290 euros pour les autres pièces.
Tu mets quoi là-dedans ?

Il te faut le processeur avec son refroidissement, une carte mère, de la RAM,
un SSD, l'alimentation et un boîtier.
Avec 290 euros, c'est très serré.
Alors avant de commander la Radeon, ouvre aussi les annonces de PC entiers.
À Tarbes, il y en avait un avec une RX 6600 aussi,
un Ryzen 7 et 32 gigas de RAM.
Le vendeur demandait 450 euros pour la tour, 451,99 avec les frais.

Donc il te reste au mieux 48 euros, avant la livraison.
Là, tu veux savoir s'il y a un SSD dedans.
Tu demandes sa capacité, une photo de l'étiquette du bloc d'alimentation,
et tu veux voir la machine démarrer.
Si le vendeur reste vague, garde tes 500 euros.
Entre particuliers, la garantie légale ne s'applique pas.
Chez un vendeur pro en France, elle dure 2 ans, même en occasion.

Et si tu veux acheter neuf ?
Chez CSL, une tour revenait à environ 494 euros livrée.
Dedans, un Ryzen 5 avec sa puce graphique intégrée, et 16 gigas de RAM.
Sauf que la puce graphique partage la RAM avec le reste du PC.
Donc pour commencer, je prendrais le petit Qwen sur le processeur.

Par exemple, sa version à 7 milliards de paramètres,
compressée en 4 bits, pèse environ 4,7 gigas sur le disque.
Donne-lui un mail à raccourcir. Et regarde si sa réponse te convient.
Par contre, sur la RX 6600 de Tarbes, vérifie que ton logiciel la gère.
Tu pourrais alors charger ce même fichier sur ses 8 gigas dédiés.

Dans une vidéo précédente, on a vu une mesure
où Qwen 27B tenait sur 8 gigas, avec un fichier très compressé.
Sauf que ce fichier ratait bien plus de tâches d'agent,
et la mesure venait d'une carte NVIDIA.
Alors sur la Radeon, ne compte pas dessus sans vérifier.
Et le Qwen suivant, celui de 14 milliards en 4 bits,
pèse environ 9 gigas. Là, tes 8 gigas ne suffisent plus.

À 800 euros, le kit neuf Cintra de Top Achat était à 799,99.
Il faut le monter toi-même, mais bon, c'est presque un jeu de Lego.
Sur la fiche, tu vois une RTX 3050
et, un peu plus bas, 16 gigas.
Tu repères où ils sont, ces 16 gigas ?

En fait, c'est la RAM du PC.
Si tu descends jusqu'au nom complet de la carte graphique, tu lis 6 gigas.
Et le Qwen de 9 gigas, rien que ses poids, ne rentre pas dedans.
Donc pour tout charger sur la carte, raye ce kit.
Si cette vidéo t'a évité un mauvais achat, abonne-toi.

Alors, au même prix, qu'est-ce qu'on trouve ?
Sur Amazon, une tour montée était à 799,99 euros, livraison gratuite.
Dedans, une RTX 3060 de 12 gigas,
sauf que sa fiche disait juste « Core i7 », sans génération ni référence.
Donc avant de payer, fais préciser le processeur au vendeur.

S'il ne répond pas, la tour CSL avec la même 3060 de 12 gigas
et un Ryzen 5 revenait à environ 824 euros livrée.
24 euros au-dessus du budget, mais tu sais ce que tu achètes.

Et en occasion, c'est encore mieux.
À Châteauneuf-les-Martigues, une tour était à 550 euros demandés,
remise en main propre.
Un Ryzen 5 5600, la même 3060 de 12 gigas, 32 gigas de RAM.
Avec les frais, il te reste environ 248 euros sur tes 800.

Par contre, garde bien le « 12 gigas » dans ta recherche.
NVIDIA a aussi vendu une 3060 de 8 gigas.

À 1 000 euros, en neuf, tu peux déjà t'arrêter à cette 3060.
Surtout si ton logiciel demande CUDA, la technologie de NVIDIA.
Sur Carrefour, une tour avec une Intel Arc B580 était à 999 euros.
Même 12 gigas sur la carte, 175 euros plus cher que la tour CSL.
Et ton logiciel doit savoir utiliser l'Intel.

Sauf qu'avec 1 000 euros, tu peux viser 16 gigas dédiés.
Avec 16 gigas, tu peux ouvrir un fichier de 14,4 gigas,
celui d'un Qwen de 27 milliards, toujours compressé.
Sur une carte de 16, il peut tenir en entier.
Par contre, ce fichier, c'est seulement les poids du modèle.
Ta conversation prend aussi de la place sur la carte.
Dans LM Studio, tu peux estimer la mémoire selon la longueur de conversation.
Commence court, puis refais l'estimation avec ton vrai document.

À Créteil, une RTX 4060 Ti de 16 gigas était à 450 euros demandés.
Avec les frais, 451,99. Ça laisse au mieux 548 euros pour la tour.
Une autre était à 325 euros à Talence, mais son vendeur n'avait aucun avis.
Avec tes 548 euros, je chercherais un Ryzen 5 5600 d'occasion,
une carte mère B550 et 32 gigas de DDR4,
puis un SSD d'un téra, un bloc neuf de 650 watts et un boîtier.
J'ai mis à l'écran le maximum que je mettrais dans chaque pièce.

Tu te souviens de la tour à 16 gigas du début ?
Chez OXIUM, avec le port, elle dépassait les 1 500 euros.
Alors à 1 500 euros, regarde Amazon.
Une tour avec une Radeon RX 9060 XT de 16 gigas
et 32 gigas de RAM revenait à environ 1 270 euros livrée.
Par contre, vendeur tiers, livraison en décembre, et Windows 10.
Une autre avait la même carte et le même processeur qu'au début.
Elle était à 1 489,90 livrée, 34 euros de moins, annoncée avant décembre.
Mais son tableau technique se contredisait : relis la fiche avant de payer.
Et sinon, tu montes autour de la carte, en restant chez NVIDIA.
La RTX 5060 Ti de 16 gigas neuve était à 799,99 sur Amazon.
Ça te laisse 700 euros pour la base.

Mais à ce budget, on voit aussi des RTX 3090 d'occasion.
Et là, on passe à 24 gigas.
Sur le même Qwen de 27 milliards, il y a un fichier moins compressé
qui pèse environ 22 gigas, mais il laisse peu de place à ta conversation.
Sinon, tu gardes celui de 14,4, et ton document a de la marge.
Une MSI était à 750 euros demandés, en main propre.
Avec les frais, il te reste environ 748 euros pour la base.
Sauf que ce prix-là était très bas, et le vendeur n'avait qu'un avis.
La plupart des autres étaient entre 1 200 et 1 500 euros.

Regarde-la à côté d'un mètre.
Elle fait presque 34 centimètres et demande 3 prises à 8 broches.
C'est pas une carte graphique, c'est une planche à repasser.
Donc vérifie le dégagement à l'intérieur du boîtier, ventilateurs en place.
MSI recommande une alimentation de 850 watts.
Dans mon calcul, j'ai réservé un bloc neuf de 1 000 watts.

J'ai aussi trouvé une tour entière à Yvetot,
avec une 3090, un Ryzen 7 5800X3D et 32 gigas de RAM.
Elle était à 1 300 euros demandés.
Sauf que le vendeur affichait 1,3 sur 5, sur 16 avis.
Donc je garde le prix pour comparer, et je passe mon tour.
Et tu vas voir, à 2 000 euros, le piège des 16 gigas revient.

À 2 000 euros, méfie-toi de cette tour à 1 309 euros sur Amazon.
Son titre disait « RTX 5060 Ti » et « 16GB ».
Tu le sens venir ?
En fait, les 16, c'est encore la RAM.
Dans le tableau de la fiche, la carte avait 8 gigas.
Même piège que le kit à 800 euros, juste 500 euros plus cher.

Côté NVIDIA, avec une RTX 5060 Ti de 16 gigas,
la moins chère vérifiée était chez Memory PC, sur Amazon.
1 719 euros, livraison gratuite.
Moins chère que le CLAW de Top Achat et le Sparkle de Cybertek.
Sauf que la tour Radeon à 1 270 euros avait déjà 16 gigas.
Ces 450 euros t'achètent NVIDIA, un Ryzen 7, Windows 11, une livraison plus tôt.
La mémoire vidéo, elle, reste à 16.

Pour 24 gigas, regarde cette annonce à Pontchâteau : 1 850 euros pour la tour.
Sur le papier, la même config qu'à Yvetot.
Remise en main propre, donc demande la référence du bloc
et une démonstration avant de te déplacer.

Et si tu la montes toi-même ?
Si la MSI à 750 est partie, compte plutôt 1 200, comme cette Palit.
Avec les frais, 1 201,99, donc il te reste au mieux 798 euros.
Aux plafonds à l'écran, ton montage pourrait monter jusqu'à 1 987 euros.
Au pire, plus cher que la tour de Pontchâteau, mais tu choisis chaque pièce.

Alors, la route que je prendrais, selon ton fichier.
Avec le Qwen de 4,7 gigas, commence par ton PC actuel.
Si tu pars de zéro, la tour CSL à 494 euros suffit pour démarrer.
Pour le Qwen de 9 gigas, je chercherais la 3060 de 12 gigas.
D'occasion à 550 euros,
ou la tour neuve à 799,99, si le vendeur nomme le processeur.

Pour le fichier de 14,4 gigas, je prendrais une carte de 16.
Le moins cher : la 4060 Ti d'occasion, si ta base tient dans 548 euros.
En neuf, la tour Radeon à 1 270, si décembre ne te gêne pas.
Je passerais aux 24 si l'estimation de mon document le justifie,
et seulement si je peux vérifier la 3090 et son alimentation.
Si tu n'es pas en France, refais le total livré chez toi.
Et note le prix avant le Black Friday :
tu as vu qu'il peut bouger en un jour.
Allez, salut !
```
