# -*- coding: utf-8 -*-
class Student(object):
	def __init__(self,name,score):
		self.name = name
		self.score = score

	def print_score(self):
		print 'name = %s, socre = %d' % (self.name,self.score)

	def get_grade(self):
		if self.score >= 90:
			return 'A'
		elif self.score >= 80:
			return 'B'
		else:
			return 'C'

std1 = Student('hank',8)
std1.age = 21						#相比较静态语言，动态语言python允许实例动态绑定任何属性(数据)
std1.print_score()
print 'age = %d' % std1.age
print std1.get_grade()	
#类是抽象的模板，比如Student类，而实例是根据类创建出来的一个个具体的“对象”，每个对象都拥有相同的方法，但各自的数据可能不同。