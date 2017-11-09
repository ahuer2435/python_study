# -*- coding: utf-8 -*-
def foo(s):
	return 10 / int(s)

def bar(s):
	return foo(s)*2

def main():
	try:
		bar(1)
		print "no error."
	except StandardError,e:
		print "Error."
	else:
		print "else no error."
	finally:
		print "finally"
	print "end"

main()
#使用try...except...else...finally ...语句的好处有：
#1. 记录出错的地方，便与调试，即打log。
#2. 使程序可以继续执行，不至于崩溃掉。