
#5.3数据存入数据库actor1_score表
import csv
import matplotlib
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import pymysql

df=pd.read_csv(r'D:\pythonPractise\douban_spider_keshe\data_analyze\all_2.csv',encoding='utf-8',names=['编号','名字','导演','编剧','主演一','主演二','主演三','类型','时长','年份','地区','语言','分数'])

pd.set_option('display.max_rows',None)    #把数据全部行展示出来
# pd.set_option('display.width',None)  #把数据全部长度展示出来
print(type(df))
actor1_list=df['主演一'].tolist()
actor1_list=list(set(actor1_list)) #去重
print(len(actor1_list))
actor1_list=actor1_list[1:]             #全部主演一名字
print(len(actor1_list))

#
actor1_movie_score = []
actor1_movie_number=[]
# 计算平均分
def averagenum(num):
    nsum = 0
    for i in range(len(num)):
        nsum += num[i]
    return nsum / len(num)


for actor1 in actor1_list:
    df = df[df['主演一'].notnull()]
    print(actor1)
    actor1_movie = df.loc[df['主演一'] == actor1]
    # actor1_movie = df[df['主演一'].str.contains(actor1)]   #只要国家名称中包含‘地区’就算进数量。如‘美国 ’，‘ 美国’均为‘美国’
    print(actor1_movie)      #每个国家对应的电影信息
    score=actor1_movie['分数'].tolist()
    print(averagenum(score))
    actor1_movie_score.append(averagenum(score))#平均分列表
    number=actor1_movie.shape[0]
    actor1_movie_number.append(number)
    print(score)
    print(number)
print(actor1_movie_score)    #电影平均分的列表
print(actor1_movie_number) #主演一的电影部数
actor1_average_score=dict(zip(actor1_list,actor1_movie_score))          #组成国家：分数的字典


def change_actor1():
    df1 = pd.read_csv(r'D:\pythonPractise\douban_spider_keshe\data_analyze\change_CSV\change_screenplayer.csv', encoding='utf-8',
                     names=['编号', '名字', '导演', '编剧', '主演一', '主演二', '主演三', '类型', '时长', '年份', '地区', '语言', '分数'])
    change_actor1=df1['主演一']
    df1['主演一'] = change_actor1.replace(actor1_average_score)
    change_actor1 = df1['主演一']
    print(change_actor1)
    df1.to_csv("D:\pythonPractise\douban_spider_keshe\data_analyze\change_CSV\change_actor1.csv")  # 现存入一个CSV
change_actor1()
# print(actor1_average_score)  #这个是字典

#############################################存入数据库

# conn = pymysql.connect("localhost", "root", "root", "doubanmovie")
# cursor = conn.cursor()
# for i in range(len(actor1_list)):
#     # sql_insert1 = "insert into actor1_score(actor1)values(%s)" % (actor1_list2[i])
#     sql_insert = "insert into actor1_score(actor1,score,movie_number)values('" + actor1_list[i] + "','" + str(actor1_movie_score[i]) + "','" + str(actor1_movie_number[i]) + "')"
#     print(sql_insert)
#     try:
#         # 执行sql语句
#         cursor.execute(sql_insert)
#         # 提交到数据库执行
#         print('插入')
#         conn.commit()
#     except:
#         continue
#         # 发生错误时回滚
#         # conn.rollback()
#
# cursor.close()
# conn.close()
