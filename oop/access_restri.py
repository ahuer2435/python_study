# -*- coding: utf-8 -*-
class Student(object):
	def __init__(self, name, socre):
		self.__name = name
		self.__socre = socre
		self._socre = socre
		self.__socre__ = socre

	def get_name(self):
		return self.__name

	def get_score(self):
		return self.__socre

	def set_socre(self,score):
		if 0 <= score <=100:
			self.__socre = score
		else:
			raise ValueError('bad socre')

std1 = Student('hank',80)
print 'name = %s, score=%d' % (std1.get_name(),std1.get_score())
std1.set_socre(100)
print 'name = %s, score=%d' % (std1.get_name(),std1.get_score())
print std1._Student__name		#尽量少用，语法没问题，但是与约定不服
print std1._socre 				#
print std1.__socre__
#print std1.__socre
#_xxx：语法没有问题，但是也尽量少用，此种约定是私有变量，不要直接访问。
#__xxx：私有变量，有语法检测，不可直接访问。
#__xxx__：特殊变量，不是作为私有变量，可以直接访问。