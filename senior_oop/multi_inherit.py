# -*- coding: utf-8 -*-
class Animal(object):
	def __init__(self):
		print "Animal."

class Mammal(Animal):		#哺乳类
	def __init__(self):
		print "Mammal."

class Bird(Animal):
	def __init__(self):
		print "Bird."

class RunnableMixin(object):
	def __init__(self):
		print "can run."

class FlyableMixin(object):
	def __init__(self):
		print "can fly."


class Dog(Mammal,RunnableMixin):
	def run(self):
		print "Dog running."

class Bat(Mammal,FlyableMixin):
	def run(self):
		print "Bat running."

#在实例化多重继承对象时，只会调用第一个基类的__init__函数。
#第二个构造函数可视为接口，增加特性的。
class Parrot(Bird,FlyableMixin):				#鹦鹉
	def run(self):
		print "Parrot running."

class Ostrich(Bird,RunnableMixin):			#鸵鸟
	def run(self):
		print "Ostrich running."

pa = Parrot()
pa.run()

#增加Mixin之后，大概表示的就是接口类的意思吧，但是也只是对人来说的约定，不具有实际意义。