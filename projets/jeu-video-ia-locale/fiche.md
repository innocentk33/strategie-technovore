# Créer un jeu vidéo avec une IA locale, sur une carte de 16 Go

> Fiche du 15/11/2026, ton choix (à la place de JARVIS, qui retourne en réserve). Placée au **jeu. 14 janv. 2027, 18 h**, **provisoire, à confirmer au radar**. Vidéo **calculée**, avec ce que tu as déjà filmé pour Strata. Idée 31 de [`strategie.md`](../../strategie.md), non notée (relevé YouTube du 15/11). Titre provisoire.

**Inspiration** (vues relevées sur YouTube le 15/11) :
- PΔX, [*J'ai créé un JEU VIDÉO en IA chez Moi !!*](https://www.youtube.com/watch?v=qOywnuU2ypM), en français, 21 min 15 s, publiée le 12/11 : 33,8 K vues en 3 jours. Il code un jeu avec une IA 100 % locale sur une Radeon AI PRO R9700 (32 Go de VRAM), à environ 80 tok/s, et pose la question de la rentabilité face à ChatGPT ou Claude. La vidéo est sponsorisée par ASUS.
- Stefan 3D AI, [*Made a Game With a $20 AI Plan and Already Got Sales*](https://www.youtube.com/watch?v=iJ83GYk2BIA) (205 K en 2 semaines, 212 K abonnés) : il présente les jeux de ses abonnés, faits avec l'IA **du cloud**. C'est un signal de demande pour le sujet « jeu + IA », pas pour le local.

- **Leur angle (à ne pas reprendre)** : un défi sur une carte pro de 32 Go (PΔX), ou une vitrine de jeux faits dans le cloud (Stefan).
- **Notre angle** : **avec la carte d'un joueur (16 Go), jusqu'où va une IA locale pour faire un jeu ?** Le code (ton mini-Minecraft et ton casse-briques de Strata comme preuves déjà filmées), puis ce qui manque encore : les sprites, les modèles 3D, les sons, et ce que chaque outil local demande en VRAM. Ta passion du jeu vidéo et ton humour gamer.

| Champ | Détail |
|---|---|
| **Pilier** | IA chez moi |
| **Format** | Longue, 10-12 min. Calculée, avec tes images de Strata |
| **Trafic visé** | Suggestions sous PΔX et sous les vidéos « j'ai créé un jeu avec l'IA » ; ta vidéo Strata y renvoie |
| **Type de hook** | Démo : le mini-Minecraft qui tourne, codé par une IA sur ta carte, sans internet |
| **Production** | 1 à 2 jours |

## Pistes (à sourcer)

- Le code : ce que le Coder de Strata a réussi et raté (chiffres de [`../strata-test/sources.md`](../strata-test/sources.md)).
- Les visuels en local : sprites et textures (génération d'images), modèles 3D (outils image → 3D), avec leur VRAM.
- Les sons et la musique en local.
- Le moteur de jeu (Godot, three.js) : ce que l'IA écrit bien, et ce qu'il faut corriger à la main.

## Points à vérifier

1. Les chiffres de Strata viennent de ses sources, et d'aucune autre.
2. Chaque outil d'image ou de 3D : sa VRAM et sa licence (usage commercial ?), relevées le jour du script.
3. Pas de nom de chaîne dans la voix.
4. `sources.md` à créer.
