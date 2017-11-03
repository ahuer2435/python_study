# -*- coding: utf-8 -*-
class Student(object):
	@property				#这是必须要加上的，定义的是读属性
	def score(self):
		return self._score

	@score.setter			#这是必须要加上的，定义的是写属性。
	def score(self,value):
		if not isinstance(value,int):
			raise ValueError("score must be integer.")
		if value < 0 or value > 100:
			raise ValueError("score must be in 0~100")
		self._score = value
		
std1 = Student()
std1.score = 600			#加上之后，std1.score = 600，等价于std1.set_score
print std1.score 			#std1.score，等价于std1.get_score()
# @property是将方法属性化，以方便调用。