
#5.3数据存入数据库time_score表
import csv
import matplotlib
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import pymysql


# 计算平均分
def averagenum(num):
    nsum = 0
    for i in range(len(num)):
        nsum += num[i]
    return nsum / len(num)


df=pd.read_csv(r'D:\pythonPractise\douban_spider_keshe\data_analyze\analyze\change_time.csv',encoding='utf-8',names=['编号','名字','导演','编剧','主演一','主演二','主演三','类型','时长','年份','地区','语言','分数'])

pd.set_option('display.max_rows',None)    #把数据全部行展示出来
# pd.set_option('display.width',None)  #把数据全部长度展示出来
print(type(df))
time_list=df['时长']
# time_list=df['时长'].astype('int')
# time_list=list(set(time_list)) #去重
time_list=time_list[1:]
print(time_list)
print(len(time_list))

# print(min(time_list))  #最小值时长
time_movie_score=[]
time_movie_number=[]
time_divided=['thrity','sixty','ninty','OneHTwenty','OneHFifty','OneHEight','MoreOHE']
thrity=df.loc[df['时长']<=30]
# print(thrity)
thrity_time=thrity['分数'].tolist()
# print(thrity_time)
score30=averagenum(thrity_time)                  #30分钟内的均分
print(averagenum(thrity_time))
len30=len(thrity_time)                        #30分钟内的电影数量
print('30一共有:',len30)
time_movie_score.append(score30)
time_movie_number.append(len30)
#########################################
sixty=df.loc[(df['时长']<=60)&(df['时长']>30)]
# print(sixty)
sixty_time=sixty['分数'].tolist()
# print(sixty_time)
score60=averagenum(sixty_time)                  #30-60分钟内的均分
print(averagenum(sixty_time))
len60=len(sixty_time)                        #30-60分钟内的电影数量
print('60一共有:',len60)
time_movie_score.append(score60)
time_movie_number.append(len60)
#########################################
ninty=df.loc[(df['时长']<=90)&(df['时长']>60)]
# print(ninty)
ninty_time=ninty['分数'].tolist()
# print(ninty_time)
score90=averagenum(ninty_time)                  #60-90分钟内的均分
print(averagenum(ninty_time))
len90=len(ninty_time)                        #60-90分钟内的电影数量
print('90一共有:',len90)
time_movie_score.append(score90)
time_movie_number.append(len90)
#########################################
OneHTwenty=df.loc[(df['时长']<=120)&(df['时长']>90)]
# print(OneHTwenty)
OneHTwenty_time=OneHTwenty['分数'].tolist()
# print(OneHTwenty_time)
score120=averagenum(OneHTwenty_time)                  #90-120分钟内的均分
print(averagenum(OneHTwenty_time))
len120=len(OneHTwenty_time)                        #90-120分钟内的电影数量
print('120一共有:',len120)
time_movie_score.append(score120)
time_movie_number.append(len120)
#########################################
OneHFifty=df.loc[(df['时长']<=150)&(df['时长']>120)]
# print(OneHFifty)
OneHFifty_time=OneHFifty['分数'].tolist()
# print(OneHFifty_time)
score150=averagenum(OneHFifty_time)                  #120-150分钟内的均分
print(averagenum(OneHFifty_time))
len150=len(OneHFifty_time)                        #120-150分钟内的电影数量
print('150一共有:',len150)
time_movie_score.append(score150)
time_movie_number.append(len150)
#########################################
OneHEight=df.loc[(df['时长']<=180)&(df['时长']>150)]
# print(OneHEight)
OneHEight_time=OneHEight['分数'].tolist()
# print(OneHEight_time)
score180=averagenum(OneHEight_time)                  #150-180分钟内的均分
print(averagenum(OneHEight_time))
len180=len(OneHEight_time)                        #150-180分钟内的电影数量
print('180一共有:',len180)
time_movie_score.append(score180)
time_movie_number.append(len180)
#########################################
MoreOHE=df.loc[df['时长']>180]
# print(MoreOHE)
MoreOHE_time=MoreOHE['分数'].tolist()
# print(MoreOHE_time)
scoreM180=averagenum(MoreOHE_time)                  #大于80分钟的均分
print(averagenum(MoreOHE_time))
lenM180=len(MoreOHE_time)                        #大于180分钟的电影数量
print('180一共有:',lenM180)
time_movie_score.append(scoreM180)
time_movie_number.append(lenM180)

print(time_movie_number)
print(time_movie_score)

print(type(time_movie_score[2]))
print(type(time_movie_number[2]))

# time_average_score=dict(zip(time_list2,time_movie_score))          #组成国家：分数的字典

# print(time_average_score)  #这个是字典
