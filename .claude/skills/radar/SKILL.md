---
name: radar
description: Radar Technovore à faire à chaque sortie de vidéo (l'auteur dit qu'une vidéo est sortie, ou une vidéo publique de vidiq_user_videos n'est pas « Publié » dans le README). Mesure la vidéo précédente, surveille les concurrents et le public français avec vidIQ, puis choisit la vidéo du prochain créneau libre et met à jour radar.md, calendrier.md, README.md et strategie.md.
---

# Radar : à chaque sortie de vidéo

Fais le radar avant le reste. Il sert à choisir la vidéo du prochain créneau libre, en général celle du lundi N+2 : celle de N+1 est déjà en montage.

1. **Notre chaîne** (`vidiq_channel_stats`, `vidiq_channel_analytics` avec `filters: video==ID`) :
   - la vidéo précédente à J+7 : `engagedViews`, durée moyenne, % regardé, abonnés gagnés, sources de trafic, part de la France ;
   - sa courbe de rétention (`report: audience_retention`) : % de spectateurs à 0:15 (cible 75 %) et à 1:00 (cible 50 %) ;
   - ses 5 premières sources dans les suggestions (`dimensions: insightTrafficSourceDetail`, `filters: insightTrafficSourceType==RELATED_VIDEO;video==ID`, 5 crédits) : qui nous suggère, et combien de temps ces spectateurs restent ;
   - le CTR et les impressions ne passent pas par l'API : demande une capture de Studio.
2. **Concurrents** : la liste de surveillance de `etudes/radar.md`, avec un appel `vidiq_outliers` par langue (`channelIds`, `thisMonth`). Note ce qui fait ×2 ou plus.
3. **Public français** : `vidiq_outliers` en `language: fr` sur les mots-clés listés dans `etudes/radar.md`.
4. **Choix** :
   - candidats : la réserve d'`idees.md`, les idées de `strategie.md` et les signaux du radar ;
   - note sur 40 avec la grille de `strategie.md` (demande × clic × production × niche) ;
   - à note proche, préfère le sujet qui a une grosse vidéo française récente (100 K vues ou plus dans le mois) : sortir dans sa semaine nous place à côté d'elle dans les suggestions ;
   - règles :
     - 3 vidéos « IA chez moi » pour 1 vidéo « génie / histoire » (décidé le 05/11) ;
     - au plus 1 vidéo de tendance sur 3 ;
     - toutes les vidéos IA sont « calculées » : sources, mesures publiées par les utilisateurs, études et calculs, sans essai sur la RTX 5080 (décidé le 25/10, voir `strategie.md`, pilier 2). Exceptions filmées chez l'auteur : l'installation (2 nov.) et le test de Strata (16 nov., décidé le 05/11) ;
     - on ne copie pas l'angle ni la miniature d'un concurrent.
5. **Écris** :
   - une entrée datée en tête de `etudes/radar.md` (chiffres + décision) ;
   - puis `calendrier.md` (ligne « Mis à jour le … »), `README.md` et le classement de `strategie.md` ;
   - et la fiche si la vidéo choisie n'en a pas.

Budget : une quinzaine d'appels vidIQ (~75 crédits). Regarde `vidiq_balance` avant. Si un sujet chaud n'attend pas deux semaines, propose-le à l'auteur au lieu de bousculer le calendrier tout seul.
