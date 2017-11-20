# -*- coding: utf-8 -*-
try:
	import cPickle as pickle
except ImportError:
	import pickle

d = dict(name='bob',age=20,score=88)
print pickle.dumps(d)

f=open('dump.txt','wb')
pickle.dump(d,f)
f.close()

g1=open('dump.txt','rb')
g2=pickle.load(g1)
g1.close()
print g2
#Pickle的问题和所有其他编程语言特有的序列化问题一样，就是它只能用于Python，
#并且可能不同版本的Python彼此都不兼容，因此，只能用Pickle保存那些不重要的数据，不能成功地反序列化也没关系。