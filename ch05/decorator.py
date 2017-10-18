# -*- coding: utf-8 -*-
def now():
	print 'henllo now'
f = now
print f.__name__		#__name__返回函数对象的名字

def log(func):			#这是一个decorator的定义，其本质是一个返回函数的高阶函数，即参数为函数，返回的也是函数。
	def wrapper(*args, **kw):	#def wrapper():
		print 'call %s():' % func.__name__
		return func(*args, **kw) #return func()
	return wrapper
#@log				#decorator的使用方法，等价于now = log(now)
def now():
	print '2017-1-23'
#now = log(now)		#用此等式代替@log也可以的。
now()
print now.__name__ #为啥这里还是now，而不是wrapper？
#注：不明白被注释部分，即func函数带参数为什么也可用，因为函数定义now不带参数，理论上func调用也是无参的才对，不明白？？

def log(text):		#通过在顶层再定义一层函数，来实现向decorator传递参数。
	def decorator(func):
		def wrapper(*args, **kw):
			print '%s %s():' % (text,func.__name__)
			return func(*args, **kw)
		return wrapper
	return decorator
@log('execute')			#等价于now = log('execute')(now)，以此来理解此式。log('execute')返回的是decorator函数，然后以now为参数，调用此函数。
def now():
	print '2017-2-24'
now()
print now.__name__ 		#打印wrapper

#在wrapper中保留now属性
import functools
def log(text):
	def  decorator(func):
		@functools.wraps(func)
		def wrapper(*args,**kw):
			print '%s %s():' % (text,func.__name__)
			return func(*args,**kw)
		return wrapper
	return decorator
@log('execute')			#等价于now = log('execute')(now)，以此来理解此式。log('execute')返回的是decorator函数，然后以now为参数，调用此函数。
def now():
	print '2017-3-24'
now()
print now.__name__  	#打印now，functools作用
