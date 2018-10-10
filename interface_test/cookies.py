import requests

host = 'http://httpbin.org/'
endpoint = 'cookies'
url = ''.join([host,endpoint])
url1 = 'http://www.baidu.com/'

r = requests.get(url1)
#print(r.cookies)
#将cookies的jar包转换为字典
d = requests.utils.dict_from_cookiejar(r.cookies)

#print(d)
#print({a.name:a.value for a in r.cookies})
#coookies ={'cookie_name':'hsadkasfkashfkasfhjka'}
#r1 = requests.get(url,cookies = coookies)
#print(r1.text)

#使用session发送cookie
s = requests.Session()
c =requests.cookies.RequestsCookieJar()
c.set('cookie-name','cookie-value',path='/',domain ='.test.com')
s.cookies.update(c)
print(requests.utils.dict_from_cookiejar(s.cookies))