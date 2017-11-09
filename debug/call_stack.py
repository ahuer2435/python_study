# -*- coding: utf-8 -*-
def foo(s):
	return 10 / int(s)

def bar(s):
	return foo(s)*2

def main():
	
	bar(0)
	print "end"

main()
#程序中的异常会层层上报，如果连主程序中都没有异常处理，
#最后异常会被python解释器捕获，然后打印调用栈内容，其中
#会从程序出错的地方开始，按照调用顺序，一步步打印到出错的源头。