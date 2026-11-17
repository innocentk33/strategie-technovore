# Critique indépendante — modele-par-vram

Relecture du 16 novembre 2026 par l’agent lot_modeles, qui n’a pas produit ces miniatures. Méthode coach-miniature-youtube : dix axes, observation des trois variantes à 168 px et moitié basse masquée. Sources lues : propositions.md, début du script corrigé du 16/11 et règles communes §2/§5. Aucun CTR ni résultat de test n’est présumé.

## Le test de la seconde

Un fichier .GGUF doit correspondre à une carte. On lit « TON MODÈLE RENTRE ? ». En i, la flèche va bien du fichier vers la carte et le repère 4 → 16 GO indique les paliers.

## Verdict par variante

**H — livrable.** Le fichier blanc à gauche et les cartes à droite racontent le choix du fichier sans benchmark. Les cartes remontées montrent leurs ventilateurs et évitent une grande zone vide. Le texte reste entier au test 50 %.

**I — livrable.** La scène la plus directe : un fichier, une flèche vers la carte, un repère de capacité. L’orientation corrigée enlève l’ambiguïté d’une carte qui produirait le fichier. Le petit libellé 4 → 16 GO est secondaire ; il n’annonce pas un gain de vitesse.

**J — livrable.** Même lecture que h avec une meilleure continuité de la palette de chaîne. Le blanc du fichier devient le premier objet de lecture puis l’œil suit le groupe de cartes, ce qui correspond à la question posée.

Le test à 50 % conserve toute l’accroche. Une grande part des objets disparaît sous le masque : ce test valide la phrase principale, pas la scène entière. Aucun détail critique n’est dans le coin de la durée. Les fichiers PNG contrôlés mesurent 3840 × 2160. Les PSD sont présents mais leur reconstruction n’a pas été revue dans cet audit visuel indépendant.

## Tableau de bord

| Axe | h | i | j |
|---|---|---|---|
| Lisibilité | 🟢 fichier + cartes | 🟢 relation très simple | 🟢 fichier + cartes |
| Composition | 🟢 côtés équilibrés | 🟢 flèche bien orientée | 🟢 cartes remontées |
| Contraste | 🟢 fichier blanc détaché | 🟢 objets nets | 🟢 contours blancs efficaces |
| Texte | 🟢 question courte | 🟢 question en haut | 🟢 question courte |
| Émotion / curiosité | 🟢 contrainte personnelle | 🟢 peut-il tenir ? | 🟢 même enjeu |
| Types | 🟢 objet + question | 🟢 schéma + question | 🟢 objet + question |
| Duo titre-image | 🟢 fichier plutôt que liste | 🟢 gamme mémoire illustrée | 🟢 même complément |
| Différenciation | 🟠 trois cartes déjà vues | 🟢 relation fichier→GPU | 🟠 actif budget réutilisé |
| Identité | 🟢 h conforme | 🟢 i conforme | 🟢 j conforme |
| Promesse / technique | 🟢 pas de modèle garanti | 🟢 4–16 Go est une gamme | 🟢 aucun résultat inventé |

## Corrections et éléments à garder

Aucune correction bloquante sur la version finale regardée. Garder la flèche fichier→GPU de i. Lors d’une prochaine révision, différencier encore h/j de carte-par-budget en réduisant le groupe de trois cartes à une seule grande carte face au fichier ; ce serait un autre concept, pas une retouche nécessaire pour cette livraison. Ne pas écrire une taille de fichier comme si elle était l’occupation totale.

## Comparaison

Hypothèse de clic : i, puis j, puis h. i exprime le lien fichier-mémoire avec le moins d’éléments ; h/j maintiennent l’aspect matériel illustré de la série. Ce classement est une hypothèse de lecture ; le test YouTube h/i/j devra conserver titre et publication constants. La présence du sujet dans le titre complète les accroches sans promettre un vainqueur général.

## Périmètre exact regardé

Planche : apercu/test-50-et-168px-kai.png, les trois rendus et la moitié basse masquée. Empreintes SHA-256 abrégées des PNG contrôlés : h: 9bfbd7a6d3a33d25 ; i: d56efa7ac2344034 ; j: a3cbed5fb03063c2. Relecture sur les dernières images confirmées figées par leur auteur ; aucun fichier de source n’a été modifié par le relecteur.
