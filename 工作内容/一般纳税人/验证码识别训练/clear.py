#! user/bin/env python
# -*- coding: utf-8 -*-
# @Author: 王琨
# @Date: 2021-08-26 16:24:47
# @LastEditors: 王琨
# @LastEditTime: 2021-08-26 16:46:52
# @FilePath: /python/工作内容/一般纳税人/大连验证码识别训练/clear.py
# @Description: 去除验证码噪点


from PIL import Image

img = Image.open('../验证码图片/hubei_identifier.png').convert('RGB')

img_array = img.load()
print(img_array)
width = img.size[0]
height = img.size[1]
for x in range(0, width):
    for y in range(0, height):
        data = img.getpixel((x, y))
        print(data)
        if data[0] <= 30 and data[1] <= 30 and data[2] <= 30:
            img.putpixel((x, y), (255, 255, 255))
img = img.convert('RGB')

img.save('0.png')
