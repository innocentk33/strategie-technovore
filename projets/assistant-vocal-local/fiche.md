# Un assistant vocal sans Internet : que peut faire ton PC ?

**Jeudi 7 janvier 2027 à 18 h (Paris) · IA chez moi · Fiche · Documentaire calculé.** [Radar du 21 novembre](../../etudes/radar.md)

**Question du spectateur.** Tu veux parler à ta machine en français quand Internet est coupé. De quoi as-tu besoin pour allumer une lampe déjà connectée ? Et si tu veux lui poser une question libre ?

**Ouverture proposée.** « Huit secondes pour comprendre “allume la lumière”, tu attendrais ? C’est l’ordre de grandeur que donne Home Assistant pour transcrire une commande avec Whisper sur un Raspberry Pi 4. Pourtant, pour cette lampe, tu peux prendre un chemin plus court. »

**Avant 30 secondes**, montre les deux trajets de cette phrase, annonce où passe le son, ce qui prend du temps et le moment où un modèle de langage devient utile. Commence par la commande qui allume la lampe. Utilise un schéma et attribue les mesures à la documentation dans le visuel.

| Ce que tu veux faire | Ce que la vidéo montre |
|---|---|
| Commander une lampe en français | Speech-to-Phrase reconnaît des commandes prévues. Assist associe la commande à une action sur un appareil déjà configuré. |
| Poser une question libre | Whisper transcrit la phrase. Un agent équipé d’un modèle local doit ensuite produire la réponse. Piper peut la lire à voix haute. |
| Choisir le matériel | Compare les temps publiés pour la transcription sur Pi 4 et Intel NUC. Affiche à part les étapes dont on ignore la durée, jusqu’au premier son de la réponse. |

**À vérifier avant le script.** Documente la langue et la configuration de chaque mesure disponible. Le chiffre de huit secondes porte sur la transcription et la phrase d’ouverture illustre une commande. Vérifie le français pour chaque brique, les modèles à télécharger avant la coupure et le fonctionnement local de l’appareil commandé.

**Miniature proposée.** Un micro, un câble réseau débranché et « IL M’ENTEND ? », à vérifier à 168 px.

**Références techniques.** [Guide de configuration locale](https://www.home-assistant.io/voice_control/voice_remote_local_assistant/) · [Retour de Home Assistant sur le français et le Raspberry Pi 4](https://www.home-assistant.io/blog/2025/06/25/voice-chapter-10/).
