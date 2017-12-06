# -*- coding: utf-8 -*-
from Tkinter import *
class Application(Frame):
	def __init__(self,master=None):
		Frame.__init__(self,master)
		self.pack()
		self.createWidget()

	def createWidget(self):
		self.helloLabel = Label(self,text='hello,world!')
		self.helloLabel.pack()
		self.quitButton = Button(self,text='Quit',command=self.quit)
		self.quitButton.pack()

app = Application()
app.master.title('hello world')
app.mainloop()		#执行入口。
#Tkinter封装了访问Tk的接口,Tk是一个图形库，支持多个操作系统，使用Tcl语言开发；
#Tk会调用操作系统提供的本地GUI接口，完成最终的GUI。
#所以，我们的代码只需要调用Tkinter提供的接口就可以了
