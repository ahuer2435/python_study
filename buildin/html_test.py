# -*- coding: utf-8 -*-
from HTMLParser import HTMLParser
from htmlentitydefs import name2codepoint

class MyHTMLParser(HTMLParser):
	def handle_starttag(self,tag,attrs):
		print('<%s>' % tag)

	def handle_endtag(self,tag):
		print('<%s>' % tag)

	def handle_startendtag(self,tag,attrs):
		print('<%s>' % tag)

	def handle_data(self,data):
		print('data:%s' % data)

	def handle_commit(self,data):
		print('<!-- -->')

	def handle_entityref(self,name):
		print('&%s:' % name)

	def handle_charref(self,name):
		print('&#%s' % name)

parser = MyHTMLParser()
parser.feed('<html><head></head><body><p>Some <a href=\"#\">html</a> tutorial...<br>END</p></body></html>')

#通过继承HTMLParser类，重写其中的方法，HTMLParser自动分解html文本，然后将分解之后的数据赋给对应的方法中的参数，方法被调用，可以打印出数据。