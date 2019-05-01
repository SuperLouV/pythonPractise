#5.1先找出所有的导演
import csv
import matplotlib
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import pymysql

df=pd.read_csv(r'D:\pythonPractise\douban_spider_keshe\data_analyze\all_2.csv',encoding='utf-8',names=['编号','名字','导演','编剧','主演一','主演二','主演三','类型','时长','年份','地区','语言','分数'])

pd.set_option('display.max_rows',None)    #把数据全部行展示出来
# pd.set_option('display.width',None)  #把数据全部长度展示出来

def averagenum(num):
    nsum = 0
    for i in range(len(num)):
        nsum += num[i]
    return nsum / len(num)


director_list=df['导演'].tolist()
print(director_list)
print(len(director_list))
director_list=list(set(director_list))
director_list=director_list[1:]
print(director_list)
print(len(director_list))
director_movie_score=[]
for director in director_list:
    print(50 * '%')
    print(director)
    director_Movie_list = df.loc[df['导演'] == director]
    print(director_Movie_list)
    score=director_Movie_list['分数'].tolist()
    print(score)
    print('score长度为：',len(score))
    # while len(score) > 1:
    #     score1=averagenum(score)
    #     director_movie_score.append(averagenum(score))  # 平均分列表
    # else:
    #     score1=score[0]
    #     director_movie_score.append(averagenum(score))  # 平均分列表
    print(averagenum(score))
    director_movie_score.append(averagenum(score))#平均分列表
    print(50 * '%')
print(director_movie_score)
#
director_average_score=dict(zip(director_list,director_movie_score))          #组成导演：分数的字典

print(director_average_score)  #这个是字典

##########################################################开始存入CSV
pd.DataFrame(director_average_score).to_csv('director_average_score.csv')
