# -*- coding: utf-8 -*-
import time,threading
balance = 0
lock = threading.Lock()

def change_it(n):
	global balance
	balance = balance+n
	balance = balance-n

def run_thread(n):
	for i in range(1000000):
		lock.acquire()
		try:
			change_it(n)
		finally:
			lock.release()

t1=threading.Thread(target=run_thread,args=(5,))
t2=threading.Thread(target=run_thread,args=(10,))
t1.start()
t2.start()
t1.join()
t2.join()
print balance
#采用Lock模块，消除多进程之间的竞争。
#python并不是一种高效的语言，每一个进程都要有一个GIL锁，进程中每个线程执行前都需要先获取锁，
#每执行100字节，解释器自动释放锁，让别的线程执行，故python的多线程其实还是串行执行的。