#!/usr/bin/env python3
"""Portrait « à la manière de Kai » pour les miniatures (15/11/2026).

Prend un portrait illustré sur fond vert uni (généré avec ChatGPT), le détoure et écrit trois fichiers :
  <sortie>/portrait-illustre-detoure.png   le visage seul, fond transparent
  <sortie>/portrait-kai.png                contour blanc + ombres décalées rouge et bleue (variante h)
  <sortie>/portrait-technovore.png         couleurs de peau gardées, contour blanc épais, ombres menthe et ardoise,
                                           halo sombre (variante j ; pas de duotone : il écrasait le contraste)

Usage : python3 -I ressources/miniatures/portrait.py <image fond vert> <dossier sources/> [nom]
  avec [nom] (ex. fry) : portrait-fry-detoure.png, portrait-fry-kai.png, portrait-fry-technovore.png
Les deux portraits ont une marge de 40 px (à 1x) autour du visage : la maquette les place avec left/top/width.
"""
import sys
from pathlib import Path

import numpy as np
from PIL import Image, ImageChops, ImageFilter


def detoure(path):
    im = Image.open(path).convert("RGB")
    a = np.asarray(im).astype(int)
    r, g, b = a[..., 0], a[..., 1], a[..., 2]
    key = (g > r + 60) & (g > b + 60)                       # le vert de l'incrustation
    alpha = Image.fromarray(np.where(key, 0, 255).astype(np.uint8))
    alpha = alpha.filter(ImageFilter.MinFilter(3)).filter(ImageFilter.GaussianBlur(1)).point(lambda v: 255 if v > 128 else 0)
    a[..., 1] = np.minimum(g, np.maximum(r, b) + 10)        # enlève le vert qui bave sur les bords
    rgb = Image.fromarray(a.clip(0, 255).astype(np.uint8))
    cut = rgb.convert("RGBA")
    cut.putalpha(alpha)
    return cut


def habille(cut, ombres, contour=25, halo=False, marge=60):
    A = cut.getchannel("A")
    size = (cut.width + 2 * marge, cut.height + 2 * marge)

    def pad(m):
        c = Image.new("L", size, 0)
        c.paste(m, (marge, marge))
        return c

    M, B = pad(A), pad(A.filter(ImageFilter.MaxFilter(contour)))
    o = Image.new("RGBA", size, (0, 0, 0, 0))
    if halo:
        glow = pad(A.filter(ImageFilter.MaxFilter(contour + 10))).filter(ImageFilter.GaussianBlur(28)).point(lambda v: int(v * .75))
        o.paste(Image.new("RGBA", size, (5, 10, 16, 255)), (0, 0), glow)
    for couleur, d in ombres:                                 # de la plus lointaine à la plus proche
        o.paste(Image.new("RGBA", size, couleur + (255,)), (0, 0), ImageChops.offset(B, d, d))
    o.paste(Image.new("RGBA", size, (255, 255, 255, 255)), (0, 0), B)
    t = Image.new("RGBA", size, (0, 0, 0, 0))
    t.paste(cut, (marge, marge))
    o.paste(t, (0, 0), M)
    return o.crop((marge - 40, marge - 40, size[0] - marge + 40, size[1] - marge + 40))


def main():
    if len(sys.argv) not in (3, 4):
        sys.exit(__doc__)
    src, out = Path(sys.argv[1]), Path(sys.argv[2])
    nom = f"portrait-{sys.argv[3]}" if len(sys.argv) == 4 else "portrait"
    out.mkdir(parents=True, exist_ok=True)
    cut = detoure(src)
    reste = int((np.asarray(cut)[..., 3] > 0).sum())
    cut.save(out / (f"{nom}-detoure.png" if nom != "portrait" else "portrait-illustre-detoure.png"))
    habille(cut, [((47, 107, 255), 24), ((255, 59, 48), 13)]).save(out / f"{nom}-kai.png")
    habille(cut, [((15, 26, 36), 30), ((7, 192, 149), 17)], contour=31, halo=True).save(out / f"{nom}-technovore.png")
    print(f"{out}/{nom}-kai.png, {nom}-technovore.png ({reste} pixels gardés)")


if __name__ == "__main__":
    main()
