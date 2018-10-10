import requests
import json
host = 'https://httpbin.org/'
endpoint = 'post'
url = ''.join([host,endpoint])

params  = {'show_env':1}
data = {'a':'朱正仁','b':'from_data'}

r = requests.post(url,params=params,data=data)


print(r.headers)
print(r.text)
resp = r.json()
print(resp['form'])