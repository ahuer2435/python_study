# -*- coding: utf-8 -*-
L = "123456"
def char2num(x):
	return {"0":0,"1":1,"2":2,"3":3,"4":4,"5":5,"6":6,"7":7,"8":8,"9":9}[x]
print char2num("9")

def fn(x,y):
	return x*10+y
print fn(1,2)

print map(char2num,L)
print reduce(fn,map(char2num,L))
# 规则fn累积处理列表，先处理前两个，再与后一个累积处理。