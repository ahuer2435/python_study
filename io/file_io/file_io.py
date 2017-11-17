# -*- coding: utf-8 -*-
with open("./test.txt",'r') as f:
	print f.read()

f = open("./test.txt",'r')
for line in f.readlines():
	print(line.strip())
f.close()

#with open("./1.png",'rb') as f:
#	print f.read()

with open("./china.txt",'rb') as f:
	print f.read()


f = open("./test_write",'w')
f.write("hello 中国\n")
f.close()