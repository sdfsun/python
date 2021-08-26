#! user/bin/env python
# -*- coding: utf-8 -*-
# @Author: 王琨
# @Date: 2021-08-26 15:37:31
# @LastEditors: 王琨
# @LastEditTime: 2021-08-26 15:37:31
# @FilePath: /python/工作内容/一般纳税人/大连验证码图片爬取.py
# @Description: 

import requests
import random
import time

for i in range(5000):
    if i % 100 == 0:
        time.sleep(2)
    url = 'https://etax.dalian.chinatax.gov.cn/dlts/gx/imgCode?r=' + str(random.random())
    res = requests.get(url)
    name = str(i) + '.jpg'
    with open('./大连验证码图片/' + name, 'wb') as f:
        f.write(res.content)
