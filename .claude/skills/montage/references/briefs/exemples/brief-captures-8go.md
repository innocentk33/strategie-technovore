Tu fais les captures web (pages réelles, phrases surlignées) pour le montage d'une vidéo YouTube française de la chaîne Technovore : « Qwen 27B sur 8 Go : plus rapide, mais à quel prix ? ». Réponds en français. Ne commite rien. N'écris que dans le projet indiqué et dans ton dossier de travail `<TMP>/cap-8go/`.

## L'outil existe
`<PREMIUM>/2026-11-qwen-27b-8go/scripts/captures-web.mjs` (copié du projet précédent, lis-le en entier) : Chrome sans interface (Mac), 1280×720 à DPR 3 ; pour chaque page il floute les pseudos GitHub / Hugging Face et les avatars, puis pour chaque « shot » il prend la capture nette et la même avec les phrases surlignées (`-surligne`, ou `-barre` pour `style: 'strike'`), plus le haut de page (`top: true`) et la page entière. `text` = phrase(s) exactes de la page à surligner, `near` = ancre pour choisir la bonne occurrence. Remplace la liste `JOBS` (garde le reste ; adapte l'en-tête). Exemples de rendu attendu : `<PREMIUM>/2026-11-meme-carte-plus-rapide/assets/shots/` (jpg) et son manifeste `edit-plan/captures.md` : regarde 2 ou 3 images.

Avant d'écrire chaque `text`, **ouvre la page** pour recopier les chaînes exactes telles qu'elles s'affichent. Une phrase introuvable = capture ratée : corrige.

## Sortie
- PNG dans `<PREMIUM>/2026-11-qwen-27b-8go/assets/captures/`, puis JPEG 2240 px de large, qualité ~90, mêmes noms, dans `.../assets/shots/` (pages entières `-page` : 1600 px).
- Les images de graphiques utiles (voir W03) en PNG dans `.../assets/images/` (téléchargées telles quelles depuis la page, avec leur URL dans le manifeste).
- Un manifeste `.../edit-plan/captures.md` : pour chaque fichier, l'URL, ce qui est surligné, et un mot si quelque chose cloche.

## Règles de l'auteur
- **Aucun pseudo, nom de chaîne ou nom de personne lisible** sur une capture : vérifie chaque image en la regardant ; floute ou recadre sinon. Les noms de projets, d'entreprises et de logiciels sont permis (Unsloth, Qwen, Hugging Face, LM Studio, llama.cpp).
- Pas de bandeau de cookies ni de pop-up sur l'image.
- Surligne seulement ce que la voix cite.

## Pages (code → URL → shots)
Les faits viennent de `<DEPOT>/projets/qwen-27b-8go/sources.md` (F1 à F17) et le texte dit de `.../script.md` (ses notes [VISUEL] disent ce que le montage veut montrer). Lis-les d'abord.
1. **W01** https://huggingface.co/unsloth/Qwen3.8-27B-GGUF/tree/main (F1, F13) : `haut` ; `fichier` = la ligne `Qwen3.8-27B-UD-IQ2_XS.gguf` avec sa taille 7.63 GB ; si visible dans la même liste, `ancien` = un fichier plus gros, de la taille de celui qui ne tenait pas (voir F2 / `recherche-mesures.md` pour son nom exact, sinon laisse tomber).
2. **W02** https://huggingface.co/unsloth/Qwen3.8-27B-GGUF/blob/main/Qwen3.8-27B-UD-IQ2_XS.gguf : `haut` (nom complet et taille).
3. **W03** https://unsloth.ai/docs/models/qwen3.8 (F4) : `haut` ; `maj` = la mention de la mise à jour Dynamic V3.1 du 11/11 ; `conditions` = la phrase qui dit les conditions des tests (contexte 128K / 256K, réflexion xhigh) ; `bench` = le graphique LiveCodeBench / DeepSWE (capture de la page autour du graphique) **et** télécharge l'image du graphique (URL gitbook citée en F4) dans `assets/images/`.
4. **W04** https://huggingface.co/Qwen/Qwen3.8-27B : `haut` (le modèle officiel).
5. **W05** https://lmstudio.ai/docs/app/advanced/per-model (F5) : `haut` ; `reglages` = les réglages GPU offload, longueur de contexte, et cache K / V en 8 ou 4 bits (surligne leurs libellés).
6. **W06** https://lmstudio.ai/docs/app/modelyaml (F7) : `reflexion` = le passage sur le contrôle de la réflexion (« thinking » / reasoning) qui dépend de la configuration du modèle.
7. **W07** https://github.com/lmstudio-ai/localization/blob/main/en/config.json (F6) : `kv` = les libellés du cache K et V (quantization type). Floute les pseudos.
8. **W08** la vidéo source des mesures F2 / F3 (https://www.youtube.com/watch?v=u_DYZhTZ2IM) : **seulement si tu peux masquer complètement le nom de la chaîne, l'avatar, les commentaires et les recommandations** : `description` = le passage de la description qui donne les vitesses 3,2 et 18 tok/s ou la GTX 1080 Ti limitée à 8 Go. Sinon, ne la capture pas et dis-le.

Si une page est inaccessible ou a changé, note-le dans le manifeste et passe à la suivante.

## Ta réponse finale (courte)
Le tableau code → fichiers produits (net / surligné) → ce qui est surligné, les pages ratées, et tout nom resté lisible.
