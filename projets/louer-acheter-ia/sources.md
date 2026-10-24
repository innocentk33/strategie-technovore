# Louer, acheter ou s'abonner : qu'est-ce qui coûte le moins cher pour l'IA ? : sources

> Phase 1 (recherche) du 23/10/2026.
> 2e vérification (Opus) du 23/10/2026 : 14 ✅ · 10 ⚠️ · 1 ❌ · 2 ❓.
> **Les prix sont relevés le 23/10/2026 ; ils seront relevés une 2e fois avant la sortie (4 janvier 2027)** et encore le jour du tournage. Les prix de la RTX 5080 ont déjà varié de 1 200 € à plus de 2 700 € entre juillet et septembre 2026 (fait 11).
> Format **calculé** : les 5 règles de `strategie.md`, pilier 2, s'appliquent (dire « j'ai fait le calcul » dans les 30 s, chaque chiffre daté, aucune estimation présentée comme mesure, euros et électricité française). Aucun chiffre de Kai n'est repris : on cite ses sources, pas ses nombres.
> Ce qui est déjà sourcé ailleurs n'est pas refait : [`projets/cout-claude-local/sources.md`](../cout-claude-local/sources.md) (S6 RTX 5080 NVIDIA, S12 OVHcloud 8×H200, S14 Scaleway, S15 EDF, S18 abonnement Claude, S19 taux de change) et [`projets/claude-ou-mon-pc-1/modeles-5080.md`](../claude-ou-mon-pc-1/modeles-5080.md).
> Légende 1re vérif : ✅ source primaire lue · ⚠️ seconde main ou nuance · ❌ faux ou à ne pas dire · ❓ introuvable.

## vidIQ (23/10/2026)

Crédits dépensés pour ce sujet : 6 appels (30 crédits) : 1 mots-clés, 1 recherche YouTube FR, 1 outliers EN (Kai), 1 recherche dans la chaîne de Kai, 1 transcription (Kai), 1 outliers FR.

### Mots-clés (France)

