#获取无重复信息的数据
import pandas as pd
import numpy as np
# df=pd.read_csv(r'D:\pythonPractise\douban_spider_keshe\data_analyze\yinyue_1.csv',encoding='utf-8',header=None,names=['a','c','e','g','i','k','l','m','o','p','q'])
# df=pd.read_csv(r'D:\pythonPractise\douban_spider_keshe\data_analyze\yinyue_1.csv',encoding='utf-8',names=['编号','名字','导演','编剧','主演一','主演二','主演三','类型','时长','年份','地区','语言','分数'])
from douban_spider_keshe.test.jiequStr import cut_str

df=pd.read_csv(r'D:\pythonPractise\douban_spider_keshe\data_analyze\all_2.csv',encoding='utf-8',names=['编号','名字','导演','编剧','主演一','主演二','主演三','类型','时长','年份','地区','语言','分数'])

pd.set_option('display.max_rows',None)    #把数据全部行展示出来
# pd.set_option('display.width',None)  #把数据全部长度展示出来
print(type(df))

# print(df.columns)
# print(df.columns[1])
# print(df.loc[1,'导演'])   #第一行的导演
# a=df.loc[df['地区'].isin('美国')]
a=df.loc[df['地区'] == '美国']    #目前仅仅是搜索美国，之后添加条件美国/英国
country_list=df['地区'].tolist()
print(country_list)

sign = '/'
print(type(sign))

print(type(country_list[0]))
print(country_list[0])
# for i in country_list:
#     print(type(str))
country_list2=[]
for str in country_list:
    try:
        if sign in str:
            location = str.index('/')
            str = str[0:location]
            print("有",str)
            # location = country_list[i].index('/')
            # country_list[i] = str[0:location]
            country_list2.append(str)
            # i += 1
        else:
            # i += 1
            # country_list2[j].append(country_list[i])
            print("没有/",str)
            country_list2.append(str)
    except:
        continue
country_list2=list(set(country_list2))               #去重
print("全部国家",country_list2)
print(len(country_list2))
# language_list=df['语言'].tolist()
# print(language_list)
# print(type(language_list[2]))
# print(type(score))
# print(score)
# print(a)
score=a['分数'].tolist()   #把分数集合为一个列表，方便计算
print("score的类型：",type(score))
scoremean=np.mean(score)        #np库计算均值
# print(score)                     #输出美国音乐平均分
# print("平均值为：",scoremean)
print(len(country_list))
# print(len(language_list))
# cut_str(country_list)



# print(language_list)
# cut_str(language_list)
# for i in language_list:

# print(data['a'])
# print(df.values)
