# -*- coding: utf-8 -*-
from flask import Flask,request,render_template

app = Flask(__name__)

@app.route('/',methods=['GET','POST'])
def home():
	print "home"
	return render_template('home.html')
	print "home end"

@app.route('/signin',methods=['GET'])
def signin_form():
	return render_template('form.html')

@app.route('/signin',methods=['POST'])
def signin():
	username = request.form['username']
	password = request.form['password']
	if username=='admin' and password=='password':
		return render_template('signin-ok.html',username=username)
	return render_template('form.html',message='Bad username or password',username=username)		#变量message在对应的form.html可以通过{{message}}直接引用。基于模板jinja2

if __name__=='__main__':
	app.run()

#这里的url对应的处理函数相当于mvc中的c，controller，负责业务逻辑，用户名检查，提取用户信息。html文件就是v，view，发给浏览器，用于显示。
#m，也就是模式model，是c传给v的，使得在v替换变量时可以从m中获取。例如变量message，框架会先封装为一个dict：{'message','Bad username or password'}，然后
#v中的{{message}}会自动替换为Bad username or password，变量username也是同样的道理。
#html一定要在templates目录下，这是固定的。这也是的python和html代码的最大限度分类，方便开发
