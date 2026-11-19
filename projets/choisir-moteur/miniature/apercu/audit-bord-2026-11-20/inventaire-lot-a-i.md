# Audit du bord inférieur — lot a–i — 20/11/2026

**26 PNG réellement rendus, 13 projets inspectés ; quatre corrigés, 22 sains et inchangés.** Recherche de toutes les variantes h*/j* dans les dossiers de rendus, sans présumer le suffixe `-kai`. Aucune autre variante h/j sans ce suffixe n’existe dans ce lot. Les sources, références et reconversions PSD ne sont pas comptées comme des variantes supplémentaires.

Chaque composition a été regardée en entier puis sur une bande inférieure agrandie. Les contours qui suivent une vraie silhouette (cheveux, peau, vêtement ou matériel) ne sont pas classés comme défauts. Seul un trait horizontal parasite sous une coupe droite de buste a été corrigé.

## Inventaire par projet

| Projet | Variantes examinées | Verdict final |
|---|---|---|
| artcraft | h-kai.png, j-kai.png | sain, inchangé |
| bases-ia-locale | h-kai.png, j-kai.png | sain, inchangé |
| cadeau-ia-locale | h-kai.png, j-kai.png | sain, inchangé |
| carte-par-budget | h-kai.png, j-kai.png | sain, inchangé |
| cartes-minage | h-kai.png, j-kai.png | sain, inchangé |
| choisir-moteur | h-kai.png, j-kai.png | corrigé et revalidé |
| claude-code-gratuit | h-kai.png, j-kai.png | corrigé et revalidé |
| claude-ou-mon-pc-1 | h-kai.png, j-kai.png | sain, inchangé |
| cout-claude-local | h-kai.png, j-kai.png | sain, inchangé |
| cout-deepseek-flash | h-kai.png, j-kai.png | sain, inchangé |
| deux-cartes-occasion | h-kai.png, j-kai.png | sain, inchangé |
| ia-locale-privee | h-kai.png, j-kai.png | sain, inchangé |
| installer-ia-locale | h-kai.png, j-kai.png | sain, inchangé |

## Correction confirmée

choisir-moteur h/j et claude-code-gratuit h/j : dans leurs maquettes HTML, top du portrait 10→30 px, largeur 730 px conservée. Le bord droit du buste et ses ombres passent sous le cadre. Textes, logos, décor et i inchangés. PNG et PSD réexportés en 3840 × 2160 ; trois calques Type Archivo Black par PSD. Les quatre PSD ont été réouverts en PNG et les preuves locales actualisées. Les i sont vérifiées identiques par hashes PNG/PSD.

Contre-revue indépendante : lot_modeles a regardé les quatre compositions à 640 px et leur bord inférieur détaillé ; elles sont validées avec empreintes complètes dans les critique-independante.md et critique-logos.md des deux projets. Les anciennes signatures sont conservées comme historiques.

Les comparaisons avant/après et mesures sont dans chaque `apercu/audit-bord-2026-11-20/`. Aucun fichier de galerie globale ni aucune opération Git n’a été effectué par cet audit.

## Empreintes complètes des PNG finaux

