import qrcode
import os
from PIL import Image
import time
start = time.time()
os.system("curl https://cdn.discordapp.com/avatars/604983644733440001/6503367a6e2d56010c24895a03e936f1.webp?size=128 > D:\\코딩\\모듈\\test.png")
print(time.time() - start)

s_img = Image.open("D:\\코딩\\모듈\\test.png")
s_img.thumbnail((60, 60))
qr = qrcode.QRCode(error_correction=qrcode.constants.ERROR_CORRECT_H)
qr.add_data(":)")
qr.make()
se_img = qr.make_image().convert("RGB")

pos = ((se_img.size[0] - s_img.size[0]) // 2, (se_img.size[1] - s_img.size[1]) // 2)
se_img.paste(s_img, pos)
se_img.save("D:\\코딩\\모듈\\test.png")