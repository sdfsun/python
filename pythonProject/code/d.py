# -*- coding: utf-8 -*
# @Author: 王琨
# @Date: 2021-08-09 20:39:37
# @LastEditors: 王琨
# @LastEditTime: 2021-08-19 10:57:40
# @FilePath: /pythonProject/d.py
# @Description:

import json
import random
import re
import time

import requests

for i in range(50):
    req = requests.get('https://snapmail.cc/emailList/doid@snapmail.cc')
    print(req.status_code)
    if req.status_code == 200:
        email_text = json.loads(req.text)[0]['html']
        validation_code = re.search(r'([0-9]{4})', email_text)
        print(validation_code.group(1))

    print("Waiting for next retry")
    time.sleep(6)

# second = [3, 4, 5, 7, 8][random.randint(0, 4)]
#
# # 第三位数字
# third = {
#     3: random.randint(0, 9),
#     4: [5, 7, 9][random.randint(0, 2)],
#     5: [i for i in range(10) if i != 4][random.randint(0, 8)],
#     7: [i for i in range(10) if i not in [4, 9]][random.randint(0, 7)],
#     8: random.randint(0, 9),
# }[second]
#
# # 最后八位数字
# suffix = random.randint(9999999, 100000000)
#
# # 拼接手机号
# print("1{}{}{}".format(second, third, suffix))
