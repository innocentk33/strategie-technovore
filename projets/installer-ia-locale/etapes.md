# Pourquoi avoir ta propre IA, et comment l'installer : les étapes jusqu'à la sortie

> Écrit le 24/10/2026. Sortie : **lun. 2 nov., 18 h**. Déjà fait : fiche, recherche, sources vérifiées deux fois, script V1, grill, [script final](script.md). Reste tout ce qui se passe chez toi. Si la semaine déraille, le pseudo (joker) prend le 2 nov. (`calendrier.md`, S2).

Coche au fur et à mesure.

## 0. Avant la capture (sam. 24 – dim. 25 oct.)

Tes décisions, celles des « Questions pour l'auteur » en bas du [script](script.md) :

- [ ] Le hook : d'accord pour que « le gouvernement américain l'a exigé » et « dix-neuf jours plus tard » arrivent après 0:22 ? (question 1)
- [ ] « Bah, tu la fais tourner chez toi, comme celle-là », ou l'autre formule (question 2)
- [ ] Le 12 juin t'a-t-il touché, et à quelle fréquence tu utilises Claude (question 3, crochet de la section 1)
- [ ] Tes essais sur la 5080 seront-ils finis le jour de la voix (question 4, crochet de la section 3)
- [ ] AVX2 : on le montre ou pas (question 7). Sans méthode vérifiée, on coupe.
- [ ] Ton sous-texte, ou celui de la fiche (« ce que tu ne possèdes pas, on peut te le retirer »)

Préparer la machine :

- [ ] Enregistrer en PDF les conditions de LM Studio (`lmstudio.ai/terms`, version du 23/08/2026) **avant** de couper le wifi ; relire le passage sur la résiliation (« trade secret », F17) et noter ta question avec ses mots anglais
- [ ] Copier les seules sections licence et résiliation dans un `.txt` (plan B, cas B)
- [ ] Désinstaller LM Studio s'il est déjà là, pour filmer une vraie première installation
- [ ] Fermer les applis et documents de travail, couper les notifications, aucune clé d'API visible, navigateur sans favoris perso
- [ ] Un chronomètre prêt (il décide du « 10 minutes » du titre)

## 0 bis. Les tests (une répétition, sans filmer, ~1 h 30)

Sur le PC de la 5080, avant la capture. Le but : connaître les réponses avant de filmer, pour ne pas découvrir un problème pendant la prise. Note tout dans un fichier `tests.md` de ce dossier, avec la date et la version de LM Studio : chaque résultat remplit un crochet du script ou confirme un fait de `sources.md`.

1. **Le réseau.** Ton PC est-il en wifi ou en câble ? Trouve le geste qui coupe internet en un clic et qui se voit à l'écran (l'icône du wifi, le mode avion, ou le câble débranché avec l'icône réseau barrée). Vérifie qu'un site ne charge plus. → Le motif du hook et de la section 4 ; si c'est un câble, on change « je coupe le wifi » dans le script.
2. **Le site.** `lmstudio.ai` propose-t-il toujours le seul bouton Bionic, et `lmstudio.ai/download` a-t-il toujours le 2e bloc « Download LM Studio » ? Version affichée (0.4.26 ou plus) et taille de l'installateur. → Le piège de la section 2 (F19, F23).
3. **L'installation.** Lance le chrono à l'ouverture de `lmstudio.ai/download`, et mets-le en pause pendant les téléchargements. Note chaque écran : un compte demandé ou pas, Bionic proposé ou pas, un modèle proposé d'office ou pas, et ce que montre le premier lancement. → Les deux crochets de la section 2.
4. **La recherche.** Le raccourci ⌘2 / Ctrl+2 ouvre-t-il bien la recherche des modèles ? Tape « gemma 4 » : regarde si un modèle « uncensored » ou « abliterated » apparaît dans la liste (il faudra recadrer). → F26, F40.
5. **L'indicateur.** À côté de Gemma 4 E4B et de Gemma 4 12B : le texte exact de l'indicateur, mot pour mot, et sa couleur. Regarde aussi un modèle trop gros pour 16 Go, pour voir l'avertissement. → Crochet de l'indicateur (F28, F29, H14). Ne cite rien qui n'est pas à l'écran.
6. **Les tailles.** Les tailles affichées pour E4B (5,9 Go au catalogue ?) et 12B (7,4 Go ?), et le dépôt (Google ou `lmstudio-community`). → Les cartes 8/16 Go (F34-F36).
7. **Le téléchargement.** Télécharge E4B : combien de temps, à quelle vitesse de connexion. → Le calcul en surimpression (F39).
8. **La première réponse.** Charge le modèle, pose une question que ton public poserait. **Arrête le chrono** à la réponse. L'appli affiche-t-elle une vitesse en tokens/s ? Note le chiffre. → Le « 10 minutes » du titre (hors téléchargement) et le crochet de la vitesse (H15) ; s'il n'y a pas de vitesse, on coupe le crochet.
9. **Hors ligne.** Coupe le réseau (geste du test 1), pose une question. LM Studio répond-il sans rien demander (pas de connexion, pas de vérification de compte) ? Relance l'appli wifi coupé : elle démarre toujours ? → La preuve de la vidéo, au hook et en section 4.
10. **Le document.** Toujours hors ligne : joins le PDF des conditions de LM Studio, pose ta question avec les mots anglais du passage sur la résiliation. Il trouve le passage ? Il lit tout ou il passe en « passages utiles » (RAG) ? S'il rate, refais avec le `.txt` court. → Choisit le plan B (A, B ou C) **avant** la capture (F30, F17).
11. **Sans carte graphique** (option). Dans les réglages, mets le déchargement GPU à zéro, recharge E4B, pose la même question : ça marche ? À quelle vitesse, à l'œil et en tokens/s ? → Le crochet du test sans carte graphique ; sans test, la phrase est coupée (F21).
12. **Sur la 5080.** Le plus gros modèle que tu prendrais, toi, sur 16 Go : ce que dit l'indicateur, et sa vitesse. → Le crochet des tailles (section 3) ; ça ne remplace pas les essais de Claude #1.

