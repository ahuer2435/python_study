# -*- coding: utf-8 -*-
class animal(object):					#类中若无数据，可以没有__init__函数。
	def run(self):
		print "annimal is running."

class cat(animal):
	def run(self):
		print "cat is running."

class dog(animal):
	def run(self):
		print "dog is running."

def twice_run(animal):
	animal.run()
	animal.run()
ani1 = animal()
cat1 = cat()
dog1 = dog()

twice_run(ani1)
twice_run(cat1)
twice_run(dog1)
# 子类属于父类，基于此可实现多态，python的多态实现没有C++那样有特殊的语法要求，直接使用。

print isinstance(ani1,dog)
print isinstance(dog1,animal)
# 在继承关系中，如果一个实例的数据类型是某个子类，那它的数据类型也可以被看做是父类。但是，反过来就不行