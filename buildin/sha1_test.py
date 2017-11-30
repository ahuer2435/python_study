# -*- coding: utf-8 -*-
import hashlib
str1 = "how to use md5 in "
str2 = "python hashlib"

sha1 = hashlib.sha1()
sha1.update(str1)
sha1.update(str2)
print sha1.hexdigest()

sha12 = hashlib.sha1()
sha12.update("how to use md5 in python hashlib")
print sha12.hexdigest()

#hashlib模块提供sha1功能，sha1用于签名，把一段内容摘录为160bit字节，通常用40个16进制表示。