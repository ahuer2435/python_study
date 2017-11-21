# -*- coding: utf-8 -*-
from multiprocessing import Process,Queue
import os,time,random

def write(q):
	for value in ['a','b','c']:
		print "put %s to queue." % value
		q.put(value)
		time.sleep(random.random())

def read(q):
	while True:
		value = q.get(True)
		print "get %s from queue." % value

if __name__=="__main__":
	q = Queue()
	pw = Process(target=write,args=(q,))
	pr = Process(target=read,args=(q,))
	pw.start()
	pr.start()
	pw.join()
	pr.terminate()	#read是死循环，不会自己结束，所以使用terminate结束之。

#进程间通信可以通过Queue，也可以通过Pipes，前者先进先出，后者相反。
#语法应该类似。

