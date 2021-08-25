#! user/bin/env python
# -*- coding: utf-8 -*-
# @Author: 王琨
# @Date: 2021-08-23 16:14:06
# @LastEditors: 王琨
# @LastEditTime: 2021-08-25 11:29:23
# @FilePath: /python/工作内容/税务/qinghai.py
# @Description: 

import requests
from user_agent import generate_user_agent
from lxml import etree


headers = {
    'user-agent': generate_user_agent()
}
url = 'http://qinghai.chinatax.gov.cn/web/zdsswfsxaj/zdaj.shtml'

response = requests.get(url=url, headers=headers, verify=False)
html = etree.HTML(response.text)
city_url = []
count = 1
while True:
    part_url = html.xpath('//*[@id="slider2"]/dt[' + str(count) + ']/a/@href')
    if part_url:
        url = 'http://qinghai.chinatax.gov.cn/' + part_url[0]
        city_url.append(url)
        count += 1
    else:
        break
