# Je teste le meilleur modèle possible avec Strata sur ma 5080

> Planning : [`calendrier.md`](../../calendrier.md), **lun. 16 nov. 2026 à 18 h**. Ta décision du 05/11 : la suite de [« 16 Go suffisent »](../claude-ou-mon-pc-1/fiche.md) (9 nov.), et une exception au « tout calculé » : celle-ci est **filmée chez toi**.

| Champ | Détail |
|---|---|
| **Pilier** | IA chez moi (testé) |
| **Modèle d'inspiration** | [Red Stapler, I ran Qwen3.8 27B on single 8GB Card!](https://www.youtube.com/watch?v=ye50BbXEczo) : le résultat d'abord, puis comment |
| **Structure** | 1. Les résultats (le meilleur modèle qui tourne avec Strata sur ta 5080, 32 Go de RAM). 2. Comment y arriver : le bon fichier, le harnais (Claude Code / OpenCode branché sur `strata connect`), les réglages. |
| **Les 15 premières secondes** | Le résultat filmé : le modèle qui code en direct sur ta machine, avec la vitesse à l'écran |

## Ce qu'on sait déjà ([sources du 9 nov.](../claude-ou-mon-pc-1/sources.md))

- Avec 32 Go de RAM, seul le **Coder** de Strata passe, à ras (≈ 33 Go demandés pour ≈ 33,5 Go visibles sous Windows) : navigateur fermé pendant l'essai.
- Mesure publiée sur une machine proche (5070 Ti, 9700X, 32 Go) : ~70 tok/s, sans contrôle de justesse. Un échec documenté du Coder sur une tâche Claude Code (Samayas) : prévoir une tâche simple **et** une tâche dure.
- Strata est instable sur 5080 (régressions de vitesse, erreur « non-finite logits » avec IQ3_S / IQ3_XXS) : note la version exacte du moteur.

## À faire

- [ ] Choisir 2 ou 3 tâches identiques à donner à Claude et au modèle local
- [ ] Filmer : installation, vitesse (tok/s affichés par Strata), résultats
- [ ] Noter version de Strata, fichier, contexte, RAM utilisée
- [ ] Script après les essais (les résultats d'abord)
