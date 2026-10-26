# Pourquoi avoir ta propre IA, et comment l'installer : les étapes jusqu'à la sortie

> Écrit le 24/10/2026. Sortie : **lun. 2 nov., 18 h**. Déjà fait : fiche, recherche, sources vérifiées deux fois, script V1, grill, script V2, ta capture (24/10) et le [script](script.md) V3 recalé dessus (25/10). Reste la voix, le montage, les miniatures et le kit d'upload. Si la semaine déraille, le pseudo (joker) prend le 2 nov. (`calendrier.md`, S2).

Coche au fur et à mesure.

## 0 et 1. Les tests et la capture : faits le 24/10

Ta capture : `D:\_Technovore\Youtube\Pourquoi avoir ta propre IA, et comment l'installer (LM Studio)\installation lm studio et test avec gemma 4.mp4` (11 min 39, Windows, LM Studio 0.4.26). On n'en garde que l'installation, Gemma 4 12B QAT, les trois tests (le mème Macron, Dr Stone hors ligne, le message louche avec et sans Think) et internet coupé. Le [script](script.md) a été recalé dessus le 25/10 (V3) ; ses plans, avec les timecodes de la capture, sont dans sa section « Plans de ta capture ».

Tombés avec la capture : le PDF des conditions de LM Studio et son plan B, AVX2, le test sans carte graphique, le chrono (13 min en tout d'après ta barre des tâches, dont 4 de téléchargement : pas de « 10 minutes » dans le titre), les tokens par seconde.

Tes décisions, dans les « Questions pour l'auteur » en bas du [script](script.md) :

- [x] Internet coupé après le test 1 : le script suit cet ordre (25/10)
- [x] Le message du test 3 et `sidedeouf.fr` sont inventés : la voix le dit (25/10). Revérifie la veille de la sortie que le domaine n'existe toujours pas
- [x] La coupure : Chrome reste sur « Ce site est inaccessible » à chaque actualisation, ça suffit comme preuve (25/10)
- [x] La demi-phrase sur Bionic : gardée (25/10)
- [x] Les réponses des tests 1 et 2 sont justes (25/10)
- [x] La fin : pas personnelle, l'usage hybride (le local pour le perso, en ligne pour le reste), écrite le 25/10
- [ ] Captures web à faire, connexion revenue : le communiqué d'Anthropic du 12/06/2026 (date visible), l'article de Simon Willison du 08/08/2025, la page des configurations requises, le billet « free for work » (08/07/2025), `ollama.com` sans compte connecté

## 2. Le texte final (mar. 27 oct.)

- [ ] Remplir les `[CROCHETS]` du [script](script.md) qui restent (plus aucun depuis le 25/10)
- [x] Grill storytelling de la V3 fait le 25/10 : [`grill-v3.md`](grill-v3.md), 8/10. Reste à appliquer son plan d'action (la fin, le test 3, la section 3, le hook, les « Et » de tête), puis à régénérer le téléprompteur
- [ ] `teleprompteur.md` et `.txt` : une ligne = un souffle, sans les `[VISUEL]`, `[SON]` ni indications. **V2 faite le 25/10** ([`teleprompteur.md`](teleprompteur.md)), calée sur la capture, tes réponses du 25/10 reportées, plus aucun ⟦…⟧ ; si tu retouches le `.md`, régénère le `.txt`

## 3. La voix (mer. 28 oct.)

- [ ] Enregistrer au SM7B, énergie selon les notes de montage (rapide au hook, posée en section 1, montées à 6:48 et 7:50)
- [ ] `ressources/voix/sm7b.sh prise.wav voix-off-montee.wav` (-16 LUFS)
- [ ] Garder un `.m4a` dans le dossier (les `.wav` ne sont pas versionnés)

## 4. Le montage (mer. 28 – ven. 30 oct.)

- [ ] `storyboard.md` calé sur `voix-off-montee.wav` (en HyperFrames : `data-start` = le timecode en secondes)
- [ ] Les composants, construits une fois (ils resserviront le 7 déc. et le 8 févr.) : les trois cases, le schéma « fichier + moteur », les deux cartes 8/16 Go façon sélection de personnage, la jauge VRAM
- [ ] Charte verte « IA chez moi », police mono pour les adresses et les noms de modèle
- [ ] **Les 15 premières secondes d'abord**, et vérifiées : internet coupé (Google « inaccessible ») + la réponse + Fable 5 coupé pour tout le monde, rien d'autre
- [ ] Aucune coupe entre l'onglet Google « inaccessible » et la réponse sur Dr Stone (c'est la preuve) ; le doublon 8:00-9:10 de la capture coupé
- [ ] La vidéo commence sur la scène de la miniature b
- [ ] Écran de fin 20 s : *OpenCode* jusqu'au 16 nov.
- [ ] Revoir la vidéo en entier : rien d'interdit à l'écran (clé, modèle « uncensored », document de travail, lien tiers)

## 5. Les trois miniatures (en parallèle, mer. 28 – ven. 30 oct.)

Charte de la série : **vert**, donc b sert de miniature par défaut. Piste corrigée le 25/10 dans la [fiche](fiche.md) : la page « Ce site est inaccessible » en fond, désaturée, et la réponse de Gemma qui s'écrit par-dessus, en grand ; texte « HORS LIGNE » ; c'est aussi le premier plan de la vidéo. c, hors niche : le piège du test 3, façon chaîne de « scam baiting » (le faux message cerclé de rouge, « IL TOMBE DEDANS ? »). Ni logo de Google ou d'Anthropic, ni annonce de Fable 5.

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
- [ ] Lun. 16 nov. : carte YouTube vers Claude #1 à 5:40, écran de fin vers Claude #1
- [ ] Lun. 7 déc. : carte YouTube vers *IA en local : comment lire le nom d'un modèle* à 4:16

## En parallèle cette semaine

Lun. 26 : **Uber sort**. Le radar se fait ce jour-là (il regarde ArtCraft à J+7), plus les tâches d'audit de S2 : 2 ou 3 miniatures d'Uber en test, les écrans de fin vers Uber, la page de chaîne. Et le script de Claude #1, calculé à partir des mesures publiées (plus d'essais depuis le 25/10).
