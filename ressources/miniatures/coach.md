# Coach miniatures : chartes « vert » et « noir » (21 octobre 2026)

**Ce que j'ai regardé :**
- les 20 rendus et les 3 planches ;
- les 7 planches concurrentes : Kai, RepoChad, The Stack, Codacus, RandomAI, WeeklyHow et AIex ;
- la miniature ArtCraft publiée et la proposition Uber B (`projets/uber/miniature/photocraft/uber-b.png`) ;
- les fiches des vidéos, pour vérifier que chaque promesse est tenue.

Chaque paire vert/noir est passée dans le script d'aperçu du skill : tiers, rendus à 360, 300 et 168 px, niveaux de gris, flou, accueil clair et sombre. Les planches sont dans `/private/tmp/claude-501/-Users-innocent-Dev-youtubeSkill/600e90a0-42e7-4f77-9adb-1ee034a07ade/scratchpad/apercu/` (dossier temporaire). Aucun fichier existant n'a été modifié.

**Repère de taille utilisé partout :**
- à 168 px de large, un texte de 100 px de haut en 1280 × 720 mesure 13 px ;
- un libellé mono de 22 px y mesure 3 px ;
- tout ce qui fait moins d'environ 50 px de haut en 1280 n'est donc que de la décoration en suggestions.

**Zone de la durée :** le rectangle x > 1100, y > 610 (en 1280 × 720).

---

## Verdict

- **La plus reconnaissable dans le flux, c'est vert.**
  - Sur `flux-vert.png`, l'ardoise moyenne #34495E est le seul fond de ce ton au milieu des noirs, des néons et des photos : on repère la famille avant de lire.
  - Sur `flux-noir.png`, les tuiles noires perdent leur cadre. Le script mesure 98 à 100 % de pourtour quasi noir sur les 10, et il ne reste que du texte qui flotte sur la page. Seule noir-06, avec son icône WhatsApp verte, accroche l'œil.
- **Prises une à une, les meilleures miniatures sont en noir.** Noir gagne 6 sujets sur 10, pour deux raisons :
  - elle montre des objets réels dans leurs vraies couleurs : Waze cyan, WhatsApp vert, la PS5 ;
  - ses textes retournent le titre : « devinée », « il triche ».

  Vert redessine tout au trait et recolore les logos en menthe : Uber, Waze, Google et WhatsApp y perdent leur reconnaissance immédiate.
- **Le partage par pilier est l'inverse de l'intuition :**
  - **noir pour « Le génie derrière l'app »**, et pour les histoires grand public (pixel, Sony) ;
  - **vert pour « IA chez moi »** : 16 Go, coût de Claude, Abonnement ou IA locale, llama.cpp.

  Chaque charte devient ainsi le contre-pied de sa niche :
  - la niche IA locale est entièrement sombre (Kai, The Stack et RepoChad en noir, Codacus en marine foncé) ;
  - les vidéos françaises sur Uber sont claires ou colorées (relevé de ta fiche `projets/uber/miniature/propositions.md`).

  C'est aussi le partage qui sort des choix sujet par sujet ci-dessous, sans que je l'aie cherché.
- **Le risque concurrent principal :**
  - noir ressemble à The Stack (fond noir, objet héros, reflet au sol) ;
  - vert reprend deux tics de Kai : le logo Claude dans un cadre, puis une flèche vers la carte graphique, et l'étiquette inclinée.
- **Le défaut commun aux deux chartes :** 6 sujets sur 10 répètent le titre au lieu de le compléter (02, 03, 05, 06, 07, 10).

---

## Fiche par sujet

Notes sur 10. « Duo » : est-ce que la miniature ajoute quelque chose au titre ?

### 01 · Le génie caché derrière la carte en temps réel d'Uber

| | Note | À 168 px | Duo |
|---|---|---|---|
| vert-01 | 6 | « 570 000 MILLIARDS » se lit ; le badge Uber et la voiture disparaissent | Ajoute un chiffre qui donne le vertige |
| noir-01 | 7 | « devinée » et l'icône Uber se lisent ; la voiture en pointillés devient une tache | Ajoute, et contredit « temps réel » : le meilleur duo des 20 |

