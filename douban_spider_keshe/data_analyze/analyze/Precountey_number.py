#4.28日可以统计特征信息，如国家电影数量
#每个国家的电影数量已经统计完成,存入MYSQL
#5.3数据存入数据库country_number表
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
country_list=df['地区'].tolist()
print(country_list)
sign = '/'
print(type(sign))

print(type(country_list[0]))
print(country_list[0])

country_list2=[]
for str1 in country_list:
    try:
        if sign in str1:
            location = str1.index('/')
            location = location-1
            str1 = str1[0:location]
            print("有",str1)
            # location = country_list[i].index('/')
            # country_list[i] = str1[0:location]
            country_list2.append(str1)
            # i += 1
        else:
            # i += 1
            # country_list2[j].append(country_list[i])
            print("没有/",str1)
            country_list2.append(str1)
    except:
        continue
country_list2=list(set(country_list2))               #去重
print("全部国家",country_list2)                 #输出全部国家在一个数组里
print(len(country_list2))         #国家数量，但是包含了重复名称
#开始遍历国家，求出每个国家的影片数量
# for country in country_list2:
#     print(50*'%')
#     print(country)
#     a = df.loc[df['地区'] == country]
#     country_score = df['分数'].tolist()
#     # country_score=country_score.mean
#     print(country_score)
#     print(50*'%')
country_movie_number=[]
for country in country_list2:
    df = df[df['地区'].notnull()]
    print(country)
    df_area = df[df['地区'].str.contains(country)]
    print(df_area.shape[0])
    number=df_area.shape[0]
    country_movie_number.append(number)
#     # print(df_area)
print(country_movie_number)
country_number=dict(zip(country_list2,country_movie_number))          #组成国家：数量的字典
# print(country_number)


##########################################
def con_mysql():
    conn = pymysql.connect("localhost", "root", "root", "doubanmovie")
    cursor = conn.cursor()

    for i in range(len(country_list2)):
        sql_insert1 = "insert into country_number(country)values(%s)" % (country_list2[i])
        sql_insert = "insert into country_number(country,number)values('" + country_list2[i] + "','" + str(
            country_movie_number[i]) + "')"
        cursor.execute(sql_insert)
        print(sql_insert)
        print('插入')
        conn.commit()
    cursor.close()
    conn.close()

