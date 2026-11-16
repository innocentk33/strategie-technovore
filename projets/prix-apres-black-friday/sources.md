# Sources — bilan Black Friday, préparation du 16/11/2026

**Statut : recherche actuelle vérifiée ; résultat futur indisponible.** Publication prévue17/12/2026. Le Black Friday27/11 et les relevés de décembre sont futurs au jour de rédaction. Le script sera écrit entièrement, mais les blocs de résultat et le verdict chiffré restent conditionnés à ces relevés. Aucun résultat futur inventé. Aucun essai matériel demandé à l'auteur.

## Faits et calculs

**F1 ✅ — Prix de référence d'une réduction.** https://www.economie.gouv.fr/dgccrf/les-fiches-pratiques/annonces-de-reduction-de-prix-ce-que-vous-devez-savoir, publication **25/08/2026**, ouvert puis rouvert **16/11/2026**. Une annonce de réduction renvoie au prix le plus bas pratiqué par le professionnel pendant les **30 jours** précédents. Une comparaison avec le prix conseillé ou celui d'autres vendeurs est une autre opération, à indiquer clairement. Ne pas accuser un marchand d'illégalité sans dossier.

**F2 ✅ — Texte juridique recoupé.** https://www.legifrance.gouv.fr/codes/article_lc/LEGIARTI000044549592, article **L112-1-1**, en vigueur depuis **28/05/2022**, version affichée au16/11/2026, ouvert puis rouvert aujourd'hui. Confirme30jours ; exception réductions successives sur période déterminée ; exclusions denrées périssables et comparaisons interprofessionnels. Le script donne règle générale cartes graphiques, sans avis juridique individuel.

**F3 ✅ — Référence16Go observée avant l'événement.** https://www.ldlc.com/fiche/PB00676833.html, relevé **16/11/2026**, ouvert puis rouvert. ASUS Dual GeForce RTX5060Ti OC Edition **16GB**, prix affiché **1079,95€ TTC** sur site français grand public, **en stock**, **1 par client**. Prix produit, livraison non relevée. Ce n'est ni le minimum du marché ni une preuve de meilleur achat. Même SKU à suivre, éviter confusion ASUS Prime/Dual.

**F4 ✅ — Référence32Go observée avant l'événement.** https://www.ldlc.com/fiche/PB00711272.html, relevé **16/11/2026**, ouvert puis rouvert. Gigabyte Radeon AI PRO R9700 AI TOP **32G**, référence **GV-R9700AI TOP-32GD**, prix affiché **2799,95€ TTC**, en stock. Prix produit, livraison non relevée. Pas de vitesse IA tirée du marketing de la fiche.

**F5 ⚠️ — Prévision de marché, pas prix de boutique.** https://www.trendforce.com/presscenter/news/20260930-13258.html, daté **30/09/2026**, ouvert via lien redirigé puis rouvert directement **16/11/2026**. Prévision **+10–15% trimestriels** pour les prix contractuels de DRAM conventionnelle au4e trimestre2026 ; **+15–20%** pour NAND. Ni mesure finale du trimestre, ni hausse uniforme trimestrielle DRAM/GDDR, ni pourcentage à appliquer aux cartes vendues en France. La fiche « environ20% par trimestre » est trop générale et non confirmée ; retirée.

**F6 — CALCUL défini, entrées futures absentes.** Variation prix produit = `(prix_final - prix_initial) / prix_initial × 100`. Économie = `prix_initial - prix_final`. Le dénominateur dépend de la question : avant→BF, BF→décembre, avant→décembre. Vérification algébrique : `prix_final = prix_initial × (1 + variation/100)`. Aucun montant futur substitué dans ces formules.

**F7 ❌ — Résultats Black Friday et décembre indisponibles aujourd'hui.** Dates prévues par `calendrier.md` : relevés20/11 et26/11, BF27/11, puis mi-décembre. Ils ne peuvent pas être certifiés16/11. Chaque case future porte `[PRIX À RELEVER]` et son statut stock. Aucune ancienne fiche ou snippet remplacée par une preuve datée du futur.

**F8 ⚠️ — Limite d'échantillonnage.** Panel de deux références chez un vendeur, choisi pour suivre16et32Go. C'est une méthode éditoriale ; pas un indice statistique du marché. Un résultat pour ces références ne répond pas à toutes les cartes, ni à tous les pays. Les prix français ne sont pas un devis livré en Afrique.

**F9 — Critère éditorial de service rendu.** Le coût pour l'IA dépend aussi du fichier qui tient, du contexte et de la compatibilité moteur. Références fournies : `../qwen-27b-8go/sources.md` F1/F3/F4/F9, relues localement16/11 ; leur double ouverture est documentée là-bas. Pas de vitesse nouvelle attribuée aux références F3/F4. Ne pas convertir euros par Go en classement universel de performance.

**F10 — Programmation.** `../../calendrier.md` fourni : publication17/12, prochaine21/12 « comment lire le nom d'un modèle », puis24/12 cadeau. Le script du17 utilise la vidéo budget26/11 et32Go30/11 comme publications passées à sa date prévue, jamais comme faits déjà publiés16/11.

## Tableau de suivi

| Référence exacte |16/11 TTC affiché|20/11|26–27/11|Mi-décembre|Stock à chaque date|
|---|---:|---|---|---|---|
|ASUS Dual5060Ti OC16GB, LDLC PB00676833|1079,95€|[PRIX À RELEVER]|[PRIX À RELEVER]|[PRIX À RELEVER]|16/11 en stock,1/client ; futurs à relever|
|Gigabyte R9700 AI TOP32G, LDLC PB00711272|2799,95€|[PRIX À RELEVER]|[PRIX À RELEVER]|[PRIX À RELEVER]|16/11 en stock ; futurs à relever|

Les relevés du20/11 complètent le point initial ; ils ne doivent pas effacer le16/11. Livraison/condition coupon/reprise/abonnement à consigner séparément. Une rupture reste une rupture, pas un prix achetable.

## Deuxième vérification,16/11

- DGCCRF rouverte :30jours et exception des comparaisons relus ; accord avec Légifrance rouvert.
- LDLC5060Ti rouverte :1079,95€, Dual OC16, stock et1/client relus.
- LDR9700 rouverte :2799,95€,AI TOP32G, stock relus.
- TrendForce rouvert :10–15% DRAM,15–20% NAND, prévisionsQ4 ; correction du20%uniforme de la fiche.
- Formule vérifiée par inversion, sans inventer valeurs.
- Aucune deuxième vérification des dates futures prétendue.
