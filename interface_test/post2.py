import requests
import json

host = 'https://httpbin.org/'
endpoint = 'post'
url = ''.join([host,endpoint])

data = {
    "info":{"code":1,"sex":"男","id":1900,"name":"朱正仁"},
    "code":1,
    "name":"陌生人","sex":"女",
    "data":[{"code":1,"sex":"男","id":1900,"name":"朱正仁"},{"code":1,"sex":"女","id":1900,"name":"朱正仁"}],
    "id":1900
}

#r= requests.post(url,data=json.dumps(data))
r= requests.post(url,json=data)

print(r.headers)
print(r.text)