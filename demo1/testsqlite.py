#! /usr/bin/env python  
# -*- coding:utf-8 -*-  
import sqlite3
connect = sqlite3.connect("test.db")#打开或创建数据库文件
print("成功打开数据库")
c = connect.cursor()#获取游标

#创建数据表
# sql = '''
# 	create table company
# 		(id int primary key not null,
# 		name text not null,
# 		age int not null,
# 		address char(50),
# 		salary real);
# '''
# 插入数据
# sql1 = '''
# 	insert into company(id,name,age,address,salary)
# 	values(1,'张三',32,"成都",8000);
# '''
# sql2 = '''
# 	insert into company(id,name,age,address,salary)
# 	values(2,'李四',42,"四川",12000);
# '''
# # sql 语句的标点符号不能写错

sql  = '''
 	select id,name ,address,salary from company
'''
cursor = c.execute(sql)
for row in cursor:
	print("id = ",row[0])
	print("name=",row[1])
	print("address",row[2])
	print("salary",row[3],"\n")




connect.commit()
connect.close()

print("查询完毕")




