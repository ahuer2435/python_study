# -*- coding: utf-8 -*-
import types
class animal(object):					#类中若无数据，可以没有__init__函数。
	def run(self):
		print "annimal is running."

class cat(animal):
	def run(self):
		print "cat is running."

class dog(animal):
	def run(self):
		print "dog is running."

d = dog()

#type()函数接受一个对象，包含内建对象和自定义的，返回对象类型。
print "type() usage:"
print type(123)
print type('123')
print type(d)
print type(int)							#类型的type返回“type”
print type(123) == types.IntType		#可引入types模块，使用其中定义好的类型作为判断。

#isintance()函数用于判断一个对象是否属于一个或者几个类型。
print "isintance() usage: "
print isinstance(d,animal)
print isinstance(d,(int,dog))

print "dir() usage: "
print dir(d)
print dir("123")
print len("123")				#len()用于求对象“123”的长度，最终会调用该对象的函数成员__len__()，当然也可以重写此函数（多态性）；其他系统函数也可能和此一样。
print "123".__len__()

#hasattr setattr getattr对象操作函数，用于判断对象是否存在属性，获取属性、设置属性（属性亦可为函数成员）
print hasattr(d,'x')
print setattr(d,'x',"123")
print hasattr(d,'x')
print getattr(d,'x')
y =  getattr(d,'run')
y()
