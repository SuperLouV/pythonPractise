# coding:utf-8
import pymysql

a=['zhao','qian','sun']
b=[5.6,4.4,7.6]
for i in range(len(b)):
    sql_insert1 = "insert into director_score(director,score)values('" + a[i] + "','" + str(b[i]) + "')"
    print(sql_insert1)





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