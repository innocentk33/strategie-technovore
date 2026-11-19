> **Mise à jour du 20/11/2026 :** le cadrage inférieur h/j a été corrigé et fait l’objet de la contre-revue ci-dessous. Les revues antérieures conservent les empreintes de leurs versions historiques ; voir [rapport du bord inférieur](apercu/audit-bord-2026-11-20/rapport.md) pour les fichiers actuels et la nouvelle contre-revue.

# Critique indépendante des logos — choisir-moteur

## Revalidation ciblée du 20/11/2026 — bord inférieur

**H : validée après correction. J : validée après correction. I : inchangée.** Relecture indépendante par lot_modeles, distinct de lot_materiel qui a produit la retouche. Les compositions finales h/j ont été vues en entier à 640 px puis sur une bande inférieure agrandie. Le portrait passe de top:10 à top:30 px : le buste et ses ombres sortent du cadre. Aucune barre horizontale de contour blanc, rouge ou menthe n’est visible en bas. Le regard vers le texte, la marge avec les objets et la reconnaissance des vrais logos sont conservés ; aucune collision nouvelle.

Cette signature porte sur la correction de cadrage et les PNG finaux. Les revues de concept et de logos précédentes restent consignées plus bas ; leurs anciennes empreintes sont historiques. La variante i n’a pas été retouchée. Les PSD et leur contrôle technique sont traités séparément par le producteur.

| Variante finale | Dimensions | SHA-256 complet du PNG |
|---|---|---|
| h | 3840 × 2160 | `6b3e0c9ad13fe91d527d2f0ea2565c0ebecf29e768bebef8c8d23cdae084c79a` |
| i | 3840 × 2160 | `9330bd956aa01cf3add132f07f3942ab53d012416f3263d3e9ff85c0cee4cc91` |
| j | 3840 × 2160 | `60890b751fe1c3da94ed32f3ca2ed233c6e9fcf28b2752af0a125c0e631fce22` |

---

16/11/2026. Relecture par l’agent lot_materiel, distinct du producteur. Cette passe porte sur les PNG corrigés après la demande de logos authentiques ; **les validations dans critique-independante.md sont antérieures à cette correction**. Le présent rapport et ses empreintes identifient les dernières images relues.

**Verdict : Les trois variantes sont validées. Aucun point bloquant restant.**

## Sources contrôlées

Les trois SVG locaux ont été comparés **octet par octet** aux téléchargements de leurs sources primaires :

- [LM Studio, kit officiel](https://lmstudio.ai/brand), [icône couleur originale](https://lmstudio.ai/assets/marketing/brand/download/logos/lm-studio-icon-color.svg) : SHA-256 `18950f44a1ba87eb6de782ed6c7691de21c1bfebf0000c7c896240aed104ffef`.
- [Ollama, dépôt officiel](https://github.com/ollama/ollama/blob/main/docs/ollama-logo.svg) : `397a6ee071cce1496edd8a86dd1c91ce005712ec161690e411b3dc7f151181f5`.
- [llama.cpp, dépôt officiel de marque](https://github.com/ggml-org/llama-brand), icône `logo/svg/icon/icon-light.svg` : `ce48c0f8e98aa4099b6f04a65b76bc32bc00c8fa39d58f15da9b73905f1918f1`.

Les fichiers consommés sont exactement ces originaux. Leurs proportions et leurs couleurs sont conservées ; les tuiles sont désormais droites. Les noms sont des légendes séparées et ne prétendent pas refaire les signatures de marque.

## Observation effective, h / i / j

**h — validée.** LM Studio possède son icône officielle à lignes arrondies ; Ollama sa silhouette complète ; llama.cpp son emblème officiel noir. La version ne recourt plus aux faux monogrammes LL, tête simplifiée ou symbole de code générique. Les trois se reconnaissent en petit, même si les noms restent secondaires.

**i — validée.** Les logos sont plus grands, nets et identifiables à 168 px. Le titre « TON IA 3 OUTILS » est séparé des cartes par un espace franc. Les trois tuiles sont de même rang et ne font pas croire à un podium de vitesse.

**j — validée.** La menthe ne recolore aucun logo. « 3 OUTILS » ne chevauche plus les tuiles : le groupe commence à y=360 et le titre a été limité à 115 px. Cet écart est visible en grand et en petit, contrairement à la version précédente signalée par l’auteur.

La question de choix reste tenue par le script : trois moteurs selon l’usage, aucun vainqueur universel inventé. Le test des 50 % conserve l’accroche explicite « TON IA / 3 OUTILS » ; les objets peuvent être partiellement cachés sans faire perdre le sujet.

Les trois PNG ont été vus à 168 px puis à 640 px, avec observation de la place du titre, des tuiles et du coin durée. Les maquettes ont été lues pour confirmer le chemin de l’asset, ses dimensions et l’absence de déformation. Les scripts corrigés du 16/11 ont été consultés pour contrôler la promesse. Cette revue ne prédit aucun CTR et ne prétend pas à une revue de marché.

## Empreintes des PNG approuvés

Tous les fichiers contrôlés mesurent 3840 × 2160.

| Variante | SHA-256 final |
|---|---|
| h | `4d0afffb992388cfc4101d855b676ac51383a9e827f213bd996a77a6cdea88f4` |
| i | `9330bd956aa01cf3add132f07f3942ab53d012416f3263d3e9ff85c0cee4cc91` |
| j | `82d94b2701bb458f71651ebe040a13e408979f6b58c373efacf0364719f5f98f` |

Les PSD suivent le contrôle du producteur ; ce verdict indépendant valide les images ci-dessus. Un nouveau changement de logo, taille ou cadrage appelle une nouvelle vérification de ses PNG.
