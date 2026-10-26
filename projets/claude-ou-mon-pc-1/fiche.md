# Abonnement ou IA locale ? #1 : 16 Go de VRAM suffisent-ils ?

> **24/10** : la série s'appelle « Abonnement ou IA locale ? » (c'est aussi la playlist) au lieu de « Claude ou mon PC ? », puisqu'on compare plusieurs abonnements à l'IA locale. Dans la voix, pas de « épisode un » : les vidéos se renvoient par ce qu'elles expliquent. Le dossier garde son nom.

> **25/10, ta décision : la vidéo est calculée, sans essai.** Les essais te prennent trop de temps. Toutes les vidéos IA sont calculées, sauf celle de l'installation (règles du calculé : [`strategie.md`](../../strategie.md), pilier 2). On fait comme Kai et Morgans Code : les mesures publiées par les utilisateurs qui ont une carte de 16 Go, les études, les notes de version et le calcul. [`modeles-5080.md`](modeles-5080.md) devient la base du calcul : son plan d'essais ne se lance plus.
>
> **Tes essais rapides, avant le 25/10** (tes mots, précisés le 25/10) : « certains modèles sont lents en local ». **Qwen3.8-27B**, fichier `UD-IQ4_XS` (14,25 Go, page d'Unsloth : fait F40 de [`deux-cartes-occasion/sources.md`](../deux-cartes-occasion/sources.md)) : très lent, mais ça marche. **Gemma 4 12B QAT** (`gemma-4-12B-it-QAT-Q4_0.gguf`, **6,98 Go**, plus 175 Mo pour la vision ; [Hugging Face, lmstudio-community](https://huggingface.co/lmstudio-community/gemma-4-12B-it-QAT-GGUF/tree/main), relu le 25/10 ; [LM Studio](https://lmstudio.ai/models/google/gemma-4-12b-qat) demande 7 Go de mémoire au minimum) : plutôt rapide. C'est du vécu, à dire comme une impression, sans chiffre et sans « j'ai testé ».
> - **Le calcul explique l'écart** : Qwen3.8-27B est dense, ses 27 milliards de paramètres travaillent à chaque mot ; Gemma 4 12B en a moins de la moitié. La version QAT a été entraînée pour supporter la compression en 4 bits, d'où un fichier deux fois plus léger que celui du Qwen. Le plafond se calcule comme dans Coût Claude (bande passante ÷ Go lus par mot) : avec les **960 Go/s** de ta 5080 (GDDR7 à 30 Gbit/s sur 256 bits : [fiche d'Inno3D de ta X3 OC](https://www.inno3d.com/product/inno3d-geforce-rtx-5080-x3-oc), relue le 25/10 ; même chiffre dans le [test de Guru3D](https://www.guru3d.com/review/review-galax-geforce-rtx-5080-1click-oc-edition/) ; la [page de NVIDIA](https://www.nvidia.com/en-us/geforce/graphics-cards/50-series/rtx-5080/) ne donne que « 16 GB GDDR7, 256-bit »), environ 67 tok/s au mieux pour le Qwen (960 ÷ 14,25) et environ 138 pour Gemma (960 ÷ 6,98). Ce sont des plafonds, pas des mesures.
> - **Pourquoi ton Qwen te paraît « très lent » alors que son plafond est correct** : deux causes possibles, sans mesure pour trancher.
>   - **Il est trop juste pour la carte.** 14,25 Go de poids sur 16 Go : il reste moins de 2 Go pour le contexte (le cache KV) et pour l'affichage de Windows si l'écran est branché sur la 5080. Dès que ça déborde, une partie passe en RAM, et la vitesse s'effondre (le Q4 qui déborde tombe à 13 tok/s chez Hardware IA). C'est la scène du point 4, avec un fichier encore plus proche de la limite.
>   - **Il réfléchit avant de répondre.** Le mode thinking de Qwen3.8 est actif par défaut (`modeles-5080.md`, section 0.1) : il écrit longtemps avant la première ligne utile, ce qui paraît lent même à bonne vitesse.
>   - Dans la vidéo, dis-le comme ça : « chez moi, ce modèle m'a paru très lent ; d'après le calcul, il est trop juste pour ma carte, et en plus il réfléchit avant de répondre ». Pas de tok/s à toi.
> - **Gemma 4 est faible en code** (`modeles-5080.md`, tableau 1.1 et section 1.2) : rapide ne veut pas dire suffisant.

> Analyse (hook, pourquoi, score) : [`strategie.md`](../../strategie.md), idée 1. Planning : [`calendrier.md`](../../calendrier.md). Premier jet : [`brouillon-script.md`](brouillon-script.md).

**Origine** : « Le second pouvoir de votre carte graphique : héberger une IA en local sur une 5080 ». Inspiration : [Red Stapler, I ran Qwen3.8 27B on single 8GB Card!](https://www.youtube.com/watch?v=ye50BbXEczo).

**Mis à jour le 18/10** : le titre met en avant ta carte de 16 Go, et la vidéo reprend le contenu du guide IA en local 2027 (voir [`archive/`](../../archive/README.md)). Elle sort le **16 nov. à 18 h** (avancée au 2 nov. le 22/10, revenue au 16 nov. le 23/10 : la vidéo qui pose les bases sort avant elle le 2 nov., aujourd'hui [celle de l'installation](../installer-ia-locale/fiche.md) depuis le 24/10 ; ses essais sur la 5080, les 23-24/10, servent ensuite à « Combien coûte Claude en local ? », le 23 nov. depuis le 24/10). Preuve : chez Kai, [Is 16GB All You Need for Serious Local LLM?](https://www.youtube.com/watch?v=i9mRnbdDYxk) fait 359 K vues en 10 jours, et ses vidéos sur le matériel et le coût font environ 2 fois plus de vues que ses tests de modèles (voir [`etudes/kai.md`](../../etudes/kai.md)).

**Ta machine**, la configuration de référence du calcul (config donnée le 22/10) :
- CPU Ryzen 7 9700X (8 cœurs), carte mère Gigabyte B850M AORUS ELITE WIFI6E ICE (4 slots DDR5) ;
- **RTX 5080 16 Go** (Inno3D X3 OC), achetée **1 100 € en 2025** (24/10) ;
- **32 Go de DDR5-6000** (2 × 16 Go, EXPO activé), payés **92,95 € en 2025** (ta correction du 24/10). La même RAM est à **560 € sur Amazon** (ton relevé du 24/10) ;
- SSD Samsung 990 EVO Plus 2 To et Crucial P3 Plus 1 To ;
- alimentation Corsair RM1000e (1000 W) ;
- **le PC complet** : monté pour jouer en 2025, **2 000 €** (24/10).

Avec 32 Go de RAM, les modèles à experts géants (Qwen3.8-Flash-Next complet, DeepSeek) sont exclus. **Depuis le 25/10, il n'y a plus de démo du tout** : le paragraphe qui suit dit quel modèle on met en avant, d'après les mesures publiées. La version Coder de Flash-Next via Strata tiendrait, mais **ta décision du 24/10** : la démo reste sur **Qwen3.8-27B dans LM Studio**, la plus simple et la plus grand public, comparée à Claude Code en mode sans échec (`--safe-mode`) des deux côtés. Strata est traité, calculé et sans démo, dans [Combien coûte Claude en local ?](../cout-claude-local/fiche.md). Raison : [Luke's Dev Lab](https://www.youtube.com/watch?v=xiMAxAQAfC4) (23/10) montre un Coder 2 fois plus rapide, mais moins soigné et moins autonome que le 27B. Plan d'essais : [`modeles-5080.md`](modeles-5080.md) ; vidéos de référence : [`references.md`](references.md).

| Champ | Détail |
|---|---|
| **Pilier** | IA chez moi (Hub + Help) |
| **Format** | Longue, 12-15 min |
| **Trafic visé** | Accueil + recherche |
| **Mot-clé** | ia en local |
| **Type de hook** | Récit avec révélation |
| **Production estimée** | ~25 h, sans essais (estimation du 25/10 ; avant : ~35 h, dont ~10 h d'essais) |

**Titres** :
1. Recherche : *IA en local : 16 Go de VRAM, est-ce que ça suffit ?*
2. Curiosité : *Ma carte graphique peut-elle remplacer mon abonnement Claude ?*
3. Mixte (recommandé) : *16 Go de VRAM suffisent-ils pour remplacer Claude ?*

**Miniature** (21/10, pilier « IA chez moi » = charte verte) : [`vert-02.png`](../../ressources/miniatures/rendus/vert-02.png). Gabarit de la série : bandeau « ABONNEMENT OU IA LOCALE » (changé le 24/10 ; avant : « CLAUDE OU MON PC »), Claude à gauche, ta 5080 à droite avec « 16 Go » dans la baie du haut, « ? » au centre. L'ancienne idée (5080 + « ÇA SUFFIT ? ») reprenait la mise en page de Kai.

**Contenu** :
1. **Le hook** : ~~la révélation, « Claude Opus 5.5 ? Non, ma carte de 16 Go »~~ : sans démo, elle tombe (25/10). Piste pour les 15 premières secondes, le contraste le plus fort des mesures publiées : sur une RTX 5080, Qwen3.8-27B écrit environ **101 tokens par seconde** en Q3 avec MTP (sudoingX), mais le Q4, à peine plus gros, déborde en RAM et tombe à **13** (Hardware IA). Même carte, même modèle, un fichier d'écart. `⚠️ à vérifier` : les deux mesures n'ont pas le même réglage (moteur, contexte, MTP) ; dis-le, ou trouve une mesure qui compare les deux fichiers dans les mêmes conditions. Puis la règle 1 du calculé, dans les 30 s : « je n'ai pas fait de banc d'essai : j'ai rassemblé les mesures de ceux qui l'ont fait ».
2. **Ce qui rentre et ce qui ne rentre pas dans 16 Go** (repris du guide) : 3 ou 4 modèles, avec les vitesses mesurées par des utilisateurs qui ont une carte de 16 Go, citées et datées dans `sources.md` (les premières sont dans `modeles-5080.md`, section 0.1 et tableau 1.1). Au moins deux mesures qui concordent pour chaque chiffre important ; sinon, dis qu'il n'y en a qu'une. Une mesure isolée de Reddit était le point faible de Kai : des mesures croisées deviennent ta force (règle du 25/10).
3. **La quantization**, en deux phrases qui se suffisent (le JPEG de l'IA : moins de bits, un fichier plus léger, un peu moins de qualité). Les noms des fichiers se décodent dans [*IA en local*](../bases-ia-locale/fiche.md), qui sort après, le 7 déc. : une phrase (« je leur consacre une vidéo entière ») et une carte YouTube à ajouter le 7 déc.
4. **Les ratés**, documentés par d'autres (plus d'essais depuis le 25/10) : le Q4 qui déborde en RAM, le Coder de Strata plus rapide mais moins soigné (Luke's Dev Lab), le thinking qui fait attendre. Ton impression sur Qwen3.8-27B (« très lent ») peut s'y glisser, comme vécu.
5. **Le calcul en quatre cas** (ta demande du 24/10) : le prix d'achat seulement, pas d'électricité (décidé le 23/10). Mêmes prix que [Louer, acheter](../louer-acheter-ia/script.md), section « Le calcul » (relevé du 23/10, à refaire avant la voix) :
   | | Contre Pro (20 $ ≈ 21,42 € TTC) | Contre Max (100 $ ≈ 107,10 € TTC) |
   |---|---|---|
   | **Tu as déjà la carte** | rien à rembourser : 21 € gardés par mois, environ 257 € par an | rien à rembourser : 107 € gardés par mois, environ 1 285 € par an |
   | **Tu achètes la carte** (5080 neuve, 1 899,95 €) | 89 mois, plus de 7 ans | 17,7 mois, environ un an et demi |
   | **Tu achètes le PC complet** (4 049,95 €) | 189 mois, environ 16 ans | 37,8 mois, plus de 3 ans |
   | **Tu achètes d'occasion** | [PRIX D'OCCASION À RELEVER] ÷ 21,42 | [PRIX D'OCCASION À RELEVER] ÷ 107,10 |

   « Gardés » ne vaut que si le modèle de 16 Go te suffit : c'est ce que les mesures et les avis des utilisateurs viennent de montrer. Puis **le pour et le contre** :
   - local, pour : tes données restent chez toi, pas de limite toutes les cinq heures, ça marche hors ligne, la carte sert aussi à jouer ;
   - local, contre : un modèle de 16 Go n'est pas Claude, tout se paie d'avance, le prix de la carte est un pari (1 179 € annoncée, 1 200 € l'été 2026, 1 900 € en octobre) ;
   - abonnement, pour : le meilleur modèle, rien à installer, rien d'avance, tu peux couper quand tu veux ;
   - abonnement, contre : rationné toutes les cinq heures et à la semaine, en dollars plus la TVA, tes textes partent chez Anthropic.

   **Ton texte du 24/10**, à reprendre dans le script (tutoiement) : « La mienne, je l'ai eue en 2025 à 1 100 €. Aujourd'hui, on la trouve à 1 900 € : la preuve que la crise du matériel a vraiment tout cassé. Mon PC complet, je l'avais monté pour jouer en 2025 : il m'a coûté 2 000 €. La RAM ne m'avait coûté que 92,95 €, alors que la même vaut aujourd'hui 560 € sur Amazon. Et en ce moment, la 5080 coûte quasiment le même prix d'occasion qu'en neuf. Donc si tu pars du matériel que tu as déjà, ça te reviendra moins cher. Ou alors, l'occasion sur des modèles en dessous : une RTX 3060 peut se trouver à partir de 240 €, selon la personne qui revend sa carte. » Pour l'IA, dis « la 3060 de 12 Go » (il en existe une de 8 Go, moins utile : conseil 1 de `deux-cartes-occasion/sources.md`). Prix à revérifier le jour de la voix.

   Enfin **ton choix**, avec tes mots ⟦à écrire : ce que tu gardes, ce que tu fais sur ta carte⟧. Rien n'est écrit à ta place.
6. **Quoi acheter (ou pas) avant le Black Friday, selon ton profil** :
   - tu as déjà une carte de 12 ou 16 Go ;
   - tu pars de zéro, en neuf **ou d'occasion** (ta demande du 24/10 : les cartes d'occasion qui donnent le plus de VRAM par euro, leurs pièges, la garantie ; faits dans [`deux-cartes-occasion/sources.md`](../deux-cartes-occasion/sources.md), section « Pour les conseils d'achat d'occasion » : 10 conseils vérifiés deux fois le 24/10, prix à relever par toi) ;
   - tu n'en as pas besoin, reste sur l'abonnement.
   Prix en euros (neuf et occasion) relevés juste avant le script, puis épinglés en commentaire le 27 nov. (Black Friday).

**Les renvois** (ta règle du 24/10 : pas de « épisode un », on renvoie par le contenu) : en amont, [la vidéo d'installation](../installer-ia-locale/fiche.md) (2 nov.) a montré LM Studio : une phrase (« si t'as jamais installé d'IA chez toi, j'ai une vidéo qui le fait pas à pas, je te la mets là ») et une carte YouTube suffisent. Les noms (B, A3B, Q4_K_M) sont expliqués après, dans *IA en local* (7 déc., ta décision du 24/10) : ici, juste ce qu'il faut pour suivre. À la fin, la suite : « ce qui ne tient pas dans seize gigas, je l'ai calculé » (Coût Claude, une semaine plus tard, le 23 nov.), comme Morgans Code relie ses vidéos entre elles.
