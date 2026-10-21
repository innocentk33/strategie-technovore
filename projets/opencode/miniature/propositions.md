# Miniature OpenCode : 8 propositions

> Fichiers à calques PhotoCraft dans [`photocraft/`](photocraft/) : `opencode-a.psd` à `opencode-h.psd`, avec leurs exports PNG 1920×1080. Test de lisibilité : [`propositions/planche-mobile.png`](propositions/planche-mobile.png) (360 px et 168 px, sur le fond du mode sombre de YouTube).
> Décors : [`propositions/miniature.html`](propositions/miniature.html) (`?v=a|b|c|d|e|f|g|h`), rendus en `photocraft/decor-*.png`. Le gros texte est un calque de texte PhotoCraft que tu peux modifier. Pour réexporter après une retouche : `photocraft-cli convert photocraft/opencode-a.psd photocraft/opencode-a.png`.

## La base commune

- Fond noir avec la grille de la série Uber, et un halo rouge `#ff453a`.
- Texte en SF Pro 800, en minuscules avec un point, 2 mots au maximum.
- Le logo OpenCode est le mot-symbole de la bannière officielle, détouré dans `photocraft/opencode-wordmark.png`.
- **Jamais de vraie clé** : les clés de C sont fausses (« F4k3 ») et coupées. La v1 du script affichait « f1YA », qui est la vraie fin d'une clé de victime.

## A · « ok » + « −264 $ » ⭐ ma recommandation

