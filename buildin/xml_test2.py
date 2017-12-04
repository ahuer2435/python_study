# -*- coding: utf-8 -*-
L = []
L.append(r'<?xml version="1.0"?>')
L.append(r'<root>')
L.append(str.encode('some & data'))			#encode需要在str中引用。
L.append(r'</root>')
#return ''.join(L)
#print ''.join(L)
print ''.join(L)		 #不明白这里的意思。
#演示的是生成xml文件，不过这种效率似乎太低了，文中推荐使用json。
