---
name: voix-off-voicestudio
description: Coach pour rendre naturelle une voix off générée avec VoiceStudio (ex-OmniVoice Studio, alternative locale et open source à ElevenLabs, moteur OmniVoice par défaut). Prépare et annote un script avec les balises propres à VoiceStudio ([pause 500ms], [laughter], [sigh]), remplace les techniques ElevenLabs qui ne marchent pas ici (MAJUSCULES épelées, balises [excited]/[whispers] lues à voix haute), recommande les paramètres (class_temperature, num_step, guidance_scale, seed, speed, postprocess_output), aide au clonage et au Voice Design par attributs, et guide la génération par prises, le montage et le doublage intégré. Utilise ce skill dès que l'utilisateur mentionne VoiceStudio, OmniVoice, OmniVoice Studio, voicestudio.sh, ou veut adapter un script ou des réglages ElevenLabs à VoiceStudio, même s'il demande simplement de « préparer ce script », « améliorer la voix » ou « pourquoi ça sonne robotique » dans un contexte VoiceStudio.
---

# Voix off naturelle avec VoiceStudio

Une voix IA sonne fausse surtout parce qu'elle est **trop régulière** : même ton, même rythme, même intensité. Le travail consiste à réintroduire de la variation humaine — dans le texte, dans le clip de référence, dans la génération, puis au montage.

VoiceStudio n'est pas ElevenLabs : plusieurs réflexes ElevenLabs y **dégradent** le résultat. Ce skill adapte la méthode au moteur par défaut de VoiceStudio (OmniVoice). Si l'utilisateur a activé un autre moteur (CosyVoice 3, IndexTTS2, VoxCPM2…), consulte `references/parametres.md`, section « Autres moteurs ».

## Les 3 pièges à ne jamais oublier

1. **Les MAJUSCULES sont épelées.** Un mot écrit en capitales est lu lettre par lettre. Ne jamais utiliser les majuscules pour l'emphase. Les réserver aux sigles qui *doivent* être épelés (SNCF, PDG). Un sigle qui se prononce comme un mot s'écrit en minuscules avec une capitale initiale (Nasa, Otan, Unesco).
2. **Une balise inconnue est lue à voix haute.** VoiceStudio transmet le texte tel quel au moteur et ne supprime pas les balises qu'il ne connaît pas. `[excited]`, `[whispers]`, `[happy]`, `<break>` (ElevenLabs / SSML) seront prononcés. N'utiliser que les balises listées dans `references/balises-et-annotation.md`.
3. **Les balises longform ne marchent que dans les onglets Audiobook et Stories.** `[slow]…[/slow]`, `[fast]…[/fast]`, `[emphasis]…[/emphasis]`, `[spell]`, `[voice:NOM]` ne sont pas interprétées sur la page Voice (génération simple). Demande ou déduis dans quel onglet l'utilisateur génère avant de les utiliser.

## Les 4 piliers du réalisme (et leur traduction VoiceStudio)

