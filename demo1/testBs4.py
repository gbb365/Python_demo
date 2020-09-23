#! /usr/bin/env python  
# -*- coding:utf-8 -*-  

# BeautifulSoup4将复杂的HTML文档转换成一个复杂的树形结构，每个节点都是python对象，所有对象可以归纳为4种
# Tag 标签及其内容：拿到它的第一个内容
# NabigableString 标签里面的内容
# BeautifulSoup 表示整个文档
# Domment	是一个特殊的NabigableString 输出的内容不包含注释符号
from bs4 import BeautifulSoup

file = open("./baidu.html","rb")#注意写双引号

html = file.read().decode("utf-8")
bs = BeautifulSoup(html,"html.parser")

# print(bs.title)
# print(type(bs.head))
# print(bs.title.string)
# print(bs.a.attrs)
# print(type(bs))
# print(bs.name)
# print(bs)

# print(bs.a.string)
# print(type(bs.a.string))

# -----------------------

#文档的遍历
# print(bs.head.contents[3])

#文档的搜索
# 1.find_all
# 字符串过滤：会查找与字符串完全匹配的内容
# t_list = bs.find_all("a")
# import re
# t_list = bs.find_all(re.compile("a"))
# print(t_list)

# 传入一个函数，根据函数的要求搜索
# def name_is_exists(tag):
# 	return tag.has_attr("name")
#
# t_list = bs.find_all(name_is_exists)
#
# for item in t_list:
# 	print(item)
#

# 2.kwargs  参数
# t_list= bs.find_all(id = "div")
# t_list = bs.find_all(href="https://www.hao123.com/")
# for item in t_list:
# 	print(item)


# 3.文本参数
# import re
# # t_list = bs.find_all(text = 'hao123')
# t_list = bs.find_all(text = re.compile("\d"))#使用正则表达式来查找包含特定内容
#
# for item in t_list:
# 	print(item)


#4. limit 参数
# t_list = bs.find_all("a",limit = 3)
# for item in t_list:
# 	print(item)

# css 选择器
# print(bs.select('title'))#通过标签查找
# t_list = bs.select(".mnav") #通过类名查找
# t_list= bs.select("#u1") #通过id

# t_list= bs.select("a[class='bri'] ") #通过属性

# t_list = bs.select("head>title")#通过子标签
# t_list = bs.select(".mnav ~ .bri")
# for item in t_list:
# 	print(item)

# 文档搜索
