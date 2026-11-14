# L'IA locale sans grosse carte graphique

> Planning : [`calendrier.md`](../../calendrier.md), **lun. 7 déc. 2026 à 18 h**. Idée de l'auteur (05/11) pour le public sans carte de 16 Go (63 % Afrique). Radar : [`etudes/radar.md`](../../etudes/radar.md), entrée du 05/11.

| Champ | Détail |
|---|---|
| **Pilier** | IA chez moi (calculé : sources et mesures publiées, aucun essai) |
| **Format** | Longue, 10-12 min |
| **Angle** | Quelle IA locale avec un petit budget ? Le PC que tu as déjà, la RAM plutôt que la carte, et Strata comme exemple |

## Strata (relevé sur GitHub le 05/11/2026, à revérifier avant le script)

- [Niko1221/Strata](https://github.com/Niko1221/Strata) : moteur d'inférence en C++, licence MIT, installation en un clic sur Windows et Linux, API OpenAI/Anthropic sur localhost. Créé le 24/09/2026, environ 40 K étoiles.
- L'astuce : les modèles « MoE » gardent leurs experts en **RAM** (voire sur le SSD) plutôt que dans la carte graphique.
- **Piège factuel** : ce n'est pas « sans matériel ». Il faut une carte RTX 20 à 50, une AMD récente ou un Mac M1+, **et beaucoup de RAM** : Qwen3.8-Flash-Next demande 37,6 à 54,8 Go (RAM + VRAM), Qwen3.6-35B-A3B 32 à 52 Go, et DeepSeek V4.1-Flash une carte de 12 Go, 46 Go de RAM au moins et ~257 Go de disque. Mesure publiée : environ 5 tokens/s en code sur RTX 5070 12 Go + 64 Go de RAM.
- La promesse honnête : « pas besoin d'une carte à 1 000 € », et non « ça tourne sur n'importe quel PC ».

## À faire

- [ ] Recherche des autres options petit budget (petits modèles sur CPU, PC d'occasion, prix de la RAM), puis double vérification
- [ ] Mots-clés vidIQ en `fr` (ia locale petit budget, ia sans carte graphique, strata)
- [ ] Titres, puis les 15 premières secondes : le résultat d'abord
