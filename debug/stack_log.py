# -*- coding: utf-8 -*-
import logging
def foo(s):
	return 10 / int(s)

def bar(s):
	return foo(s)*2

def main():
	try:
		bar(0)
	except Exception as e:
		logging.exception(e)
	else:
		pass
	finally:
		pass
	print "end"

main()
#可以使用logging模块记录错误，执行时，除了报错之外，程序可以继续执行。
#后面学过IO时，可以将stack保存到文件。