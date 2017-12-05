# -*- coding: utf-8 -*-
import Image,ImageFilter
im = Image.open("./test.jpg")
im2 = im.filter(ImageFilter.BLUR)
im2.save("./test2.jpg","jpeg")
#使用ImageFilter模块使图像变模糊。