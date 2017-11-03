# -*- coding: utf-8 -*-
class Student(object):
	__slots__=("name","age")

std1 = Student()
std1.name = "hank"
std1.age = 25
#std1.score = 99

print std1.name,std1.age #,std1.score

#子类中若无__slots__，则子类绑定对象无限制；若有__slots__，则子类只能绑定父类和子类__slots__的并集。
class GraduateStudent(Student):
#	__slots__=("name","age")
	pass
grd = GraduateStudent()
grd.age = 25
grd.score = 78
print grd.age,grd.score
