# Abonnement ou IA locale ? #1 : 16 Go de VRAM suffisent-ils ?

> **24/10** : la série s'appelle « Abonnement ou IA locale ? » (c'est aussi la playlist) au lieu de « Claude ou mon PC ? », puisqu'on compare plusieurs abonnements à l'IA locale. Dans la voix, pas de « épisode un » : les vidéos se renvoient par ce qu'elles expliquent. Le dossier garde son nom.

> Analyse (hook, pourquoi, score) : [`strategie.md`](../../strategie.md), idée 1. Planning : [`calendrier.md`](../../calendrier.md). Premier jet : [`brouillon-script.md`](brouillon-script.md).

**Origine** : « Le second pouvoir de votre carte graphique : héberger une IA en local sur une 5080 ». Inspiration : [Red Stapler, I ran Qwen3.8 27B on single 8GB Card!](https://www.youtube.com/watch?v=ye50BbXEczo).

**Mis à jour le 18/10** : le titre met en avant ta carte de 16 Go, et la vidéo reprend le contenu du guide IA en local 2027 (voir [`archive/`](../../archive/README.md)). Elle sort le **16 nov. à 18 h** (avancée au 2 nov. le 22/10, revenue au 16 nov. le 23/10 : la vidéo qui pose les bases sort avant elle le 2 nov., aujourd'hui [celle de l'installation](../installer-ia-locale/fiche.md) depuis le 24/10 ; ses essais sur la 5080, les 23-24/10, servent ensuite à « Combien coûte Claude en local ? », le 23 nov. depuis le 24/10). Preuve : chez Kai, [Is 16GB All You Need for Serious Local LLM?](https://www.youtube.com/watch?v=i9mRnbdDYxk) fait 359 K vues en 10 jours, et ses vidéos sur le matériel et le coût font environ 2 fois plus de vues que ses tests de modèles (voir [`etudes/kai.md`](../../etudes/kai.md)).

**Machine de test** (config donnée le 22/10) :
- CPU Ryzen 7 9700X (8 cœurs), carte mère Gigabyte B850M AORUS ELITE WIFI6E ICE (4 slots DDR5) ;
- **RTX 5080 16 Go** (Inno3D X3 OC), achetée **1 100 € en 2025** (24/10) ;
- **32 Go de DDR5-6000** (2 × 16 Go, EXPO activé), payés **92,95 € en 2025** (ta correction du 24/10). La même RAM est à **560 € sur Amazon** (ton relevé du 24/10) ;
- SSD Samsung 990 EVO Plus 2 To et Crucial P3 Plus 1 To ;
- alimentation Corsair RM1000e (1000 W) ;
- **le PC complet** : monté pour jouer en 2025, **2 000 €** (24/10).

Avec 32 Go de RAM, les modèles à experts géants (Qwen3.8-Flash-Next, DeepSeek) sont exclus. Plan d'essais : [`modeles-5080.md`](modeles-5080.md) ; vidéos de référence : [`references.md`](references.md).

| Champ | Détail |
|---|---|
| **Pilier** | IA chez moi (Hub + Help) |
| **Format** | Longue, 12-15 min |
| **Trafic visé** | Accueil + recherche |
| **Mot-clé** | ia en local |
| **Type de hook** | Récit avec révélation |
| **Production estimée** | ~35 h, dont ~10 h d'essais (estimation, fusion de deux fiches) |

**Titres** :
1. Recherche : *IA en local : 16 Go de VRAM, est-ce que ça suffit ?*
2. Curiosité : *Ma carte graphique peut-elle remplacer mon abonnement Claude ?*
3. Mixte (recommandé) : *16 Go de VRAM suffisent-ils pour remplacer Claude ?*

**Miniature** (21/10, pilier « IA chez moi » = charte verte) : [`vert-02.png`](../../ressources/miniatures/rendus/vert-02.png). Gabarit de la série : bandeau « ABONNEMENT OU IA LOCALE » (changé le 24/10 ; avant : « CLAUDE OU MON PC »), Claude à gauche, ta 5080 à droite avec « 16 Go » dans la baie du haut, « ? » au centre. L'ancienne idée (5080 + « ÇA SUFFIT ? ») reprenait la mise en page de Kai.

**Contenu** :
1. **La révélation (hook)** : on montre le résultat, « Claude Opus 5.5 ? Non, ma carte de 16 Go. »
2. **Ce qui rentre et ce qui ne rentre pas dans 16 Go** (repris du guide) : 3 ou 4 modèles, avec la vitesse mesurée chez toi. Mesure toi-même, ne cite pas Reddit : c'est le point faible de Kai.
3. **La quantization**, en deux phrases qui se suffisent (le JPEG de l'IA : moins de bits, un fichier plus léger, un peu moins de qualité). Les noms des fichiers se décodent dans [*IA en local*](../bases-ia-locale/fiche.md), qui sort après, le 7 déc. : une phrase (« je leur consacre une vidéo entière ») et une carte YouTube à ajouter le 7 déc.
4. **Les ratés** des essais.
5. **Le calcul en quatre cas** (ta demande du 24/10) : le prix d'achat seulement, pas d'électricité (décidé le 23/10). Mêmes prix que [Louer, acheter](../louer-acheter-ia/script.md), section « Le calcul » (relevé du 23/10, à refaire avant la voix) :
   | | Contre Pro (20 $ ≈ 21,42 € TTC) | Contre Max (100 $ ≈ 107,10 € TTC) |
   |---|---|---|
   | **Tu as déjà la carte** | rien à rembourser : 21 € gardés par mois, environ 257 € par an | rien à rembourser : 107 € gardés par mois, environ 1 285 € par an |
   | **Tu achètes la carte** (5080 neuve, 1 899,95 €) | 89 mois, plus de 7 ans | 17,7 mois, environ un an et demi |
   | **Tu achètes le PC complet** (4 049,95 €) | 189 mois, environ 16 ans | 37,8 mois, plus de 3 ans |
   | **Tu achètes d'occasion** | [PRIX D'OCCASION À RELEVER] ÷ 21,42 | [PRIX D'OCCASION À RELEVER] ÷ 107,10 |

   « Gardés » ne vaut que si le modèle de 16 Go te suffit : c'est ce que ton test vient de montrer. Puis **le pour et le contre** :
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
