# -*- coding: utf-8 -*-
def reversed_cmp(x,y):
	if x < y:
		return 1
	elif x > y:
		return -1
	return 0

print sorted([2,4,5,3,2,7,8,12,0],reversed_cmp)

def ignore_case_cmp(x,y):
	s1 = x.upper()
	s2 = y.upper()
	if s1 < s2:
		return -1
	elif s1 > s2:
		return 1
	return 0

print sorted(['Atut','dtydyt','sgsg','vui','GUGj'],ignore_case_cmp)

# 高阶函数sorted接受其他函数作为参数实例
# 比较结果 返回-1 为小于< ;1 为大于；0为相等