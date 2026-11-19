> **Mise à jour du 20/11/2026 :** le cadrage inférieur h/j a été corrigé et fait l’objet de la contre-revue ci-dessous. Les revues antérieures conservent les empreintes de leurs versions historiques ; voir [rapport du bord inférieur](apercu/audit-bord-2026-11-20/rapport.md) pour les fichiers actuels et la nouvelle contre-revue.

> **Validation antérieure à la correction des logos.** Pour les derniers PNG, voir [critique-logos.md](critique-logos.md), avec vérification indépendante et empreintes finales.

## Revalidation ciblée du 20/11/2026 — bord inférieur

**H : validée après correction. J : validée après correction. I : inchangée.** Relecture indépendante par lot_modeles, distinct de lot_materiel qui a produit la retouche. Les compositions finales h/j ont été vues en entier à 640 px puis sur une bande inférieure agrandie. Le portrait passe de top:10 à top:30 px : le buste et ses ombres sortent du cadre. Aucune barre horizontale de contour blanc, rouge ou menthe n’est visible en bas. Le regard vers le texte, la marge avec les objets et la reconnaissance des vrais logos sont conservés ; aucune collision nouvelle.

Cette signature porte sur la correction de cadrage et les PNG finaux. Les revues de concept et de logos précédentes restent consignées plus bas ; leurs anciennes empreintes sont historiques. La variante i n’a pas été retouchée. Les PSD et leur contrôle technique sont traités séparément par le producteur.

| Variante finale | Dimensions | SHA-256 complet du PNG |
|---|---|---|
| h | 3840 × 2160 | `7de1fe57cca38dc801d48e40e4f2180a9b860047e15d937152ba99baf8fb7b9c` |
| i | 3840 × 2160 | `7094e7bc57516c5e8f06f9e05feea1de7c5a79b5c35f518d0fdb287a8671e02a` |
| j | 3840 × 2160 | `1cee9f7434d887ac945140fae3dbc42491a946898a2aa46c1e70816d1d91a8ef` |

---

# Critique indépendante — claude-code-gratuit

16/11/2026 — relecteur distinct de l’auteur des maquettes. Grille du skill coach-miniature-youtube appliquée après lecture du script corrigé et de propositions.md. **Validation finale : les trois variantes h/i/j sont livrables après corrections et seconde visualisation indépendante.**

## Revalidation finale du 16/11/2026

**H : validée. I : validée. J : validée. Aucun point bloquant restant.**

Les trois scènes sont remontées et le libellé CLAUDE CODE agrandi. En h/j, le libellé reste petit mais il est désormais récupérable à 168 px ; en i, il est net. Le test 50 % conserve CLAUDE CODE au-dessus du masque. Pas de collision entre la question, l’écran et le visage.

Seconde visualisation effective : planche 168 px + test 50 %, comparaison 640 px, puis réexécution du script coach sur les PNG finaux. Les fichiers `apercu/coach-independant/` correspondent à cette version finale. La revue indépendante porte sur les images ; le contrôle technique des PSD est effectué par l’agent producteur.

Empreintes SHA-256 complètes des images finales approuvées :

- `h-kai.png` : `86a5a0b823cd1af23a38ea3858f283d7ff4e1462dcdb6f7fced1298b35412092`
- `i-kai.png` : `8214cde4b834b3d088bc40edbafe614b33e5ee54a85826deb54ad369a9cb199d`
- `j-kai.png` : `0856361d56e76e8268f642d0f90c478670d17830d701b88e9492af9fa77fa6d4`

Les observations, axes et corrections ci-dessous consignent la première passe. La présente validation finale les remplace pour la composition et les libellés corrigés ; les réserves de différenciation sans recherche concurrentielle et le classement hypothétique restent valables.

## Test de la seconde

Une interface de code envoie une demande à une autre IA, et Morpheus doute que le résultat soit équivalent.

## Verdict

Le concept est fidèle à la distinction interface/modèle du script. h et j portent une vraie interrogation ; i fait mieux comprendre le chemin technique grâce à l’écran agrandi. Le principal défaut est l’identification : à 168 px, le petit libellé CLAUDE CODE des versions à portrait disparaît, et le test des 50 % ne garde presque aucun indice de code.

