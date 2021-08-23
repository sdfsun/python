# -*- coding: utf-8 -*-
# @Author: 王琨
# @Date: 2021-07-29 14:55:12
# @LastEditors: 王琨
# @LastEditTime: 2021-07-29 17:14:49
# @FilePath: \pythonProject\shuushuu.py
# @Descripttion: shuu网站图片链接

import requests
from lxml import etree
from user_agent import generate_user_agent
import json
import time


def proxy(obj):
    while True:
        proxy_url = 'http://17610040106.v4.dailiyun.com/query.txt?key=NP86444E99&word=&count=1&rand=false&ltime=0&norepeat=false&detail=false'
        response = requests.get(proxy_url, headers=obj)
        proxies = response.text.strip()
        if proxies:
            break
        else:
            time.sleep(15)
    print(proxies)
    return proxies


def main():
    start_time = time.time()
    url_list = []
    for i in range(1, 100):
        try:
            url = 'https://e-shuushuu.net/?page=' + str(i)
            headers = {
                'User-Agent': generate_user_agent()
            }
            proxies = {
                'http:': proxy(headers)
            }
            response = requests.get(url=url, headers=headers, proxies=proxies)
            html = etree.HTML(response.text)
            shuu_url_list = html.xpath('//a[@class="thumb_image"]/@href')
            for url in shuu_url_list:
                shuu_url = 'https://e-shuushuu.net/' + url
                url_list.append(shuu_url)
        except Exception:
            print(i)
            break

    with open('shuu_url.json', 'w') as f:
        json.dump(url_list, f)

    begin_time = time.time()
    print(begin_time - start_time)
