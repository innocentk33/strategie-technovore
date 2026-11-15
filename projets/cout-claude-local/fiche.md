# Combien coûte Claude Fable 5.2 chez toi ?

> **15/11, ta décision : fusion avec [Combien coûte Kimi K3.1 Pro chez toi ?](../../archive/cout-kimi/fiche.md)**, archivée. La vidéo sort le **lun. 14 déc., 18 h** (créneau de Kimi), au lieu du jeu. 31 déc., qui passe au radar. Titre provisoire : *Combien coûte Claude Fable 5.2 chez toi ? (j'ai fait le calcul)*.
> - **Pourquoi Fable 5.2** : sorti le 09/11/2026 chez Anthropic (avec Mythos 5.2, réservé à des organisations vérifiées), annoncé jusqu'à 30 % plus rapide et 20 % moins cher en API que Fable 5.1 ([9to5Mac](https://9to5mac.com/2026/11/09/anthropic-upgrades-claude-with-new-fable-5-2-model-details-here/), [SD Times](https://sdtimes.com/ai/anthropic-introduces-claude-fable-5-2-mythos-5-2/), relevé le 15/11). C'est le modèle en tendance ; Kai a fait 105 K vues (x38) avec Fable 5 (voir « Origine »). Si un autre Claude sort avant le script, on prend le dernier.
> - **Le modèle de calcul change** : Anthropic ne publie ni la taille ni les poids, donc on calcule avec les **modèles ouverts d'environ 1 To**, dont Kimi K3.1 Pro (la vidéo de Kimi tient en une partie). DeepSeek V4.1 Flash, l'ancien modèle de calcul, a sa propre vidéo le 30 nov. : on y renvoie.
> - **Nouvelle inspiration** : Pop Theory, [*What It Actually Costs to Run a 1TB AI Model at Home*](https://www.youtube.com/watch?v=yw5mMVq6gas), 17 min 22 s, publiée le 13/11 : **8 569 vues en 2 jours avec 1,49 K abonnés** (page YouTube, 15/11). Vidéo entièrement calculée (« we ran no tests of our own »). **Son angle (à ne pas reprendre)** : une seule facture en dollars pour chaque route (2 Mac Studio, serveur DDR5, 8 DGX Spark, 11 RTX PRO 6000, DGX Station, serveur DDR4 d'occasion, lecture sur SSD), la consommation, la vitesse, puis qui devrait en construire un. Il cite Muse Spark Open, Mistral Large 4 et Kimi K3.1 Pro (« about a terabyte or more ») : tailles à vérifier sur Hugging Face. **Notre angle** : le titre Claude, les prix en euros TVA comprise et en FCFA, les routes à la portée d'un particulier d'abord, et le retournement sur ce qui tient vraiment sur ta 5080.
> - **À refaire** : le [script v2](script.md) date du 22/10 (Opus 5.5, DeepSeek comme modèle de calcul, Kimi K3 en deux phrases, promesse de « Louer, acheter » au 4 janv.). Il faut une v3 : modèle Fable 5.2, modèle de calcul d'environ 1 To, `sources.md` à compléter (Kimi K3.1 Pro, les routes, les prix de novembre). Garde le calcul en quatre cas de Claude #1.
> - **Miniature** : V9 (Michael Scott, Severance, `miniature/sources/michael-vert.png`), avec M. Krabs (`krabs-vert.png`, l'ancienne miniature de Kimi) en rechange. Plan : [`plan-kai-31-12.md`](../../ressources/miniatures/plan-kai-31-12.md).
>
> **15/11, plus tôt** : la vidéo sortait le jeu. 31 déc., à la place de *L'IA cachée dans ta carte graphique*, archivée.
>
> **05/11** : récupère de [Claude #1](../claude-ou-mon-pc-1/fiche.md) (section 5 de sa fiche) le calcul en quatre cas et les conseils d'achat (neuf et occasion), retirés du script du 9 nov. pour le garder court.

> **Publication : lun. 23 nov. à 18 h** (avancée du 4 janv. au 2 nov. le 21/10, reculée au 16 nov. le 22/10 pour réutiliser les essais de [Claude #1](../claude-ou-mon-pc-1/fiche.md), au 30 nov. le 23/10, quand Claude #1 est passé au 16 nov., puis au 23 nov. le 24/10, à ta demande, pour sortir avant le Black Friday). Format **calculé** : les règles sont dans [`strategie.md`](../../strategie.md), pilier 2. Planning : [`calendrier.md`](../../calendrier.md), S4-S5. Études : [`etudes/kai.md`](../../etudes/kai.md) (idée 2) et [`etudes/morganscode.md`](../../etudes/morganscode.md).

**Origine** : la série de Kai « What Would It Cost to Run [modèle] Locally? », qui compte 4 de ses 7 plus gros succès. Par exemple [Claude Fable 5](https://www.youtube.com/watch?v=fXWFSTSvnVM) (105 K vues, x38), [Claude Opus 5](https://www.youtube.com/watch?v=yJCHNdQ8sLs) (166 K vues, x23,5) et [DeepSeek V4.1 Flash](https://www.youtube.com/watch?v=04ePeOyRN0k) (529 K vues, x20,9). Personne ne fait ce format en français.

| Champ | Détail |
|---|---|
| **Pilier** | IA chez moi (Hub) |
| **Format** | Longue, 13-16 min |
| **Trafic visé** | Accueil + recherche |
| **Mot-clé** | ia en local / claude en local |
| **Type de hook** | Une idée reçue, puis une vraie question avec des réponses contradictoires |
| **Production estimée** | ~25-30 h (estimation) : surtout de la recherche et des animations, presque pas d'essais |

**Titres** (prends le dernier modèle Claude sorti au moment du script) :
1. Recherche : *Faire tourner Claude en local : combien ça coûte vraiment ?*
2. Curiosité : *J'ai calculé le PC qu'il faut pour faire tourner Claude chez moi*
3. Mixte (recommandé) : *Combien coûte Claude Opus 5.5 en local ? (j'ai fait le calcul)*

**Miniature** (21/10, charte verte) : [`vert-05.png`](../../ressources/miniatures/rendus/vert-05.png). Ta 5080 minuscule au pied d'une baie de serveurs géante, « Claude chez moi, » et le prix calculé dans l'étiquette (« ?? ??? € » pour l'instant). L'ancienne idée (logo Claude, flèche, serveurs) était la mise en page de la série de Kai.

**Contenu** (la structure de Kai, avec les différences de Technovore) :
1. **Hook** : « On peut remplacer Claude par une IA locale », puis une vraie question trouvée sur Reddit ou X, avec des réponses qui se contredisent.
   - ⚠️ **Règle des 15 premières secondes** (22/10, `strategie.md`, section 5) : ce sont les secondes les plus fortes de la vidéo. Ouvre sur le prix final calculé (celui de la miniature) ou sur l'image de ta 5080 à côté de la baie de serveurs, puis l'idée reçue. La question Reddit vient juste après.
2. **La transparence d'abord** : Anthropic ne publie ni la taille de Claude ni ses poids. On calcule donc avec le plus gros modèle ouvert de même niveau, et on le dit tout de suite. Candidat au 21/10 : **DeepSeek V4.1 Flash** (552 milliards de paramètres, ~16 milliards actifs par token), que DeepSeek place au niveau d'Opus 5 en code. Ces chiffres viennent de Morgans Code : à revérifier dans la fiche du modèle et le tableau de DeepSeek.
3. **Le calcul de mémoire** (paramètres × bits), **du moins cher au plus cher** : ta 5080 (16 Go), un Mac Studio, un serveur à 8 GPU, puis plusieurs serveurs.
   - **Strata, ta décision du 24/10** : on en parle ici, **calculé et théorique, sans démo** ; la démo de [la vidéo des 16 Go](../claude-ou-mon-pc-1/fiche.md) reste sur Qwen3.8-27B dans LM Studio.
     - Le cas à calculer : comment Strata fait tenir Qwen3.8-Flash-Next (125 milliards de paramètres) sur un PC de jeu (experts en RAM, table Ngram sur le SSD), et le Coder (la moitié des experts) avec 32 Go de RAM. Les chiffres sont dans [`modeles-5080.md`](../claude-ou-mon-pc-1/modeles-5080.md), section 0.2.
     - La nuance à donner : Luke's Dev Lab, [Qwen 3.8 27B vs Strata Coder](https://www.youtube.com/watch?v=xiMAxAQAfC4) (23/10/2026, 53 K vues au 24/10, vidIQ), même config (16 Go de VRAM, 32 Go de RAM). Le Coder écrit environ 2 fois plus vite (40 contre 17 tok/s sur sa carte bridée à 70 W). Mais le 27B donne des interfaces plus soignées et demande moins de coups de pouce : le Coder a attendu des tests bloqués et a enregistré des fichiers dans le mauvais dossier. Luke préfère le 27B.
4. **Ce qui te démarque de Kai** : les prix en euros, TVA comprise. Pas d'électricité (décidé le 23/10 : le seul coût est l'achat).
5. **Le retournement** : ce qui tient vraiment sur une 5080, d'après les mesures publiées (plus d'essai depuis le 25/10). Reprends les mesures de Claude #1 (sorti le 16 nov., une semaine avant) et mets-le en écran de fin. En pratique, on fait le quotidien en local et les tâches les plus dures dans le cloud.
6. **Le verdict selon ton profil.**

**Points à vérifier** :
- le dernier modèle Claude sorti ;
- le plus gros modèle ouvert du moment et sa taille officielle ;
- les prix de location de serveurs, en euros ;
