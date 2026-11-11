# Qwen 4 arrive : les cartes graphiques qui le feront tourner

> Fiche du 10/11/2026, ta demande (« au plus vite »). Placée au **jeu. 12 nov., 18 h** dans le [`calendrier.md`](../../calendrier.md) et le [`README.md`](../../README.md), d'après le [radar du 10/11](../../etudes/radar.md) (32/40). Vidéo **calculée** : règles du pilier 2 dans [`strategie.md`](../../strategie.md).

**Inspiration** : Weights & Wonders, [*Don't Miss Out on These GPUs Before Qwen 4's Release!*](https://www.youtube.com/watch?v=kQKCp7PlVxY) (25,6 K vues, ×4,2 en 2 jours, publiée le 08/11 ; vidIQ, 10/11). On ne copie ni son angle (budget de 1 500 $, prix américains) ni sa miniature.

| Champ | Détail |
|---|---|
| **Pilier** | IA chez moi (actu) |
| **Format** | Longue, 10-12 min. Calculée |
| **Trafic visé** | Recherche « Qwen 4 » (personne n'en parle en français au 10/11) et suggestions sous Weights & Wonders, Morgans Code, Tech_Sama |
| **Type de hook** | Enjeu : si Qwen 4 27B tient ses promesses, les cartes qui le font tourner vont monter. **Corrigé le 11/11** : elles ont déjà monté sans lui (+20 % en 30 jours pour la 5060 Ti et la 5080, Q20) ; le hook du script part de là. |
| **Production** | 1 à 2 jours |

## Ce qu'on sait vraiment (radar du 10/11, corrigé le 11/11 par la relecture)

> **Corrigé le 11/11** (relecture du script, [`grill-v1.md`](grill-v1.md), faits Q1, Q2, Q3, Q6 et Q9 de [`sources.md`](sources.md)) : le 27B n'est pas « confirmé ». Flash-Next date du 24/08, et le Q4_K_M pèse 16,56 Go.


- **Confirmé par écrit** :
  - le 22/09/2026 (conférence Apsara), le communiqué d'Alibaba dit seulement que Qwen 4 est « en entraînement », sans nom de version, ni date, ni taille (Q1) ;
  - le 24/08, Qwen3.8-Flash-Next (Hugging Face) présente l'architecture de Qwen 4 (Q2) ;
  - teaser officiel « The becoming begins » le 06/11 ;
  - **depuis le 11/11, Qwen4-Max-Preview** dans le cloud d'Alibaba, jusqu'au 25/11, avec l'abonnement seulement (Q3).
- **Annoncé à l'oral, écrit nulle part par Alibaba** : les noms Qwen 4 Max, Plus, Flash et **27B**. D'après 36Kr (23/09) et d'autres sites, ils ont été montrés à la conférence, le 27B comme version ouverte prioritaire ; une source les attribue plutôt à un post sur X (Q6). Ni taille, ni date, ni licence, ni poids.
- **Rumeur** : une sortie en novembre (propos de seconde main, conférence du 29/10) ; des identifiants `qwen4-*` dans du code (28/10).
- **Aucun fichier Qwen 4 sur Hugging Face** au 10/11. Si Qwen 4 sort avant la publication, la vidéo change : tailles réelles des fichiers au lieu de l'estimation.
- **À dire dans la vidéo** : « ce qui est sûr » / « ce qu'on raconte », séparés à l'écran. Jamais une rumeur présentée comme un fait.

## L'angle Technovore

- Le point de départ calculable : **Qwen3.8-27B**, le plus proche du Qwen 4 27B annoncé. Son Q4_K_M fait **16,56 Go** au 11/11 (Q9 ; 16,46 Go le 24/10, F41 de [`deux-cartes-occasion/sources.md`](../deux-cartes-occasion/sources.md), fichiers republiés depuis) : il ne tient pas dans 16 Go.
- **Les prix en euros**, relevés en France le jour du script, et un encart pour l'Afrique francophone (63 % du public) : ce qui se trouve vraiment, et à quel prix. [CROCHET : tes relevés]
- **Trois paliers** : 16 Go (ce que tu as : quel fichier choisir, renvoi vers *16 Go de VRAM suffisent*), 24 Go, 32 Go (renvoi vers la vidéo 32 Go du 23 nov.).
- **Le conseil honnête** : faut-il acheter avant la sortie ? Le seul signal de hausse de prix chez W&W (Tesla P100 de 80 à 180 $ en deux mois sur eBay) est une observation américaine : à vérifier ou à dire comme telle.

## Titres

1. *Qwen 4 arrive : quelle carte graphique pour le faire tourner chez toi ?*
2. *Qwen 4 : achète cette carte graphique avant qu'elle monte (ou pas)*
3. Recommandé : *Qwen 4 arrive : ce qu'il te faudra pour le faire tourner chez toi*

## Miniature

**Faite le 11/11, style OpenCode** (la charte verte est abandonnée) : [`miniature/propositions.md`](miniature/propositions.md). Logo Qwen et une vraie ASUS TUF 5090 en petit, « RTX 5090 » en blanc, « 7 900 € » en rouge, et un meme à droite : Harold (a, recommandée) ou Jackie Chan « WTF » (b), pour le test A/B. Le prix reprend le hook (Q21) : à revérifier le 12/11. Rien qui dise que Qwen 4 est sorti.

~~Ancienne idée (10/11) : charte verte, carte au trait, « QWEN 4 / 24 GO ? ».~~

## Points à vérifier avant le script

1. Qwen 4 est-il sorti entre le 10 et le 12/11 (blog Qwen, Hugging Face, GitHub) ?
2. Sources primaires de l'annonce du 22/09 (Alibaba Cloud, Apsara) : citer celles-là, pas un article de seconde main.
3. Prix du jour en euros, TVA comprise (neuf et occasion), datés.
4. `sources.md` à créer, comme dans les autres projets.
