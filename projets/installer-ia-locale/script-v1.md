# Pourquoi avoir ta propre IA, et comment l'installer (LM Studio) : script v1

**Titre recommandé** : *IA en local : installe ta propre IA, gratuite et sans abonnement* (titre 3 de la fiche, version sans chiffre). Si ton chrono tient « 10 minutes » **hors téléchargement**, prends *IA en local : installe ta propre IA en 10 minutes (gratuit, sans abonnement)* : la phrase qui le tient est déjà dans la section 4 (F39, H10). [CROCHET : TON CHOIX APRÈS LE CHRONO]

**V1 du 24/10/2026** (phase 3), écrite d'après la [fiche](fiche.md) et [`sources.md`](sources.md) (colonne « 2e vérif » et formulations exactes de sa dernière section). Sortie : **lun. 2 nov. 2026, 18 h**. Le grill vient ensuite (`grill-v1.md`).

**Durée** : 1 352 mots de voix off (mesure en bas), plus tes crochets. À ton débit (145 mots/min) : 9 min 20, avant tes crochets ; ils ajoutent environ une minute de capture commentée, ce qui donne 10 à 11 min. Timecodes calculés à 145 mots/min, à recaler sur la vraie prise.

**Texte et sous-texte** :
- **Texte** : une IA en local, c'est un fichier chez toi et une appli qui le fait tourner. Avec LM Studio, ça s'installe comme un jeu.
- **Sous-texte** : ce que tu ne possèdes pas, on peut te le retirer (Fable 5 au hook, récolté à la fin). Planté une deuxième fois à la section 5 : même l'appli, tu ne la possèdes pas complètement (ses conditions, lues par le modèle lui-même) ; le fichier, lui, reste sur ton disque. [CROCHET : TON SOUS-TEXTE À TOI ; CELUI-CI EST UNE PROPOSITION DE LA FICHE]
- **À ne pas recadrer** : ce n'est pas une vidéo contre le cloud. Tu utilises Claude tous les jours et tu le dis à 0:55 : le local, c'est le plan B que tu contrôles, et ce que tu gardes pour toi.

**Fil rouge** : le wifi. Coupé au hook (la preuve), annoncé à la relance de 75 % (« dans deux minutes, je coupe le wifi pour de vrai »), coupé en vrai à la section 5, et rappelé dans la dernière phrase de la fin.

**Boucles ouvertes** :
1. « Une IA que personne ne peut te couper à distance » (0:34-0:42) → tenue à la section 5 (wifi coupé, en vrai), récoltée à la fin.
2. « Dès le premier clic sur le site officiel, il y a un piège » (0:45) → refermée à la section 3 (Bionic, 4:13).
3. « Ton PC, il peut ? » (2:58) → refermée par l'indicateur de l'appli (5:57, relance de 60 %).
4. « Combien moins fort que le cloud ? » (2:41) → ouverte exprès, refermée par Claude #1 (16 nov.).
5. « C'est là qu'on verra si “tes données restent chez toi”, c'est vrai » (relance de 75 %, 6:51) → refermée par le document (7:28-8:10).

**Format** : tuto **testé**. Tout ce qui se passe chez toi (écrans d'installation, nom de l'indicateur, vitesse, chrono, document, test sans carte graphique) est dans un `[CROCHET]` ou un `[VISUEL : capture à faire]`. Aucun libellé d'interface n'est inventé : le script ne cite que « Download LM Studio » (relu sur la page, F23) et le raccourci Ctrl+2 / ⌘2 (doc, F26).

**Conventions** : texte normal = voix off. `[VISUEL : …]` = animation ou capture. `[SON : …]` = bruitage ou musique. `[CROCHETS EN MAJUSCULES]` = à remplir par toi. Nombres en lettres pour la lecture ; les noms de modèle et les adresses s'écrivent en code dans les visuels et se disent comme ils se lisent (« Gemma quatre E quatre B »). Rien de tout ça ne se lit, sauf la voix off.

**Interdits à l'écran** (tes règles) : aucune clé d'API ; aucun modèle « uncensored » ni « abliterated », même dans une liste de recherche (recadre ou floute la capture) ; aucune appli ni aucun document de travail ; aucun lien tiers vers LM Studio.

---

## 0. Hook (0:00 – 0:53) · objectif : 75 % à 0:15, 50 % à 1:00

