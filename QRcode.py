import qrcode
import os
from PIL import Image

s_img = Image.open("your path")
s_img.thumbnail((60, 60))
qr = qrcode.QRCode(error_correction=qrcode.constants.ERROR_CORRECT_H)
qr.add_data(":)")
qr.make()
se_img = qr.make_image().convert("RGB")

pos = ((se_img.size[0] - s_img.size[0]) // 2, (se_img.size[1] - s_img.size[1]) // 2)
se_img.paste(s_img, pos)
se_img.save("your path")
