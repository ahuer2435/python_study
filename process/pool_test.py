# -*- coding: utf-8 -*-
from multiprocessing import Pool
import os,time,random

def long_def_task(name):
	print 'Run task,name: %s, id: %d.' % (name, os.getpid())
	start = time.time()
	time.sleep(random.random()*3)
	end = time.time()
	print 'Task %s runs %0.2f seconds' % (name,(end-start))

if __name__=='__main__':
	print "Parent process %d." % os.getpid()
	p=Pool(2)
	for i in range(5):
		p.apply_async(long_def_task,args=(i,))	#p代表一个容器，可以通过apply_async函数放入进程，放入的进程自动执行。
	print "waiting all subprocesses done.."
	p.close()	#代表不可再放入进程，
	p.join()
	print "all subprocesses done."	
#利用Pool可以批量创建启动子进程。