# -*- coding: utf-8 -*-
#test for
sum = 0
for x in range(101):
    sum = sum + x
print "sum = %d" % sum

#test while
sum = 0
n = 99
while n > 0:
    sum = sum + n
    n = n - 2
print "sum = %d" % sum

#test raw_input
birth = int(raw_input('birth: '))
if birth < 2000:
    print '00前'
else:
    print '00后'