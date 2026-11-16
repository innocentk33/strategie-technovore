#!/usr/bin/env python3
"""Aperçu d'une ou plusieurs miniatures YouTube telles que le spectateur les voit.

Produit, dans le dossier de sortie :
  - planche_<nom>.png   : grille des tiers + zone de la durée, rendus aux tailles
                          réelles (fil mobile, suggestions), niveaux de gris,
                          version floutée (test du plissement d'yeux), palette dominante
  - accueil_clair.png / accueil_sombre.png : simulation de page d'accueil, la ou les
                          miniatures au milieu de miniatures voisines (--contexte)
  - comparaison.png     : versions côte à côte aux petites tailles (si plusieurs images)
  - metriques.json      : mesures brutes (résolution, poids, contraste, couleurs...)
et affiche un résumé avec des alertes.

Les métriques sont des indices pour orienter le regard, pas un verdict.

Usage :
  python apercu_miniature.py mini.jpg --titre "Mon titre" --sortie apercu/
  python apercu_miniature.py v1.png v2.png --titre "Titre A" "Titre B"
  python apercu_miniature.py mini.jpg --contexte concurrent1.jpg concurrent2.jpg
  python apercu_miniature.py mini.jpg --chaine "Ma chaîne"

Dépendance : Pillow (pip install pillow).
"""

import argparse
import json
import math
import os
import sys

try:
    from PIL import Image, ImageDraw, ImageFilter, ImageFont, ImageOps, ImageStat
except ImportError:
    sys.exit("Pillow est requis : pip install pillow")

RATIO_CIBLE = 16 / 9
TAILLE_TRAVAIL = (1280, 720)
TAILLES_REELLES = [
    ("Fil mobile (~360 px)", 360),
    ("Accueil ordinateur (~300 px)", 300),
    ("Suggestions (~168 px)", 168),
]
# Zone approximative du badge de durée (bas droite), en fraction de l'image
ZONE_DUREE = (0.86, 0.86, 0.985, 0.975)

FOND_CLAIR = (255, 255, 255)
FOND_SOMBRE = (15, 15, 15)
TEXTE_CLAIR = (15, 15, 15)
TEXTE_SOMBRE = (241, 241, 241)
TEXTE_SECONDAIRE_CLAIR = (96, 96, 96)
TEXTE_SECONDAIRE_SOMBRE = (170, 170, 170)


# ---------------------------------------------------------------- utilitaires

def police(taille, gras=False):
    candidats = (
        ["DejaVuSans-Bold.ttf", "Arial Bold.ttf", "arialbd.ttf", "LiberationSans-Bold.ttf"]
        if gras
        else ["DejaVuSans.ttf", "Arial.ttf", "arial.ttf", "LiberationSans-Regular.ttf"]
    )
    dossiers = [
        "",
        "/usr/share/fonts/truetype/dejavu/",
        "/usr/share/fonts/truetype/liberation/",
        "/Library/Fonts/",
        "/System/Library/Fonts/Supplemental/",
        "C:/Windows/Fonts/",
    ]
    for nom in candidats:
        for dossier in dossiers:
            try:
                return ImageFont.truetype(dossier + nom, taille)
            except OSError:
                continue
    try:
        return ImageFont.load_default(size=taille)
    except TypeError:
        return ImageFont.load_default()


def charger(chemin):
    img = Image.open(chemin)
    img = ImageOps.exif_transpose(img)
    if img.mode in ("RGBA", "LA", "P"):
        img = img.convert("RGBA")
        fond = Image.new("RGB", img.size, (128, 128, 128))
        fond.paste(img, mask=img.split()[-1])
        return fond
    return img.convert("RGB")


def en_16_9(img, taille):
    """Recadre au centre en 16:9 (comme le ferait l'affichage) puis redimensionne."""
    return ImageOps.fit(img, taille, Image.LANCZOS, centering=(0.5, 0.5))


