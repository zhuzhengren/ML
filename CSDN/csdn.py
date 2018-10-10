import  re, requests
url = "https://blog.csdn.net/imail2016/article/details/72381989"
csdn_response = requests.get(url)
tt="sss<article>bbb </article>ddd"
pat = '(.*)<article>(.*)</article>.*'

matchObj = re.search(pat,csdn_response.text.encode('utf-8'),re.M|re.I)
if  matchObj:
    print("matchObj.group() : ", matchObj.group())
    print("matchObj.group(1) : ", matchObj.group(1))
    print("matchObj.group(2) : ", matchObj.group(2))
else:
    print("match error")