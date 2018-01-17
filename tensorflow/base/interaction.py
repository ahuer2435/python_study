# -*- coding: utf-8 -*-
import tensorflow as tf
sess = tf.InteractiveSession()
x = tf.Variable([1.0,2.0])
a = tf.constant([3.0,3.0])
x.initializer.run()	#初始化变量
sub = tf.subtract(x,a)	#x减a
print sub.eval()
# 使用Tensor.eval() 和 Operation.run() 方法代替 Session.run()