Ne teste pas 8 Go de VRAM : tu n'en as pas, la carte « 8 Go » reste **calculée** d'après le catalogue, et sa légende le dit.

**Après la répétition**, pour que la capture montre une vraie première installation : supprime le modèle dans LM Studio (onglet des modèles), désinstalle l'appli, et vérifie que le dossier des modèles est vide. Le PDF et le `.txt` restent hors de ce dossier.

## 1. La capture (lun. 26 – mar. 27 oct.)

Une seule session, dans l'ordre du script. Chrono lancé à l'ouverture de `lmstudio.ai/download`, arrêté à la première réponse, **téléchargements non comptés**. Note au fur et à mesure ce que tu vois : ça remplit les crochets.

| # | Plan | Pour le crochet / la section |
|---|---|---|
| 1 | `lmstudio.ai` : le bouton unique « Download LM Studio Bionic » | Section 2, le piège |
| 2 | On tape `lmstudio.ai/download`, le 2e bloc ; la page des configurations requises | Section 2 |
| 3 | Chaque écran de l'installation, version visible (0.4.26 ou plus) | Crochet : un compte ? Bionic proposé ? un modèle d'office ? |
| 4 | Le premier lancement | Crochet : ce que tu vois, en une phrase |
| 5 | (option) GPU désactivé dans les réglages : ça tourne, à quelle vitesse | Crochet du test sans carte graphique, sinon on coupe |
| 6 | ⌘2 / Ctrl+2, « gemma 4 » ; **seulement les dépôts officiels** (Google, `lmstudio-community`), recadre si un « uncensored » ou « abliterated » apparaît | Section 3 |
| 7 | L'indicateur de compatibilité en gros plan ; note-le **mot pour mot**, avec sa couleur | Crochet de l'indicateur |
| 8 | Les tailles affichées (Gemma 4 E4B 5,9 Go, 12B 7,4 Go ?) et le plus gros modèle que tu prends sur la 5080 | Crochet des tailles |
| 9 | Le bouton de téléchargement et **toute** la barre (elle sert de fond pendant 1 min 20) | Section 3, pendant le téléchargement |
| 10 | Le modèle qui se charge, la discussion, ta 1re question (une question de ton public, pas du code), la vitesse en tokens/s → **stop chrono** | Section 4 |
| 11 | Le clic sur l'icône du wifi qui se barre, une question, la réponse, **sans coupe** | Section 4 **et** le hook (même cadrage : ce plan peut servir aux deux) |
| 12 | Wifi toujours coupé : le PDF joint, ta question, la réponse. **Plan B décidé maintenant** (A : il se trompe, on le garde ; B : refaire sur le `.txt` ; C : pas de document, on coupe) | Section 4, le document |

Captures web (le wifi revenu) : le communiqué d'Anthropic du 12/06/2026 (date visible), l'article de Simon Willison du 08/08/2025, le billet « free for work » (08/07/2025), `ollama.com` sans compte connecté, le passage des conditions de LM Studio.

## 2. Le texte final (mar. 27 oct.)

- [ ] Remplir tous les `[CROCHETS]` du [script](script.md) avec ce que tu as noté
- [ ] Choisir le titre : « en 10 minutes » seulement si ton chrono le tient hors téléchargement, et la phrase de la section 3 le dit
- [ ] Repasser le grill, variante storytelling, sur le hook et tes crochets : test des 30 secondes, liaisons (le script est à 2,3 pour 100 mots, garde-les au-dessus de 1,5), aucun « vous »
- [ ] `teleprompteur.md` et `.txt` : une ligne = un souffle, sans les `[VISUEL]`, `[SON]` ni indications

