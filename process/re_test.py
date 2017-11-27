# -*- coding: utf-8 -*-
import re
test = '用户输入的字符串'
if re.match(r'正则表达式',test):
	print 'ok'
else:
	print 'failed'