# -*- coding: utf-8 -*-
def calc_sum(*args):
	sum = 0
	for n in args:
		sum = sum + n
	return sum

f = calc_sum(1,3,5)
print f

# 可变参数函数定义及调用。这里的f是函数调用

def laze_sum(*args):
	def sum():
		ax = 0
		for n in args:
			ax = ax + n
		return ax
	return sum
f = laze_sum(1,3,5,7)
f2 = laze_sum(1,3,5,7)
print f == f2
print f()
# 这里的f是函数sum，f()才是函数调用。laze_sum函数每次返回的函数sum都是不同的。

def count():
	fs = []
	for i in range(1,4):
		def f():
			return i*i
		fs.append(f)
	return fs
f1,f2,f3= count()	#count函数返回的是一个list，所以左值也应该是一个list。
print f1()
print f2()
print f3() 
# 结果都是9，即i值都是用的for循环最后的值3，而不是，1,2,3的对应使用。返回函数不要引用任何循环变量或者后继会改变的变量，否则结果可能与预期不一致。

def count():
	fs = []
	for i in range(1,4):
		def f(j):
			def g():
				return j*j
			return g
		fs.append(f(i))
	return fs
f1,f2,f3= count()	#相当于f1 = f(1)的地址，以此类推。
print f1()
print f2()
print f3() 
# 其实就是讲，返回函数返回的是函数，参数使用最终的结果，就是表明返回函数的执行时机是比较靠后的。



