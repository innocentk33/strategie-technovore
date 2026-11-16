# Sources : créer un petit jeu avec une IA locale

Recherche du **16 novembre 2026**. V1 documentaire : code, images, 3D et audio sont distingués. Aucune nouvelle génération, installation, capture ou mesure demandée à l'auteur. Aucun asset n'a été créé pour cette recherche.

| Fait | Information utilisable | Source, date | Statut et deuxième vérification |
|---|---|---|---|
| F1 | Archives Strata : **Coder IQ1_M, Pi 1.5.2, réflexion high, contexte 131 072, machine 16 Go VRAM + environ 32 Go RAM**. Casse-briques en 8 min 12 s, une demande, 493 lignes ; mini-Minecraft en 34 min 58 s avec 3 relances. Le premier message du mini-Minecraft prétend avoir écrit le fichier sans appel d'écriture. | `../strata-test/sources.md`, T41, relevé le 14/11/2026 ; chemins Windows documentés dans ce dossier | ✅ faits fournis relus deux fois dans le fichier ; ⚠️ rushes Windows non ouverts ici. Aucune nouvelle mesure personnelle revendiquée. |
| F2 | Rush existant `Tous les tests strata.mp4` : casse-briques avec vies/bonus ; mini-Minecraft avec déplacement et placement de blocs. Pas de console F12 ni version téléphone filmées. | Même dossier T45, `D:\_Technovore\Youtube\Strata test`, 14/11 | ✅ archive documentée, pas capture créée aujourd'hui. La finale dit « d’après les archives » et tient avec schémas si le rush est indisponible. |
| F3 | Code Strata sur carte 16 Go : résultats publics de T7 sur 5070 Ti + 32 Go RAM ; c'est une preuve de vitesse, sans vérification de justesse. | Dossier T7 ; https://github.com/Niko1221/Strata/issues/4997 (02/11/2026), ouvert et rouvert pendant recherche mémoire | ⚠️ mesure unique ; pas preuve qu'un jeu est correct ou commercialisable. Aucun tok/s ajouté ici. |
| F4 | SDXL base 1.0 génère des images ; base utilisable seule, refiner facultatif. | https://huggingface.co/stabilityai/stable-diffusion-xl-base-1.0 (sortie 26/07/2023, lu 16/11) | ✅ carte primaire ouverte puis rouverte. VRAM minimale fiable non spécifiée sur les pages lues : **aucune promesse chiffrée de fonctionnement sur 16 Go**. |
| F5 | SDXL 1.0 : CreativeML Open RAIL++-M, usages sous conditions, pas de restriction générale « non commercial ». Les droits de tiers ne sont pas garantis ; l'utilisateur reste responsable des sorties. | https://huggingface.co/stabilityai/stable-diffusion-xl-base-1.0/raw/main/LICENSE.md (26/07/2023) | ✅ licence primaire lue, version blob ouverte puis réouverte en brut ; pas de promesse « tout est libre de droits ». |
| F6 | Diffusers décrit déplacement de composants vers CPU pour réduire VRAM, avec compromis de performance. Pas un minimum universel. | https://huggingface.co/docs/diffusers/optimization/memory (16/11) | ✅ doc ouverte puis rouverte ; ne pas convertir taille de checkpoint en VRAM maximale. |
| F7 | TripoSR : reconstruction 3D depuis une image, environ 6 Go VRAM avec réglages par défaut ; MIT pour code ET poids préentraînés selon auteurs. | https://github.com/VAST-AI-Research/TripoSR (2024, consulté 16/11) | ✅ primaire ouverte puis rouverte ; ⚠️ exigence annoncée, pas deux mesures indépendantes. Le temps « <0,5 s » sur A100 n'est pas transposé à une carte de joueur. |
| F8 | MusicGen medium : documentation recommande au moins 16 Go GPU pour modèles moyens ; petits modèles/séquences possibles sur moins. | https://github.com/facebookresearch/audiocraft/blob/main/docs/MUSICGEN.md (16/11) | ✅ doc ouverte puis rouverte ; ⚠️ recommandation du projet, pas mesure sur notre carte. |
| F9 | AudioCraft : code MIT, poids CC-BY-NC 4.0. Ne pas recommander le workflow avec ces poids comme libre pour un projet commercial. | https://github.com/facebookresearch/audiocraft (16/11), section License | ✅ ouverte puis rouverte ; ne pas attribuer automatiquement la licence du code aux poids ou les restrictions des poids à toute sortie de façon non démontrée. |
| F10 | Godot est MIT et permet les jeux commerciaux ; texte de licence et notices tierces à conserver. | https://docs.godotengine.org/en/stable/about/complying_with_licenses.html (16/11) | ✅ doc primaire ouverte puis rouverte. La licence du moteur ne couvre pas tous les assets ajoutés. |
| F11 | Starter Kit 3D Platformer Kenney : code MIT ; sprites, modèles et sons CC0. | https://github.com/kenneyNL/Starter-Kit-3D-Platformer (copyright 2026, lu 16/11) | ✅ dépôt ouvert puis rouvert. Alternative d'assets documentée, pas créée ni testée dans cette tâche. |
| F12 | Proposition de workflow : code et assets produits par étapes séparées, libérant les ressources entre modèles ; une image n'est pas automatiquement une animation cohérente, et un objet reconstruit ne garantit pas collisions/rig/optimisation. | Déduction éditoriale de F1/F4/F6/F7/F10 ; pas un benchmark | ⚠️ conseil de production, pas nouvelle mesure ou promesse de jeu fini. |

## Double vérification et corrections

Les URL F4–F11 ont été ouvertes puis **rouvertes réellement**, avec relecture des exigences mémoire et licences. T41 et T45 du dossier Strata ont été relus ; aucun accès aux fichiers Windows n'est prétendu. F3 est la même source publique que le dossier mémoire, pas un nouveau benchmark.

- La démonstration de code ne prouve ni sprites, ni sons, ni 3D générés dans les mêmes 16 Go. La V1 l'explique.
- Le mini-Minecraft n'est pas présenté comme réussi au premier message. Les 3 relances et la fausse affirmation d'écriture font partie du résultat fourni.
- Aucune vitesse A100 de TripoSR n'est annoncée sur un GPU de jeu.
- MusicGen : code MIT ≠ poids MIT. La piste commerciale simple utilise plutôt des assets avec licence adaptée, tels les sons CC0 documentés.
- Aucun seuil SDXL inventé pour combler une absence de valeur. Le tableau affiche « dépend du pipeline ; minimum non certifié ».
- Exemples visuels d'outils : captures des pages officielles ou schémas légendés. Un rendu officiel n'est pas montré comme création de l'auteur. Les rushes existants ont une attribution d'archive explicite.

Requêtes : `site:huggingface.co/docs/diffusers SDXL "8GB"` ; `site:github.com/Stability-AI/generative-models SDXL "VRAM"`. Les licences ont été lues à la source ; aucun conseil juridique personnalisé. Le script ne transforme pas son budget VRAM en une garantie de workflow simultané.