**vert-01**
- **Point fort :** un vrai gros chiffre (569 707 381 193 162 cellules au niveau le plus fin de H3) et les hexagones, qui sont le décor de la vidéo.
- **Défaut :** il y a 5 blocs de texte, et le sous-titre « pour suivre chaque voiture » dit plus que la vidéo. Ton storyboard présente ce chiffre comme le niveau le plus fin possible (« une grille qui peut descendre jusqu'à… »), et la grille sert à trouver un chauffeur.
- **Correction :** supprime la ligne mono (y ≈ 538). Passe le badge Uber en noir #000 avec le mot en blanc : en menthe, ce n'est plus Uber.

**noir-01**
- **Point fort :** « sa position est devinée » contredit le « temps réel » du titre. La vidéo tient la promesse (navigation à l'estime, voitures fantômes), et l'image correspond à son premier plan : un téléphone, une carte sombre, des voitures autour du point bleu.
- **Défaut :** l'élément qui porte la promesse, la voiture en pointillés, mesure 120 px de long. En suggestions, il est invisible.
- **Correction :** ta version `uber-b.png` (« elle existe ? ») règle déjà ce problème :
  - le téléphone est plus serré ;
  - la voiture fantôme est agrandie et désignée par une flèche ;
  - un halo rouge et une grille détachent la tuile du mode sombre.

  Reprends ce décor tel quel, et garde « sa position est devinée. » comme variante de texte pour le test A/B.

**À garder : noir**, sous la forme `uber-b`. La vidéo sort le 9/11 : c'est la priorité.

### 02 · 16 Go de VRAM suffisent-ils pour remplacer Claude ? (Abonnement ou IA locale ? #1)

| | Note | À 168 px | Duo |
|---|---|---|---|
| vert-02 | 5 | La carte graphique, « 16 Go » et « ÇA SUFFIT ? » se lisent ; le cadre Claude devient un carré sombre | Répète la question du titre |
| noir-02 | 4 | Seul « assez ? » reste ; la carte gris foncé se fond dans le noir | Répète (« 16 Go de VRAM ») |

**vert-02**
- **Point fort :** la hiérarchie est claire et la 5080 se reconnaît.
- **Défauts :**
  - la cédille du Ç flotte dans l'interligne : on lit un glyphe parasite posé sur SUFFIT ;
  - le pied de l'établi coupe la marque « techn|ovore » ;
  - la composition (logo Claude dans un cadre, pointillé vers la carte, étiquette inclinée) est celle de Kai (« HERE WE GO. LOL »), sur le même sujet.
- **Correction :** passe au gabarit de la série, celui de vert-10 (voir le sujet 10) :
  - « ABONNEMENT OU IA LOCALE ? » en bandeau ;
  - Claude à gauche, ta 5080 à droite ;
  - « 16 Go » en annotation droite (non inclinée) de 90 px sur la carte ;
  - plus d'établi.

  Si tu gardes la mise en page actuelle : ajoute au moins 30 px d'interligne entre ÇA et SUFFIT, et supprime l'établi.

**noir-02**
- **Point fort :** en plein écran, la carte argentée et le « ? » vert sont élégants.
- **Défaut :** le corps de la carte (#1C1C1E à #3A3A3C) n'a presque aucun écart de valeur avec le fond. Sur la version floutée, il ne reste que l'icône Claude et « assez ? ».
- **Correction :**
  - remplace « 16 Go de VRAM, » par « ma 5080, », qui ajoute ton vécu (le titre ne le dit pas) ;
  - agrandis la carte à 760 px de large en supprimant le reflet ;
  - éclaircis la coque avec un dégradé de #8E8E93 à #3A3A3C.

**À garder : vert**, au gabarit de la série. Les sujets 02 et 10 sont deux épisodes de la même série : leurs miniatures doivent se ressembler.

### 03 · Comment Waze sait qu'il y a un bouchon avant que tu le voies

| | Note | À 168 px | Duo |
|---|---|---|---|
| vert-03 | 6 | La route en diagonale et « IL SAVAIT. » se lisent ; « toi », « bouchon » et le badge non | « avant toi » répète « avant que tu le voies » |
| noir-03 | 7 | Le bouchon rouge, le détour bleu et l'icône cyan : on comprend la scène | Même répétition |

**vert-03**
- **Point fort :** la diagonale donne du mouvement, et les ondes au-dessus des voitures suggèrent le mécanisme (les téléphones émettent).
- **Défauts :**
  - la flèche pointillée traverse le vide, hors de la route : on ne sait pas si c'est un itinéraire ou de l'information ;
  - le contraste de valeurs est faible (0,15, alerte du script) ;
  - en menthe, Waze n'est plus Waze.
- **Correction :** remplace « avant toi, » par « personne ne l'a signalé, ». C'est ton Short du 10/12, et la vidéo le tient : les téléphones servent de capteurs de vitesse. Le spectateur se demande alors comment Waze a su. Passe aussi le badge Waze en cyan #33CCFF.

**noir-03**
- **Point fort :** la plus claire des deux, et l'icône en vraies couleurs remplace la fin du titre coupée sur mobile.
- **Défauts :**
  - le texte répète le titre ;
  - c'est le même téléphone, la même carte et la même rivière que noir-01.
- **Correction :**
  - même texte que pour vert : en gris « personne ne l'a signalé, », en blanc « il savait. » ;
  - retire la rivière pour que la route rouge et bleue domine seule.

  Le gabarit téléphone commun à Uber et Waze peut devenir la signature du pilier, à condition que la couleur dominante change à chaque vidéo.

**À garder : noir.**

### 04 · Le génie caché du pixel : comment ton écran trompe tes yeux

| | Note | À 168 px | Duo |
|---|---|---|---|
| vert-04 | 7 | Écran blanc, loupe RVB, « PAS DE BLANC. » : tout se lit | Complète : le titre dit « trompe », l'image montre comment |
| noir-04 | 8 | La sphère RVB est l'image la plus forte des 20 ; « de blanc. » se lit | Complète |

**vert-04**
- **Point fort :** l'avant/après est dans l'image (un écran blanc, puis une loupe où il n'y a plus de blanc), et « BLANC. » écrit en menthe est un bon clin d'œil.
- **Défaut :** trois éléments secondaires ne servent à rien :
  - l'étiquette inclinée « RVB » (un tic de Kai et de Codacus) ;
  - le libellé mono « blanc ? » (3 px en suggestions) ;
  - le trait pointillé.
- **Correction :** supprime ces trois éléments et agrandis la loupe de 15 % vers le bas à gauche, pour qu'elle couvre davantage l'écran blanc.

**noir-04**
- **Point fort :** couleur, matière et mystère. C'est une miniature « simple » : un seul objet, qui pose une question.
- **Défaut :** rien dans l'image ne montre un écran blanc ; la contradiction n'apparaît qu'en lisant.
- **Correction :** place derrière la sphère un écran de téléphone blanc pur (#FFFFFF, environ 280 × 500 px, x 40 à 320), que la sphère chevauche comme une loupe. Tu récupères l'avant/après de vert-04, et une surface claire qui détache la tuile en mode sombre.

**À garder : noir.**

### 05 · Combien coûte Claude Opus 5.5 en local ? (j'ai fait le calcul)

| | Note | À 168 px | Duo |
|---|---|---|---|
| vert-05 | 5 | L'étiquette de prix et la baie se lisent ; « COMBIEN ? » est limite | Deux questions (l'étiquette et « COMBIEN ? ») qui répètent le titre ; le vrai prix, lui, complétera |
| noir-05 | 4 | Sur la version floutée, il ne reste que l'icône Claude ; la baie disparaît | Idem |

**Le problème est le même pour les deux.** C'est la mise en page de la série de Kai « What Would It Cost to Run… Locally? » : logo Claude, flèche, serveurs, prix en gros. Même sujet, et ta fiche dit d'ailleurs « style Kai ». Ton angle à toi, c'est ta 5080 : sers-t'en.

**vert-05**
- **Point fort :** l'étiquette de prix est un bon objet : on comprend « prix » sans lire.
- **Défauts :**
  - c'est une copie de Kai ;
  - le cadre Claude et l'établi apparaissent déjà dans 02 et 10.
- **Correction :**
  - remplace le cadre Claude et le pointillé par ta 5080 dessinée en petit (environ 220 px de large, annotation « ma 5080 »), posée au pied d'une baie agrandie à environ 560 px de haut : la différence de taille dit « voilà ce qu'il faut » sans un mot ;
  - supprime « COMBIEN ? » et laisse « Claude chez moi, » au-dessus de l'étiquette ;
  - écris le prix calculé à 130 px dans l'étiquette, en prévoyant la largeur d'un prix à 6 chiffres suivi de « € », au cas où le calcul dépasserait 99 999 €.

**noir-05**
- **Point fort :** le rouge (« ce qu'on te prend ») est le bon code pour un prix.
- **Défauts :**
  - la baie (#1C1C1E) est invisible en petit ;
  - « ?? ??? € » est en SF Mono : c'est la seule ligne principale des 10 qui n'est pas dans la police de la charte.
- **Correction :**
  - même concept que pour vert (ta 5080 minuscule face à la baie) ;
  - prix dans la police principale, en rouge #FF453A, à 150 px ;
  - façades des serveurs éclaircies à #636366, avec des LED de 14 px.

**À garder : vert** (pilier IA chez moi), avec le concept refait.

Anthropic ne publie pas les poids de Claude. La miniature « Claude chez moi » reste honnête si tu dis dans la première minute que le calcul se fait avec le plus gros modèle ouvert du même niveau, comme le prévoit ta fiche.

### 06 · Comment 50 ingénieurs faisaient tourner WhatsApp pour 900 millions de personnes

| | Note | À 168 px | Duo |
|---|---|---|---|
| vert-06 | 6 | « 50 INGÉNIEURS. » se lit parfaitement, le logo aussi ; les 50 silhouettes deviennent un pointillé | Répète les deux chiffres du titre |
| noir-06 | 7 | La plus lisible des 20 : l'icône verte et « 50 » | Répète tout le titre |

**vert-06**
- **Point fort :** un « 50 » menthe géant, avec une hiérarchie parfaite.
- **Défauts :**
  - les deux rangées de silhouettes, le crochet et « toute l'équipe » tombent dans la zone de la durée (alerte du script : 0,13) et sont illisibles ;
  - le logo WhatsApp a perdu son vert.
- **Correction :** supprime les silhouettes, le crochet et la légende. Remplis le logo en vert WhatsApp #25D366 et agrandis-le de 15 %.

**noir-06**
- **Point fort :** le contraste entre 900 millions et 50 combine deux types de miniature, gros chiffres et comparaison.
- **Défaut :** la miniature et le titre disent exactement la même chose.
- **Correction :** garde l'image et change le titre, qui n'a plus besoin des chiffres. Deux pistes :
  - « Comment WhatsApp tournait avec une équipe minuscule » ;
  - « Le génie caché de WhatsApp : une équipe minuscule » (la même formule que les titres Uber et pixel).

  Raccourcis aussi la ligne grise à « 900 millions, » et grossis-la de 40 %.

**À garder : noir.** Les chiffres sont justes : 50 ingénieurs pour 900 millions d'utilisateurs, selon Wired en septembre 2015.

### 07 · Comment Google sait en une milliseconde que ton pseudo est déjà pris

| | Note | À 168 px | Duo |
|---|---|---|---|
| vert-07 | 5 | « 0,001 s » et le chrono se lisent ; Google, le champ et le tampon gris « DÉJÀ PRIS » se perdent | Répète « une milliseconde » et « déjà pris » |
| noir-07 | 6 | « il triche. » se lit ; la carte devient un rectangle sombre barré d'un trait rouge | « il triche » ajoute un retournement ; la ligne grise répète le titre |

**vert-07**
- **Point fort :** le pseudo « technovore » déjà pris, un clin d'œil à la chaîne.
- **Défauts :**
  - six éléments se disputent l'image : badge, libellé, champ, tampon, chrono et chiffre ;
  - le chrono à zéro ne dit rien ;
  - « 0,001 s » frôle la zone de la durée.
- **Correction :**
  - supprime le chrono et « 0,001 s » ;
  - mets « IL TRICHE. » à droite (Archivo Black, 150 px) ;
  - agrandis le champ et le tampon de 40 % à gauche, et passe le tampon en menthe pour qu'il ressorte.

**noir-07**
- **Point fort :** le retournement fait cliquer : on veut savoir quel raccourci prend Google.
- **Défauts :**
  - la ligne grise répète le titre ;
  - aucun signe de Google dans l'image ;
  - la carte contient trois lignes de texte de 21 à 34 px, illisibles en petit.
- **Correction :**
  - supprime « en 1 milliseconde, », « Crée ton compte » et « réponse en 0,001 s » ;
  - mets le « G » de Google en couleurs (70 px) en haut de la carte ;
  - agrandis la carte de 25 %.

**À garder : noir.** Promesse à tenir : la vidéo doit montrer ce raccourci, et dire si Google l'a documenté ou si c'est la technique classique. Sinon, « il triche » devient une accusation sans preuve.

### 08 · Tu n'as jamais possédé tes jeux (et Sony vient de le prouver)

| | Note | À 168 px | Duo |
|---|---|---|---|
| vert-08 | 3 | Seul « PAS À TOI. » se lit ; les boîtes ressemblent à des bocaux et les pointillés disparaissent | Paraphrase le titre, et rien ne parle de jeux ni de Sony |
| noir-08 | 7 | La PS5 se reconnaît et « pas à toi. » claque ; les trois cartes ne sont plus que des points | « acheté. pas à toi. » est plus percutant que le titre, mais dit la même chose |

**vert-08**
- **Point fort :** le texte est le bon.
- **Défaut :** le concept ne se lit pas : ni console, ni manette, ni boîtier de jeu reconnaissable.
- **Correction :** remplace les cinq boîtes par une PS5 dessinée au trait (environ 420 px de haut, à gauche) et un seul boîtier de jeu barré « supprimé » à côté. Le texte reste en haut.

**noir-08**
- **Point fort :** un objet que tout ton public reconnaît. La version numérique, sans lecteur de disque, sert même le propos.
- **Défaut :** les cartes « Acheté » et « Supprimé » mesurent 130 px et leurs pastilles 20 px : en suggestions, il n'en reste rien.
- **Correction :** supprime les trois cartes et descends le bloc de texte d'environ 100 px pour le centrer en hauteur sur la PS5. Autre option : garder une seule carte « Supprimé », à 260 × 330 px.

**À garder : noir.** La miniature ne montre pas ce que Sony a fait : la vidéo doit le nommer dans les 30 premières secondes.

### 09 · Le dev qui a mis ChatGPT dans ton PC (l'histoire de llama.cpp)

| | Note | À 168 px | Duo |
|---|---|---|---|
| vert-09 | 6 | « 1 SOIRÉE. », « 2023 » et « llama.cpp » se lisent ; le terminal devient des traits | Complète : le titre ne parle pas de la soirée |
| noir-09 | 4 | Un rectangle noir et « une soirée. » ; l'écran est vide aux deux tiers | Complète |

**vert-09**
- **Point fort :** « codé en 1 soirée » est à la fois vrai et étonnant : le README d'origine dit « hacked in an evening ».
- **Défaut :** quatre blocs se disputent l'image (terminal, nom, calendrier, phrase). Le calendrier fait doublon et repousse « 1 SOIRÉE. » tout en bas.
- **Correction :**
  - supprime le calendrier ;
  - agrandis l'ordinateur de 20 % vers la droite ;
  - garde une seule ligne de commande, et « llama.cpp » à 90 px.

  Le levier le plus fort serait le visage de Georgi Gerganov (la vidéo parle de lui), si tu trouves une photo sous licence libre.

**noir-09**
- **Point fort :** sobre.
- **Défaut :** il n'y a rien à regarder : un écran noir sur un fond noir.
- **Correction :** remplis l'écran avec « llama.cpp » en 110 px au centre, et éclaircis le fond de l'écran à #1C1C1E.

**À garder : vert.**

Le titre contient une erreur factuelle : llama.cpp faisait tourner LLaMA, le modèle de Meta, pas ChatGPT. « Le dev qui a mis un ChatGPT dans ton PC » garde l'idée sans l'erreur.

### 10 · Abonnement ou IA locale ? #2

| | Note | À 168 px | Duo |
|---|---|---|---|
| vert-10 | 6 | Le bandeau, le logo Claude, le « ? » et le ventilateur se lisent ; les deux libellés mono non | Le bandeau reprend le nom de la série, ce qui est normal, mais rien ne dit ce qui change dans cet épisode |
| noir-10 | 5 | Le bandeau et l'icône Claude sont excellents ; la carte graphique s'éteint | Idem |

**vert-10**
- **Point fort :** c'est le meilleur gabarit de série des 20 : un bandeau fixe en haut, un duel gauche/droite, la question au centre.
- **Défaut :** aucun élément propre à l'épisode : le #1 et le #2 auraient la même miniature.
- **Correction :** place le logo du modèle local choisi (vraies couleurs, environ 170 px) dans la baie supérieure du PC, à la place de la barre vide, et supprime les deux libellés mono. Vérifie aussi que « Claude Opus 5.5 » sera encore le dernier modèle fin janvier.

**noir-10**
- **Point fort :** « Abonnement ou IA locale ? » en grand et l'icône orange sont lisibles à toutes les tailles.
- **Défauts :**
  - le libellé « RTX 5080 · 16 GO » sort en police à empattements, alors que noir-02 l'affiche en mono avec le même code : c'est un repli de police ;
  - la carte graphique est trop sombre.
- **Correction :** supprime le libellé, éclaircis la coque et ajoute le logo du modèle, comme pour vert.

**À garder : vert**, avec le même gabarit pour 02.

---

## Comparaison des deux chartes

### Dans le flux

| | Vert | Noir |
|---|---|---|
| Mode sombre (#0F0F0F) | Ressort : fond moyen, 0 % de pourtour noir | Se fond : 98 à 100 % de pourtour quasi noir sur les 10 |
| Mode clair | Ressort | Ressort très fort, comme un bloc noir |
| À 168 px | Les capitales se lisent partout ; les dessins fins se perdent | Le texte principal se lit ; les objets gris foncé se perdent (02, 05, 09, 10) |
| Reconnaissance de la famille | Immédiate, par la couleur du fond | Faible : fond noir et texte blanc, c'est le code de toute la niche IA |
| Émotion | Faible : un schéma calme, contraste de 0,15 à 0,19 (3 alertes « terne ») | Plus forte : des objets réels et des retournements |
| Monotonie | 10 tuiles ardoise et menthe : seul le dessin varie | La couleur de l'objet varie d'une vidéo à l'autre |

### Ressemblances avec les concurrents

| Élément | Chez qui | Charte concernée | Risque | Parade |
|---|---|---|---|---|
| Fond noir, objet héros, reflet au sol | The Stack | Noir | Fort | Supprimer le reflet, invisible à 168 px de toute façon ; mettre une grille sombre et un halo discret, comme `uber-b` |
| Logo Claude dans un cadre, flèche vers la carte graphique ou les serveurs | Kai | vert-02, vert-05, noir-05 | Fort, sur le même sujet | Logo et machine côte à côte sans flèche, ou jeu sur la différence de taille |
| Étiquette inclinée sur le matériel | Kai, Codacus, RepoChad | Vert (le badge menthe) | Moyen | Badge droit (0°), ou annotation avec ligne de rappel, comme sur un schéma technique |
| Point final coloré | RepoChad (« THE CATCH. »), Kai (« USELESS. ») | Les deux | Moyen | Le garder, sans compter dessus pour être reconnu |
| Fond marine quadrillé avec carte graphique plate | Codacus | Vert | Faible : ton ardoise plus clair, sans néon | Ne jamais assombrir l'ardoise ni ajouter de lueurs |

RandomAI (bandeau jaune et captures de jeux), WeeklyHow (visage et captures) et AIex (visage et bandeaux rouges) ne ressemblent à aucune des deux chartes.

### Quelle charte pour quel pilier

- **Le génie derrière l'app → noir.**
  - Les sujets tournent autour d'objets et de marques que tout le monde reconnaît : l'icône en couleur sur fond noir fait le travail.
  - Les voisines en français sont claires ou colorées, donc une tuile noire et soignée s'en détache.
  - Noir prolonge aussi la miniature d'ArtCraft et la proposition Uber B, déjà dans ce style.
  - Même logique pour les sujets « grandes histoires de la tech », comme le pixel (la fiche le classe dans ce pilier) et Sony.
- **IA chez moi → vert.**
  - Toutes les voisines sont noires ou marine foncé : l'ardoise est le contre-pied.
  - Le dessin au trait explique la mémoire, la taille des modèles et le prix sans photo de produit.
  - llama.cpp suit cette règle, puisque son sujet est l'IA en local.
- **Si tu préfères une seule charte, prends vert.** C'est elle qu'on reconnaît. Importe alors depuis noir les logos et objets en vraies couleurs ; sans eux, vert perd ses meilleurs sujets (Uber, WhatsApp, PS5).

Avec deux chartes, la reconnaissance tient à une grammaire commune (règles ci-dessous) et non à la couleur du fond. Le test A/B proposé plus bas sert à vérifier ce partage avant de le figer.

---

## Classement

**Top 5 global, en l'état :**
1. **noir-04** (8) : l'image la plus forte des 20, et un duo qui complète le titre.
2. **noir-08** (7) : un objet que tout le monde reconnaît et une émotion nette (l'injustice), qui parle à un public de joueurs.
3. **noir-01** (7) : le meilleur duo titre-miniature. Sa version `uber-b` est encore au-dessus.
4. **noir-06** (7) : la plus lisible à 168 px ; elle n'a contre elle que la répétition du titre.
5. **vert-04** (7) : l'avant/après le plus clair.

Juste derrière : noir-03. Les plus faibles : vert-08 (3), puis noir-02, noir-05 et noir-09 (4).

**La version à garder pour chaque sujet :**

| # | Sujet | À garder | Correction prioritaire |
|---|---|---|---|
| 01 | Uber (9/11) | Noir, sous la forme `uber-b` | Test A/B « elle existe ? » contre « devinée » |
| 02 | 16 Go (#1) | Vert | Gabarit de série, cédille, établi supprimé |
| 03 | Waze | Noir | « personne ne l'a signalé, » à la place de « avant toi, » |
| 04 | Pixel | Noir | Un écran blanc derrière la sphère |
| 05 | Coût de Claude en local | Vert, concept refait | Ta 5080 minuscule face à la baie, plus de flèche façon Kai |
| 06 | WhatsApp | Noir | Changer le titre, pas l'image |
| 07 | Google | Noir | Supprimer la ligne grise et le texte de la carte, ajouter le G de Google |
| 08 | Sony | Noir | Supprimer les trois cartes |
| 09 | llama.cpp | Vert | Supprimer le calendrier ; « un ChatGPT » dans le titre |
| 10 | Abonnement ou IA locale ? #2 | Vert | Le logo du modèle de l'épisode sur le PC |

---

## Règles de charte à figer

### Communes aux deux chartes (ce qui fait « Technovore »)

1. **Mise en page :**
   - un seul objet héros dans la moitié gauche, sur au moins 40 % de la largeur ;
   - le texte aligné à gauche à partir de x ≈ 700, centré en hauteur ;
   - seule exception, la série « Abonnement ou IA locale ? » : bandeau en haut et duel gauche/droite.
2. **Texte, deux lignes au maximum :**
   - une ligne de contexte de 4 mots au plus, en gris, à environ 45 % de la taille ;
   - une ligne principale de 3 mots au plus, de 110 px de haut minimum, terminée par « . » ou « ? » ;
   - la ligne de contexte n'existe que si elle dit quelque chose que le titre ne dit pas.
3. **Zone interdite :** le rectangle de la durée (x > 1100, y > 610) et une marge de 40 px sur tous les bords.
4. **Logos dans leurs vraies couleurs :** Uber #000, Waze #33CCFF, WhatsApp #25D366, Claude orange. Tout le reste suit la charte.
5. **Rien d'important sous 50 px de haut.** Les libellés mono servent dans la vidéo, pas sur la miniature.
6. **Une couleur de marque commune :** la menthe #07C095 dans les deux chartes. Dans noir, elle remplace le vert #30D158 ; c'est le fil qui relie les deux piliers.
7. **La marque « technovore »** reste en bas à gauche, à taille et position fixes. Elle est illisible à 168 px : ce sont le fond et la grammaire du texte qui font la reconnaissance, pas elle.
8. **Polices sous licence libre.**
   - Noir utilise SF Pro et SF Mono, des polices Apple. Leur licence, de mémoire, réserve leur usage à la conception d'interfaces pour les plateformes Apple : vérifie-la avant de les utiliser sur une chaîne monétisée.
   - Remplace-les par Inter (déjà dans `fonts/`, licence OFL) et JetBrains Mono. Le rendu changera peu, et le repli en police à empattements de noir-10 disparaîtra.

### Vert (IA chez moi, llama.cpp)

- **Fond :** ardoise #34495E quadrillée, jamais assombrie (sinon elle rejoint Codacus).
- **Polices :** Archivo Black en capitales pour la ligne principale, Inter 800 pour le contexte.
- **Dessin :**
  - au trait #E8EEF2, d'au moins 4 px d'épaisseur ;
  - un grand objet plutôt que trois petits ;
  - pas d'établi décoratif.
- **Couleur :** la menthe est le seul accent, hors logos.
- **Badges :** droits, jamais inclinés.
- **À proscrire :** la composition « logo dans un cadre, flèche, machine ».
- **Série « Abonnement ou IA locale ? » :**
  - « ABONNEMENT OU IA LOCALE ? » en bandeau, à hauteur fixe ;
  - Claude à gauche, la machine à droite ;
  - l'élément propre à l'épisode (« 16 Go », logo du modèle) toujours au même endroit sur la machine.

### Noir (génie derrière l'app, grandes histoires)

- **Fond :**
  - noir avec une grille sombre et un halo de la couleur d'accent derrière l'objet, comme sur `uber-b` ;
  - jamais de noir uni : le cadre doit se voir sur le #0F0F0F du mode sombre.
- **Objet :**
  - réel, en couleur et lumineux ;
  - un objet gris foncé (carte graphique, serveur) doit être éclairci, ou remplacé ;
  - pas de reflet au sol (c'est la signature de The Stack).
- **Texte :** Inter ExtraBold en minuscules, interlettrage de −4 %, contexte en gris #8E8E93.
- **Ponctuation finale :** rouge #FF453A pour ce qu'on te prend, menthe #07C095 pour ce que tu as ou gagnes.

### Ce qui varie

Le concept, l'objet, la couleur du logo et, dans noir, la couleur de la ponctuation. Rien d'autre ne bouge pendant au moins 5 vidéos.

---

## Tests A/B à prévoir

**Uber (9/11) :**
- version 1, en première position : `uber-b` avec « elle existe ? » ;
- version 2 : la même image, avec « sa position est devinée. ».

Seul le texte change : tu sauras si ton public préfère la question ou l'affirmation.

**Le choix de charte, sur la vidéo Waze :**
- version 1 : noir-03 corrigée ;
- version 2 : la même scène et le même texte, en vert.

Seule la charte change : c'est ce test qui confirmera ou non le partage « noir pour les applis ».

**Rappels sur « Tester et comparer » :**
- la fonction ne marche que sur ordinateur ;
- le gagnant est choisi sur la part de durée de visionnage, pas sur le taux de clic ;
- un test dure jusqu'à 2 semaines ;
- n'y touche pas pendant qu'il tourne : modifier le titre ou la miniature l'arrête.

## Points factuels relevés

- **vert-01 :** « pour suivre chaque voiture » ne correspond pas à ce que dit la vidéo (voir le sujet 01).
- **05 :** les poids de Claude ne sont pas publics, donc le calcul doit être présenté comme une estimation.
- **07 :** « il triche » doit être démontré dans la vidéo.
- **08 :** l'événement Sony doit être nommé et sourcé.
- **09 :** llama.cpp faisait tourner LLaMA, pas ChatGPT (voir le titre corrigé au sujet 09).
- **Vérifiés et justes :**
  - 50 ingénieurs pour 900 millions d'utilisateurs (Wired, 2015) ;
  - 569 707 381 193 162 cellules H3 ;
  - « hacked in an evening » et mars 2023 pour llama.cpp.

---

> **Suite donnée (21/10)** : partage par pilier adopté par l'auteur. Les corrections ci-dessus sont appliquées dans la v2 (voir [`propositions.md`](propositions.md), § 3). La v1 critiquée ici est dans [`rendus/v1/`](rendus/v1/).
