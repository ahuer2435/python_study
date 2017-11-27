# -*- coding: utf-8 -*-
import re
str_test = '102300'
m = re.match(r'^(\d+)(0*)',str_test)
print m.groups(0)
print m.groups(1)
print m.groups(2)

m = re.match(r'^(\d+?)(0*)',str_test)
print m.groups(0)
print m.groups(1)
print m.groups(2)
#()括号代表分组，若正则表达式包含()，则可以使用groups()方法，提取分组后的结果。
#r'' 一般用于存放正则表达式。
#python正则表达式一般是贪婪策略，加入？采用非贪婪策略。