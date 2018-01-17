# -*- coding: utf-8 -*-
import tensorflow as tf
state = tf.Variable(0,name="counter")
one = tf.constant(1)
new_value = tf.add(state,one)
update = tf.assign(state,new_value)

init_op = tf.initialize_all_variables()

with tf.Session() as sess:
  sess.run(init_op)
  print sess.run(state)
  
  for _ in range(3):
    #sess.run(update)	#new_value对应的tf.add会重新计算，然后更新state
    print sess.run(update)	#打印state，也可以替换为update，其依赖的东西会自动计算。