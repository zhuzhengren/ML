import requests
import json

host = 'https://httpbin.org/'
endpoint = 'post'
url = ''.join([host,endpoint])
#普通上传文件
files = {'file':open('main.py','rb')}
#将字符串当做文件传输
files2= {'file':('test.txt','send sss')}
#自定义文件名，文件类型以及请求头
files3 = {'file':open('main.py','rb')}
#流式上传
with open("main.py") as f:
    r = requests.post(url,data=f)

#r = requests.post(url,files=files2)

print(r.headers)
print(r.text)