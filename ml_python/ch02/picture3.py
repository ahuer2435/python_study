# -*- coding: utf-8 -*-
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.colors import ListedColormap


class Perceptron(object):
  def __init__(self,eta=0.01,n_iter=10):
    self.eta=eta
    self.n_iter = n_iter

  def fit(self,X,y):
    #shape = [n_samples,n_features],X 是一个dataframe，也就是一个100*2的矩阵，X.shape[1]返回列数，X.shape[0]返回行数。
    #numpy的shape函数可以提取行列信息。
    self.w_ = np.zeros(1 + X.shape[1])   #1*3 矩阵
    self.errors_ = []                   #可变数组

    #内层一次循序判断一个样本,内层循环结束变量一次判断样本,这也是外层一次循环,共循环n_iter多次.
    for _ in range(self.n_iter):
      errors = 0
      #X是100*2矩阵，xi是1*2矩阵；y是100*1矩阵，target是一个标量
      for xi,target in zip(X,y):	#按行遍历
        #update也是一个标量
        update = self.eta * (target - self.predict(xi))
        #self.w_[1:]是一个1*2的矩阵.
        self.w_[1:] += update * xi
        #疑惑：self.w_[0]是一个标量， update也是一个标量
        self.w_[0] += update
        errors += int(update != 0.0)	#errors标量累计样本判断次数
      self.errors_.append(errors)	#errors_向量存储每次外层循环之后,该次样本判断的失误率,如果收敛的话,应该是逐渐减小.
    return self

  def net_input(self,X):
    #dot方法计算向量点积wTx,这里的X是实参xi,1*2的矩阵,返回结果是一个标量.这也是扩展之后的wTx
    return np.dot(X,self.w_[1:]) + self.w_[0]

  def predict(self,X):
    #这里的X是实参xi,1*2的矩阵,返回结果是一个标量.
    return np.where(self.net_input(X) >= 0.0,1,-1)

def plot_decision_regions(X,y,classifier,resolution=0.02):
  markers = ('s','x','o','^','v')
  colors = ('red','blue','lightgreen','gray','cyan')
  cmap = ListedColormap(colors[:len(np.unique(y))])

  #获取第一个和第二个特征值的最大值和最小值限定
  x1_min,x1_max = X[:, 0].min() - 1, X[:, 0].max() + 1
  x2_min,x2_max = X[:, 1].min() - 1, X[:, 1].max() + 1
  xx1,xx2 = np.meshgrid(np.arange(x1_min,x1_max,resolution),np.arange(x2_min,x2_max,resolution))
  Z = classifier.predict(np.array([xx1.ravel(),xx2.ravel()]).T)
  Z = Z.reshape(xx1.shape)
  plt.contourf(xx1,xx2,Z,alpha=0.4,cmap=cmap)
  plt.xlim(xx1.min(),xx1.max())
  plt.ylim(xx2.min(),xx2.max())

  for idx,cl in enumerate(np.unique(y)):
    plt.scatter(x=X[y == cl,0], y=X[y == cl,1],alpha=0.8,c=cmap(idx),marker=markers[idx],label=cl)


#使用pandas从UCI机器学习库中读取鸢（yuan）尾花数据集
#并转换为DataFrame对象加载到内存，使用tail()方法显示。
df = pd.read_csv('https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data',header=None)
print (df.tail())
#读取前100个类标[0,100) ，第四个数据的值，y是一个100*1的列向量，元素为字符串。
y = df.iloc[0:100,4].values
#转化类标，1代表变色鸢尾，-1代表山鸢尾，y是一个100*1行的列向量，元素是-1或者1。
y = np.where(y == 'Iris-setosa',-1,1)
#读取前100个样本的第1个和第3个数据的值
#X由100*2的矩阵
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

plot_decision_regions(X,y,classifier=ppn)
plt.xlabel('sepal length [cm]')
plt.ylabel('petal length [cm]')
plt.legend(loc='upper left')
plt.show()
