
import csv
import matplotlib
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

# 绘制散点图
df=pd.read_csv(r'D:\pythonPractise\douban_spider_keshe\data_analyze\change_CSV\final_test.csv',encoding='utf-8',names=['导演','编剧','主演一','主演二','主演三','类型','时长','地区','分数'])
pd.set_option('display.max_rows',None)    #把数据全部行展示出来
plt.rcParams['font.sans-serif'] = ['SimHei']
examDf = pd.DataFrame(df)
examDf.head()
print(examDf.head())

def director_scatter():
    plt.figure(figsize=(20, 6))
    # 绘制散点图,examDf.jt为X轴，examDf.hk为Y轴
    plt.scatter(examDf.导演, examDf.分数, color='darkgreen', label="director score", s=2)  # s为点大小
    # 添加图的标签（x轴，y轴）
    plt.xlabel("导演评分分布")  # 设置X轴标签
    plt.ylabel("电影评分分布")  # 设置Y轴标签
    plt.title("director score相关图")
    plt.savefig('./director_scatter.png')
    plt.show()  # 显示图像


def screenplayer_scatter():
    plt.figure(figsize=(20, 6))
    plt.scatter(examDf.编剧, examDf.分数, color='y', label="screenplayer score", s=2)  # s为点大小
    # 添加图的标签（x轴，y轴）
    plt.xlabel("编剧评分分布")  # 设置X轴标签
    plt.ylabel("电影评分分布")  # 设置Y轴标签
    plt.title("screenplayer score相关图")
    plt.savefig('./screenplayer_scatter.png')
    plt.show()  # 显示图像

def actor1_scatter():
    plt.figure(figsize=(20, 6))
    plt.scatter(examDf.主演一, examDf.分数, color='b', label="actor1 score", s=2)  # s为点大小
    # 添加图的标签（x轴，y轴）
    plt.xlabel("主演一评分分布")  # 设置X轴标签
    plt.ylabel("电影评分分布")  # 设置Y轴标签
    plt.title("actor1 score相关图")
    plt.savefig('./actor1_scatter.png')
    plt.show()  # 显示图像

def actor2_scatter():
    plt.figure(figsize=(20, 6))
    plt.scatter(examDf.主演二, examDf.分数, color='r', label="actor2 score", s=2)  # s为点大小
    # 添加图的标签（x轴，y轴）
    plt.xlabel("主演二评分分布")  # 设置X轴标签
    plt.ylabel("电影评分分布")  # 设置Y轴标签
    plt.title("actor2 score相关图")
    plt.savefig('./actor2_scatter.png')
    plt.show()  # 显示图像


def actor3_scatter():
    plt.figure(figsize=(20, 6))
    plt.scatter(examDf.主演三, examDf.分数, color='k', label="actor3 score", s=2)  # s为点大小
    # 添加图的标签（x轴，y轴）
    plt.xlabel("主演三评分分布")  # 设置X轴标签
    plt.ylabel("电影评分分布")  # 设置Y轴标签
    plt.title("actor3 score相关图")
    plt.savefig('./actor3_scatter.png')
    plt.show()  # 显示图像
director_scatter()
actor1_scatter()
actor2_scatter()
actor3_scatter()
screenplayer_scatter()
# def country_scatter():
#     plt.figure(figsize=(20, 6))
#     plt.scatter(examDf.地区, examDf.分数, color='m', label="country score", s=2)  # s为点大小
#     # 添加图的标签（x轴，y轴）
#     plt.xlabel("地区评分分布")  # 设置X轴标签
#     plt.ylabel("电影评分分布")  # 设置Y轴标签
#     plt.title("country score相关图")
#     plt.show()  # 显示图像
#
# def type_scatter():
#     plt.figure(figsize=(20, 6))
#     plt.scatter(examDf.类型, examDf.分数, color='m', label="type score", s=2)  # s为点大小
#     # 添加图的标签（x轴，y轴）
#     plt.xlabel("类型评分分布")  # 设置X轴标签
#     plt.ylabel("电影评分分布")  # 设置Y轴标签
#     plt.title("type score相关图")
#     plt.show()  # 显示图像
# type_scatter()