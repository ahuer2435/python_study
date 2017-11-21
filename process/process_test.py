# -*- coding: utf-8 -*-
from multiprocessing import Process
import os

def run_proc(name):
	print "run child process, name:%s, id:%d." % (name,os.getpid())

if __name__ == '__main__':
	print "Parent process,id:%s ." % os.getpid()
	p=Process(target=run_proc,args=('test',))
	p.start()
	p.join()	#等待子进程结束，未结束时，等待。
	print "Process end."	
#使用multiprocessing模块，可以创建跨平台的python程序。
#getpid()函数兼容linux和winds。