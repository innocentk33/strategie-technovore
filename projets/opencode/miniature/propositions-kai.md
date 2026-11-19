# Miniatures Kai — 19/11 — opencode

Nouvelles variantes h/i/j du 19 novembre 2026. Les anciens PNG, PSD, maquettes, propositions.md et tout script de rendu préexistant sont conservés. Compétences appliquées : miniature-kai, coach-miniature-youtube et imagegen intégré. Base des prompts : prompts-chatgpt-31-12.md. Références visuelles : anciennes variantes du projet, série Kai approuvée du 16/11, Archivo Black locale.

**Titre associé dans upload.md :** OpenCode piraté : j'ai lu le code, tes clés API étaient rangées telles quelles

**Texte :** TES CLÉS / VOLÉES ?

**Concept :** Le vrai mot-symbole OpenCode, une grande clé physique symbolique et Kevin Hart sidéré. La clé est un dessin générique : aucun texte de credential, même partiel, aucune vraie clé API. Le visage regarde le texte à gauche. La variante i agrandit logo et clé et enlève le visage.

**Promesse tenue par la vidéo :** Le script distingue clairement l’application locale de la Console touchée. La question interroge le risque historique de vol raconté dans cette vidéo, sans affirmer que les clés de chaque spectateur ont fuité. Elle ne vise pas une nouvelle attaque ni tous les utilisateurs d’OpenCode. Aucun assaillant identifié, aucun point d’entrée supposé, aucun montant ou nombre de victimes ajouté. Le titre raconte l’examen du code ; la miniature concentre l’enjeu personnel.

| Variante | Palette | Composition |
|---|---|---|
| h | noir calme, blanc, jaune #ffcc33 ; ombres rouge/bleue | texte à gauche, portrait illustré à droite regardant le texte, scène sous l’accroche |
| i | fond uni #141e27, menthe #07c095, copie du mot accentué blanche | sans visage, texte sur une ligne en haut, objets agrandis dessous |
| j | palette Technovore identique à i ; peau naturelle | même scène et même portrait que h |

Le vrai logo garde ses couleurs dans les trois variantes. Archivo Black, trois textes droits (ligne1, copie décalée, segment accentué). L’écart vertical entre le bas des lettres/ombres et les objets est visible ; aucune tuile ne touche l’accroche. Aucun objet essentiel dans le coin de la durée.

## Sources et reproduction

- propositions/miniature-kai.html?v=h|i|j : HTML/CSS/SVG modifiable.
- sources/kai-2026-11-19/ : portrait brut, détourages, habillages, logos exacts, prompts et provenance.
- rendre-kai.sh : les trois PNG 3840×2160 et les trois planches ; `--psd` réexporte aussi les PSD.
- export-kai-psd.py : utilise ressources/miniatures/psd.py avec profils Chrome temporaires.
- rendus/{h,i,j}-kai.png et photocraft/{h,i,j}-kai.psd : fichiers nouveaux distincts des anciennes versions.
- apercu/kai/comparaison-168px.png, comparaison-640px.png, comparaison-50-pourcent.png : vrais tests de lecture et moitié basse masquée.

Les PSD contiennent le décor raster et trois calques de texte modifiables ; objets, logos et portrait peuvent être modifiés séparément dans les sources HTML/SVG/PNG puis réexportés. Les polices Archivo Black sont installées localement.

## Contrôle indépendant

Revue indépendante des trois variantes achevée par lot_materiel : [critique-kai.md](critique-kai.md). Les PNG finaux sont approuvés, avec leurs SHA-256 complets consignés. Le classement éventuel est une hypothèse ; aucun résultat public de CTR ou de test YouTube n’est inventé. Tester h/i/j à titre constant, sans publication ou modification de YouTube effectuée par cette production.

## Contrôle technique

Les dimensions PNG sont 3840×2160. Les contrôles de PSD reconverti, calques texte, écarts et empreintes sont consignés dans apercu/kai/validation.md. Le test 50 % conserve toute l’accroche ; il ne prétend pas conserver tous les objets du bas.

Correction de relecture appliquée avant livraison : ajout du point d’interrogation à VOLÉES ? pour distinguer le risque du spectateur de la fuite historique de la Console. PNG, PSD et planches ont été régénérés après ce changement.
