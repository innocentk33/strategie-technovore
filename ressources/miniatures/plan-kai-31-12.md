# Miniatures à la manière de Kai, du 23/11 au 31/12/2026

> **15/11, ta décision** : toutes les vidéos jusqu'au 31/12 ont leurs 3 miniatures « à la manière de Kai » (h, i, j, skill `miniature-kai`) et un test A/B à 3. Tu génères d'abord les illustrations avec ChatGPT, dans l'ordre des dates. Les vidéos de matériel pur montrent le matériel au lieu d'un visage. Une composition « Severance » est possible pour certaines vidéos, pas pour toutes : tes références sont des pistes pour les prochaines, et on la choisit au cas par cas.
>
> Strata (16/11) et « même carte » (19/11) sont déjà faites. Le calendrier bouge souvent : on maquette dans l'ordre des dates, et les vidéos lointaines restent au stade du brief ci-dessous.

## Les trois cas

| Cas | h (palette de Kai) | i (Technovore, sans image) | j (Technovore) |
|---|---|---|---|
| **Visage** (meme) | texte à gauche, visage à droite qui regarde le texte (ou texte en haut, selon la vidéo) | scène à plat, texte sur une ligne en haut | visage aux couleurs de peau, même mise en page que h |
| **Matériel pur** (ta demande) | l'illustration du matériel prend la place du visage | scène à plat (objets SVG) | l'illustration du matériel, en Technovore |
| **Severance** | visage de face en très grand, coupé sous les yeux, la tête ouverte et les objets dedans, texte sur une ligne en haut | scène à plat | idem h, en Technovore |

**Le texte, à gauche ou en haut** (15/11, ta demande) : on lit de gauche à droite, donc le texte vient en premier. Selon la vidéo, il va à gauche (le visage ou l'objet à droite, tourné vers lui) ou sur une ligne en haut. Plus jamais de visage à gauche avec le texte à droite (c'était la mise en page de Strata et du 19/11).

**Ombre blanche** (15/11, ton choix) : en Technovore, la copie décalée du mot en couleur (0,055 em en bas à droite) est **blanche**, sans contour.

**Fond de Technovore (i et j), 15/11, ta demande** : sombre et uni (`#141e27`), sans grille ni dégradé, pour plus de contraste. L'ombre décalée du mot menthe passe en blanc (l'ardoise foncée disparaissait sur ce fond). C'est appliqué à Strata et au 19/11 (rendus i et j refaits).

Pour le matériel, je n'ajoute pas de nouvelle variable de test : l'image remplace simplement le visage. Corrige-moi si tu voulais autre chose.

**Severance**, d'après tes références du 15/11 ([`reference-tete-ouverte-kai.webp`](images/reference-tete-ouverte-kai.webp), [`reference-tete-en-bas.jpg`](images/reference-tete-en-bas.jpg), [`reference-tete-anneau.jpg`](images/reference-tete-anneau.jpg)). Prototype : [`propositions/severance-prototype.html`](propositions/severance-prototype.html), rendu [`images/prototype-severance.png`](images/prototype-severance.png) :
- le visage est de face, en très grand, coupé en bas sous les yeux, le regard levé vers ce qu'il y a dans sa tête ; le texte tient sur une ligne en haut ;
- `portrait.py --coupe 0.17` ouvre la tête (un ovale sombre) et sort un 2e calque, `-devant` (le bord avant et le visage), que la maquette pose par-dessus les objets : ils ont l'air dedans ;
- 1 à 3 objets dans la tête, gros, qui débordent vers le haut ; pas plus, sinon rien ne se lit à 168 px ;
- c'est la composition de la miniature « Don't overpay » de Kai : on garde l'idée, pas son visage, ses lunettes ni sa signature. L'anneau d'écrans autour de la tête (3e référence) reste une variante possible ;
- le portrait doit être généré **de face, le regard levé** : prompt spécial ci-dessous (V2, V6, V9).
- **À trancher** : la coupe va-t-elle sur h et j (h contre j reste un test de palette), ou sur j seul (j teste alors Severance) ?

## Les 12 vidéos

La colonne « Cas » dit où va le texte ; c'est ma proposition, tu peux la changer vidéo par vidéo. Severance n'est que proposé sur 3 vidéos. Les textes sont des questions déjà portées par le hook de la fiche. **Le script doit les tenir.** On ne met aucun chiffre ni verdict tant que tes relevés n'existent pas.

