# Génération des assets — 16/11/2026

Outil : image_gen intégré, sans API/CLI externe. Référence de direction : les prompts ChatGPT 31/12 et les images de matériel existantes de Technovore.

Prompt exécuté (spécification complète de l’asset) :

> Petite ferme de minage d’occasion : châssis ouvert métallique, trois anciennes cartes noires à deux ventilateurs, câbles et alimentation, vue trois quarts, silhouette compacte. Illustration générique sans marque/modèle. Aplats, contours noirs épais, facettes anguleuses, métal gris/anthracite/cuivre. Fond #00FF00 sans ombre, aucun vert sur le matériel, aucun texte/logo/prix/nombre, carré 2048 × 2048, marge généreuse.

Source fond vert conservée dans `sources/`. Détourage reproductible avec `ressources/miniatures/portrait.py` ; versions h et j naturelles avec ombres de palette. Les fichiers `*-cadre.png`, lorsqu’ils existent, recadrent les marges transparentes pour la mise en page, sans modifier le sujet.