## 3. La voix (mer. 28 oct.)

- [ ] Enregistrer au SM7B, énergie selon les notes de montage (rapide au hook, posée en section 1, montées à 1:59, 6:34 et 6:54)
- [ ] `ressources/voix/sm7b.sh prise.wav voix-off-montee.wav` (-16 LUFS)
- [ ] Garder un `.m4a` dans le dossier (les `.wav` ne sont pas versionnés)

## 4. Le montage (mer. 28 – ven. 30 oct.)

- [ ] `storyboard.md` calé sur `voix-off-montee.wav` (en HyperFrames : `data-start` = le timecode en secondes)
- [ ] Les composants, construits une fois (ils resserviront le 7 déc. et le 8 févr.) : les trois cases, le schéma « fichier + appli », les deux cartes 8/16 Go façon sélection de personnage, la jauge VRAM
- [ ] Charte verte « IA chez moi », police mono pour les adresses et les noms de modèle
- [ ] **Les 15 premières secondes d'abord**, et vérifiées : wifi coupé + Fable 5 coupé pour tout le monde, rien d'autre
- [ ] Aucune coupe entre le wifi barré et la réponse (c'est la preuve)
- [ ] La vidéo commence sur la scène de la miniature b
- [ ] Écran de fin 20 s : *OpenCode* jusqu'au 16 nov.
- [ ] Revoir la vidéo en entier : rien d'interdit à l'écran (clé, modèle « uncensored », document de travail, lien tiers)

## 5. Les trois miniatures (en parallèle, mer. 28 – ven. 30 oct.)

Charte de la série : **vert**, donc b sert de miniature par défaut. Piste de la fiche : l'icône du wifi barrée et une bulle qui répond quand même ; texte « HORS LIGNE » ou « COUPÉ ? », sans répéter le titre ; ni logo d'Anthropic, ni annonce de Fable 5.

- [ ] 10 à 15 références dans `miniature/refs/`
- [ ] Concept et brief avec `/youtube thumbnail`
- [ ] Maquette `miniature/propositions/miniature.html?v=a|b|c` : a (noir) et b (vert) **exactement la même scène**, c hors niche (note la chaîne et la vidéo d'origine dans `propositions.md`)
- [ ] Critique avec `/coach-miniature-youtube`, corrections, test des 50 %
- [ ] Rendu 4K et PSD (`photocraft/`)

## 6. Le kit d'upload (ven. 30 oct.)

- [ ] `upload.md` : mots-clés vidIQ (ia en local, installer ia en local, lm studio, ollama), chapitres tirés du storyboard, description avec `lmstudio.ai/download → 2e bloc` et les sources
- [ ] Sous-titres `installer-ia-locale.fr.srt` et `.en.srt`
- [ ] Section « Suggestions » : 4 ou 5 vidéos françaises du mois sur le sujet (dont *Adieu le cloud pour les LLM ! Vive le local*, Le Lab IA), leurs miniatures dans `miniature/hotes/`, la planche (`planches.py --suggestions`), la comparaison à 168 px, l'enchaînement

Les crédits vidIQ sont encore pleins jusqu'au 12/11 : pas besoin de les économiser ici.

## 7. Programmer (sam. 31 oct.)

- [ ] Rendu final, upload, titre, description, chapitres, sous-titres, tags
- [ ] « Tester et comparer » avec a, b et c
- [ ] Programmée **lun. 2 nov., 18 h**
- [ ] `README.md` et `calendrier.md` : statut **Programmé**
- [ ] Dim. 1er nov. : marge

## 8. Après la sortie

- [ ] Lun. 2 nov. : statut **Publié** avec le lien, dans le README et le calendrier ; puis le radar (`CLAUDE.md`), qui regarde Uber à J+7
- [ ] Lun. 9 nov. : cette vidéo à J+7 au radar suivant (rétention à 0:15, cible 75 %, et à 1:00, cible 50 %) ; capture de Studio pour le CTR et le gagnant du test
- [ ] Lun. 16 nov. : carte YouTube vers Claude #1 à 6:15, écran de fin vers Claude #1
- [ ] Lun. 7 déc. : carte YouTube vers *IA en local : comment lire le nom d'un modèle* à 4:07

## En parallèle cette semaine

Lun. 26 : **Uber sort**. Le radar se fait ce jour-là (il regarde ArtCraft à J+7), plus les tâches d'audit de S2 : 2 ou 3 miniatures d'Uber en test, les écrans de fin vers Uber, la page de chaîne. Et le script de Claude #1 avec les résultats des essais.
