# -*- coding: utf-8 -*-
import logging
logging.basicConfig(level=logging.INFO)
def foo(s):
	n = int(s)
	logging.info('n = %d' % n)
	return 10/n

def main():
	foo('0')

main()