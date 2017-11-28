# -*- coding: utf-8 -*-
from collections import namedtuple
Point = namedtuple('point',['x','y'])
p = Point(1,2)
print p.x
print p.y

print isinstance(p,Point)
print isinstance(p,tuple)
#collections集合提供namedtuple模块，可以以属性的形式引用tuple元素。
#namedtuple继承与tuple。