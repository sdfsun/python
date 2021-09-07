#!user/bin/env python
# -*- coding: utf-8 -*-
# @Author: 王琨
# @Date: 2021-08-26 16:24:47
# @LastEditors: 王琨
# @LastEditTime: 2021-09-02 14:09:40
# @FilePath: /python/工作内容/一般纳税人/验证码识别训练/clear.py
# @Description: 去除验证码噪点


import cv2
import numpy as np


def clamp(pv):
    if pv > 255:
        return 255
    if pv < 0:
        return 0
    else:
        return pv


def gaussian_noise(image):
    h, w, c = image.shape
    for row in range(h):
        for col in range(w):
            s = np.random.normal(0, 20, 3)
            b = image[row, col, 0]
            g = image[row, col, 1]
            r = image[row, col, 2]
            image[row, col, 0] = clamp(b + s[0])
            image[row, col, 1] = clamp(g + s[1])
            image[row, col, 2] = clamp(r + s[2])
    cv2.imshow('noise image', image)


src = cv2.imread('../验证码图片/qingdao_identifier.png')
cv2.imshow('input_image', src)

gaussian_noise(src)
dst = cv2.GaussianBlur(src, (15, 15), 0)
cv2.imshow('Gaussian_blur2', dst)
cv2.waitKey(0)
cv2.destroyAllWindows()
