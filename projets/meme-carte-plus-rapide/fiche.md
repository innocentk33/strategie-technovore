# Même carte, 2 fois plus rapide

> Fiche du 10/11/2026. Idée 16 de [`strategie.md`](../../strategie.md) (34/40), placée au **jeu. 19 nov., 18 h** au [radar du 10/11](../../etudes/radar.md). Vidéo **calculée**.

**Inspiration** : Code Unpacked, « llama.cpp… 4× Faster » (11,2 K vues en un jour avec 506 abonnés, 22/10 ; [étude](../../etudes/outliers-2026-10-22.md)), et le meilleur format de Morgans Code. On ne reprend pas leur angle.

| Champ | Détail |
|---|---|
| **Pilier** | IA chez moi |
| **Format** | Longue, 10-12 min. Calculée : réglages et mesures publiées, aucune vitesse à toi |
| **Trafic visé** | Recherche (« ia en local plus rapide », « llama.cpp ») et suggestions |
| **Type de hook** | Résultat chiffré : d'après les mesures publiées, le même PC va [X] fois plus vite avec trois réglages |
| **Production** | 1 à 2 jours |

## Contenu (à affiner)

- Les réglages qui changent la vitesse sans changer de carte : le bon fichier (quantisation), le déchargement sur la carte, la taille du contexte, le cache KV quantisé, le décodage spéculatif ou le MTP, le bon moteur (llama.cpp, LM Studio, Ollama).
- Chaque gain vient d'une mesure publiée, datée, et si possible de deux qui concordent (règle 3 du calculé).
- Le pont : vers *16 Go de VRAM suffisent* (9 nov.) et vers *32 Go de VRAM* (23 nov.).

## Points à vérifier

1. Les versions de llama.cpp et LM Studio du jour, et ce qu'elles changent.
2. Au moins deux mesures concordantes par gain cité.
3. `sources.md` à créer.