def couper_texte(draw, texte, fnt, largeur_max, lignes_max=2):
    mots = texte.split()
    lignes, courante = [], ""
    for mot in mots:
        essai = (courante + " " + mot).strip()
        if draw.textlength(essai, font=fnt) <= largeur_max:
            courante = essai
        else:
            if courante:
                lignes.append(courante)
            courante = mot
        if len(lignes) == lignes_max:
            break
    if courante and len(lignes) < lignes_max:
        lignes.append(courante)
    utilises = " ".join(lignes).split()
    if len(utilises) < len(mots) and lignes:
        dernier = lignes[-1]
        while dernier and draw.textlength(dernier + "…", font=fnt) > largeur_max:
            dernier = dernier[:-1]
        lignes[-1] = dernier.rstrip() + "…"
    return lignes


def pixels(img):
    if hasattr(img, "get_flattened_data"):
        return list(img.get_flattened_data())
    return list(img.getdata())


# ---------------------------------------------------------------- mesures

def palette_dominante(img, n=6):
    petite = img.copy()
    petite.thumbnail((240, 240))
    quant = petite.quantize(colors=10, method=Image.Quantize.FASTOCTREE)
    pal = quant.getpalette()
    comptes = sorted(quant.getcolors(), reverse=True)
    total = sum(c for c, _ in comptes)
    fusion = []  # fusionne les teintes quasi identiques
    for compte, idx in comptes:
        rgb = tuple(pal[idx * 3: idx * 3 + 3])
        for f in fusion:
            if sum((a - b) ** 2 for a, b in zip(f["rgb"], rgb)) ** 0.5 < 32:
                f["compte"] += compte
                break
        else:
            fusion.append({"rgb": rgb, "compte": compte})
    fusion.sort(key=lambda f: -f["compte"])
    return [
        {
            "hex": "#{:02X}{:02X}{:02X}".format(*f["rgb"]),
            "rgb": f["rgb"],
            "part": round(f["compte"] / total, 3),
        }
        for f in fusion[:n]
    ]


