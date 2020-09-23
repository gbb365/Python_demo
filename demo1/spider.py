#! /usr/bin/env python  
# -*- coding:utf-8 -*-  

from bs4 import BeautifulSoup
import re
import urllib.request,urllib.error
import xlwt
import sqlite3

# 保存数据到数据库
def saveData2(datalist, dbpath):
	init_db(dbpath)
	conn = sqlite3.connect(dbpath)
	cursor = conn.cursor()
	for data in datalist:
		for index in range(len(data)):
			if index == 4 or index ==5:
				continue
			data[index] = '"'+str(data[index])+'"'
		sql = '''
			insert into douban250(
			info_link,pic_link,cname,ename,score,rated,instroduction,info
			)values(%s)
		'''%",".join(data)#相当于insert into(?,?,?,?) values("xx","xx","xx","xx")

		#返回一个由 iterable 中的字符串拼接而成的字符串。
		# 如果 iterable 中存在任何非字符串值包括 bytes 对象则会引发 TypeError。
		# 调用该方法的字符串将作为元素之间的分隔。
		print(sql)
		cursor.execute(sql)	#注意空格
		conn.commit()
	cursor.close()
	conn.close()


def init_db(dbpath):
	sql = '''
		create table douban250(
			id integer primary key autoincrement,
			info_link text,
			pic_link text,
			cname text,
			ename varchar,
			score number,
			rated number,
			instroduction text,
			info text
		
		);
	'''
	conn = sqlite3.connect(dbpath)
	cursor = conn.cursor()
	cursor.execute(sql)
	conn.commit()
	conn.close()

def main():
	baseurl = "https://movie.douban.com/top250?start=?"
	dbpath = "movie.db"
	datalist = getData(baseurl)
	savepath = "douban2502.xls"
	# save(datalist,savepath)
	# askUrl(baseurl)
	saveData2(datalist,dbpath)
# 注意写模式串的时候还是复制的比较好，自己打容易多写一些空格，无法读取正确的内容
findLink = re.compile(r'<a href="(.*?)">') #创建正则表达式对象
findImage = re.compile(r'<img .*src="(.*?)"',re.S)#re.s  让换行符包含在字符中
# findTitle = re.compile(r'<span class = "title">(.+)</span>')
findTitle = re.compile(r'<span class="title">(.*)</span>') #影片名称
findRating = re.compile(r'<span class="rating_num" property="v:average">(.+)</span>')#评分
# findJudge = re.compile(r'<span>(\d+)评价</span>')#评分人数

findInq = re.compile(r'<span class="inq">(.*)</span>')#概况
findBd = re.compile(r'<p class=""(.*?)</p>',re.S)#相关信息

# 爬取网页
def getData(baseurl):
	datalist = []

	for i in range(0,10):  #调用获取250条的页面信息
		url = baseurl+ str(i*25)
		html = askUrl(url)# 保存获取到的源码

		# 爬取到一个页面就要解析一个
		soup = BeautifulSoup(html,"html.parser")
		for item in soup.find_all('div',class_="item"):
			# print(item) #测试，查看电影item的全部信息
			data = [] #保存一部电影的所有信息
			item = str(item)
			# print(item)
			# break
			#
			link = re.findall(findLink,item)[0]#保存链接
			# print(link)
			data.append(link)
			imgSrc = re.findall(findImage,item)[0]#图片
			# print(link)
			data.append(imgSrc)
			titles =re.findall(findTitle,item)#影片名称
			if(len(titles)==2):
				ctitle = titles[0]
				data.append(ctitle)
				otitle = titles[1].replace("/","")
				data.append(otitle)
			else:
				data.append(titles[0])
				data.append(' ') # 外文名留空

			ratint =re.findall(findRating,item)[0]#评分
			data.append(ratint)
			judgeNum = re.findall(r'<span>(\d+)\w+</span>',str(item))[0]
			# judgeNum = re.findall(findJudge,str(item))[0]#评分人数
			print(judgeNum)
			data.append(judgeNum)
			inq = re.findall(findInq,item)#概述
			if len(inq) != 0 :
				inq = inq[0].replace(".","")
				data.append(inq)
			else:
				data.append(" ")
			bd = re.findall(findBd,item)[0]#相关信息
			bd = re.sub('<br(\s+)?/>(\s+)?'," ",bd)
			bd = re.sub('/',"",bd)
			bd = re.sub('>',"",bd)
			bd = re.sub(' ',"",bd)
			data.append(bd.strip())
			datalist.append(data)
	# print(datalist)
	return datalist

# 得到一个指定地址的网页内容
def askUrl(url):
	head  = {# 用户代理，告诉服务器，我们是什么类型的浏览器，本质是告诉浏览器我们可以接受什么内容
		# 模拟浏览器头部信息，像豆瓣发请求
		"User-Agent" :"User-Agent: Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36"
	}
	request = urllib.request.Request(url,headers=head)
	html = ""
	try:
		response = urllib.request.urlopen(request)
		html = response.read().decode('utf-8')#读取整个网页的内容
		# print(html)
	except urllib.error.URLError as e:
		if hasattr(e,"code"):
			print(e.code)
		if hasattr(e,"reason"):
			print(e.reason)

	return html
def save(dataList,savepath):
	# print('save')
	workBook = xlwt.Workbook(encoding = "utf-8",style_compression=0)
	workSheet = workBook.add_sheet('豆瓣电影top250',cell_overwrite_ok=True)
	col = ("电影详情链接","图片链接","影片中文名","影片外文名","评分","评分数","概况","相关信息")
	for i in range(0,8):
		workSheet.write(0,i,col[i])#写入列名
	for i in range(0,250):
		print("第%d条" %(i+1))
		data = dataList[i];
		for j in range(0,8):
			workSheet.write(i+1,j,data[j]) # 坐标别写漏，否则出现什么类型转换错误
	workBook.save(savepath)#保存数据


if __name__ == '__main__':
	main()
	# init_db("text.db")
	print("爬取完毕！")