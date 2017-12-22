# -*- coding: utf-8 -*-
import sqlite3
conn = sqlite3.connect('test.db')
cursor = conn.cursor()
#execute字符串参数格式是严格的，都是具有意义的。
#数字不知道什么意思，不是大小。
cursor.execute('create table user (id varchar(20) primary key, name varchar(2))')
print cursor.rowcount
cursor.execute('insert into user (id,name) values (\'1\',\'hank\')')
print cursor.rowcount
#cursor.execute('select * from user where id=?',('1',))
cursor.execute('select * from user where id=? or name=?',('1','asdf'))
values = cursor.fetchall()
print values
cursor.close()
conn.commit()
conn.close()