# -*- coding: utf-8 -*-
import Image
im = Image.open("./test.jpg")
w,h = im.size
im.thumbnail((w//2,h//2))	#缩放50%的记法。
im.save("./test1.jpg","jpeg")
print w,h
#使用Image模块对图像的操作。