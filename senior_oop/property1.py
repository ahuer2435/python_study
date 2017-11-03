# -*- coding: utf-8 -*-
class Student(object):
	def get_score(self):
		return self._score

	def set_score(self,score):
		if not isinstance(score,int):
			raise ValueError("score must be integer.")
		if score < 0 or score > 100:
			raise ValueError("score must be in 0~100")
		self._score = score
		
std1 = Student()
std1.set_score(100)
#print std1.get_score()
print std1._score		#这种形式也可以访问，但是通常不会用，或者直接使用私有变量的__xxx。	
