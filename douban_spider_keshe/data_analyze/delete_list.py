#删除之前的空格
import pandas as pd
import numpy as np
df=pd.read_csv(r'D:\pythonPractise\douban_spider_keshe\yinyue_Movie\doubanyinyue1000.csv',encoding='utf-8',header=None,names=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q'])
# columns=["25","1","2","3","4","5","6","7","8","9","10","11","12","13","14","15","16"]
pd.set_option('display.max_rows',None)    #把数据全部行展示出来
# pd.set_option('display.width',None)  #把数据全部长度展示出来
print(type(df))

dp=df.drop('b',inplace=False,axis=1)
dp=dp.drop('d',inplace=False,axis=1)
dp=dp.drop('f',inplace=False,axis=1)
dp=dp.drop('h',inplace=False,axis=1)
dp=dp.drop('j',inplace=False,axis=1)

# print(dp)
# dp.to_csv("yinyue_1.csv")