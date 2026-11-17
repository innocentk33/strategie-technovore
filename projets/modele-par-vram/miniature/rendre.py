#!/usr/bin/env python3
"""Rend les 3 PNG 4K et les PSD à textes modifiables ; profil Chrome isolé."""
from pathlib import Path
import importlib.util, subprocess, tempfile, sys, json
from PIL import Image, ImageDraw, ImageFont
HERE=Path(__file__).resolve().parent
ROOT=HERE.parents[2]
PAGE=HERE/'propositions/miniature-kai.html'
spec=importlib.util.spec_from_file_location('psd',ROOT/'ressources/miniatures/psd.py')
psd=importlib.util.module_from_spec(spec);spec.loader.exec_module(psd)
with tempfile.TemporaryDirectory(prefix='kai-chrome-') as profile, tempfile.TemporaryDirectory(prefix='kai-psd-') as tmp:
 def chrome(url,*args):
  return subprocess.run([psd.CHROME,'--headless=new','--no-first-run','--hide-scrollbars','--allow-file-access-from-files','--user-data-dir='+profile,'--window-size=1280,720','--force-device-scale-factor=3','--virtual-time-budget=3500',*args,url],capture_output=True,text=True,check=True).stdout
 psd.chrome=chrome
 for v in ['h','i','j']:
  (HERE/'rendus').mkdir(exist_ok=True)
  chrome(PAGE.as_uri()+'?v='+v,'--screenshot='+str(HERE/'rendus'/f'{v}-kai.png'))
  if '--png-only' not in sys.argv: psd.build(PAGE.as_uri()+'?v='+v,HERE/'photocraft'/f'{v}-kai.psd',tmp)
# Planche 168 px et test moitie basse cachee, tous visibles sans zoom.
a=HERE/'apercu';a.mkdir(exist_ok=True)
board=Image.new('RGB',(600,300),'#0f0f0f');d=ImageDraw.Draw(board)
for n,v in enumerate('hij'):
 im=Image.open(HERE/'rendus'/f'{v}-kai.png').convert('RGB').resize((168,95),Image.Resampling.LANCZOS)
 x=20+n*195;d.text((x,8),v,fill='white');board.paste(im,(x,30))
 test=im.copy();ImageDraw.Draw(test).rectangle((0,48,168,95),fill='#303030');board.paste(test,(x,165))
d.text((20,140),'50 % : moitie basse masquee',fill='white')
board.save(a/'test-50-et-168px-kai.png')
print('PNG 4K, planche 168 px et 50 %, PSD exportes.')
