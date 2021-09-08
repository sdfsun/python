#! user/bin/env python
# -*- coding: utf-8 -*-
# @Author: 王琨
# @Date: 2021-08-20 13:54:33
# @LastEditors: 王琨
# @LastEditTime: 2021-08-20 13:54:33
# @FilePath: /python/test/test_foodSampling.py
# @Description: 

import requests
from user_agent import generate_user_agent
from lxml import etree
import time
headers = {
        'Connection': 'close',
        'user-agent': generate_user_agent()
    }
res = requests.get('https://etax.ningbo.chinatax.gov.cn/yhs-web/api/yhsyzm/get?1631008417224', headers=headers, )
print(res.status_code)
with open('./src.jpg', 'wb') as f:
    f.write(res.content)
