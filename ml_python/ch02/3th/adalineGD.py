# -*- coding: utf-8 -*-
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

class AdalineGD(object):
  def __init__(self,eta=0.001,n_iter=10):
    self.eta=eta
    self.n_iter = n_iter
    
  def fit(self,X,y):
    #shape = [n_samples,n_features],X.shape[1]应该就是n_features，列数。
    #numpy的shape函数可以提取行列信息。
    #self.w_是一个1乘3的向量。
    self.w_ = np.zeros(1 + X.shape[1])
    #self.errors_ = []
    self.cost_ = []
    
    for _ in range(self.n_iter):
      #output是101行1列的数组，
      output = self.net_input(X)
      print ('output = ')
      print (output)
      #errors是类标与净输入之差
      #在adaline中净输入与激励函数是相同的
      errors = (y - output)
      print ('errors = ')
      print (errors)
      #特征矩阵与误差向量的乘积，以此更新1到m位置的权值。
      self.w_[1:] += self.eta * X.T.dot(errors)
      #self.w_[0]作用是什么？
      self.w_[0] += self.eta * errors.sum()
      #cost是sse，误差平方和，以此作为预测标准
      cost = (errors**2).sum()/2.0
      self.cost_.append(cost)
      print ('cost = ')
      print (cost)
    return self
  
  #返回值是一个101行1列的向量，表示净输入量z，不过这里加上了0号权值。
  def net_input(self,X):
    #dot方法计算向量点积wTx,为什么要加上self.w_[0]？？？
    return np.dot(X,self.w_[1:]) + self.w_[0]
  
  def activation(self,X):
    return self.net_input(X)
  
  def predict(self,X):
    return np.where(self.activation(X) >= 0.0,1,-1)

#读取源数据
#X是101行2列的矩阵
#y是101行1列的类标，只有1和-1两个值。
df = pd.read_csv('https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data',header=None)
#print (df.tail)
y = df.iloc[0:10,4].values
y = np.where(y == 'Iris-setosa',-1,1)
X = df.iloc[0:10,[0,2]].values
#print (y)


#eta=0.01，绘图  
fig, ax = plt.subplots(nrows=1,ncols=2,figsize=(8,4))
adal = AdalineGD(n_iter=10,eta=0.01).fit(X,y)
ax[0].plot(range(1,len(adal.cost_)+1),np.log10(adal.cost_),marker='o')
ax[0].set_xlabel('Epochs')
ax[0].set_ylabel('log(Sum-squared-error)')
ax[0].set_title('Adaline - Learning rate 0.01')

#eta=0.0001，绘图
adal2 = AdalineGD(n_iter=10,eta=0.0001).fit(X,y)
#为啥不带log函数
ax[1].plot(range(1,len(adal2.cost_)+1),adal2.cost_,marker='o')
ax[1].set_xlabel('Epochs')
ax[1].set_ylabel('log(Sum-squared-error)')
ax[1].set_title('Adaline - Learning rate 0.0001')
plt.show()

#adal = AdalineGD(n_iter=10,eta=0.001).fit(X,y)