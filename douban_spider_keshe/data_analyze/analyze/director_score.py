#4.28日可以统计特征信息，如国家电影数量
#每个国家的电影数量已经统计完成
#5.3数据存入数据库director_score表
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
director_list=df['导演'].tolist()
director_list=list(set(director_list)) #去重
print(len(director_list))
director_list=director_list[1:]             #全部导演名字
print(len(director_list))

#
director_movie_score = []
director_movie_number=[]
# 计算平均分
def averagenum(num):
    nsum = 0
    for i in range(len(num)):
        nsum += num[i]
    return nsum / len(num)


for director in director_list:
    df = df[df['导演'].notnull()]
    print(director)
    director_movie = df.loc[df['导演'] == director]
    # director_movie = df[df['导演'].str.contains(director)]   #只要国家名称中包含‘地区’就算进数量。如‘美国 ’，‘ 美国’均为‘美国’
    print(director_movie)      #每个国家对应的电影信息
    score=director_movie['分数'].tolist()
    print(averagenum(score))
    director_movie_score.append(averagenum(score))#平均分列表
    number=director_movie.shape[0]
    director_movie_number.append(number)
    print(score)
    print(number)
print(director_movie_score)    #电影平均分的列表
print(director_movie_number) #导演的电影部数
# director_average_score=dict(zip(director_list2,director_movie_score))          #组成国家：分数的字典

# print(director_average_score)  #这个是字典

#############################################存入数据库

conn = pymysql.connect("localhost", "root", "root", "doubanmovie")
cursor = conn.cursor()
for i in range(len(director_list)):
    # sql_insert1 = "insert into director_score(director)values(%s)" % (director_list2[i])
    sql_insert = "insert into director_score(director,score)values('" + director_list[i] + "','" + str(director_movie_score[i]) + "')"
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
