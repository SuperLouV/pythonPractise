# coding:utf-8
import MySQLdb

conn = MySQLdb.connect(host='127.0.0.1',
                       port=3306,
                       charset='utf8',
                       passwd='123456',
                       user='root',
                       db='immo'
                       )
cursor = conn.cursor()
sql_insert = "insert into user(userid,username) values(16,'name19')"
sql_update = "update user set username='name7' where userid=7"
sql_delete = "delete from user where usrid<5"
try:
    cursor.execute(sql_insert)
    print
    cursor.rowcount  # 执行过inset改变了几行
    cursor.execute(sql_delete)
    print
    cursor.rowcount  # 同上
    cursor.execute(sql_update)
    print
    cursor.rowcount
    conn.commit()
except Exception as e:
    print
    e
    conn.rollback()  # 回滚事务

cursor.close()
conn.close()