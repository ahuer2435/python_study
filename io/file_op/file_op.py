# -*- coding: utf-8 -*-
import os
print os.name
print os.uname()
print os.environ
print os.getenv("PATH")

print os.path.abspath(".")
#os.mkdir("/home/yanqiao/workspace/python_study/io/file_op/test")
#os.rmdir("/home/yanqiao/workspace/python_study/io/file_op/test")
print os.path.join("/home/yanqiao/workspace","test")	#不依赖于具体目录或文件，纯字符串操作
print os.path.split("/home/yanqiao/workspace/test.txt")
print os.path.splitext("/home/yanqiao/workspace/test.txt")

for x in os.listdir('.'):
	if os.path.isdir(x):
		print x

for x in os.listdir('.'):
	if os.path.splitext(x)[1] == '.py':
		print x
