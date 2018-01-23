# -*- coding: utf-8 -*-
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
class Perceptron(object):
  def __init__(self,eta=0.01,n_iter=10):
    self.eta=eta
    self.n_iter = n_iter
    
  def fit(self,X,y):
    #shape = [n_samples,n_features],X.shape[1]应该就是n_features，列数。
    #numpy的shape函数可以提取行列信息。
    self.w_ = np.zeros(1 + X.shape[1])
    self.errors_ = []
    
    for _ in range(self.n_iter):
      errors = 0
      #X是101行，2列矩阵，xi是1行2列向量；y是101行列向量，target是一个标量
      for xi,target in zip(X,y):
        #update也是一个标量	
        update = self.eta * (target - self.predict(xi))
        self.w_[1:] += update * xi
        #疑惑：self.w_[0]是一个标量，update是一个向量，如何相加呢？？？ update是一个标量
        self.w_[0] += update
        errors += int(update != 0.0)
      self.errors_.append(errors)
    return self
  
  def net_input(self,X):
    #dot方法计算向量点积wTx
    return np.dot(X,self.w_[1:]) + self.w_[0]
  
  def predict(self,X):
    return np.where(self.net_input(X) >= 0.0,1,-1)

#使用pandas从UCI机器学习库中读取鸢（yuan）尾花数据集
#并转换为DataFrame对象加载到内存，使用tail方法显示。
df = pd.read_csv('https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data',header=None)
print (df.tail)
#读取前100个类标，第四个数据的值
y = df.iloc[0:100,4].values
#转化类标，1代表变色鸢尾，-1代表山鸢尾，y是一个101行的列向量。
y = np.where(y == 'Iris-setosa',-1,1)
#读取前100个类标，第1个和第三个数据的值
#X由101行，2列的矩阵
X = df.iloc[0:100,[0,2]].values
    
ppn = Perceptron(eta=0.1,n_iter=10)
#利用鸢尾花数据集训练感知器
ppn.fit(X,y)
#画出每次迭代错误分类数量的曲线，已检验算法是否收敛，并找到可以分开两种鸢尾花的决策边界。
#x轴代表迭代次数，y轴代表误匹配数。
plt.plot(range(1,len(ppn.errors_)+1),ppn.errors_,marker='o')
plt.xlabel('Epochs')
plt.ylabel('Number of misclassifications')
plt.show()