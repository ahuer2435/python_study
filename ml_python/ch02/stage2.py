# -*- coding: utf-8 -*-
import numpy as np
import pandas as pd
import numpy as np
class Perceptron(object):
  def __init__(self,eta=0.01,n_iter=10):
    self.eta=eta
    self.n_iter = n_iter

  def fit(self,X,y):
    #shape = [n_samples,n_features],X.shape[1]应该就是n_features，列数。
    print (X.shape[0])
    print (X.shape[1])
    self.w_ = np.zeros(1 + X.shape[1])
    self.errors_ = []

    print (self.w_)
    print (self.errors_)

    for _ in range(self.n_iter):
      errors = 0
      for xi,target in zip(X,y):
        update = self.eta * (target - self.predict(xi))
        self.w_[1:] += update * xi
        #疑惑：self.w_[0]是一个标量，update是一个向量，如何相加呢？？？
        self.w_[0] += update
        #print (self.w_)
        errors += int(update != 0.0)
      self.errors_.append(errors)
      print (self.errors_)
      print (xi)
      print (target)
    return self

  def net_input(self,X):
    #dot方法计算向量点积wTx
    return np.dot(X,self.w_[1:]) + self.w_[0]

  def predict(self,X):
    return np.where(self.net_input(X) >= 0.0,1,-1)

df = pd.read_csv('https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data',header=None)
print (df.tail())
y = df.iloc[0:75,4].values
y = np.where(y == 'Iris-setosa',-1,1)
#print (y)
X = df.iloc[0:75,[0,2]].values
#print (X)

ppn = Perceptron(eta=0.1,n_iter=10)
#利用鸢尾花数据集训练感知器
ppn.fit(X,y)
