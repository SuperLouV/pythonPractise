import csv
import matplotlib
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import pymysql

df=pd.read_csv(r'D:\pythonPractise\douban_spider_keshe\data_analyze\change_CSV\change_type2.csv',encoding='utf-8',names=['编号','名字','导演','编剧','主演一','主演二','主演三','类型','时长','年份','地区','语言','分数'])
pd.set_option('display.max_rows',None)    #把数据全部行展示出来
df_country=df['地区'].tolist()
sign = '/'

country_list2=[]
for str1 in df_country:
    try:
        if sign in str1:
            location = str1.index('/')
            location = location-1
            str1 = str1[0:location]
            country_list2.append(str1)
        else:
            country_list2.append(str1)
    except:
        continue
print(country_list2)
print(len(country_list2))

df['地区']=country_list2
df.to_csv('change_country1.csv')
