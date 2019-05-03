# coding:utf-8
import pymysql

a=['zhao','qian','sun']
b=[5.6,4.4,7.6]
c=['487 分钟', 'Japan: 127 分钟', '79分钟', '157分钟(韩国)', 'UK: 101 分钟', 'Japan: 138 分钟', '126分钟(美国)', '60 分钟', '113分钟', '401分钟(英国)', '174分钟']
# for i in range(len(b)):
#     sql_insert1 = "insert into director_score(director,score)values('" + a[i] + "','" + str(b[i]) + "')"
#     print(sql_insert1)
# a=a[1:]
# print(a)
sign1=':'
sign2='分'
timelong=[]
for timelong1 in c:
    location1 = timelong1.index('分钟')
    timelong2 = timelong1[:location1]
    if sign1 in timelong2:
        location2=timelong1.index(sign1)+1
        timelong3 = timelong2[location2:]
    else:
        timelong3 = timelong2
    timelong.append(timelong3)
print(timelong)
    # if sign1 in timelong1:
    #     location2=timelong1.index(sign1)
    #     print(location2)
    #     timelong2=timelong1[:location1]
    #     print(timelong2)
    # if sign1 in c:
    #     if sign2 in c:
    #     else:








# conn = pymysql.connect("localhost", "root", "root", "doubanmovie")
# cursor = conn.cursor()
#
# for i in range(len(a)):
#     sql_insert = "insert into director_score(director,score) values(a[i],5.6)"
#     sql_insert1 = "insert into director_score(director,score)values('" + a[i] + "','" + str(b[i]) + "')"
#     cursor.execute(sql_insert1)
#     print('插入')
#     conn.commit()
# cursor.close()
# conn.close()