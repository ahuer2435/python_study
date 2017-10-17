# -*- coding: utf-8 -*-
print map(lambda x: x*x, [1,3,5,7,9])

f = lambda x: x*x			#匿名函数作为函数对象
l = [2,4,6,8]
print map(f,l)

def build(x,y):
	return lambda: x+y		#匿名函数作为返回值
print build(4,5)()			#返回值是函数名，调用需要加入().

# python 对匿名函数支持有限，可以少用吧