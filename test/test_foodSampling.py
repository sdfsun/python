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

url = 'https://spcjsac.gsxt.gov.cn/'
headers = {
    'user-agent': generate_user_agent(),
    'Connection': 'close'
}
