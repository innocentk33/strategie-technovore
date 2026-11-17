# Génération des assets — 16/11/2026

Outil : image_gen intégré, sans API/CLI externe. Référence de direction : les prompts ChatGPT 31/12 et les images de matériel existantes de Technovore.

Prompt exécuté (spécification complète de l’asset) :

> Réemploi local du trio généré pour carte-par-budget, même source et même traitement de détourage ; aucune nouvelle image n’était nécessaire. Prompt du trio : cartes à un, deux et trois ventilateurs, sans marque, en escalier ; aplats, contours noirs, facettes anguleuses ; métal gris/noir, touches rouge/violet ; fond #00FF00 sans ombre, aucun vert sur l’objet, aucun texte/prix/logo ; carré 2048 × 2048, marge généreuse.

Source fond vert conservée dans `sources/`. Détourage reproductible avec `ressources/miniatures/portrait.py` ; versions h et j naturelles avec ombres de palette. Les fichiers `*-cadre.png`, lorsqu’ils existent, recadrent les marges transparentes pour la mise en page, sans modifier le sujet.
