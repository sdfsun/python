# -*- coding: utf-8 -*
# @Author: 王琨
# @Date: 2021-08-09 20:39:37
# @LastEditors: 王琨
# @LastEditTime: 2021-08-19 10:57:40
# @FilePath: /pythonProject/d.py
# @Description:


import requests
from user_agent import generate_user_agent
headers = {
        'Connection': 'close',
        'user-agent': generate_user_agent()
    }
for i in range(10000):
    res = requests.get('https://etax.ningbo.chinatax.gov.cn/yhs-web/api/yhsyzm/get?1631008417224', headers=headers, )
    print(res.status_code)
    with open('./' + str(i) + '.jpg', 'wb') as f:
        f.write(res.content)
