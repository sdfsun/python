# -*- coding: utf-8 -*
# @Author: 王琨
# @Date: 2021-08-09 20:39:37
# @LastEditors: 王琨
# @LastEditTime: 2021-08-19 10:57:40
# @FilePath: /pythonProject/d.py
# @Description:

import json
import re
import time

import requests

for i in range(50):
    req = requests.get('https://snapmail.cc/emailList/acokuw1@snapmail.cc')
    print(req.status_code)
    if req.status_code == 200:
        email_text = json.loads(req.text)[0]['html']
        validation_code = re.search(r'([0-9]{4})', email_text)
        print(validation_code.group(1))
        print(validation_code.group(1))

    print("Waiting for next retry")
    time.sleep(6)
