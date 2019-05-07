
#5.3数据存入数据库actor3_score表
import csv
import matplotlib
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import pymysql
def averagenum(num):
    nsum = 0
    for i in range(len(num)):
        nsum += num[i]
    return nsum / len(num)

#################################aiqing
df_aiqing=pd.read_csv(r'D:\pythonPractise\douban_spider_keshe\aiqing_Movie\doubanaiqing1000.csv',encoding='utf-8',names=['编号','名字','导演','编剧','主演一','主演二','主演三','类型','时长','年份','地区','语言','分数'])
pd.set_option('display.max_rows',None)    #把数据全部行展示出来
# pd.set_option('display.width',None)  #把数据全部长度展示出来
print(df_aiqing.columns)
aiqing_score=df_aiqing['分数'].tolist()
aiqing_average_score=averagenum(aiqing_score)
print('爱情片平均分：',aiqing_average_score)
#################################donghua
df_donghua=pd.read_csv(r'D:\pythonPractise\douban_spider_keshe\donghua_Movie\doubandonghua1000.csv',encoding='utf-8',names=['编号','名字','导演','编剧','主演一','主演二','主演三','类型','时长','年份','地区','语言','分数'])
pd.set_option('display.max_rows',None)    #把数据全部行展示出来
# pd.set_option('display.width',None)  #把数据全部长度展示出来
donghua_score=df_donghua['分数'].tolist()
donghua_average_score=averagenum(donghua_score)
print('动画片平均分：',donghua_average_score)
#################################donghua
df_dongzuo=pd.read_csv(r'D:\pythonPractise\douban_spider_keshe\dongzuo_Movie\doubandongzuo1000.csv',encoding='utf-8',names=['编号','名字','导演','编剧','主演一','主演二','主演三','类型','时长','年份','地区','语言','分数'])
pd.set_option('display.max_rows',None)    #把数据全部行展示出来
# pd.set_option('display.width',None)  #把数据全部长度展示出来
dongzuo_score=df_dongzuo['分数'].tolist()
dongzuo_average_score=averagenum(dongzuo_score)
print('动作片平均分：',dongzuo_average_score)
#################################juqing
df_juqing=pd.read_csv(r'D:\pythonPractise\douban_spider_keshe\juqing_Movie\doubanjuqing1000.csv',encoding='utf-8',names=['编号','名字','导演','编剧','主演一','主演二','主演三','类型','时长','年份','地区','语言','分数'])
pd.set_option('display.max_rows',None)    #把数据全部行展示出来
# pd.set_option('display.width',None)  #把数据全部长度展示出来
juqing_score=df_juqing['分数'].tolist()

juqing_average_score=averagenum(juqing_score)
print('剧情片平均分：',juqing_average_score)
#################################kehuan
df_kehuan=pd.read_csv(r'D:\pythonPractise\douban_spider_keshe\kehuan_Movie\doubankehuan1000.csv',encoding='utf-8',names=['编号','名字','导演','编剧','主演一','主演二','主演三','类型','时长','年份','地区','语言','分数'])
pd.set_option('display.max_rows',None)    #把数据全部行展示出来
# pd.set_option('display.width',None)  #把数据全部长度展示出来
kehuan_score=df_kehuan['分数'].tolist()
kehuan_average_score=averagenum(kehuan_score)
print('科幻片平均分：',kehuan_average_score)
#################################xiju
df_xiju=pd.read_csv(r'D:\pythonPractise\douban_spider_keshe\xiju_Movie\doubanxiju1000.csv',encoding='utf-8',names=['编号','名字','导演','编剧','主演一','主演二','主演三','类型','时长','年份','地区','语言','分数'])
pd.set_option('display.max_rows',None)    #把数据全部行展示出来
# pd.set_option('display.width',None)  #把数据全部长度展示出来
xiju_score=df_xiju['分数'].tolist()
xiju_average_score=averagenum(xiju_score)
print('喜剧片平均分：',xiju_average_score)
#################################xuayi
df_xuayi=pd.read_csv(r'D:\pythonPractise\douban_spider_keshe\xuanyi_Movie\doubanxuanyi1000.csv',encoding='utf-8',names=['编号','名字','导演','编剧','主演一','主演二','主演三','类型','时长','年份','地区','语言','分数'])
pd.set_option('display.max_rows',None)    #把数据全部行展示出来
# pd.set_option('display.width',None)  #把数据全部长度展示出来
xuayi_score=df_xuayi['分数'].tolist()
xuayi_average_score=averagenum(xuayi_score)
print('悬疑片平均分：',xuayi_average_score)
#################################yinyue
df_yinyue=pd.read_csv(r'D:\pythonPractise\douban_spider_keshe\yinyue_Movie\doubanyinyue1000.csv',encoding='utf-8',names=['编号','名字','导演','编剧','主演一','主演二','主演三','类型','时长','年份','地区','语言','分数'])
pd.set_option('display.max_rows',None)    #把数据全部行展示出来
# pd.set_option('display.width',None)  #把数据全部长度展示出来
yinyue_score=df_yinyue['分数'].tolist()
yinyue_average_score=averagenum(yinyue_score)
print('音乐片平均分：',yinyue_average_score)

# type = {
# '爱情片': 6.910017152658611,
# '动画片': 7.182758620689662,
# '动作片': 6.5966971746915934,
# '剧情片': 7.328073901040708,
# '科幻片': 6.560277777777789,
# '喜剧片': 6.8151914785696235,
# '悬疑片': 6.6662292817679525,
# '音乐片': 7.4518207282913105,
# }
print(type)

types=['爱情','动画','动作','剧情','科幻','喜剧','悬疑','音乐']
types_score=[6.91,7.18,6.60,7.33,6.56,6.82,6.67,7.45]
types_number=[2915,841,2513,4714.1080,3943,1448,357]
types_average_score=dict(zip(types,types_score))
print(types_average_score)

def change_type():
    df1 = pd.read_csv(r'D:\pythonPractise\douban_spider_keshe\data_analyze\change_CSV\change_type1.csv', encoding='utf-8',
                     names=['编号', '名字', '导演', '编剧', '主演一', '主演二', '主演三', '类型', '时长', '年份', '地区', '语言', '分数'])
    change_type=df1['类型']
    df1['类型'] = change_type.replace(types_average_score)
    change_type = df1['类型']
    print(change_type)
    df1.to_csv("D:\pythonPractise\douban_spider_keshe\data_analyze\change_CSV\change_type2.csv")  # 现存入一个CSV
change_type()
#############################################存入数据库
def databases():
    conn = pymysql.connect("localhost", "root", "root", "doubanmovie")
    cursor = conn.cursor()
    for i in range(len(types)):
        sql_insert = "insert into type_score(type,score,number)values('" + types[i] + "','" + str(
            types_score[i]) + "','" + str(types_number[i]) + "')"
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

