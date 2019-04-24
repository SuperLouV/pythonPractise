#
# import pymysql
#
# # 打开数据库连接（ip/数据库用户名/登录密码/数据库名）
# db = pymysql.connect("localhost", "root", "root", "test")
# # 使用 cursor() 方法创建一个游标对象 cursor
# cursor = db.cursor()
#
# # 使用 execute()  方法执行 SQL 查询
# cursor.execute("SELECT VERSION()")
# # 使用 fetchone() 方法获取单条数据.
# data = cursor.fetchone()
# print("Database version : %s " % data)

# 关闭数据库连接
# db.close()

# *===================================*
# * Created by Zhihua_w.
# * Author: Wei ZhiHua
# * Date: 2017/1/10 0005
# * Time: 下午 2:39
# * Project: PYTHON STUDY
# * Power: DATABASE
# *===================================*

import pymysql

# 打开数据库连接（ip/数据库用户名/登录密码/数据库名）
db = pymysql.connect("localhost", "root", "root", "test")
# 使用 cursor() 方法创建一个游标对象 cursor
cursor = db.cursor()

# SQL 查询语句
sql = "SELECT * FROM t1"

try:
    # 执行SQL语句
    cursor.execute(sql)
    # 获取所有记录列表
    results = cursor.fetchall()
    for row in results:
        a = row[0]
        b = row[1]
        c = row[2]
        # 打印结果
        print("a=%s,b=%s,c=%s" % \
              (a,b,c))
except:
    print("Error: unable to fecth data")

# 关闭数据库连接
db.close()