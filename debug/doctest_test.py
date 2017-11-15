# -*- coding: utf-8 -*-
class Dict(dict):
	'''
	>>> d1 = Dict()
	>>> d1['x'] = 100
	>>> d1.x
	100
	>>> d1.y = 200
	>>> d1['y']
	200
	 >>> d2 = Dict(a=1, b=2, c='3')
    >>> d2.c
    '3'
    >>> d2['empty']
    Traceback (most recent call last):
        ...
    KeyError: 'empty'
    >>> d2.empty
    Traceback (most recent call last):
        ...
    AttributeError: 'Dict' object has no attribute 'empty'
    '''
	def __init__(self, **kw):
		super(Dict,self).__init__(**kw)	# 返回的是基类

	def __getattr__(self,key):
		try:
			return self[key]
		except KeyError:
			raise AttributeError(r"'Dict' object has no attribute '%s'" % key)

	def __setattr__(self,key,value):
		self[key] = value

if __name__=='__main__':
	import doctest
	doctest.testmod()
	print "test start."


#doctest模块实现以注释的形式测试代码。expected提示出错的地方；got提示应该出现的东西，调用栈使用...代替。