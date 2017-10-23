#!/usr/bin/env python
# -*- coding: utf-8 -*-
import Image					#引入模块
im = Image.open('test.png')		#打开图像文件
print im.format, im.size, im.mode		#查看文件属性

im.thumbnail((300,200))
im.save('thumb.jpg', 'JPEG')
print im.format, im.size, im.mode

#安装PIL指令：
#sudo apt-get build-dep python-imaging
#sudo apt-get install libjpeg8 libjpeg62-dev libfreetype6 libfreetype6-dev
#sudo pip install Pillow

#检测安装是否成功：
# $ python
# >>> import PIL
# >>> PIL.VERSION
# '1.1.7'
# 参考：http://blog.csdn.net/hanshileiai/article/details/51681239

# python当前环境的查看与设置：
import sys
print sys.path
sys.path.append('/workspace/python_study/')			#临时修改
print sys.path

# 永久修改
print PYTHONPATH