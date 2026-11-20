# Carte graphique pour l’IA locale : combien coûte la mémoire dont tu as besoin ?

> **20/11/2026** — Le créneau du 26 novembre revient au [setup Black Friday pour l’IA locale](../setup-black-friday-ia-locale/fiche.md). Le guide sur la carte seule est prévu le **jeudi 7 janvier 2027 à 18 h**, après la vidéo sur la RAM et la VRAM. Revérifier les offres et dater les prix avant la voix.

> **Angle du 18/11/2026 (ta demande)** : « tu t'apprêtes à mettre 600 € dans une carte graphique au Black Friday pour l'IA locale ». Choisir comme pour le jeu ne marche pas : la mémoire d'abord (ce qui rentre), puis le débit mémoire (la vitesse d'écriture). V3 réécrite et grillée ([grill-v3.md](grill-v3.md)), recherches dans `recherche/`. Les paliers 300/500/800 € ci-dessous sont l'historique.
> **Titres, ton choix du 19/11/2026** : test A/B entre A, *Carte graphique pour l’IA locale : combien coûte la mémoire dont tu as besoin ?* (titre actuel, gardé dans le README et le calendrier), et B, *N'achète pas une carte graphique pour l'IA locale avant d'avoir vu cette vidéo*.
> **Version de référence du 16/11/2026 : [script corrigé](script.md), [téléprompteur](teleprompteur.txt), [sources](sources.md) et [roast indépendant](grill-v1.md).** Format documentaire calculé : aucun nouvel essai, achat, enregistrement logiciel ou ouverture de LM Studio à produire. Les pistes ci-dessous restent l’historique ; les faits et limites du script corrigé prévalent.
> Fiche du 14/11/2026, à ta demande (« en prévision du Black Friday »). Placée au **jeu. 26 nov., 18 h**, la veille du Black Friday (ven. 27 nov.), à la place d'[IA locale privée](../ia-locale-privee/fiche.md), qui recule au lun. 11 janv. Vidéo **calculée**. Idée 28 de [`strategie.md`](../../strategie.md), non notée (ta demande du 14/11). Titre provisoire.

**Inspiration** : Locally, [*The Best Local AI GPU For Every Budget (November 2026)*](https://www.youtube.com/watch?v=-ImyaGElyfk), 12 min 21 s, publiée le 14/11 : 1 570 vues quelques heures après sa sortie, avec 4,5 K abonnés (page YouTube, 14/11). **Signal pas encore prouvé** : à remesurer au radar du 16/11.
- **Son angle (à ne pas reprendre)** : un classement par paliers de prix en dollars, avec des liens affiliés Amazon US. Sa thèse : « à chaque budget, la mémoire bat la vitesse de jeu ». Par exemple, la RTX 5070 (12 Go, 900 $) perd contre la RTX 5060 Ti (16 Go, 100 $ de moins, 111,5 tok/s sur gpt-oss-20b).
- **Notre angle** : les mêmes paliers, mais **en euros, TVA comprise, aux prix du Black Friday en France**, avec un encart Afrique (ce qu'on trouve à Abidjan, Kinshasa et Douala, et l'occasion). Pour chaque palier, la question est la même : « quel modèle tient dedans ? », et on renvoie aux vidéos qui le prouvent (16 Go, Strata, 32 Go).

| Champ | Détail |
|---|---|
| **Pilier** | IA chez moi |
| **Format** | Longue, 10-12 min. Calculée |
| **Trafic visé** | Recherche saisonnière (« meilleure carte graphique ia », « black friday carte graphique ») et suggestions sous Locally et sous notre vidéo Qwen 4 |
| **Type de hook** | Résultat chiffré : la carte la plus chère du palier [X] fait tourner un modèle plus petit que celle à [Y] € |
| **Production** | 1 à 2 jours |

## À ne pas confondre avec

- [Qwen 4 : quelle carte acheter (ou pas)](../qwen-4-cartes/fiche.md) (publiée le 12/11) : là, on choisissait une carte pour **un** modèle. Ici, on donne la meilleure carte **par budget**, quel que soit le modèle.
- [32 Go de VRAM au moins cher](../deux-cartes-occasion/fiche.md) (30 novembre, avant ce guide) : c'est le palier du haut. Ici, on le cite en une phrase et on y renvoie.
- [Le cadeau IA locale](../cadeau-ia-locale/fiche.md) (24 déc.) : c'est une machine entière, en paliers de budget. Il reprendra ces prix, mis à jour.

## Pistes (à sourcer)

- Les paliers : environ 300 €, 500 €, 800 € et plus de 1 000 €, en euros. Pour chacun : la carte, sa VRAM, le plus gros modèle qui tient, et une vitesse publiée.
- Le piège du palier : une carte plus chère avec moins de VRAM (12 Go contre 16 Go).
- L'occasion (RTX 3060 12 Go, RTX 3090 24 Go) : la garantie, et ce que ça demande au PC (alimentation).
- Le Black Friday : relève les prix des cartes **avant** (le 20/11 environ) et **pendant** (26/11). Ces relevés servent aussi à la vidéo [Le Black Friday a-t-il fait baisser les prix ?](../prix-apres-black-friday/fiche.md) (17 déc.).

## Points à vérifier

1. Les prix en euros, datés et relevés par toi : [PRIX À RELEVER]. Aucun prix en dollars converti sans le dire.
2. Les vitesses : au moins une mesure publiée par carte, avec le modèle et la quantization.
3. **Délai** : la règle veut qu'on écrive quatre créneaux à l'avance, et cette vidéo n'en a que trois (fiche le 14/11, sortie le 26/11). À écrire juste après Strata.
4. `sources.md` à créer.
