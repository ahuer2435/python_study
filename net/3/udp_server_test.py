# -*- coding: utf-8 -*-
import socket

s = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
s.bind(("127.0.0.1",9999))
print "bind udp on 9999..."
while True:
	#这里的addr包含ip:portid
	data,addr = s.recvfrom(1024)
	print "received from %s:%s." % addr
	s.sendto("hello,%s!" % data,addr)
	#这里的addr是sendto目标的参数，也就是client的ip:portid,不是前一个字符串的参数。