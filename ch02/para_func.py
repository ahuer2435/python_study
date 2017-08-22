# -*- coding: utf-8 -*-
#定义默认参数要牢记一点：默认参数必须指向不变对象

#wrong test
def add_end(L=[]):		#[] 是变量
    L.append('END')
    return L

print add_end()
print add_end()

#right test
def add_end(L=None):	#None 是常亮
    if L is None:
        L = []
    L.append('END')
    return L
print add_end()
print add_end()

#可变参数
def calc(*numbers):
    sum = 0
    for n in numbers:
        sum = sum + n * n
    return sum
print calc()
print calc(1,2)
print calc(1,2,3)
nums=[4,5,6]
print calc(*nums)

#关键字参数
def person(name, age, **kw):
    print 'name:', name, 'age:', age, 'other:', kw
person('Michael', 30)
person('Adas', 45, gender='M', job='Engineer')
kw = {'city': 'Beijing', 'job': 'Engineer'}
person('Jack', 24, **kw)

#组合参数
def func(a, b, c=0, *args, **kw):
    print 'a =', a, 'b =', b, 'c =', c, 'args =', args, 'kw =', kw
func(1, 2)
func(1, 2, c=3)
func(1, 2, 3, 'a', 'b')
func(1, 2, 3, 'a', 'b', x=99)