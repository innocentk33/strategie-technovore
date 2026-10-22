# Claude ou mon PC ? #1 : 16 Go de VRAM suffisent-ils ?

> Analyse (hook, pourquoi, score) : [`strategie.md`](../../strategie.md), idée 1. Planning : [`calendrier.md`](../../calendrier.md). Premier jet : [`brouillon-script.md`](brouillon-script.md).

**Origine** : « Le second pouvoir de votre carte graphique : héberger une IA en local sur une 5080 ». Inspiration : [Red Stapler, I ran Qwen3.8 27B on single 8GB Card!](https://www.youtube.com/watch?v=ye50BbXEczo).

**Mis à jour le 18/10** : le titre met en avant ta carte de 16 Go, et la vidéo reprend le contenu du guide IA en local 2027 (voir [`archive/`](../../archive/README.md)). Elle sort le **2 nov. à 18 h** (avancée du 16 nov. le 22/10 : ses essais sur la 5080, les 23-24/10, servent ensuite à « Combien coûte Claude en local ? », le 16 nov.). Preuve : chez Kai, [Is 16GB All You Need for Serious Local LLM?](https://www.youtube.com/watch?v=i9mRnbdDYxk) fait 359 K vues en 10 jours, et ses vidéos sur le matériel et le coût font environ 2 fois plus de vues que ses tests de modèles (voir [`etudes/kai.md`](../../etudes/kai.md)).

**Machine de test** (config donnée le 22/10) :
- CPU Ryzen 7 9700X (8 cœurs), carte mère Gigabyte B850M AORUS ELITE WIFI6E ICE (4 slots DDR5) ;
- **RTX 5080 16 Go** (Inno3D X3 OC) ;
- **32 Go de DDR5-6000** (2 × 16 Go, EXPO activé), payés **99 € en 2025**. Le même kit est affiché à 491,99 $ en octobre 2026 ;
- SSD Samsung 990 EVO Plus 2 To et Crucial P3 Plus 1 To ;
- alimentation Corsair RM1000e (1000 W).

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

**Miniature** (21/10, pilier « IA chez moi » = charte verte) : [`vert-02.png`](../../ressources/miniatures/rendus/vert-02.png). Gabarit de la série : bandeau « CLAUDE OU MON PC », Claude à gauche, ta 5080 à droite avec « 16 Go » dans la baie du haut, « ? » au centre. L'ancienne idée (5080 + « ÇA SUFFIT ? ») reprenait la mise en page de Kai.

**Contenu** :
1. **La révélation (hook)** : on montre le résultat, « Claude Opus 5.5 ? Non, ma carte de 16 Go. »
2. **Ce qui rentre et ce qui ne rentre pas dans 16 Go** (repris du guide) : 3 ou 4 modèles, avec la vitesse mesurée chez toi. Mesure toi-même, ne cite pas Reddit : c'est le point faible de Kai.
3. **La quantization**, expliquée avec une image (Kai utilise celle du grand bureau face au petit bureau avec une étagère).
4. **Les ratés** des essais.
5. **Ce que ça coûte** : la consommation de la 5080 pendant qu'elle code, au tarif français de l'électricité, comparée à l'abonnement Claude.
6. **Quoi acheter (ou pas) avant le Black Friday, selon ton profil** :
   - tu as déjà une carte de 12 ou 16 Go ;
   - tu pars de zéro ;
   - tu n'en as pas besoin, reste sur l'abonnement.
   Prix en euros relevés juste avant le script (24-25 oct.), puis épinglés en commentaire le 27 nov. (Black Friday).

**Le fil de la série** : c'est le premier épisode. Termine sur la suite : « ce qui ne tient pas dans 16 Go, je l'ai calculé, et ça sort le 16 nov. » (Coût Claude), comme Morgans Code relie ses vidéos entre elles.
