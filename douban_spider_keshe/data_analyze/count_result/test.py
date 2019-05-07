
import numpy as np
from sklearn import datasets,linear_model
from sklearn.model_selection import train_test_split #这里是引用了交叉验证
from sklearn.linear_model import LinearRegression  #线性回归
from sklearn import metrics

# 定义训练数据
x = np.array([[100,4,9.3],[50,3,4.8],[100,4,8.9],
              [100,2,6.5],[50,2,4.2],[80,2,6.2],
              [75,3,7.4],[65,4,6],[90,3,7.6],[90,2,6.1]])
print(x)
X = x[:,:-1]   #x[:,m:n]，即取所有数据集的第m到n-1列数据
Y = x[:,-1]  #x[:,n]表示在全部数组（维）中取第n个数据，直观来说，x[:,n]就是取所有集合的第n个数据,
print(X,Y)

# 训练数据
regr = linear_model.LinearRegression()
regr.fit(X,Y)
print('coefficients(b1,b2...):',regr.coef_)         #回归系数
print('intercept(b0):',regr.intercept_)             #截距

# 预测
x_test = np.array([[102,6],[100,4]])
y_test = regr.predict(x_test)
print(y_test)