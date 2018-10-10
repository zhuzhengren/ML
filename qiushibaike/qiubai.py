# -*- coding:UTF-8 -*-
import urllib,re
import urllib2
page=1
url='http://www.qiushibaike.com/hot/page/'+str(page)
user_agent='Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.78 Safari/537.36 '
headers={'User-Agent':user_agent}
try:
    request = urllib2.Request(url,headers = headers)
    response = urllib2.urlopen(request)
    content = response.read().decode('utf-8')
    str1='<div.*?class="author.*?>.*?<a.*?</a>.*?<a.*?>.*?<h2>(.*?)</h2>'+\
         '.*?<div class="content">.*?<span>(.*?)</span>.*?</div>'+\
         '.*?<div class="stats.*?class="number">(.*?)</i>'

    pattern = re.compile(str1,re.S)
    items = re.findall(pattern, content)
    for item in items:
        print item[0],item[1],item[2]

except urllib2.URLError, e:
    if hasattr(e,"code"):
        print e.code
    if hasattr(e,"reason"):
        print e.reason