[VISUEL : capture plein écran de ta machine, LM Studio ouvert avec le modèle chargé. Le curseur clique sur l'icône du wifi, qui se barre. Pas de titre, pas de logo, pas de visage. **Capture à faire, wifi coupé après le téléchargement du modèle** (H1).]
[SON : clic sec, puis le souffle du PC, rien d'autre.]

Je coupe le wifi.

[VISUEL : capture à faire : une question tapée dans LM Studio, la réponse qui s'écrit, l'icône du wifi barrée toujours visible dans le coin.]

Et mon IA me répond quand même.

[VISUEL : coupe nette sur fond sombre. « 12 juin 2026 » en gros, puis la capture du communiqué d'Anthropic du 12/06/2026 (anthropic.com/news/fable-mythos-access), date visible. Frise : 9 juin (sortie) → 12 juin (coupure), « 3 jours ».]
[SON : coupure de courant, façon serveur qui s'éteint.]

Le douze juin, Anthropic a coupé Fable 5, le modèle le plus puissant qu'il ait jamais ouvert au public. Pour tout le monde. Trois jours après sa sortie.

[VISUEL : la frise continue : 12 juin → 1er juillet, « 19 jours ». En petit sous la frise : « directive américaine de contrôle des exportations, appliquée par Anthropic ».]

Et ce n'était même pas son choix : c'est le gouvernement américain qui l'a exigé. Fable 5 est revenu dix-neuf jours plus tard.

Sauf que du coup, on sait une chose : ça peut arriver n'importe quand, chez n'importe quel fournisseur, même quand il n'est pas d'accord. Alors aujourd'hui, on installe une IA qui tourne chez toi, que personne ne peut te couper à distance.

[VISUEL : retour sur ta machine, le wifi toujours barré, le curseur clignote dans LM Studio.]

Pas besoin d'être dev, pas de terminal. Mais dès le premier clic sur le site officiel, il y a un piège. Je te le montre tout à l'heure.

[VISUEL : flash d'une demi-seconde sur la page d'accueil de lmstudio.ai, floutée, un point d'interrogation sur son unique bouton.]

---

## 1. Pourquoi une IA chez toi (0:53 – 2:58)

[VISUEL : trois cases vides à l'écran, charte verte. Elles se remplissent une à une : « Personne ne la coupe », « Tes données restent chez toi », « Ni abonnement, ni internet ».]

Alors, pourquoi en vouloir une chez toi ? Moi, j'utilise Claude tous les jours, et je vais continuer.

[CROCHET : CE POUR QUOI TU T'EN SERS, EN UNE PHRASE. SI LE 12 JUIN T'A TOUCHÉ (UN PROJET BLOQUÉ, UN CHANGEMENT DE MODÈLE), UNE PHRASE ; SINON, RIEN.]

Sauf que Claude, je ne le contrôle pas. Une IA chez moi, c'est mon plan B, celui que je contrôle. Et je vois trois raisons d'en avoir un.

[VISUEL : la case « Personne ne la coupe » s'allume.]

La première, tu viens de la voir : personne ne peut te la couper à distance. Et Fable 5, c'est loin d'être le seul cas. En août 2025, quand GPT-5 est sorti, OpenAI a retiré GPT-4o de ChatGPT le jour même. Les abonnés ont râlé, et il est revenu quelques jours plus tard.

[VISUEL : capture des notes de version d'OpenAI ou de l'article de Simon Willison (08/08/2025), date en gros. Puis TechCrunch (28/07/2025), en petit : « limites hebdomadaires, Pro et Max ».]

Et ça touche aussi Claude : la même année, Anthropic a ajouté des limites par semaine à ses abonnements Pro et Max. Bref, ton fournisseur peut changer ses prix, ses conditions, ou retirer un modèle. Et toi, tu n'as pas ton mot à dire.

[VISUEL : la case « Tes données restent chez toi » s'allume. Un document qui part vers un nuage, barré ; le même document qui reste dans le PC.]
[SON : « whoosh » qui part, puis coupé net.]

La deuxième, c'est tes données. D'après la doc de LM Studio, même quand tu lui donnes un document, tout le traitement se fait sur ta machine. Du coup, au travail, ton code ou les fichiers d'un client ne sortent pas de ton PC. Et justement, LM Studio est gratuit, à la maison comme au travail : ils l'ont annoncé en juillet 2025. Le lien est en description.

[VISUEL : capture du billet « free for work » de LM Studio, date du 08/07/2025 visible.]

[VISUEL : la case « Ni abonnement, ni internet » s'allume. Une barre de téléchargement de jeu qui se remplit, puis « Prêt à jouer, hors ligne ».]
[SON : le « ding » de fin de téléchargement d'un launcher.]

La troisième : une fois le modèle téléchargé, ni abonnement, ni internet. En fait, c'est comme un jeu installé en entier sur ton disque : tu le lances même hors ligne.

[VISUEL : retour face caméra ou capture fixe, sans effet.]

Par contre, je préfère être honnête tout de suite : un modèle qui tient dans ton PC est moins fort que les plus gros du cloud. Combien moins fort que le cloud ? J'ai fait le test sur ma carte, et je te montre tout dans une vidéo qui sort dans deux semaines.

[CROCHET : SI TES ESSAIS SUR LA 5080 SONT FAITS, UN DEMI-INDICE SANS CHIFFRE (« ÇA M'A SURPRIS », « ÇA DÉPEND DE LA TÂCHE »). SINON, RIEN.]

Pour ne pas la rater, abonne-toi : sur Technovore, il y a une nouvelle vidéo chaque lundi.

[VISUEL : bouton « S'abonner », 3 secondes, en bas à droite. Pas d'animation de cloche.]

---

## 2. Ce qu'il te faut (2:58 – 3:58)

[VISUEL : deux colonnes, « Mac » et « PC ». Chaque condition s'écrit pendant qu'elle se dit. Source à l'écran : lmstudio.ai/docs/app/system-requirements, relevé le 24/10/2026.]

Donc, ton PC à toi, il peut la faire tourner ? Voilà ce que demande LM Studio. Sur Mac, il faut une puce Apple, M1 ou plus récent, et macOS 14 : les Mac Intel ne marchent pas. Sur PC, ton processeur doit gérer AVX2, donc les très vieux processeurs sont exclus.

[CROCHET : SI TU VEUX MONTRER COMMENT VÉRIFIER AVX2 SUR SON PC, TA MÉTHODE EN UNE PHRASE (À VÉRIFIER AVANT DE LA FILMER). SINON, RIEN.]

Et LM Studio conseille seize gigas de RAM, plus quatre gigas de mémoire sur la carte graphique sous Windows. Ce sont des conseils, hein : un Mac de huit gigas tourne aussi, avec de petits modèles.

[VISUEL : une jauge « VRAM » vide à côté d'une carte graphique. Deux repères : 8 Go, 16 Go. Sur la ligne du Mac : « mémoire du Mac ».]

Et pour la suite, retiens une seule chose : c'est la mémoire de ta carte graphique, la VRAM, qui décide. Ou la mémoire de ton Mac. Plus elle est grande, plus le modèle peut être gros. On s'en sert dans deux minutes pour choisir le tien.

Et sans carte graphique, du coup ?

[CROCHET : TON TEST SANS CARTE GRAPHIQUE (GPU DÉSACTIVÉ DANS LES RÉGLAGES DE LM STUDIO) : ÇA MARCHE OU PAS, ET À QUELLE VITESSE, À L'ŒIL. SANS TEST, COUPE LA QUESTION ET CE CROCHET (F21).]

Bref, pas besoin d'une machine de guerre pour commencer.

---

## 3. Installer LM Studio (3:58 – 5:11)

[VISUEL : schéma très simple, deux blocs : « un fichier (le modèle) » + « une appli (LM Studio) » = ton IA. Le bloc « appli » s'allume.]

Bon, on installe. En fait, une IA en local, c'est deux choses : un fichier, le modèle, et une appli qui le fait tourner. On commence par l'appli. Et voilà le piège dont je te parlais.

[VISUEL : capture à faire dans ton navigateur : la page d'accueil de lmstudio.ai, son bouton unique « Download LM Studio Bionic » entouré en rouge. Puis la barre d'adresse : on tape `lmstudio.ai/download`. Sur la page, le premier bloc (Bionic) barré, le deuxième bloc entouré en vert.]
[SON : buzzer d'arcade sur le bouton de l'accueil, « ding » sur le deuxième bloc.]

Va sur lmstudio.ai/download, pas sur la page d'accueil : elle te propose Bionic, une autre appli, un agent. Ici, prends le deuxième bloc, « Download LM Studio ». Il existe pour Windows, Mac et Linux.

Bionic, c'est le même éditeur, mais une appli à part, sortie cet été, avec des abonnements pour son cloud. Du coup, si tu cliques sur le gros bouton de l'accueil, tu repars avec un agent qui te propose son cloud payant, alors que toi, tu voulais juste ton IA à toi. On en reparlera un jour. Aujourd'hui, on veut l'appli classique, celle qui fait tourner le modèle chez toi, gratuitement. Et ne passe jamais par le lien d'un autre site : prends-la toujours là.

[VISUEL : texte à l'écran, 3 secondes : « lmstudio.ai/download → 2e bloc ». Le même texte en description.]

Ensuite, franchement, ça s'installe comme un jeu. L'installateur fait un peu plus d'un demi-giga sur Windows et sur Mac, tu le lances, et c'est parti.

[VISUEL : capture à faire : chaque écran de l'installation, en accéléré, le numéro de version visible.]

[CROCHET : CE QUE L'INSTALLATION DEMANDE VRAIMENT, ÉCRAN PAR ÉCRAN, EN UNE OU DEUX PHRASES : UN COMPTE OU PAS, UNE PROPOSITION D'INSTALLER BIONIC OU PAS, UN MODÈLE PROPOSÉ D'OFFICE OU PAS. LA VERSION À L'ÉCRAN : 0.4.26 OU PLUS RÉCENTE.]

[CROCHET : CE QUE TU VOIS AU PREMIER LANCEMENT, EN UNE PHRASE.]

---

## 4. Choisir et télécharger un modèle (5:11 – 7:06) · relances à 60 % (l'indicateur) et à 75 % (le wifi)

[VISUEL : le schéma revient, le bloc « fichier » s'allume, encore vide.]

L'appli est là. Sauf qu'elle est vide : il lui manque le fichier, le cerveau. Donc on va le chercher.

[VISUEL : capture à faire : la recherche des modèles, ouverte au raccourci (afficher « Ctrl + 2 » / « ⌘ + 2 » à l'écran), « gemma 4 » tapé. **Ne garde que les dépôts officiels (Google, `lmstudio-community`) : si une variante « uncensored » ou « abliterated » apparaît dans la liste, recadre ou floute avant le montage.**]

Ouvre la recherche des modèles : Ctrl plus deux sur PC, Commande plus deux sur Mac. Et tape gemma 4. Gemma 4, c'est Google : sorti en avril, sous licence Apache 2.0. En gros, tu as le droit de t'en servir, même pour ton travail.

Dans les résultats, tu verras aussi des versions refaites par n'importe qui. Prends celles des éditeurs officiels : Google, ou lmstudio-community.

[VISUEL : les noms de la liste grossissent, « 12B » et « Q4_K_M » surlignés, puis un tampon « vidéo à part » se pose dessus.]

Dans la liste, tu vas voir des noms bizarres : douze B, Q quatre K M… Je leur consacre une vidéo entière bientôt. Pour l'instant, ne lis pas les noms. Regarde plutôt ce que l'appli te dit, parce qu'avant même de télécharger, elle te dit si le modèle tient dans ta machine. Et c'est pour ça que je te montre LM Studio : tu ne grilles pas six gigas de data pour un modèle qui ne tournera jamais chez toi.

[VISUEL : capture à faire : l'indicateur de compatibilité à côté d'un modèle, en gros plan.]

[CROCHET : CE QUE DIT L'INDICATEUR À L'ÉCRAN, MOT POUR MOT, ET SA COULEUR SI ELLE SE VOIT. NE CITE UNE ÉTIQUETTE (« FULL GPU OFFLOAD POSSIBLE ») QUE SI ELLE EST À L'ÉCRAN (F28, F29, H14).]

[VISUEL : deux cartes, façon sélection de personnage : « 8 Go de VRAM → Gemma 4 E4B, 5,9 Go » et « 16 Go → Gemma 4 12B, 7,4 Go ». Légende : « tailles du catalogue de LM Studio, 24/10/2026 ».]

Alors, si ta carte a huit gigas, prends Gemma 4 E4B : cinq virgule neuf gigas dans le catalogue, il te laisse de la marge. Et si elle en a seize, Gemma 4 12B, sorti en juin : sept virgule quatre gigas.

[CROCHET : LES TAILLES QUE TU LIS DANS L'APPLI, SI ELLES DIFFÈRENT. ET SUR TA 5080 : LE MODÈLE PLUS GROS QUE TU PRENDS, TOI, EN UNE PHRASE ; SINON, RIEN.]

[VISUEL : capture à faire : le bouton de téléchargement, la barre qui avance. En surimpression, le calcul : « appli + modèle ≈ 6,5 Go · 100 Mbit/s ≈ 9 min · 10 Mbit/s ≈ 1 h 25 ».]

Tu cliques sur télécharger, et là, il faut être patient. Entre l'appli et le modèle, ça fait environ six gigas et demi. À cent mégabits, c'est neuf minutes. À dix mégabits, plus d'une heure. Donc mon chrono ne compte pas le téléchargement.

[CROCHET : TON CHRONO HORS TÉLÉCHARGEMENT, DE L'OUVERTURE DE LMSTUDIO.AI/DOWNLOAD À LA PREMIÈRE RÉPONSE. C'EST LUI QUI DÉCIDE DU « 10 MINUTES » DU TITRE.]

[VISUEL : la barre de téléchargement en fond, floutée. L'icône du wifi, encore allumée, clignote.]
[SON : la musique baisse, un tic-tac.]

Pendant que ça télécharge, je te préviens : dans deux minutes, je coupe le wifi pour de vrai, et je lui fais lire un document. C'est là qu'on verra si « tes données restent chez toi », c'est vrai.

---

## 5. Lui parler (7:06 – 8:32)

[VISUEL : capture à faire : le modèle qui se charge, puis la fenêtre de discussion.]

C'est bon, il est téléchargé. Tu le charges, et tu lui parles comme à n'importe quel chat.

[CROCHET : TA PREMIÈRE QUESTION ET SA RÉPONSE, À L'ÉCRAN. UNE QUESTION QUE TON PUBLIC POSERAIT (PAS UN TEST DE CODE).]

[CROCHET : SI L'APPLI AFFICHE UNE VITESSE (TOKENS PAR SECONDE), LE CHIFFRE ET CE QUE ÇA DONNE À L'ŒIL, AVEC UNE PHRASE : « UN TOKEN, EN GROS, C'EST UN MORCEAU DE MOT ». SI ELLE N'AFFICHE RIEN, COUPE CE CROCHET (H15).]

[VISUEL : capture à faire : le curseur sur l'icône du wifi, qui se barre. Même cadrage que le hook.]
[SON : le même clic sec qu'à 0:00.]

Et maintenant, tu te rappelles le début ? Je coupe le wifi.

[CROCHET : TA QUESTION HORS LIGNE ET SA RÉPONSE, EN VRAI, SANS COUPE AU MONTAGE ENTRE LE WIFI BARRÉ ET LA RÉPONSE.]

Et en effet, il répond. D'après la doc de LM Studio, une fois le modèle sur ta machine, tout tourne en local, même sans internet.

[VISUEL : capture à faire : un PDF public joint à la discussion. Proposition : les conditions d'utilisation de LM Studio (lmstudio.ai/terms, version du 23/08/2026), enregistrées en PDF avant de couper le wifi. **Le wifi reste coupé pendant tout le test** : la dernière phrase de la section le dit. Aucun document de travail.]

Deuxième test, le document. Tu peux lui joindre un PDF, un Word ou un fichier texte. S'il est court, le modèle le lit en entier. S'il est long, LM Studio ne lui passe que les passages utiles. Imagine un pote qui n'a pas le temps de lire tout le livre : il va droit aux bonnes pages. Du coup, mets dans ta question les mots que tu t'attends à trouver, ça l'aide à tomber sur les bonnes.

Pour le test, je prends un document public : les conditions d'utilisation de LM Studio lui-même. Et je lui demande : est-ce que cette appli est open source ?

[CROCHET : SA RÉPONSE, À L'ÉCRAN. LA BONNE RÉPONSE (SOURCES.MD, F17) : NON, LE CODE EST UN « TRADE SECRET », ET L'ÉDITEUR PEUT METTRE FIN À LA LICENCE AVEC UN PRÉAVIS. S'IL SE TROMPE, GARDE-LE ET DIS-LE : ÇA MONTRE LA LIMITE D'UN PETIT MODÈLE.]

[VISUEL : le passage des conditions surligné, en anglais, avec la date : « Company may terminate these Terms by providing notice ».]

Voilà la nuance : l'appli est propriétaire, et son éditeur peut même mettre fin à la licence, avec un préavis. Sauf que le fichier du modèle, lui, il reste sur ton disque. Et tout ça s'est passé wifi coupé : le document n'est jamais sorti de ma machine.

[VISUEL : l'icône du wifi barrée, en gros, puis le schéma « fichier + appli » : le bloc « fichier » brille, le bloc « appli » porte un petit cadenas.]

---

## 6. Fin (8:32 – 9:22)

[VISUEL : le schéma complet : fichier + appli = ton IA. Le wifi barré à côté.]
[SON : la musique du début revient, plus posée.]

Voilà comment on a une IA à soi : un fichier sur ton disque, une appli pour le lancer, et un wifi que tu peux couper.

[CROCHET : CE QUE TU EN FAIS, TOI, EN UNE OU DEUX PHRASES : TON PLAN B, CE QUE TU GARDES POUR TOI ET QUE TU NE DONNES PAS AU CLOUD.]

Et si tu veux que même l'appli soit libre, l'autre option, c'est Ollama : open source, avec une appli sur Mac et Windows, et le terminal pour aller plus loin.

[VISUEL : capture de ollama.com, sans compte connecté, 3 secondes.]

Fable 5 est revenu, cette fois. Mais ce que tu ne possèdes pas, on peut te le retirer. Ce fichier-là, personne ne peut te le couper à distance.

Dis-moi en commentaire ta carte graphique, ou ton Mac, et le modèle qui a tourné chez toi. Et si rien ne tient, écris-le aussi : on cherchera ensemble le bon modèle. Et la suite de la série, c'est juste là.

[VISUEL : écran de fin, 20 s, charte verte. **Jusqu'au 16 nov.** : la vidéo IA la plus récente, *OpenCode a été gravement piraté (explication !)* (21 oct.). **Dès le 16 nov.** : « 16 Go de VRAM suffisent-ils pour remplacer Claude ? ». Bouton « S'abonner » à droite. La phrase dite (« la suite de la série ») tient dans les deux cas.]

---

## Relances d'attention

Timecodes de la voix seule, à 145 mots/min (tes crochets les décaleront).

| Temps | Type | Ce qui se passe |
|---|---|---|
| 0:00 | Visuel + son | Le wifi qui se barre, clic sec |
| 0:01 | Preuve | La réponse qui s'écrit, wifi barré |
| 0:04 | Chiffre + coupe | « 12 juin », le communiqué daté, la frise, « 3 jours » |
| 0:16 | Retournement | « Ce n'était même pas son choix » |
| 0:25 | Enjeu | « N'importe quand, chez n'importe quel fournisseur » |
| 0:45 | Boucle ouverte | Le piège du premier clic, flash de la page d'accueil |
| 0:55 | Lien au vécu | « J'utilise Claude tous les jours » (ton crochet) |
| 1:22 | Exemple daté | GPT-4o retiré le jour même |
| 1:33 | Retournement | « Et ça touche aussi Claude » |
| 1:51 | Visuel + son | Le document qui part vers le nuage, coupé net |
| 2:19 | Image gamer + son | Le jeu installé hors ligne, « ding » de launcher |
| 2:41 | Honnêteté + boucle | « Combien moins fort ? J'ai fait le test sur ma carte » |
| 2:52 | Appel à l'action | Abonnement (≈ 31 %) |
| 2:58 | Question | « Ton PC à toi, il peut la faire tourner ? » |
| 3:52 | Question + crochet | « Et sans carte graphique, du coup ? » |
| 4:13 | Boucle refermée + son | Le piège : Bionic, buzzer puis « ding » |
| 5:00 | Image gamer | « Ça s'installe comme un jeu » |
| 5:11 | Relance | « Elle est vide : il lui manque le cerveau » |
| 5:45 | Boucle repoussée | Les noms bizarres, tampon « vidéo à part » |
| 5:57 | Boucle refermée (≈ 60 %) | L'indicateur de compatibilité : « ton PC, il peut ? » (ton crochet) |
| 6:17 | Choix | Les deux cartes « sélection de personnage » |
| 6:34 | Chiffre | Neuf minutes, ou plus d'une heure |
| 6:51 | Relance (≈ 75 %) | « Dans deux minutes, je coupe le wifi pour de vrai » |
| 7:06 | Preuve | Première question (ton crochet) |
| 7:13 | Boucle refermée | Le wifi coupé, en vrai, même clic qu'au hook |
| 7:35 | Image | Le pote qui va droit aux bonnes pages |
| 8:00 | Retournement | Le modèle lit les conditions de sa propre appli |
| 8:10 | Nuance | « L'appli est propriétaire… le fichier reste sur ton disque » |
| 8:54 | Récolte | « Ce que tu ne possèdes pas, on peut te le retirer » |

**Total** : 29 relances en 9 min 22 de voix, environ une toutes les 19 secondes. Le plus long trou : 2:58 → 3:52 (54 s, les conditions techniques), à surveiller au grill.

## Points de décrochage

| Moment | Risque | Problème | Parade |
|---|---|---|---|
| Hook, 0:15-0:53 | Élevé | Les formulations exactes de la 2e vérif font 101 mots jusqu'à « à distance » : 42 s à 145 mots/min. La question centrale (« une IA que personne ne coupe ») est montrée à 0:04 par le contraste (mon IA répond, Fable 5 coupé), mais dite en mots à 0:34-0:42 | Débit plus rapide sur le hook (à 180 mots/min, 35 s) ; sinon, en grill : sortir « Fable 5 est revenu dix-neuf jours plus tard » des 30 s (à la frise, en texte seul) |
| Section 1 (0:53-2:58) | Élevé | Le « pourquoi » juste après le hook : risque « contexte » | Trois cases qui s'allument, un fait daté par raison, la boucle du piège encore ouverte ; à couper en grill si la v2 est longue (la raison 3 est la plus courte à sauter) |
| Section 2 | Moyen | Une liste de conditions techniques (AVX2, macOS 14) | Deux colonnes qui s'écrivent, une phrase par condition, la question « ton PC, il peut ? » refermée seulement à l'indicateur |
| Section 3 | Moyen | L'installation est la partie la plus plate d'un tuto | Le piège Bionic ouvre la section (boucle de 0:40), l'installation en accéléré |
| Le téléchargement | Élevé | Un temps mort réel à l'écran | Le calcul en surimpression, puis la relance de 75 % (« je coupe le wifi pour de vrai ») pendant que la barre avance |
| Section 5, le document | Moyen | Si le modèle se trompe sur les conditions | Garder l'erreur : ça montre la limite annoncée à 2:31 ; ou changer de document (question 4) |

## Notes de montage

- **Charte verte « IA chez moi »**, police mono pour les adresses et les noms de modèle.
- **Le wifi barré** est le motif de la vidéo : même cadrage et même clic à 0:00 et à la section 5 ; il revient en vignette à la fin. Le montage ne coupe pas entre le wifi barré et la réponse (preuve).
- **Composants à construire une fois** : les trois cases, le schéma « fichier + appli », les deux cartes de sélection 8/16 Go, la jauge VRAM. Le schéma resservira pour llama.cpp (8 févr.) ; la jauge pour *IA en local : comment lire le nom d'un modèle* (7 déc.).
- **Captures** : lmstudio.ai (accueil, download, terms, docs), le billet « free for work », le communiqué d'Anthropic du 12/06/2026, ollama.com. Aucune capture d'annonce de Fable 5 en miniature (fiche) ; dans la vidéo, le communiqué daté sert de preuve.
- **Énergie** : rapide sur le hook, posée sur la section 1, montée à 4:13 (le piège), 6:51 (la relance) et 7:13 (le wifi coupé).
- **Carte YouTube** : vers *IA en local : comment lire le nom d'un modèle* à 5:45 (« je leur consacre une vidéo entière »), **à ajouter le 7 déc.**, jour de sa sortie. Vers Claude #1 à 2:41 (« j'ai fait le test sur ma carte »), **à ajouter le 16 nov.**
- **Miniature** : la scène du hook (le wifi barré, une bulle qui répond) ; la vidéo commence sur elle.

## Faits utilisés

| Ce que dit le script | Section | Ligne de `sources.md` | Statut (2e vérif) |
|---|---|---|---|
| « Je coupe le wifi. Et mon IA me répond quand même. » (wifi coupé après le téléchargement) | 0, 5 | H1 | ✅ |
| Le 12 juin, Fable 5 coupé pour tout le monde, 3 jours après sa sortie (9 juin) | 0 | F1, F2, H2, H4 | ✅ |
| « le modèle le plus puissant qu'il ait jamais ouvert au public » (au passé) | 0 | F11, F12, H3 | ⚠️ formulation de la 2e vérif, mot pour mot |
| « c'est le gouvernement américain qui l'a exigé » (sans Lutnick) | 0 | F3, F7, H7 | ⚠️ formulation de la 2e vérif |
| « même quand il n'est pas d'accord » | 0 | F6 | ✅ |
| Revenu 19 jours plus tard (1er juillet) | 0, 6 | F8, F9, H5, H8 | ⚠️ formulation de la 2e vérif (« 19 jours plus tard ») |
| « que personne ne peut te couper à distance » | 0, 6 | H6, H11 | ⚠️ formulation de la 2e vérif (« à distance ») |
| GPT-4o retiré le jour de GPT-5 (août 2025), revenu quelques jours plus tard, « les abonnés ont râlé » | 1 | F13 | ⚠️ formulation de la 2e vérif ; pas de « certains ont résilié » |
| Anthropic : limites par semaine sur Pro et Max, en 2025 | 1 | F15 | ✅ |
| Le traitement des documents se fait sur ta machine, d'après la doc | 1, 5 | F30 | ✅ |
| « gratuit, à la maison comme au travail : ils l'ont annoncé en juillet 2025 » | 1 | F16, F18 | ✅ (formulation de la 2e vérif) ; ni « open source », ni « pour toujours » |
| Ni abonnement, ni internet une fois le modèle téléchargé | 1, 5 | H1, H9 | ✅ |
| Un modèle qui tient dans ton PC est moins fort que les plus gros du cloud | 1 | fiche, plan 2 | non sourcé : affirmation générale, tenue par Claude #1 (16 nov.) |
| Mac : puce Apple (M1 ou plus), macOS 14, pas de Mac Intel ; PC : AVX2 ; 16 Go de RAM conseillés ; 4 Go de VRAM conseillés sous Windows ; Mac de 8 Go avec de petits modèles | 2 | F20 | ✅ (formulation de la 2e vérif) |
| La VRAM (ou la mémoire du Mac) décide de la taille du modèle | 2 | déduit de F20, F35, F36 | ⚠️ déduction, dite sans chiffre |
| Sans carte graphique | 2 | F21 | crochet : à tester avant de le dire |
| lmstudio.ai/download, pas l'accueil (Bionic) ; deuxième bloc « Download LM Studio » ; Windows, Mac et Linux | 3 | F23, F27, H13 | ✅ (formulation de la 2e vérif, mot pour mot) |
| Bionic : même éditeur, appli à part, sortie cet été (16/07/2026), abonnements pour son cloud | 3 | F22, F25, F18 | ⚠️ formulation de la 2e vérif (offre gratuite + deux abonnements) |
| Installateur d'un peu plus d'un demi-giga sur Windows et Mac (619 et 571 Mo) | 3 | F27 (2e vérif) | ✅ (mesure de la 2e vérif) |
| Version 0.4.26 ou plus récente | 3 | F19 | crochet : à lire à l'écran |
| Recherche des modèles : Ctrl+2 / ⌘+2 | 4 | F26 | ✅ |
| Gemma 4 : Google, avril 2026, Apache 2.0 ; la 12B en juin | 4 | F34 | ⚠️ formulation de la 2e vérif (« sorti en avril, la 12B en juin ») |
| « Je leur consacre une vidéo entière bientôt » (12B, Q4_K_M) | 4 | règle de l'auteur | renvoi par le contenu, carte le 7 déc. |
| L'appli dit si le modèle tient avant le téléchargement | 4 | F28, F29, H14 | ⚠️ « l'appli te dit si ça tient » ; étiquette en crochet |
| 8 Go → Gemma 4 E4B (5,9 Go, laisse de la marge) ; 16 Go → Gemma 4 12B (7,4 Go) | 4 | F34, F35, F36 | ⚠️ tailles du catalogue, à relever à l'écran |
| Environ 6,5 Go à télécharger ; 9 min à 100 Mbit/s, plus d'une heure à 10 Mbit/s | 4 | F39, H10 | ⚠️ calcul, dit « environ » ; chrono hors téléchargement en crochet |
| Vitesse affichée (tokens/s) | 5 | H15 | crochet : seulement si l'interface l'affiche |
| « tout tourne en local, même sans internet » | 5 | H1 | ✅ |
| Documents : PDF, Word, texte ; en entier s'il est court, passages utiles s'il est long ; mettre les mots attendus dans la question | 5 | F30 | ✅ |
| L'appli est propriétaire ; l'éditeur peut mettre fin à la licence avec un préavis | 5 | F17, H6 | ⚠️ formulation de la 2e vérif (« trade secret », « terminate… by providing notice ») |
| « L'autre option, c'est Ollama : open source, avec une appli sur Mac et Windows, et le terminal pour aller plus loin. » | 6 | F31, F33, H12 | ✅ (formulation de la 2e vérif, mot pour mot) |

Non utilisés, volontairement : la citation d'Anthropic du 12/06 en entier (F6, gardée pour la frise si tu veux la montrer en anglais), Mythos 5 (F11), le classificateur à 99 % (F10), le retrait définitif de GPT-4o en février 2026 (F14), Qwen3.5 9B (F35), les 4 Go de RAM du plus petit Gemma (F37), Bionic pour Linux (F22), le « 0,1 % » d'OpenAI (F14), les mots-clés vidIQ (F38, pour la description).

## Mesure (24/10/2026)

Comptée sur la voix off seule (sections 0 à 6, sans titres, sans `[…]`, sans tableaux), en séparant aux espaces.

| Mots de voix off | Durée à 145 mots/min | Mots des 30 premières secondes | Liaisons / 100 mots (liste stricte) | Liaisons / 100 mots (liste du grill) | « vous » | Crochets à remplir |
|---|---|---|---|---|---|---|
| 1 352 | 9 min 20 | 72 (84 jusqu'à la fin de la phrase de l'enjeu) | 1,85 (25 liaisons) | 2,37 (32) | 0 | 14 |

- **Mots des 30 premières secondes** : à 145 mots/min, 30 s = 72 mots, de « Je coupe le wifi » à « …ça peut arriver n'importe quand ». La phrase de l'enjeu finit à « …même quand il n'est pas d'accord » (84 mots, 0:35), la promesse à « …à distance » (101 mots, 0:42), et le hook avec son pont à « …tout à l'heure » (130 mots, 0:53). Les 15 premières secondes (37 mots) vont jusqu'à « …Trois jours après sa sortie » : le wifi coupé et Fable 5 y sont tous les deux.
- **Liste stricte** : donc, du coup, en fait, sauf que, en effet, voilà comment, alors, bref, en gros, par contre, justement (donc 4, du coup 5, en fait 2, sauf que 3, en effet 1, voilà comment 1, alors 4, bref 2, en gros 1, par contre 1, justement 1).
- **Liste du grill** (`storytelling.md`, section 3) : la liste stricte, plus mais, et là, parce que, tu te rappelles (mais 3, et là 1, parce que 1, imagine 1, tu te rappelles 1).

## Questions pour l'auteur

1. **Le hook dépasse 30 s** : les formulations exactes de la 2e vérif font 101 mots jusqu'à « à distance » (≈ 42 s à ton débit). Tu acceptes de les dire plus vite, ou on sort « Fable 5 est revenu dix-neuf jours plus tard » de la voix (en texte sur la frise) pour gagner 4 s ?
2. **Le 12 juin et toi** : t'a-t-il touché (un projet, un modèle à changer) ? Si oui, c'est le meilleur vécu de la section 1. Sinon, le crochet saute.
3. **« J'ai fait le test sur ma carte »** : tes essais sur la 5080 sont-ils faits au 2 nov. ? Sinon, la phrase devient « je fais le test sur ma carte, ça sort dans deux semaines ».
4. **Le document public** : je propose les conditions d'utilisation de LM Studio (le modèle lit les règles de sa propre appli, et ça pose la nuance de H6). Si tu préfères plus simple, un document public de ton public (un PDF officiel d'un examen, une page Wikipédia en PDF) ; dans ce cas, la nuance « l'appli est propriétaire » passe en une phrase avant Ollama.
5. **Le titre** : « 10 minutes » ou sans chiffre ? Ça dépend de ton chrono hors téléchargement (section 4).
6. **Bionic « sortie cet été »** : tu veux le nommer davantage (« LM Studio vs Bionic » pourrait faire une vidéo, 3 052 recherches en France) ou le garder en une phrase ?
7. **La raison 1** cite OpenAI et Anthropic. Si tu trouves que ça charge la section, on garde Fable 5 et GPT-4o, et les limites de Claude sautent.
8. **AVX2** : tu veux montrer comment le vérifier ? Je n'ai pas de méthode sourcée ; il faudra la choisir et la vérifier avant de la filmer.
