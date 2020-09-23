#! /usr/bin/env python  
# -*- coding:utf-8 -*-  

import xlwt
#
# #创建workbook
# workbook = xlwt.Workbook(encoding="utf-8")
# worksheet = workbook.add_sheet('sheet1')
# workbook.save('student.xls')
# worksheet.write(0,0,'hello')
# workbook.save('student.xls')

# 将数据写入表格
workbook = xlwt.Workbook(encoding = "utf-8")
worksheet = workbook.add_sheet("sheet1")
for i in range(0,10):
	for j in range(0,i+1):
		worksheet.write(i,j,"%d*%d=%d" %(i+1,j+1,(i+1)*(j+1)))

workbook.save("student1.xls")