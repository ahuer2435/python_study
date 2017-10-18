# -*- coding: utf-8 -*-
import functools
def log(func):
	@functools.wraps(func)
	def wrapper(*args, **kw):
		print 'begin call'
		func(*args, **kw)
		print 'end call'
	return wrapper
@log
def now():
	print '2017-10-18'
now()
print now.__name__

#第二题没有做出来
