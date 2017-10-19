# -*- coding: utf-8 -*-
# int函数的特性是将字符串转化为整数。base指定进制，表示字符串按照base进制表示的数，int返回的是转换后的十进制数
print int("123")
print int("123",base=16)
print int("123",16)
print int("1010",2)

# 定义一个二进制转化函数。
def int2(x):
	return int(x,2)
print int2('101011')

# 偏函数的应用
import functools
int8 = functools.partial(int,base=8)
print int8('234')

max10 = functools.partial(max,10)
print max10(2,3,4,5)
# 偏函数通过functools下的partial函数实现，功能是固定函数的一个参数，进而封装成一个新的函数。
