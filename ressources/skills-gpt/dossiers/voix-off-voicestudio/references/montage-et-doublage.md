# Génération, montage et doublage avec VoiceStudio

## 1. Deux façons de générer

**Page Voice (lot par lot).** Idéale pour la méthode des prises multiples.
- Coller un lot, générer 2 à 4 fois (la seed non épinglée donne une prise différente à chaque fois), télécharger chaque prise, passer au lot suivant.
- Changer de profil de référence selon l'intention du lot si l'utilisateur en a plusieurs.
- Les balises longform ne fonctionnent pas ici.

**Onglet Stories / Audiobook (script entier).** Pratique pour une première version complète ou un long script.
- Accepte `[slow]`, `[fast]`, `[emphasis]`, `[voice:NOM]`, une vitesse globale et une vitesse par ligne.
- Gère les jointures :
  - « Trim engine silence » coupe le silence ajouté par le moteur ;
  - « Gap between lines » ajoute un silence entre les lignes (250 ms par défaut) ;
  - « Gap between paragraphs » ajoute un silence aux lignes vides (350 ms).
- Une `[pause]` explicite remplace l'écart entre lignes au lieu de s'y ajouter.
- « Vary repeated lines » donne une prise différente aux lignes identiques.
- Chaque chapitre peut être pré-écouté.

Approche mixte conseillée :
1. Rendre tout le script dans Stories pour avoir une base.
2. Régénérer les moments clés sur la page Voice avec plusieurs prises.
3. Remplacer ces passages au montage.

## 2. Assembler les prises (Premiere Pro, DaVinci, CapCut…)

1. Importer toutes les prises et les poser dans l'ordre du script sur une piste.
2. Pour chaque phrase, écouter les versions et garder celle qui colle au contexte.
3. Pour les phrases importantes, **combiner des morceaux de plusieurs prises**. C'est là que le résultat devient le plus humain.
4. Couper les blancs superflus, en **gardant des pauses volontaires** sur les moments importants.

## 3. Vitesse

- Régler `speed` à la génération plutôt qu'au montage : l'étirement temporel des logiciels de montage déforme souvent la voix.
- Pour caler une phrase sur une durée précise, utiliser le paramètre `duration`.
- En dernier recours, ajuster le rythme en jouant sur les pauses plutôt que sur la voix.

## 4. Égalisation

VoiceStudio applique déjà un **filtre passe-haut et un compresseur** à chaque rendu (24 kHz mono). Au montage :
- Pas de gros passe-haut supplémentaire : vérifier d'abord à l'oreille.
- Chercher les résonances désagréables : augmenter fortement une bande étroite, la balayer, puis atténuer la fréquence gênante.
- Éviter les préréglages d'effet qui ajoutent de la réverbération (Cinematic, Warm) pour une voix off, sauf si c'est voulu.
- Un clip de référence enregistré dans une pièce qui résonne donne une voix clonée qui résonne. Il vaut mieux réenregistrer le clip que corriger au montage.
- Enregistrer le réglage final en preset pour garder un son cohérent d'une vidéo à l'autre.

## 5. Doublage (espace « Dub » intégré)

VoiceStudio a son propre atelier de doublage : pas besoin de passer par ElevenLabs.

**Préparer**
1. Ouvrir Dub, importer la vidéo, l'audio, ou une URL.
2. La transcription se fait automatiquement.
3. Choisir le fournisseur de traduction dans Settings > Models > Translation.

**Traduire et relire**
4. Choisir une ou plusieurs langues cibles et traduire.
5. **Relire la traduction** segment par segment : c'est le point le plus important pour un rendu naturel.

**Régler les voix et le timing**
6. Attribuer une voix par locuteur. L'attribution automatique est active par défaut. Pour garder sa propre voix, choisir son profil cloné.
7. Chaque segment peut avoir son volume, sa vitesse et une note de direction.
8. La timeline permet de déplacer et redimensionner les segments, et signale les chevauchements.

**Générer et contrôler**
9. Générer. Vérifier les segments manquants ou en échec, et les dépassements de timing, avant d'exporter.
10. Si une traduction est trop longue, le mode de calage (Strict Slot) l'accélère en conservant la hauteur, ce qui peut sonner précipité. Dans ce cas, **raccourcir la traduction** plutôt que d'accélérer la voix.

**Exporter**
11. Choisir la piste, le format et le mixage avec la musique et les effets d'origine.
12. Pour YouTube, exporter l'**audio seul** de la piste doublée.

Variante pour plus de contrôle : exporter soi-même, depuis le logiciel de montage, une piste voix seule et une piste musique/effets. Doubler la piste voix, puis remonter trois pistes (voix originale comme guide de timing, voix doublée, ambiance) avant d'exporter.

**Publier sur YouTube**
1. YouTube Studio → **Langues** → choisir la vidéo.
2. Supprimer le doublage automatique de YouTube s'il existe pour cette langue.
3. Ajouter la langue et envoyer le fichier audio.
4. Traduire le titre et la description.
5. Dans les statistiques, regarder les vues **par piste audio** pour mesurer l'effet du doublage.

Les menus de VoiceStudio et de YouTube Studio évoluent. En cas d'écart avec l'interface, vérifier la documentation actuelle.
