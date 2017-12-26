# -*- coding: utf-8 -*-
# 导入:
from sqlalchemy import Column,String,create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

# 创建对象的基类:
Base = declarative_base()

# 定义User对象:
class User(Base):
	# 表的名字:
	__tablename__ = 'user2'

	 # 表的结构:
	id = Column(String(20),primary_key=True)
	name = Column(String(20))

# 初始化数据库连接:
engine = create_engine('mysql+mysqlconnector://root:v@localhost:3306/test2')
# 创建DBSession类型:
DBSession = sessionmaker(bind=engine)

# 创建session对象:
session = DBSession()
# 创建新User对象:
new_user = User(id='4',name='Hunk')
# 添加到session:
session.add(new_user)
# 提交即保存到数据库:
session.commit()
# 关闭session:
session.close()

session = DBSession()
user = session.query(User).filter(User.id=='2').one()
print 'type:',type(user)
print 'name:',user.name
session.close()

#id 需要递增；插入过的id不可重复插入，id需要加1.
#数据库---create_engine()---sessionmaker()---DBSession().