"""Planches et contrôle des PNG/PSD de cette miniature. --convert rouvre les PSD."""
from pathlib import Path
from PIL import Image,ImageDraw,ImageChops,ImageStat
import hashlib,json,struct,subprocess,sys
root=Path(__file__).resolve().parent
out=root/'apercu/kai';out.mkdir(parents=True,exist_ok=True)
if '--convert' in sys.argv:
 for v in 'hij':
  subprocess.run([str(Path.home()/'.local/bin/photocraft-cli'),'convert',str(root/f'photocraft/{v}-kai.psd'),str(out/f'{v}-psd-verifie.png')],capture_output=True,text=True,check=True)
board=Image.new('RGB',(620,335),'#0f0f0f');dr=ImageDraw.Draw(board)
large=Image.new('RGB',(1968,410),'#0f0f0f');dl=ImageDraw.Draw(large)
verify=Image.new('RGB',(1968,810),'#0f0f0f');dv=ImageDraw.Draw(verify)
report={'date':'2026-11-19','project':root.parent.name,'variants':{}}
for n,v in enumerate('hij'):
 png=root/f'rendus/{v}-kai.png';psd=root/f'photocraft/{v}-kai.psd'
 a=Image.open(png).convert('RGB');b=Image.open(out/f'{v}-psd-verifie.png').convert('RGB');raw=psd.read_bytes();h=struct.unpack('>4sH6sHIIHH',raw[:26]);types=raw.count(b'TySh')
 assert h[0]==b'8BPS' and (h[5],h[4])==(3840,2160) and types==3
 assert a.size==b.size==(3840,2160)
 x=24+n*200;dr.text((x,12),v.upper(),fill='white');board.paste(a.resize((168,95),Image.Resampling.LANCZOS),(x,35));half=a.resize((168,95),Image.Resampling.LANCZOS);ImageDraw.Draw(half).rectangle((0,48,168,95),fill='#383838');board.paste(half,(x,175))
 x=12+n*652;dl.text((x,8),v.upper(),fill='white');large.paste(a.resize((640,360),Image.Resampling.LANCZOS),(x,34));verify.paste(a.resize((640,360),Image.Resampling.LANCZOS),(x,35));verify.paste(b.resize((640,360),Image.Resampling.LANCZOS),(x,435));dv.text((x,10),v+' PNG',fill='white');dv.text((x,410),v+' PSD rouvert',fill='white')
 report['variants'][v]={'png_dimensions':list(a.size),'psd_dimensions':[h[5],h[4]],'editable_type_blocks':types,'png_sha256':hashlib.sha256(png.read_bytes()).hexdigest(),'psd_sha256':hashlib.sha256(raw).hexdigest(),'psd_png_mean_absolute_error':round(sum(ImageStat.Stat(ImageChops.difference(a,b)).mean)/3,4),'png_bytes':png.stat().st_size,'psd_bytes':len(raw)}
dr.text((24,149),'Moitié basse masquée — 50 %',fill='white');board.save(out/'test-50-et-168px.png');large.save(out/'comparaison-640px.png');verify.save(out/'verification-psd.png');(out/'verification-technique.json').write_text(json.dumps(report,ensure_ascii=False,indent=2))
print(root.parent.name,{k:r['psd_png_mean_absolute_error'] for k,r in report['variants'].items()})
