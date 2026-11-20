# VoiceStudio : notes de génération (20/11)

Test de [VoiceStudio](https://github.com/debpalash/VoiceStudio) (moteur par défaut OmniVoice) pour la voix de « 32 Go pour Qwen 27B ». Texte tiré de `teleprompteur.md` (V5, grillé 8/10), **sans changement de fond** : seule l'écriture a été adaptée au moteur.

- [`voicestudio.txt`](voicestudio.txt) : 55 lots pour la page **Voice**. Ne colle que le texte sous chaque ligne `LOT …`, sinon l'en-tête sera lu.
- [`voicestudio-stories.txt`](voicestudio-stories.txt) : le même texte sans en-têtes, pour une première version complète dans l'onglet **Stories / Audiobook**. Une phrase par ligne et une ligne vide entre les lots. Il est généré depuis `voicestudio.txt` : si tu en changes un, refais l'autre.

Aucune pause n'est balisée (ni `[pause]`, ni `...`) : les silences se règlent au montage. Seules balises restantes : un `[sigh]` et un `[laughter]`, donc les deux fichiers marchent sur les deux onglets. Vérifié avec `verifier_script.py --mode voice` : seuls restent les sigles voulus.

## Ce qui a changé par rapport au téléprompteur

1. **Tous les nombres en toutes lettres** : prix, dates, gigas, références de cartes. La normalisation automatique lit mal « 5060 », « 31,4 » ou « 262 000 ».
2. **Pas de majuscules d'emphase** : elles seraient épelées. ASUS, NVIDIA et VRAM sont réécrits (voir le tableau). L'emphase reste portée par ton texte (mot fort en fin de phrase, phrases courtes) ; les pauses viendront au montage.
3. **Liaisons et prononciations écrites comme elles se disent (20/11, ta demande)**, pour que le moteur ne les rate pas :
   - « plus » qui ne se prononce pas : *plu de si millions*, *plu chère*, *plu zépaisses*, *ne compile plu* ; et quand le *s* s'entend : *de pluss*, *en pluss* ;
   - nombres + euros : *hui cent zeuros*, *quatre-vingt zeuros*, *mille quatre cent quatre-vingt-troi zeuros*, *si cent soixante-di zeuros* ;
   - chiffres qui changent devant une consonne : *si millions*, *hui gigas*, *hui broches*, *vin novembre*, *cent vingt-hui mille*, *quatre-vingt-di soixante* ;
   - liaisons obligatoires : *en nun mois*, *un nordinateur*, *on na vu*, *en noccasion*, *du troi zau cinq*, *deu zans*, *les zautres*, *ses zoutils*, *tes zapplis*, *un nachat*, *un nadaptateur*, *en nacceptant*, *en naccepte*, *tou ten bas*, *quatre-vingt-di za aussi*.
   Les liaisons facultatives sont laissées de côté, pour garder ton ton parlé (*t'as*, *si t'es malin*).
4. **Les lignes du téléprompteur sont recollées en phrases**. En Stories, chaque ligne est un rendu séparé avec un silence de 250 ms : tes coupures en milieu de phrase auraient haché la voix.
5. Deux sons non verbaux seulement, à retirer si ça sonne faux :
   - `[sigh]` avant « Bon, la boîte dit trente-deux gigas » (lot 12) ;
   - `[laughter]` après « Noël sans cartes » (lot 20).

## Prononciation : à corriger selon ta façon de dire

| Dans le script | Écrit pour le moteur | Si ça sonne mal |
|---|---|---|
| Qwen 27B | Kwen vingt-sept bé | « Tchouène », ou le dictionnaire de prononciation de l'app |
| VRAM | vé-ram | `[[vé ram]]` |
| RTX 5060 Ti | RTX cinquante soixante Ti | « Ti » peut sortir « ti » ou « taï » : teste |
| RX 9060 XT | RX quatre-vingt-dix soixante XT | |
| B65 / B70 | bé soixante-cinq / bé soixante-dix | |
| R9700 | R quatre-vingt-dix-sept cents | « R quatre-vingt-dix-sept zéro zéro » |
| A770, V100, M6 | A sept cent soixante-dix, vé cent, M six | |
| ASUS, ASRock, NVIDIA | Asus, Asrock, Nvidia | « Ènvidia » si le « N » saute |
| PCIe 3.0 | PCI Express trois | |
| llama.cpp | lama CPP | |
| CUDA | Couda | |
| 12V-2x6 | douze V deux fois six | |
| Ryzen AI Max+ | Ryzen AI Max Plus | « A I » se lit à la française |
| leboncoin | le bon coin | |
| Hugging Face, tokens, slot, chipset, week-end | inchangés | anglicismes : à écouter |

Sigles gardés en capitales parce qu'ils s'épellent : RTX, RX, XT, AMD, LDLC, ATX, TVA, PC, CPP, AI.

Mets les mots récurrents (Kwen, vé-ram, Nvidia, cinquante soixante Ti) dans le **dictionnaire de prononciation** de l'app une fois trouvés : tu gardes la même prononciation d'un bout à l'autre, et dans les prochaines vidéos.

## Garder ton ton et ta constance

Le clonage copie ta **manière de parler**, pas seulement ton timbre. C'est donc le clip de référence qui porte ton ton, bien plus que le texte.

- **Clip de référence** : ta propre voix, 3 à 10 s, au SM7B, sec, avec sa transcription exacte. Prends un passage de tes anciennes vidéos où tu es naturel, pas un texte lu à froid.
- **Deux profils au maximum**, avec le même micro et la même pièce :
  - « posé » pour les explications et les garanties (lots 8-10, 26, 42-45) ;
  - « énergique » pour le hook et les chutes (lots 1-4, 11, 18, 20, 27, 32, 54).
  Vérifie à l'écoute que le timbre reste le même d'un profil à l'autre. Sinon, un seul profil pour toute la vidéo.
- **Mêmes réglages du début à la fin** : la constance vient de là.

| Réglage | Valeur |
|---|---|
| Moteur | OmniVoice (par défaut) |
| `num_step` | 32 |
| `guidance_scale` | 2,0 |
| `speed` | 1,0 ; 1,05 si c'est plus lent que ta vraie voix |
| `class_temperature` | essaie le lot 1 à 0, 0,3 et 0,5, choisis à l'oreille, puis ne change plus |
| `postprocess_output` | actif : il coupe les blancs du moteur, tu poses les tiens au montage |

Seed libre pendant les prises. Épingle-la dès qu'une prise sonne vraiment comme toi.

## Ordre de travail conseillé

1. Rends tout `voicestudio-stories.txt` dans Stories pour une base complète et le minutage.
2. Sur la page Voice, refais **3 à 4 prises** des moments clés : lots 1, 2, 4, 11, 18, 20, 27, 32, 54. Nomme-les `lot11_v1.wav`, `lot11_v2.wav`…
3. Au montage, garde la meilleure prise par phrase. Tu peux combiner des morceaux de plusieurs prises. Passe ensuite la voix dans `ressources/voix/sm7b.sh` comme d'habitude.
4. Ajoute les pauses au montage. Rappel de ta règle : pas de raté, de souffle ni de blanc.

## Prix à relire le 26-27/11

Les lots de prix sont isolés pour pouvoir les regénérer seuls si un prix bouge : 16, 17, 19, 21, 30, 31, 35, 38, 40, 47-52 (marqués « à relire » dans les en-têtes). Les lots 3, 6, 18, 32, 33 et 39 reprennent aussi des montants : vérifie-les s'ils changent.
