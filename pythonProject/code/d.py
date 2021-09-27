# -*- coding: utf-8 -*
# @Author: 王琨
# @Date: 2021-08-09 20:39:37
# @LastEditors: 王琨
# @LastEditTime: 2021-08-19 10:57:40
# @FilePath: /pythonProject/d.py
# @Description:


def isPalindrome(self, x: int) -> bool:
    a = 0
    b = x
    while x != 0:
        a = a * 10 + b % 10
        b = b // 10
    if a == x:
        return True
    else:
        return False
