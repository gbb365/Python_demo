#! /usr/bin/env python  
# -*- coding:utf-8 -*-
import re
import sqlite3
import urllib.request

from bs4 import BeautifulSoup


def askurl(url):
	head = {  # 用户代理，告诉服务器，我们是什么类型的浏览器，本质是告诉浏览器我们可以接受什么内容
		# 模拟浏览器头部信息，像豆瓣发请求
		"User-Agent": "User-Agent: Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36"
	}
	request = urllib.request.Request(url,headers = head)
	html = ""
	try:
		response = urllib.request.urlopen(request)
		html = response.read().decode("utf-8")
	except urllib.error.URLError as e :
		if hasattr(e,"code"):
			print(e.code)
		if hasattr(e,"reason"):
			print(e.reason)
	return html

def getdata(url):
	datalist = []
	for i in range(0,10):
		url = url +str(i*25)
		html = askurl(url)
		soup = BeautifulSoup(html,"html.parser")
		for item in soup.find_all("div",class_ = "item"):
			link = item.find("a").get("href")
			img = item.find("img").get("src")
			name = item.find_all("span",class_ = "title")
			if len(name) == 2:
				cname = name[0].get_text();
				ename = name[1].get_text();
			else:
				cname = name[0].get_text();
				ename = None
			score = item.find("span",class_ = "rating_num").get_text();
			count = re.findall(r'<span>(\d+)\w+</span>', str(item))[0]
			info = item.find('p', class_='').get_text()
			info = re.sub(" ", "", info)

			if item.find('span', class_="inq"):
				desc = item.find('span', class_="inq").get_text()
			else:
				desc = None
			desc = str(desc)
			desc = re.sub('<br(\s+)?/>(\s+)?', "", desc)
			desc = re.sub('/', "", desc)
			desc = re.sub('>', "", desc)
			desc = re.sub(' ', "", desc)

			data = [link,img,cname,ename,score,count,info,desc]
			datalist.append(data)
	return datalist


def savedata(datalist,savepath):
	initdb(savepath)
	conn = sqlite3.connect(savepath)
	cur = conn.cursor()
	for data in datalist:
		for index in range(len(data)):
			if index == 5 or index == 5:
				continue
			data[index] = '"'+str(data[index])+'"'
		sql = '''
					insert into douban250000(
					info_link,pic_link,cname,ename,score,rated,instroduction,info
					)values(%s)
				''' % ",".join(data)  # 相当于insert into(?,?,?,?) values("xx","xx","xx","xx")
		cur.execute(sql)
		conn.commit()
	cur.close()
	conn.close()


def initdb(savepath):
	sql = '''
			create table douban250000(
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
	conn = sqlite3.connect(savepath)
	cur = conn.cursor()
	cur.execute(sql)
	conn.commit()
	conn.close()



def main():
	url = "https://movie.douban.com/top250?start=?"
	# savepath = "demo.xls"
	datalist = getdata(url)
	savepath = "mov.db"
	savedata(datalist,savepath)



if __name__ == '__main__':
	main()