# Miniatures des six vidéos précédentes — 19 novembre 2026

Demande : adapter Qwen 4, 16 Go de VRAM, l’installation de LM Studio, Uber, OpenCode piraté et ArtCraft au style des dernières miniatures.

## Livrables et charte

Trois variantes par vidéo : h (palette Kai et illustration), i (Technovore sans visage), j (Technovore avec illustration). Police Archivo Black, texte à gauche ou en haut, un segment accentué et sa copie décalée. Fond Technovore uni `#141e27`, accent `#07c095`, copie blanche. Logos authentiques, proportions conservées, espace net entre titre et objets.

18 PNG 3840 × 2160, 18 PSD à textes modifiables, sources HTML/SVG et images, prompts/provenance, scripts de reproduction, planches 168 px et moitié basse masquée. Les anciens fichiers sont conservés. Aucun changement de miniature publiée sur YouTube n’est effectué.

## Méthode

1. Lire les scripts et les sources historiques : la miniature promet le contenu de la vidéo existante, sans actualiser artificiellement les prix ou les performances.
2. Adapter une scène distinctive par vidéo à la charte h/i/j ; réutiliser les véritables logos et générer les illustrations manquantes selon la base de prompts du projet.
3. Rendre et inspecter les PNG ; exporter les PSD via PhotoCraft CLI et vérifier leurs textes modifiables.
4. Faire critiquer chaque variante par un autre agent GPT‑6.1 Sol, effort élevé ; corriger les problèmes et revoir les rendus modifiés.
5. Rassembler les variantes dans la galerie locale et vérifier leur détection dans la régie.

## Répartition et indépendance

| Producteur | Vidéos | Relecteur |
|---|---|---|
| lot_materiel | Qwen 4, 16 Go de VRAM | lot_usages |
| lot_modeles | OpenCode, ArtCraft | lot_materiel |
| lot_usages | Uber, installer LM Studio | lot_modeles |

Les nouvelles maquettes se trouvent dans chaque `miniature/propositions/miniature-kai.html`, les briefs dans `propositions-kai.md` et les revues dans `critique-kai.md`. Les scripts `rendre-kai.sh` complètent les anciens scripts au lieu de les remplacer.

Le test h/j compare principalement les palettes. i change aussi la composition : sa comparaison avec j ne mesure pas exclusivement l’effet d’un visage. Les classements des agents restent des hypothèses à confronter au public.

## État final

Les cinq étapes sont terminées. Les 18 variantes ont été critiquées par les relecteurs indépendants prévus ci-dessus. OpenCode a reçu une correction de formulation, réexportée et revalidée. Les 18 PNG et PSD mesurent 3840 × 2160 ; chaque PSD contient des calques de texte Archivo Black et ne présente aucun avertissement PhotoCraft. Les empreintes des PNG concordent avec celles des critiques, les 84 liens locaux de la galerie aboutissent et la régie détecte les 18 variantes. Voir [LIVRAISON.md](LIVRAISON.md).
