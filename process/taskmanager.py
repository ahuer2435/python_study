# -*- coding: utf-8 -*-
import random,time,Queue
from multiprocessing.managers import BaseManager

#定义发送任务和接受结果队列。
task_queue = Queue.Queue()
result_gueue = Queue.Queue()

#定义一个以BaseManager为基类的类QueueManager
class QueueManager(BaseManager):
	pass

#通过类QueueManager将两个队列注册到网上，注册时需为队列起一个独一无二的名字，
#callable参数指定队列Queue()对象
QueueManager.register("get_task_queue",callable=lambda:task_queue)
QueueManager.register("get_result_queue",callable=lambda:result_gueue)

#实例化一个QueueManager对象manager，绑定本地端口5000，和验证码abc
manager = QueueManager(address=('',5000),authkey="abc")
#启动Queue
manager.start()

#通过网络也就是manager访问Queue对象。
task = manager.get_task_queue()
result = manager.get_result_queue()

for i in range(10):
	n = random.randint(0,100)
	print "Put task %d ..." % n
	task.put(n)		#将任务放入Queue，这里实际是存入一些随机数，正真的处理是在worker中
					#相当于存入待处理的数据。

print "Try get results..."
for i in range(10):
	r = result.get(timeout=10)			#获取worker处理之后的结果数据。
	print "result:%s" % r
manager.shutdown()		#关闭Queue

#python 提供BaseManager模块实现进程间分布式处理，模型是一个master多个worker，
#master分配任务，work具体执行。master作为服务器，worker作为client。