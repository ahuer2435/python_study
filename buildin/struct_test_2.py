# -*- coding: utf-8 -*-
import struct
print struct.pack('>I',10240099)
#unpack将字符串转化为整数
print struct.unpack('>HI','\xf0\xf0\xf0\xf0\x80\x80')
s = '\x42\x4d\x38\x8c\x0a\x00\x00\x00\x00\x00\x36\x00\x00\x00\x28\x00\x00\x00\x80\x02\x00\x00\x68\x01\x00\x00\x01\x00\x18\x00'
print struct.unpack('<ccIIIIIIHH',s)
#struct功能就是字符串和数字字符相互转化的功能。
#pack调用两个参数，第一个是处理指令，明白其含义；第二个代表待处理字符串或者整数。