def familles_saturees(palette, part_min=0.03):
    """Nombre de familles de teintes vives (hors noirs, blancs, gris) dans la palette."""
    familles = set()
    for c in palette:
        r, g, b = [v / 255 for v in c["rgb"]]
        mx, mn = max(r, g, b), min(r, g, b)
        if c["part"] < part_min or mx < 0.35 or (mx - mn) / mx < 0.45:
            continue
        if mx == r:
            h = ((g - b) / (mx - mn)) % 6
        elif mx == g:
            h = (b - r) / (mx - mn) + 2
        else:
            h = (r - g) / (mx - mn) + 4
        familles.add(int(h * 60 // 40))  # tranches de 40° sur le cercle chromatique
    return len(familles)


def carte_contours(img):
    gris = en_16_9(img, (384, 216)).convert("L")
    return gris.filter(ImageFilter.FIND_EDGES).point(lambda v: 255 if v > 40 else 0)


def densite_zone_duree(bords):
    w, h = bords.size
    x0, y0, x1, y1 = ZONE_DUREE
    zone = bords.crop((int(x0 * w), int(y0 * h), int(x1 * w) - 1, int(y1 * h) - 1))
    return round(ImageStat.Stat(zone).mean[0] / 255, 3)


def densite_details(img):
    """Densité de contours par case de la grille 3x3 (indice de zones chargées)."""
    bords = carte_contours(img)
    w, h = bords.size
    cases = []
    noms = [
        ["haut-gauche", "haut-centre", "haut-droite"],
        ["milieu-gauche", "centre", "milieu-droite"],
        ["bas-gauche", "bas-centre", "bas-droite"],
    ]
    for ligne in range(3):
        for col in range(3):
            boite = (col * w // 3 + 2, ligne * h // 3 + 2, (col + 1) * w // 3 - 2, (ligne + 1) * h // 3 - 2)
            moyenne = ImageStat.Stat(bords.crop(boite)).mean[0] / 255
            cases.append({"case": noms[ligne][col], "densite": round(moyenne, 3)})
    valeurs = [c["densite"] for c in cases]
    moyenne = sum(valeurs) / len(valeurs)
    ecart = math.sqrt(sum((v - moyenne) ** 2 for v in valeurs) / len(valeurs))
    return cases, round(moyenne, 3), round(ecart, 3)


def mesurer(chemin, img):
    w, h = img.size
    gris = img.convert("L")
    stat = ImageStat.Stat(gris)
    hsv = img.convert("HSV")
    sat = ImageStat.Stat(hsv.split()[1]).mean[0] / 255

    # Bande de 4 % sur le pourtour : c'est elle qui touche l'interface de YouTube
    bord = 0.04
    bandes = [
        img.crop((0, 0, w, int(h * bord))),
        img.crop((0, int(h * (1 - bord)), w, h)),
        img.crop((0, 0, int(w * bord), h)),
        img.crop((int(w * (1 - bord)), 0, w, h)),
    ]
    moyennes_bords = [ImageStat.Stat(b).mean for b in bandes]
    couleur_bords = tuple(int(sum(m[i] for m in moyennes_bords) / 4) for i in range(3))
    pix_bords = [p for b in bandes for p in pixels(b.resize((max(1, b.width // 4), max(1, b.height // 4))))]
    bords_blancs = sum(1 for p in pix_bords if min(p) > 225) / len(pix_bords)
    bords_noirs = sum(1 for p in pix_bords if max(p) < 35) / len(pix_bords)

    hist = gris.histogram()
    total = w * h
    tres_clair = sum(hist[235:]) / total
    tres_sombre = sum(hist[:25]) / total

    cases, densite_moy, densite_ecart = densite_details(img)
    palette = palette_dominante(img)
    poids = os.path.getsize(chemin)

    return {
        "fichier": os.path.basename(chemin),
        "largeur": w,
        "hauteur": h,
        "ratio": round(w / h, 3),
        "poids_octets": poids,
        "poids_mo": round(poids / 1_000_000, 2),
        "format": (Image.open(chemin).format or "?"),
        "luminosite_moyenne": round(stat.mean[0] / 255, 3),
        "contraste_valeurs": round(stat.stddev[0] / 255, 3),
        "saturation_moyenne": round(sat, 3),
        "part_tres_claire": round(tres_clair, 3),
        "part_tres_sombre": round(tres_sombre, 3),
        "couleur_moyenne_bords": "#{:02X}{:02X}{:02X}".format(*couleur_bords),
        "part_bords_quasi_blancs": round(bords_blancs, 3),
        "part_bords_quasi_noirs": round(bords_noirs, 3),
        "palette": palette,
        "familles_couleurs_vives": familles_saturees(palette_dominante(img, n=10), part_min=0.015),
        "densite_details_par_case": cases,
        "densite_details_moyenne": densite_moy,
        "densite_details_ecart": densite_ecart,
        "densite_zone_duree": densite_zone_duree(carte_contours(img)),
    }


def alertes(m):
    a = []
    if abs(m["ratio"] - RATIO_CIBLE) > 0.02:
        a.append(f"Ratio {m['ratio']} au lieu de 1,778 (16:9) : l'image sera recadrée ou bordée.")
    if m["largeur"] < 640:
        a.append("Largeur inférieure à 640 px : YouTube refuse la miniature.")
    elif m["largeur"] < 1280:
        a.append("Moins de 1280 × 720 : image moins nette, et un test A/B serait dégradé en 480p.")
    if m["poids_mo"] > 2:
        a.append(f"{m['poids_mo']} Mo : au-dessus de 2 Mo, l'upload depuis un téléphone échoue "
                 "(l'ordinateur accepte jusqu'à 50 Mo).")
    if m["contraste_valeurs"] < 0.17:
        a.append("Contraste de valeurs faible : l'image risque de paraître terne et plate en petit.")
    if m["part_bords_quasi_blancs"] > 0.5:
        a.append(f"{round(m['part_bords_quasi_blancs'] * 100)} % du pourtour est quasi blanc : "
                 "la miniature se fond dans le mode clair.")
    if m["part_bords_quasi_noirs"] > 0.5:
        a.append(f"{round(m['part_bords_quasi_noirs'] * 100)} % du pourtour est quasi noir : "
                 "la miniature se fond dans le mode sombre.")
    if m["densite_zone_duree"] > max(0.08, 1.5 * m["densite_details_moyenne"]):
        a.append("Beaucoup de détails sous la zone de la durée (bas droite) : "
                 "vérifier que rien d'important n'y est caché.")
    if m["familles_couleurs_vives"] >= 4:
        a.append(f"{m['familles_couleurs_vives']} familles de couleurs vives : la palette se disperse, "
                 "aucune couleur ne domine.")
    return a


# ---------------------------------------------------------------- rendus

def avec_grille(img):
    base = en_16_9(img, TAILLE_TRAVAIL).copy()
    calque = Image.new("RGBA", base.size, (0, 0, 0, 0))
    d = ImageDraw.Draw(calque)
    w, h = base.size
    for i in (1, 2):
        x, y = w * i // 3, h * i // 3
        for dx in range(-1, 2):
            d.line([(x + dx, 0), (x + dx, h)], fill=(0, 0, 0, 120))
            d.line([(0, y + dx), (w, y + dx)], fill=(0, 0, 0, 120))
        d.line([(x, 0), (x, h)], fill=(255, 255, 255, 220), width=1)
        d.line([(0, y), (w, y)], fill=(255, 255, 255, 220), width=1)
    for i in (1, 2):
        for j in (1, 2):
            cx, cy = w * i // 3, h * j // 3
            d.ellipse([cx - 7, cy - 7, cx + 7, cy + 7], outline=(255, 214, 0, 255), width=3)
    # Zone de sécurité de la durée : semi-transparente pour voir ce qu'elle recouvre
    x0, y0, x1, y1 = ZONE_DUREE
    boite = [int(x0 * w), int(y0 * h), int(x1 * w), int(y1 * h)]
    d.rounded_rectangle(boite, radius=6, fill=(0, 0, 0, 90), outline=(255, 60, 60, 255), width=3)
    d.text(((boite[0] + boite[2]) / 2, (boite[1] + boite[3]) / 2), "durée",
           fill=(255, 255, 255, 230), font=police(22, gras=True), anchor="mm")
    return Image.alpha_composite(base.convert("RGBA"), calque).convert("RGB")


def avec_badge(img_petite):
    """Ajoute le badge de durée à peu près à la taille où YouTube l'affiche."""
    img = img_petite.copy()
    d = ImageDraw.Draw(img)
    w, h = img.size
    fnt = police(max(8, round(h * 0.062)), gras=True)
    texte = "12:34"
    tw = d.textlength(texte, font=fnt)
    marge = max(3, round(w * 0.012))
    pad = max(2, round(w * 0.009))
    bh = max(10, round(h * 0.095))
    boite = [w - marge - tw - 2 * pad, h - marge - bh, w - marge, h - marge]
    d.rounded_rectangle(boite, radius=max(2, round(h * 0.02)), fill=(0, 0, 0))
    d.text(((boite[0] + boite[2]) / 2, (boite[1] + boite[3]) / 2), texte,
           fill=(255, 255, 255), font=fnt, anchor="mm")
    return img


def arrondir(img, rayon):
    masque = Image.new("L", img.size, 0)
    ImageDraw.Draw(masque).rounded_rectangle([0, 0, img.size[0] - 1, img.size[1] - 1], radius=rayon, fill=255)
    fond = Image.new("RGBA", img.size, (0, 0, 0, 0))
    fond.paste(img, mask=masque)
    return fond


def taille_reelle(img, largeur):
    h = round(largeur * 9 / 16)
    return avec_badge(en_16_9(img, (largeur, h)))


def planche(img, m, titre=None):
    marge = 30
    col_g = 1280
    largeur = marge * 3 + col_g + 400
    hauteur = 1450
    p = Image.new("RGB", (largeur, hauteur), (236, 236, 236))
    d = ImageDraw.Draw(p)
    f_titre = police(30, gras=True)
    f_label = police(18, gras=True)
    f_petit = police(16)

    d.text((marge, 18), f"Aperçu — {m['fichier']}", fill=(20, 20, 20), font=f_titre)
    if titre:
        d.text((marge, 56), f"Titre : {titre}", fill=(70, 70, 70), font=f_petit)

    y = 90
    d.text((marge, y), "Grille des tiers (intersections en jaune) et zone de la durée (cadre rouge)",
           fill=(40, 40, 40), font=f_label)
    p.paste(avec_grille(img), (marge, y + 28))

    y2 = y + 28 + 720 + 30
    x = marge
    for label, w in TAILLES_REELLES:
        petite = taille_reelle(img, w)
        d.text((x, y2), label, fill=(40, 40, 40), font=f_label)
        p.paste(petite, (x, y2 + 28))
        x += w + 40

    y3 = y2 + 28 + 203 + 40
    x = marge
    gris = ImageOps.grayscale(en_16_9(img, (360, 203))).convert("RGB")
    d.text((x, y3), "Niveaux de gris (contraste de valeurs)", fill=(40, 40, 40), font=f_label)
    p.paste(gris, (x, y3 + 28))
    x += 360 + 40
    floue = en_16_9(img, (360, 203)).filter(ImageFilter.GaussianBlur(6))
    d.text((x, y3), "Floutée (test du plissement d'yeux)", fill=(40, 40, 40), font=f_label)
    p.paste(floue, (x, y3 + 28))

    # colonne de droite : palette et mesures
    xd = marge * 2 + col_g
    yd = 90
    d.text((xd, yd), "Palette dominante", fill=(40, 40, 40), font=f_label)
    yd += 32
    for c in m["palette"]:
        d.rectangle([xd, yd, xd + 70, yd + 44], fill=tuple(c["rgb"]), outline=(120, 120, 120))
        d.text((xd + 85, yd + 4), c["hex"], fill=(30, 30, 30), font=f_label)
        d.text((xd + 85, yd + 25), f"{round(c['part'] * 100)} % de l'image", fill=(90, 90, 90), font=f_petit)
        yd += 56

    yd += 16
    d.text((xd, yd), "Mesures (indices, pas verdicts)", fill=(40, 40, 40), font=f_label)
    yd += 30
    lignes = [
        f"{m['largeur']} × {m['hauteur']} px, ratio {m['ratio']}",
        f"{m['format']}, {m['poids_mo']} Mo",
        f"Luminosité moyenne : {m['luminosite_moyenne']}",
        f"Contraste de valeurs : {m['contraste_valeurs']}",
        f"Saturation moyenne : {m['saturation_moyenne']}",
        f"Familles de couleurs vives : {m['familles_couleurs_vives']}",
        f"Pourtour quasi blanc : {round(m['part_bords_quasi_blancs'] * 100)} %",
        f"Pourtour quasi noir : {round(m['part_bords_quasi_noirs'] * 100)} %",
        f"Détails sous la durée : {m['densite_zone_duree']}",
        "Zones les plus chargées :",
    ]
    top = sorted(m["densite_details_par_case"], key=lambda c: -c["densite"])[:3]
    lignes += [f"  {c['case']} ({c['densite']})" for c in top]
    for ligne in lignes:
        d.text((xd, yd), ligne, fill=(30, 30, 30), font=f_petit)
        yd += 24

    al = alertes(m)
    if al:
        yd += 14
        d.text((xd, yd), "Alertes", fill=(170, 30, 30), font=f_label)
        yd += 28
        for a in al:
            for ligne in couper_texte(d, "• " + a, f_petit, 360, lignes_max=4):
                d.text((xd, yd), ligne, fill=(120, 30, 30), font=f_petit)
                yd += 22
            yd += 6
    return p


def carte(img, titre, chaine, sombre, largeur=360):
    h = round(largeur * 9 / 16)
    mini = arrondir(avec_badge(en_16_9(img, (largeur, h))), 12)
    hauteur = h + 110
    fond = FOND_SOMBRE if sombre else FOND_CLAIR
    c = Image.new("RGBA", (largeur, hauteur), fond + (255,))
    c.alpha_composite(mini, (0, 0))
    d = ImageDraw.Draw(c)
    d.ellipse([0, h + 12, 36, h + 48], fill=(120, 120, 120) if sombre else (200, 200, 200))
    f_t = police(16, gras=True)
    f_s = police(13)
    lignes = couper_texte(d, titre, f_t, largeur - 50, lignes_max=2)
    y = h + 12
    for ligne in lignes:
        d.text((48, y), ligne, fill=TEXTE_SOMBRE if sombre else TEXTE_CLAIR, font=f_t)
        y += 21
    d.text((48, y + 4), chaine, fill=TEXTE_SECONDAIRE_SOMBRE if sombre else TEXTE_SECONDAIRE_CLAIR, font=f_s)
    d.text((48, y + 22), "12 k vues · il y a 2 jours",
           fill=TEXTE_SECONDAIRE_SOMBRE if sombre else TEXTE_SECONDAIRE_CLAIR, font=f_s)
    return c


def placeholder(index, sombre):
    teintes = [(84, 110, 122), (121, 85, 72), (69, 90, 100), (96, 125, 139), (93, 64, 55), (55, 71, 79)]
    base = teintes[index % len(teintes)]
    img = Image.new("RGB", (640, 360), base)
    d = ImageDraw.Draw(img)
    d.ellipse([60, 60, 300, 300], fill=tuple(min(255, v + 50) for v in base))
    d.rectangle([340, 110, 600, 170], fill=tuple(min(255, v + 90) for v in base))
    d.rectangle([340, 190, 540, 240], fill=tuple(max(0, v - 30) for v in base))
    return img


def page_accueil(images, titres, contexte, chaine, sombre):
    colonnes, lignes = 3, 2
    largeur_carte, gout = 360, 16
    cartes = []
    voisins = list(contexte)
    i_voisin = 0
    positions_cible = [1, 3, 5, 0, 2, 4][: len(images)]
    for pos in range(colonnes * lignes):
        if pos in positions_cible:
            k = positions_cible.index(pos)
            cartes.append(carte(images[k], titres[k], chaine, sombre, largeur_carte))
        else:
            if i_voisin < len(voisins):
                img_v = voisins[i_voisin]
                titre_v = "Vidéo voisine (contexte)"
            else:
                img_v = placeholder(pos, sombre)
                titre_v = "Autre vidéo de la page d'accueil"
            i_voisin += 1
            cartes.append(carte(img_v, titre_v, "Autre chaîne", sombre, largeur_carte))
    h_carte = cartes[0].size[1]
    W = colonnes * largeur_carte + (colonnes + 1) * gout
    H = lignes * h_carte + (lignes + 1) * gout + 40
    fond = FOND_SOMBRE if sombre else FOND_CLAIR
    page = Image.new("RGBA", (W, H), fond + (255,))
    d = ImageDraw.Draw(page)
    d.text((gout, 10), "Simulation page d'accueil — mode " + ("sombre" if sombre else "clair"),
           fill=TEXTE_SECONDAIRE_SOMBRE if sombre else TEXTE_SECONDAIRE_CLAIR, font=police(15, gras=True))
    for idx, c in enumerate(cartes):
        r, col = divmod(idx, colonnes)
        page.alpha_composite(c, (gout + col * (largeur_carte + gout), 40 + gout + r * (h_carte + gout)))
    return page.convert("RGB")


def comparaison(images, noms):
    largeurs = [360, 168]
    marge = 24
    hauteur_ligne = 203 + 40
    W = marge + len(images) * (360 + 168 + 3 * marge)
    H = marge + hauteur_ligne + 50
    p = Image.new("RGB", (W, H), (236, 236, 236))
    d = ImageDraw.Draw(p)
    x = marge
    for img, nom in zip(images, noms):
        d.text((x, marge - 4), nom, fill=(30, 30, 30), font=police(16, gras=True))
        xx = x
        for w in largeurs:
            p.paste(taille_reelle(img, w), (xx, marge + 24))
            xx += w + marge
        x += 360 + 168 + 3 * marge
    return p


# ---------------------------------------------------------------- principal

def main():
    ap = argparse.ArgumentParser(description="Aperçu de miniatures YouTube aux tailles réelles.")
    ap.add_argument("images", nargs="+", help="miniature(s) à analyser (jusqu'à 3 pour une comparaison)")
    ap.add_argument("--titre", nargs="*", default=[], help="titre(s) des vidéos, dans le même ordre")
    ap.add_argument("--contexte", nargs="*", default=[], help="miniatures voisines (concurrents, autres vidéos)")
    ap.add_argument("--chaine", default="Ta chaîne", help="nom de la chaîne affiché sous le titre")
    ap.add_argument("--sortie", default="apercu_miniature", help="dossier de sortie")
    args = ap.parse_args()

    if len(args.images) > 3:
        sys.exit("Trois miniatures au maximum à la fois.")
    os.makedirs(args.sortie, exist_ok=True)

    images, mesures, noms = [], [], []
    for i, chemin in enumerate(args.images):
        img = charger(chemin)
        images.append(img)
        m = mesurer(chemin, img)
        m["alertes"] = alertes(m)
        mesures.append(m)
        nom = os.path.splitext(os.path.basename(chemin))[0]
        noms.append(nom)
        titre = args.titre[i] if i < len(args.titre) else None
        planche(img, m, titre).save(os.path.join(args.sortie, f"planche_{nom}.png"))

    titres = [args.titre[i] if i < len(args.titre) else "Titre de la vidéo (non fourni)" for i in range(len(images))]
    contexte = [charger(c) for c in args.contexte]
    page_accueil(images, titres, contexte, args.chaine, sombre=False).save(os.path.join(args.sortie, "accueil_clair.png"))
    page_accueil(images, titres, contexte, args.chaine, sombre=True).save(os.path.join(args.sortie, "accueil_sombre.png"))
    if len(images) > 1:
        comparaison(images, noms).save(os.path.join(args.sortie, "comparaison.png"))

    with open(os.path.join(args.sortie, "metriques.json"), "w", encoding="utf-8") as f:
        json.dump(mesures, f, ensure_ascii=False, indent=2)

    for m in mesures:
        print(f"\n== {m['fichier']} ==")
        print(f"{m['largeur']}×{m['hauteur']} px, ratio {m['ratio']}, {m['format']}, {m['poids_mo']} Mo")
        print(f"Contraste de valeurs {m['contraste_valeurs']}, saturation {m['saturation_moyenne']}, "
              f"luminosité {m['luminosite_moyenne']}")
        print("Palette : " + ", ".join(f"{c['hex']} ({round(c['part'] * 100)} %)" for c in m["palette"]))
        top = sorted(m["densite_details_par_case"], key=lambda c: -c["densite"])[:3]
        print("Zones les plus chargées : " + ", ".join(f"{c['case']} ({c['densite']})" for c in top))
        if m["alertes"]:
            print("Alertes :")
            for a in m["alertes"]:
                print("  - " + a)
        else:
            print("Aucune alerte automatique.")
    print(f"\nFichiers écrits dans {os.path.abspath(args.sortie)} :")
    for f in sorted(os.listdir(args.sortie)):
        print("  " + f)


if __name__ == "__main__":
    main()