Visualisation effective des trois variantes dans `apercu/comparaison-640px.png`, `apercu/test-50-et-168px-kai.png`, puis simulation d’accueil sombre et planches (gris, flou, durée) générées dans `apercu/coach-independant/`. Les vignettes voisines de la simulation sont fictives : elles testent l’interface, pas la concurrence réelle.

## Dix axes de la première passe, h / i / j

| Axe | h | i | j | Observation |
|---|---|---|---|---|
| Lisibilité | 🟠 | 🟢 | 🟠 | Question nette ; CLAUDE CODE trop petit dans h/j. |
| Composition | 🟠 | 🟠 | 🟠 | Scène sous la mi-hauteur : le sujet disparaît au test 50 %. |
| Contraste | 🟢 | 🟢 | 🟢 | Blancs et silhouettes détachés en gris et sur accueil sombre. |
| Texte | 🟢 | 🟢 | 🟢 | Quatre mots, une question ; aucun gain fictif. |
| Émotion | 🟢 | 🟠 | 🟢 | Scepticisme de Morpheus lisible, i plus pédagogique. |
| Types | 🟢 | 🟢 | 🟢 | Question + comparaison de composants ; réaction illustrée en h/j. |
| Titre-image | 🟢 | 🟢 | 🟢 | La question d’équivalence complète la connexion décrite au titre. |
| Différenciation | 🟠 | 🟠 | 🟠 | Le terminal/chip est générique ; pas de recherche concurrentielle nouvelle. |
| Identité | 🟢 | 🟢 | 🟢 | Archivo Black, palettes et ombres de la charte. |
| Promesse/technique | 🟢 | 🟢 | 🟢 | 3840×2160, illustration nette ; l’équivalence reste une question. |

## Corrections ciblées de la première passe (appliquées)

### Priorité 1 — faire reconnaître Claude Code en petit

Dans l’écran de h/j, augmente le libellé de 25 à environ 44–48 px à 1×, ou compose CLAUDE et CODE sur deux lignes grasses. Vérifie le même changement dans i : pas de dépassement du cadre.

### Priorité 2 — conserver un indice de code au test 50 %

Remonte la scène d’environ 80–100 px dans h/j et 55 px dans i, puis ajuste pour ne pas toucher le titre. Il faut qu’une partie du terminal et son libellé restent au-dessus de y=360, sans déplacer le visage vers le texte.

### Priorité 3 — conserver la distinction interface/modèle

Garde la flèche et la puce comme deux éléments distincts. Évite une pastille égal ou le mot « IDENTIQUE » : le script ne démontre pas cette équivalence.

## À garder et hypothèse de test

Le regard vers la gauche, le fond calme et le scepticisme de Morpheus. Aucun besoin d’ajouter des prix ou un débit.

i > j > h pour la compréhension du sujet ; j est le challenger émotionnel. Ce classement est une hypothèse de conception, pas un résultat de CTR.

Tester h/i/j à titre et fenêtre de publication constants dans « Tester et comparer ». Les variantes i changent aussi la composition et les objets : i contre j mesure une alternative sans visage, pas une expérience où le visage serait la seule variable.

## Trace des images vues

Fichiers PNG 3840 × 2160 inspectés le 16/11. Empreintes de la version initiale :

- `h-kai.png` : `6e06dc1a3440513df810d2d82c0ce7e839d3e87376cfc4f0a18556c2c159d7f5`
- `i-kai.png` : `dacfdfda6b54d0f9f229c63e968dbce7300f2278fb9c2f15f8d1d8b9a4c7dc98`
- `j-kai.png` : `297c43076f8d58a1eaeee71e08d91f9461415d8b5ba28a019c8a952bb3af4fc5`

Les empreintes ci-dessus appartiennent à la première passe ; celles de la revalidation finale font foi. Les portraits sont des memes illustrés explicitement autorisés par l’auteur ; la présence réelle des acteurs dans la vidéo n’est pas suggérée.
