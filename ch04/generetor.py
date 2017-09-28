# -*- coding: utf-8 -*-
g = (x*x for x in range(10))
for n in g:
	print n

def fib(max):
	n,a,b = 0,0,1
	while n < max:
		yield b
		a,b = b, a+b
		n = n+1
for n in fib(6):
	print n

# 生成器是一种迭代器，可以将list和函数包装成迭代器。
# 生成器包装list时，是一种以时间换空间的策略。
# 生成器原理上是一种for循环的过程中不断计算出下一个元素，类似斐波那契函数那样。