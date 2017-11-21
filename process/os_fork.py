# -*- coding: utf-8 -*-
import os
print "Process id %d start..." % os.getpid()
pid = os.fork()
if pid==0:
	print "child process,id:%d, parent process id:%d" % (os.getpid(),os.getppid())
else:
	print "parent process,id:%d" % os.getpid()	
#只能在linux平台使用，os.fork()基于linux的fork()函数。