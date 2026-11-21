# Pièges déjà rencontrés (symptôme → cause → correction)

## Voix
| Symptôme | Cause | Correction |
|---|---|---|
| « et et », « un un », deux mots superposés dans la voix livrée (12/11) | transcription par Whisper ou Parakeet par prises isolées | wav2vec2 verbatim sur toute la prise, découpée dans les silences ; retranscrire ±2 s autour de chaque raccord (`verif_raccords.py`) |
| mot tranché à un raccord | coupe héritée d'un ancien montage, pas calée sur l'énergie | bords calés sur les îlots d'énergie ou le creux le plus bas (`voix.py`) |
| « soixante-dix » au lieu de « 5060 Ti » | pause resserrée entre « 5060 » et « Ti », ou synthèse qui fond le « Ti » | ne pas resserrer cet écart ; prendre la phrase dans l'autre version ; reprise de l'auteur (`retouches.md`) |
| trous de silence numérique, effet de porte (19/11) | atténuation de 35 dB sur un fond presque nul, ou zéros insérés | remplacer par du fond pris tout près (`retouche_voix.py`), jamais de zéros ; voix clonée : remplacer au lieu d'atténuer |
| grondement de ventilation | bruit de la pièce | coupe sous 80 Hz (`retouche_voix.py`) ; remesurer le plancher par zone |
| l'attaque d'un /s/ prise pour un bruit | détection de bruit sur l'étendue d'un mot | jamais de traitement à ±30 ms d'un mot wav2vec2 |
| saut de hauteur audible à un changement de source (5 dans la revue 1 du 32 Go) | les deux versions clonées n'ont pas la même hauteur | PSOLA par bloc (`strata_psola.py`), rampes (`cale_hauteur.py`) ; jamais `asetrate` |
| marche de niveau ou de fond à un changement de source | gain et fond différents | `cale_gains.py`, fond des pauses commun, fondus égale puissance de 30 ms |
| chiffres avalés | accélération trop forte | ×1,25 au plus ; `no_tempo` sur les chiffres (« vers 32 gigas ») |
| soupir ou rire de synthèse qui sonne faux | balises `[sigh]`, `[laughter]` | les couper |

## Reprises de l'auteur (vraie voix dans une voix clonée)
| Symptôme | Cause | Correction |
|---|---|---|
| la greffe s'entend (timbre, hauteur) au milieu d'une phrase clonée | vraie voix et clone ne se fondent pas sur quelques mots | préférer remplacer la **phrase entière** ; greffer seulement un nom, pris dans une phrase dite à vitesse normale ; demander à l'auteur de réenregistrer la phrase complète |
| une reprise démarre 3 demi-tons plus haut que la voix autour | intonation appuyée de l'auteur en début de phrase | PSOLA borné : jamais plus de 1 demi-ton d'écart avec la voix voisine ; vérifier la hauteur des 3 s avant et après |
| un faux départ collé dans la voix | les reprises contiennent des essais ratés (« faux-depart-en-france ») | transcrire tout le fichier, écarter les essais (banque, classe « non utilisé »), garder la meilleure prise |
| un détail disparaît (« sur leboncoin », « le 20 novembre » dans R3) | l'auteur a reformulé sa phrase | le texte de l'auteur prime, mais signale-lui ce qui est perdu ; vérifier que l'écran ne montre pas un fait que la voix ne dit plus |
| un nom de carte mal étiqueté dans la banque | wav2vec2 entend « dix », « i », « xt » pour « Ti » | étiqueter d'après la liste des cartes du script, `verifie: false` tant que l'auteur n'a pas confirmé |
| la reprise reste plus lente que la voix remplacée | mot isolé, plus lent et appuyé | tempo par passage au-delà du ×1,1 (×1,25 au plus), mesuré et noté dans `tempo_note` |
| plans décalés ou ancres cassées après les reprises | durée de la voix changée, mot reformulé | comparer `edit-plan/dry-starts.json` avant / après, corriger les `T()` |

