import requests
host = 'http://httpbin.org/'
endpoint = 'cookies/set/sessioncookie/123456789'
url = ''.join([host,endpoint])
url1 = 'http://httpbin.org/cookies'

#r= requests.get(url)
#print(r.text)

#初始化一个session对象
#session = requests.Session()
#session.get(url)
#保持一个会话，通过会话访问URL，会话会保存cookies等值
#r1 = session.get(url1)
#print(r1.text)

header1 = {'test1':'aa'}
header2 = {'test1':'bb'}

session1 =requests.Session()
session1.headers.update(header1)#已经存在服务器的信息
r2 = session1.get('http://httpbin.org/headers',headers = header2)#发送新的headers信息
print(r2.text)
print("************************************************")
#删除session信息
session1.headers['test2'] =None
#r3 = session1.get('http://httpbin.org/headers',headers = header2)
#print(r3.text)