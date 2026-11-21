---
paths:
  - "projets/**/voicestudio*"
  - "projets/**/teleprompteur*"
  - "ressources/voix/prononciations.md"
---

# Écrire un texte pour la voix de synthèse (VoiceStudio)

Ces règles valent pour **tout agent** (Claude, GPT, Gemini…) qui prépare un texte destiné à une voix de synthèse : aujourd'hui VoiceStudio, avec la voix clonée de l'auteur (moteur OmniVoice). Le but est que le moteur dise le texte **comme l'auteur le dirait**, sans changer le fond.

## Entrée et sortie

- **Entrée** : `projets/<nom>/teleprompteur.md`, la version finale et grillée. Ne réécris pas le fond. Si une phrase te paraît poser problème, signale-la à l'auteur au lieu de la changer en silence.
- **Sorties**, dans le dossier du projet :
  - `voicestudio.txt` : le texte en lots. Chaque lot commence par une ligne d'en-tête `LOT <n> — <intention>` (par exemple « hook, énergique »), qui n'est pas lue : l'auteur colle seulement le texte dessous.
  - `voicestudio-stories.txt` : le même texte sans les en-têtes, pour un rendu complet. Fabrique-le à partir de `voicestudio.txt`, par exemple avec `grep -v -E "^LOT [0-9]+" voicestudio.txt | cat -s`.
  - `voicestudio.md` : les notes (prononciations choisies, lots à faire en plusieurs prises, lots de prix).
- Ne modifie ni `teleprompteur.md` ni `teleprompteur.txt`.

## Les règles d'écriture

### 1. Aucune pause

- Pas de balise de pause (`[pause]`, `[pause 500ms]`).
- Pas de points de suspension (`...` ou `…`) : remplace-les par une virgule.

Les silences se posent au montage.

### 2. Mise en forme

- **Une phrase par ligne**, et une ligne vide entre deux lots. Recolle les lignes du téléprompteur, qui coupent souvent les phrases en deux.
- **Un lot = 1 à 3 phrases.** Un moment fort (hook, révélation, chute, phrase finale) forme un lot à lui seul, pour pouvoir en faire plusieurs prises.
- **Les phrases qui contiennent un prix vont dans leurs propres lots**, avec « (à relire le JJ/MM) » dans l'en-tête : on peut ainsi les regénérer seules si un prix change.

### 3. Pas de majuscules sauf les sigles

Le moteur **épelle** tout mot écrit en capitales.
- Garde les capitales pour les sigles que l'auteur épelle : RTX, RX, AMD, LDLC, ATX, TVA, PC, IA, AI.
- Écris en minuscules ce qui se prononce comme un mot : Nvidia, Intel, Gigabyte.
- N'utilise jamais les majuscules pour l'emphase : l'emphase vient du mot fort placé en fin de phrase.

### 4. Tous les nombres en toutes lettres

Prix, dates, quantités, pourcentages, références de cartes : « deux mille huit cents euros », « trente et un virgule quatre », « le vingt novembre ».

### 5. La prononciation s'écrit comme elle se dit

Le moteur rate les liaisons et les finales qui changent selon le mot suivant : écris le son, pas l'orthographe.

- **« plus »**
  - sans le s : « plus de 3 » → « plu de trois », « plu chère », « ne compile plu » ;
  - avec la liaison : « plus épaisses » → « plu zépaisses » ;
  - avec le s qui s'entend : « de pluss », « en pluss ».
- **Chiffres dont la finale tombe devant une consonne** : « si millions », « hui gigas », « hui broches », « vin novembre », « cent vingt-hui mille ».
- **Nombre suivi de « euros »**, avec la liaison : « hui cent zeuros », « quatre cent zeuros », « quatre-vingt zeuros », « mille quatre cent quatre-vingt-troi zeuros ».
- **Liaisons obligatoires** : « les zautres », « ses zoutils », « tes zapplis », « deu zans », « du troi zau cinq », « on na vu », « en noccasion », « tou ten bas ».
- **Liaison en « n » devant « un »** : elle s'écrit avec une apostrophe : « en n'un mois ». « D'un » reste tel quel.
- **Liaisons facultatives** : ne les écris pas (« pas encore », « c'est avant »). Le ton reste parlé, comme celui de l'auteur (« t'as », « si t'es malin »).

### 6. Conventions de l'auteur (21/11)

| Écrit | Pour le moteur |
|---|---|
| Numéro de carte à 4 chiffres | **toujours en milliers**, jamais en deux moitiés (21/11) : 5060 = « cinq mille soixante », 5090 = « cinq mille quatre-vingt-dix », 3060 = « trois mille soixante », 9060 = « neuf mille soixante », 9700 = « neuf mille sept cent » |
| Ti | té i (« RTX cinq mille soixante té i ») |
| XT | ix té |
| 9060 XT | neuf mille soixante ix té |
| R9700 | èr neuf mille sept cent |
| ASUS | azus |

`ressources/voix/prononciations.md` montre comment l'auteur dit chaque carte dans ses reprises. Certaines reprises anciennes sont en deux moitiés (« cinquante soixante », « trente soixante ») : pour un texte de synthèse, c'est la règle des milliers ci-dessus qui s'applique. Tout autre nom propre ou anglicisme dont tu n'es pas sûr (Qwen, llama.cpp, Hugging Face, CUDA) : propose une graphie et note-la dans `voicestudio.md`, pour que l'auteur la valide à l'écoute.

**Quand l'auteur donne une nouvelle convention**, ajoute-la au tableau ci-dessus, avec sa date.

### 7. Sons non verbaux

Seules deux balises sont reconnues par le moteur : `[laughter]` (rire) et `[sigh]` (soupir). N'en mets **pas plus de deux dans tout le script**, et signale-les dans les notes : l'auteur décide s'il les garde.

Toute autre balise sera **lue à voix haute**, par exemple `[excited]`, `[whispers]`, `[breath]` ou la balise SSML `<break>`.

## Vérification avant de rendre

1. Lance `grep -n -E "\[pause|\.\.\.|…|[0-9]" voicestudio-stories.txt`. Il doit ne rien trouver.
2. Cherche les mots en capitales : `grep -n -o -E "\b[A-ZÉÈÀ]{2,}\b" voicestudio-stories.txt | sort -u`. Il ne doit rester que les sigles voulus.
3. Relis en entier une fois, à voix haute dans ta tête : chaque « plus », chaque nombre suivi d'« euros », chaque mot qui commence par une voyelle après « les », « des », « ses », « un », « en » ou « on ».
4. Si tu changes `voicestudio.txt`, refais `voicestudio-stories.txt`.

Exemple de référence : `projets/deux-cartes-occasion/voicestudio.txt`. Il a été écrit le 20/11, **avant** les conventions du 21/11 : il contient encore « Ti », « Asus », « nun » et « R quatre-vingt-dix-sept cents ». Ne le recopie pas tel quel.
