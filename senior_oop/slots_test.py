# -*- coding: utf-8 -*-
from types import MethodType
class Student(object):
	pass

def set_age(self,age):
	self.age = age



std = Student()
std.name = "hank"		#属性需以:obj.attr绑定
print std.name

#方法也需以obj.func形式绑定。MethodType方法将方法set_age绑定到对象std，\
#但是并不是说set_age是std的方法，其方法设定还需要以obj.func形式，例如std.set_age_std
#当不设定对象时，方法绑定在类上
std.set_age_std = MethodType(set_age,std,Student)	
std.set_age_std(25)
print std.age 			#方法以self引入的变量，当方法绑定对象后，变量也就成为对象的属性了，变量的绑定是在对象调用方法之后

#std1没有绑定属性，所以其不存在这些属性。
#std1 = Student()			
#print std1.name
#print std1.age

Student.set_age_std = MethodType(set_age,None,Student)	
std1 = Student()
std1.set_age_std(100)
#print std1.name
print std1.age