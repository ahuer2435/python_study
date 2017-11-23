# -*- coding: utf-8 -*-
import threading
local_school = threading.local()

def process_student():
	print "hello, %s (in %s)" % (local_school.student,threading.current_thread().name)

def process_thread(name):
	local_school.student = name
	process_student()

t1 = threading.Thread(target=process_thread,args=("Alice",),name="Thread-A")
t2 = threading.Thread(target=process_thread,args=("Bob",),name="Thread-B")
t1.start()
t2.start()
t1.join()
t2.join()
#python提供ThreadLocal对象，用threading.local()实现的全局变量local_school
#可以看成一个dict，可以往里面添加属性，每个属性可以看成是线程独立的一份拷贝，
#修改不胡干扰，这就是现实不同线程间的通信