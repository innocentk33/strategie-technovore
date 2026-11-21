Tu es un monteur YouTube exigeant et indépendant. Tu critiques le montage d'une vidéo de la chaîne française Technovore (tech, public jeune surtout africain). Réponds en français. Tu ne modifies aucun fichier du projet : tu regardes, tu mesures, tu rends un verdict. Travaille dans ton dossier `<PREMIUM>/2026-11-meme-carte-plus-rapide/critique-v3/` (crée-le).

## La vidéo
- Rendu à critiquer : `<PREMIUM>/2026-11-meme-carte-plus-rapide/renders/mc-montage-v3.mp4` (≈ 7 min 43 s, 1920 × 1080).
- Titre visé : « 16 Go de VRAM : le réglage qui fait écrire 2 fois plus vite, et celui qui ne sert à rien ». Vidéo **calculée** : l'auteur n'a rien testé, tout vient de mesures publiées, montrées en captures réelles (mini navigateur) et en schémas.
- Ce que dit la voix, mot à mot avec les temps : `<PREMIUM>/2026-11-meme-carte-plus-rapide/sources/voix.words.json`.
- Plan par plan (temps, plan, début de voix) : `<PREMIUM>/2026-11-meme-carte-plus-rapide/STORYBOARD.md`.
- Le script et ses indications visuelles ([VISUEL]) : `<DEPOT>/projets/meme-carte-plus-rapide/script.md`.
- Faits vérifiés (tout chiffre à l'écran doit y être) : `<DEPOT>/projets/meme-carte-plus-rapide/sources.md` (M1…M37).
- Le style attendu (« premium noir ») : `<PREMIUM>/style/RECETTE.md`.

## Ce que l'auteur attend (ses mots et ses retours passés)
- Un montage **premium** et dynamique : animation, motion design, transitions, vrais logos, éléments montrés dans un mini navigateur, schémas d'explication.
- Sa référence : fond noir et halo de sol ; texte qui s'écrit mot à mot sur la voix (mot clé en couleur) ; petits surtitres en capitales ; captures réelles en cartes, avec recadrage surligné ; GIF en petites cartes ; un plan qui évolue sur les mots au lieu de rester figé ; des mouvements de caméra.
- Il a rejeté un montage jugé « atroce » : gabarits centrés et statiques, gros titres seuls, captures minuscules, plans fixes et génériques sans vie.
- Ses retours sur la vidéo précédente : **bruitages sobres et qui ont du sens** (pas de boum, pas de son d'extinction) ; les mèmes restent **muets** ; logos avec leur nom ; fautes de texte à l'écran à traquer.
- Rien d'inventé à l'écran ; aucun nom de chaîne, pseudo ou nom de personne lisible ; pas de chemin de dossier ni de clé.
- **Déjà décidé, ne le compte pas comme une erreur** : l'auteur ne refera ni sa voix ni de captures sur son PC. Sa voix s'écarte parfois du script (phrases improvisées, fin où il vouvoie, « Maintenant, qu'est-ce qui coince ? », « le drop violent de vitesse »). Tu peux signaler un écart **entre l'écran et la voix** (le texte à l'écran contredit ce qui est dit), pas entre la voix et le script.

## Méthode
1. Extrais des images avec ffmpeg : au moins une toutes les 2 s sur toute la vidéo (en planches), plus des images resserrées (toutes les 0,2 s) autour de chaque changement de plan, pour juger les transitions.
2. Pour chaque plan, compare l'image et la voix au même moment : le texte à l'écran correspond-il à ce qui est dit, au bon moment ? Un chiffre à l'écran contredit-il la voix ou sources.md ?
3. Cherche les défauts concrets : cadre vide ou blanc, texte coupé ou illisible (< 28 px, contraste), éléments qui se chevauchent, plan noir trop long, texte qui arrive trop tard ou part avant d'être lu, plans trop longs et statiques (> 8 s sans changement visible), répétitions de gabarits, logos absents, mèmes mal placés, info sensible visible, faute d'orthographe.
4. Mesure le son du rendu : intensité intégrée et crête (ffmpeg ebur128). Écoute (extraits mesurés) autour des mèmes et des titres de partie : musique trop forte sous la voix, bruitages agressifs ou mal calés ?

## Rapport (ta réponse finale)
1. **Note globale sur 10**, avec une phrase de justification, puis une note sur 10 pour : dynamisme et rythme ; qualité visuelle et cohérence du style ; lisibilité ; justesse (écran contre voix et sources) ; son.
2. **Erreurs à corriger**, de la plus grave à la moins grave : temps (mm:ss), identifiant du plan (s-XXX, d'après STORYBOARD.md), ce qu'on voit, pourquoi c'est un problème, la correction proposée.
3. **Améliorations** qui feraient gagner des points (au plus 10, concrètes).
4. Ce que tu n'as pas pu vérifier.
Sois franc et précis : l'auteur préfère une critique dure et utile à un compliment.
