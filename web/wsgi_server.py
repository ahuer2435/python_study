# -*- coding: utf-8 -*-
from wsgiref.simple_server import make_server
from wsgi_client import application

httpd = make_server('',8000,application)
print "Serving HTTP on port 8000..."
httpd.serve_forever()
#make_server模块提供web服务器，服务器调用application函数。
#web服务有三个部分组成：接受浏览器http请求，生成html文档，将html文档作为http响应的body发送给浏览器。
#make_server提供“接受浏览器http请求”功能，并调用请求处理函数application。
#application提供后两个功能。