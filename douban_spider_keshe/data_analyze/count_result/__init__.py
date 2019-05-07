
import csv
import matplotlib
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import pymysql
# 绘制散点图
df=pd.read_csv(r'D:\pythonPractise\douban_spider_keshe\data_analyze\change_CSV\final.csv',encoding='utf-8',names=['导演','编剧','主演一','主演二','主演三','类型','时长','地区','分数'])
pd.set_option('display.max_rows',None)    #把数据全部行展示出来
plt.scatter(df.分数, df.导演, color='b', label="Exam Data")

# 添加图的标签（x轴，y轴）
plt.xlabel("director")
plt.ylabel("Score")
# 显示图像
plt.show()