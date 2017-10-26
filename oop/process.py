# -*- coding: utf-8 -*-
std1 = {'name':'hank','score':99}
std2 = {'name':'hunk','score':100}

def print_score(std):
	print '%s: %s' % (std['name'],std['score'])
print_score(std1)
print_score(std2)

#面向过程打印学生名字和分数。
#面向过程：计算机程序视为一系列的命令集合，即一组函数的顺序执行。为了简化程序设计，
#面向过程把函数继续切分为子函数，即把大块函数通过切割成小块函数来降低系统的复杂度。