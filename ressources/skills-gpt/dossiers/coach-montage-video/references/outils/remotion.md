# Mise en œuvre : Remotion (React)

Remotion décrit une vidéo avec des composants React rendus image par image. Ce fichier traduit la méthode en recettes Remotion. Si les skills Remotion officiels sont disponibles dans l'environnement (`remotion-best-practices`, `remotion-markup`, `remotion-captions`…), ils font foi pour la syntaxe et les imports selon la version installée.

## Règles d'or
- Tout mouvement dépend de `useCurrentFrame()`. Les transitions et animations CSS, ou les classes d'animation Tailwind, ne se rendent pas correctement.
- Le temps se compte en **images**. À 60 i/s, une durée en secondes × 60 = images. Garder une petite fonction `const s = (sec: number) => Math.round(sec * fps)` évite les erreurs.
- Dans une `<Sequence from={…}>`, `useCurrentFrame()` repart de 0 : chaque animation peut être écrite comme si elle commençait au début.
- Aléatoire : uniquement `random('graine')` de `remotion` ou le bruit de `@remotion/noise`, jamais `Math.random()` (chaque image serait différente au rendu).
- Une animation réutilisable = un composant avec des props (l'équivalent d'un preset).

## Recettes

### Pop de texte (70 → 110 → 100 %)
```tsx
import { Easing, interpolate, useCurrentFrame } from "remotion";

export const PopText: React.FC<{ text: string; color?: string }> = ({ text, color = "#D9730D" }) => {
  const frame = useCurrentFrame();
  const scale = interpolate(frame, [0, 7, 12], [0.7, 1.1, 1], {
    extrapolateLeft: "clamp",
    extrapolateRight: "clamp",
    easing: Easing.out(Easing.quad),
  });
  return (
    <div style={{ transform: `scale(${scale})`, filter: `drop-shadow(0 0 12px ${color})` }}>
      {text}
    </div>
  );
};
```

### Zoom lissé avec point d'attention sur la règle des tiers
```tsx
const frame = useCurrentFrame();
const scale = interpolate(frame, [0, 45], [1, 1.3], {
  extrapolateRight: "clamp",
  easing: Easing.inOut(Easing.cubic),
});
// transformOrigin = le point qui reste fixe : le sujet, placé sur un tiers
<AbsoluteFill style={{ transform: `scale(${scale})`, transformOrigin: "33.3% 33.3%" }}>
  {/* plan */}
</AbsoluteFill>
```
Garder le même `transformOrigin` d'un plan à l'autre maintient le regard au même endroit entre les coupes.

### Tracé qui se dessine (équivalent Trim Paths)
```tsx
import { evolvePath } from "@remotion/paths";

const progress = interpolate(frame, [0, 30], [0, 1], {
  extrapolateRight: "clamp",
  easing: Easing.out(Easing.cubic),
});
const { strokeDasharray, strokeDashoffset } = evolvePath(progress, d);
<path d={d} fill="none" stroke="#fff" strokeWidth={6}
      strokeDasharray={strokeDasharray} strokeDashoffset={strokeDashoffset} />
```

### Texte machine à écrire
```tsx
const visible = Math.floor(
  interpolate(frame, [0, text.length * 2], [0, text.length], { extrapolateRight: "clamp" })
);
<span>{text.slice(0, visible)}</span>
```

### Overlay sur fond noir (mode Écran)
```tsx
import { Video } from "@remotion/media";
import { staticFile } from "remotion";

<Video src={staticFile("overlays/light-leak.mp4")} style={{ mixBlendMode: "screen" }} />
```
Pour les light leaks de transition, Remotion propose aussi `lightLeak()` (`@remotion/effects`) et les transitions `@remotion/transitions` (`TransitionSeries`).

### Bruitage calé sur un événement
```tsx
import { Audio } from "@remotion/media";

<Sequence from={s(12.4)}>          {/* instant de l'impact */}
  <Audio src={staticFile("sfx/impact.wav")} volume={0.4} />
</Sequence>
```
Un riser se place pour **finir** sur l'événement : `from = événement − durée du riser`.

### Étalonnage
`filter: "brightness(1.05) contrast(1.1) saturate(1.15)"` sur le plan, ou les effets `brightness()`, `contrast()`, `saturation()` de `@remotion/effects` pour les composants canvas.

## Montage 100 % code : traduction des étapes de la méthode

| Étape de la méthode | En Remotion |
|---|---|
| Projet 1920×1080, 60 i/s | `<Composition width={1920} height={1080} fps={60} durationInFrames={…}>` |
| Voix off découpée | Fichier audio de la voix off ; les débuts de passages viennent du script (minutage ou transcription horodatée) |
| Musique posée tout de suite | Piste audio sur toute la durée, volume réduit sous la voix |
| Script coloré | Un tableau de scènes `{ debut, duree, categorie, contenu }` qui génère les `<Sequence>` : la couleur devient le type de composant (VID, IMG, ECR, ANI, TXT, MEM) |
| Coupes sur le rythme | Liste des images des temps forts, utilisée pour caler les débuts de scènes |
| Sous-titres | `@remotion/captions` |
| Sound design | Une liste de bruitages `{ instant, fichier, volume }` rendue en `<Sequence>` |
| Prévisualiser / exporter | Remotion Studio pour prévisualiser, rendu en MP4 ; rendu avec transparence possible (ProRes 4444 ou WebM) pour importer une animation dans un autre logiciel |

Avantage pour la critique : comme tout est décrit en données, une remarque du rapport peut souvent se traduire par une modification précise d'une ligne du tableau de scènes.
