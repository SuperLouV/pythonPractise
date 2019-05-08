import matplotlib.pyplot as plt
import numpy as np

#打开数据库获取需要的值
import pymysql

conn = pymysql.connect("localhost", "root", "root", "doubanmovie")
cursor = conn.cursor()

sql='select country,score,number from country_scores where number > 200'
# sql_insert = "insert into actor1_score(actor1,score,movie_number)values('" + actor1_list[i] + "','" + str(actor1_movie_score[i]) + "','" + str(actor1_movie_number[i]) + "')"
print(sql)
 # 执行sql语句
cursor.execute(sql)
conn.commit()
results = cursor.fetchall()
print(results)
print(type(results))
cursor.close()
conn.close()
countrys=[]
numbers=[]
scores=[]
country_score=[]
country_number=[]
plt.rcParams['font.sans-serif'] = ['SimHei']
for row in results:
    country = row[0]
    score = row[1]
    number = row[2]
    a=[country,number]
    country_number.append(a)
    b=[country,score]
    country_score.append(b)
    countrys.append(country)
    numbers.append(number)
    scores.append(score)

print(scores)
# print(countrys)
plt.figure(figsize=(10, 6))
plt.bar(countrys,numbers,width=0.3,color='b')
for a,b in zip(countrys,numbers):
    plt.text(a, b+0.05, '%.0f' % b, ha='center', va= 'bottom',fontsize=18)
plt.xlabel("国家")  # 设置X轴标签
plt.ylabel("电影数量")  # 设置Y轴标签
plt.title("不同国家电影数量")
plt.savefig('./country_number.png')
plt.show()

plt.figure(figsize=(10, 6))
plt.bar(countrys,scores,width=0.3,color='g')
for a,b in zip(countrys,scores):
    plt.text(a, b+0.05, '%.2f' % b, ha='center', va= 'bottom',fontsize=18)  #2f为小数点后两位
plt.xlabel("国家")  # 设置X轴标签
plt.ylabel("电影分数")  # 设置Y轴标签g
plt.title("样本数在200以上的国家电影均分")
plt.savefig('./country_score.png')
plt.show()
########################################################################
#
conn = pymysql.connect("localhost", "root", "root", "doubanmovie")
cursor = conn.cursor()

sql='select country,score,number from country_scores where score > 7.5 and number>10'
# sql_insert = "insert into actor1_score(actor1,score,movie_number)values('" + actor1_list[i] + "','" + str(actor1_movie_score[i]) + "','" + str(actor1_movie_number[i]) + "')"
print(sql)
 # 执行sql语句
cursor.execute(sql)
conn.commit()
results1 = cursor.fetchall()
print(results1)
print(type(results1))
print(len(results1))
cursor.close()
conn.close()


countrys1=[]
numbers1=[]
scores1=[]
country_score1=[]
country_number1=[]
for row1 in results1:
    country1 = row1[0]
    score1 = row1[1]
    number1 = row1[2]
    # a=[country1,number1]
    # country_number1.append1(a)
    # b=[country,score]
    # country_score.append(b)
    countrys1.append(country1)
    numbers1.append(number1)
    scores1.append(score1)
print(scores1)
plt.figure(figsize=(20, 6))
plt.bar(countrys1,scores1,width=0.3,color='y')
for a,b in zip(countrys1,scores1):
    plt.text(a, b+0.05, '%.2f' % b, ha='center', va= 'bottom',fontsize=8)
plt.xlabel("国家")  # 设置X轴标签
plt.ylabel("电影分数")  # 设置Y轴标签
plt.title("平均分高于7.5分的国家（最小样本数10）")
plt.savefig('./highest_score.png')
plt.show()