- **À gauche** : la requête « 请回复ok » dans une bulle bleue, puis un « ok » géant dans une bulle grise.
- **À droite** : un ticket de caisse « Clé API Anthropic » (8 966 requêtes, 35 026 055 tokens), avec le total « −264 $ » en rouge.
- **Angle** : l'absurde. Quelqu'un a payé avec l'argent d'un autre… pour un « ok » ?
- **Lien avec la vidéo** : le hook s'ouvre sur cette bulle à 0:00. Quand l'aperçu se lance tout seul sur l'accueil, le spectateur voit donc la suite directe de la miniature.
- **Pourquoi 264 $ et pas 2,15 $ (l'idée de la fiche)** :
  - « −2,15 $ » se lit comme une petite somme, alors que c'est seulement le solde négatif du crédit OpenAI ;
  - les 264,09 $ sont ce qui est parti sur la clé Anthropic de Max (voir `sources.md`).
- **Honnêteté** : le ticket est celui de *la clé*, pas du « ok ». La vidéo dit bien que 264 $ sont partis sur la clé. Ne pas écrire « 264 $ pour un ok ».
- **Avec le titre** : le titre dit « OpenCode piraté » et « clés API », la miniature montre *ce que* le pirate en a fait. Aucun mot en commun avec le titre, et ça marche aussi avec le titre 2 (*Il a payé pour un « ok »*).

## B · « piraté. »

- **Visuel** : le logo OpenCode géant, en glitch rouge et bleu avec une tranche décalée. Dessous, « piraté. » en rouge lumineux.
- **Angle** : l'actu brute. C'est la mise en page de Code Bear (170 K vues en 2 jours), passée en français et en noir.
- **Pour qui** : la recherche (« opencode piraté »). C'est le trafic visé dans la fiche, et le plus lisible à 168 px.
- **Point faible** : « piraté » répète le titre (« s'est fait pirater »). La miniature n'ajoute donc rien au titre, elle le confirme.

## C · « en clair. »

- **Visuel** : la table `provider` de la Console, inclinée en 3D, avec une colonne `credentials` où l'on lit les clés. La ligne `openai | sk-proj-Ab12Cd34…` est encadrée en rouge. À droite, « en » en blanc et « clair. » en rouge.
- **Angle** : l'ingénierie de la faille. C'est la vraie différence avec Code Bear et Kai, et elle annonce la section 3.
- **Pour qui** : les devs et les apprentis devs, l'ancien public Flutter/Kotlin.
- **Risque** : « en clair » est un mot de dev. Un spectateur qui n'a jamais touché une base de données ne voit qu'un tableau. Le titre (« tes clés API ») aide à comprendre, mais c'est la moins grand public des trois.

## D · Elliot + « hacké. » (ajoutée le 20/10, écartée par l'auteur : « pas du tout bon »)

- **Visuel** : à gauche, Rami Malek (Elliot dans *Mr. Robot*) détouré, désaturé et légèrement bleuté, avec un liseré rouge. Un trait rouge vertical sépare les deux moitiés. À droite, le logo OpenCode et « hacké. » en rouge lumineux.
- **Photo** : ce n'est **pas** une image de la série. C'est une photo de Rami Malek à la PaleyFest 2015, par **Dominick D**, sous licence **CC BY 2.0** ([Wikimedia Commons](https://commons.wikimedia.org/wiki/File:Rami_Malek_in_2015_(2).jpg)), détourée dans PhotoCraft (`photocraft/elliot-detoure.png`). Original dans [`sources/`](sources/).
- **Obligation** : la licence CC BY demande de créditer l'auteur. Si tu publies D, mets cette ligne dans la description : *Miniature : photo de Rami Malek par Dominick D (CC BY 2.0, via Wikimedia Commons), modifiée.*
- **Ce qui reste** : la licence couvre les droits du photographe. Elle ne donne pas l'accord de Rami Malek pour l'usage de son image. C'est le même risque, faible, que pour toutes les chaînes qui mettent des acteurs en miniature.
- **Différence avec Code Bear** : il utilise une capture d'Elliot en capuche, de face. Ici, c'est un autre cliché, en couleur, dans la charte de la chaîne, donc on ne prend pas ta vidéo pour la sienne. En contrepartie, sans la capuche, il ressemble moins au hacker de la série : seuls ceux qui connaissent l'acteur feront le lien.

## E · *This is fine* + « tout va bien. » (ajoutée le 20/10, écartée par l'auteur)

- **Visuel** : le chien de *This is fine* dans la pièce en feu, en fondu vers le noir. À droite, le logo OpenCode et « tout va bien. », avec « bien. » en rouge.
- **Angle** : l'ironie. OpenCode prend feu et tout le monde fait comme si de rien n'était. Le meme est connu de tous, y compris hors du milieu dev.
- **Point fort** : c'est la seule miniature en couleur, avec des jaunes vifs. Au milieu de miniatures tech sombres, l'œil va d'abord sur elle.
- **Points faibles** :
  - **la source fait 800×450 px** : agrandie, elle est un peu floue en plein écran, mais pas aux tailles réelles de la planche ;
  - **le meme reste l'œuvre de KC Green** : il tolère les partages, mais il s'est plaint quand une pub l'a repris (Artisan, mai 2026). Le risque est faible pour une miniature, et nul si tu le crédites dans la description : *« This is fine » : KC Green, Gunshow.*

## F · « OPENCODE HACKÉ » + Anonymous ⭐ choix de l'auteur

- **Visuel** :
  - c'est la mise en page de Code Bear : fond de code vert façon Matrix, icône OpenCode en haut, « OPENCODE » en blanc et « HACKÉ » en rouge, en capitales très grasses (SF Pro 1000) ;
  - le personnage au masque d'Anonymous, en capuche, est fondu à droite. Il n'est pas détouré : la capuche noire se confond avec le fond noir, donc un masque elliptique le fait se fondre dans le décor.
- **Source** : `anonymous-1536x1024.jpeg`, fournie par l'auteur. L'origine n'est pas connue : si c'est une photo de banque d'images libre (Unsplash, Pexels), il n'y a rien à faire ; sinon, il faut retrouver l'auteur. Le masque de Guy Fawkes vient de *V pour Vendetta*, mais on le voit partout depuis Anonymous.
- **Point fort** : la formule a fait ses preuves (170 K vues en 2 jours chez Code Bear), et elle est très lisible à 168 px.
- **Point faible** : elle ressemble beaucoup à la miniature de Code Bear. Dans les suggestions, à côté de la sienne, on peut croire à un doublon. Le masque d'Anonymous la distingue de son Elliot.

## G et H · même formule que F, avec un meme (ajoutées le 20/10)

Le fond, l'icône et le texte « OPENCODE HACKÉ » sont ceux de F. Seul le personnage de droite change. Comparaison à 168 px : [`propositions/planche-mobile-fgh.png`](propositions/planche-mobile-fgh.png).

- **G · le chien de *This is fine*** : il est assis avec sa bulle « THIS IS FINE. », sur une lueur de feu orange. L'ironie : OpenCode est piraté, et le chien dit que tout va bien.
  - Source : PNG transparent fourni par l'auteur (`Lighthearted-Take-On-Stressful-Situation-PNG.png`, chien de droite), agrandi ×3 (`photocraft/chien-this-is-fine.png`).
  - C'est la plus colorée des trois : l'orange ressort sur le noir.
  - Le dessin reste celui de KC Green. Crédit à mettre en description : *« This is fine » : KC Green, Gunshow.*
- **H · Michael Scott, la grimace « yikes »** (*The Office*) : détouré, avec un liseré rouge, en bas à droite. La réaction : « aïe, mes clés ».
  - Source : `Micheal scott yikes .png`. Elle n'était **pas** transparente : je l'ai détourée dans PhotoCraft avec une sélection d'objet, puis j'ai effacé une tache du mur et le liseré blanc.
  - **Qualité** : l'image d'origine ne fait que 500×249 px, agrandie ×3,6. Ça passe aux tailles réelles, mais c'est un peu mou en plein écran. Une capture HD de la même scène corrigerait ça.
  - C'est une image de la série (NBCUniversal), comme toutes les miniatures avec Michael Scott.
- **F, G ou H ?**
  - **F** fait « hacker » : c'est la plus sérieuse.
  - **G** fait sourire, et le chien parle à tout le monde.
  - **H** a un vrai visage avec une émotion forte, le plus efficace en général pour le CTR.
  - Comme les trois partagent la même mise en page, un test A/B F/G/H montrerait exactement quel personnage fait cliquer.

## Test A/B

YouTube accepte 3 miniatures par test. Mon trio : **F, G et H**. C'est la même mise en page, donc le test isole une seule variable : le personnage (Anonymous, chien *This is fine* ou Michael Scott). A et C restent en réserve pour un second test si les trois font un CTR faible. Le critère est la part de durée de visionnage, pas le CTR. Avec A, B et C, on apprendrait plutôt :
- l'**objet absurde** (A) ;
- l'**actu brute** (B) ;
- la **preuve technique** (C).

Pour une vidéo d'actu, la plupart des vues arrivent dans les 48 premières heures. Si tu ne veux pas risquer de lancer avec la mauvaise, publie avec A et laisse le test tourner derrière.
