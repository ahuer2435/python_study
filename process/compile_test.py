# -*- coding: utf-8 -*-
import re
str_test = "010-1234567"
re_telephone = re.compile(r'(\d{3})-(\d{3,8})$')
print re_telephone.match(str_test).groups()
print re_telephone.match(str_test).groups(0)
print re_telephone.match(str_test).groups(1)
print re_telephone.match(str_test).groups(2)
#疑惑：为啥单独引用，看到的还是完整的？
#python处理正则表达式分两步：（1）编译正则表达式；
#（2）是使用编译好的正则表达式匹配字符串。
#可以采用先编译，后使用，进而减少编译次数。