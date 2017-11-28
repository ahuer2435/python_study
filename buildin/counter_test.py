# -*- coding: utf-8 -*-
from collections import Counter
c = Counter()
for ch in "programming":
	c[ch] = c[ch]+1
print c 
#Counter模块在这里计算字符串中字符出现次数。
#没有看出内部原理。