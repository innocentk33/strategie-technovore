from pathlib import Path
import hashlib,json,subprocess
from PIL import Image,ImageChops,ImageDraw,ImageStat

p=Path(__file__).resolve().parent
pcli=str(Path.home()/'.local/bin/photocraft-cli')
report={}
sheet=Image.new('RGB',(1596,341),(15,15,15));draw=ImageDraw.Draw(sheet)
for n,v in enumerate('hij'):
 png=p/'rendus'/f'{v}-kai.png';psd=p/'photocraft'/f'{v}-kai.psd'
 info=json.loads(subprocess.check_output([pcli,'info',str(psd)]))
 target=p/'apercu'/f'{v}-psd-verifie.png'
 subprocess.run([pcli,'convert',str(psd),str(target)],check=True,capture_output=True)
 original=Image.open(png).convert('RGB');reopened=Image.open(target).convert('RGB')
 diff=ImageChops.difference(original,reopened)
 layers=[x for x in info['layers'] if x['kind']=='Type']
 item={'png':list(original.size),'png_octets':png.stat().st_size,'sha256_png':hashlib.sha256(png.read_bytes()).hexdigest(),'psd': [info['width'],info['height']], 'psd_octets':psd.stat().st_size,'calques_texte':len(layers),'textes':[x['text']['text'] for x in layers],'fontes':[x['text']['font'] for x in layers],'avertissements':info['warnings'],'difference_moyenne_255':sum(ImageStat.Stat(diff).mean)/3}
 if v!='i':
  face=Image.open(p/'sources'/('portrait-kai.png' if v=='h' else 'portrait-technovore.png'))
  item['portrait_bas_source_dans_page']=35+face.getbbox()[3]*740/face.width
  item['coupe_buste_sous_cadre']=item['portrait_bas_source_dans_page']>720
 assert original.size==(3840,2160)
 assert [info['width'],info['height']]==[3840,2160]
 assert len(layers)==3 and not info['warnings']
 assert all(x['text']['font']=='Archivo Black' for x in layers)
 report[v]=item
 x=24+n*524;sheet.paste(reopened.resize((500,281),Image.Resampling.LANCZOS),(x,36));draw.text((x,12),v.upper()+' PSD rouvert',fill='white')
(p/'apercu'/'verification-technique.json').write_text(json.dumps(report,ensure_ascii=False,indent=2)+'\n')
sheet.save(p/'apercu'/'verification-psd-500px.png')
print(json.dumps(report,ensure_ascii=False,indent=2))
