# 54 Go de VRAM pour environ 32 € : que valent ces cartes de minage pour ton IA ?

**Publication prévue le lundi 25 janvier 2027 à 18 h (Paris).** [Calendrier du 20 novembre](../../calendrier.md)

> **Version de référence du 16/11/2026 : [script corrigé](script.md), [téléprompteur](teleprompteur.txt), [sources](sources.md) et [roast indépendant](grill-v1.md).** Format documentaire calculé : aucun nouvel essai, achat, enregistrement logiciel ou ouverture de LM Studio à produire. Les pistes ci-dessous restent l’historique ; les faits et limites du script corrigé prévalent.
> Fiche du 15/11/2026, à ta demande (remplir les créneaux radar de janvier). Placée au **jeu. 21 janv. 2027, 18 h**, **provisoire, à confirmer au radar**. Vidéo **calculée**. Idée 32 de [`strategie.md`](../../strategie.md), non notée (relevé YouTube du 15/11). Titre provisoire.

**Inspiration** (vues relevées sur YouTube le 15/11) : Kai, [*54GB VRAM For $35 The Cheapest Local AI Hack?*](https://www.youtube.com/watch?v=oUsXv7ZoYQg) (22,8 K vues en 18 h, publiée le 14/11) : un utilisateur de Reddit paie environ 35 $ une ferme de minage de neuf P106-100 (la puce de la GTX 1060 sans sortie vidéo). Qwen 3.6 35B A3B y tourne à plus de 30 tok/s dans Ollama, mais un 70B dense plafonne vers 4,5 tok/s. En français : DiscoverID, [*J'ai transformé une Carte Graphique à 150€ en un PC Gamer 4K (BC-250)*](https://www.youtube.com/watch?v=PCgWUJ1_aVY) (216 K vues en 3 semaines).
- **Leur angle (à ne pas reprendre)** : le hack viral, puis ce que le titre ne dit pas (les cartes en série vont à la vitesse d'une seule).
- **Notre angle** : **le guide pour petit budget, en euros et en FCFA** : quelles cartes de minage ou d'occasion (P106, P104, BC-250, Tesla P40…) valent le coup pour l'IA locale, ce qu'elles font tourner, et les pièges (pilotes, alimentation, carte mère, bruit). C'est le public de la chaîne : 63 % en Afrique.

| Champ | Détail |
|---|---|
| **Pilier** | IA chez moi |
| **Format** | Longue, 10-12 min. Calculée |
| **Trafic visé** | Suggestions sous Kai et DiscoverID ; recherche « carte graphique pas chère ia » |
| **Type de hook** | Résultat chiffré : neuf cartes pour environ 32 €, 54 Go de VRAM… et la vitesse d'une seule |
| **Production** | 1 à 2 jours |

## Pistes (à sourcer)

- Pourquoi un MoE va vite même sur ces cartes, et pas un modèle dense (renvoi à [RAM, VRAM ou mémoire unifiée](../ram-vram-unifiee/fiche.md), 31 déc., et à [Deux cartes graphiques](../multi-gpu/fiche.md), 7 déc.).
- Les prix d'occasion en France et en Afrique, relevés par toi.
- Les limites : pilotes CUDA, PCIe x1, consommation (sans calcul d'électricité, règle du 23/10).

## Points à vérifier

1. Remonter au post Reddit et aux articles (Tom's Hardware, Wccftech), et les dater.
2. Vérifier quelles cartes sont encore prises en charge par llama.cpp et Ollama.
3. `sources.md` à créer.
