# -*- coding: utf-8 -*-
from flask import Flask
from flask import request

app = Flask(__name__) #什么作用？app可能指向Flask的一个实例

@app.route('/',methods=['GET','POST'])	#在这里解析浏览器的url请求，参数是url中的路径和方法，以下函数是对应的处理函数。
def home():
	return '<h1>home</h1>'

@app.route('/signin',methods=['GET'])	#利用到装饰器功能。装饰器集中处理一些共性问题，是的下面定义的函数主要对应参数的处理函数就可以了，进一步封装。
def signin_form():
	return '''<form action="/signin" method="post">
			<p><input name="username"></p>
			<p><input name="password" type="password"></p>
			<p><button type="submit">Sign In</button></p>
			</form> '''

@app.route("/signin",methods=['POST'])
def signin():
	if request.form['username']=='admin' and request.form['password']=='password':
		return '<h3>Hello,admin</h3>'
	return '<h3>Bad usernamne or password</h3>'

if __name__=='__main__':
	print "a"
	app.run()
	print "b"
