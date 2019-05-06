
#5.3数据存入数据库actor3_score表
import csv
import matplotlib
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import pymysql
def averagenum(num):
    nsum = 0
    for i in range(len(num)):
        nsum += num[i]
    return nsum / len(num)

#################################aiqing
df_aiqing=pd.read_csv(r'D:\pythonPractise\douban_spider_keshe\aiqing_Movie\doubanaiqing1000.csv',encoding='utf-8',names=['编号','名字','导演','编剧','主演一','主演二','主演三','类型','时长','年份','地区','语言','分数'])
pd.set_option('display.max_rows',None)    #把数据全部行展示出来
# pd.set_option('display.width',None)  #把数据全部长度展示出来
print(df_aiqing.columns)
aiqing_score=df_aiqing['分数'].tolist()
aiqing_average_score=averagenum(aiqing_score)
print('爱情片平均分：',aiqing_average_score)
#################################donghua
df_donghua=pd.read_csv(r'D:\pythonPractise\douban_spider_keshe\donghua_Movie\doubandonghua1000.csv',encoding='utf-8',names=['编号','名字','导演','编剧','主演一','主演二','主演三','类型','时长','年份','地区','语言','分数'])
pd.set_option('display.max_rows',None)    #把数据全部行展示出来
# pd.set_option('display.width',None)  #把数据全部长度展示出来
donghua_score=df_donghua['分数'].tolist()
donghua_average_score=averagenum(donghua_score)
print('动画片平均分：',donghua_average_score)
#################################donghua
df_dongzuo=pd.read_csv(r'D:\pythonPractise\douban_spider_keshe\dongzuo_Movie\doubandongzuo1000.csv',encoding='utf-8',names=['编号','名字','导演','编剧','主演一','主演二','主演三','类型','时长','年份','地区','语言','分数'])
pd.set_option('display.max_rows',None)    #把数据全部行展示出来
# pd.set_option('display.width',None)  #把数据全部长度展示出来
dongzuo_score=df_dongzuo['分数'].tolist()
dongzuo_average_score=averagenum(dongzuo_score)
print('动作片平均分：',dongzuo_average_score)
#################################juqing
df_juqing=pd.read_csv(r'D:\pythonPractise\douban_spider_keshe\juqing_Movie\doubanjuqing.csv',encoding='utf-8',names=['编号','名字','导演','编剧','主演一','主演二','主演三','类型','时长','年份','地区','语言','分数'])
pd.set_option('display.max_rows',None)    #把数据全部行展示出来
# pd.set_option('display.width',None)  #把数据全部长度展示出来
juqing_score=df_juqing['分数'].tolist()
juqing_average_score=averagenum(juqing_score)
print('剧情片平均分：',juqing_average_score)
#################################kehuan
df_kehuan=pd.read_csv(r'D:\pythonPractise\douban_spider_keshe\kehuan_Movie\doubankehuan1000.csv',encoding='utf-8',names=['编号','名字','导演','编剧','主演一','主演二','主演三','类型','时长','年份','地区','语言','分数'])
pd.set_option('display.max_rows',None)    #把数据全部行展示出来
# pd.set_option('display.width',None)  #把数据全部长度展示出来
kehuan_score=df_kehuan['分数'].tolist()
kehuan_average_score=averagenum(kehuan_score)
print('科幻片平均分：',kehuan_average_score)
#################################xiju
df_xiju=pd.read_csv(r'D:\pythonPractise\douban_spider_keshe\xiju_Movie\doubanxiju1000.csv',encoding='utf-8',names=['编号','名字','导演','编剧','主演一','主演二','主演三','类型','时长','年份','地区','语言','分数'])
pd.set_option('display.max_rows',None)    #把数据全部行展示出来
# pd.set_option('display.width',None)  #把数据全部长度展示出来
xiju_score=df_xiju['分数'].tolist()
xiju_average_score=averagenum(xiju_score)
print('喜剧片平均分：',xiju_average_score)
#################################xiju
df_xiju=pd.read_csv(r'D:\pythonPractise\douban_spider_keshe\xiju_Movie\doubanxiju1000.csv',encoding='utf-8',names=['编号','名字','导演','编剧','主演一','主演二','主演三','类型','时长','年份','地区','语言','分数'])
pd.set_option('display.max_rows',None)    #把数据全部行展示出来
# pd.set_option('display.width',None)  #把数据全部长度展示出来
xiju_score=df_xiju['分数'].tolist()
xiju_average_score=averagenum(xiju_score)
print('喜剧片平均分：',xiju_average_score)
# print(type(df))
# actor3_list=df['主演三'].tolist()
# actor3_list=list(set(actor3_list)) #去重
# print(len(actor3_list))
# actor3_list=actor3_list[1:]             #全部主演三名字
# print(len(actor3_list))
#
# #
# actor3_movie_score = []
# actor3_movie_number=[]
# 计算平均分

