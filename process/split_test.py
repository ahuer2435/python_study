# -*- coding: utf-8 -*-
import re
print 'a b   c'.split(' ')
#[]表示任意一项，+表示至少一个
print re.split(r'[\s+\,\:]+','a, b::   c')

