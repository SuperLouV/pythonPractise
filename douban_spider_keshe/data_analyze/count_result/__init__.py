import pandas as pd

from sklearn.model_selection import train_test_split #训练数据，划分训练集
from sklearn.linear_model import LinearRegression  #线性回归
from sklearn import metrics
import numpy as np
import matplotlib.pyplot as plt
df=pd.read_csv(r'D:\pythonPractise\douban_spider_keshe\data_analyze\change_CSV\final.csv',encoding='utf-8',names=['导演','编剧','主演一','主演二','主演三','类型','时长','地区','分数'])
pd.set_option('display.max_rows',None)    #把数据全部行展示出来
print(df.head())
print(df.shape)  #数据的维度
np.isnan(df).any()           #判断是否空值
df.dropna(inplace=True)                   #删去空值
print(df.shape)
#现在我们开始准备样本特征X
X = df[['导演','编剧','主演一','主演二','主演三','类型','时长','地区']]
print(X.head())
y=df[['分数']]
print(y.head())
#把X和y的样本组合划分成两部分，一部分是训练集，一部分是测试集
#　　随机数种子控制每次划分训练集和测试集的模式，其取值不变时划分得到的结果一模一样，其值改变时，划分得到的结果不同。
# 若不设置此参数，则函数会自动选择一种随机模式，得到的结果也就不同。
X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=1)#test_size-测试集占总样本比例，如20%表示为0.2，默认0.25
print (X_train.shape)
print (y_train.shape)
print (X_test.shape)
print (y_test.shape)
#可以看到75%的样本数据被作为训练集，25%的样本被作为测试集。
linreg = LinearRegression()
linreg.fit(X_train, y_train)
print (linreg.intercept_)
print (linreg.coef_)
print('y=0.1429074a+0.36510676b+0.36510676c+0.23537985d+0.30375269e+0.10476197f+0.05599598g+-0.11444683h-1.53791708')