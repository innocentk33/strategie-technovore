# Grill V4 : « 32 Go pour Qwen 27B : les prix, les routes et leurs pièges » (20/11/2026)

> Critiqué : [`teleprompteur.txt`](teleprompteur.txt) (ce qui sera dit), puis [`script.md`](script.md) (voix + [VISUEL]), version aux prix du 20/11. Comparé à [`grill-v3.md`](grill-v3.md) (7/10, version du 19/11). Méthode : skill `youtube-script-grill`, mode B, **variante storytelling** (test des 30 secondes, 11 axes + S1 à S6) ; règles de `.claude/rules/script.md`.
>
> **Pages rouvertes le 20/11/2026** par moi, sans panier ni achat : les 8 fiches LDLC (WebFetch), Amazon et GMKtec (navigateur intégré : WebFetch renvoyait 503 et 429), `config.json` de Qwen et l'API Hugging Face, la page de spécifications Gigabyte de ta carte mère, la page Corsair de la RM1000e, les notes de version CUDA (actuelles et archive 13.0), le README de llama.cpp, les fiches service-public F11094, F10485 et F11007. Ce que je n'ai **pas** pu lire est listé en section 3.
>
> **Débit** : 1667 mots au téléprompteur (compte par espaces, identique à l'en-tête). À 145 mots/min : 11 min 30. À ton débit monté (≈ 233 mots/min, mesuré dans `../meme-carte-plus-rapide/grill-v3.md`) : ≈ 7 min 10.

## 1. Verdict

**7,5/10 tel quel. 8,5/10 avec les 2 corrections bloquantes et les importantes (3 à 10).**

La V4 a appliqué presque tout le grill V3 : « ce jour-là » à la place de « ce soir », « de mon relevé », « la même quantité de mémoire », la réponse aux 900 € (« Pas un giga de plus »), la marge du hook récoltée sur le Mac mini, un verdict par profil qui nomme une carte, « Prends la mienne ». Le hook tient toujours, la question tombe à 19 s à ton débit, et la première partie commence par une réponse.

Les deux nouveaux problèmes viennent du relevé du 20/11. **Le fichier 4 bits a été remis en ligne le 11/11 et pèse maintenant 16,56 Go** : l'addition fait 31,4, plus 31,3. Et **le plan dit « prix relevés chez LDLC »**, alors que la paire la plus importante du verdict vient d'Amazon. Le gros défaut de récit, lui, est neuf : la paire de 9060 XT à 1400 € a fait entrer **deux « 500 euros » différents en 12 lignes**, et elle a ramené un « sauf que » de plus. Il y en a maintenant 11, dont 3 d'affilée dans la route 1. C'est devenu le « Bref » de la V3.

## 2. Test des 30 secondes

Temps cumulés au téléprompteur : à 145 mots/min, puis à 233 entre parenthèses.

| Tranche | Ce que dit la voix | Verdict |
|---|---|---|
| 0-6 s (0-4) | > « Tu peux payer 900 euros de plus pour la même quantité de mémoire : » | **Vert.** « Tu » au premier mot, le chiffre fort au 4e mot, raccord avec la miniature « 32 GO / PAS CHER ? » (deux cartes). |
| 6-21 s (4-13) | > « 32 gigas sur une seule carte, chez le même marchand, le même jour. Et même avec ces 32 gigas, Qwen 27B en 4 bits, avec sa conversation la plus longue, te laisse moins d'un giga de marge. » | **Vert.** La preuve est à l'écran (deux prix, LDLC, 20/11, en stock : relus, exacts). L'enjeu monte : même la carte chère est juste. « Moins d'un giga » tient toujours avec le nouveau fichier (marge ≈ 0,57 Gio). |
| 21-31 s (13-19) | > « Du coup, pour faire tourner Qwen 27B chez toi, quelle route vers 32 gigas tu prends, et quel piège elle te cache ? » | **Vert.** Une seule question, en mots simples. Elle finit au 74e mot : 30,6 s à 145 mots/min (pile à la limite), 19 s à ton débit. |
| Plan, 31-55 s (19-34) | > « Aujourd'hui, on va voir… avec leurs prix relevés chez LDLC le 20 novembre… Et à la fin, ce que ces 900 euros de plus t'achètent vraiment, et la route que je prendrais selon le PC que tu as déjà. » | **Orange.** Quatre livrables concrets et une raison de rester (les 900 €, la route finale). « Aujourd'hui » arrive après 15 s à tous les débits. Mais « chez LDLC » est faux pour deux offres (B2). |
| Pont, 55 s (34) | > « Première réponse, et elle peut déjà t'économiser une carte : … 24 gigas suffisent. Donc les 32, en fait, c'est pour lui laisser une longue mémoire. » | **Vert.** Une réponse qui rend service, puis une deuxième question (pourquoi la mémoire grossit). |

**Budget** : 74 mots jusqu'à la fin de la question. Aucun salut, aucun contexte, aucun « dans cette vidéo » avant 15 s, aucune phrase de remplissage. L'abonnement arrive vers 4:40 (2:55 à ton débit), après « 2 cartes, c'est de la place, pas de la vitesse » : bien placé.

**À changer dans les 30 s** : rien. Le plan, juste après, a une erreur (B2).

### Le hook à 900 € ou le Mac mini ?

Garde les 900 €. Trois raisons :
- **La miniature** montre deux cartes et « PAS CHER ? ». Le hook à 900 € y répond directement ; un Mac mini à l'ouverture la contredirait.
- **L'honnêteté** : le Mac a 32 gigas *partagés*, un délai de plus de 15 jours, et ton propre verdict dit que la conversation complète n'y rentre pas. Ouvrir sur lui, ce serait promettre une route que la vidéo démonte.
- **La récolte** : les 900 € reviennent deux fois (route 2 et verdict). Le Mac n'aurait qu'une récolte, et elle serait négative.

Utilise plutôt le Mac comme **révélation annoncée dans le plan** : « dont une où un ordinateur entier coûte moins cher qu'une seule carte ». C'est une boucle de plus, et elle se ferme à 6:53 (réécriture en I7).

## 3. Erreurs factuelles

### Pages relues et calculs refaits

| Ce que dit la voix | Page rouverte le 20/11 et ce que j'y ai lu | Verdict |
|---|---|---|
| B65 « 1900 euros, à 5 centimes près », en stock | LDLC PB00751013 : « ASRock Intel Arc Pro B65 Creator 32GB », « 1 899€95 », « En stock » | Exact |
| B70 « à 2400 » | PB00751010 : « 2 399€95 », « En stock » | Exact |
| R9700 ASRock « à 2400, mais livrable sous 7 jours » | PB00751015 : « 2 399€95 », « En stock sous 7 jours (23/11/2026) » | Exact le 20/11, périmé le 30/11 (I5) |
| R9700 Gigabyte « à 2800, en stock » | PB00711272 : « 2 799€95 », « En stock » | Exact |
| 5060 Ti 16 Go d'ASUS « bien en stock : 1080 euros », « limitée à une par client » | PB00676833 : « ASUS Dual GeForce RTX 5060 Ti OC Edition 16GB », « 1 079€95 », « En stock », « Quantité limitée à 1 par client ». **Aussi lu : « 2.5 » slots, 50 mm d'épaisseur** | Exact. L'épaisseur est à signaler dans le piège du boîtier (I1) |
| A770 « 460 euros… une rupture en ligne » | PB00522209 : « 459€95 », « Rupture », « Dispo dans 1 boutique » | Exact (en ligne ; une boutique l'a) |
| 5090 TUF « 9400 euros, et en rupture » | PB00663200 : « 9 399€95 », « Rupture » | Exact |
| Mac mini M6 32 Go / 512 Go « 1709 euros », « le délai dépasse 15 jours » | PB00751971 : « 1 709€00 », « En stock dans + de 15 jours » | Exact |
| RX 9060 XT 16 Go d'ASUS « 700 euros sur Amazon », panier, « livraison… du 3 au 5 janvier » | amazon.fr B0F7LTBFZF (navigateur intégré) : « ASUS Prime Radeon RX 9060 XT 16GB GDDR6 OC Edition… 2.5 Slot… », « 699,99€ », « Expéditeur / Vendeur Amazon », bouton panier présent, « Livraison GRATUITE 3 - 5 janvier Ou livraison accélérée 31 décembre - 2 janvier », « Neufs (26) à partir de 699,99€ » | Exact. **« Noël sans cartes » est tenu** pour cette offre : les deux livraisons tombent après le 25/12. Les 25 autres vendeurs, je ne les ai pas ouverts |
| Mini-PC « un peu plus de 2000 euros en 64 gigas, en précommande », « TVA » pas claire, « mémoire fixe » | gmktec.fr (navigateur) : « €2.299,99 » barré, « €2.029,99 », « 64GB RAM +1TB SSD » sélectionné, « OFFRE BLACK FRIDAY EN PRÉCOMMANDE : -80 € », « Offre valable uniquement pour la configuration 64 Go + 1 To », code « BLACKFRIDAY80 », « Expédition estimée : du 7 au 9 décembre 2026 », « LPDDR5X fixe (non évolutif) ». Aucune mention TVA, TTC ou HT | Exact. **Mais** 2299,99 − 2029,99 = 270, pas 80 : je ne sais pas si le code de −80 € est déjà dans les 2029,99 (C1) |
| « 2 gigas pour 32 000 tokens, 8 pour 128 000, 16 pour 262 000 » | `config.json` de Qwen3.8-27B : 64 couches dont 1 sur 4 en `full_attention` (16), `num_key_value_heads` 4, `head_dim` 256, `max_position_embeddings` 262144. 16 × 2 × 4 × 256 × 2 octets = 65 536 octets par token → 2 / 8 / 16 Gio | Exact (hors état récurrent des 48 couches linéaires : ≈ 0,14 Gio en float32, mon calcul) |
| « 16 gigas et demi sur Hugging Face », « un peu plus de 15 », « Ça fait 31,3 » | API Hugging Face, `unsloth/Qwen3.8-27B-GGUF` : `Qwen3.8-27B-UD-Q4_K_M.gguf` = **16 564 259 744 octets, remis en ligne le 11/11/2026** (sources.md dit 16,46 Go, lu le 24/10) | **Faux de 0,1 : 15,43 + 16 = 31,43 Gio, donc 31,4** (B1). « 16 et demi » et « un peu plus de 15 » tiennent |
| « moins d'un giga de marge » | 32 − 31,43 = 0,57 Gio ; avec l'état récurrent, ≈ 0,43 | Exact |
| « 24 gigas suffisent » (conversation courte) | 15,43 + 2 = 17,4 Gio, plus environ 1 de tampons | Exact |
| Carte mère : 2e slot « 4 lignes en PCIe 3.0 », « passe par le chipset » | Page de spécifications Gigabyte (navigateur) : « Chipset: 1 x PCI Express x16 slot, supporting PCIe 3.0 and running at x4 (PCIEX4) » | Exact. « Tout en bas » et « 5 emplacements » viennent du manuel, que je n'ai pas pu rouvrir |
| Alimentation : « 1000 watts », « peut-être 2 prises 8 broches » | Page Corsair RM1000e : « 1000 Watts », « Native 600W-capable 12V-2x6 cable », un câble « 12V-2x6 to Dual 8-Pin (6+2) » listé | Cohérent. Le nombre de prises par câble n'était pas lisible dans le texte de la page : le « peut-être » reste nécessaire |
| « llama.cpp coupe le modèle en tranches de couches », chacune son tour | README de `tools/server` : « layer (default): split layers and KV across GPUs (pipelined) » | Exact |
| « pilote 580 la dernière branche », « CUDA 13 ne compile plus pour elle » | Notes CUDA 13.0 (archive) : « Offline compilation and library support for these architectures have been removed in CUDA Toolkit 13.0 ». Notes actuelles (CUDA 13.5) : cuFFT et cuSPARSE « Removed support for Maxwell, Pascal, and Volta ». Branche 580 : Phoronix bloqué ; seulement des résumés de presse (Tom's Hardware, TechSpot) qui citent NVIDIA | CUDA 13 exact. 580 : cohérent, source primaire non relue |
| « 2 ans de garantie légale », neuf ou occasion, « 2 ans pour du neuf, et 12 mois pour de l'occasion » | service-public F11094 (« Vérifié le 17 août 2026 ») : « 2 ans à partir du jour de la délivrance du bien », « neufs ou d'occasion », présomption 24 mois pour le neuf, « un délai d'un an » pour l'occasion, exclusion des biens « vendus par un particulier » | Exact |
| « il ne peut pas les réduire » | Article L219-1 (« d'ordre public ») non rouvert | Non revérifié (sources.md : ✅ le 24/10) |
| « 14 jours après la réception pour te rétracter » | F10485 (« Vérifié le 01 janvier 2026 ») : « 14 jours calendaires », « à partir du lendemain de la réception du bien » | Exact |
| « entre particuliers… vices cachés… à toi de les prouver » | F11007 (« Vérifié le 25 novembre 2025 ») : « C'est à vous de prouver l'existence du vice caché » | Exact |
| Renvoi « comment Qwen 27B y tourne quand même, juste en changeant de fichier » | `../qwen-27b-8go/teleprompteur.txt`, l. 1 : « Sur une carte de 8 gigas, tu changes un seul fichier » ; publiée le 23/11 | Exact |

### Calculs de la voix, refaits

| Dit | Calcul | Verdict |
|---|---|---|
| 900 € | 2799,95 − 1899,95 = 900,00 | Exact |
| 920 la paire d'A770 | 2 × 459,95 = 919,90 | Exact |
| 1400 la paire de 9060 XT | 2 × 699,99 = 1399,98 | Exact |
| 2160 la paire de 5060 Ti | 2 × 1079,95 = 2159,90 | Exact |
| « bat la B65 de 500 euros » | 1899,95 − 1399,98 = 499,97 | Exact |
| « 500 chez ASRock » | 2399,95 − 1899,95 = 500,00 | Exact, mais c'est un autre écart (I3) |
| « Même pas la moitié du prix d'une seule carte de 32 gigas » | moitié de 1899,95 = 949,98 ; 919,90 < 949,98 | Exact de 30 €. Ça casse si la B65 descend à 1839,80 € ou moins, alors qu'elle a pris +100 € entre le 16 et le 20/11 (I2) |
| Mac mini moins cher que la carte de 32 Go la moins chère | 1709 < 1899,95 (191 € d'écart) | Exact |
| « 31,3 » | 16 564 259 744 / 2^30 = 15,43 ; + 16 = 31,43 | **Faux : 31,4** (B1) |

### Pages que je n'ai pas pu lire

- **Phoronix** (branche 580) : bloqué par Cloudflare, en WebFetch comme en curl. Je n'ai que des résumés de presse.
- **Manuel Gigabyte** (`mb_manual_b850m-ae-wf6e-ice_1003_e.pdf`) : le téléchargement renvoie 196 octets de HTML. La position « tout en bas » et les 5 emplacements ne sont donc pas revérifiés.
- **Guide AMD ROCm/PyTorch** : le PDF existe (HTTP 200, 3,9 Mo). Je n'ai pas extrait son contenu.
- **Fiche technique NVIDIA de la V100** : PDF téléchargé, texte non extractible ici. « Ni ventilateur ni sortie vidéo » reste sans source propre à la V100 (I6).
- **Légifrance / L219-1** : non rouvert.
- **Corsair** : page lue, mais le tableau des prises par câble n'apparaît pas dans le texte.

## 4. Manquements aux règles, une par une

| Règle | État | Détail |
|---|---|---|
| 1. Hook en « tu », chiffre fort avant 15 s, rien de « dans cette vidéo » avant 15 s, zéro remplissage avant 30 s | OK | 900 € au 4e mot ; « Aujourd'hui » à 35 s (22 s). |
| 2. Question avant 30 s, plan en livrables par « Aujourd'hui, on va voir… », raison de rester, 1re partie = réponse | Presque | Question finie à 30,6 s à 145 mots/min, 19 s à ton débit. Plan concret, mais « chez LDLC » est faux (B2). |
| 3. Pas de « j'ai rien testé », mais rien qui laisse croire à un test | OK | « Celui que j'ai regardé », « D'après son manuel », « il ne me resterait peut-être », « la route que je prendrais » : tout est au conditionnel ou sur pièces. Aucun « j'ai mesuré ». |
| 4. Aucun nom de chaîne ni de site de tests | OK | LDLC, Amazon, GMKtec, Hugging Face, llama.cpp, marques : autorisés. |
| 5. Un seul renvoi sans date, pas d'annonce de la suite, fin = verdict + « Allez, salut ! » | OK | « on a vu dans une vidéo précédente » ; fin correcte. |
| 6. Abonnement après un service rendu, pas avant 30 s | OK | Après « 2 cartes, c'est de la place, pas de la vitesse ». |
| 7. Téléprompteur : lignes à lire, `.txt` = `.md`, 14 mots max, chiffres, aucun crochet | OK | `diff` : identiques. Ligne la plus longue : 14 mots. Aucun crochet. Seul « deux RTX 3090 » (l. 82) reste en lettres : toléré par la règle (« deux 5060 Ti »), mais toutes les autres paires sont en chiffres (« 2 cartes ») ; mets « 2 RTX 3090 » pour être homogène. |
| 8. Ton d'ami, liaisons ≥ 1,5 / 100 mots, humour gamer, pas de tics, pas d'anecdote inventée | Presque | 41 liaisons strictes (donc 10, sauf que 11, du coup 6, en fait 4, par contre 4, alors 3, voilà 2, pourtant 1) : 2,46 pour 100 mots. Mais 11 « sauf que » (I8), et deux faux suspens légers (C4). Humour : « le boss de fin », « Noël sans cartes ». Aucune anecdote inventée. |
| 9. Tutoiement partout | OK | Aucun « vous ». |

L'en-tête METRICS de `script.md` annonce « 36 liaisons, soit 2,26 pour 100 mots » : 36 / 1667 = 2,16. Le chiffre est à recompter (C2).

### Les points que tu soupçonnais, tranchés

| Point | Verdict |
|---|---|
| « prix relevés chez LDLC » alors qu'une offre vient d'Amazon et une de GMKtec | **Erreur confirmée**, bloquante et facile à corriger (correction 2). |
| « Même pas la moitié » (919,90 contre 949,98) | Vrai le 20/11, à 30 € près. Fragile : faux si la B65 descend à 1839,80 €. Important (correction 4). |
| Les deux « 500 euros » | Confusion réelle à l'oral : deux écarts différents en 12 lignes, et « la B65 de 500 euros » s'entend comme un prix. Important (correction 5). |
| « Noël sans cartes » | **Tenu** pour l'offre vendue par Amazon : livraison du 3 au 5 janvier, ou du 31/12 au 2/01 en accélérée. Les 25 autres vendeurs n'ont pas été ouverts. Garde-la, au passé (correction 7). |
| Hook à 900 € ou Mac mini | Garde les 900 € (miniature, honnêteté, double récolte) ; le Mac passe en révélation annoncée dans le plan (correction 9). |
| Verdict « si tu pars de zéro » | Il nomme bien une carte (la B65), donc le spectateur sait quoi acheter. Mais « de zéro » est flou (sans carte ? sans PC ?), la paire à 1400 € y crée la confusion des 500, et deux vérifications manquent : la prise 12V-2x6 de la B65 et la livraison en janvier de la paire (correction 5). |
| Cohérence voix / `tableau-offres.md` / [VISUEL] | Les prix, stocks et dates sont identiques partout et exacts sur les pages relues. Écarts : les visuels de la jauge (15,3 / 16,46 / 31,3 / 0,7) sont périmés (correction 1) ; le visuel du verdict (l. 136) dit encore « tu pars de zéro » et n'a pas le profil « tu as déjà 24 gigas » de la fin ; le visuel du mini-PC ne dit rien du code de −80 € (correction 11) ; `tableau-offres.md` n'a ni l'épaisseur des cartes ni la prise de la B65, et ses espaces manquent (correction 18). |

## 5. Tableau de bord

| Axe | Note | En une phrase |
|---|---|---|
| 1. Promesse | vert | Prix, routes, pièges, et la réponse aux 900 € : tout est livré. |
| 2. Alignement | vert | « garde ton argent » et le profil « 24 gigas » font passer le spectateur avant la vente. |
| 3. Problème profond | orange | « Ne pas payer pour rien » est posé et résolu ; la peur de se tromper n'est jamais dite en mots. |
| 4. Public & complexité | vert | Le cache traduit en « notes », l'addition faite avec lui. |
| 5. Valeur & originalité | vert | Euros du même jour, slot x4, câbles, droit français, encart Afrique : personne ne fait ça en français. |
| 6. Structure | vert | Besoin → 3 routes → recours → choix par profil. |
| 7. Histoire | orange | Un comparatif bien relancé, sans crise ; normal pour une vidéo calculée, ne l'invente pas. |
| 8. Mais / donc | vert | Chaque route : promesse, puis obstacle. |
| 9. Engagement | orange | « fais l'addition avec moi » reste la seule interpellation qui fait calculer le spectateur. |
| 10. Oralité & liaisons | orange | 2,46 / 100 mots, mais 11 « sauf que », dont 3 d'affilée dans la route 1. |
| 11. Tics d'IA | orange | Deux « pas A, c'est B » assumés (le boss de fin, la thèse) ; « voilà le truc » et « c'est là que ça devient bizarre » annoncent au lieu de livrer. |
| S1. 30 secondes | vert | Les 6 questions passent ; question à 19 s à ton débit. |
| S2. Pont | vert | « 24 gigas suffisent… Donc les 32, c'est pour lui laisser une longue mémoire » ouvre la question suivante. |
| S3. Retournements | vert | Un toutes les 15 à 30 s ; c'est même trop régulier (I8). |
| S4. Planté / récolté | vert | 900 € (hook → route 2 → verdict), 31,3 (calcul → Mac), 24 gigas (réponse 1 → fin), « slot, boîtier, câbles » en motif. |
| S5. Personnages et enjeu | orange | Le spectateur et « ma tour » ; pas d'autre personnage, normal ici. |
| S6. Fin | vert | Elle retourne la question : la meilleure carte est celle que tu n'achètes pas, récolte de la première réponse. |

## 6. Ce qu'il faut garder

- **Le hook** et son visuel : deux prix relus, exacts, du même jour, les deux en stock.
- **« Pas un giga de plus, en tout cas. »** : la réponse sèche aux 900 €.
- **« Alors fais l'addition avec moi »** et la jauge : le meilleur moment pédagogique.
- **« le boss de fin, c'est pas le prix, c'est la règle du magasin »** et **« Noël sans cartes »** (tenu par la page Amazon).
- **« Prends la mienne »** : ça humanise sans prétendre avoir testé.
- **Le verdict par profil**, et surtout « la limite d'une par client ne te gêne plus, puisque t'en achètes qu'une » : le piège de la route 1 devient un argument.
- **La récolte du Mac** : « souviens-toi de l'addition du début ».
- **L'encart Abidjan, Dakar, Kinshasa.**

## 7. Corrections, classées

Les réécritures sont au format du téléprompteur (14 mots au plus par ligne, chiffres, aucun crochet). Recopie-les dans `script.md` et dans les deux téléprompteurs.

### Bloquant

**1. (B1) L'addition fait 31,4, plus 31,3.** Le fichier `UD-Q4_K_M` a été remis en ligne le 11/11 : 16 564 259 744 octets, soit 16,56 Go ou 15,43 Gio (API Hugging Face, lue le 20/11). 15,43 + 16 = 31,43.

> l. 41 : « Ça fait 31,3. »

```
Ça fait 31,4.
```

> l. 219 : « 31,3 gigas pour la conversation complète. »

```
31,4 gigas pour la conversation complète.
```

Dans `script.md` : l. 30, « ≈ 0,7 » devient « ≈ 0,6 » ; l. 40, « Qwen3.8-27B Q4_K_M » devient « Qwen3.8-27B-UD-Q4_K_M » ; l. 52, le visuel devient « 15,4 Gio (16,56 Go sur Hugging Face) + 16 (conversation complète) = 31,4 Gio », « Il reste un trait de 0,6 » (16,56 vient des octets de l'API ; vérifie le chiffre que la page affiche avant la capture) ; l. 144, « 31,3 sur 32 » devient « 31,4 sur 32 ». Ajoute dans `sources.md` un fait F109 (taille du 11/11) qui remplace la taille de F41 et le calcul de F81 pour la voix. Revérifie la taille le jour de la voix : Unsloth remet ses fichiers en ligne souvent.

**2. (B2) Le plan attribue tous les prix à LDLC.** La 9060 XT vient d'Amazon, le mini-PC de GMKtec. Le visuel du plan (« LEURS PRIX DU 20/11 ») est déjà juste : seule la voix se trompe.

> l. 14-16 : « Ensuite, 3 routes vers 32 gigas, / avec leurs prix relevés chez LDLC le 20 novembre, / et le piège de chacune. »

```
Ensuite, 3 routes vers 32 gigas,
avec leurs prix relevés le 20 novembre,
et le piège de chacune.
```

(Version plus forte en I7.)

### Important

**3. (I1) Le piège du boîtier ne parle que de cartes de 2 slots, alors que celles que tu cites sont plus épaisses.** La 5060 Ti Dual d'ASUS est donnée en « Dual Slot » mais aussi en « 2.5 » slots, 50 mm d'épaisseur (fiche LDLC relue) ; la 9060 XT Prime en « 2.5 Slot » (titre Amazon). Ce n'est pas une erreur prouvée : le nombre d'emplacements dépend de l'équerre, et le demi-slot en plus est une question de place sous la carte mère, que seul le schéma du manuel (non relu) ou ton boîtier tranchent. Mais c'est justement la 5060 Ti que le verdict te fait ajouter : préviens le spectateur.

> l. 92-93 : « Du coup, une carte de 2 slots dedans dépasse sous la carte mère, / et il te faut un boîtier à 5 emplacements. »

```
Du coup, une carte de 2 slots dedans dépasse sous la carte mère,
et il te faut un boîtier à 5 emplacements.
Et les 5060 Ti et 9060 XT du relevé sont plus épaisses :
2 slots et demi, donc mesure la place sous ta carte mère.
```

Ajoute l'épaisseur au visuel de la l. 74 et un fait F110 (LDLC PB00676833 : « Dual Slot », « 2.5 », 50 mm ; Amazon B0F7LTBFZF : « 2.5 Slot »).

**4. (I2) « Même pas la moitié » tient à 30 € près.** 919,90 contre 949,98. La B65 a bougé de 100 € en quatre jours, et le Black Friday tombe le 27/11. Si elle passe à 1839,80 € ou moins, la phrase devient fausse.

> l. 61 : « Même pas la moitié du prix d'une seule carte de 32 gigas ! »

```
À peu près la moitié du prix d'une seule carte de 32 gigas !
```

(Si ta relecture du 26-27/11 montre une B65 toujours au-dessus de 1840 €, tu peux garder « Même pas la moitié ».)

**5. (I3) Deux « 500 euros » différents en 12 lignes, et un qui s'entend mal.** « bat la B65 de 500 euros » peut s'entendre « la B65 à 500 euros ». Puis « ou 500 chez ASRock » parle d'un autre écart (R9700 ASRock moins B65). Dis un écart, puis un prix. J'en profite pour clarifier « si tu pars de zéro » (sans carte ? sans PC ?), ajouter le piège propre à cette paire (janvier), en retirer un « sauf que », et dater le délai d'ASRock (« sous 7 jours » visait le 23/11, une semaine avant la sortie).

> l. 201-214, de « Si tu pars de zéro » à « si tu peux attendre une semaine. »

```
Si t'as pas encore de carte de 16 gigas,
moi, je ne commencerais pas par une paire.
Sur le papier, la paire de 9060 XT à 1400 euros
coûte 500 euros de moins que la B65.
Seulement, elle cumule tous les pièges de la route :
slot, boîtier, câbles, une livraison en janvier,
et une vitesse qui ne double pas.
Et ton logiciel doit gérer ces 2 cartes AMD aussi.
Donc je prendrais la B65, à 1900 euros :
la moins chère des offres en stock du relevé,
avec la même quantité de mémoire que la R9700 à 2800.
Elle se branche en 12V-2x6 :
regarde si ton alim a ce câble, ou un adaptateur.
Et avant de cliquer, tu vérifies que ton logiciel la gère.
S'il ne la gère pas, là,
une R9700 et son guide officiel peuvent avoir un sens :
900 euros de plus chez Gigabyte,
ou 2400 euros chez ASRock, livrable sous 7 jours ce jour-là.
```

La prise de la B65 est sur sa fiche LDLC (« 1 X PCI Express 16 Broches (12V-2x6) », relue le 20/11). La page dit le connecteur de la carte, pas ce qu'exige l'alimentation : d'où « ce câble, ou un adaptateur ». Ajoute-la à `sources.md` (F111) et au visuel du verdict. Cette réécriture retire 2 « sauf que » (l. 204 et 210).

**6. (I4) « Ce que la R9700 a en plus » sous-entend que la B65 n'a pas de guide.** F83 prouve seulement que la R9700 en a un. Personne n'a cherché l'équivalent chez Intel.

> l. 128-129 : « Ce que la R9700 a en plus sur le papier, / c'est un guide officiel d'AMD pour y faire tourner ses outils d'IA. »

```
Ce que j'ai trouvé côté R9700,
c'est un guide officiel d'AMD pour y faire tourner ses outils d'IA.
```

**7. (I5) Des disponibilités au présent qui seront périmées le 30/11.** Le grill V3 avait corrigé « ce soir » pour l'A770 ; le même risque touche les nouvelles offres. Voici ce qui casse si les pages bougent avant la voix. Relis-les le 26-27/11 :

| Phrase | Ce qui la casse |
|---|---|
| « 900 euros de plus » (hook, route 2, verdict) | B65 ou R9700 Gigabyte qui bouge, ou l'une des deux en rupture |
| « Même pas la moitié » | B65 ≤ 1839,80 € (I2) |
| « la moins chère en stock de mon relevé » | B70 ou R9700 ASRock sous la B65 |
| « Donc un ordinateur complet coûte moins cher que la carte de 32 gigas la moins chère » | B65 ≤ 1709 € (191 € de marge) |
| « bat la B65 de 500 euros » et « 500 chez ASRock » | n'importe lequel des trois prix |
| « Celle-là, tu peux la mettre au panier », « Noël sans cartes » | Amazon qui livre avant Noël, ou rupture |
| « est bien en stock : 1080 euros » | stock ou prix de la 5060 Ti |
| « livrable sous 7 jours », « si tu peux attendre une semaine » | la date affichée (23/11) sera passée le 30/11 |

Réécriture du paragraphe AMD de la route 1, qui retire aussi le « sauf que » de la l. 79 (I8) :

> l. 75-80

```
Et chez AMD ?
La Radeon RX 9060 XT de 16 gigas d'ASUS
était à 700 euros sur Amazon, donc 1400 la paire.
Celle-là, tu pouvais la mettre au panier.
Mais ce jour-là, la livraison était annoncée du 3 au 5 janvier.
Bref : rupture, une par client, ou Noël sans cartes.
```

**8. (I6) La V100 a perdu sa précaution.** Le grill V3 (E6) demandait « comme les autres cartes de serveur ». Aucun fait de `sources.md` ne parle du refroidissement ni des sorties de la V100 elle-même (seulement le conseil 4, tiré de la P40 et de la MI50), et je n'ai pas pu extraire sa fiche NVIDIA.

> l. 146-147 : « En plus, elle n'a ni ventilateur ni sortie vidéo : / tout est à refaire autour. »

```
En plus, comme les autres cartes de serveur,
elle n'a ni ventilateur ni sortie vidéo :
tout est à refaire autour.
```

Ou bien source-la (fiche NVIDIA de la V100 PCIe) dans un F112, et garde ta phrase.

**9. (I7, optionnel mais recommandé) Le plan peut annoncer la révélation du Mac.** C'est une boucle de plus, qui se ferme à 6:53, et elle corrige aussi B2. Elle dépend de la marge de 191 € (I5) : vérifie-la avant.

> l. 14-16

```
Ensuite, 3 routes vers 32 gigas,
avec leurs prix relevés le 20 novembre,
dont une où un ordinateur entier
coûte moins cher qu'une seule carte de 32 gigas,
et le piège de chacune.
```

**10. (I8) 11 « sauf que ».** L. 29, 62, 70, 79, 97, 130, 137, 156, 164, 204 et 210 ; trois d'affilée dans la route 1 (l. 62, 70, 79 : A770, 5060 Ti, 9060 XT). À la troisième, on entend la recette, comme les « Bref » de la V3. La correction 5 en retire deux (l. 204, 210), la correction 7 un (l. 79). Retire encore ces deux-là :

> l. 70-71 : « Sauf qu'il y a une petite ligne sous le prix : / limitée à une par client. »

```
Seulement, il y a une petite ligne sous le prix :
limitée à une par client.
```

Et l. 156 : « Sauf que, déjà, le délai dépasse 15 jours. » devient :

```
Premier hic : le délai dépasse 15 jours.
```

Il en restera 6 (l. 29, 62, 97, 130, 137, 164), espacés d'au moins une minute en moyenne.

### Confort

**11. (C1) Le prix du mini-PC est ambigu sur la page.** 2299,99 barrés, 2029,99 affichés, et un code « BLACKFRIDAY80 » de −80 € à part. Inclus ou pas, je ne peux pas le dire. Arrondis pour rester vrai dans les deux cas :

> l. 162 : « Celui que j'ai regardé affiche un peu plus de 2000 euros en 64 gigas, »

```
Celui que j'ai regardé affiche autour de 2000 euros en 64 gigas,
```

Visuel l. 116 : ajoute « code de −80 € affiché à part, inclus ou non : pas clair ».

**12. (C2) L'en-tête METRICS se trompe de calcul.** « 36, soit 2,26 pour 100 mots » : 36 / 1667 = 2,16. Avec la même liste, je compte 41 (2,46). Recompte-le après les corrections.

**13. (C3) « Notes », puis « réserve » : deux mots pour la même chose.**

> l. 29 : « Sauf que cette réserve-là grossit à chaque message. »

```
Sauf que ces notes-là grossissent à chaque message.
```

**14. (C4) Deux annonces au lieu de faits.** « Parce que voilà le truc : » (l. 25) et « Troisième route, et c'est là que ça devient bizarre. » (l. 150) sont des faux suspens légers (`anti-ia.md`, section 2). Le fait suivant est assez fort tout seul.

```
Parce que pendant que tu discutes,
le modèle garde des notes sur tout ce qui a été dit.
```

```
Troisième route : changer carrément d'ordinateur.
```

**15. (C5) L'A770 était en rupture en ligne, et une boutique l'avait.** Pour rester exact :

> l. 64 : « ce jour-là, tu ne pouvais pas la commander. »

```
ce jour-là, tu ne pouvais pas la commander en ligne.
```

**16. (C6) « deux RTX 3090 » en lettres (l. 82)**, alors que toutes les autres paires sont en chiffres : « Et 2 RTX 3090 ? ».

**17. (C7) Un profil manque au verdict : celui qui a déjà une Radeon de 16 gigas.** Ton public en a. Une ligne suffit, si tu veux (F107 ne dit rien de la compatibilité logicielle, d'où la vérification) :

```
Et si ta carte de 16 gigas est une Radeon,
regarde la 9060 XT à 700 euros, livraison en janvier,
et vérifie que ton logiciel gère les 2.
```

**18. (C8) Hors script, à remettre d'accord (je n'y ai pas touché).** `README.md` (l. 32) et `calendrier.md` (l. 31) disent encore « 1 590 mots, 10:57 » et « prix relevés le 16/11 ». Le script fait 1667 mots, avec des prix du 20/11. L'en-tête de `script.md` dit toujours « V3 du 19/11 ». `tableau-offres.md` a des espaces manquants (« panier de2 », « 32Go », « 1/client », « TVA non dite ») et n'a ni l'épaisseur des cartes ni la prise de la B65.

## 8. Les corrections du grill V3 : tiennent-elles ?

| V3 | État en V4 |
|---|---|
| E1 « ce soir » | Corrigé (« ce jour-là »). Le même risque revient sur les nouvelles offres (correction 7). |
| E2 « la moins chère en stock » de tout LDLC | Corrigé (« de mon relevé »). |
| E3 « la même mémoire » | Corrigé (« la même quantité de mémoire »). |
| E4 Go / Gio | Corrigé, mais le chiffre de base a changé (correction 1). |
| E5 renvoi [F41] | Corrigé. |
| E6 V100 « comme les autres cartes de serveur » | **Perdu** (correction 8). |
| E7 « les vidéos anglaises adorent » | Supprimé. |
| E8 « llama.cpp » au lieu de « le moteur » | Corrigé. |
| P2 marge récoltée sur le Mac, mini-PC en 64 | Corrigé. |
| P3 réponse aux 900 € | Corrigé, à nuancer (correction 6). |
| P4 verdict qui hésite | Corrigé, mais la nouvelle paire à 1400 € l'a brouillé (correction 5). |
| P5 « Prends la mienne » | Corrigé. |
| P6 prix arrondis | Corrigé. |
| P7 recours neuf et occasion | Corrigé. |
| P8 « Bref » | 3 au lieu de 4, mais 11 « sauf que » (correction 10). |
| P9 « Le modèle consulté » | Corrigé. |
| P10 plan prix et pièges mélangés | Corrigé ; une nouvelle erreur sur LDLC (correction 2). |

## 9. Plan d'action

1. Corrections 1 et 2 (31,4 et le plan), puis F109 dans `sources.md`.
2. Corrections 5 et 7 (verdict sans double 500, route 1 datée), puis 3 et 8 (boîtier, V100).
3. Corrections 4, 6 et 10, et la 9 si tu veux la révélation du Mac dans le plan.
4. Le 26-27/11, relis les 10 pages avec le tableau de la correction 7 : chaque ligne qui casse se corrige avant la voix.
5. Recompte les mots et les liaisons, remets `README.md` et `calendrier.md` d'accord.
