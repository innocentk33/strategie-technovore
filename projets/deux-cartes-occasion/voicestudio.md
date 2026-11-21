# VoiceStudio : notes de génération (refait le 21/11 avec les conventions du jour)

Voix de « 32 Go pour Qwen 27B ». Texte tiré de `teleprompteur.md` (V5, grillé 8/10), **sans changement de fond** : seule l'écriture a été adaptée au moteur. Règles : [`.claude/rules/voix-synthese.md`](../../.claude/rules/voix-synthese.md).

- [`voicestudio.txt`](voicestudio.txt) : 83 lots pour la page **Voice**. Ne colle que le texte sous chaque ligne `LOT …`, sinon l'en-tête sera lu.
- [`voicestudio-stories.txt`](voicestudio-stories.txt) : le même texte sans en-têtes, pour une version complète dans **Stories / Audiobook**. Généré depuis `voicestudio.txt` : si tu en changes un, refais l'autre.

Aucune pause balisée, aucun point de suspension (le « 2800 euros… » du téléprompteur devient une virgule : les silences se posent au montage). Seules balises : un `[sigh]` (lot 14, avant « Bon, la boîte dit trente-deux gigas ») et un `[laughter]` (lot 25, après « Noël sans cartes »). Retire-les si ça sonne faux.

## Ce qui change par rapport à la version du 20/11

- **Conventions du 21/11** : Ti → « té i », XT → « ix té », numéros de carte en milliers (5060 → « cinq mille soixante », 5080 → « cinq mille quatre-vingt », 9060 XT → « neuf mille soixante ix té »), R9700 → « èr neuf mille sept cent », ASUS → « azus », « en nun mois » → « en n'un mois ».
- **Lots refaits** : chaque phrase de prix est dans son propre lot (ou avec ses voisines de prix), marquée « à relire le 26/11 ». L'ancien découpage (55 lots) mélangeait prix et texte.
- Le lot 6 de l'ancienne version (« la même carte, 400 euros plus chère… ») est maintenant isolé.

## Prononciations à valider à l'écoute

| Dans le script | Écrit pour le moteur |
|---|---|
| Qwen 27B | Kwen vingt-sept bé |
| VRAM | vé-ram |
| RTX 5060 Ti | RTX cinq mille soixante té i |
| RTX 5080 / 5090 | cinq mille quatre-vingt / cinq mille quatre-vingt-di za aussi (liaison écrite) |
| RX 9060 XT | RX neuf mille soixante ix té |
| Arc A770 | Arc A sept cent soixante-dix |
| Arc Pro B65 / B70 | bé soixante-cinq / bé soixante-diss |
| Radeon AI PRO R9700 | Radeon AI Pro èr neuf mille sept cent |
| Tesla V100 | Tesla vé cent |
| Mac mini M6 | Mac mini M six |
| ASUS, ASRock | azus, Asrock |
| CUDA 13, pilote 580 | couda treize, cinq cent quatre-vingt |
| llama.cpp | lama CPP |
| PCIe 3.0 | PCI Express trois |
| 12V-2x6 | douze V deux fois six |
| Ryzen AI Max+ | Ryzen AI Max Plus |
| leboncoin | le bon coin |
| NVIDIA | Nvidia |

Sigles gardés en capitales : RTX, RX, AMD, LDLC, ATX, TVA, PC, IA, AI, CPP, PCI (ce dernier hors liste officielle, à confirmer).

Garde la même graphie d'un bout à l'autre ; ajoute les mots récurrents au dictionnaire de prononciation de l'app.

## Réglages (inchangés)

| Réglage | Valeur |
|---|---|
| Moteur | OmniVoice |
| `num_step` | 32 |
| `guidance_scale` | 2,0 |
| `speed` | 1,0 ; 1,05 si c'est plus lent que ta vraie voix |
| `class_temperature` | essaie le lot 1 à 0, 0,3 et 0,5, choisis à l'oreille, puis ne change plus |
| `postprocess_output` | actif |

Deux profils au maximum (« posé » et « énergique »), même micro et même pièce ; seed épinglée dès qu'une prise sonne comme toi.

## Lots à faire en plusieurs prises (3 à 4)

1, 2, 4 (hook) ; 13 et 14 (révélation et chute de l'addition) ; 21 et 22 (le boss de fin) ; 25 (« Noël sans cartes ») ; 44 (« Rien. C'est la même carte. ») ; 36 (abonnement) ; 82 (phrase finale).

## Prix à relire le 26/11

Lots marqués « à relire » : 3, 6, 19, 20, 21, 24, 26, 27, 38, 39, 40, 41, 42, 43, 45, 46, 49, 50, 55, 58, 61, 69, 71, 73, 75, 77, 78, 80. Si un prix bouge, regénère seulement ce lot.
