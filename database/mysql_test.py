# -*- coding: utf-8 -*-
# 导入MySQL驱动:
import mysql.connector
# 注意把v设为你的root口令:这一步之前需要首先创建数据库test2，创建方法：http://www.linuxidc.com/Linux/2016-12/138081.htm
conn = mysql.connector.connect(user='root',password='v',database='test2',use_unicode=True)
cursor = conn.cursor()
# 创建user2表:
cursor.execute('create table user2 (id varchar(20) primary key,name varchar(20))')
# 插入一行记录，注意MySQL的占位符是%s:
cursor.execute('insert into user2 (id,name) values (%s,%s)',['1','Michael'])
print cursor.rowcount

# 提交事务:sqlite似乎没有这一步，也有
conn.commit()
cursor.close()

# 运行查询:
cursor2 = conn.cursor()
cursor2.execute('select * from user2 where id=%s',('1',))
values = cursor2.fetchall()
print values

# 关闭Cursor和Connection:
cursor2.close()
conn.close()
