# Vérifications : boucle courte, revues de voix, critiques, rendus

## Boucle courte (à chaque modification de `montage.py`)

```bash
MC_DRY=1 python3 scripts/montage.py 2>&1 | tail -2
python3 scripts/montage.py 2>&1 | tail -1 && npx --yes hyperframes@0.9.47 check 2>&1 | grep -E "✗|⚠|error\(s\)|Check (passed|failed)|pins" | cut -c1-220
```

**Lis les avertissements**, ne les masque pas : compare-les à la liste de la fois précédente et traite chaque **nouveau**. Pour les compter par type : `npx --yes hyperframes@0.9.47 check 2>&1 | grep -E "⚠|✗" | sort | uniq -c`.

Avertissements attendus (vus sur le 8 Go et sur un projet neuf le 21/11), à vérifier sans forcément corriger :
- `✗ #s-NNN-wN 1.41:1 (need 3:1)` dans la partie Contraste : les mots en gris fantôme de `ktg()` avant qu'ils s'allument ; voulu, la section ne fait pas échouer le check ;
- `dead_stretch` sur les 11 dernières secondes : l'écran de fin reste fixe pour les éléments YouTube ;
- `first_frame_empty` : **regarde la planche à 0 s** ; si l'accroche n'y est pas, corrige (règle « la promesse dès 0,2 s ») ;
- « This is hyperframes 0.9.47, but this project pins hyperframes@0.9.75 » dans un ancien projet (`demarrage.md`, étape 2) ;
- `audio_clip_silent` sur une voix fictive (`demarrage.md`).
À traiter : `line_unread` (une ligne qui part avant d'avoir pu être lue : tiens-la plus longtemps), `text_below_floor` (texte sous 28 px), tout `http_error` (fichier introuvable, souvent un chemin hors du projet), tout nouveau type.

Puis **regarde les images** aux moments touchés. Les temps se calculent depuis `edit-plan/timeline.json` (ici, le milieu des trois premiers plans) :

```bash
T=$(python3 -c "
import json;t=json.load(open('edit-plan/timeline.json'));print(','.join(str(round(x['start']+min(2.5,x['duration']*.6),2)) for x in t[:3]))"); npx --yes hyperframes@0.9.47 snapshot --at $T --no-end -o renders/snap-test 2>&1 | tail -1
```

Ou simplement deux temps précis (en secondes, séparés par une virgule) :

```bash
npx --yes hyperframes@0.9.47 snapshot --at 13.2,159 --no-end -o renders/snap-2 2>&1 | tail -1
```

Le dossier contient une image par temps et `contact-sheet.jpg` (planche) : ouvre-la avec Read. `snapshot --review -o renders/review` fait une planche de toute la vidéo. Un `check` qui passe ne montre pas à quoi ça ressemble : on ne dit jamais « c'est bon » sans avoir regardé.

Cherche à chaque planche : un mème sur un texte, un texte coupé ou sous un autre, un cadre vide, une silhouette grise de produit, un logo blanc sur blanc, une adresse fausse, un chiffre différent de la voix.

## Revues de la voix (2 au plus)

Par un sous-agent Opus qui **n'a pas monté la voix** et ne lit pas les rapports de celui qui l'a montée (brief : `briefs/modele-verif-voix.md`). Il transcrit en verbatim, aligne sur le téléprompteur, vérifie un par un les prix, chiffres et noms, mesure l'énergie (coupes, clics, blancs, souffles, trous numériques), les raccords et, pour une voix clonée, chaque changement de source (niveau, hauteur, débit, classés inaudible / léger / gênant). Il ne modifie rien.

Ensuite : tu corriges (ou le monteur de la voix corrige), puis **une seconde revue, la dernière**. Ce qui reste douteux part dans la liste « à écouter au casque » de ton message final, avec les temps. L'auteur a fixé ce plafond le 21/11 (« j'autorise max 2 reviews de la voix »).

Chaque correction de voix change les temps : relance `montage.py` (les ancres suivent) et regarde les plans touchés.

## Rendu 1080p et critiques (3 au plus)

```bash
npx --yes hyperframes@0.9.47 render -o renders/<court>-montage-v1.mp4 > renders/render-v1.log 2>&1; tail -1 renders/render-v1.log
```

Le rendu prend longtemps (une vidéo de 9 min) : lance-le en arrière-plan et attends la notification. Mesure ensuite la durée (`ffprobe`) et le son (`son.md`).

Critique par un sous-agent Opus indépendant, sur le rendu 1080p (brief : `briefs/modele-critique.md`) : note globale et par axe (dynamisme, style, lisibilité, justesse, son), erreurs datées et rangées de la plus grave à la moins grave, avec le plan `s-NNN`. Les critiques passées ont donné 6,5 → 7 → 7,5 sur le 32 Go, et 7,5 sur le 8 Go.

Tu corriges les erreurs bloquantes et la plupart des autres, tu vérifies **chaque correction par une planche** au temps exact (une correction peut en casser une autre), puis nouveau rendu et nouvelle critique. Trois tours au plus. Dis-lui ce qui est déjà décidé (voix non refaite, pas de capture Amazon possible…) pour qu'il ne le compte pas comme une erreur.

## 1080p puis 4K

Au dernier 1080p, **tu t'arrêtes** : chemin du fichier, ce qui a changé, ce qui reste douteux, puis tu demandes s'il veut des retouches ou la 4K. Exception : carte blanche donnée **pour cette vidéo** (« je te laisse tout terminer ») ; alors tu lances la 4K une fois les critiques et corrections finies, et tu le dis dans le message final.

```bash
npx --yes hyperframes@0.9.47 render --resolution 4k --fps 30 -o renders/<court>-montage-final-4k.mp4 > renders/render-4k.log 2>&1; tail -1 renders/render-4k.log
```

Contrôle de la 4K : `ffprobe -v error -show_entries format=duration:stream=width,height,r_frame_rate -of csv=p=0 renders/<fichier>.mp4` (3840 × 2160, 30/1, même durée que le 1080p), le niveau (`son.md`) et quelques images extraites.

## Ce qu'une machine ne vérifie pas
Personne n'écoute au casque dans cette chaîne de travail : tout est mesuré. Dis-le à l'auteur et donne-lui la liste courte et datée des passages à écouter (prononciations douteuses, raccords de source, débit).
