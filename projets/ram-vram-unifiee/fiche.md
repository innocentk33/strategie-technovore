# RAM, VRAM ou mémoire unifiée : laquelle fait tourner ton IA le plus vite ?

> Fiche du 14/11/2026, à ta demande. Placée au **jeu. 3 déc., 18 h**, à la place de [DeepSeek V4.1 Flash](../cout-deepseek-flash/fiche.md), qui sort désormais juste avant, le lun. 30 nov. (15/11) : DeepSeek montre le résultat (sans carte graphique, 64 Go de RAM), et cette vidéo explique pourquoi. Elle prépare le [Mac mini](../mac-mini-ia/fiche.md) (10 déc.) en posant la mémoire unifiée. Vidéo **calculée**, plus les mesures de ton test [Strata](../strata-test/fiche.md) (16 nov.). Idée 29 de [`strategie.md`](../../strategie.md), non notée (ta demande du 14/11). Titre provisoire.

**Inspiration** : Locally, [*RAM vs VRAM vs Unified Memory (Local AI)*](https://www.youtube.com/watch?v=WpHKek1GV70) (titre de départ : *Which Memory Runs Local AI Fastest (RAM, VRAM, Unified)*), 12 min 50 s, publiée le 11/11 : 1 991 vues en 3 jours, avec 4,5 K abonnés (page YouTube, 14/11).
- **Son angle (à ne pas reprendre)** : la vitesse dépend de la bande passante, pas de la taille. La vitesse maximale vaut la bande passante divisée par la taille du modèle. Sur un 27B dense (environ 17 Go en 4 bits), il annonce moins de 6 tok/s avec 64 Go de DDR5 (83 à 96 Go/s) contre 33 tok/s sur une RTX 3090 (936 Go/s). Selon lui, déborder en RAM coûte 71 % de vitesse. Sa conclusion : la RAM est lente.
- **Notre angle (ton contre-pied)** : c'est vrai pour un modèle **dense**. Avec un modèle **MoE** et le bon moteur, la RAM redevient utile. Strata garde les experts en RAM, et ton test du 16 nov. tourne sur 16 Go de VRAM **et 32 Go de RAM**. La vraie question n'est donc pas « RAM ou VRAM ? », mais « quel modèle, avec quel moteur ? ».

| Champ | Détail |
|---|---|
| **Pilier** | IA chez moi |
| **Format** | Longue, 10-12 min. Calculée, avec tes mesures de Strata |
| **Trafic visé** | Recherche (« ram ou vram ia », « mémoire unifiée ia locale ») et suggestions sous Locally et sous ta vidéo Strata |
| **Type de hook** | Croyance renversée : « la RAM, c'est trop lent pour l'IA »… sauf que ma vidéo Strata tourne avec la moitié du modèle en RAM [CROCHET : le chiffre de ton test] |
| **Production** | 1 à 2 jours |

## Pistes (à sourcer)

- Les trois mémoires et leur bande passante : DDR5 en double canal, GDDR7, mémoire unifiée (Mac, Ryzen AI Max+ « Strix Halo »).
- La règle « bande passante ÷ taille » pour un modèle dense, et pourquoi un MoE ne lit qu'une partie de ses poids à chaque mot.
- Strata : ce qui est en VRAM, ce qui est en RAM, ce qui passe par le SSD (tes relevés : RAM 30,8 / 31 Go, lecture disque d'environ 200 Mo/s pendant qu'il écrit).
- Le pont vers le Mac mini (10 déc.) : la mémoire unifiée, grande mais plus lente qu'une carte graphique.
- Le prix de la RAM en novembre 2026 (en hausse, voir [Le Black Friday a-t-il fait baisser les prix ?](../prix-apres-black-friday/fiche.md)).

## Points à vérifier

1. **Les chiffres de Strata viennent de [`../strata-test/sources.md`](../strata-test/sources.md)**, et d'aucune autre source.
2. **L'affirmation à tenir** : « avec un modèle MoE et le bon moteur, la RAM compte autant que la VRAM pour **faire tenir** le modèle ». Ne jamais dire « la RAM est aussi rapide que la VRAM » : c'est faux, et la vitesse de ton test vient de la carte.
3. Les bandes passantes : la fiche technique du constructeur, pas un forum.
4. Ne pas recouper [petits budgets / 4 à 16 Go](../modele-par-vram/fiche.md) (18 janv.) : ici, on explique la mémoire ; là-bas, on donnera un modèle par palier.
5. `sources.md` à créer.
