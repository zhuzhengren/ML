# -*- coding:UTF-8 -*-
import urllib
import urllib2
import cookielib
import re

#使用cookie
cookie = cookielib.MozillaCookieJar()
hander=urllib2.HTTPCookieProcessor(cookie)
opener = urllib2.build_opener(hander)
#添加请求头User-Agent
agent='Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.78 Safari/537.36'
opener.addheaders=[('User-Agent',agent),
                   ('Referer','http://192.168.12.66/login?back_url=http%3A%2F%2F192.168.12.66%2F')]
response = opener.open('http://192.168.12.66/login?back_url=http%3A%2F%2F192.168.12.66%2F')
#读取页面中隐藏的token
html = response.read()
reg=r'<meta content="(.+?)" name="csrf-token" />'
token_reg=re.compile(reg)
token=re.findall(token_reg,html)
auth_token=token[0]
#构建请求数据
form_data = urllib.urlencode({  #注意urlencode方法
    "utf8": '✓',
    "authenticity_token":auth_token,
    "back_url": "http://192.168.12.66/",
    "username": "zhuzhengren",
    "password": "874347989",
    "login": "登录 »"})


# 发送请求，登录系统
result = opener.open('http://192.168.12.66/login', form_data)
result = opener.open('http://192.168.12.66/projects/mj5_qc_test/issues')
result = result.read()
#print result
str=r'<td .*?subject.*?>.*?>(.*?)</a>.*?user active.*?>(.*?)</a>.*?fixed_version">.*?>(.*?)</a>'
re.compile(str)
title = re.findall(str,result)
f = open('file.txt','w')
for i in title:
#    print i[0],i[1]
    f.write(i[0])
    f.write('\t')
    f.write(i[1])
    f.write('\t')
    f.write(i[2])
    f.write('\r\n')
f.close()
