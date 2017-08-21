# -*- coding: utf-8 -*-
# test base
a = 3.0/7
if a >= 0:
    print True
else:
    print False

# test string
print '\\\t\\'
print r'\\\t\\' 

# test varible
a = 'ABC'
b = a
a = 'XYZ'
print a
print b

#test encode
print u'中文'.encode('utf-8')

#test format
print  'Hi, %s, you have $%10d.' % ('Michael', 1000000)