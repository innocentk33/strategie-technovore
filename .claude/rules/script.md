---
paths:
  - "projets/**/fiche.md"
  - "projets/**/brouillon*.md"
  - "projets/**/script*.md"
  - "projets/**/grill*.md"
  - "projets/**/storyboard.md"
  - "projets/**/teleprompteur*"
---

# Écriture : brouillon, script, grill, storyboard

- `teleprompteur.md` et `.txt` : une ligne = un souffle ; les `[MARQUEURS]`, `⟦à écrire⟧` et `(indications)` ne se lisent pas. **Les nombres s'y écrivent en chiffres** (« 16 gigas », « 7900 euros », « 20 % », « Qwen 3.8 »), plus faciles à lire (demande de l'auteur, 11/11) ; on garde en lettres « un », « zéro » et ce qui n'est pas une quantité (« trois quarts », « deux 5060 Ti »). Le script garde ses nombres en lettres s'il veut ; le téléprompteur, non.
- `storyboard.md` : timecodes calés sur `voix-off-montee.wav` ; en HyperFrames, `data-start` = le timecode en secondes.

**Les 15 premières secondes sont les plus fortes de la vidéo** (règle du 22/10, section 5 de `strategie.md`) :
- on y met le meilleur moment : le résultat, le chiffre le plus fou ou l'image promise par la miniature ;
- on n'y met ni contexte, ni présentation, ni « dans cette vidéo » ;
- à vérifier à chaque brouillon, script, grill et storyboard ;
- origine : ArtCraft perdait 34 % de ses spectateurs en 15 s (`etudes/audit-2026-10-22.md`).

**Les 30 premières secondes n'ont aucune phrase de remplissage, et le script se dit comme à un ami** (23/10, section 5 de `strategie.md`) :
- chaque phrase des 30 s confirme le clic, ouvre une question ou fait monter l'enjeu ; la question centrale est posée avant 30 s, puis un pont ouvre la boucle suivante ;
- les faits arrivent avec des liaisons orales (« donc », « du coup », « en fait », « sauf que », « en effet », « voilà comment… ») et une réaction ; on ne les empile pas comme une fiche. Repère : 1,5 liaison ou plus pour 100 mots (nos téléprompteurs : 0,7 à 0,9) ;
- le contrôle est la variante storytelling du skill `youtube-script-grill` (test des 30 secondes et axe 10) ;
- origine : `etudes/storytelling-2026-10-23.md`.

**Vers la fin des 30 premières secondes, on annonce le plan en livrables concrets** (11/11, constat de l'auteur, `etudes/audit-2026-11-11.md` § 2 bis) :
- 3 ou 4 choses précises que le spectateur va voir ou obtenir, plus le défi ou la révélation de la fin. Exemple de la référence (Weights & Wonders, 2:03) : « quels modèles j'ai pris, ce que j'ai dû faire pour qu'ils rentrent, à quelle vitesse ça tourne, et où ça casse » ;
- pas une étiquette vague : « on fait les comptes de ta carte » (16 Go) n'annonce rien de concret, et la vidéo a perdu un tiers de ses spectateurs juste après ;
- avant le plan, **on montre le résultat** (l'IA qui répond sans internet, l'agent qui fait tout en un message) ; on explique après ;
- juste après le plan, **la première partie commence par une réponse ou une démo**, pas par une définition ou une conversion d'unités. La théorie vient quand le spectateur en a besoin.

**L'appel à l'abonnement des vidéos d'achat** (12/11, demande de l'auteur, première fois sur Qwen 4) :
- la phrase : « **Si cette vidéo t'a évité un mauvais achat, abonne-toi.** » ;
- elle sert pour les vidéos qui aident à choisir ou à acheter : cartes graphiques, VRAM, budgets, prix, Black Friday, Mac mini, louer ou acheter, cadeau ;
- **dans la voix**, place-la juste après le moment où la vidéo a rendu service : la réponse, la règle ou le prix. Pas en ouverture, pas dans les 30 premières secondes ;
- **dans le kit d'upload**, mets-la dans la description (le bloc « abonne-toi ») et à la fin du commentaire épinglé ;
- pour les autres vidéos (vie privée, nom d'un modèle…), adapte le service rendu, au lieu de forcer « mauvais achat ».
