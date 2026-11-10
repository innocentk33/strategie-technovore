# Le génie caché du paiement sans contact

> Analyse (hook, pourquoi, score) : [`strategie.md`](../../strategie.md), idée 19. Planning : [`calendrier.md`](../../calendrier.md), **lun. 5 avr. 2027 à 18 h, provisoire**. Recherche : [`sources.md`](sources.md) (phase 1 du 23/10/2026).

| Champ | Détail |
|---|---|
| **Pilier** | Le génie derrière l'app (Hub) |
| **Format** | Longue, 9-11 min |
| **Trafic visé** | Accueil + suggestions (à côté de ByteMonk et des vidéos « comment ça marche » sur Face ID) |
| **Mot-clé** | paiement sans contact / apple pay sécurité (« paiement sans contact » < 750 recherches/mois en France au 23/10/2026 ; « nfc » 115 575/mois dans le monde) |
| **Type de hook** | Choc (chiffre) |
| **Production estimée** | ~25 h (estimation : animations de tap NFC, de jeton et de code à usage unique ; pas de carte, donc plus léger qu'Uber) |

**Titres** :
1. Recherche : *Comment fonctionne le paiement sans contact ?*
2. Curiosité : *Ton téléphone paie sans jamais donner ton numéro de carte*
3. Mixte (recommandé, à valider par toi) : *Comment ton téléphone paie sans jamais donner ton numéro de carte*

> Le titre dit « téléphone » exprès : une **carte** physique sans contact envoie bien son numéro, c'est le **téléphone** (Apple Pay, Google Wallet) qui envoie un faux numéro (voir `sources.md`, faits 11 à 15).

**Miniature** : à faire. Piste (charte noire) : un téléphone qui touche un terminal, deux numéros de carte, l'un barré. À concevoir quand la vidéo se rapproche, après avoir regardé les miniatures des vidéos hôtes (règle « Suggestions » de `CLAUDE.md`).

**Les 15 premières secondes** (règle du 22/10, `strategie.md`, section 5) : le chiffre le plus fort d'abord. Piste, à faire confirmer en phase 2 : *« En 2025, en France, 9 euros de fraude pour 100 000 euros payés avec un téléphone en magasin. Avec la carte : 47. »* (Banque de France, rapport 2025 de l'Observatoire de la sécurité des moyens de paiement, communiqué du 7/09/2026). Puis la question centrale avant 30 s : *comment ton téléphone peut-il payer sans que le magasin voie ton numéro de carte ?* Pas de contexte, pas de « dans cette vidéo ».

**Texte et sous-texte** (le « problème de surface / problème profond » du skill grill) :
- **Texte** : ce qui se passe en moins d'une seconde quand tu poses ton téléphone sur un terminal : le numéro de remplacement (le « jeton »), la puce qui garde le secret (l'élément sécurisé), le code à usage unique.
- **Sous-texte** (proposé, à valider par toi) : tu n'as pas à faire confiance à la caisse, au terminal ni au réseau du magasin. Le système ne cache pas ton numéro : il t'évite d'en avoir besoin, et ce qu'il envoie ne sert qu'une fois. La sécurité vient de la conception, pas de la confiance.

**Contenu** (ordre proposé) :
1. Le geste banal : tu poses ton téléphone, ça bipe. Le chiffre de la Banque de France.
2. Le problème : un terminal inconnu, un magasin inconnu, quelques centimètres d'air. Ce que le NFC envoie (portée, quelques millimètres à centimètres).
3. Premier tour : le numéro de remplacement (DAN chez Apple, DPAN chez Google). Il est créé une fois, à l'ajout de la carte, avec la banque ou le réseau (Visa, Mastercard, etc.).
4. Deuxième tour : l'élément sécurisé. La puce qui ne parle qu'après ton visage ou ton code.
5. Troisième tour : le code à usage unique (cryptogramme, compteur de transaction, nombre imprévisible du terminal). Pourquoi on ne peut pas rejouer un paiement.
6. La limite honnête : les plafonds (50 € par paiement en France, vérifié le 10/09/2026), la carte physique qui, elle, envoie son numéro, et les attaques de « pré-lecture » (Cambridge, 2012) quand le nombre imprévisible ne l'est pas.
7. Ce que ça change pour toi : paie avec le téléphone plutôt que la carte physique si tu veux le plus sûr (chiffre de fraude).

**Référence** : ByteMonk, *The Hidden Security Magic Behind Mobile Payments* (195 K vues, ×4,4, 5:40, 04/05/2025). On en tire la structure (Apple : élément sécurisé + DAN ; Google : jeton ; compromis), **pas le texte**. Attention : ByteMonk dit que Google Pay garde le jeton dans le cloud et en redemande un à chaque paiement ; la documentation Google pour les développeurs dit que le jeton est **stocké sur l'appareil** (`sources.md`, fait 15). Ne pas reprendre ce point.

**À vérifier** (devenu `sources.md`, faits 1 à 24) :
- le plafond du sans contact en France (50 € par opération, service-public.gouv.fr, vérifié le 10/09/2026, avec date) et le cumul fixé par la banque ;
- la portée du NFC (NFC Forum : « jusqu'à 2 cm », conformité certifiée à 5 mm) ;
- l'élément sécurisé (Apple) et la certification EMVCo / Common Criteria ;
- le numéro de compte de l'appareil (DAN) et le cryptogramme ;
- pourquoi on ne peut pas rejouer un paiement (compteur + nombre imprévisible) et la limite (attaque de pré-lecture) ;
- le chiffre de fraude mobile (Banque de France 2025) ;
- Google Wallet : comment le cryptogramme est produit sans élément sécurisé (HCE) : non retrouvé dans la documentation lue ;
- **le public africain** : quelle part de ton audience paie par NFC ? Le paiement mobile dominant en Afrique francophone passe par le mobile money (Orange Money, Wave, etc.), pas par le NFC [à demander à l'auteur / à vérifier]. **Ta réponse (23/10)** : le sans contact est utilisé en Afrique.

## Corrections de la 2e vérification (23/10)

- **Les 15 premières secondes** : « 9 euros avec un téléphone, 47 avec la carte » est trompeur. Le 47 est la moyenne de toute la carte, **internet compris** (124). En magasin, en 2025, le sans contact est aussi à 9 € pour 100 000 € (rapport complet de l'OSMP, graphique G11). Piste juste : « Sur internet, la carte se fait frauder 124 euros pour 100 000. Posée sur un terminal sans contact : 9. »
- **Point 7 du contenu** (« paie avec le téléphone si tu veux le plus sûr, chiffre de fraude ») : les chiffres ne le montrent pas (9 € des deux côtés en 2025 ; le téléphone était plus fraudé en 2023 et 2024). Garde l'argument technique : le téléphone ne donne pas ton numéro.
- **« La carte physique envoie son numéro »** : maintenant sourcé (Newcastle, ACM CCS 2014 ; Black Hat Europe 2019). Le titre tient.
- **Point 5** (« pourquoi on ne peut pas rejouer un paiement ») : dis « une banque bien faite refuse un compteur déjà vu » ; en 2019, des chercheurs ont montré que ce n'est pas toujours le cas. Voir `sources.md`, faits 16, 19 et lignes 25 à 31.
