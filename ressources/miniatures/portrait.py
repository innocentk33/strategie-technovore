#!/usr/bin/env python3
"""Portrait « à la manière de Kai » pour les miniatures (15/11/2026).

Prend un portrait illustré sur fond vert uni (généré avec ChatGPT), le détoure et écrit trois fichiers :
  <sortie>/portrait-illustre-detoure.png   le visage seul, fond transparent
  <sortie>/portrait-kai.png                contour blanc + ombres décalées rouge et bleue (variante h)
  <sortie>/portrait-technovore.png         couleurs de peau gardées, contour blanc épais, ombres menthe et ardoise,
                                           halo sombre (variante j ; pas de duotone : il écrasait le contraste)

Usage : python3 -I ressources/miniatures/portrait.py <image fond vert> <dossier sources/> [nom] [--miroir] [--coupe 0.17]
  avec [nom] (ex. fry) : portrait-fry-detoure.png, portrait-fry-kai.png, portrait-fry-technovore.png
  avec --miroir : le portrait est retourné (il regarde vers la gauche, pour un texte à gauche ; donne-lui un autre nom, ex. fry-g)
  avec --coupe Y (fraction de la hauteur, 15/11, composition « Severance ») : écrit en plus portrait[-nom]-coupe-kai.png
  et -coupe-technovore.png : la tête ouverte (ovale sombre) à la hauteur Y, plus un calque -devant (le bord avant et le visage)
  que la maquette pose PAR-DESSUS les objets, pour qu'ils aient l'air dans la tête. Le centre et la largeur de l'ouverture
  sont notés dans la sortie (en px de l'image habillée). Le portrait idéal est de face, le regard levé.
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


def coupe(cut, y):
    """Tête ouverte vue de face (composition « Severance », 15/11) : le crâne est coupé à la hauteur y (px)
    et l'ouverture est un ovale (bord couleur peau, intérieur sombre). Rend (image, masque_devant, plateau) :
    le masque garde ce qui passe DEVANT les objets (le bord avant de l'ouverture et tout le visage dessous)."""
    from PIL import ImageDraw
    a = np.asarray(cut)
    xs = np.nonzero(a[y, :, 3] > 0)[0]
    x0, x1 = int(xs.min()), int(xs.max())
    rx, cx = (x1 - x0) / 2, (x0 + x1) / 2
    ry = rx * .26                                                   # vue un peu de dessus
    skin = a[y + 12:y + 40, int(cx - rx / 3):int(cx + rx / 3), :3].reshape(-1, 3).mean(0)
    out = cut.copy()
    al = np.asarray(out.getchannel("A")).copy()
    al[:y, :] = 0
    out.putalpha(Image.fromarray(al))
    d = ImageDraw.Draw(out)
    bord = tuple(int(min(255, c * 1.1 + 12)) for c in skin) + (255,)
    d.ellipse((x0, y - ry, x1, y + ry), fill=bord, outline=(0, 0, 0, 255), width=max(4, int(rx * .02)))
    e = rx * .07                                                    # épaisseur du bord
    rxi, ryi = rx - e, ry - e * .6
    d.ellipse((cx - rxi, y - ryi, cx + rxi, y + ryi), fill=tuple(int(c * .28) for c in skin) + (255,))
    # devant = sous l'arc bas de l'ovale intérieur (dans sa largeur), sous la ligne de coupe ailleurs
    H, W = cut.height, cut.width
    X, Y = np.meshgrid(np.arange(W), np.arange(H))
    t = np.clip((X - cx) / rxi, -1, 1)
    arc = np.where(np.abs(X - cx) < rxi, y + ryi * np.sqrt(1 - t ** 2), y)
    devant = Image.fromarray(np.where(Y > arc, 255, 0).astype(np.uint8))
    return out, devant, (cx, y, rx * 2)


def calque_devant(habillee, devant, marge=40):
    """Applique le masque « devant » (coordonnées du portrait) à l'image habillée (40 px de marge en plus)."""
    m = Image.new("L", habillee.size, 0)
    m.paste(devant, (marge, marge))
    # ce qui déborde sous ou à côté du portrait (contour, ombres) suit la ligne la plus proche : on prolonge le masque
    arr = np.asarray(m).copy()
    top = arr.argmax(0)
    for x in range(arr.shape[1]):
        col = arr[:, x]
        if col.any():
            arr[top[x]:, x] = 255
    o = habillee.copy()
    o.putalpha(ImageChops.multiply(habillee.getchannel("A"), Image.fromarray(arr)))
    return o


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
    args = sys.argv[1:]
    y_coupe = None
    if "--coupe" in args:
        i = args.index("--coupe")
        y_coupe = float(args[i + 1])
        del args[i:i + 2]
    miroir = "--miroir" in args
    if miroir:
        args.remove("--miroir")
    if len(args) not in (2, 3):
        sys.exit(__doc__)
    src, out = Path(args[0]), Path(args[1])
    nom = f"portrait-{args[2]}" if len(args) == 3 else "portrait"
    out.mkdir(parents=True, exist_ok=True)
    cut = detoure(src)
    if miroir:                                                     # le visage regarde vers la gauche (texte à gauche)
        from PIL import ImageOps
        cut = ImageOps.mirror(cut)
    reste = int((np.asarray(cut)[..., 3] > 0).sum())
    cut.save(out / (f"{nom}-detoure.png" if nom != "portrait" else "portrait-illustre-detoure.png"))
    habille(cut, [((47, 107, 255), 24), ((255, 59, 48), 13)]).save(out / f"{nom}-kai.png")
    habille(cut, [((15, 26, 36), 30), ((7, 192, 149), 17)], contour=31, halo=True).save(out / f"{nom}-technovore.png")
    print(f"{out}/{nom}-kai.png, {nom}-technovore.png ({reste} pixels gardés)")
    if y_coupe is not None:
        c, devant, (cx, cy, w) = coupe(cut, int(y_coupe * cut.height))
        for style, kw in (("kai", dict(ombres=[((47, 107, 255), 24), ((255, 59, 48), 13)])),
                          ("technovore", dict(ombres=[((15, 26, 36), 30), ((7, 192, 149), 17)], contour=31, halo=True))):
            fond = habille(c, **kw)
            fond.save(out / f"{nom}-coupe-{style}.png")
            calque_devant(fond, devant).save(out / f"{nom}-coupe-{style}-devant.png")
        # habille() recadre avec 40 px de marge autour de l'image d'origine
        print(f"{nom}-coupe-*.png (+ -devant) : ouverture centrée en x={cx + 40:.0f}, y={cy + 40:.0f}, large de {w:.0f} px (image de {cut.width + 80} px)")


if __name__ == "__main__":
    main()
