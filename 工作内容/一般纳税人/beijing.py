#! /usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: 王琨
# @Date: 2021-08-26 10:04:29
# @LastEditors: 王琨
# @LastEditTime: 2021-08-26 10:04:44
# @FilePath: /python/工作内容/一般纳税人/beijing.py
# @Description: 北京一般纳税人查询 可以直接拼接URL访问

import requests
from user_agent import generate_user_agent
from lxml import etree


def main(identifier):
    part_url = 'http://etax.beijing.chinatax.gov.cn/WSBST/bsdt/swdjzcx/queryto.jsp?nsrsbh='

    url = part_url + identifier
    Dict = {}
    headers = {
        'user-agent': generate_user_agent(),
    }

    res = requests.get(url=url, headers=headers)
    html = etree.HTML(res.text)
    for i in range(1, 11):
        key = html.xpath('//table//tr[' + str(i) + ']/td[1]//text()')[0]
        value = html.xpath('//table//tr[' + str(i) + ']/td[2]//text()')[-1]
        Dict[key] = value
    if '非' in Dict['增值税纳税人类别 ：']:
        print('否')
    else:
        print('是')


if __name__ == '__main__':
    ID = '91110105MA005AEF36'
    main(ID)
