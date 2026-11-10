---
paths:
  - "ressources/voix/**"
  - "ressources/regie/**"
---

# Outils de `ressources/` (voix et régie)

Voix : `ressources/voix/sm7b.sh prise.wav [sortie.wav]` passe une prise dans une chaîne ffmpeg (-16 LUFS). Les réglages se changent à l'oreille, avec les variables en tête du script.

La régie (`ressources/regie/`) : `node ressources/regie/regie.mjs`, puis http://localhost:4321 (Node seul, sans dépendance).
- Le lecteur affiche tous les `.md` ; le conducteur lit le tableau « Suivi des projets » du README et la colonne Pilier du calendrier.
- Changer un statut réécrit la ligne du projet dans `README.md` et dans la grille de `calendrier.md`, avec la date du jour ; la ligne « Mis à jour le … » du calendrier reste à écrire. Les cases à cocher réécrivent leur `.md`.
- Si tu changes le format de ces deux tableaux, relance `node ressources/regie/verif.mjs`.
