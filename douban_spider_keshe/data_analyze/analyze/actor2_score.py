
#5.3数据存入数据库actor2_score表
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
actor2_list=df['主演二'].tolist()
actor2_list=list(set(actor2_list)) #去重
print(len(actor2_list))
actor2_list=actor2_list[1:]             #全部主演二名字
print(len(actor2_list))

#
actor2_movie_score = []
actor2_movie_number=[]
# 计算平均分
def averagenum(num):
    nsum = 0
    for i in range(len(num)):
        nsum += num[i]
    return nsum / len(num)


for actor2 in actor2_list:
    df = df[df['主演二'].notnull()]
    print(actor2)
    actor2_movie = df.loc[df['主演二'] == actor2]
    # actor2_movie = df[df['主演二'].str.contains(actor2)]   #只要国家名称中包含‘地区’就算进数量。如‘美国 ’，‘ 美国’均为‘美国’
    print(actor2_movie)      #每个国家对应的电影信息
    score=actor2_movie['分数'].tolist()
    print(averagenum(score))
    actor2_movie_score.append(averagenum(score))#平均分列表
    number=actor2_movie.shape[0]
    actor2_movie_number.append(number)
    print(score)
    print(number)
print(actor2_movie_score)    #电影平均分的列表
print(actor2_movie_number) #主演二的电影部数
actor2_average_score=dict(zip(actor2_list,actor2_movie_score))          #组成国家：分数的字典

def change_actor2():
    df1 = pd.read_csv(r'D:\pythonPractise\douban_spider_keshe\data_analyze\change_CSV\change_actor1.csv', encoding='utf-8',
                     names=['编号', '名字', '导演', '编剧', '主演一', '主演二', '主演三', '类型', '时长', '年份', '地区', '语言', '分数'])
    change_actor2=df1['主演二']
    df1['主演二'] = change_actor2.replace(actor2_average_score)
    change_actor2 = df1['主演二']
    print(change_actor2)
    df1.to_csv("D:\pythonPractise\douban_spider_keshe\data_analyze\change_CSV\change_actor2.csv")  # 现存入一个CSV
change_actor2()
# print(actor2_average_score)  #这个是字典

#############################################存入数据库

# conn = pymysql.connect("localhost", "root", "root", "doubanmovie")
# cursor = conn.cursor()
# for i in range(len(actor2_list)):
#     # sql_insert1 = "insert into actor2_score(actor2)values(%s)" % (actor2_list2[i])
#     sql_insert = "insert into actor2_score(actor2,score,movie_number)values('" + actor2_list[i] + "','" + str(actor2_movie_score[i]) + "','" + str(actor2_movie_number[i]) + "')"
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
