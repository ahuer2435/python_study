# -*- coding: utf-8 -*-
import hashlib
str1 = "how to use md5 in "
str2 = "python hashlib"

md5 = hashlib.md5()
md5.update(str1)
md5.update(str2)
print md5.hexdigest()

md52 = hashlib.md5()
md52.update("how to use md5 in python hashlib")
print md52.hexdigest()

#hashlib模块提供md5功能，md5用于签名，把一段内容摘录为128bit字节，通常用32个16进制表示。