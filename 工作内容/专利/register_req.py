# -*- coding: utf-8 -*-
# @Author: 王琨
# @Date: 2021-10-21 10:58:32
# @Descripttion:

import random
import string

import requests


def get_proxies():
    ip_url = "http://152.136.208.143:5000/w/ip/random"
    proxies = requests.get(ip_url, headers={'User-Agent': 'Mozilla/5.0'}).json()
    print(proxies['http'])
    return proxies['http']


def create_phone():
    # 第二位数字
    second = [3, 4, 5, 7, 8][random.randint(0, 4)]

    # 第三位数字
    third = {
        3: random.randint(0, 9),
        4: [5, 7, 9][random.randint(0, 2)],
        5: [i for i in range(10) if i != 4][random.randint(0, 8)],
        7: [i for i in range(10) if i not in [4, 9]][random.randint(0, 7)],
        8: random.randint(0, 9),
    }[second]

    # 最后八位数字
    suffix = random.randint(9999999, 100000000)

    # 拼接手机号
    return "1{}{}{}".format(second, third, suffix)


def main():
    char_A = string.ascii_uppercase
    char_a = string.ascii_lowercase
    char_n = string.digits
    char_t = '~!@#$%^&*()'
    username_n = random.randint(4, 19)
    password_n = random.randint(12, 19)
    username_l = []
    password_l = []
    for i_1 in range(username_n // 2):
        username_l.append(random.choice(string.ascii_letters))
    if random.randint(0, 1) == 1:
        username_l.append('_')
    for i_2 in range(username_n // 2, username_n):
        username_l.append(random.choice(char_n))

    for j_1 in range(password_n // 4 * 1):
        password_l.append(random.choice(char_A))
    for j_2 in range(password_n // 4 * 1, password_n // 4 * 2):
        password_l.append(random.choice(char_a))
    for j_3 in range(password_n // 4 * 2, password_n // 4 * 3):
        password_l.append(random.choice(char_n))
    for j_4 in range(password_n // 4 * 3, password_n):
        password_l.append(random.choice(char_t))
    username = ''.join(username_l)  # 用户名
    password = ''.join(password_l)  # 密码

    headers = {
        'Connection': 'keep-alive',
        'Accept': '*/*',
        'X-Requested-With': 'XMLHttpRequest',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.81 Safari/537.36 Edg/94.0.992.50',
        'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
        'Origin': 'http://123.233.113.66:8060',
        'Referer': 'http://123.233.113.66:8060/pubsearch/portal/uiregister-showRegisterPage.shtml',
        'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6',
    }

    data_username = {
        'userNameForCheck': username
    }
    proxies = {
        'http': get_proxies()
    }
    preExecuteSearch = 'http://123.233.113.66:8060/pubsearch/patentsearch/preExecuteSearch!preExecuteSearch.do'
    s = requests.session()
    cookies = s.post(url=preExecuteSearch, headers=headers, proxies=proxies, verify=False)
    print(cookies.cookies, cookies.text)


if __name__ == "__main__":
    main()