1. **Variation du ton et du débit.** Se règle par la ponctuation, le paramètre `speed`, les balises `[slow]`/`[fast]` en longform, et surtout **le clip de référence** : le clonage reproduit la *manière de parler* du clip, pas seulement le timbre. Un clip plat donne une voix plate, un clip animé donne une voix animée. C'est le levier expressif le plus fiable du moteur par défaut.
2. **Pauses.** Utiliser `[pause]` (350 ms), `[pause 500ms]`, `[pause 1.5s]` (jusqu'à 10 s). Ces balises insèrent un vrai silence et fonctionnent sur tous les moteurs. Les `...` et les virgules restent utiles pour les micro-pauses et l'intonation.
3. **Emphase, sans majuscules.** Placer le mot fort en fin de phrase (l'accent tonique du français tombe en fin de groupe), l'isoler par une pause courte, écrire une phrase très courte, utiliser une tournure emphatique (« c'est … qui »), la répétition, ou `!`. En longform : `[emphasis]mot[/emphasis]`. Détails et exemples dans la référence.
4. **Un script écrit comme on parle.** Si le texte sonne rédigé ou généré par IA, signale-le et propose de le réécrire plus oralement avant d'annoter.

Sons non verbaux : n'utiliser que **`[laughter]`** (rire) et **`[sigh]`** (soupir). Les autres balises du moteur (`[question-ah]`, `[surprise-wa]`, `[confirmation-en]`, `[dissatisfaction-hnn]`…) ne produisent que des onomatopées (« ah », « oh », « wa ») sans intérêt pour une voix off : ne jamais les proposer.

Le moteur par défaut n'a **pas de contrôle d'émotion** (`[happy]`, `[sad]` ne sont pas reconnus). Le seul style de diction accepté est `whisper`, à régler via le champ de style / Voice Design, pas dans le texte.

## Identifier le besoin

- **A. Annoter un script** → lis `references/balises-et-annotation.md`, puis section A ci-dessous
- **B. Convertir un script ou des réglages ElevenLabs** → section B
- **C. Choisir / cloner / concevoir une voix** → section C
- **D. Paramètres de génération** → `references/parametres.md`
- **E. Générer, assembler, monter, doubler** → `references/montage-et-doublage.md`
- **F. Diagnostic** (« ça sonne robotique ») → vérifie d'abord les 3 pièges, puis le clip de référence, puis les paramètres (`class_temperature` à 0, clip plat, `postprocess_output` qui a supprimé des pauses voulues…), puis le montage.

## A. Annoter un script

Format de sortie :

```
LOT 1 — [intention : ex. « accroche, curieux »]
<texte annoté, prêt à coller>

LOT 2 — [intention]
<texte annoté>
```

Les lignes `LOT …` sont des repères de lecture : précise à l'utilisateur de ne coller que le texte sous chaque en-tête, sinon l'en-tête sera prononcé.

Après les lots, une section **Notes** courte :
- lots à générer plusieurs fois (moments clés) ;
- lots qui gagneraient à utiliser un autre profil de référence (plus énergique, plus posé), si l'utilisateur en a plusieurs ;
- mots à risque de prononciation (sigles, anglicismes, noms propres) avec une correction proposée (voir « Prononciation » dans la référence) ;
- phrases reformulées pour l'oral : dis-le clairement, ne change pas le fond en silence.

Avant de rendre un script annoté, vérifie-le avec le script fourni (voir plus bas). Si l'utilisateur veut un fichier, exporte en **.txt** par défaut.

## B. Convertir depuis ElevenLabs

Applique cette table, puis vérifie avec le script :

| ElevenLabs | VoiceStudio (moteur par défaut) |
|---|---|
| MOT EN MAJUSCULES (emphase) | minuscules + position finale / pause courte / phrase courte ; `[emphasis]…[/emphasis]` en longform |
| `[excited]`, `[whispers]`, `[sad]`… (v3) | supprimer. Énergie : ponctuation + clip de référence animé. Chuchotement : style `whisper` |
| `<break time="1s"/>` | `[pause 1s]` |
| `...` et `!` | inchangés, fonctionnent aussi |
| Rire, soupir implicites | `[laughter]`, `[sigh]` |

Pour la correspondance des réglages (stabilité, similarité, exagération du style, vitesse), vois `references/parametres.md`.

## C. Voix : cloner ou concevoir

**Clonage (recommandé pour le français).**
- Clip de référence de **3 à 10 s** (20 s max si on fournit la transcription).
- Enregistré **sec et près du micro** : l'écho du clip se retrouve dans la voix clonée.
- Fournir la transcription exacte du clip améliore le résultat.
- Choisir un clip dont la diction correspond au ton voulu.

Astuce clé pour la variation : enregistrer **2 ou 3 clips de sa propre voix avec des énergies différentes** (posé, enthousiaste, confidentiel), en faire des profils distincts, puis choisir le profil selon l'intention de chaque lot. Vérifie à l'écoute que le timbre reste cohérent d'un profil à l'autre.

**Consentement.** Ne cloner que sa propre voix ou une voix pour laquelle on a l'autorisation. Si la demande vise la voix de quelqu'un d'autre, propose un Voice Design ou un clip de l'utilisateur lui-même.

**Voice Design (sans clip).** Le moteur par défaut ne comprend qu'un vocabulaire fixe d'attributs. Il ignore les descriptions libres.
- **Genre** : male / female
- **Âge** : child / teenager / young adult / middle-aged / elderly
- **Hauteur** : very low / low / moderate / high / very high pitch
- **Style** : whisper
- **Accent anglais** : american, british, australian, canadian, indian, chinese, korean, japanese, portuguese, russian — seulement si le texte est en anglais
- **Dialectes chinois** : seulement si le texte est en chinois

Traduis toujours une description (« homme jeune, voix grave et charismatique ») en chaîne d'attributs : `male, young adult, low pitch`. Précise ce qui sera ignoré (« charismatique »).

Le Voice Design est entraîné sur l'anglais et le chinois et peut être instable dans d'autres langues. Pour une voix off en français, préfère le clonage. Pour une description libre, le moteur VoxCPM2 l'accepte.

Une fois une prise réussie, **épingler la seed** (« Keep this seed » ou verrouiller le profil depuis l'historique) pour retrouver exactement la même voix.

## Le « secret » : générer par petits lots et multiplier les prises

- Générer lot par lot (1 à 3 phrases), pas tout le script d'un coup.
- La seed n'est pas épinglée par défaut, donc **chaque rendu diffère légèrement**. En local, les prises ne coûtent rien : en générer 2 à 4 par lot important.
- Au montage, choisir la meilleure prise par phrase et **combiner des morceaux de plusieurs prises**. L'assemblage de ces variations imite la parole humaine.
- Nommer les fichiers systématiquement : `lot01_v1.wav`, `lot01_v2.wav`…

Alternative pour les longs scripts : l'onglet **Stories / Audiobook** rend tout le texte d'un coup. Il gère des silences maîtrisés entre lignes et paragraphes, la vitesse par ligne, les balises longform, et l'option **Vary repeated lines**. Détails dans `references/montage-et-doublage.md`.

## Script de vérification

`scripts/verifier_script.py` repère dans un script annoté :
- les mots en majuscules (qui seront épelés) ;
- les balises inconnues (qui seront lues à voix haute) ;
- les balises longform utilisées en mode Voice ;
- les pauses de plus de 10 s ;
- les lots de plus de 4 096 caractères.

```bash
python scripts/verifier_script.py script.txt --mode voice      # page Voice
python scripts/verifier_script.py script.txt --mode longform   # Audiobook / Stories
```

Lance-le sur ta propre sortie avant de la rendre. Corrige ce qu'il signale, ou explique pourquoi un sigle en majuscules est voulu.

## Documentation à jour

VoiceStudio évolue vite (renommé depuis OmniVoice Studio, interface Electron). Si un paramètre ou un menu ne correspond pas à ce que voit l'utilisateur, consulte :
- https://voicestudio.sh/docs
- `docs/expressive-speech.md`, `docs/generation-parameters.md` et `docs/voice-design.md` sur https://github.com/debpalash/VoiceStudio

Ne promets jamais un effet qu'un moteur ne supporte pas.

Réponds dans la langue de l'utilisateur ; annote le script dans la langue du script.
