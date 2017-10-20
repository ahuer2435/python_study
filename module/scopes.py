#!/usr/bin/env python
# -*- coding: utf-8 -*-

'a scopes test sample'

__author__ = 'ahuer2435'

def _private_1(name):
	return 'hello %s' % name

def _private_2(name):
	return 'hi %s' % name


def greeting(name):
	if len(name) > 3:
		return _private_1(name)
	else:
		return _private_2(name)
# 对于外部调用者，可以隐藏_private_n函数实现。
print greeting('ahuer2435')