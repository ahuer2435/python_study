# -*- coding: utf-8 -*-
L = [1,2,3,4,5,6,7,8]
def is_odd(x):
	return x % 2 == 1
print filter(is_odd,L)

L = ["qw","a"," ","","tyu"]
def not_emtry(s):
	return s and s.strip()
print filter(not_emtry,L)
