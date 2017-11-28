# -*- coding: utf-8 -*-
from collections import OrderedDict
d=dict([('a',1),('b',2),('c',3)])
print d

od=OrderedDict([('a',1),('d',20),('c',3)])
print od
#OrderedDict模块可以按照插入顺序对dict元素排序，可以基于此实现一个FIFO。