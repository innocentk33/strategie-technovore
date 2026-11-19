# Six vidéos précédentes — miniatures du 19 novembre 2026

[Ouvrir la galerie des 18 variantes](index.html) · [Planche 1](planche-1.jpg) · [Planche 2](planche-2.jpg) · [Test à 168 px](planche-168px.png)

| Vidéo | Accroche |
|---|---|
| Qwen 4 : quelle carte graphique acheter (ou pas) ? | ACHETER / TROP TÔT ? |
| 16 Go de VRAM suffisent (si tu prends le bon fichier) | TON FICHIER / DÉBORDE ? |
| Pourquoi avoir ta propre IA, et comment l’installer (LM Studio) | TON IA / HORS LIGNE |
| Uber | VRAIMENT / LÀ ? |
| OpenCode piraté | TES CLÉS / VOLÉES ? |
| ArtCraft | FINI / L’ABO ? |

Chaque vidéo possède trois propositions : **h**, palette Kai avec portrait ; **i**, palette Technovore sans portrait ; **j**, palette Technovore avec portrait. Les logos authentiques restent séparés des accroches et conservent leurs couleurs.

## Fichiers

Dans chaque dossier `projets/<vidéo>/miniature/` :

- `rendus/h-kai.png`, `i-kai.png`, `j-kai.png` : PNG 3840 × 2160.
- `photocraft/h-kai.psd`, `i-kai.psd`, `j-kai.psd` : PSD avec textes modifiables en Archivo Black. Les décors sont rasterisés dans le PSD ; les objets restent modifiables dans la maquette HTML/SVG.
- `propositions/miniature-kai.html` : composition source, variantes `?v=h`, `?v=i`, `?v=j`.
- `rendre-kai.sh` et `export-kai-psd.py` : reproduction des exports.
- `propositions-kai.md` : intention et provenance des illustrations/logos.
- `critique-kai.md` : critique indépendante, variantes inspectées et empreintes SHA-256.
- `apercu/kai/` : contrôles à petite taille et masquage de la moitié inférieure.

Les anciens rendus, PSD, maquettes et scripts de génération sont conservés. Les vidéos et leurs textes n’ont pas été modifiés par ce travail.

## Vérification

La répartition entre producteurs et relecteurs figure dans [PLAN.md](PLAN.md). Chaque lot est relu par un autre agent GPT‑6.1 Sol, effort élevé. L’ajout du point d’interrogation sur OpenCode vient de cette critique : le script concerne une partie des utilisateurs de la Console, pas les clés de tous les spectateurs.

[verification-livraison.json](verification-livraison.json) rassemble les dimensions, empreintes, calques de texte, avertissements PhotoCraft et contrôles des liens. [verification-regie.json](verification-regie.json) consigne la détection des 18 variantes par l’API locale de la régie.

Reconstituer la galerie et contrôler les fichiers :

```sh
python3 ressources/miniatures/serie-2026-11-19/galerie.py
python3 ressources/miniatures/serie-2026-11-19/verifier.py
```

Les préférences des relecteurs sont des hypothèses visuelles, pas des prévisions de CTR. h et j comparent principalement la palette ; i change aussi la composition. Aucun test de diffusion ni changement de miniature sur YouTube n’a été effectué.
