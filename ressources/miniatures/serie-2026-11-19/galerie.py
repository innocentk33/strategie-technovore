"""Assemble les livrables de la série, sans modifier les miniatures originales.
Usage : python3 ressources/miniatures/serie-2026-11-19/galerie.py
"""
from pathlib import Path
from html import escape
import json
from PIL import Image, ImageDraw, ImageFont

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[2]
TITLES = {
    'qwen-4-cartes': 'Qwen 4 : quelle carte graphique acheter (ou pas) ?',
    'claude-ou-mon-pc-1': '16 Go de VRAM suffisent (si tu prends le bon fichier)',
    'installer-ia-locale': "Pourquoi avoir ta propre IA, et comment l’installer (LM Studio)",
    'uber': 'La carte d’Uber est une illusion (et c’est génial)',
    'opencode': 'OpenCode piraté : pourquoi tes clés API valent de l’or',
    'artcraft': 'ArtCraft : il a recréé Adobe avec une IA',
}
PROJECTS = list(TITLES)

LABELS = {'h': 'h · Palette Kai', 'i': 'i · Technovore sans portrait', 'j': 'j · Technovore illustré'}
FONT = ImageFont.truetype('/System/Library/Fonts/Supplemental/Arial.ttf', 18)


def build():
    previews = HERE / 'apercus'
    previews.mkdir(exist_ok=True)
    sections, manifest = [], []
    for slug in PROJECTS:
        project = ROOT / 'projets' / slug
        title = TITLES[slug]
        cards = []
        for variant, label in LABELS.items():
            png = project / 'miniature' / 'rendus' / f'{variant}-kai.png'
            psd = project / 'miniature' / 'photocraft' / f'{variant}-kai.psd'
            if not png.exists():
                raise FileNotFoundError(png)
            with Image.open(png) as original:
                original.load()
                if original.size != (3840, 2160):
                    raise ValueError(f'{png}: dimensions {original.size}')
                preview = original.convert('RGB').resize((640, 360), Image.Resampling.LANCZOS)
                preview.save(previews / f'{slug}-{variant}.jpg', quality=92)
            if not psd.exists():
                raise FileNotFoundError(psd)
            manifest.append({'projet': slug, 'variante': variant,
                             'png': str(png.relative_to(ROOT)), 'psd': str(psd.relative_to(ROOT)),
                             'dimensions': [3840, 2160], 'octets_png': png.stat().st_size})
            prefix = f'../../../projets/{slug}/miniature'
            cards.append(f'<article><h3>{escape(label)}</h3><a href="{prefix}/rendus/{variant}-kai.png"><img src="apercus/{slug}-{variant}.jpg" width="640" height="360" loading="lazy" alt="{escape(title)} — {variant}"></a><p><a href="{prefix}/rendus/{variant}-kai.png">PNG 4K</a> · <a href="{prefix}/photocraft/{variant}-kai.psd">PSD</a></p></article>')
        review_logos = (f' · <a href="../../../projets/{slug}/miniature/critique-logos.md">Relecture des logos</a>'
                        if (project / 'miniature' / 'critique-logos.md').exists() else '')
        sections.append(f'<section id="{slug}"><h2>{escape(title)}</h2><div class="grid">{"".join(cards)}</div><p><a href="../../../projets/{slug}/miniature/propositions-kai.md">Concept et sources</a> · <a href="../../../projets/{slug}/miniature/critique-kai.md">Critique indépendante</a>{review_logos}</p></section>')
    page = '''<!doctype html><html lang="fr"><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>Technovore · 18 miniatures</title><style>
    *{box-sizing:border-box}body{margin:0;background:#101820;color:#fff;font:16px/1.5 system-ui,sans-serif}main{max-width:1500px;margin:auto;padding:40px 28px}h1{font-size:clamp(30px,4vw,54px);letter-spacing:-.04em;margin:0}header p{color:#afc2ce;max-width:850px}section{padding:24px 0 34px;border-top:1px solid #34495e}h2{font-size:22px}h3{font-size:14px;color:#afc2ce}a{color:#30d6ad;text-underline-offset:3px}.grid{display:grid;grid-template-columns:repeat(3,minmax(0,1fr));gap:20px}img{display:block;width:100%;height:auto;border-radius:6px}article p{font-size:14px}.mobile img{max-width:168px}.mobile .grid{grid-template-columns:repeat(3,168px)}button{padding:10px 16px;border:1px solid #07c095;color:#fff;background:#20313e;border-radius:6px;cursor:pointer;margin:12px 0 28px}@media(max-width:760px){.grid{grid-template-columns:1fr}.mobile .grid{grid-template-columns:repeat(auto-fit,168px)}main{padding:25px 18px}}
    </style><main><header><p>TECHNOVORE · SÉRIE DU 19 NOVEMBRE 2026 · VIDÉOS PRÉCÉDENTES</p><h1>6 vidéos, 18 miniatures</h1><p>Les trois variantes côte à côte. Clique sur une image pour ouvrir le PNG 4K. Les PSD conservent les textes modifiables ; les scènes restent modifiables dans les sources HTML/SVG.</p><button onclick="document.body.classList.toggle('mobile');this.textContent=document.body.classList.contains('mobile')?'Afficher en grand':'Tester à 168 px'">Tester à 168 px</button></header>'''+''.join(sections)+'</main></html>'
    (HERE / 'index.html').write_text(page)
    (HERE / 'manifest.json').write_text(json.dumps(manifest, ensure_ascii=False, indent=2)+'\n')
    # Trois planches lisibles, et un index compact à la taille réelle de 168 px.
    groups = [('1', PROJECTS[:3]), ('2', PROJECTS[3:])]
    for index, group in groups:
        sheet = Image.new('RGB', (1024, 50 + 246 * len(group)), '#101820')
        draw = ImageDraw.Draw(sheet)
        for col, label in enumerate(LABELS.values()):
            draw.text((16 + col * 336, 15), label, font=FONT, fill='#c7d4dc')
        for row, slug in enumerate(group):
            y = 50 + row * 246
            draw.text((16, y), slug, font=FONT, fill='white')
            for col, variant in enumerate(LABELS):
                with Image.open(previews / f'{slug}-{variant}.jpg') as img:
                    sheet.paste(img.resize((320, 180), Image.Resampling.LANCZOS), (16 + col * 336, y + 32))
        sheet.save(HERE / f'planche-{index}.jpg', quality=94)
    mobile = Image.new('RGB', (568, 42 + 128 * len(PROJECTS)), '#101820')
    draw = ImageDraw.Draw(mobile)
    for col, variant in enumerate(LABELS):
        draw.text((16 + col * 184, 10), variant, font=FONT, fill='white')
    for row, slug in enumerate(PROJECTS):
        for col, variant in enumerate(LABELS):
            with Image.open(previews / f'{slug}-{variant}.jpg') as img:
                mobile.paste(img.resize((168, 95), Image.Resampling.LANCZOS), (16 + col * 184, 42 + row * 128))
    mobile.save(HERE / 'planche-168px.png')
    print(f'{len(manifest)} PNG 4K + PSD vérifiés ; galerie et 3 planches assemblées.')


if __name__ == '__main__':
    build()
