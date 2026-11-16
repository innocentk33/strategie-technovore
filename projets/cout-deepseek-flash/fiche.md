# Combien coûte DeepSeek V4.1 Flash chez toi ?

> **Version de référence du 16/11/2026 : [script corrigé](script.md), [téléprompteur](teleprompteur.txt), [sources](sources.md) et [roast indépendant](grill-v1.md).** Format documentaire calculé : aucun nouvel essai, achat, enregistrement logiciel ou ouverture de LM Studio à produire. Les pistes ci-dessous restent l’historique ; les faits et limites du script corrigé prévalent.
> **16/11, ta demande** : la vidéo recule au **jeu. 3 déc., 18 h** (le 30 nov. va à [32 Go de VRAM](../deux-cartes-occasion/fiche.md)). [RAM, VRAM ou mémoire unifiée](../ram-vram-unifiee/fiche.md) ne la suit plus : elle passe au jeu. 31 déc. L'explication « pourquoi la RAM suffit ici » (un MoE ne lit qu'une partie de ses poids) doit donc tenir en quelques phrases dans cette vidéo.
>
> **15/11, ta demande : nouvel angle et nouvelle date.** Titre provisoire : *DeepSeek V4.1 Flash sans carte graphique : 64 Go de RAM suffisent ?* La vidéo sort le **lun. 30 nov., 18 h** (avancée du 18 janv.), parce que le modèle est déjà sorti et qu'en janvier il serait vieux. Elle sort juste avant [RAM, VRAM ou mémoire unifiée](../ram-vram-unifiee/fiche.md) (3 déc.), qui explique pourquoi la RAM suffit ici.
>
> **Inspiration** : Kai, [*Deepseek V4.1 Flash Runs With No GPU Just 64GB RAM*](https://www.youtube.com/watch?v=wiMs92u-dk0), 29 min 52 s, publiée le 13/11 : **60 154 vues en 2 jours, avec 74,4 K abonnés** (page YouTube, 15/11). Ce qu'il montre : llama-modchip, des correctifs sur llama.cpp, fait tenir DeepSeek V4 Flash 0731 (284B, environ 13B actifs par mot) dans un fichier de 56,93 Go à 1,71 bit par poids. Ça tourne à 8,66 tok/s sur un portable Ryzen 9 9955HX avec 64 Go de DDR5, sans carte graphique, et deux personnes extérieures l'ont reproduit. Le piège : d'après les notes de version, ce fichier est 60,8 % moins bon en perplexité (7,30 contre 4,54) que les poids d'origine. L'échelle d'AtomicChat va de 79 Go (21 % moins bon) à 144 Go (à 0,2 % près). Selon lui, passer de 64 à 96 Go de RAM coûte 460 $ de plus.
> - **Son angle (à ne pas reprendre)** : l'exploit technique, puis le démontage du mot « lossless ».
> - **Notre angle** : le prix en euros (et en FCFA) de la RAM qu'il faut à chaque palier de qualité (64, 96, 128 Go), contre l'abonnement, avec la méthode de Coût Claude. Le hook : « sans carte graphique », mais à quel prix pour la qualité ?
> - **À vérifier** : la version exacte (Kai parle de V4 Flash 0731, la fiche de V4.1 Flash) ; les notes de llama-modchip et l'échelle d'AtomicChat à la source ; les prix de la DDR5 en euros, relevés par toi. Pas de nom de chaîne dans la voix.
>
> Fiche du 10/11/2026, série « combien coûte [le modèle du moment] » de la réserve d'[`idees.md`](../../idees.md). Placée au jeu. 3 déc. au [radar du 10/11](../../etudes/radar.md) (30/40), puis **reculée au lun. 18 janv. 2027, 18 h, le 14/11** (provisoire, à confirmer au radar) : le 3 déc. va à [RAM, VRAM ou mémoire unifiée](../ram-vram-unifiee/fiche.md). Vidéo **calculée**, sur la méthode de [Combien coûte Claude en local ?](../cout-claude-local/fiche.md) (30 nov.).

**Signal** : Morgans Code, *DeepSeek V4.1 1017 Flash Is Opus-Level: What Does It Really Cost to Run?* (15,3 K, ×1,6, 19/10) ; RepoChad, *Run FULL DeepSeek v4.1 Flash on a 12GB GPU* (53,7 K, ×2,6, 02/11) (vidIQ, radar du 10/11).

| Champ | Détail |
|---|---|
| **Pilier** | IA chez moi |
| **Format** | Longue, 10-12 min. Calculée |
| **Trafic visé** | Recherche « DeepSeek en local » et suggestions sous Morgans Code et RepoChad |
| **Type de hook** | Résultat chiffré : le prix en euros (et en FCFA) du PC qui le fait tourner, contre l'abonnement |
| **Production** | 1 à 2 jours (la méthode est celle de Coût Claude) |

## ⚠️ Le modèle du moment peut changer

Depuis le 16/11, la vidéo sort le 3 déc. (le 30 nov. depuis le 15/11) : le modèle est fixé, c'est DeepSeek V4.1 Flash.

## Points à vérifier

1. La taille des fichiers sur Hugging Face, le jour du script.
2. Les mesures publiées (au moins deux concordantes), datées.
3. Les prix en euros TVA comprise ; pas d'électricité (décision du 23/10).
4. `sources.md` à créer.
