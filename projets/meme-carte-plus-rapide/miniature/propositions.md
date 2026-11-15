# Miniatures de « Même carte, 2 fois plus rapide » (jeu. 19/11/2026) : propositions du 15/11

> Méthode : skill [`miniature-kai`](../../../.claude/skills/miniature-kai/SKILL.md) (h, i, j). Maquette : [`propositions/miniature-kai.html`](propositions/miniature-kai.html) (`?v=h|i|j`) ; rendus 4K avec `./rendre.sh` dans [`rendus/`](rendus/) ; PSD dans [`photocraft/`](photocraft/) ; test 168 px et 50 % : [`apercu/test-50-et-168px-kai.png`](apercu/test-50-et-168px-kai.png).
>
> **Le visage est provisoire** : c'est le portrait de Strata (The Rock sceptique), en attendant celui de cette vidéo (prompt § 4). Ne publie pas h ni j avec lui : deux miniatures de suite avec le même visage se confondraient.

## 1. Le concept

- **La vidéo** (fiche du 10/11, pas encore de script) : les réglages qui font aller la même carte plus vite (le bon fichier, le déchargement, le contexte, le cache KV quantisé, le MTP, le bon moteur), chaque gain tenu par des mesures publiées.
- **Texte** : « **TA CARTE / BRIDÉE ?** ». Le titre dit le gain (« 2 fois plus rapide »), la miniature dit le problème : ta carte va moins vite qu'elle ne pourrait. Aucun mot du titre ne se répète.
- **Objet** : la carte, et un compteur de vitesse dont l'aiguille touche « 2× » (zone rouge). C'est l'objet de cette vidéo ; rien de repris d'une scène de Kai.
- **Émotion** : le doute (« tu es sûr que ta carte donne tout ? »). Elle dépendra du portrait final.

## 2. Les trois variantes

| | Rendu | Ce qu'on y voit |
|---|---|---|
| **h**, Kai + visage | [`rendus/h-kai.png`](rendus/h-kai.png) | Visage à gauche, « TA CARTE » blanc / « BRIDÉE ? » jaune, la carte jaune et le compteur sous le texte |
| **i**, Technovore sans visage | [`rendus/i-kai.png`](rendus/i-kai.png) | Fond ardoise, « TA CARTE BRIDÉE ? » sur une ligne en haut, la carte menthe à gauche, le grand compteur à droite |
| **j**, Technovore + visage | [`rendus/j-kai.png`](rendus/j-kai.png) | Comme h, en ardoise et menthe ; le visage garde ses couleurs de peau |

## 3. À tenir dans la vidéo

- **« 2× »** sur le compteur : c'est le chiffre de la fiche (« [X] fois plus vite »). Il faut au moins deux mesures publiées qui concordent (règle 3 du calculé). Si le script trouve moins, change le repère (`2×` dans `#gauge`) ou remplace-le par une flèche sans chiffre.
- **« Bridée »** : la vidéo doit dire clairement que les réglages par défaut laissent de la vitesse de côté, sinon le mot promet trop.

## 4. Le portrait à générer (ChatGPT)

**15/11, ta remarque** : pas de visage générique (le « jeune joueur » est écarté), un meme ou un personnage connu. Pistes pour « TA CARTE / BRIDÉE ? » (le doute, le soupçon) :

1. ⭐ **Fry de Futurama, les yeux plissés** (« Not sure if… ») : le meme du soupçon par excellence, il colle mot pour mot à « bridée ? ». Déjà un dessin animé, donc le style illustré lui va sans effort.
2. **Leonardo DiCaprio qui pointe du doigt** (*Once Upon a Time in Hollywood*) : la reconnaissance, « eh, c'est ma carte ! ». Plus positif, moins de doute.
3. **Jim Halpert qui regarde la caméra** (*The Office*) : la complicité, « tu savais pas ? ». Plus subtil, se lit moins bien à 168 px.

The Rock reste celui de Strata : on n'en remet pas un deuxième de suite.

Prompt pour Fry (à adapter si tu choisis un autre meme) :

```
Illustration de Fry, le livreur roux de Futurama, dans la pose du meme « Not sure if… » : les yeux très plissés, l'air soupçonneux, la bouche serrée. Cadrage tête et épaules, de trois quarts, le regard tourné vers la droite de l'image. Style illustration éditoriale, comme une peinture numérique à aplats : contours nets, ombres franches, couleurs vives, fidèle au personnage. Fond uni vert vif (#00FF00), sans dégradé ni ombre portée. Aucun texte, aucun logo. Format carré, 2048 × 2048 px, le personnage bien centré, coupé en bas au niveau des épaules.
```

Si ChatGPT refuse le personnage, demande « un jeune homme roux, cheveux en pétard, t-shirt rouge, yeux très plissés et soupçonneux, style dessin animé » : le meme se reconnaît à l'expression.

Dépose l'image dans `sources/` sous le nom `portrait-illustre.png`, puis : `python3 -I ressources/miniatures/portrait.py projets/meme-carte-plus-rapide/miniature/sources/portrait-illustre.png projets/meme-carte-plus-rapide/miniature/sources/` et `./rendre.sh`.
