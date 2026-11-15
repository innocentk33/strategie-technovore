# Miniatures de « Même carte, 2 fois plus rapide » (jeu. 19/11/2026) : propositions du 15/11

> Méthode : skill [`miniature-kai`](../../../.claude/skills/miniature-kai/SKILL.md) (h, i, j). Maquette : [`propositions/miniature-kai.html`](propositions/miniature-kai.html) (`?v=h|i|j`) ; rendus 4K avec `./rendre.sh` dans [`rendus/`](rendus/) ; PSD dans [`photocraft/`](photocraft/) ; test 168 px et 50 % : [`apercu/test-50-et-168px-kai.png`](apercu/test-50-et-168px-kai.png).
>
> **15/11 : tes deux portraits sont en place** (Fry et DiCaprio, générés avec ChatGPT, détourés par `portrait.py <image> sources/ <nom>`). La maquette prend le visage par `?p=fry` ou `?p=dicaprio`.

## 1. Le concept

- **La vidéo** (fiche du 10/11, pas encore de script) : les réglages qui font aller la même carte plus vite (le bon fichier, le déchargement, le contexte, le cache KV quantisé, le MTP, le bon moteur), chaque gain tenu par des mesures publiées.
- **Texte** : « **TA CARTE / BRIDÉE ?** ». Le titre dit le gain (« 2 fois plus rapide »), la miniature dit le problème : ta carte va moins vite qu'elle ne pourrait. Aucun mot du titre ne se répète.
- **Objet** : la carte, et un compteur de vitesse dont l'aiguille touche « 2× » (zone rouge). C'est l'objet de cette vidéo ; rien de repris d'une scène de Kai.
- **Émotion** : le doute (« tu es sûr que ta carte donne tout ? »). Elle dépendra du portrait final.

## 2. Les variantes

| | Rendu | Ce qu'on y voit |
|---|---|---|
| **i**, Technovore sans visage | [`rendus/i-kai.png`](rendus/i-kai.png) | Fond ardoise, « TA CARTE BRIDÉE ? » sur une ligne en haut, la carte menthe à gauche, le grand compteur à droite |
| **h-fry** / **j-fry** | [`h-fry.png`](rendus/h-fry.png), [`j-fry.png`](rendus/j-fry.png) | Fry qui plisse les yeux (« Not sure if… ») : le soupçon, mot pour mot « bridée ? » |
| **h-dicaprio** / **j-dicaprio** | [`h-dicaprio.png`](rendus/h-dicaprio.png), [`j-dicaprio.png`](rendus/j-dicaprio.png) | DiCaprio qui pointe : son doigt mène l'œil droit sur la carte et le compteur ; la reconnaissance plus que le doute |

h = palette de Kai (jaune, ombres rouge et bleue), j = ardoise et menthe ; le visage garde ses couleurs de peau dans les deux. PSD : `photocraft/h-fry.psd`, `j-fry.psd`, `h-dicaprio.psd`, `j-dicaprio.psd`, `i-kai.psd`.

> **15/11, ta décision : le test A/B oppose h-dicaprio, i-kai et j-dicaprio** ([`h-dicaprio.png`](rendus/h-dicaprio.png), [`i-kai.png`](rendus/i-kai.png), [`j-dicaprio.png`](rendus/j-dicaprio.png)), à charger dans « Tester et comparer » à l'upload. Fry reste en réserve (`h-fry`, `j-fry`).

**Le test A/B (3 miniatures)** : la méthode garde h, i et j avec **le même visage** (h contre j = la palette, i contre j = le visage). Choisis donc un visage : **DiCaprio** pour la composition (le doigt pointe la carte), **Fry** pour le sens (le soupçon). Autre test possible, si tu préfères comparer les memes : j-fry, j-dicaprio et i.

## 3. À tenir dans la vidéo

- **« 2× »** sur le compteur : c'est le chiffre de la fiche (« [X] fois plus vite »). Il faut au moins deux mesures publiées qui concordent (règle 3 du calculé). Si le script trouve moins, change le repère (`2×` dans `#gauge`) ou remplace-le par une flèche sans chiffre.
- **« Bridée »** : la vidéo doit dire clairement que les réglages par défaut laissent de la vitesse de côté, sinon le mot promet trop.

## 4. Les portraits (faits le 15/11)

Tu as écarté le visage générique ; tu as généré Fry (`sources/portrait-fry-chatgpt.webp`) et DiCaprio (`sources/portrait-dicaprio-chatgpt.webp`). Droits : images générées d'un personnage de dessin animé et d'un acteur, utilisés comme memes ; même risque faible que les autres memes de la chaîne.
