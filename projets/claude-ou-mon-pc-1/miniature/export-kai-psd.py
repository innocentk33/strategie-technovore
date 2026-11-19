#!/usr/bin/env python3
"""Reproduction Kai h/i/j : PNG 4K et PSD. Conserve le pipeline historique."""
from pathlib import Path
import importlib.util,subprocess,tempfile,json,sys,hashlib
from PIL import Image,ImageDraw,ImageChops,ImageStat
HERE=Path(__file__).resolve().parent;ROOT=HERE.parents[2];PAGE=HERE/'propositions/miniature-kai.html'
spec=importlib.util.spec_from_file_location('psd',ROOT/'ressources/miniatures/psd.py');psd=importlib.util.module_from_spec(spec);spec.loader.exec_module(psd)
variants=[v for v in sys.argv[1:] if v in ('h','i','j')] or list('hij')
with tempfile.TemporaryDirectory(prefix='kai19-chrome-') as profile,tempfile.TemporaryDirectory(prefix='kai19-psd-') as tmp:
 def chrome(url,*args):
  return subprocess.run([psd.CHROME,'--headless=new','--no-first-run','--hide-scrollbars','--allow-file-access-from-files','--user-data-dir='+profile,'--window-size=1280,720','--force-device-scale-factor=3','--virtual-time-budget=3500',*args,url],capture_output=True,text=True,check=True).stdout
 psd.chrome=chrome
 for v in variants:
  (HERE/'rendus').mkdir(exist_ok=True)
  if '--psd-only' not in sys.argv:chrome(PAGE.as_uri()+'?v='+v,'--screenshot='+str(HERE/'rendus'/f'{v}-kai.png'))
  if '--png-only' not in sys.argv:psd.build(PAGE.as_uri()+'?v='+v,HERE/'photocraft'/f'{v}-kai.psd',tmp)
a=HERE/'apercu/kai';a.mkdir(exist_ok=True,parents=True)
board=Image.new('RGB',(600,300),'#0f0f0f');dr=ImageDraw.Draw(board);large=Image.new('RGB',(1952,390),'#111');ld=ImageDraw.Draw(large)
for n,v in enumerate('hij'):
 im=Image.open(HERE/'rendus'/f'{v}-kai.png').convert('RGB');x=20+n*195;small=im.resize((168,95),Image.Resampling.LANCZOS);dr.text((x,8),v,fill='white');board.paste(small,(x,30));test=small.copy();ImageDraw.Draw(test).rectangle((0,48,168,95),fill='#333');board.paste(test,(x,165));large.paste(im.resize((640,360),Image.Resampling.LANCZOS),(n*656,30));ld.text((n*656,8),v,fill='white')
dr.text((20,140),'50 % : moitie basse masquee',fill='white');board.save(a/'test-50-et-168px.png');board.crop((0,0,600,130)).save(a/'comparaison-168px.png');large.save(a/'comparaison-640px.png');half=large.copy();hd=ImageDraw.Draw(half)
for n in range(3):hd.rectangle((n*656,210,n*656+640,390),fill='#333')
half.save(a/'comparaison-50-pourcent.png')
report=[]
for v in 'hij':
 png=HERE/'rendus'/f'{v}-kai.png';item={'variante':v,'png':list(Image.open(png).size),'sha256':hashlib.sha256(png.read_bytes()).hexdigest()};f=HERE/'photocraft'/f'{v}-kai.psd'
 if f.exists():
  info=json.loads(subprocess.check_output([psd.PCLI,'info',str(f)]));item.update(psd=[info['width'],info['height']],calques_texte=[x.get('text') for x in info['layers'] if x['kind']=='Type'],avertissements=info['warnings']);converted=a/f'{v}-psd-reouvert.png';subprocess.run([psd.PCLI,'convert',str(f),str(converted)],check=True,capture_output=True);im=Image.open(png).convert('RGB');other=Image.open(converted).convert('RGB');item['difference_moyenne_png_psd']=sum(ImageStat.Stat(ImageChops.difference(im,other)).mean)/3
 report.append(item)
(a/'verification-technique.json').write_text(json.dumps(report,ensure_ascii=False,indent=2));print('PNG, PSD et planches Kai : termines')
