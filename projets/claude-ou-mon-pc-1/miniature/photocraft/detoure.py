"""RTX 5080 Founders Edition fournie par l'auteur le 05/11 (image produit NVIDIA, sources/rtx5080-fe-auteur.webp) → photocraft/rtx5080-detoure.png.
L'image arrive déjà détourée (canal alpha propre, équerre et connecteur PCIe compris) : on recadre au plus juste.
Usage : python3 -I photocraft/detoure.py (depuis miniature/)."""
from PIL import Image
im = Image.open("sources/rtx5080-fe-auteur.webp").convert("RGBA")
im.crop(im.getchannel("A").getbbox()).save("photocraft/rtx5080-detoure.png")
