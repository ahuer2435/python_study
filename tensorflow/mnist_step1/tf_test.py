# -*- coding: utf-8 -*-
import input_data
import tensorflow as tf
#mnist是一个轻量级的类。它以Numpy数组的形式存储着训练、校验和测试数据集
mnist = input_data.read_data_sets("MNIST_data/", one_hot=True)
#x代表无限张图片，每个图片是一个784维向量的张量，其值代表每个像素是对应标签数字的概率。作为输入。
x = tf.placeholder("float", [None, 784])
#表示变量，初始值全为零的权值和偏置量。作为输入。
W = tf.Variable(tf.zeros([784,10]))
b = tf.Variable(tf.zeros([10]))
#tf.matmul(x,W)代表x乘W。结果[None,10],表示每个图片是某个数字的权值。+b之后，意义不变。
#y是一个十维向量，把权值权值换算为概率，也是[None，10]代表每个图片是某个数字的概率。作为预测输出。
y = tf.nn.softmax(tf.matmul(x,W) + b)
#y_占位符，代表每个图片是什么数字。
y_ = tf.placeholder("float", [None,10])
#cross_entropy衡量预测的有效性，是一个值，标量
cross_entropy = -tf.reduce_sum(y_*tf.log(y))
#使用梯度下降法优化cross_entropy，至此构建结束。
train_step = tf.train.GradientDescentOptimizer(0.01).minimize(cross_entropy)
#初始化所有变量
init = tf.initialize_all_variables()
#构建一个sess，在sess中运行初始化变量。
sess = tf.Session()
sess.run(init)
#开始训练模型，训练一千次，每次随机挑选100个样本
for i in range(1000):
  #batch_xs表示训练images，batch_ys表示训练label
  batch_xs, batch_ys = mnist.train.next_batch(100)
  #train_step表示训练方法
  sess.run(train_step, feed_dict={x: batch_xs, y_: batch_ys})
#比较训练结果y与标签y_
correct_prediction = tf.equal(tf.argmax(y,1), tf.argmax(y_,1))
#计算训练精度
accuracy = tf.reduce_mean(tf.cast(correct_prediction, "float"))
#利用训练结果，计算测试集的正确率，应该是同一个sess
print accuracy
print sess.run(accuracy, feed_dict={x: mnist.test.images, y_: mnist.test.labels})

#每个像素都有一个正负的权值，表示是某个label的概率。进而计算整个图片关于label的概率