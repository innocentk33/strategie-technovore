"""Fichiers PhotoCraft à calques : le décor (rendu sans texte) + un calque de texte modifiable par texte de la page.
Usage : python3 -I psd.py [vert|noir] [n …]   (sans argument : toutes) → photocraft/<style>-NN.psd
        python3 -I psd.py --page <maquette.html> <dossier de sortie> [v …]   (maquettes d'un projet, ?v=a|b|c) → <dossier>/<v>.psd
        python3 -I psd.py --page <page.html> <requête> <sortie.psd>     (une page de projet, ex. --page projets/x/miniature/propositions/miniature.html v=b projets/x/miniature/photocraft/b.psd)
Pour vérifier un PSD : photocraft-cli convert photocraft/vert-01.psd /tmp/vert-01.png
Marche sur Mac et sur Windows (Chrome et photocraft-cli à leur place habituelle, ou photocraft-cli dans le PATH).
"""
import html, json, pathlib, re, shutil, subprocess, sys, tempfile

HERE = pathlib.Path(__file__).resolve().parent
CHROME = next((c for c in ["/Applications/Google Chrome.app/Contents/MacOS/Google Chrome",
                           r"C:\Program Files\Google\Chrome\Application\chrome.exe",
                           r"C:\Program Files (x86)\Google\Chrome\Application\chrome.exe"] if pathlib.Path(c).exists()), "google-chrome")
PCLI = shutil.which("photocraft-cli") or next((str(c) for c in [pathlib.Path.home() / ".local/bin/photocraft-cli",
                                                                pathlib.Path(r"C:\Program Files\PhotoCraft\photocraft-cli.exe")] if c.exists()), "photocraft-cli")
OUT = HERE / "photocraft"
S = 3  # page de 1280×720 rendue en 3840×2160 ; les positions lues dans la page sont multipliées par S


def chrome(url, *args):
    return subprocess.run([CHROME, "--headless=new", "--hide-scrollbars", "--allow-file-access-from-files",
                           "--window-size=1280,720", f"--force-device-scale-factor={S}", "--virtual-time-budget=3000", *args, url],
                          capture_output=True, text=True, encoding="utf-8", check=True).stdout


def build(url, psd, tmp):
    decor = pathlib.Path(tmp) / f"{psd.stem}.png"
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
            "x": it["x"] * S, "y": it["y"] * S, "text": text, "name": " ".join(text.split())[:30], "font": it["font"], "size": it["size"] * S,
            "weight": first["weight"], "color": first["color"], "tracking": it["tracking"], "horizontalScale": it["hscale"]})]
        if first["weight"] != 400:
            cmd += ["--cmd", "type.setStyle", "--params", json.dumps({"weight": first["weight"], "variations": {"wght": first["weight"]}})]
        if "\r" in text and it.get("leading"):  # texte sur plusieurs lignes : l'interligne de la page
            cmd += ["--cmd", "type.setStyle", "--params", json.dumps({"leading": it["leading"] * S})]
        pos = 0
        base = {"color": first["color"], "weight": first["weight"], "size": it["size"] * S}
        for r in it["runs"]:  # morceaux d'une autre couleur, graisse ou taille (un <span> dans le texte)
            diff = {} if r["t"] == "\r" else {k: v for k, v in (("color", r["color"]), ("weight", r["weight"]), ("size", r.get("size", it["size"]) * S)) if v != base[k]}
            if "weight" in diff:
                diff["variations"] = {"wght": diff["weight"]}
            if diff:
                cmd += ["--cmd", "type.setStyle", "--params", json.dumps({"range": [pos, pos + len(r["t"])], **diff})]
            pos += len(r["t"])
        if it.get("stroke"):  # -webkit-text-stroke derrière le texte (paint-order) : seule la moitié dépasse
            cmd += ["--cmd", "layer.layerStyle.stroke", "--params", json.dumps({"size": round(it["stroke"]["w"] / 2 * S), "position": "outside", "color": it["stroke"]["color"]})]
        if it.get("shadow"):
            sh = it["shadow"]
            cmd += ["--cmd", "layer.layerStyle.dropShadow", "--params", json.dumps({"color": sh["color"], "opacity": 100, "blend": "normal", "angle": 90, "useGlobalLight": False,
                                                                                    "distance": round(abs(sh["dy"]) * S), "size": round(sh["blur"] * S), "add": True})]
        if it["opacity"] < 1:
            cmd += ["--cmd", "layer.setProps", "--params", json.dumps({"opacity": it["opacity"]})]
    psd.parent.mkdir(parents=True, exist_ok=True)
    subprocess.run(cmd + ["--out", str(psd)], capture_output=True, text=True, encoding="utf-8", check=True)
    print(psd.name, len(items), "calques de texte")


if __name__ == "__main__":
    with tempfile.TemporaryDirectory() as tmp:
        if sys.argv[1:2] == ["--page"]:
            page = pathlib.Path(sys.argv[2]).resolve().as_uri()
            if "=" in sys.argv[3]:  # --page <page.html> v=b <sortie.psd>
                build(f"{page}?{sys.argv[3]}", pathlib.Path(sys.argv[4]).resolve(), tmp)
            else:  # --page <maquette.html> <dossier> [v …]
                for v in sys.argv[4:] or ["a", "b", "c"]:
                    build(f"{page}?v={v}", pathlib.Path(sys.argv[3]).resolve() / f"{v}.psd", tmp)
        else:
            styles = [sys.argv[1]] if len(sys.argv) > 1 else ["vert", "noir"]
            kept = {"vert": "2 5 9 10", "noir": "1 1b 3 4 6 7 8"}
            for s in styles:
                for k in sys.argv[2:] or kept[s].split():
                    name = f"{s}-{int(k.rstrip('b')):02d}{'b' if k.endswith('b') else ''}"
                    build(f"{(HERE / f'{s}.html').as_uri()}?n={k}", OUT / f"{name}.psd", tmp)
