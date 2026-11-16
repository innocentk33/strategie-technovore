# Tester une miniature

Trois niveaux, du plus rapide au plus fiable.

## 1. Planche d'aperçu (script local)

`scripts/apercu_miniature.py` (dépendance : Pillow ; chemins relatifs au dossier du skill).

```bash
# Une miniature, avec son titre
python3 scripts/apercu_miniature.py mini.jpg --titre "Titre de la vidéo" --sortie apercu/

# Deux ou trois versions à comparer (titres dans le même ordre)
python3 scripts/apercu_miniature.py v1.png v2.png --titre "Titre A" "Titre B" --sortie apercu/

# Avec les miniatures concurrentes autour, et le nom de la chaîne
python3 scripts/apercu_miniature.py mini.jpg --contexte concu1.jpg concu2.jpg --chaine "Ma chaîne"
```

Fichiers produits :
- `planche_<nom>.png` : grille des tiers et zone de la durée sur l'image, rendus aux tailles réelles (360, 300 et 168 pixels de large, avec le badge de durée), niveaux de gris, version floutée, palette dominante, mesures et alertes.
- `accueil_clair.png` et `accueil_sombre.png` : la miniature au milieu d'une page d'accueil simulée. Les voisines sont les images passées avec `--contexte`, sinon des blocs neutres. Avec de vraies miniatures concurrentes, le test est bien plus parlant.
- `comparaison.png` : les versions côte à côte aux petites tailles (si plusieurs images).
- `metriques.json` : toutes les mesures.

Comment lire les mesures :
- **Contraste de valeurs** (écart-type de la luminosité, 0 à 0,5) : en dessous de 0,17 environ, l'image paraît terne. Une image très contrastée n'est pas forcément lisible pour autant : regarder la version en niveaux de gris.
- **Pourtour quasi blanc / quasi noir** : au-delà de 50 %, la miniature se fond dans l'interface du mode correspondant.
- **Familles de couleurs vives** : 4 ou plus suggère une palette dispersée.
- **Détails sous la durée** : densité de contours dans la zone du badge ; élevée = quelque chose y est peut-être caché.
- **Zones les plus chargées** : densité de contours par case de la grille. Utile pour voir où se concentre le détail ; les photos texturées donnent des valeurs plus élevées partout, donc comparer les cases entre elles plutôt qu'à un seuil.

Ces mesures orientent le regard. Le jugement se fait en regardant les rendus en petit et la page d'accueil simulée.

Si le script ne peut pas tourner (pas de Python, pas de fichier), décris à l'utilisateur comment faire le test lui-même : réduire l'image à 168 pixels de large, la regarder une seconde, puis la passer en noir et blanc.

## 2. Simulateur de page d'accueil en ligne

Des outils comme thumbsup.tv (cité par Isaac) placent la miniature et le titre dans une fausse page YouTube, avec de vraies vidéos autour. Pratique pour voir le duo titre-miniature en situation, sur ordinateur et mobile. Si la miniature ne ressort pas, retour au croquis.

## 3. Test A/B dans YouTube Studio (« Tester et comparer »)

Le seul test qui mesure le comportement réel du public. Fonctionnement relevé dans l'aide YouTube en octobre 2026 (à revérifier, la fonction évolue) :
- Jusqu'à **3 variantes** : titres seuls, miniatures seules, ou combinaisons titre + miniature.
- Le gagnant est choisi sur la **part de durée de visionnage**, pas sur le taux de clic. Une miniature qui attire des clics de gens qui repartent aussitôt peut perdre.
- Durée : de quelques jours à **2 semaines** selon les impressions.
- **Uniquement sur ordinateur**, dans YouTube Studio, avec les fonctionnalités avancées activées.
- Non éligibles : Shorts, lives programmés, premières (éligibles une fois converties), vidéos pour enfants, réservées aux adultes ou privées.
- Modifier le titre ou la miniature pendant le test l'arrête.
- Une miniature en dessous de 1280 × 720 fait passer toutes les variantes en 480p.
- Résultats possibles : gagnant, performances équivalentes, ou non concluant (la première variante est alors conservée).

Conseils pour un test lisible :
- **Changer une seule chose importante** entre les variantes (le concept, ou le texte, ou le visage), sinon on ne sait pas ce qui a fait la différence.
- **Mettre en première position** la variante préférée : c'est elle qui reste si le test n'est pas concluant.
- **Noter le résultat** et ce qu'il apprend sur le public, pour orienter les miniatures suivantes. Un « équivalent » est aussi une information : la variable testée compte peu.