| PNG | État final | SHA-256 |
|---|---|---|
| `projets/artcraft/miniature/rendus/h-kai.png` | sain, inchangé | `40016b1f77a8cd729cee8f2152686738be369ed559c976c1ec92602eb9539dd9` |
| `projets/artcraft/miniature/rendus/j-kai.png` | sain, inchangé | `85103c1d5de4570f5d06fdee5ecd3a15ba1ac5d14c515312a1cf2e5ad3a59fc4` |
| `projets/bases-ia-locale/miniature/rendus/h-kai.png` | sain, inchangé | `5a355397fae7106e65fb5a699635d6218115b4eb7edb3c8c0dbfc996bd79364c` |
| `projets/bases-ia-locale/miniature/rendus/j-kai.png` | sain, inchangé | `88670db87532ed6e7919ac1e9484f1a90b4680e6828e8464862ccb56283c9e2d` |
| `projets/cadeau-ia-locale/miniature/rendus/h-kai.png` | sain, inchangé | `748e0731fc96fdc319537495af67de43922fb3cc2b2452dab517b6e54da28bee` |
| `projets/cadeau-ia-locale/miniature/rendus/j-kai.png` | sain, inchangé | `4bee1bd766cc9738058c8831f5aef7ba7716e08b3e107e434ab130974a85097d` |
| `projets/carte-par-budget/miniature/rendus/h-kai.png` | sain, inchangé | `03306b3619551be3bab611db74ca28c6f60a72d0dea9a543cc0b898eeec83a3e` |
| `projets/carte-par-budget/miniature/rendus/j-kai.png` | sain, inchangé | `e634f60650730a65d77ef7dcb8b385e7a47bc2e5c14d9a15e74418c0ede6f430` |
| `projets/cartes-minage/miniature/rendus/h-kai.png` | sain, inchangé | `35126b0dff792b81ec90853cd0ba5b34bfb085565b1efe3fc31d115b8d7dd72f` |
| `projets/cartes-minage/miniature/rendus/j-kai.png` | sain, inchangé | `0badbd0fc713770d93c36e835aa7d0942876e2ae0ea20512f4ce74a88157c4a9` |
| `projets/choisir-moteur/miniature/rendus/h-kai.png` | corrigé et revalidé | `6b3e0c9ad13fe91d527d2f0ea2565c0ebecf29e768bebef8c8d23cdae084c79a` |
| `projets/choisir-moteur/miniature/rendus/j-kai.png` | corrigé et revalidé | `60890b751fe1c3da94ed32f3ca2ed233c6e9fcf28b2752af0a125c0e631fce22` |
| `projets/claude-code-gratuit/miniature/rendus/h-kai.png` | corrigé et revalidé | `7de1fe57cca38dc801d48e40e4f2180a9b860047e15d937152ba99baf8fb7b9c` |
| `projets/claude-code-gratuit/miniature/rendus/j-kai.png` | corrigé et revalidé | `1cee9f7434d887ac945140fae3dbc42491a946898a2aa46c1e70816d1d91a8ef` |
| `projets/claude-ou-mon-pc-1/miniature/rendus/h-kai.png` | sain, inchangé | `9b575c804ba8c94b7ed302a0f610fe2129baa610d0ad16cee47dec11234bd817` |
| `projets/claude-ou-mon-pc-1/miniature/rendus/j-kai.png` | sain, inchangé | `39db82c9b59baf550b004439404373f6923c1a716174668c448ba852ca7492ba` |
| `projets/cout-claude-local/miniature/rendus/h-kai.png` | sain, inchangé | `f32d8acf7467e0ca36d1eeb113b10b3bd594ccbdf6ee4de9e80dbdaf78e0271a` |
| `projets/cout-claude-local/miniature/rendus/j-kai.png` | sain, inchangé | `b98a8e291679d36653ab5a1993b68d8608159a4affe9801a44e449f992222076` |
| `projets/cout-deepseek-flash/miniature/rendus/h-kai.png` | sain, inchangé | `cef2231a6137fb076411e2dea2641317de3f69f23a77957584f9e76b23319abe` |
| `projets/cout-deepseek-flash/miniature/rendus/j-kai.png` | sain, inchangé | `fc4ee95238c95849986199b1c12c54d7e5cc0c08aaa305ccfffcbfc48a8e1f7b` |
| `projets/deux-cartes-occasion/miniature/rendus/h-kai.png` | sain, inchangé | `b7e43e67a31113de102f5dac0769cef7e92fbb087c5419515cb8a2bf1337c4d3` |
| `projets/deux-cartes-occasion/miniature/rendus/j-kai.png` | sain, inchangé | `943fffca9fdb78cd1b70865e59d0909208a338fa34b6e42d825781b89e9009a6` |
| `projets/ia-locale-privee/miniature/rendus/h-kai.png` | sain, inchangé | `f2b7f873152dd2a7ad7e123ea59cee09c07f5d986713abc2a204c4ecaa1edb3c` |
| `projets/ia-locale-privee/miniature/rendus/j-kai.png` | sain, inchangé | `4688f08b18ad1434daf63c3bcd4d37a7b90681ece7668171c6ffb6c1b8c03a6e` |
| `projets/installer-ia-locale/miniature/rendus/h-kai.png` | sain, inchangé | `23844d46df3413b607c762a15ba7d4d7c4f751f67a86e3d2ccf09aeace6fff3d` |
| `projets/installer-ia-locale/miniature/rendus/j-kai.png` | sain, inchangé | `72131109200916c452262c7727557246381137d18b81b50fb9a7d09c357ba0ae` |
