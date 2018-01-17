# -*- coding: utf-8 -*-
import tensorflow as tf
matrix1 = tf.constant([[3.,3.]])	#1x2的矩阵
matrix2 = tf.constant([[2.],[2.]])	#2x1的矩阵
product = tf.matmul(matrix1,matrix2)	#矩阵相乘
sess = tf.Session()			
result = sess.run(product)
print result
sess.close()
