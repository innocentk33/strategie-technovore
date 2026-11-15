# Critique visuelle indépendante des neuf générations — 15/11/2026

Les neuf PNG du manifeste ont été ouverts et inspectés individuellement avec `view_image`, dans leurs chemins de travail. Les prompts de `prompts-chatgpt-31-12.md` ont été lus. Les références Keanu et trois cartes n'étant pas disponibles, leur fidélité stylistique exacte n'est pas vérifiable ; la cohérence interne du lot l'est.

## Verdict d'ensemble

Lot visuellement réussi et exploitable pour les miniatures : contours noirs lisibles, facettes anguleuses, bonne séparation entre sujets et fond, émotions immédiates et personnages reconnaissables. Aucun sujet n'exige un miroir. Les silhouettes ne présentent pas d'ombre portée visible ni de contamination verte évidente. Pas de texte parasite. Quelques volumes utilisent de légers dégradés ou textures, donc le résultat n'est pas strictement limité à des aplats.

Les dimensions PNG ont été vérifiées directement dans les en-têtes : **1254 × 1254 px pour les neuf images**, et non les 2048 × 2048 demandés. Cette limite du résultat livré doit être annoncée. Ce n'est pas une raison suffisante pour consommer l'unique correction, qui pourrait répéter le même écart. Le contrôle de pixels communiqué par l'agent principal indique également un vert dominant proche de RGB (3, 250, 4), sans uniformité numérique parfaite. Visuellement le fond reste exploitable pour un détourage avec tolérance ; il ne faut pas annoncer un fond strictement #00FF00.

## Verdict par image

| Image | Conformité et lecture | Défauts bloquants | Écarts mineurs / réserves | Décision |
|---|---|---|---|---|
| Boromir | Guerrier reconnaissable, cheveux châtains, barbe rousse, fourrure, gravité, regard gauche ; cercle pouce-index lisible. | Aucun pour l'usage prévu. | Marge haute très faible ; broche ornée d'un arbre, assimilable à un emblème malgré « aucun logo ». Le cercle de main est un peu anguleux mais compréhensible. | Conserver. |
| Mac mini | Petit boîtier argenté, deux ports ronds et fente, trois quarts légèrement en plongée, silhouette complète. | Aucun. | Ombres légèrement graduelles ; objet un peu sous le centre vertical, sans gêne au montage. | Conserver. |
| PC gamer | Tour vitrée complète, rouge/violet, GPU à trois ventilateurs clairement visible, trois quarts, aucun logo. | Aucun. | Marge haute et basse assez serrée. Plusieurs bandes lumineuses évoquent des LED : le prompt demande à la fois un intérieur éclairé et « aucune LED », ambiguïté à ne pas surinterpréter. Aucun vert interne visible. | Conserver. |
| M. Krabs | Reconnaissance immédiate, sourire avide, éclats dans les yeux, pinces rapprochées, orientation gauche. | Aucun empêchant de comprendre le personnage ; cadrage non conforme à l'exigence stricte de coupe sous les pinces. | Partie basse des pinces tronquée. Marge au-dessus des yeux très faible. Yeux pâles jaune-vert, bien distincts du fond vif, mais à surveiller si le détourage supprime trop largement les teintes vertes. | Conserver avec réserve de cadrage ; priorité moindre que Bean. |
| Jim | Reconnaissable, chemise/cravate, trois quarts gauche, regard spectateur, sourcil levé et lèvres pincées convaincants. | Aucun. | Marge haute très faible ; cheveux plus volumineux que « courts ». | Conserver. |
| Math Lady | Femme blonde mûre reconnaissable dans le registre du meme ; sourcils froncés, regard levé, centrée, aucun geste gênant. | Aucun. | Yeux davantage ouverts que plissés ; menton légèrement relevé, donc moins droit que demandé. Expression de perplexité reste claire. Bonne marge haute utile à la composition Severance. | Conserver. |
| Mr Bean | Très reconnaissable, sourire ravi et dents visibles, regard gauche, tweed et petit cadeau rouge/blanc réussis. | **Pour la conformité de la composition : le bas du paquet et des mains est coupé.** Impossible de retrouver les parties manquantes par simple recadrage. | Marge haute très faible ; légère texture de tweed, compatible visuellement avec la série mais moins plate. | **Unique correction prioritaire : dézoomer pour garder tout le cadeau et les mains.** |
| Drake | Refus immédiatement lisible ; tête vers la droite, paume ouverte à gauche, orange, cinq doigts crédibles. | Aucun. | Légère texture/dégradé de cheveux ; sans incidence pratique. | Conserver. |
| Michael | Reconnaissable, face centrée, regard levé, yeux écarquillés et bouche ouverte ; horreur/sidération forte. | Aucun. | Menton un peu relevé mais axe frontal conservé ; compatible avec l'effet Severance prévu. | Conserver. |

## Une seule correction proposée

**Choix : `projets/cadeau-ia-locale/miniature/sources/bean-vert.png`.** Le visage et l'émotion sont déjà bons. Le cadeau est l'accessoire narratif central et son bas manque ; corriger le cadrage a donc plus de valeur que reprendre une légère variation de style ou tenter de corriger la résolution via une nouvelle génération. Il ne s'agit pas de demander une régénération du lot.

Prompt correctif précis, à utiliser avec l'image Bean existante en référence :

> Corrige UNIQUEMENT le cadrage de cette illustration de Mr Bean. Conserve exactement le visage reconnaissable, le sourire ravi montrant les dents, le regard vers la gauche, la veste de tweed marron, la cravate, le petit cadeau rouge à ruban blanc et le style à aplats anguleux avec contours noirs. Dézoome le buste suffisamment : tête entière avec 6–8 % de marge verte au-dessus ; cadeau ENTIER, ses quatre coins et son bord inférieur entièrement visibles ; deux mains entières serrant les côtés du paquet, doigts anatomiquement cohérents, aucun doigt ni poignet coupé par le bord inférieur. Le cadeau doit finir au moins 8 % au-dessus du bord inférieur. Coupe le personnage en bas sur la veste SOUS les mains et SOUS le cadeau. Ne réduis pas artificiellement la taille du cadeau et ne change pas son geste. Trois quarts vers la gauche, centré. Fond vert uni #00FF00 sans ombre ni dégradé, aucune trace de vert sur sujet. Aucun texte ni logo. Carré 2048 × 2048 demandé. Une seule illustration.

Ce rapport n'a déclenché aucune génération ni modification d'image. Après l'unique correction, un contrôle visuel est nécessaire pour confirmer le cadrage ; aucune seconde correction n'est proposée.

## Contrôle final de l'unique correction Bean

Nouvelle version de `bean-vert.png` inspectée visuellement avec `view_image` après sa livraison. **Correction validée : conserver cette version.** Le cadeau entier, son bord inférieur et les deux mains sont maintenant visibles ; le personnage est coupé sur la veste sous les poignets et le paquet. La prise du cadeau est crédible, le sourire ravi et la ressemblance sont conservés, le regard reste dirigé vers la gauche. Le style à contours noirs et facettes chaudes est cohérent avec le lot. Fond vif dégagé autour du buste, sans ombre portée visible.

Réserves mineures : la marge supérieure semble plutôt de 3 % que des 6–8 % demandés, et le cadrage montre davantage de buste que le portrait initial. Aucun de ces points ne compromet l'accessoire ou l'émotion. Le fond reste destiné à un détourage avec tolérance. **Aucune autre génération proposée ou effectuée.** La première version reste conservée sous `bean-vert-initial.png` d'après le signalement de l'agent principal.
