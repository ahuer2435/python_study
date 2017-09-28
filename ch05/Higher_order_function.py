# -*- coding: utf-8 -*-
f = abs
print f(-10)

def add(x,y,f):
	return f(x)+f(y)
print add(6,-7,abs)
	
# 函数名视为一个变量，变量可以存储函数名。
# 高阶函数：函数可以作为参数传递给函数。