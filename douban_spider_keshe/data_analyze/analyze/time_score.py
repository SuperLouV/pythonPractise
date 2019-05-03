
#5.3数据存入数据库time_score表
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
time_list=df['时长'].tolist()
time_list=list(set(time_list)) #去重
time_list=time_list[1:]
print(time_list)
print(len(time_list))
print(type(time_list))
# print(min(time_list))  #最小值时长
# print(max(time_list))
#
time_movie_score = []
time_movie_number=[]
sign1=':'
sign2='分钟'
timelong=[]
for timelong1 in time_list:                      #提取时长数字
    location1 = timelong1.index(sign2)
    timelong2 = timelong1[:location1]
    if sign1 in timelong2:
        location2=timelong1.index(sign1)+1
        timelong3 = timelong2[location2:]
    else:
        timelong3 = timelong2
    timelong.append(timelong3)
print(timelong)
# 计算平均分
# def averagenum(num):
#     nsum = 0
#     for i in range(len(num)):
#         nsum += num[i]
#     return nsum / len(num)

#
# for time in time_list:
#     df = df[df['时长'].notnull()]
#     print(time)
#     time_movie = df.loc[df['时长'] == time]
#     # time_movie = df[df['时长'].str.contains(time)]   #只要国家名称中包含‘地区’就算进数量。如‘美国 ’，‘ 美国’均为‘美国’
#     print(time_movie)      #每个国家对应的电影信息
#     score=time_movie['分数'].tolist()
#     print(averagenum(score))
#     time_movie_score.append(averagenum(score))#平均分列表
#     number=time_movie.shape[0]
#     time_movie_number.append(number)
#     print(score)
#     print(number)
# print(time_movie_score)    #电影平均分的列表
# print(time_movie_number) #时长的电影部数


#############################################存入数据库

# conn = pymysql.connect("localhost", "root", "root", "doubanmovie")
# cursor = conn.cursor()
# for i in range(len(time_list)):
#     # sql_insert1 = "insert into time_score(time)values(%s)" % (time_list2[i])
#     sql_insert = "insert into time_score(time,score,movie_number)values('" + str(time_list[i]) + "','" + str(time_movie_score[i]) + "','" + str(time_movie_number[i]) + "')"
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
