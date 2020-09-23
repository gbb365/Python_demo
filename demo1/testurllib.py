#! /usr/bin/env python  
# -*- coding:utf-8 -*-  

import urllib.request

# response = urllib.request.urlopen("http://www.baidu.com")
# print(response.read().decode('UTF-8'))##解析获取到的密码

# data = bytes(urllib.parse.urlencode({'hello':'world'}),encoding = 'utf-8')
# print(urllib.request.urlopen('http://www.httpbin.org/post',data = data).read().decode('utf-8'))

# try:
# 	response = urllib.request.urlopen("http://www.httpbin.org/get",timeout=0.01)
# 	print(response.read().decode('UTF-8'))##解析获取到的密码
#
# except urllib.error.URLError as e:
# 	print("time out")

# response = urllib.request.urlopen("http://www.baidu.com")
# print(response.status)
# print(response.getheader("Set-Cookie"))
# print(response)


# headers = {
# 	"User-Agent":"User-Agent: Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36"
# }
# data = bytes(urllib.parse.urlencode({'name':'eric'}),encoding = 'utf-8')
# url = 'http://httpbin.org/post'
# req = urllib.request.Request(url = url,data = data,headers=headers,method = 'POST')
#
# response = urllib.request.urlopen(req)
# print(response.read().decode('utf-8'))

headers = {
	"User-Agent":"User-Agent: Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36"
}
url = 'https://www.douban.com'
# 构造一个request 请求对象，包含请求头等一些关键信息
req = urllib.request.Request(url = url,headers=headers)
# 返回HttpResponse对象
response = urllib.request.urlopen(req)
print(response)
# 可以改成使用request  response = requests.get(url)
# print(response.read().decode('utf-8'))
