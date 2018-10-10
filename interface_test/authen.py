import requests

#通过基本的输入方法
#r= requests.get('http://httpbin.org/basic-auth/user/passwd',auth=('user','passwd'))
#print(r.text)

#使用httpbasicauth认证
#from requests.auth import HTTPBasicAuth
#r1 = requests.get('http://httpbin.org/basic-auth/user/passwd',auth=HTTPBasicAuth('user','passwd'))
#print(r1.text)

#使用digest
from requests.auth import HTTPDigestAuth
r2 = requests.get('http://httpbin.org/digest-auth/user/passwd/MD5',auth=HTTPDigestAuth('user','passwd'))
print(r2.text)

