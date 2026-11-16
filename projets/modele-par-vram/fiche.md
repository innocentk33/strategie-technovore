# Quel modèle ta carte peut faire tourner ? De 4 à 16 Go de VRAM

> **Version de référence du 16/11/2026 : [script corrigé](script.md), [téléprompteur](teleprompteur.txt), [sources](sources.md) et [roast indépendant](grill-v1.md).** Format documentaire calculé : aucun nouvel essai, achat, enregistrement logiciel ou ouverture de LM Studio à produire. Les pistes ci-dessous restent l’historique ; les faits et limites du script corrigé prévalent.
> **Fiche du 14/11/2026, à ta demande** (ex-`petit-budget-ia/`, *L'IA locale sans grosse carte graphique*, renommée le 14/11). Les petits budgets sont désormais traités par paliers de VRAM. La thèse « la RAM plutôt que la carte » part dans [RAM, VRAM ou mémoire unifiée](../ram-vram-unifiee/fiche.md) (3 déc.), et le créneau du 7 déc. va au [multi-GPU](../multi-gpu/fiche.md). Placée au lun. 25 janv., puis au **lun. 18 janv. 2027, 18 h** (le 15/11, à la place de DeepSeek, avancé au 30 nov.), **provisoire, à confirmer au radar**. Vidéo **calculée**. Idée 27 de [`strategie.md`](../../strategie.md), non notée (ta demande du 14/11). Titre provisoire. Idée de départ (05/11) : le public sans carte de 16 Go (63 % en Afrique).

**Inspiration** : Codacus, [*What's the Best AI Model Your GPU Can Actually Run? 4GB to 16GB VRam*](https://www.youtube.com/watch?v=tek-IY9BRWc), 26 min 8 s, publiée le 02/11 : **56 676 vues en 12 jours, avec 46,8 K abonnés** (page YouTube, 14/11). Le [radar du 12/11](../../etudes/radar.md) notait déjà que l'angle 8 à 12 Go se renforçait (Kai : 60 K vues avec un modèle sur 12 Go ; 8 Go, c'est la VRAM d'un joueur sur quatre, d'après Steam en octobre).
- **Son angle (à ne pas reprendre)** : une montée de 4 à 16 Go avec 16 modèles MoE de moins de 40B, puis DeepSeek V4.1 Flash (763B) sur une seule carte. Les « fits » sont surtout calculés à partir des tailles de fichiers, et les essais mesurés sont signalés. Il donne une ligne de commande llama.cpp (`--moe-cache-mib`) qu'il n'a jamais lancée en entier. La vidéo est sponsorisée par Cline.
- **Notre angle** : **un palier, un modèle, un usage**. Pour 4, 6, 8, 12 et 16 Go, on donne le meilleur modèle qui tient, ce qu'il sait faire (discuter, résumer, coder) et la RAM qu'il demande, avec les cartes qu'on trouve vraiment en Afrique et d'occasion. Plus court que ses 26 minutes, et on part de la carte que tu as déjà.

| Champ | Détail |
|---|---|
| **Pilier** | IA chez moi |
| **Format** | Longue, 12-14 min. Calculée |
| **Trafic visé** | Recherche (« quel modèle ia pour ma carte graphique », « ia locale 8 go vram ») et suggestions sous Codacus, sous l'installation et sous 16 Go |
| **Type de hook** | Résultat chiffré : même une carte de [X] Go fait tourner [modèle] |
| **Production** | 1 à 2 jours |

## Strata (relevé sur GitHub le 05/11/2026, à revérifier avant le script)

- [Niko1221/Strata](https://github.com/Niko1221/Strata) : moteur d'inférence en C++, licence MIT, installation en un clic sur Windows et Linux, API OpenAI/Anthropic sur localhost. Créé le 24/09/2026, environ 40 K étoiles.
- L'astuce : les modèles « MoE » gardent leurs experts en **RAM** (voire sur le SSD) plutôt que dans la carte graphique. **Depuis le 14/11, l'explication détaillée va dans la vidéo du 3 déc.** Ici, une phrase et un renvoi.
- **Piège factuel** : ce n'est pas « sans matériel ». Il faut une carte RTX 20 à 50, une AMD récente ou un Mac M1+, **et beaucoup de RAM** : Qwen3.8-Flash-Next demande 37,6 à 54,8 Go (RAM + VRAM), Qwen3.6-35B-A3B 32 à 52 Go, et DeepSeek V4.1-Flash une carte de 12 Go, 46 Go de RAM au moins et ~257 Go de disque. Mesure publiée : environ 5 tokens/s en code sur RTX 5070 12 Go + 64 Go de RAM.
- La promesse honnête : « pas besoin d'une carte à 1 000 € », et non « ça tourne sur n'importe quel PC ».

## À faire

- [ ] Recherche par palier (4, 6, 8, 12, 16 Go) : un modèle, sa taille de fichier, la RAM demandée, une vitesse publiée. Puis double vérification.
- [ ] Les cartes de chaque palier, neuves et d'occasion, en euros et en FCFA.
- [ ] Mots-clés vidIQ en `fr` (ia locale petit budget, ia sans carte graphique, quel modèle pour ma carte graphique).
- [ ] Titres, puis les 15 premières secondes : le résultat d'abord.
- [ ] Ne pas recouper [16 Go suffisent](../claude-ou-mon-pc-1/fiche.md) (le palier 16 Go y renvoie) ni *RAM, VRAM ou mémoire unifiée* (31 déc. depuis le 16/11)