| Mot-clé | Volume/mois | Concurrence | Remarque |
|---|---|---|---|
| ia en local rentable | <750 | non fournie | Le mot de la fiche n'a pas de volume mesurable |
| ia local | 108 220 (global) · 11 392 en France | 47,1/100 | −19 % sur 30 j |
| ia en local | 21 403 | 41,6/100 | +91 % sur 30 j |
| ollama | 334 853 · 9 849 en France | 68/100 | −7 % |
| lm studio | 247 760 · 2 581 en France | 59,4/100 | +9 % |
| claude code | 2 693 482 · 46 632 en France | 72/100 | stable |
| intelligence artificielle | 33 409 · 12 850 en France | 50,7/100 | +73 % |
| abonnement claude prix | non mesuré | | (mot de la stratégie : pas d'appel dédié) |

### Vidéos de référence (EN)

| Titre | Chaîne (abonnés) | Vues | × moyenne | URL | Ce qu'on retient (structure, hook) |
|---|---|---|---|---|---|
| Can a Mac Mini Replace your $200 AI Subscription? | Kai (54,9 K) | 325 761 (publiée 28/09/2026, 19:41) | ×8,17 (vidIQ) | https://www.youtube.com/watch?v=3R7yba577uA | Hook : l'extrait de relevé bancaire (« 200 $ partis dans un abonnement »), puis **un chiffre-surprise** annoncé tout de suite (« 79 $, le maximum qu'un Mac Mini produit en un mois »). Annonce de la date des prix (« tous les prix sont au 28 septembre »). Il expose d'abord le meilleur argument **pour** l'achat, puis le retourne : l'abonnement est un paquet de trois choses (le modèle, le calcul pour lire le contexte, un volume), le matériel n'en remplace qu'une. Calcul à voix haute (bande passante ÷ taille du modèle). Un « mois réaliste » après le « mois de rêve ». Fin : qui doit vraiment acheter, et un plan pratique (d'abord baisser l'abonnement, tester une API à 20 $, puis seulement acheter). Description : liste complète des sources datées. Chiffres de la description à ne pas reprendre sans leur source |
| Mac Studio vs $200/Month For AI: Which Is Worth It? | RepoChad (11,8 K) | 278,6 K (28/08/2026, 12:01) | ×43 | https://www.youtube.com/watch?v=psNfWOOtBGM | Même question, plus petite chaîne : confirme la demande |
| The Truth About Running AI On Your Own Hardware | Locally (3,5 K) | 139,3 K (9/08/2026, 13:56) | ×725 | https://www.youtube.com/watch?v=HRLhJjaCu-E | Idem |
| Apple Just Killed AI Subscriptions Forever (Mac Mini M6 & M5 Pro) | AI Master (341 K) | 174,3 K (31/08/2026, 19:51) | ×10 | https://www.youtube.com/watch?v=-miLBs7eYU8 | Le contre-exemple de ton : titre-promesse, que la vidéo de Kai démonte |

### Ce qui existe en français

| Titre | Chaîne | Vues | Date | Angle (à ne pas copier) |
|---|---|---|---|---|
| Faire tourner une IA à la maison sans cloud ? J'ai testé pour que vous n'ayez pas à le faire ! | Tom's Basement (56 K) | 194,6 K | 25/10/2025 | Test d'un mini PC (Geekom A9 Max) avec Ollama : performances, pas d'argent |
| Comparaison des abonnements Claude Pro, Max et gratuit : quel Claude choisir selon TON usage ? | Liwa (10 K) | 27,6 K | 16/03/2026 | Choix d'abonnement, rien sur le local |
| CLAUDE 20$, 100$ ou 200$ : LE MEILLEUR FORFAIT ? | Anthony Marandon (4,7 K) | 3,3 K | 2/12/2025 | Comparatif d'abonnements |
| Tout Comprendre sur Claude IA en 22 Minutes | Yassine Sdiri (294 K) | 1,1 M | 22/03/2026 | Prise en main, hors sujet mais gros hôte |

Aucune vidéo française ne compare abonnement, location de GPU et achat avec un calcul en euros et l'électricité française (confirme le radar du 21/10 et `etudes/kai.md`). Les recherches FR 6 mois sur « carte graphique ou abonnement IA » ne remontent rien de pertinent.

### Ce que ça dit pour nous

- **Demande** : « ia local » fait 108 K recherches par mois (11,4 K en France) et « ia en local » double en un mois (+91 %) : le sujet est porté. Le mot de la fiche (« ia en local rentable ») n'est pas mesurable, mais il se rattache à ces mots.
- **Angle libre** : l'angle « euros + électricité française + location à l'heure » n'existe pas en français ; en anglais, Kai a démontré la demande (326 K, ×8,2) et son public européen lui a reproché les prix américains (`etudes/kai.md`).
- **Ce qu'il faut ajouter à Kai** : trois routes et pas deux (s'abonner, louer le GPU à l'heure, acheter), et des prix en euros TTC. Sa vidéo compare l'abonnement à un Mac Mini ; nous comparons à une RTX 5080 que l'auteur possède, avec une mesure de consommation (⟦mesure de Claude #1⟧).
- **Mots du titre** : « louer », « acheter », « s'abonner », « IA », « euros ». La formule « j'ai fait le calcul » dit le format dès le titre.
- **Conséquence honnête de la structure Kai** : sa leçon est de ne pas comparer au mauvais prix. À nous de dire que la 5080 ne fait pas tourner Claude (voir `claude-ou-mon-pc-1`), donc que « rentable » veut dire « rentable pour ce qu'un modèle de 16 Go peut faire ».

## Prix relevés

> Tous TTC sauf mention « HT ». Relevés les 23/10/2026 (sauf mention). **À relever une 2e fois avant la sortie.**

| Article | Prix | Boutique | URL | Date du relevé |
|---|---|---|---|---|
| Gainward GeForce RTX 5080 Python III (16 Go) | **1 899,95 €** TTC, en stock | LDLC | https://www.ldlc.com/recherche/rtx%205080/ | 23/10/2026 |
| Gainward GeForce RTX 5080 Python III | 1 899,95 € TTC, en stock | Materiel.net | https://www.materiel.net/recherche/rtx%205080/ | 23/10/2026 |
| Gainward GeForce RTX 5080 Phoenix GS V1, « article jamais utilisé » | 1 852,45 € TTC, 1 seul en stock | Materiel.net | https://www.materiel.net/recherche/rtx%205080/ | 23/10/2026 |
| Gigabyte RTX 5080 GAMING OC 16G, WINDFORCE OC SFF, Gainward Phoenix V1 | 1 999,95 € TTC | LDLC et Materiel.net | mêmes pages | 23/10/2026 |
| MSI RTX 5080 16G VENTUS 3X OC | 1 969,95 € TTC, rupture | LDLC | https://www.ldlc.com/recherche/rtx%205080/ | 23/10/2026 |
| PNY RTX 5080 16GB Overclocked Triple Fan | 2 039,98 € (2 029,99 € + 9,99 € livraison) | CDiscount, via comparateur | https://www.comparateur-gamer.fr/prix/pny-rtx-5080-16gb-overclocked-triple-fan-751492794266 | 23/10/2026 à 12 h |
| PNY RTX 5080 Triple Fan, autres offres | 2 236,02 € (InMac) ; 2 249,90 € (Cybertek, Grosbill) | idem | idem | 23/10/2026 |
| PC complet LDLC PC11 BOOSTER (Core Ultra 7 265KF, RTX 5080, 32 Go) | **4 049,95 €** TTC, « sous 7 jours » | LDLC | https://www.ldlc.com/recherche/pc%20gamer%20rtx%205080/ | 23/10/2026 |
| PC complet LDLC PC BBBG (Ryzen 7 9800X3D, RTX 5080, 32 Go) | 4 299,95 € TTC, « sous 7 jours » | LDLC | idem | 23/10/2026 |
| Amazon.fr, RTX 5080 | non relevé (erreur 503) | Amazon.fr | https://www.amazon.fr/s?k=rtx+5080 | 23/10/2026 |
| Claude Pro | 20 $/mois (17 $/mois en annuel, 200 $ d'avance), **sans taxes** ; aucun prix en euros affiché | Anthropic | https://claude.com/fr-fr/pricing | 23/10/2026 |
| Claude Max | « à partir de 100 $ »/mois, sans taxes (5x : 100 $ ; 20x : 200 $ d'après la page d'aide) | Anthropic | https://claude.com/fr-fr/pricing ; page d'aide FR (introuvable le 23/10) | 23/10/2026 |
| Claude Pro, App Store français | 22,00 €/mois ou 249,99 €/an | Apple App Store (relevé par SSD Nodes) | https://www.ssdnodes.com/learn/lang/fr/claude-pro-in-france-what-you-pay | 10/10/2026 (tiers) |
| ChatGPT Plus | 23 €/mois (TVA non précisée) | presse (ITdaily) | https://itdaily.com/news/software/chatgpt-pro-100-euro/ | 13/04/2026 (tiers) |
| ChatGPT Pro (5x) | 103 €/mois (le titre dit « 100 euros ») | presse (ITdaily) | idem | 13/04/2026 (tiers) |
| ChatGPT Pro (20x) | 229 €/mois | presse (ITdaily) | idem | 13/04/2026 (tiers) |
| OVHcloud, instance `rtx5000-28` (1 GPU RTX 5000, VRAM non lue) | 0,36 €/h **HT** | OVHcloud, catalogue public | https://eu.api.ovh.com/1.0/order/catalog/public/cloud?ovhSubsidiary=FR | 23/10/2026 |
| OVHcloud, `l4-90` (1 GPU L4, 24 Go) | 0,75 €/h HT | idem | idem | 23/10/2026 |
| OVHcloud, `l40s-90` (1 GPU L40S, 48 Go) | 1,40 €/h HT | idem | idem | 23/10/2026 |
| OVHcloud, `h100-380` (1 GPU H100) | 2,80 €/h HT | idem | idem | 23/10/2026 |
| Scaleway, L4-1-24G | 0,79 €/h HT (≈ 574,87 €/mois à 730 h) | Scaleway, page tarifs GPU | https://www.scaleway.com/en/pricing/gpu/ | 23/10/2026 |
| RunPod, RTX 5090 (32 Go) | 0,69 $/h (Community) ; 1,19 $/h (Secure) | RunPod | https://www.runpod.io/pricing | 23/10/2026 (page « Updated October 8, 2026 ») |
| RunPod, RTX 4090 (24 Go) | 0,34 $/h (Community) ; 0,89 $/h (Secure) | RunPod | idem | idem |
| RunPod, L4 (24 Go) | 0,44 $/h ; 0,59 $/h | RunPod | idem | idem |
| Vast.ai | prix de marché dynamiques, non lus | Vast.ai | https://vast.ai/pricing | ❓ |
| Électricité, Tarif Bleu option Base (6 kVA) | **0,2001 €/kWh TTC** ; abonnement 15,86 €/mois TTC ; « applicable à compter du 1er août 2026 pour toute nouvelle souscription » | EDF | https://particulier.edf.fr/fr/accueil/electricite-gaz/tarif-bleu.html | 23/10/2026 |
| Électricité, option Heures Creuses (3 kVA) | 0,2142 €/kWh en heures pleines ; 0,1589 €/kWh en heures creuses ; abonnement 12,13 €/mois | EDF | idem | 23/10/2026 |
| Taux de change | 1 € = 1,1205 $ | BCE | https://www.ecb.europa.eu/stats/policy_and_exchange_rates/euro_reference_exchange_rates/html/eurofxref-graph-usd.en.html | 22/10/2026 |

## Faits

| # | Affirmation (telle qu'on la dirait) | Source (URL ; auteur, date) | 1re vérif | 2e vérif |
|---|---|---|---|---|
| 1 | Claude Pro coûte 20 $ par mois (17 $ par mois en facturation annuelle, 200 $ d'avance) et Claude Max « à partir de 100 $ » par mois ; les prix affichés « n'incluent pas les taxes applicables ». | https://claude.com/fr-fr/pricing ; Anthropic, lu le 23/10/2026 (déjà S18 dans `cout-claude-local/sources.md`) | ✅ | ✅ relu le 23/10/2026 : « 20 $ si facturé mensuellement », « 17 $ … (200 $ facturés à l'avance) », Max « À partir de $100 », « Les prix affichés n'incluent pas les taxes applicables » |
| 2 | Max existe en deux paliers : 5x à 100 $ et 20x à 200 $ par mois. | Page d'aide d'Anthropic (https://support.anthropic.com/fr/articles/11049744-combien-coute-le-plan-max), redirigée puis introuvable le 23/10 ; contenu lu dans un résumé de recherche | ⚠️ (page d'aide non lue ; la page de prix ne distingue pas 5x et 20x) | ⚠️ la page de prix confirme les deux paliers (« 5x ou 20x l'utilisation de Pro par session de 5 heures ») ; les 200 $ du 20x viennent du centre d'aide (support.claude.com, article 11049744), lu seulement en résumé de recherche (la page renvoie une 404 à notre outil). Il précise que ces prix valent pour le web, pas pour les applis mobiles |
| 3 | Les abonnements Claude ont des limites d'usage sur une fenêtre glissante de 5 heures, et peuvent avoir des plafonds hebdomadaires ou mensuels. | https://claude.com/fr-fr/pricing (FAQ) | ✅ | ✅ relu : « fenêtre glissante de cinq heures » ; « les formules payantes ajoutent des limites hebdomadaires » |
| 4 | **Prix en euros pour la France** : Anthropic n'affiche aucun prix en euros sur sa page de tarifs ; l'App Store français affiche 22,00 €/mois (Pro) au 10/10/2026. En ajoutant 20 % de TVA au prix web converti au taux BCE du 22/10, Pro ≈ 21,42 €, Max 5x ≈ 107,10 €, Max 20x ≈ 214,19 €. Ce sont des **calculs**, pas des prix affichés. | App Store : https://www.ssdnodes.com/learn/lang/fr/claude-pro-in-france-what-you-pay (10/10/2026) ; calcul : 20 ÷ 1,1205 × 1,2 | ⚠️ (le prix exact facturé s'affiche sur claude.ai/upgrade avant paiement : à relever à la main) | ⚠️ calcul refait : 21,42 €, 107,10 €, 214,19 €, identique. Les 22,00 €/mois et 249,99 €/an de l'App Store viennent toujours de SSD Nodes (tiers, 10/10/2026, TVA non précisée). Dire « environ 21 € par mois avec la TVA, d'après mon calcul » ; le prix réel se relève sur claude.ai/upgrade |
| 5 | Taux de change : 1 € = 1,1205 $ (BCE, 22/10/2026). | https://www.ecb.europa.eu/stats/policy_and_exchange_rates/euro_reference_exchange_rates/html/eurofxref-graph-usd.en.html | ✅ | ✅ relu : 1,1205 au 22/10/2026 |
| 6 | ChatGPT en France : Plus 23 €/mois, nouveau Pro 103 €/mois (5x l'usage de Plus), ancien Pro 229 €/mois (20x). | https://itdaily.com/news/software/chatgpt-pro-100-euro/ ; Jens Jonkers, 13/04/2026. L'article ne dit pas si la TVA est incluse et se contredit (« 100 euros » dans le titre, 103 dans le texte) | ⚠️ (presse, 6 mois d'âge ; page officielle OpenAI illisible : erreur 403) | ⚠️ ITdaily relu (Jens Jonkers, 13/04/2026) : 23, 103 et 229 €, TVA non précisée. OpenAI toujours illisible (403 sur chatgpt.com, openai.com et help.openai.com). D'autres sites français divergent (Plus à 23 ou 24 € ; Pro à 103 ou 115 €). Dire « environ 23 € » pour Plus ; relever à la caisse avant de citer Pro |
| 7 | « OpenAI a fermé les inscriptions au plan Pro à 200 $ depuis le 10 septembre 2026. » | Description de la vidéo de Kai ; aucune confirmation trouvée | ❓ (une seule source, sans lien vers OpenAI ; à ne pas dire) | ❓ inchangé : ne pas dire |
| 8 | Chez Anthropic, le coût moyen d'un développeur est d'environ 13 $ par jour actif et de 150 à 250 $ par mois, avec moins de 30 $ par jour pour 90 % des utilisateurs. | https://code.claude.com/docs/en/costs ; Anthropic. Citation : « the average cost is around $13 per developer per active day and $150-250 per developer per month, with costs remaining below $30 per active day for 90% of users » (déploiements d'entreprise, à la consommation par jetons) | ✅ (nuance : c'est le prix API en entreprise, pas un abonnement individuel) | ✅ relu mot à mot ; la page précise « Across enterprise deployments » et « Claude Code charges by API token consumption » : c'est un coût d'entreprise à la consommation, pas un abonnement |
| 9 | La RTX 5080 a 16 Go de GDDR7, une puissance graphique totale (TGP) de 360 W et demande une alimentation de 850 W. | NVIDIA France : https://www.nvidia.com/fr-fr/geforce/graphics-cards/50-series/rtx-5080/ ; déjà S6 de `cout-claude-local/sources.md` (lu le 22/10/2026) | ✅ (repris, non refait) | ✅ relu sur nvidia.com/fr-fr : 16 Go de GDDR7, 360 W, alimentation de 850 W |
| 10 | RTX 5080 en France le 23/10/2026 : 1 899,95 € chez LDLC et Materiel.net (Gainward Python III, en stock), 2 039,98 € chez CDiscount (PNY). | Voir tableau « Prix relevés » | ✅ (pages de recherche des boutiques ; prix mouvants) | ✅ relu le 23/10/2026 : 1 899,95 € chez LDLC (en stock, 1 boutique) et Materiel.net (en stock) ; 2 039,98 € chez CDiscount via le comparateur (relevé de 15 h) |
| 11 | Le prix de la 5080 bouge beaucoup : prix de lancement français 1 129 € (FE) et 1 179 € (custom) en 2025 ; relevés 1 199,99 € (juillet 2026, Amazon.fr), 1 699,99 € (22/09), 2 723,99 € (8/09, MSI Trio) ; 2 039,98 € le 23/10 ; plus bas à 1 200 € le 29/07 et médiane sur 91 jours à 1 632 € selon le comparateur. | https://www.comparateur-gamer.fr/prix/pny-rtx-5080-16gb-overclocked-triple-fan-751492794266 (23/10/2026) ; https://www.cowcotland.com/news/96665/la-geforce-rtx-5080-disponible-a-1129-euros-en-fe-1179-euros-en-custom-par-msi.html | ⚠️ (comparateur et presse ; historique incomplet : « pas encore assez de relevés ») | ⚠️ corrigé. Lancement : 1 179 € annoncés pour la Founders Edition (janvier 2025), puis 1 129 € peu après (presse, Cowcotland non lisible : 403). Comparateur relu : plus bas 1 200 € le 29/07 (année non affichée), « prix habituel » (médiane sur 91 jours) 1 632 €, et « pas assez de données » pour l'historique. Les 1 199,99 € (Amazon), 2 723,99 € et 1 699,99 € ne figurent pas sur la page : ne pas les dire |
| 12 | Un PC complet avec une RTX 5080 coûte de 4 049,95 € à 4 399,95 € chez LDLC (6 modèles les moins chers, tous 32 Go de RAM, livraison sous 7 jours ou plus de 15 jours). | https://www.ldlc.com/recherche/pc%20gamer%20rtx%205080/ ; LDLC, 23/10/2026 | ✅ | ✅ relu : premier PC fixe à 4 049,95 € (PC11 BOOSTER, Core Ultra 7 265KF, 32 Go, « sous 7 jours »), puis 4 099,95 € et 4 199,95 €. Attention : la page montre des portables « RTX 5080 » dès 2 699,95 € ; la puce des portables n'est pas la carte de bureau, ne pas les comparer |
| 13 | Location chez OVHcloud (HT) : 0,36 €/h pour une instance `rtx5000-28`, 0,75 €/h pour un GPU L4 (24 Go), 1,40 €/h pour un L40S (48 Go), 2,80 €/h pour un H100. | https://eu.api.ovh.com/1.0/order/catalog/public/cloud?ovhSubsidiary=FR ; catalogue public, lu le 23/10/2026 (même méthode que S12) | ✅ (HT ; la VRAM de `rtx5000-28` n'est pas dans le catalogue ; disponibilité réelle non vérifiée) | ✅ catalogue relu (devise EUR, champ « tax » = 20 % du prix : les prix sont HT). **Correction** : `rtx5000-28` est une **Quadro RTX 5000 de 16 Go** (génération 2018), pas une carte récente ; L4 24 Go, L40S 48 Go, H100 80 Go. Dire « une vieille carte pro de 16 Go à 0,36 € de l'heure HT » |
| 14 | Location chez Scaleway : GPU L4 24 Go à 0,79 €/h « avant taxes », soit environ 575 € par mois en continu ; les L40S et H100 ne sont pas disponibles à Paris-1 le 23/10. | https://www.scaleway.com/en/pricing/gpu/ ; Scaleway, lu le 23/10/2026. Le 22/10 : H100 à 2,87 €/h (S14 de `cout-claude-local`) | ✅ (la VRAM « 24 Go » vient du nom `L4-1-24G`) | ✅ relu : « Prices before tax », L4-1-24G à 0,79 €/h (≈ 574,87 €/mois) ; L40S et H100 indisponibles à PAR-1, proposés à PAR-2 (prix non lus) |
| 15 | Location chez RunPod (en dollars) : RTX 5090 0,69 $/h (Community) ou 1,19 $/h (Secure) ; RTX 4090 0,34 $/h ou 0,89 $/h ; L4 0,44 $/h ou 0,59 $/h ; H100 SXM 2,69 $/h ou 3,99 $/h. Page « Updated October 8, 2026 ». | https://www.runpod.io/pricing ; RunPod | ⚠️ (le tableau affiché n'étiquette pas les colonnes : l'attribution Community/Secure vient des données structurées de la page ; TVA non précisée) | ⚠️ relu, identique (« Updated October 8, 2026 »). Taxes non mentionnées. Dire « en dollars, hors taxes éventuelles » |
| 16 | Vast.ai : marché à prix variables (« set by supply and demand across 40+ data centers »), grille non lue. | https://vast.ai/pricing | ❓ (prix horaires introuvables avec notre outil) | ⚠️ remonté à l'API publique de Vast.ai (console.vast.ai/api/v0/bundles, 23/10/2026, offres vérifiées à 1 GPU, à la demande) : RTX 5080 dès 0,303 $/h (médiane 0,468 $/h, 10 offres) ; RTX 4090 dès 0,442 $/h (médiane 0,807, 32 offres) ; RTX 5090 dès 0,543 $/h (médiane 1,076, 34 offres). Prix de marché instantanés, taxes non précisées : dire « environ », avec la date |
| 17 | Électricité : option Base du Tarif Bleu à 0,2001 €/kWh TTC, abonnement 6 kVA 15,86 €/mois TTC, à partir du 1er août 2026 ; option Heures Creuses (3 kVA) 0,2142 €/kWh en heures pleines, 0,1589 €/kWh en heures creuses. Les tarifs évoluent en général les 1er février et 1er août. | https://particulier.edf.fr/fr/accueil/electricite-gaz/tarif-bleu.html ; EDF, lu le 23/10/2026 (confirme S15). Hausse annoncée en février 2027 : Selectra seul (S15) | ✅ (grille EDF) · ⚠️ (hausse de février 2027) | ✅ EDF relu : 0,2001 €/kWh TTC en option Base (affiché sur la ligne 3 kVA ; Selectra : le même prix jusqu'à 6 kVA), abonnement 6 kVA 15,86 €/mois, « à compter du 1er août 2026 » ; HC 3 kVA identique. Grille issue de la délibération CRE n° 2026-147 du 15/07/2026 (communiqué du 16/07 : + 2,5 % TTC en moyenne au 1er août). La CRE annonce le prochain mouvement au 1er février 2027, qui couvrira un « reliquat » du mécanisme de capacité : ni le sens ni le montant ne sont publiés |
| 18 | Le tarif de l'électricité au 1er janvier 2027 (jour de la vidéo, le 4 janvier) sera celui d'août 2026 sauf révision au 1er février : à relever le jour du tournage. | https://particulier.edf.fr/fr/accueil/electricite-gaz/tarif-bleu.html (« évoluent … le 1er février et le 1er août ») | ⚠️ (déduction) | ✅ remonté à la CRE : « le prochain mouvement des TRVE, le 1er février 2027 » (communiqué du 16/07/2026). Le 4 janvier 2027, le tarif sera donc celui du 1er août 2026 |
| 19 | Consommation de la 5080 de l'auteur pendant l'écriture d'un modèle : **⟦mesure de Claude #1⟧** (essais des 23-24/10, wattmètre). Avant la mesure : TGP de 360 W (NVIDIA, #9) ; ordre de grandeur de 300 à 450 W pour un PC complet pendant l'écriture, présenté comme **estimation** dans `modeles-5080.md` section 4.5. | `projets/claude-ou-mon-pc-1/modeles-5080.md` | ❓ (la mesure n'existe pas encore ; ne pas présenter 300-450 W comme une mesure) | ❓ inchangé : la mesure n'existe pas encore |
| 20 | Une RTX 5080 ne fait pas tourner Claude (poids non publics) : elle fait tourner des modèles ouverts de la taille de la mémoire (≈ 16 Go). Qwen3.8-27B pèse 16,05 Go en 4 bits d'après Kai ; la fiche de modèle est à lire. | `projets/claude-ou-mon-pc-1/modeles-5080.md` ; `projets/cout-claude-local/sources.md` S1, S2 (Anthropic ne publie pas de poids) ; Kai (https://www.youtube.com/watch?v=3R7yba577uA) pour les 16,05 Go | ⚠️ (poids de Qwen3.8-27B : Kai seul, fiche Hugging Face non lue ici) | ✅ remonté à Hugging Face (dépôt `Qwen/Qwen3.8-27B` ; fichiers d'Unsloth, 23/10/2026) : en 4 bits, de 14,25 Go (IQ4_XS) à 17,56 Go (Q4_K_XL), et 16,06 Go en Q4_0. Dire « environ 16 Go en 4 bits » |
| 21 | Le prix de louer le **modèle** plutôt que le GPU : Kai cite OpenRouter pour Qwen3.8-27B à 0,1312 $ par million de tokens en entrée et 2,378 $ en sortie (moyenne pondérée, 28/09/2026). | Description de la vidéo de Kai ; https://openrouter.ai/qwen/qwen3.8-27b (page non rendue par notre outil) | ❓ (à remonter à OpenRouter ; si on ajoute cette 4e route, ne pas reprendre le chiffre de Kai) | ⚠️ remonté à l'API d'OpenRouter (23/10/2026) : prix catalogue de `qwen/qwen3.8-27b` = 0,20 $ par million de tokens en entrée et 2,50 $ en sortie. Les chiffres de Kai (0,1312 et 2,378 $) sont une moyenne pondérée de septembre : ne pas les reprendre |
| 22 | Le coût de l'électricité est faible face au reste : à 0,2001 €/kWh, 120 heures par mois à 350 W font 8,40 € ; 240 heures à 450 W font 21,61 €. | Calcul (voir « Seuil de rentabilité ») avec #17 | ✅ (calcul, avec une puissance en hypothèse) | ✅ recalculé indépendamment : 8,40 €, 16,81 €, 7,20 € et 21,61 €, identiques |
| 23 | (ajouté en 2e vérif) Hook de `strategie.md` : « Un abonnement Claude, tous les mois. Ou une carte graphique, une seule fois. Au bout de combien de mois l'achat devient rentable ? » | Faits #1, #20 et le calcul | — | ⚠️ la carte ne remplace pas Claude (#20) : la réponse honnête est « jamais » contre Pro (plus de 10 ans), « environ 19 mois » contre Max 5x, et seulement pour ce qu'un modèle de 16 Go sait faire. Le hook tient si la réponse le dit dans les 30 s |
| 24 | (ajouté en 2e vérif) « Matière » : « 13 $ par développeur et par jour actif : ce que coûte un développeur moyen ». | Fait #8 | — | ⚠️ trop large : c'est la moyenne des déploiements **en entreprise**, facturés au token. Dire « en entreprise, Claude Code coûte en moyenne 13 $ par développeur et par jour actif, d'après Anthropic » |
| 25 | (ajouté en 2e vérif) « Matière » : « 1 200 € à 2 723,99 € : la même carte a changé de prix de plus du double en trois mois ». | Fait #11 | — | ❌ les 2 723,99 € ne sont pas sur la page du comparateur (et c'était un autre modèle, une MSI Trio). Dire : « au plus bas à 1 200 € cet été, 1 900 € minimum aujourd'hui » |
| 26 | (ajouté en 2e vérif) Anecdote : « la même RTX 5080 était à 1 129 € à sa sortie et à 2 039,98 € le 23/10/2026 ». | Faits #10, #11 | — | ⚠️ compare une Founders Edition à un PNY chez CDiscount. Dire : « annoncée à 1 179 € en janvier 2025 ; la moins chère est à 1 899,95 € le 23 octobre 2026 » (presse pour le prix de lancement) |
| 27 | (ajouté en 2e vérif) « Lecture » : la précision de la mesure de consommation change le résultat de moins d'un à deux mois. | Calcul refait | — | ✅ contre Max 5x à 120 h : 19,0 mois à 300 W, 19,7 mois à 450 W ; à 240 h, 21,0 à 22,2 mois |
| 28 | Sur Vast.ai, le GPU se paie à la seconde tant que l'instance est allumée, même quand elle ne calcule rien ; le stockage se paie en continu, même instance arrêtée, jusqu'à ce qu'on la supprime. (ajouté au grill, vérifié le 23/10/2026) | https://docs.vast.ai/documentation/instances/pricing ; Vast.ai, lu le 23/10/2026. Citations : « Charged per second while your instance is running » ; « Billed continuously while your instance exists, regardless of running state » ; « Storage charges continue even when instances are stopped » | ✅ | ✅ (grill) : dire « tu paies tant que la machine est allumée, et le stockage même machine arrêtée, d'après la doc de Vast.ai » ; le prix du stockage n'est pas relevé |
| 29 | Calcul refait au grill (script indépendant, mêmes hypothèses que le script v1) : identique au dixième pour les deux tableaux du « Seuil de rentabilité ». En plus : sensibilité contre Max 5x à 240 h = 20,5 mois à 300 W (le fait 27 donne 21,0 à 22,2 pour 350 à 450 W) ; frise sur 36 mois à 120 h : Max 5x ≈ 3 856 €, achat 1 899,95 + 36 × 8,40 ≈ 2 202 €, location Vast.ai médiane ≈ 1 804 €, la moins chère ≈ 1 168 € ; la location dépasse Pro (21,42 €) à partir de ≈ 51 h par mois (médiane) ou ≈ 79 h (offre la moins chère), soit environ 2 h par jour. (ajouté au grill, vérifié le 23/10/2026) | Calcul, faits #4, #16, #17, #22 | ✅ | ✅ (grill) : à 120 h, la location Vast.ai reste sous l'achat pendant 45,5 mois (médiane) à 79 mois ; c'est la route la moins chère pour qui paie un Max, sur ce modèle de 16 Go |

## Seuil de rentabilité (calcul)

**Hypothèses (chacune écrite)**
1. Prix de la carte : P = 1 899,95 € TTC (LDLC, Gainward Python III, 23/10/2026). Prix du PC complet : 4 049,95 € TTC (LDLC PC11 BOOSTER). L'auteur possède déjà sa 5080 : pour lui, le coût d'achat est un coût passé ; le calcul parle du spectateur qui hésite.
2. Électricité : c = 0,2001 €/kWh TTC (EDF Base, 6 kVA, 1er août 2026) ; l'abonnement EDF n'est pas compté (il existe de toute façon).
3. Puissance : **hypothèse de 350 W pendant l'écriture, à remplacer par ⟦mesure de Claude #1⟧**. Coût électrique mensuel = W ÷ 1000 × heures × c.
4. Heures de génération par mois : 120 h (≈ 4 h par jour) et 240 h (≈ 8 h par jour). Ce sont des cas types, pas des mesures.
5. Abonnements TTC : prix web en dollars ÷ 1,1205 × 1,2 (TVA 20 % ajoutée au prix affiché, non vérifiée à la caisse) ; ChatGPT : prix ITdaily d'avril 2026 pris tel quel.
6. Location TTC : prix HT × 1,2 (un particulier paie la TVA) ; RunPod : prix en dollars ÷ 1,1205, sans TVA ajoutée (non précisée).
7. Une carte de 16 Go et un abonnement ne rendent pas le même service (fait 20) : « rentable » compare des coûts, pas des performances.
8. La carte n'a pas de valeur de revente, ni d'autre usage (jeu) dans le calcul.

**Résultats (calculés le 23/10/2026)**

Coût électrique mensuel à 0,2001 €/kWh : 350 W × 120 h = 8,40 € ; 350 W × 240 h = 16,81 €. Variation de la puissance : 300 W et 120 h = 7,20 € ; 450 W et 240 h = 21,61 €.

*Acheter la carte contre s'abonner* (mois = P ÷ (abonnement − électricité)) :

| Contre | Prix mensuel TTC | 120 h (8,40 €) : carte seule | 120 h : PC complet | 240 h (16,81 €) : carte seule |
|---|---|---|---|---|
| Claude Pro (≈ 21,42 €) ou ChatGPT Plus (23 €) | 21,42 € / 23 € | 146 mois / 130 mois | 311 / 278 mois | 412 / 307 mois |
| ChatGPT Pro 5x (103 €) | 103 € | 20,1 mois | 42,8 mois | 22,0 mois |
| Claude Max 5x (≈ 107,10 €) | 107,10 € | **19,3 mois** | 41,0 mois | 21,0 mois |
| Claude Max 20x (≈ 214,19 €) | 214,19 € | **9,2 mois** | 19,7 mois | 9,6 mois |

*Acheter la carte contre louer un GPU* (mois = P ÷ (location − électricité), 350 W) :

| Location | Prix à l'heure TTC | Coût à 120 h | Carte rentable en | Coût à 240 h | Carte rentable en |
|---|---|---|---|---|---|
| OVH RTX 5000 (0,36 € HT) | 0,432 € | 51,8 € | 43,7 mois (3,6 ans) | 103,7 € | 21,9 mois (1,8 an) |
| OVH L4 24 Go (0,75 € HT) | 0,900 € | 108,0 € | 19,1 mois (1,6 an) | 216,0 € | 9,5 mois |
| Scaleway L4 24 Go (0,79 € HT) | 0,948 € | 113,8 € | 18,0 mois (1,5 an) | 227,5 € | 9,0 mois |
| RunPod RTX 4090 Community (0,34 $) | 0,303 € | 36,4 € | 67,8 mois (5,7 ans) | 72,8 € | 33,9 mois (2,8 ans) |
| RunPod RTX 5090 Community (0,69 $) | 0,616 € | 73,9 € | 29,0 mois (2,4 ans) | 147,8 € | 14,5 mois (1,2 an) |

**Lecture**
- Contre un abonnement à 20-23 €, aucune carte ne se rentabilise (plus de 10 ans). Contre un Max à 100 € environ, il faut environ 19 à 21 mois pour la carte seule, plus de 3 ans avec un PC complet à 4 050 €. Contre un Max 20x (≈ 214 €), environ 9 à 10 mois.
- L'électricité pèse peu : de 7 à 22 € par mois selon la puissance et les heures. La précision de la mesure de la consommation change le résultat de moins d'un à deux mois.
- Louer à l'heure bat l'achat pour un usage léger : 36 à 114 € par mois à 120 h, selon la carte, contre une carte à 1 900 €.
- Le prix de la carte pèse davantage que tout le reste : à 1 200 € (plus bas relevé en juillet) tous les délais baissent d'un tiers environ.
- Réserve : la carte de 16 Go ne remplace pas le service d'un abonnement (fait 20) ; ce tableau compare des prix, pas des capacités.
- Script de calcul : `/private/tmp/claude-501/-Users-innocent-Dev-youtubeSkill/e157317b-e0c6-49ed-a993-29af06a1f505/scratchpad/calc.py` (temporaire, à refaire dans le dépôt si on le garde).

## Matière pour le script

**Chiffres forts**
- 19 mois : seuil de la carte (1 899,95 €) contre un Max à 100 $ + TVA, usage de 120 h par mois (calcul).
- Plus de 10 ans contre un abonnement à 20 €.
- 7 à 22 € d'électricité par mois : le poste le plus petit.
- 0,2001 €/kWh (EDF, août 2026), 1,1205 $ pour 1 € (BCE).
- 1 200 € à 2 723,99 € : la même carte a changé de prix de plus du double en trois mois (fait 11).
- 13 $ par développeur et par jour actif, 150 à 250 $ par mois (Anthropic, fait 8) : ce que « coûte » un développeur moyen.

**Démonstrations en motion design**
- La balance : à gauche l'abonnement en barres mensuelles qui s'empilent, à droite le prix de la carte et une petite jauge d'électricité (faits 1, 10, 17).
- Les trois chemins sur une même frise de 36 mois : abonnement, location, achat ; le point où les courbes se croisent (calcul).
- Le compteur de watts de la prise pendant que la carte écrit : ⟦mesure de Claude #1⟧.
- Le prix de la même carte sur trois mois (jul.-oct. 2026) (fait 11).

**Anecdote SOURCÉE** : la même RTX 5080 était à 1 129 € à sa sortie en 2025 et à 2 039,98 € le 23/10/2026 (faits 10, 11) : acheter une carte, c'est aussi parier sur le prix du marché.

**Questions que se pose le public** (tirées de `etudes/kai.md`, 50 commentaires de Kai du 17/10) : au bout de combien de temps ça devient rentable ? (fil de 52 likes) ; et l'électricité en Europe (135 likes, 44 réponses) ; que peut faire **ma** carte ? ; vie privée (364 likes). [à demander à l'auteur : son usage mensuel réel de Claude et le nombre d'heures où sa 5080 travaille]

## Points ouverts

- **⟦mesure de Claude #1⟧** : puissance au mur de la 5080 pendant l'écriture (essais des 23-24/10). Remplacer les 350 W d'hypothèse.
- **2e relevé de prix avant la sortie (4 janvier 2027)** et relevé le jour du tournage : cartes, PC, abonnements (euros réels depuis claude.ai/upgrade), locations.
- Prix réels en euros TTC des abonnements Claude : à relever à la caisse (fait 4) ; Max 5x/20x à confirmer sur la page d'aide FR.
- OpenAI : page officielle illisible (403) ; ITdaily a six mois (fait 6) ; le « plan Pro fermé » de Kai n'est pas confirmé (fait 7).
- Amazon.fr non lisible (503) ; Topachat 404 ; Vast.ai dynamique : compléter à la main.
- VRAM de l'instance OVH `rtx5000-28` à vérifier (la RTX 5000 de NVIDIA existe en 16 Go, non lue ici).
- La TVA sur la location (RunPod, prix en dollars) : vérifier avant de les mettre dans un calcul TTC.
- Hausse de l'électricité en février 2027 : à relever à la CRE, pas seulement chez Selectra (S15).
- Décider si l'on ajoute la route « louer le modèle à la requête » (OpenRouter) à la comparaison (fait 21).
- Aucun chiffre de Kai n'est repris : ses sources (code.claude.com, OpenRouter, EIA) sont citées mais seul `code.claude.com` a été lu ici.

## 2e vérification : prix et seuil (23/10/2026)

**Prix re-relevés le 23/10/2026** : identiques à la phase 1 pour LDLC, Materiel.net, le PC LDLC, Claude, OVHcloud, Scaleway, RunPod, EDF et la BCE. Ce qui change :
- OVHcloud `rtx5000-28` = **Quadro RTX 5000, 16 Go, génération 2018** (catalogue public) ;
- **Vast.ai** (API publique) : RTX 5080 dès 0,303 $/h, médiane 0,468 $/h ; RTX 4090 dès 0,442 $/h ; RTX 5090 dès 0,543 $/h (fait 16) ;
- **OpenRouter**, Qwen3.8-27B : 0,20 $ / 2,50 $ par million de tokens (fait 21) ;
- **CRE** : grille du 1er août 2026 (délibération n° 2026-147 du 15/07/2026), prochain mouvement le 1er février 2027 (faits 17, 18) ;
- toujours illisibles : OpenAI (403 sur trois adresses), Amazon.fr (page vide, code 202), le centre d'aide Anthropic (404).

**Seuil de rentabilité refait de zéro** (mêmes hypothèses, script indépendant) : **je trouve pareil**, au dixième près, pour chaque case des deux tableaux (146 / 130 / 20,1 / 19,3 / 9,2 mois pour la carte à 120 h ; 43,7 / 19,1 / 18,0 / 67,8 / 29,0 mois pour la location). Deux lignes de plus pour la location, avec Vast.ai converti au taux BCE, sans TVA ajoutée :

| Location | Prix à l'heure | Coût à 120 h | Carte rentable en | Coût à 240 h | Carte rentable en |
|---|---|---|---|---|---|
| Vast.ai RTX 5080, offre la moins chère (0,303 $) | 0,270 € | 32,4 € | 79,0 mois | 64,9 € | 39,5 mois |
| Vast.ai RTX 5080, médiane (0,468 $) | 0,418 € | 50,1 € | 45,5 mois | 100,2 € | 22,8 mois |

**Remarques sur la méthode** (le calcul est juste, ces points changent la façon de le dire) :
- La ligne OVH « RTX 5000 » compare la 5080 à une carte de 2018 : dis-le, ou remplace-la par la RTX 5080 de Vast.ai, qui compare la même carte.
- À 1 200 € (plus bas de l'été), le seuil contre Max 5x passe de 19,3 à 12,2 mois (− 37 %), ce qui confirme « environ un tiers de moins ».
- Les prix de location en dollars (RunPod, Vast.ai) sont sans TVA : pour un particulier en France, ils peuvent être plus hauts.

## Pour le script : ce qu'on peut dire, ce qu'on ne dit pas

**Formulations sûres** (toutes datées du 23 octobre 2026)
1. « Je n'ai pas fait tourner Claude chez moi : ses poids ne sont pas publics. Alors j'ai fait le calcul, et voici d'où viennent les chiffres » (règle 1 du calculé ; #20).
2. « La RTX 5080 la moins chère est à 1 899,95 € chez LDLC et Materiel.net » (#10).
3. « Claude Pro, c'est 20 dollars par mois hors taxes ; avec la TVA et le taux du jour, environ 21 € » (#1, #4, #5 ; calcul, pas prix affiché).
4. « Contre un abonnement à 20 €, la carte n'est jamais rentable : plus de dix ans. Contre un Max à 100 dollars, il faut environ 19 mois, à 4 heures par jour » (calcul, #23).
5. « L'électricité, c'est le plus petit poste : de 7 à 22 € par mois, au tarif bleu d'EDF de 0,2001 € le kWh » (#17, #22).
6. « Louer une L4 de 24 Go chez Scaleway coûte 0,79 € de l'heure hors taxes » ; « une RTX 5080 se loue dès 30 centimes de dollar de l'heure sur Vast.ai » (#14, #16).
7. « En entreprise, Anthropic donne une moyenne de 13 dollars par développeur et par jour de travail, au token » (#8, #24).
8. « Cet été, cette carte est descendue à 1 200 € ; aujourd'hui, 1 900 € minimum » (#11, #25).
9. « Le Qwen de 27 milliards de paramètres pèse environ 16 Go en 4 bits : il tient tout juste dans la carte » (#20).
10. « Le tarif de l'électricité change en général le 1er février et le 1er août ; le prochain mouvement est le 1er février 2027 » (#17, #18).

**À ne pas dire, ou à dire autrement**
- « Ma 5080 consomme 300 à 450 W » comme une mesure : c'est une estimation tant que ⟦mesure de Claude #1⟧ n'existe pas (#19).
- « OpenAI a fermé le Pro à 200 $ » (#7).
- Les prix ChatGPT Pro à 103 ou 229 € sans les avoir relevés à la caisse (#6).
- « 2 723,99 € » et « la même carte a plus que doublé en trois mois » (#25).
- « 1 129 € à la sortie » face à un PNY à 2 039,98 € : dire « annoncée à 1 179 € » face à « 1 899,95 € aujourd'hui » (#26).
- Les prix OpenRouter de Kai (0,1312 / 2,378 $) (#21).
- « La carte remplace l'abonnement » : elle remplace un service plus petit (#20, #23).
- « RTX 5000 » sans dire que c'est une carte de 2018 (#13).
- « 13 $ : ce que coûte un développeur » sans « en entreprise » (#24).
- Un prix d'abonnement en euros présenté comme un prix affiché : c'est un calcul (#4).
