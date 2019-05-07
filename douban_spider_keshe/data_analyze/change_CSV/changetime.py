import csv
import matplotlib
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import pymysql

df=pd.read_csv(r'D:\pythonPractise\douban_spider_keshe\data_analyze\change_CSV\change_type2.csv',encoding='utf-8',names=['编号','名字','导演','编剧','主演一','主演二','主演三','类型','时长','年份','地区','语言','分数'])
pd.set_option('display.max_rows',None)    #把数据全部行展示出来
df_year=df['年份'].tolist()
print(df_year)
# for year in df_year:
