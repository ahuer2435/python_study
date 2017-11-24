# -*- coding: utf-8 -*-
import time,sys,Queue
from multiprocessing.managers import BaseManager

#定义一个以BaseManager为基类的类QueueManager
class QueueManager(BaseManager):
	pass

#注册QueueManager，指定Queue的名字，这里的名字要和master中保持一致。
QueueManager.register("get_task_queue")
QueueManager.register("get_result_queue")

#是指master的ip地址
#server_add = "127.0.0.1"
server_add = "192.168.200.210"
print "Connect to server %s..." % server_add

#实例化一个QueueManager对象manager，端口和验证码需要与master保持一致。
m = QueueManager(address=(server_add,5000),authkey="abc")
# 连接master
m.connect()
# 获取Queue对象
task = m.get_task_queue()
result = m.get_result_queue()

for i in range(10):
	try:
		n = task.get(timeout=1)			#获取task数据
		print "run task %d * %d ..." % (n,n)
		r = "%d * %d = %d" % (n,n,n*n)
		time.sleep(1)
		result.put(r)					#将结果存入result queue
	except Queue.Empty:
		print "task queue is empty."
print "worker done."
