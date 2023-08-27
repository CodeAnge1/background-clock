import os
import time
import ctypes
from datetime import datetime as dt
from PIL import Image, ImageDraw, ImageFont

# date_time = str(dt.now()).split('.')[0].split(' ')[1]

font = ImageFont.truetype(f'{os.getcwd()}/font.ttf', 72)
ImageDraw.ImageDraw.font = ImageFont.truetype(f'{os.getcwd()}/font.ttf', 72)

while True:
	img = Image.open('background.jpg')
	img = Image.open('background.jpg')
	img_w, img_h = img.size
	d = ImageDraw.Draw(img)
	date_time = str(dt.now()).split('.')[0].split(' ')[1]
	x1, y1, x2, y2 = d.textbbox((0,0), date_time, font=font)

	t_w, t_h = x2-x1, y2-y1

	d.text((img_w//2-t_w//2, 150), date_time, fill=(255, 255, 255))

	img.save("new.jpg")
	SPI_SETDESKWALLPAPER = 20 
	ctypes.windll.user32.SystemParametersInfoW(20, 0, "new.jpg" , 0)
