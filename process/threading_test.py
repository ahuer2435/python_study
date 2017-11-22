# -*- coding: utf-8 -*-
import time,threading

def loop():
	print "in loop thread %s is running..." % threading.current_thread().name
	n = 0
	while n < 5:
		n=n+1
		#print "thread %s >>> %s" (threading.current_thread().name,n)
		time.sleep(1)
	print "in loop thread %s ended." % threading.current_thread().name

print "thread %s is running...." % threading.current_thread().name
t=threading.Thread(target=loop,name="LoopThread")
t.start()
t.join()
print "thread %s end." % threading.current_thread().name
#主线程默认名字为MainThread。
#创建线程的接口threading.Thread()，设置线程函数以及线程名字，名字默认Thread-1，Thread-2，...