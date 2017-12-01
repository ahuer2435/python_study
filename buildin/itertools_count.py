# -*- coding: utf-8 -*-
import itertools
natuals = itertools.count(2.1)
for n in natuals:
	print n
#count用于输出无线的整数序列

#cs = itertools.cycle("ABC")
#for c in cs:
#	print c
#cycle迭代器的循环可以选择字符串中的每个字符。

#ns = itertools.repeat("ab",10)
#for n in ns:
#	print n
#repeat迭代器的循环只能是整个字符串。可以设置重复次数