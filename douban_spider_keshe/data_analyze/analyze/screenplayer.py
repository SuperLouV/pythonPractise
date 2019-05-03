
#5.3数据存入数据库screenplayer_score表
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
screenplayer_list=df['编剧'].tolist()
screenplayer_list=list(set(screenplayer_list)) #去重
print(len(screenplayer_list))
screenplayer_list=screenplayer_list[1:]             #全部编剧名字
print(len(screenplayer_list))

#
screenplayer_movie_score = []
screenplayer_movie_number=[]
# 计算平均分
def averagenum(num):
    nsum = 0
    for i in range(len(num)):
        nsum += num[i]
    return nsum / len(num)


for screenplayer in screenplayer_list:
    df = df[df['编剧'].notnull()]
    print(screenplayer)
    screenplayer_movie = df.loc[df['编剧'] == screenplayer]
    # screenplayer_movie = df[df['编剧'].str.contains(screenplayer)]   #只要国家名称中包含‘地区’就算进数量。如‘美国 ’，‘ 美国’均为‘美国’
    print(screenplayer_movie)      #每个国家对应的电影信息
    score=screenplayer_movie['分数'].tolist()
    print(averagenum(score))
    screenplayer_movie_score.append(averagenum(score))#平均分列表
    number=screenplayer_movie.shape[0]
    screenplayer_movie_number.append(number)
    print(score)
    print(number)
print(screenplayer_movie_score)    #电影平均分的列表
print(screenplayer_movie_number) #编剧的电影部数
# screenplayer_average_score=dict(zip(screenplayer_list2,screenplayer_movie_score))          #组成国家：分数的字典

# print(screenplayer_average_score)  #这个是字典

#############################################存入数据库

conn = pymysql.connect("localhost", "root", "root", "doubanmovie")
cursor = conn.cursor()
for i in range(len(screenplayer_list)):
    # sql_insert1 = "insert into screenplayer_score(screenplayer)values(%s)" % (screenplayer_list2[i])
    sql_insert = "insert into screenplayer_score(screenplayer,score,movie_number)values('" + screenplayer_list[i] + "','" + str(screenplayer_movie_score[i]) + "','" + str(screenplayer_movie_number[i]) + "')"
    print(sql_insert)
    try:
        # 执行sql语句
        cursor.execute(sql_insert)
        # 提交到数据库执行
        print('插入')
        conn.commit()
    except:
        continue
        # 发生错误时回滚
        # conn.rollback()

cursor.close()
conn.close()
