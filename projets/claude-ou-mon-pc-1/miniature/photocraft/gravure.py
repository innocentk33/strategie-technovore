"""Variante e : la 5080 FE de l'auteur en noir et blanc, façon gravure (trame de lignes discrète) → photocraft/rtx5080-gravure.png.
Usage : python3 -I photocraft/gravure.py (depuis miniature/, après photocraft/detoure.py). Réglages en tête."""
import numpy as np
from PIL import Image, ImageFilter, ImageOps

W = 2880          # largeur de sortie (960 px de maquette × 3)
PAS = 9           # pas de la trame en px de sortie (≈ 3 px de maquette)
TRAME = 0.45      # part de la trame dans le mélange (0 = N&B lisse, 1 = gravure pure)
im = Image.open("photocraft/rtx5080-detoure.png")
im = im.resize((W, round(im.height * W / im.width)), Image.LANCZOS)
alpha = im.getchannel("A")
g = ImageOps.autocontrast(im.convert("L"), cutoff=(1, 0.5))
g = g.filter(ImageFilter.UnsharpMask(6, 160, 2))
l = np.asarray(g, dtype=np.float32) / 255
l = np.clip((l - 0.12) / 0.62, 0, 1) ** 0.85           # noirs francs, alu presque blanc
y, x = np.mgrid[0:l.shape[0], 0:l.shape[1]]
onde = (np.sin((y + 0.18 * x) * 2 * np.pi / PAS) + 1) / 2  # lignes légèrement obliques, comme une taille-douce
grave = np.clip((l - onde) * 6 + 0.5, 0, 1)               # ligne épaisse dans les ombres, fine dans les lumières
out = (1 - TRAME) * l + TRAME * grave
res = Image.fromarray((out * 255).astype(np.uint8)).convert("RGBA")
res.putalpha(alpha)
res.save("photocraft/rtx5080-gravure.png")
print(res.size)
