# -*- coding: utf-8 -*-
class Student(object):
	def __init__(self,name):
		self.name = name
	def __str__(self):
		return "Student object (name : %s)" % self.name

std = Student("hank")
print std
#特殊函数__str__()返回打印对象的结果。


class Fin(object):
	def __init__(self):
		self.a, self.b = 0, 1

	def __iter__(self):
		return self

	def next(self):
		self.a, self.b = self.b, self.a+self.b
		if self.a > 1000:
			raise StopIteration()
		return self.a

fi = Fin()
for i in fi:
	print i
#特殊函数__iter__将类序列化，使之可以适用于for循环，每次调用i即是调用next()函数，
#此形式遇到StopIteration()结束调用。


class Fin(object):
	def __getitem__(self,n):
		if isinstance(n,int):
			a,b = 1,1
			for x in range(n):
				a,b = b, a+b
			return a
		if isinstance(n,slice):
			start = n.start
			stop = n.stop
			a,b = 1,1
			L = []
			for x in range(stop):
				if x >= start:
					L.append(a)
				a,b = b,a+b
			return L

fi2 = Fin()
print "in __getitem__"
print fi2[3]
print fi2[0:5]
#特殊函数__getitem__修饰的类，可以适用于下表运算和切片技术。近似于list结构；通过此函数可以将类
#封装为满足list，dict等数据类型的运算。

class Student(object):
	def __init__(self,name):
		self.name = name

#	def __getattr__(self,attr):
#		if attr == "score":
#			return 99
	def __getattr__(self, attr):
		if attr=='age':
			return lambda: 25
		raise AttributeError('\'Student\' object has no attribute \'%s\'' % attr)		#感觉没有多大意义，因为与系统默认提供的错误提示一致。

std2 = Student("hunk")
print "in __getattr__"
print std2.name
#print std2.score()
print std2.age()

class Chain(object):
    def __init__(self, path=''):
        self._path = path

    def __getattr__(self, path):
        return Chain('%s/%s' % (self._path, path))

    def __str__(self):
        return self._path
print "in __getattr__2"
ch1 = Chain()
print ch1.status.user.timeline.list
#不明白这里要表达的意思是什么？


class Student(object):
    def __init__(self, name):
        self.name = name

    def __call__(self):
        print('My name is %s.' % self.name)
print "in __call__"
s = Student("tiger")
print s()
print callable([1, 2, 3])
print callable(Student("tiger"))
#特殊函数__call__可以将对象函数化，以函数形式调用对象。
#对实例进行直接调用就好比对一个函数进行调用一样，所以你完全可以把对象看成函数，把函数看成对象，因为这两者之间本来就没啥根本的区别。
#如果你把对象看成函数，那么函数本身其实也可以在运行期动态创建出来，因为类的实例都是运行期创建出来的，这么一来，我们就模糊了对象和函数的界限。
#那么，怎么判断一个变量是对象还是函数呢？其实，更多的时候，我们需要判断一个对象是否能被调用，能被调用的对象就是一个Callable对象