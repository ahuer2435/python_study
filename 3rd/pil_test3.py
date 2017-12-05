# -*- coding: utf-8 -*-
import Image,ImageDraw,ImageFont,ImageFilter
import random

def rndChar():
	return chr(random.randint(65,90))

def rndColor():
	return (random.randint(64,255),random.randint(64,255),random.randint(64,255))

def rndColor2():
	return (random.randint(32,127),random.randint(32,127),random.randint(32,127))

width = 60 * 4		#宽度
height = 60			#高度
image = Image.new("RGB",(width,height),(255,255,255))
font = ImageFont.truetype("Arial.ttf",36)
draw = ImageDraw.Draw(image)	#通过image创建draw。

#填充随机240*60随机颜色
for x in range(width):
	for y in range(height):
		draw.point((x,y),fill=rndColor())

#填充随机字符
#参数：位置，字符，字体，颜色。
for t in range(4):
	draw.text((60*t+10,10),rndChar(),font=font,fill=rndColor2())

#模糊图像
image = image.filter(ImageFilter.BLUR)
image.save("./code3.jpg","jpeg")	

#通过draw绘制图像和字符，注意draw的定义，以image为参数。