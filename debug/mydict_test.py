# -*- coding: utf-8 -*-
import unittest
from mydict import Dict

class TestDict(unittest.TestCase):
	def test_init(self):
		d = Dict(a=1,b='test')
		self.assertEquals(d.a,1)
		self.assertEquals(d.b,'test')
		self.assertTrue(isinstance(d,dict))

	def test_key(self):
		d=Dict()
		d['key'] = 'value'
		self.assertEquals(d.key,'value')

	def test_attr(self):
		d = Dict()
		d.key = 'value'
		self.assertTrue('key' in d)
		self.assertEquals(d['key'],'value')

	def test_keyerror(self):
		d = Dict()
		with self.assertRaises(KeyError):
			value = d['empty']

	def test_attrerror(self):
		d = Dict()
		with self.assertRaises(AttributeError):
			value = d.empty

#目的是练习使用unittest进行单元测试。
#unittest会自动执行以"test"开头的函数。