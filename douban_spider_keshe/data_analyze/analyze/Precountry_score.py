#4.28日可以统计特征信息，如国家电影数量
#每个国家的电影数量已经统计完成
import csv
import matplotlib
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd


df=pd.read_csv(r'D:\pythonPractise\douban_spider_keshe\data_analyze\all_2.csv',encoding='utf-8',names=['编号','名字','导演','编剧','主演一','主演二','主演三','类型','时长','年份','地区','语言','分数'])

pd.set_option('display.max_rows',None)    #把数据全部行展示出来
# pd.set_option('display.width',None)  #把数据全部长度展示出来
print(type(df))
country_list=df['地区'].tolist()
print(country_list)
sign = '/'
print(type(sign))

print(type(country_list[0]))
print(country_list[0])
# for i in country_list:
#     print(type(str))
country_list2=[]
for str in country_list:
    try:
        if sign in str:
            location = str.index('/')
            location = location-1
            str = str[0:location]
            print("有",str)
            # location = country_list[i].index('/')
            # country_list[i] = str[0:location]
            country_list2.append(str)
            # i += 1
        else:
            # i += 1
            # country_list2[j].append(country_list[i])
            print("没有/",str)
            country_list2.append(str)
    except:
        continue
country_list2=list(set(country_list2))               #去重
print("全部国家",country_list2)                 #输出全部国家在一个数组里
print(len(country_list2))         #国家数量，但是包含了重复名称

country_movie_score=[]

#计算每个国家平均分
def averagenum(num):
    nsum = 0
    for i in range(len(num)):
        nsum += num[i]
    return nsum / len(num)


for country in country_list2:
    df = df[df['地区'].notnull()]
    print(country)
    df_area = df[df['地区'].str.contains(country)]   #只要国家名称中包含‘地区’就算进数量。如‘美国 ’，‘ 美国’均为‘美国’
    print(df_area)      #每个国家对应的电影信息
    score=df_area['分数'].tolist()
    print(score)
    print(averagenum(score))
    country_movie_score.append(averagenum(score))#平均分列表


country_average_score=dict(zip(country_list2,country_movie_score))          #组成国家：分数的字典
print(country_movie_score)
print(country_average_score)  #这个是字典