| Date | Vidéo | Cas | Texte (l1 / l2) | Visage recommandé | Rechanges | Objet de la scène |
|---|---|---|---|---|---|---|
| lun. 23/11 | [32 Go pour Qwen 27B](../../projets/deux-cartes-occasion/fiche.md) | visage, texte à gauche | 32 GO / PAS CHER ? | **Fry** (déjà généré, retourné par `--miroir` pour regarder le texte) | Oprah « you get a car », Ron Swanson | deux cartes empilées, tuile Qwen, étiquette 32 GO |
| jeu. 26/11 | [Carte par budget](../../projets/carte-par-budget/fiche.md) | matériel, texte en haut | PAYER PLUS / POUR RIEN ? | **3 cartes graphiques** de tailles différentes (M1) | (les cartes SVG de Strata) | étiquettes de prix vides, remplies avec tes relevés du 20 et du 26/11 |
| lun. 30/11 | [DeepSeek sans carte graphique](../../projets/cout-deepseek-flash/fiche.md) | visage, texte à gauche | ET LA / QUALITÉ ? | **Keanu Reeves** « whoa » (V1) | Pikachu surpris, Nick Young confus | tuile DeepSeek, barrettes de RAM, carte barrée. Pas de chiffre : la version du modèle est à vérifier |
| jeu. 3/12 | [RAM, VRAM ou unifiée](../../projets/ram-vram-unifiee/fiche.md) | **Severance** (proposé), texte en haut | LA RAM / TROP LENTE ? | **Roll Safe** (doigt sur la tempe) (V2) | Gru et son plan, Walter White | dans la tête : deux barrettes de RAM et une carte (le prototype) |
| lun. 7/12 | [Deux cartes graphiques](../../projets/multi-gpu/fiche.md) | visage, texte à gauche | 2 CARTES / 2× PLUS VITE ? | **Boromir** « on ne fait pas simplement… » (V3) | Gordon Ramsay exaspéré, Steve Harvey choqué | deux cartes reliées, « ×2 ? ». On n'affirme pas « plus lent » : une seule mesure publiée |
| jeu. 10/12 | [Mac mini ou PC gamer](../../projets/mac-mini-ia/fiche.md) | matériel, texte en haut | LE PETIT / GAGNE ? | **Mac mini** (M2) contre **PC gamer** (M3) | — | les deux machines face à face, « VS ». La question reste ouverte tant que le calcul n'est pas fait |
| lun. 14/12 | [Coût de Claude Fable 5.2](../../projets/cout-claude-local/fiche.md) (fusion avec Kimi, 15/11) | **Severance** (proposé), texte en haut | CLAUDE / ?? ??? € | **Michael Scott** (horrifié) (V9) | **M. Krabs** (V4, l'ancienne miniature de Kimi, déjà générée), M. Burns qui joint les doigts | dans la tête, une baie de serveurs et la tuile Claude. Le prix arrive avec le calcul du script |
| jeu. 17/12 | [Prix après le Black Friday](../../projets/prix-apres-black-friday/fiche.md) | visage, texte à gauche | LES PRIX / ONT BAISSÉ ? | **Jim Halpert** (regard caméra, sceptique) (V5) | Stonks (seulement si tes relevés montrent une hausse), Grumpy Cat | étiquette barrée, carte. Aucun verdict avant tes relevés de mi-décembre |
| lun. 21/12 | [Le nom d'un modèle](../../projets/bases-ia-locale/fiche.md) | **Severance** (proposé), texte en haut | TU LIS / ÇA ? | **la dame des maths** (Renata Sorrah, perdue dans les calculs) (V6) | Travolta perdu (Pulp Fiction), Charlie Day et son tableau en liège | dans la tête, deux blocs « A3B » et « .GGUF » (la fiche veut les lire à 168 px) |
| jeu. 24/12 | [Le cadeau IA locale](../../projets/cadeau-ia-locale/fiche.md) | visage, texte à gauche | TON CADEAU / SANS CLOUD ? | **Mr Bean** (paquet cadeau, ravi) (V7) | Joey Tribbiani, Chuck Norris pouce levé | une boîte cadeau qui contient une carte. Pas de budget écrit avant tes relevés du 18/12 |
| lun. 28/12 | [Louer, acheter ou s'abonner](../../projets/louer-acheter-ia/fiche.md) | visage, texte à gauche | TU PAIES / TROP ? | **Drake** (main levée, il refuse) (V8) | Tom (Tom et Jerry) choqué, Gus Fring | trois tuiles (abonnement, location, carte), point d'interrogation |
| jeu. 31/12 | *Radar* (15/11 : Coût de Claude passe au 14/12) | — | — | — | — | — |

On n'utilise pas The Rock, DiCaprio, Harold ni Jackie Chan (déjà pris). Aucun visage ne revient deux fois, rechanges compris. On écarte les personnages verts (le Grinch, Shrek, Kermit), que le détourage mangerait. J'écarte aussi les enfants acteurs et les personnalités politiques : c'est une proposition de ma part, pas ta règle, tu peux la lever.

Ce plan remplace les sections « Miniature (charte verte) » des fiches. Je ne les ai pas modifiées : une autre session travaille sur ces fiches en ce moment.

Le Mac mini et le PC gamer sont des illustrations, pas des photos : la fiche du Mac mini disait « ni photo du Mac mini ». Si « images du matériel » voulait dire de vraies photos, on a tes photos de 5080 (`strata-test/miniature/sources/rtx5080-*-auteur.png`), mais pas de Mac mini.

## La génération (ChatGPT)

**Tous les prompts, complets et prêts à copier, sont dans [`prompts-chatgpt-31-12.md`](prompts-chatgpt-31-12.md)** : 9 images restent à faire (V3 à V9, M2, M3), dans une seule conversation, avec ton image de Keanu jointe comme référence de style. Les visages regardent vers la gauche, sauf ceux des compositions Severance, de face et les yeux levés.

Le détourage : `python3 -I ressources/miniatures/portrait.py <image> <sources/> <nom>`, avec `--miroir` si l'image regarde du mauvais côté et `--coupe 0.17` pour Severance (la sortie donne le centre et la largeur de l'ouverture).

## Les maquettes (15/11)

Une seule maquette pour toutes les vidéos : [`propositions/kai-31-12.html`](propositions/kai-31-12.html)`?d=<dossier du projet>&v=h|i|j`. Chaque vidéo y a ses textes, sa mise en page (`gauche`, `materiel` ou `severance`) et ses deux scènes (h/j et i). Rendus : `projets/<d>/miniature/rendus/{h,i,j}-kai.png` ; PSD : `photocraft/{h,i,j}-kai.psd` (3 calques de texte chacun). Planche à 168 px : [`images/test-168px-31-12.png`](images/test-168px-31-12.png).

- Les 9 images du 15/11 n'ont pas eu besoin de `--miroir` : elles regardent déjà du bon côté.
- Severance : la tête s'ouvre à `--coupe 0.21` (et non 0.17) pour Michael et Math Lady, sinon l'ouverture est trop étroite sur une tête avec des cheveux. La coupe est sur h **et** j (h contre j reste un test de palette), à toi de dire si tu préfères j seul.
- Les textes longs (« 2 CARTES / 2× PLUS VITE ? », « LES PRIX / ONT BAISSÉ ? », « TON CADEAU / SANS CLOUD ? ») restent petits à 168 px, surtout en i (une seule ligne). Si tu veux les raccourcir, `?l1=…&l2=…` les change sans toucher la maquette.
- « -?? % » (17/12) et « ?? ??? € » (14/12) attendent tes relevés et le calcul du script.
- Relecture d'un agent Opus indépendant (15/11) : 22 miniatures recalées (chevauchements, objets qui flottaient au-dessus de la tête ouverte, scènes décentrées). Restent deux défauts des images sources : le blouson de Drake et le buste de Boromir touchent le bord gauche de l'image. Boromir est agrandi pour que la coupe sorte du cadre. Drake est régénéré le 15/11 avec de la marge (`drake-vert-dezoome.png`, détouré en `portrait-drake2-*`) : son contour est complet, le fondu n'est plus utilisé (l'option `fade` reste dans la maquette). L'image a moins de pixels sur Drake, donc il est un peu plus doux en 4K plein écran.

## Suivi

| Date | Images reçues | Maquette | Rendus + PSD | Test A/B décidé |
|---|---|---|---|---|
| 23/11 | Fry ✓ | ✓ | ✓ | |
| 26/11 | M1 : **pas sur le disque** (`carte-par-budget/miniature/sources/` est vide) | | | |
| 30/11 | Keanu : **pas sur le disque** | | | |
| 3/12 | Roll Safe : **pas sur le disque** | | | |
| 7/12 | Boromir ✓ | ✓ | ✓ | |
| 10/12 | Mac mini ✓, PC gamer ✓ | ✓ | ✓ | |
| 14/12 | Michael ✓ (Krabs ✓ en rechange) | ✓ Severance | ✓ | |
| 17/12 | Jim ✓ | ✓ | ✓ | |
| 21/12 | Math Lady ✓ | ✓ Severance | ✓ | |
| 24/12 | Mr Bean ✓ | ✓ | ✓ | |
| 28/12 | Drake ✓ | ✓ | ✓ | |
| 31/12 | (radar) | | | |
