# Être suggéré : où YouTube place nos vidéos (23/10/2026)

> Fait avec le skill `/youtube`. Chiffres vidIQ du 23/10/2026 (`vidiq_channel_analytics`, `insightTrafficSourceType==RELATED_VIDEO`, dimension `insightTrafficSourceDetail`). L'API ne rend que les 25 premières sources ; la liste complète est dans Studio > Statistiques > Contenu > Sources de trafic > Vidéos suggérées. La procédure qui en sort est dans [`CLAUDE.md`](../CLAUDE.md) (« Un dossier projet », étape 8, et « Radar »).

## Le principe

On ne choisit pas les vidéos à côté desquelles on est suggéré : YouTube nous place à côté de celles que regardent les mêmes spectateurs, puis continue si ceux qui cliquent restent. On agit donc sur le sujet, le moment de sortie, la miniature face à ces vidéos et l'enchaînement de nos propres vidéos.

## Les chiffres

**Toute la chaîne (23/07 → 23/10)** : les suggestions viennent presque toutes de tutos Flutter français (B2A Tech 39 vues, Menttor iO 27, Caoch Kurty 26, Driss AS, SleentO, Djiby Sensei), plus notre formation `M_kTIYcak8o` (15). Elles nourrissent l'ancien catalogue, pas le nouveau format.

**ArtCraft (19 → 23/10)** :

| Vidéo qui suggère ArtCraft | Vues | Durée moyenne |
|---|---|---|
| Basti Sans MS, « La fin de ADOBE à cause de cette version GRATUITE ? » (`-oykj1GrxUQ`, 181 K vues, sortie le 18/10) | 7 | 2 min 04 |
| Tech_Sama (GPU), Vision IA, ThePrimeagen, joepkg (sur ArtCraft) | 2 à 5 chacune | 58 s à 6 min 13 |
| Le Potager (rap), LIMIT (actualité), Radio Nova | 2 à 5 chacune | 0 à 18 s (sauf 2 vues de Radio Nova, trop peu pour conclure) |

**Lecture** :
- la première source est une grosse vidéo française du même sujet sortie la veille, dont le titre partage probablement nos mots (« Adobe », « gratuit ») ;
- YouTube nous a aussi testés sur un public français généraliste, qui ne clique pas et part en quelques secondes : c'est une partie du CTR de 0,9 % ;
- le public tech reste plusieurs minutes : c'est lui qu'on vise.

## Les 5 leviers

1. **Sortir dans la semaine d'une grosse vidéo française du même sujet** (100 K vues ou plus dans le mois). On reprend les mots de son titre, jamais son angle ni sa miniature.
2. **Gagner le clic à côté d'elle** : notre miniature passe sur une planche, à 168 px, entre 4 ou 5 vidéos où l'on risque d'être suggéré. La question : qu'est-ce que la nôtre promet que la leur ne dit pas ? Repère : CTR moyen des suggestions de 9,5 % (guide du skill, une seule agence, décembre 2025) ; notre objectif est d'au moins 3 %.
3. **Enchaîner nos vidéos** :
   - écran de fin avec une seule vidéo, la suivante de la playlist du même pilier ;
   - une fiche pendant le plateau de rétention (3:20 à 8:40 sur ArtCraft), là où il reste du monde : seulement 8 % des spectateurs voient l'écran de fin ;
   - playlists par pilier, dans l'ordre, en avant sur la page de la chaîne ;
   - écran de fin et fiche vers le nouveau format sur la formation et la vidéo d'installation (environ 2 300 vues par mois).
4. **Garder ceux qui cliquent** : c'est la règle des 15 premières secondes. Le public généraliste qui part en 18 s n'est pas grave ; il faut que le public tech passe 1:00 (cible 50 %).
5. **Garder les tutos Flutter publics** : les autres tutos Flutter les suggèrent et ils font nos heures de visionnage.

Tags et description pèsent peu ici : c'est surtout qui regarde, et combien de temps.
