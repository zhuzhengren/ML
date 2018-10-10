import  requests
import json

host = 'https://httpbin.org/'
endpoint = 'get'
url = ''.join([host,endpoint])
url2 = 'http://res.static.mojing.cn/170718-1-2-1/android/zh/1/page/443513.js'
r = requests.get(url2)

#print(r.url)
#print(r.status_code)
#print(r.reason)
#print(r.text)
print(r.content)
#print(r.cookies)
#print(r.request.headers)
response = r.json()
print(type(response))