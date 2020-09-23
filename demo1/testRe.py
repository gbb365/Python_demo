#! /usr/bin/env python  
# -*- coding:utf-8 -*-  

#正则表达式的使用
import re
# 创建模式对象

# pat = re.compile("AA")
# m = pat.search("AABAABBAABAA")#只会找到第一个

# m  = re.search("asd","Aasd")#前面的是规则，后面的是串

# m = re.findall("a","abkcadogja") #前面是规则，后面是字符串。选择所有
# m = (re.findall("[A-Z]+","ADDFHfdlkghHJB"))
# print(m)

#SUB

# print(re.sub("a","A","abcdcasd")) #找到a，用A替换

#建议在正则表达式中，被比较的字符串前面加上r，不用担心转义字符的
a = r"\aadb-\'"
# print(a)

# a = "1234人人民或喝过"
# pat = re.compile("(\d+)\w+")
# m = re.findall(pat,a)
# print(m)
data =['1','2','3','4']
bat = ','.join(data)
print(bat[7])