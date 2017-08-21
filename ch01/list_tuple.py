p = ['asp', 'php']
s = ['python', 'java', p, 'scheme']
print p
print s

print p[0]
print s[-1]
print s[-2]
print s[2][1]

t = ('a', 'b', ['A', 'B'])
t[2][0] = 'X'
t[2][1] = 'Y'
t[2].insert(1,'C')
print t
