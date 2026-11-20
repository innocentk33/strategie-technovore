from pathlib import Path
from PIL import Image,ImageDraw
p=Path(__file__).resolve().parent
for width,name,half in [(168,'comparaison-168px.png',False),(500,'comparaison-500px.png',False),(168,'test-50-et-168px-kai.png',True),(500,'test-50-pourcent-500px.png',True)]:
 h=round(width*9/16);gap=24
 sheet=Image.new('RGB',(3*width+4*gap,h+60),(15,15,15));d=ImageDraw.Draw(sheet)
 for n,v in enumerate('hij'):
  im=Image.open(p/'rendus'/f'{v}-kai.png').convert('RGB').resize((width,h),Image.Resampling.LANCZOS)
  if half: ImageDraw.Draw(im).rectangle((0,h//2,width,h),fill=(55,55,55))
  x=gap+n*(width+gap);sheet.paste(im,(x,36));d.text((x,12),v.upper(),fill='white')
 sheet.save(p/'apercu'/name)
