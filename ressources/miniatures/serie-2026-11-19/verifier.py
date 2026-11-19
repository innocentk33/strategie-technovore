"""Contrôle les fichiers livrés et les liens de la galerie, sans modifier les sources."""
from pathlib import Path
from html.parser import HTMLParser
import hashlib
import json
import shutil
import subprocess

from PIL import Image
from galerie import HERE, ROOT, PROJECTS, LABELS


class Links(HTMLParser):
    def __init__(self):
        super().__init__()
        self.paths = []

    def handle_starttag(self, tag, attrs):
        for key, value in attrs:
            if key in ('href', 'src') and value and not value.startswith(('#', 'http:', 'https:')):
                self.paths.append(value)


def main():
    cli = shutil.which('photocraft-cli') or str(Path.home() / '.local/bin/photocraft-cli')
    results = []
    for slug in PROJECTS:
        base = ROOT / 'projets' / slug / 'miniature'
        for doc in ('propositions-kai.md', 'critique-kai.md', 'rendre-kai.sh',
                    'export-kai-psd.py', 'propositions/miniature-kai.html'):
            assert (base / doc).is_file(), (slug, doc)
        review = (base / 'critique-kai.md').read_text()
        for variant in LABELS:
            png = base / 'rendus' / f'{variant}-kai.png'
            psd = base / 'photocraft' / f'{variant}-kai.psd'
            digest = hashlib.sha256(png.read_bytes()).hexdigest()
            with Image.open(png) as img:
                img.verify()
                assert img.size == (3840, 2160), png
            info = json.loads(subprocess.check_output([cli, 'info', str(psd)], text=True))
            assert (info['width'], info['height']) == (3840, 2160), psd
            assert not info.get('warnings'), info.get('warnings')
            texts = [layer['text'] for layer in info['layers'] if layer['kind'] == 'Type']
            assert len(texts) >= 2, psd
            assert all(t['font'] == 'Archivo Black' for t in texts), texts
            assert digest in review, f'{slug}/{variant}: empreinte finale absente de la revue'
            results.append({'projet': slug, 'variante': variant, 'dimensions': [3840, 2160],
                            'sha256_png': digest, 'sha256_psd': hashlib.sha256(psd.read_bytes()).hexdigest(),
                            'calques_texte': texts, 'avertissements': [],
                            'empreinte_presente_dans_critique': True})
    parser = Links()
    parser.feed((HERE / 'index.html').read_text())
    missing = [s for s in parser.paths if not (HERE / s).resolve().exists()]
    assert not missing, missing
    report = {'miniatures': results, 'liens_locaux_verifies': len(parser.paths), 'liens_manquants': []}
    (HERE / 'verification-livraison.json').write_text(json.dumps(report, ensure_ascii=False, indent=2) + '\n')
    print(f'{len(results)} PNG/PSD contrôlés ; empreintes présentes dans les critiques ; {len(parser.paths)} liens valides.')


if __name__ == '__main__':
    main()
