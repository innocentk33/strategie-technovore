from pathlib import Path
import importlib.util, tempfile, subprocess, sys
sys.dont_write_bytecode=True
HERE=Path(__file__).resolve().parent
spec=importlib.util.spec_from_file_location('psd',HERE.parents[2]/'ressources/miniatures/psd.py')
mod=importlib.util.module_from_spec(spec);spec.loader.exec_module(mod)
def chrome(url,*args):
 with tempfile.TemporaryDirectory(prefix='miniature-psd-') as profile:
  return subprocess.run([mod.CHROME,'--headless=new',f'--user-data-dir={profile}','--hide-scrollbars','--allow-file-access-from-files','--window-size=1280,720','--force-device-scale-factor=3','--virtual-time-budget=3000',*args,url],capture_output=True,text=True,check=True).stdout
mod.chrome=chrome
with tempfile.TemporaryDirectory() as tmp:
 for v in (sys.argv[1:] or ('h','i','j')):
  mod.build((HERE/'propositions/miniature-kai.html').as_uri()+f'?v={v}', HERE/'photocraft'/f'{v}-kai.psd',tmp)
