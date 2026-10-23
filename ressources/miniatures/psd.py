"""Fichiers PhotoCraft à calques : le décor (rendu sans texte) + un calque de texte modifiable par texte de la page.
Usage : python3 -I psd.py [vert|noir] [n …]   (sans argument : toutes) → photocraft/<style>-NN.psd
Pour vérifier un PSD : photocraft-cli convert photocraft/vert-01.psd /tmp/vert-01.png
"""
import html, json, pathlib, re, subprocess, sys, tempfile

HERE = pathlib.Path(__file__).resolve().parent
CHROME = "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"
PCLI = pathlib.Path.home() / ".local/bin/photocraft-cli"
OUT = HERE / "photocraft"
S = 3  # page de 1280×720 rendue en 3840×2160 ; les positions lues dans la page sont multipliées par S


def chrome(url, *args):
    return subprocess.run([CHROME, "--headless=new", "--hide-scrollbars", "--allow-file-access-from-files",
                           "--window-size=1280,720", f"--force-device-scale-factor={S}", "--virtual-time-budget=3000", *args, url],
                          capture_output=True, text=True, check=True).stdout


def build(style, n, tmp):
    url = f"file://{HERE}/{style}.html?n={n}"
    name = f"{style}-{int(n.rstrip('b')):02d}{'b' if n.endswith('b') else ''}"
    decor = pathlib.Path(tmp) / f"{name}.png"
    chrome(url + "&layer=decor", f"--screenshot={decor}")
    dump = re.search(r'<pre id="dump">(.*?)</pre>', chrome(url + "&dump=1", "--dump-dom"), re.S)
    items = json.loads(html.unescape(dump.group(1)))

    cmd = [str(PCLI), "run", "--new", json.dumps({"width": 1280 * S, "height": 720 * S, "resolution": 72}),
           "--cmd", "file.placeEmbedded", "--params", json.dumps({"path": str(decor), "scale": 100, "center": [640 * S, 360 * S], "smartObject": False}),
           "--cmd", "layer.setProps", "--params", json.dumps({"name": "décor"})]
    for it in items:
        text = "".join(r["t"] for r in it["runs"])
        first = it["runs"][0]
        cmd += ["--cmd", "type.create", "--params", json.dumps({
            "x": it["x"] * S, "y": it["y"] * S, "text": text, "name": text.strip()[:30], "font": it["font"], "size": it["size"] * S,
            "weight": first["weight"], "color": first["color"], "tracking": it["tracking"], "horizontalScale": it["hscale"]})]
        if first["weight"] != 400:
            cmd += ["--cmd", "type.setStyle", "--params", json.dumps({"weight": first["weight"], "variations": {"wght": first["weight"]}})]
        pos = 0
        for r in it["runs"]:
            if r["color"] != first["color"]:
                cmd += ["--cmd", "type.setStyle", "--params", json.dumps({"range": [pos, pos + len(r["t"])], "color": r["color"]})]
            pos += len(r["t"])
        if it["opacity"] < 1:
            cmd += ["--cmd", "layer.setProps", "--params", json.dumps({"opacity": it["opacity"]})]
    psd = OUT / f"{name}.psd"
    subprocess.run(cmd + ["--out", str(psd)], capture_output=True, text=True, check=True)
    print(name, len(items), "calques de texte")


if __name__ == "__main__":
    OUT.mkdir(exist_ok=True)
    styles = [sys.argv[1]] if len(sys.argv) > 1 else ["vert", "noir"]
    kept = {"vert": "2 5 9 10", "noir": "1 1b 3 4 6 7 8"}
    with tempfile.TemporaryDirectory() as tmp:
        for s in styles:
            for k in sys.argv[2:] or kept[s].split():
                build(s, k, tmp)
