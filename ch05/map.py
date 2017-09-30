# -*- coding: utf-8 -*-
L = [1,3,5,7,9,11]
def f(x):
	return x*x
print map(f,L)


L = ['adam', 'LISA', 'barT']
def char_pr(s):
	return s.islower()
print char_pr('a')

def str_pr1(s):
	return s.lower()
print str_pr1('AsDF')
def str_pr2(s):
	return s.capitalize()
print str_pr2("aSDFG")

print map(str_pr2,L)

# 规则f遍历L，返回一个列表。