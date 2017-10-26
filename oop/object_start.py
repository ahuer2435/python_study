# -*- coding: utf-8 -*-
# python中class的定义
class Student(object):
	def __init__(self,name,score):			#class 的__init__函数用于初始化数据，在定义对象的时候自动调用,相当于构造函数，在实例化时参数要对应。
		self.name = name
		self.score = score
		print 'create instance: %s' % self.name

	def print_score(self):			#class 的成员函数至少有一个self参数，才可以引用自己的数据
		print 'name = %s, socre = %d' % (self.name, self.score)

std1 = Student('hank',99)
std1.print_score()

# 面向对象：把计算机程序视为一组对象的集合，而每个对象都可以接收其他对象发过来的消息，
# 并处理这些消息，计算机程序的执行就是一系列消息在各个对象之间传递。
# 给对象发消息实际上就是调用对象对应的关联函数，我们称之为对象的方法（Method）。
# 面向对象程序设计实质是一种消息驱动型设计方式，与其他消息驱动型本质上一致，只是驱动方式上不同，或者不够完美。泪如C++和ROS