## Montage
| Symptôme | Cause | Correction |
|---|---|---|
| `KeyError: phrase introuvable après …` | ancre absente après le curseur (mot mal transcrit, nombre écrit en lettres, apostrophe) | écrire l'ancre comme dans `voix.words.json` (chiffres, apostrophes en espaces), ou une autre phrase du même plan |
| un élément s'allume au mauvais moment | l'ancre trop courte a trouvé une autre occurrence (« exactement », « b70 ») | ancre de 2-3 mots, ou `after=` ; dans `ladder`, temps borné `t = max(t, sc.start + .6 + k*.06)` |
| un état de départ écrasé (ligne qui ne s'allume pas) | deux tweens sur le même élément | le second tween avec `kind='move'` (`immediateRender:false` automatique) |
| silhouette grise à la place d'un produit | photo absente : `P()` renvoie le substitut sans erreur | ajouter la photo ; `grep -l placeholder-produit compositions/*.html` avant le rendu |
| capture absente, plan de repli à la place | `web()` renvoie `None` | vérifier que `assets/shots/<code>-*` existe |
| logo blanc sur pastille blanche | `MLOGO` a pris `amazon-blanc.svg` | préférer le nom exact |
| débordement de RAM 2,2 fois trop grand (21/11) | débordement dessiné à une autre échelle | même échelle que la carte (`gauge`, corrigé dans `blocs.py`) |
| point de Dakar décalé | `row-reverse` sur le point et son libellé | point en position absolue, libellé à part |
| mème qui cache un titre (régression v3 du 32 Go) | mème déplacé sans revoir le plan d'arrivée | planche au temps exact de chaque mème après chaque déplacement |
| mème dont on ne voit pas la chute | coupé par le plan suivant | l'avancer ou le retirer |
| adresse inventée dans le mini navigateur (32 Go v2, v3) | URL reconstituée de mémoire | la vraie adresse de la page ; une page de PDF en carte |
| légende qui dit l'inverse de la voix (8 Go v3) | surtitre écrit d'après le script, pas d'après la phrase dite | relire chaque surtitre contre la phrase au même moment |
| cadre vide pendant les 3 premières secondes (8 Go v3) | éléments de l'accroche ancrés trop tard | légende et visuel de l'accroche dès 0,2 s |
| pastille recouverte par la barre de lecture | élément à 23 px du bas | rien d'important à moins de ~80 px du bas |
| texte sur texte pendant 1-2 images entre deux plans de texte | fondu enchaîné de 0,25 s | coupe sèche entre deux plans de texte (point encore ouvert sur le 32 Go) |
| plan statique de 4 à 7 s | une seule carte qui attend la suivante | faire entrer les éléments suivants en fantôme, ou montrer la capture qui existe |
| un tampon « VITESSE : NON » (18/11) | `stamp()` | interdit : mème muet ou ligne de texte |

## Outils
| Symptôme | Cause | Correction |
|---|---|---|
| `verif_*.py` absents du nouveau projet | `rsync --exclude 'verif*'` non ancré | `--exclude '/verif*'` (voir `demarrage.md`) |
| planche de mèmes qui échoue (`hstack`) | images de hauteurs différentes | les remettre à la même hauteur |
| extraction d'image d'un mjpeg qui échoue | plage de couleurs non standard | `-strict unofficial` dans ffmpeg |
| mp4 Tenor de 0,04 s | fichier tronqué | vérifier la durée avec `ffprobe`, prendre une autre source |
| paquet `@svg-maps/africa` en 404 | n'existe pas | extraire l'Afrique de `@svg-maps/world@2.0.0` |
| `checklist()` qui plante | chaque élément demande trois champs | `(texte, temps, couleur)` |
| Amazon vide ou CAPTCHA en capture | détection de robot | pas de contournement : carte de prix dessinée |
| `torch` introuvable | aucun Python de la machine ne l'a | `uv run --no-project --with torch --with transformers --with numpy python …`, en arrière-plan |
| une commande de rendu lancée avec une autre version de HyperFrames | `npm run render` utilise la version de `package.json` (0.9.75 hérité du gabarit) | toujours `npx --yes hyperframes@0.9.47` ; dans un projet neuf, épingle 0.9.47 dans `package.json` (`demarrage.md`, étape 2) |
| « This is hyperframes 0.9.47, but this project pins hyperframes@0.9.75 » à la fin de `check` | épingle du gabarit `starter-long` | attendu dans les anciens projets ; disparaît quand `package.json` épingle 0.9.47 |
| `check` échoue en `http_error: 404` sur la voix | `MC_VOICE` pointe hors du projet | mettre la voix (même fictive) dans `assets/audio/` |
| `index.html` remplacé par des plans de test | `scripts/test_slice.py` lancé | relancer `montage.py`, effacer `compositions/test-*.html` |
