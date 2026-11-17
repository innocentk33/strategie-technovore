# Les 11 vidéos sans miniature — 16 novembre 2026

Demande : réaliser trois variantes par vidéo, avec les sources du projet et une critique indépendante de chaque image. Base d'illustration : [prompts-chatgpt-31-12.md](../prompts-chatgpt-31-12.md). Les scripts corrigés du 16 novembre priment sur les anciennes pistes des fiches.

## Production

1. Lire les scripts, retenir une question courte et une scène qui tiennent leur promesse.
2. Appliquer la charte `miniature-kai` : h, palette Kai et illustration ; i, Technovore sans visage ; j, Technovore et illustration. Pour les vidéos de matériel, l'objet remplace le visage. Texte à gauche ou en haut, Archivo Black, fond Technovore uni `#141e27`, accent `#07c095`, copie décalée blanche.
3. Réutiliser les assets pertinents et générer les illustrations manquantes à partir des prompts de référence. Conserver les prompts et leur provenance dans chaque projet.
4. Exporter les PNG 3840 × 2160, les maquettes HTML reproductibles et les PSD à textes modifiables avec PhotoCraft CLI.
5. Faire une revue croisée des rendus : lisibilité à 168 px, moitié supérieure, chevauchements, durée YouTube, promesse du script et style. Corriger, puis revoir les variantes modifiées.
6. Rassembler les 33 images dans une galerie locale et vérifier leur détection par la régie.

## Répartition

Tous les agents sont GPT‑6.1 Sol, effort élevé. Aucun ne valide son propre lot.

| Lot | Projets | Relecteur indépendant prévu |
|---|---|---|
| Matériel | carte-par-budget, ram-vram-unifiee, modele-par-vram, cartes-minage | Agent modèles |
| Modèles | qwen-27b-8go, cout-deepseek-flash, petits-modeles-experts | Agent usages |
| Usages | claude-code-gratuit, ia-locale-privee, jeu-video-ia-locale, choisir-moteur | Agent matériel |

Les h/j partagent la composition pour comparer les palettes. Le test i/j compare une composition sans portrait à une composition avec portrait ; il ne mesure donc pas exclusivement l'effet du visage. Pour le matériel, i compare la scène schématique à l'illustration.

## Livrables

Dans chaque `projets/<nom>/miniature/` : `rendus/`, `photocraft/`, `sources/`, `propositions/`, `propositions.md` et `apercu/`. La critique indépendante est consignée dans ce même dossier. Aucun test YouTube n'est lancé automatiquement.

## Réalisé et vérifié le 16/11

Les 33 PNG 3840 × 2160 et 33 PSD sont produits. Les 33 PSD ont été ouverts avec PhotoCraft CLI : dimensions correctes, au moins trois calques de texte modifiables, aucune alerte. Les onze critiques indépendantes couvrent chaque h/i/j ; RAM i et les douze variantes usages ont été revues après correction. Les onze projets ont une image détectée dans l’API de la régie.

[Livraison et accès aux fichiers](LIVRAISON.md) · [Contrôle des PSD et empreintes finales](verification-psd.json)

## Correction logos du 16/11

Les douze variantes Qwen, DeepSeek, Claude Code et trois moteurs ont été corrigées avec les véritables marques. Le chevauchement de «3 OUTILS» et des tuiles est supprimé. Relecture indépendante GPT‑6.1 Sol, effort élevé, validée sur chaque variante ; rapports `critique-logos.md` dans les quatre projets, empreintes finales consignées. Les douze PSD modifiés ont été rouverts et vérifiés. Bibliothèque de logos et règle de reconnaissance ajoutées aux ressources et consignes du projet.
