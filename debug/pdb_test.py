# -*- coding: utf-8 -*-
import pdb
def foo(s):
	n = int(s)
	pdb.set_trace()
	return 10/n

def main():
	foo('0')

main()

# pdb 调试命令：
# n 执行下一跳
# l 显示源代码
# p n 查看变量n。