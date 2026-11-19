# Génération des assets — 16/11/2026

Outil : image_gen intégré, sans API/CLI externe. Référence de direction : les prompts ChatGPT 31/12 et les images de matériel existantes de Technovore.

Prompt exécuté (spécification complète de l’asset) :

> Meme Roll Safe : homme noir cheveux courts, moustache fine, veste noire, index sur la tempe, sourire entendu, sourcil levé. Trois quarts, regard vers la gauche, tête/main entières. Peinture numérique à aplats, contours noirs, facettes anguleuses, peau marron naturelle. Fond #00FF00, aucun vert sur le sujet, aucun texte/logo. Carré 2048 × 2048, marge sur trois côtés, coupe seulement aux épaules.

Source fond vert conservée dans `sources/`. Détourage reproductible avec `ressources/miniatures/portrait.py` ; versions h et j naturelles avec ombres de palette. Les fichiers `*-cadre.png`, lorsqu’ils existent, recadrent les marges transparentes pour la mise en page, sans modifier le sujet.
