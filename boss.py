import re
import requests
import time


def get_page(page, headers):
    url = "https://www.zhipin.com/c101010100/h_101010100/?query=python&page={page}".format(
        page=page)
    response = requests.get(url, headers)
    if response.status_code == 200:
        text = response.text

    else:
        print("错误代码:" + str(response.status_code))
        print(response)
        print('获取页面失败')
    return text


def parser_page(text, page):
    # text='<a href="/job_detail/1412226095.html" ka="search_list_16" data-itemid="16"'
    host = 'http://www.zhipin.com'
    urls = []
    index = 1

    pattern = re.compile(r'<a href="(.+?)" ka="search_.+?"')
    results = pattern.findall(text)

    # 遍历该页的所有职位信息，并构造详细页面的url
    for i in results:
        i = host + i + "?search_list_{num}".format(num=(page - 1) * 15 + index)
        urls.append(i)
        index += 1
    return urls


def get_detail(url, headers):
    response = requests.get(url, headers)
    if response.status_code == 200:
        text = response.text
    else:

        print("获取详细页面失败")
    return text


def parser_detail(text):
    # 解析职位信息
    text = text.replace("<br>", " ")
    pattern = re.compile(
        r'<span class="time">(.+?)<.+?class="name">(.+?)<span class="badge">'
        r'(.+?)<.+?p>(.+?)<.+?/em>(.+?)<.+?/em>(.+?)</p>', re.S)
    position_info = pattern.findall(text)[0]
    position_info = {
        '发布时间': position_info[0],
        '职位名称': position_info[1],
        '薪资': position_info[2],
        '地点': position_info[3],
        '工作经验': position_info[4],
        '学历要求': position_info[5],
    }

    # 解析公司信息
    pattern = re.compile(
        r'<h3 .+?"_blank">(.+?)<.+?p>(.+?)</p.+?p>(.+?)<.+?/em>(.+?)<.+?/em>(.+?)</p>',
        re.S)
    company_info = pattern.findall(text)[0]
    company_info = {
        '公司名称': company_info[0],
        '公司全称': company_info[1],
        '行业': company_info[2],
        '公司状况': company_info[3],
        '公司人数': company_info[4],
    }

    # 解析任职要求描述
    # <div class="text">

    pattern = re.compile(r'<div class="text">(.+?)</div', re.S)
    description = pattern.findall(text)
    description = {
        '任职要求描述': description
    }
    print(position_info)
    print(company_info)
    print(description)


def main():
    headers = {
        'Host':' www.zhipin.com',
        'User-Agent': ' Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.146 Safari/537.36'
       }
    for i in range(1, 11):
        time.sleep(1)  # 防止爬虫爬取过快
        text = get_page(1, headers)
        urls = parser_page(text, 1)
        for url in urls:
            text = get_detail(url, headers)
            parser_detail(text)


main()