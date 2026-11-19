from pathlib import Path
from PIL import Image,ImageDraw
p=Path(__file__).resolve().parent
for w,name,half in [(168,'comparaison-168px.png',False),(640,'comparaison-640px.png',False),(640,'comparaison-50-pourcent.png',True)]:
 h=round(w*9/16);gap=24;sheet=Image.new('RGB',(3*w+4*gap,h+60),(15,15,15));d=ImageDraw.Draw(sheet)
 for n,v in enumerate('hij'):
  im=Image.open(p/'rendus'/f'{v}-kai.png').convert('RGB').resize((w,h),Image.Resampling.LANCZOS)
  if half:ImageDraw.Draw(im).rectangle((0,h//2,w,h),fill=(55,55,55))
  x=gap+n*(w+gap);sheet.paste(im,(x,36));d.text((x,12),v.upper(),fill='white')
 sheet.save(p/'apercu/kai'/name)
