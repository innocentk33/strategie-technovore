"""Planches de lisibilité sur le fond du mode sombre de YouTube (#0f0f0f).
Usage : python3 -I planches.py <dossier des miniatures concurrentes (un sous-dossier par chaîne)>
  planches/flux-vert.png, flux-noir.png : 4 des nôtres parmi 8 concurrentes, à 300 px (accueil mobile)
  planches/168.png : les nôtres à 168 px (colonne des suggestions)
Ou : python3 -I planches.py --suggestions <notre miniature> <dossier des vidéos hôtes (.jpg)>
  planches/suggestions-<nom>.png : la nôtre au milieu des vidéos où YouTube risque de la suggérer, à 168 px
"""
import pathlib, random, sys
from PIL import Image, ImageDraw

HERE = pathlib.Path(__file__).resolve().parent
BG = (15, 15, 15)


def tile(path, w):
    im = Image.open(path).convert("RGB").resize((w, w * 9 // 16), Image.LANCZOS)
    mask = Image.new("L", im.size, 0)
    ImageDraw.Draw(mask).rounded_rectangle((0, 0, *im.size), radius=max(4, w // 30), fill=255)
    return im, mask


def grid(paths, w, cols, out, gap=16):
    rows = -(-len(paths) // cols)
    h = w * 9 // 16
    sheet = Image.new("RGB", (cols * (w + gap) + gap, rows * (h + gap) + gap), BG)
    for i, p in enumerate(paths):
        im, mask = tile(p, w)
        sheet.paste(im, (gap + (i % cols) * (w + gap), gap + (i // cols) * (h + gap)), mask)
    sheet.save(out)


if __name__ == "__main__":
    if sys.argv[1] == "--suggestions":
        ours, hosts = pathlib.Path(sys.argv[2]), sorted(pathlib.Path(sys.argv[3]).glob("*.jpg"))[:5]
        hosts.insert(len(hosts) // 2, ours)
        (HERE / "planches").mkdir(exist_ok=True)
        grid(hosts, 168, 1, HERE / f"planches/suggestions-{ours.stem}.png", gap=10)
        sys.exit()
    comp = sorted(pathlib.Path(sys.argv[1]).glob("*/*.jpg"))
    out = HERE / "planches"
    out.mkdir(exist_ok=True)
    rnd = random.Random(7)
    for style, ours in [("vert", ["02", "05", "09", "10"]), ("noir", ["01", "03", "04", "06"])]:
        mix = rnd.sample(comp, 8) + [HERE / f"rendus/{style}-{k}.png" for k in ours]
        rnd.shuffle(mix)
        grid(mix, 300, 4, out / f"flux-{style}.png")
    grid(sorted((HERE / "rendus").glob("*.png")), 168, 6, out / "168.png", gap=10)
    print(sorted(p.name for p in out.iterdir()))
