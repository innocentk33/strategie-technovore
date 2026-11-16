# Paramètres de génération VoiceStudio

Ces réglages se trouvent dans le panneau **Production Overrides**, disponible sur la page Voice et dans l'onglet Audiobook. Par l'API locale (`http://localhost:3900`), ce sont les mêmes noms de champs.

## Sommaire
1. Correspondance ElevenLabs → VoiceStudio
2. Tous les paramètres utiles
3. Préréglage de départ pour une voix off
4. Faire respirer la voix
5. Autres moteurs

## 1. Correspondance ElevenLabs → VoiceStudio

| Réglage ElevenLabs (méthode d'origine) | Équivalent VoiceStudio | Commentaire |
|---|---|---|
| Stabilité basse | `class_temperature` ↑ (défaut 0, essayer 0,3 à 0,7) ; `position_temperature` (défaut 5,0) | Plus de variation expressive, mais aussi plus d'artefacts (mots mâchés, dérive du timbre). Monter par petites touches. |
| Similarité ~70 % | Qualité du clip de référence + `guidance_scale` (défaut 2,0) | La fidélité au timbre dépend surtout du clip : 3 à 10 s, sec, proche du micro, avec sa transcription. Garder 2,0 et n'ajuster qu'en comparant à l'oreille. |
| Exagération du style ↑ | Aucun paramètre équivalent | Utiliser un clip de référence plus animé : le clonage copie la diction. |
| Vitesse | `speed` (1,0 = normal, >1 plus rapide) ; `[slow]`/`[fast]` en longform ; vitesse par ligne dans Stories | Régler à la génération plutôt qu'au montage. |
| Choix du modèle v2 / v3 | Choix du moteur (Model Catalogue) | Par défaut : OmniVoice. Voir « Autres moteurs ». |
| Régénérations gratuites | Seed non épinglée | Chaque rendu diffère, et en local c'est illimité. |
| — | `num_step` | 16 = rapide (défaut de la page Voice), 32 = plus propre (défaut Audiobook). |
| — | `postprocess_output` | Actif par défaut, supprime les longs silences. |
| — | Seed | Épingler une prise réussie pour la reproduire à l'identique. |

## 2. Paramètres utiles

- **`num_step`**
  - 16 pour tester vite.
  - 32 pour le rendu final.
  - Moins d'étapes donne un son plus rugueux, parfois un peu plus « humain » : à tester, sans en faire une règle.
- **`guidance_scale`** (2,0) : guidage du conditionnement. Rester proche de la valeur par défaut.
- **`class_temperature`** (0 = déterministe) : le principal levier de variation.
- **`position_temperature`** (5,0) : aléatoire sur l'ordre de génération. Rarement besoin d'y toucher.
- **`speed`** : facteur de vitesse. `duration` (durée fixe en secondes) est prioritaire sur `speed` s'il est défini, ce qui est utile pour caler une phrase sur un plan.
- **`postprocess_output`** : le désactiver quand les silences naturels font partie de la performance. Les `[pause]` balisées ne sont pas concernées.
- **Seed** : non épinglée par défaut. L'historique affiche la seed de chaque prise ; « Keep this seed » ou le verrouillage du profil la fixe. L'onglet Audiobook accepte une seed globale.
- **Style / instruct** : sur le moteur par défaut, seulement les attributs du Voice Design. Le seul style de diction est `whisper`. Si le style et le clip se contredisent, c'est le clip qui gagne.

Le moteur produit du 24 kHz mono, avec une chaîne de mastering automatique (filtre passe-haut + compresseur).

## 3. Préréglage de départ pour une voix off

À présenter comme un point de départ à tester sur un lot, pas comme une vérité :

- **Moteur** : OmniVoice par défaut, avec un profil cloné à partir d'un clip animé.
- **`num_step`** : 32
- **`guidance_scale`** : 2,0
- **`class_temperature`** : générer le même lot à 0, 0,3 et 0,5, puis choisir à l'oreille.
- **`speed`** : 1,0 à 1,1 selon le débit naturel de la voix.
- **`postprocess_output`** : actif, sauf si le script repose sur des silences non balisés.
- **Seed** : non épinglée pendant la phase de prises multiples ; épinglée pour refaire une prise précise.

## 4. Faire respirer la voix (moteur par défaut)

Il n'y a pas de balise `[breath]` sur le moteur par défaut. Voici la méthode de contournement, dans l'ordre d'efficacité :

1. **Mettre les respirations dans le clip de référence** : 8 à 15 s avec des inspirations audibles entre les phrases. Le clone reprend cette diction.
2. **Écrire des fragments courts avec des pauses** : `Je peux pas... [pause 300ms] je peux plus...`
3. **Désactiver `postprocess_output`**, pour ne pas couper les silences où se trouvent les respirations.
4. **Monter `class_temperature` à 0,3–0,7** et générer plusieurs prises.
5. **Garder la meilleure** et épingler sa seed.

C'est un contournement : l'aléatoire qui produit une belle respiration produit aussi des mots mal articulés. Pour des respirations placées précisément, utiliser CosyVoice 3.

## 5. Autres moteurs (à installer, optionnels)

- **CosyVoice 3**
  - Balises `[breath]` et `[laughter]`, emphase `<strong>mot</strong>`.
  - Instructions en langage naturel (« parle comme quelqu'un d'épuisé »), actuellement seulement via l'API.
  - Installation non triviale.
- **IndexTTS2**
  - Seul moteur avec des émotions graduées : 8 émotions (joyeux, en colère, triste, effrayé, dégoûté, mélancolique, surpris, calme), un clip d'émotion de référence, ou une description d'émotion avec un curseur d'intensité.
  - Réglable dans l'onglet Audiobook ou via l'API `/ws/tts`.
- **VoxCPM2**
  - Instruction en préfixe dans le texte : `(parle vite, essoufflé) Je peux pas m'arrêter.`
  - Accepte aussi une description libre en Voice Design.
  - L'adhérence varie selon la voix et la langue.
- **OmniVoice GGUF** : même modèle, quantifié, pour les petites cartes graphiques (moins de 6 Go de VRAM) ou le CPU.

Les balises non verbales `[laughter]` et `[sigh]` sont propres au moteur par défaut (CosyVoice 3 a aussi `[laughter]`) : ne pas les supposer disponibles sur les autres moteurs.
