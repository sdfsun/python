# -*- coding: utf-8 -*-
# @Time : 2021/7/7-17:43
# @Author : Warren
# @Email : 18410065868@163.com
# @File : trademark_req.py
# @Project : pythonProject
# @Description : 使用requests请求

import requests
import time
from lxml import etree
from user_agent import generate_user_agent

headers = {
    'user-agent': generate_user_agent()
}

url = 'http://wcjs.sbj.cnipa.gov.cn/txnRead01.do?NPxosaad=qAq3qarE1lfE1lfE1rSi_rYyDSzQi78ETIdsFdmNZ7aqqtmUaNf_qAqq1q'

response = requests.get(url=url, headers=headers)
with open('x.html', 'w') as f:
    f.write(response.content.decode('utf-85'))

