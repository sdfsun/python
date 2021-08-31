#! user/bin/env python
# -*- coding: utf-8 -*-
# @Author: 王琨
# @Date: 2021-08-26 15:37:31
# @LastEditors: 王琨
# @LastEditTime: 2021-08-26 15:37:31
# @FilePath: /python/工作内容/一般纳税人/大连验证码图片爬取.py
# @Description: 

import requests
import time
import requests
from user_agent import generate_user_agent


for i in range(1):
    headers = {
        'user-agent': generate_user_agent()
    }
    params = (
        ('time', str(int(time.time())*1000)),
    )
    url = 'https://etax.fujian.chinatax.gov.cn/tycx-cjpt-web/cxptGz/builderCaptcha.do?t=1630286668045'
    res = requests.get(url=url, headers=headers, params=params)
    print(res.status_code)
    name = str(i) + '.jpg'
    with open('/home/kerwin/Dev/字母验证码/' + name, 'wb') as f:
        f.write(res.content)
    time.sleep(1)
