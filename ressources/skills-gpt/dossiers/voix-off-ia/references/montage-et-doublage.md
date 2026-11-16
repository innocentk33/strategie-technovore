# Montage de la voix off et doublage

Les étapes sont décrites avec Premiere Pro, mais tout logiciel avec une timeline convient (DaVinci Resolve, CapCut, Audacity pour l'audio seul…). Adapte les noms de menus au logiciel de l'utilisateur.

## 1. Assembler les prises

1. Importer toutes les générations dans le projet.
2. Poser les lots dans l'ordre du script sur une seule piste, sans se soucier du timing pour l'instant.
3. Pour chaque phrase avec plusieurs versions : écouter toutes les prises, garder celle qui colle le mieux au contexte.
4. Pour les phrases importantes : **combiner des morceaux de plusieurs versions** (début de la v1, milieu de la v3…). C'est là que le résultat devient le plus humain.

## 2. Rythme et pauses

- Une fois la ligne complète, couper les silences superflus. Astuce : utiliser une deuxième piste pour démarrer la phrase suivante juste à la fin de la précédente, puis ramener sur une piste.
- **Garder ou ajouter des pauses volontaires** sur les moments importants. Couper tous les silences améliore peut-être la rétention, mais rend la voix mécanique.

## 3. Vitesse

- Mieux vaut régler la vitesse **à la génération** (curseur de vitesse de l'outil TTS).
- Si la voix est trop lente ou trop rapide après coup : l'étirement temporel des logiciels de montage déforme souvent la voix (effet « chipmunk » sans conservation de la hauteur, artefacts avec). Solutions : régénérer avec une autre vitesse, ou ajuster le rythme manuellement en raccourcissant/allongeant les pauses plutôt que la voix elle-même.

## 4. Égalisation (rendre la voix plus « pro »)

Avec un égaliseur paramétrique :
1. **Filtre passe-haut** pour couper les basses inutiles (grondements) — souvent autour de 80–100 Hz pour une voix, à ajuster à l'oreille.
2. **Chercher les fréquences qui résonnent** : augmenter fortement une bande étroite, la balayer jusqu'à entendre une résonance désagréable ou un effet « boîte / écho », puis l'atténuer.
3. Ajuster à l'oreille, par petites touches, en comparant avec/sans effet.

Une fois le réglage trouvé, **l'enregistrer en preset** pour l'appliquer à toutes les vidéos et garder un son cohérent.

## 5. Doublage multilingue

L'intérêt : l'essentiel des utilisateurs de YouTube ne parle pas la langue d'origine de la vidéo. Doubler dans quelques grandes langues peut multiplier l'audience potentielle.

### Préparer les pistes
1. Dans la timeline finale, couper tout sauf la voix off → exporter en MP3 (**piste voix**).
2. Faire l'inverse : couper la voix off → exporter la musique et les effets (**piste ambiance**).

### Générer le doublage
3. Dans l'outil de doublage (ex. onglet Dubbing d'ElevenLabs) : langue d'origine, langue cible, envoyer la **piste voix seule**. Envoyer la voix isolée évite que la musique perturbe la transcription et la synthèse.

### Remonter
4. Dans le logiciel de montage, trois pistes :
   - en haut : voix originale (**guide de timing**, sera coupée ensuite)
   - au milieu : voix doublée
   - en bas : piste ambiance
5. Caler la voix doublée sur les visuels en s'aidant de la voix originale.
6. Couper la voix originale, appliquer le même preset d'égalisation à la voix doublée, exporter **l'audio seul**.

### Publier sur YouTube
7. YouTube Studio → **Langues** → choisir la vidéo.
8. Vérifier que YouTube n'a pas déjà créé un doublage automatique dans cette langue ; si oui, le supprimer.
9. Ajouter la langue et envoyer le fichier audio doublé.
10. Traduire aussi **titre et description** dans chaque langue.

### Mesurer
Dans les statistiques YouTube, regarder les vues **par piste audio** plutôt que le total : c'est là que l'effet du doublage devient visible.

Rappelle que les fonctions de YouTube Studio évoluent : si un menu ne correspond pas, vérifie l'interface actuelle (recherche web si disponible).
