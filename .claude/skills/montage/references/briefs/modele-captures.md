<!-- Modèle (origine de chaque variable : ../sous-agents.md, « D’où viennent les variables »). Remplace : {{TITRE}}, {{PROJET}}, {{DEPOT_PROJET}}, {{DATE_RELEVE}} (date des prix dits par la voix), {{PAGES}} (liste numérotée W01…Wnn : page, ce qu'il faut surligner, prix ou détail du relevé), {{PRODUITS}}, {{LOGOS}}, {{SCRATCH}}. Exemples réels : exemples/brief-captures-32go.md, brief-captures-8go.md. Modèle : Sonnet. -->
Tu prépares les images (captures web, photos de produits, logos) du montage d'une vidéo YouTube française de la chaîne Technovore : « {{TITRE}} ». Réponds en français. Ne commite rien. N'écris que dans `{{PROJET}}/` et `{{SCRATCH}}`.

## À lire d'abord
- Le script avec ses indications [VISUEL] : `{{DEPOT_PROJET}}/script.md`.
- Les faits et leurs URL : `{{DEPOT_PROJET}}/sources.md` (et le relevé de prix daté s'il existe, dans `{{DEPOT_PROJET}}/recherche/`).
- L'outil : `{{PROJET}}/scripts/captures-web.mjs` (lis-le en entier) : Chrome sans interface, 1280×720 à DPR 3 ; il floute pseudos et avatars, prend pour chaque « shot » la capture nette et la même avec les phrases surlignées (`-surligne`, ou `-barre` pour `style: 'strike'`), le haut de page (`top: true`) et la page entière. `text` = phrase(s) exactes de la page, `near` = ancre. Remplace la liste `JOBS`. Lancement : `node scripts/captures-web.mjs assets/captures [codes…]`. Exemple du rendu attendu : `<PREMIUM>/2026-11-qwen-27b-32go/assets/shots/` et son manifeste `edit-plan/captures.md`.

## Règle sur les prix
La voix cite les prix du {{DATE_RELEVE}}. Une capture d'offre n'est utile que si elle montre **le même prix** (ou le détail cité : quantité limitée, rupture, délai, vendeur tiers) ; sinon ne la mets pas dans `assets/shots/` et note seulement le prix du jour dans le manifeste. Pas de contournement de CAPTCHA ni de détection de robot (Amazon bloque : note-le et passe). Bandeaux de cookies refusés ou masqués.

## À produire
PNG dans `assets/captures/`, puis JPEG 2240 px de large, qualité ~90, mêmes noms, dans `assets/shots/` (pages entières `-page` : 1600 px). Manifeste `edit-plan/captures.md` : fichier → URL → ce qui est surligné → prix du jour → ce qui cloche.
{{PAGES}}
- **Photos de produits** (site du fabricant ou fiche marchand, fond propre, haute définition, URL dans le manifeste) dans `assets/images/produits/` : {{PRODUITS}} ; version `-detoure.png` si le détourage est propre.
- **Logos** (SVG de préférence) dans `assets/logos/<nom>.svg` : {{LOGOS}} ; logos simples depuis `https://cdn.jsdelivr.net/npm/simple-icons@13.21.0/icons/<nom>.svg`.

## Règles de l'auteur
- **Aucun pseudo, nom de chaîne ou nom de personne lisible** sur une image : regarde chaque image, floute ou recadre. Marques, marchands et logiciels permis.
- Surligne seulement ce que la voix cite. URL réelles uniquement.

## Ta réponse finale (courte)
Le tableau fichier → ce qui est montré / surligné ; les prix du jour qui ont changé depuis le {{DATE_RELEVE}} ; les pages ratées ou bloquées ; tout nom resté lisible.
