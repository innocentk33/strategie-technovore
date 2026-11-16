# Deux cartes graphiques pour l'IA : à savoir avant d'acheter la deuxième

> **Version de référence du 16/11/2026 : [script corrigé](script.md), [téléprompteur](teleprompteur.txt), [sources](sources.md) et [roast indépendant](grill-v1.md).** Format documentaire calculé : aucun nouvel essai, achat, enregistrement logiciel ou ouverture de LM Studio à produire. Les pistes ci-dessous restent l’historique ; les faits et limites du script corrigé prévalent.
> Fiche du 14/11/2026, à ta demande. Placée au **lun. 7 déc., 18 h**, à la place de « petits budgets », qui devient [Quel modèle ta carte peut faire tourner ?](../modele-par-vram/fiche.md) (25 janv., provisoire). Elle sort deux semaines après [32 Go de VRAM au moins cher](../deux-cartes-occasion/fiche.md) (23 nov.), dont elle est la suite. Vidéo **calculée**. Idée 26 de [`strategie.md`](../../strategie.md), non notée (ta demande du 14/11). Titre provisoire.

**Inspiration** : Weights & Wonders, [*Watch This Before Building a Multi-GPU Local AI Setup!*](https://www.youtube.com/watch?v=sF_P1OICoEw), 15 min 23 s, publiée le 11/11 (le 12/11, heure de Paris) : **32 914 vues en 3 jours, avec 1,74 K abonnés** (page YouTube, 14/11). Le [radar du 12/11](../../etudes/radar.md) la notait déjà à 1 562 vues/h. C'est la même chaîne que notre inspiration pour Qwen 4.
- **Son angle (à ne pas reprendre)** : six questions de ses commentaires, avec ses tests. En layer split (le mode par défaut de llama.cpp), la deuxième carte n'accélère pas : elle donne de la place. Sur deux RX 7900 XTX, il mesure 36 tok/s avec une carte et 34 avec deux. Le tensor split, lui, va environ 1,3 fois plus vite, à condition que les deux cartes soient sur des ports rapides. Il traite aussi la carte lente à côté d'une rapide, NVIDIA avec AMD, et l'idée que 2 × 16 Go ne font jamais 32 Go.
- **Notre angle** : la checklist **avant d'acheter** la deuxième carte, en euros, sur un vrai PC de joueur : la carte mère (16 lignes PCIe sur le premier port, souvent 4 sur le second), l'alimentation, le boîtier, et ce que tu gagnes vraiment (de la place, pas de la vitesse). On part de ta question du 23 nov. (« et si j'ajoutais une carte ? ») au lieu de reprendre ses six questions.

| Champ | Détail |
|---|---|
| **Pilier** | IA chez moi |
| **Format** | Longue, 10-12 min. Calculée (mesures publiées, doc de llama.cpp, manuels de cartes mères) |
| **Trafic visé** | Suggestions sous Weights & Wonders et sous notre vidéo 32 Go ; recherche (« deux cartes graphiques ia », « multi gpu llama.cpp ») |
| **Type de hook** | Résultat contre-intuitif : deux cartes, et ça va **moins** vite (36 contre 34 tok/s, mesure publiée) |
| **Production** | 1 à 2 jours |

## Pistes (à sourcer)

- Layer split contre tensor split : ce que fait chaque mode, et où on le règle (llama.cpp, Ollama, LM Studio, Strata).
- Pourquoi 2 × 16 Go ne font pas 32 Go utilisables : le cache KV et les copies sur chaque carte.
- La carte mère : comment lire le manuel (x16/x4 ou x8/x8) ; quelques cartes mères vendues en France.
- Deux cartes différentes (une lente et une rapide, NVIDIA et AMD) : est-ce que ça marche ?
- L'alimentation et le boîtier : le coût caché de la deuxième carte.

## Points à vérifier

1. Les mesures publiées sont celles de sa description : LithiumDevourer, xenodeve et jeffbolznv sur GitHub, le blog de Jeff Geerling, infermeld. Remonte à chaque source et date-la. Ne cite que ce qui est mesuré.
2. Pas de nom de chaîne dans la voix ([sources anonymes](../../CLAUDE.md) : « un créateur a mesuré… ») ; les noms vont dans `sources.md`.
3. Ne pas refaire la vidéo des 32 Go (30 nov. depuis le 16/11) : on renvoie à ses prix et à ses routes vers 32 Go.
4. `sources.md` à créer.
