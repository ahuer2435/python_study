# -*- coding: utf-8 -*-

def foo(s):
	return 10 / int(s)

def bar(s):
	try:
		foo(s)*2
	except StandardError,e:
		print "Error and raise"
		raise e 					#这里的except部分只是记录了此处出错，但是并未对错误做处理，所以可以把异常继续上报，让上一级去处理，执行结果和stack_log.py差不多。 
	

def main():
	try:
		bar(0)
	except Exception,e:
		logging.exception(e)
	else:
		pass
	finally:
		pass
	print "end"

main()
#可以使用logging模块记录错误，执行时，除了报错之外，程序可以继续执行。
#后面学过IO时，可以将stack保存到文件。