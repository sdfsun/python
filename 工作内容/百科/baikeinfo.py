#! user/bin/env python
# -*- coding: utf-8 -*-
# @Author: 王琨
# @Date: 2021-08-09 20:39:37
# @LastEditors: 王琨
# @LastEditTime: 2021-08-20 10:18:30
# @FilePath: /python/工作内容/baike/baikeinfo.py
# @Description: 百度百科

import requests
from urllib.parse import quote
from lxml import etree
from user_agent import generate_user_agent


def query(cont):
    url = 'https://baike.baidu.com/item/' + quote(cont)

    headers = {
        'User-Agent': generate_user_agent()
    }
    response = requests.get(url=url, headers=headers)
    html = etree.HTML(response.text)
    introduction = html.xpath('//*[@class="lemma-summary"]//text()')
    name = html.xpath('//*[@class="basicInfo-item name"]/text()')
    value = html.xpath('//*[@class="basicInfo-item value"]/text()')

    return introduction, name, value


if __name__ == '__main__':
    content = '华为技术有限公司'
    result = query(content)
    print(result)
