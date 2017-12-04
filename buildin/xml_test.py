# -*- coding: utf-8 -*-
from xml.parsers.expat import ParserCreate

class DefaultSaxHandler(object):
	def start_element(self,name,attrs):
		print("sax:start_element: %s, attrs:%s" % (name,str(attrs)))

	def end_element(self,name):
		print("sax:end_element:%s" % name)

	def char_daa(self,text):
		print("sax:char_data: %s" % text)

xml=r'''<?xml version="1.0"?>
<ol>
	<li><a href = "/python">Python</a></li>
	<li><a href = "/ruby">Rudy</a></li>
</ol>
'''

handler = DefaultSaxHandler()
parser = ParserCreate()
parser.returns_unicode = True
parser.StartElementHandler = handler.start_element
parser.EndElementHandler = handler.end_element
parser.CharacterDataHandler = handler.char_daa
parser.Parse(xml)
#ParserCreate类提供自动分解xml文件内容，分解之后的传入handler中的各个函数，用以调用。