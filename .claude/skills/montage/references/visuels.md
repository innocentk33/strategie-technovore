# Visuels : captures, produits, logos, schémas, carte, mèmes

Un sous-agent Sonnet prépare les images en parallèle de la voix (brief : `briefs/modele-captures.md`). Tu regardes ensuite **chaque image** avant de la monter.

## Captures web (`scripts/captures-web.mjs`)

Chrome sans interface piloté par le protocole DevTools, fenêtre 1280 × 720 à DPR 3. Pour chaque page, il floute pseudos et avatars, puis pour chaque « shot » il prend la capture nette, la même avec les phrases surlignées en jaune (`-surligne`, ou `-barre` pour `style: 'strike'`), plus le haut de page (`top: true`) et la page entière (`-page`).

```bash
node scripts/captures-web.mjs assets/captures            # tout
node scripts/captures-web.mjs assets/captures W03 W04    # seulement ces codes
```

La liste `JOBS` est propre à chaque vidéo : `{ code: 'W01', suffix, url, hide: ['pseudo à flouter'], prep: JS, keep, shots: [{ id, text: ['phrase exacte de la page', …], near: 'ancre', top: true, style: 'strike' }] }`. Le 32 Go a une aide `ldlc(suffixe, id, prix, détail)` pour les fiches LDLC, et des scripts `prep` qui refusent les cookies (service-public : `SP_PREP` ; YouTube : `YT_PREP`, qui ne garde que la description).

Chaîne de production :
- PNG nets dans `assets/captures/` (3840 × 2160), puis JPEG de 2240 px de large, qualité ~90, mêmes noms, dans `assets/shots/` (pages entières `-page` : 1600 px). Le montage lit `assets/shots/<code>-<n>-<id>(-surligne).jpg`.
- Manifeste `edit-plan/captures.md` : fichier → URL → ce qui est surligné → prix du jour → ce qui cloche.

Règles :
- **Surligne seulement ce que la voix cite.**
- **Aucun pseudo, nom de chaîne ou nom de personne lisible** : `hide`, floutage, recadrage. Les noms de marques, de marchands et de logiciels sont permis.
- Bandeaux de cookies : refuser (option la plus discrète) ou masquer ; aucun pop-up sur l'image.
- **Pas de contournement de CAPTCHA ni de détection de robot.** Amazon bloque le navigateur sans interface : les offres Amazon se montrent en **cartes de prix dessinées** (`offer`, `ladder`, `twin`), jamais en fausse capture.
- **Prix** : la voix cite les prix d'une date (le relevé). Une capture n'est utile **que si elle montre le même prix, ou le détail cité** (« 1 par client », « rupture », « en stock dans + de 15 jours », date de livraison, vendeur tiers). Si le prix a bougé, pas de capture : on note le prix du jour dans le manifeste et on le signale à l'auteur (ex. le 21/11, l'offre Amazon de la RX 9060 XT avait disparu).
- L'adresse affichée dans la barre du mini navigateur est **la vraie adresse** de la page (`web(..., url='huggingface.co/…/fichier.gguf')`, raccourcie par « … » si besoin), jamais une adresse inventée. Une page tirée d'un PDF se montre en carte (`kind='card'`), pas dans un faux navigateur.
- Recadre pour qu'aucune ligne coupée ou titre parasite ne dépasse sous un bandeau ; commence déjà zoomé si la page entière montre une image cassée ou un curseur.
- Un relevé fourni par l'auteur (capture leboncoin envoyée par lui) se monte tel quel, présenté comme « relevé de l'auteur », sans nom de vendeur particulier.

## Photos de produits

- Depuis le site du fabricant ou la fiche marchand, fond propre, haute définition, URL notée dans le manifeste ; dans `assets/images/produits/`.
- Version détourée `-detoure.png` (fond blanc uni → transparence) quand c'est propre ; `P('clé')` la prend d'abord.
- Si une photo exacte n'existe pas, une variante de même format est acceptable si on le sait (la « V100 » du 32 Go est une V100S) : ne la nomme pas autrement à l'écran.

## Logos

- SVG de préférence, dans `assets/logos/<nom>.svg|png`. Les logos simples viennent de simple-icons : `https://cdn.jsdelivr.net/npm/simple-icons@13.21.0/icons/<nom>.svg`.
- Jamais de faux logo : sinon le nom en texte.
- La table `MLOGO` de `montage.py` doit prendre le fichier au nom exact (`amazon.svg`) avant une variante (`amazon-blanc.svg`), sinon un logo blanc atterrit sur une pastille blanche (piège du 21/11). LDLC a des lettres blanches : pastille sombre (`MBG`).

## Schémas

Dessinés en HTML par des briques (`gauge`, `bars`, `tiles`, `compare`, schémas propres dans `montage.py`). Ils sont **à l'échelle** : deux jauges se comparent sur la même échelle, un débordement en RAM se dessine à la même échelle que la carte (corrigé le 21/11 : il était 2,2 fois trop grand), les segments arrivent sur les mots qui les nomment. Une illustration le dit dans son surtitre (« (illustration) »).

## Carte d'Afrique

`assets/images/afrique.json` (pays extraits de `@svg-maps/world@2.0.0`, licence CC BY 4.0, avec leurs centres) et sa licence `afrique-LICENCE-CC-BY-4.0.md` sont dans le projet 32 Go : recopie-les. Le paquet `africa` de svg-maps renvoyait 404. **Crédit obligatoire dans la description** : « Carte : svg-maps, CC BY 4.0 ». Le point d'une ville se place en absolu et son libellé à part (sinon un `row-reverse` décale le point, piège de Dakar).

## Mèmes

- **Muets** (`build.py` les pose en `<video muted>`), en petite carte arrondie étiquetée « GIF », de 1,4 à 2 s, sur le mot qui les appelle (`T('…') - .1`).
- Ils parlent au public (jeune, francophone, surtout africain) et collent au propos : « omg wow » sur « si t'es malin », facepalm sur « ta marge », « 2000 years later » sur une livraison en janvier, « nani » sur « ils t'achètent quoi », une chute sur « te coûter tout un week-end ». Visages d'acteurs et memes connus permis.
- Ils **remplacent** le tampon : un mème muet ou une simple ligne de texte avec le mot clé en couleur.
- **Placement** : une boîte `(x, y, w, h)` sur une zone vide du plan, **jamais sur un titre ou un chiffre**, 30 à 40 px de marge avec tout élément. Vérifie chaque mème sur une planche à son temps exact : déplacer un mème pour corriger un plan peut le faire tomber sur un titre (régression de la critique v3 du 32 Go).
- Si le plan suivant le coupe trop tôt, avance-le (`- .3`) ou retire-le : un mème dont on ne voit pas la chute ne sert à rien.
- Fichiers dans `assets/memes/*.mp4`. Un mp4 de Tenor peut ne durer que 0,04 s : vérifie la durée avec `ffprobe -v error -show_entries format=duration -of csv=p=0 fichier.mp4` et prends une autre source si besoin.
