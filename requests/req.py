import requests
r = requests.get('http://pythontab.com/justTest')
#print(r.text)
def saveImage( imgUrl,imgName = 'default.jpg'):
    r= requests.get(imgUrl, stream=True)
    image = r.content
    destDir = "D:\ "
    print("保存图片"+destDir+imgName+"\n")
    try:
        with open(destDir+imgName,"wb") as jpg:
            jpg.write(image)
            return
    except IOError:
        print("IO Error")
        return
    finally:
        jpg.close()

url="https://ss3.bdstatic.com/70cFv8Sh_Q1YnxGkpoWK1HF6hhy/it/u=1356334559,1220813122&fm=26&gp=0.jpg"
url2='http://n.sinaimg.cn/news/20170811/TKhJ-fyixiay6493876.jpg'
#saveImage(url2,'2.jpg')
#r = requests.get('http://api.github.com/events', stream=True)
r = requests.get('http://www.pythontab.com/html/2017/ITzixun_0801/1161.html')
#print(r.headers['Content-Type'])

url = 'http://192.168.12.66/login'
r = requests.get(url)
#print(r.cookies['_redmine_session'])
url= "http://pythontab.com/cookies"
cookies={'cookies_are':'working'}
r = requests.get(url,cookies=cookies)
print(r.url)
print(r.history)