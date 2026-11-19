from pathlib import Path
import argparse
import importlib.util, tempfile, subprocess
HERE=Path(__file__).resolve().parent
spec=importlib.util.spec_from_file_location('psd',HERE.parents[2]/'ressources/miniatures/psd.py')
mod=importlib.util.module_from_spec(spec);spec.loader.exec_module(mod)
def chrome(url,*args):
 with tempfile.TemporaryDirectory(prefix='miniature-psd-') as profile:
  return subprocess.run([mod.CHROME,'--headless=new',f'--user-data-dir={profile}','--hide-scrollbars','--allow-file-access-from-files','--window-size=1280,720','--force-device-scale-factor=3','--virtual-time-budget=3000',*args,url],capture_output=True,text=True,check=True).stdout
mod.chrome=chrome
parser = argparse.ArgumentParser()
parser.add_argument('variants', nargs='*')
variants = parser.parse_args().variants or ['h', 'i', 'j']
if any(v not in ('h', 'i', 'j') for v in variants):
 parser.error('Variantes acceptées : h, i, j')
with tempfile.TemporaryDirectory() as tmp:
 for v in variants:
  mod.build((HERE/'propositions/miniature-kai.html').as_uri()+f'?v={v}', HERE/'photocraft'/f'{v}-kai.psd',tmp)
