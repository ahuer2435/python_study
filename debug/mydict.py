# -*- coding: utf-8 -*-
class Dict(dict):
	def __init__(self, **kw):
		super(Dict,self).__init__(**kw)	# 返回的是基类

	def __getattr__(self,key):
		try:
			return self[key]
		except KeyError:
			raise AttributeError(r"'Dict' object has no attribute '%s'" % key)

	def __setattr__(self,key,value):
		self[key] = value

#相当于在基类的基础之上增加了__getattr__和__setattr__对key的修饰。