#! /usr/bin/env python  
# -*- coding:utf-8 -*-  

# 某个指定页面的内容
import re
import urllib.request,urllib.error
import operator
import xlwt
from bs4 import BeautifulSoup


def askUrl(url):
	head = {  # 用户代理，告诉服务器，我们是什么类型的浏览器，本质是告诉浏览器我们可以接受什么内容
		# 模拟浏览器头部信息，像豆瓣发请求
		"User-Agent": "User-Agent: Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36"
	}
	requst = urllib.request.Request(url,headers=head)

	html = ""
	try:
		response = urllib.request.urlopen(requst)
		html = response.read().decode("utf-8") # 读取整个网页的内容
	except urllib.error.URLError as e:
		if hasattr(e,"code"):
			print(e.code)
		if hasattr(e,"reason"):
			print(e.reason)
	return html


# 获取网页数据
def getdata(baseurl):
	datalist = []
	for i in range(0,10):
		# 共25个页面需要爬取
		url = baseurl+str(i*25)
		html = askUrl(url)
		#对爬取的整个网页进行解析
		soup = BeautifulSoup(html,"html.parser")
		# 遍历整个页面所有有item标签的下面的需要的元素
		for item in soup.find_all('div',class_='item'):
			data = []

			link = item.find('a').get('href')
			img_lisk = item.find('img').get('src')
			name = item.find_all('span',class_ = 'title')
			if len(name) == 2:
				cname = name[0].get_text()
				ename = name[1].get_text()
				ename = re.sub('/','',ename)
			else:
				cname = name[0].get_text()
				ename = None

			score = item.find('span', class_='rating_num').get_text()
			# \w 匹配字母或数字或下划线或汉字 等价于 '[^A-Za-z0-9_]'。
			count = re.findall(r'<span>(\d+)\w+</span>', str(item))[0]
			info = item.find('p',class_='').get_text()
			info = re.sub(" ","",info)

			if item.find('span',class_= "inq"):
				desc = item.find('span',class_= "inq").get_text()
			else:
				desc = None
			desc = str(desc)
			desc = re.sub('<br(\s+)?/>(\s+)?', "", desc)
			desc = re.sub('/', "", desc)
			desc= re.sub('>', "", desc)
			desc = re.sub(' ', "", desc)
			#data.append(desc.strip())
			data = [link,img_lisk,cname,ename,score,count,desc,info]
			datalist.append(data)
			# print(datalist)
			# break
	print(datalist[1])
	# 按照评分人数升序返回
	#datalist.sort(key = operator.itemgetter(5),reverse=False)
	return datalist

# 数据保存
def savedata(dataList,savepath):
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



def main():
	baseurl = "https://movie.douban.com/top250?start=?"
	savepath = "250.xls"
	datalist = getdata(baseurl)
	savedata(datalist,savepath)




if __name__ == '__main__':

	main()
	print("爬取完成")
	'''
		就三步：
		askUrl()获取单个页面的内容
		getdata()循环askUrl(),并对取到的内容进行解析保存到list
		savedata()将datalist中的数据保存到表格或者数据库
		
		关键是怎么找到标签的内容
	'''