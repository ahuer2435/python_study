# -*- coding: utf-8 -*-
import tensorflow as tf
input1 = tf.placeholder(tf.float32)
input2 = tf.placeholder(tf.float32)
output = tf.multiply(input1, input2)
#feed 该机制 可以临时替代图中的任意操作中的 tensor 可以对图中任何操作提交补丁, 直接插入一个 tensor
with tf.Session() as sess:
  print sess.run([output], feed_dict={input1:[7.], input2:[2.]})
