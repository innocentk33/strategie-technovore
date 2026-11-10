"""Détoure la main gauche de sources/mains-darkness-stocksnap-cc0.jpg (« Hands Darkness », StockSnap, CC0) → photocraft/main-detouree.png.
Variante d. Contour tracé à la main (polygone), agrandi ×3 : la seule version en ligne fait 960 px de large.
À remplacer par la photo des mains de l'auteur. Usage : python3 -I photocraft/detoure-main.py (depuis miniature/)."""
from PIL import Image, ImageDraw, ImageFilter
# contour relevé sur un agrandissement ×4 de la zone (180, 750) : x = 180 + px/4, y = 750 + py/4
D = [(60,840),(80,660),(110,590),(170,520),(250,460),(330,420),(420,385),(480,340),(540,280),(600,215),(680,190),(780,165),(860,140),(910,105),(980,72),
     (1080,52),(1180,40),(1230,50),(1240,85),(1210,115),(1150,140),(1090,165),(1050,190),(1090,250),(1112,300),(1095,345),(1050,355),(990,330),(930,300),
     (880,330),(900,400),(950,460),(1000,520),(1015,575),(1050,565),(1150,560),(1240,585),(1278,630),(1260,670),(1200,690),(1080,715),(950,740),(800,770),
     (650,795),(480,805),(400,822)]
P = [(180 + x / 4, 750 + y / 4) for x, y in D] + [(283, 1000), (300, 1150), (320, 1304), (165, 1304), (172, 1100), (175, 960)]  # avant-bras
im = Image.open("sources/mains-darkness-stocksnap-cc0.jpg").convert("RGB")
mask = Image.new("L", im.size, 0)
ImageDraw.Draw(mask).polygon(P, fill=255)
im.putalpha(mask.filter(ImageFilter.GaussianBlur(1.2)))
im = im.crop(mask.getbbox())
im.resize((im.width * 3, im.height * 3), Image.LANCZOS).save("photocraft/main-detouree.png")
