# Mise en œuvre : HyperFrames (HTML)

HyperFrames (open source, par HeyGen) décrit une vidéo en HTML : des éléments placés dans le temps avec des attributs `data-*`, animés par une bibliothèque « seekable » (GSAP le plus souvent, mais aussi CSS, Lottie, Three.js, Anime.js, WAAPI), puis rendus en MP4 par un navigateur sans interface et FFmpeg. Pas d'étape de build : le fichier `index.html` se prévisualise tel quel.

Le framework est jeune et évolue vite. Si les skills HyperFrames sont disponibles dans l'environnement (`/hyperframes`, `/hyperframes-core`, `/music-to-video`…), ils font foi. Sinon, ils s'installent avec `npx skills add heygen-com/hyperframes`, et la documentation est sur hyperframes.heygen.com.

## Règles d'or
- Le temps se compte en **secondes**. Les valeurs « en images » de la méthode se convertissent à 60 i/s (7 images ≈ 0,12 s).
- Chaque élément temporel porte `class="clip"`, `data-start`, `data-duration` et `data-track-index`.
- Les animations vivent dans une timeline GSAP **en pause**, enregistrée dans `window.__timelines[<id de composition>]` : c'est le moteur qui la positionne à chaque image. Les positions dans la timeline sont des instants de la composition.
- Déterminisme : pas d'animation liée à l'horloge réelle, pas de `Math.random()` évalué au rendu. Précalculer les valeurs aléatoires avec un générateur seedé.
- Les vidéos sont muettes (`muted playsinline`) ; le son passe par des éléments `<audio>`.
- Une animation réutilisable = une sous-composition ou un bloc du catalogue (l'équivalent d'un preset).

## Squelette de composition
```html
<div id="stage" data-composition-id="video" data-start="0" data-width="1920" data-height="1080">
  <!-- éléments .clip ici -->
  <script src="https://cdn.jsdelivr.net/npm/gsap@3/dist/gsap.min.js"></script>
  <script>
    const tl = gsap.timeline({ paused: true });
    // tweens ici
    window.__timelines = window.__timelines || {};
    window.__timelines.video = tl;
  </script>
</div>
```

## Recettes

### Pop de texte (70 → 110 → 100 %)
```html
<h1 id="titre" class="clip" data-start="2" data-duration="3" data-track-index="1"
    style="filter: drop-shadow(0 0 12px #D9730D)">Texte</h1>
```
```js
tl.fromTo("#titre", { scale: 0.7 }, { scale: 1.1, duration: 0.12, ease: "power2.out" }, 2)
  .to("#titre", { scale: 1, duration: 0.08, ease: "power1.inOut" });
```

### Zoom lissé avec point d'attention sur la règle des tiers
```html
<div id="camera" class="clip" data-start="10" data-duration="4" data-track-index="0"
     style="transform-origin: 33.3% 33.3%"> <!-- plan --> </div>
```
```js
tl.fromTo("#camera", { scale: 1 }, { scale: 1.3, duration: 0.75, ease: "power2.inOut" }, 10);
```
Garder le même `transform-origin` d'un plan à l'autre maintient le regard au même endroit entre les coupes.

### Tracé qui se dessine (équivalent Trim Paths)
```js
const path = document.querySelector("#fleche");
const len = path.getTotalLength();
gsap.set(path, { strokeDasharray: len, strokeDashoffset: len });
tl.to(path, { strokeDashoffset: 0, duration: 0.5, ease: "power2.out" }, 4);
```

### Texte machine à écrire
```js
const el = document.querySelector("#machine");
el.innerHTML = [...el.textContent].map(c => `<span style="opacity:0">${c}</span>`).join("");
tl.to("#machine span", { opacity: 1, duration: 0.01, stagger: 0.035 }, 5);
```

### Overlay sur fond noir (mode Écran)
```html
<video class="clip" src="overlays/light-leak.mp4" data-start="8" data-duration="1.5"
       data-track-index="3" muted playsinline style="mix-blend-mode: screen"></video>
```
Le catalogue propose aussi des transitions prêtes à l'emploi (par exemple `npx hyperframes add flash-through-white`) et le paquet `@hyperframes/shader-transitions`.

### Bruitage calé sur un événement
```html
<audio src="sfx/impact.wav" data-start="12.4" data-duration="1" data-track-index="5" data-volume="0.4"></audio>
```
Un riser se place pour **finir** sur l'événement : `data-start = événement − durée du riser`.

### Étalonnage
`filter: brightness(1.05) contrast(1.1) saturate(1.15);` sur le plan.

## Montage 100 % code : traduction des étapes de la méthode

| Étape de la méthode | En HyperFrames |
|---|---|
| Projet 1920×1080, 60 i/s | `data-width` / `data-height` sur la composition ; cadence choisie au rendu (voir l'aide de `npx hyperframes render`) |
| Voix off découpée | Un `<audio>` pour la voix off ; les débuts de passages viennent du script (minutage ou transcription horodatée) |
| Musique posée tout de suite | `<audio>` sur toute la durée, `data-volume` réduit |
| Script coloré | Chaque passage devient un `.clip` ; la couleur indique le type d'élément (VID, IMG, ECR, ANI, TXT, MEM) |
| Coupes sur le rythme | `data-start` calés sur les temps forts ; skill `/music-to-video` quand la musique doit piloter le montage |
| Sous-titres, voix IA, animation réactive au son | Gérés par les skills HyperFrames |
| Prévisualiser / exporter | `npx hyperframes preview` puis `npx hyperframes render` (Node.js 22+ et FFmpeg requis) |

Migration : le skill `/remotion-to-hyperframes` porte une composition Remotion existante vers HyperFrames.
