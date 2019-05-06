
#5.3数据存入数据库year_score表
import csv
import matplotlib
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import pymysql

df=pd.read_csv(r'D:\pythonPractise\douban_spider_keshe\data_analyze\all_1.csv',encoding='utf-8',names=['编号','名字','导演','编剧','主演一','主演二','主演三','类型','时长','年份','地区','语言','分数'])

pd.set_option('display.max_rows',None)    #把数据全部行展示出来
# pd.set_option('display.width',None)  #把数据全部长度展示出来
print(type(df))
year_list=df['年份'].tolist()
year_list=list(set(year_list)) #去重
year_list=year_list[1:]
print(year_list)
print(len(year_list))
print(min(year_list))  #最小值年份
#
year_movie_score = []
year_movie_number=[]
# 计算平均分
def averagenum(num):
    nsum = 0
    for i in range(len(num)):
        nsum += num[i]
    return nsum / len(num)


for year in year_list:
    df = df[df['年份'].notnull()]
    print(year)
    year_movie = df.loc[df['年份'] == year]
    # year_movie = df[df['年份'].str.contains(year)]   #只要国家名称中包含‘地区’就算进数量。如‘美国 ’，‘ 美国’均为‘美国’
    print(year_movie)      #每个国家对应的电影信息
    score=year_movie['分数'].tolist()
    print(averagenum(score))
    year_movie_score.append(averagenum(score))#平均分列表
    number=year_movie.shape[0]
    year_movie_number.append(number)
    print(score)
    print(number)
print(year_movie_score)    #电影平均分的列表
print(year_movie_number) #年份的电影部数
year_average_score=dict(zip(year_list,year_movie_score))          #组成国家：分数的字典

# print(year_average_score)  #这个是字典

#############################################存入数据库

conn = pymysql.connect("localhost", "root", "root", "doubanmovie")
cursor = conn.cursor()
for i in range(len(year_list)):
    # sql_insert1 = "insert into year_score(year)values(%s)" % (year_list2[i])
    sql_insert = "insert into year_score(year,score,movie_number)values('" + str(year_list[i]) + "','" + str(year_movie_score[i]) + "','" + str(year_movie_number[i]) + "')"
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
