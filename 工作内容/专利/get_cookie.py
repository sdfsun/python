# -*- coding: utf-8 -*-
# @Author: 王琨
# @Date: 2021-10-20 13:43:29
# @Descripttion:

import json
import random
import re
import string
import time

import cv2 as cv
import muggle_ocr
import pysnooper
import pytesseract
import requests
from PIL import Image
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver import DesiredCapabilities
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from user_agent import generate_user_agent


def getDriver():
    options = webdriver.ChromeOptions()
    options.add_argument("--disable-extensions")
    options.add_argument("--disable-gpu")
    options.add_experimental_option('excludeSwitches', ['enable-automation'])
    options.add_argument("--disable-blink-features=AutomationControlled")
    # options.add_argument('--headless')  # 无界面形式
    options.add_argument('--no-sandbox')  # 取消沙盒模式
    options.add_argument('--disable-setuid-sandbox')
    # options.add_experimental_option('useAutomationExtension', False)
    options.add_argument('--incognito')  # 启动进入隐身模式
    options.add_argument('--lang=zh-CN')  # 设置语言为简体中文
    options.add_argument('--user-agent=' + generate_user_agent())
    options.add_argument('--hide-scrollbars')
    options.add_argument('--disable-bundled-ppapi-flash')
    options.add_argument('--mute-audio')
    # options.add_argument('--proxy-server={}'.format(get_proxies()))
    browser = webdriver.Chrome(options=options)
    browser.maximize_window()
    browser.execute_cdp_cmd("Network.enable", {})
    browser.execute_cdp_cmd("Network.setExtraHTTPHeaders", {"headers": {"User-Agent": "browserClientA"}})
    browser.execute_cdp_cmd('Page.addScriptToEvaluateOnNewDocument', {"source": """
        Object.defineProperty(navigator, 'webdriver', {
            get: () => undefined
            })
        """})

    return browser


def recognize_text(image):
    # 边缘保留滤波  去噪
    blur = cv.pyrMeanShiftFiltering(image, sp=8, sr=60)
    # 灰度图像
    gray = cv.cvtColor(blur, cv.COLOR_BGR2GRAY)
    # 二值化  设置阈值  自适应阈值的话 黄色的4会提取不出来
    ret, binary = cv.threshold(gray, 185, 255, cv.THRESH_BINARY_INV)
    # 逻辑运算  让背景为白色  字体为黑  便于识别
    cv.bitwise_not(binary, binary)
    # 识别
    test_message = Image.fromarray(binary)
    text = pytesseract.image_to_string(test_message)
    text = re.findall('\d+', text)
    text = ''.join(text)
    print(text)
    return text


def main():
    List = []
    info = dict()
    url = 'http://123.233.113.66:8060/pubsearch/portal/uilogin-forwardLogin.shtml'
    with open('./data/userinfo.json') as f:
        userinfo = json.load(f)

    for username in userinfo.keys():
        password = userinfo[username]
        driver = getDriver()
        driver.get(url)
        WebDriverWait(driver, 10).until(lambda x: x.find_element(By.XPATH, '//*[@id="j_username"]'))
        while True:
            name = driver.find_element(By.XPATH, '//*[@id="j_username"]')
            name.click()
            time.sleep(1)
            name.send_keys(username)  # 输入用户名
            word = driver.find_element(By.XPATH, '//*[@id="j_password_show"]')
            word.click()
            time.sleep(1)
            word.send_keys(password)  # 输入用户密码

            img = driver.find_element(By.XPATH, '//*[@id="codePic"]')
            driver.save_screenshot('./data/full.png')
            left = img.location['x']
            top = img.location['y']
            right = img.location['x'] + img.size['width']
            bottom = img.location['y'] + img.size['height']
            im = Image.open('./data/full.png')
            im = im.crop((left, top, right, bottom))
            im.save('./data/cut.png')
            # with open('./cut.png', 'rb') as f:
            #     image = f.read()
            # sdk = muggle_ocr.SDK(model_type=muggle_ocr.ModelType.Captcha)
            # text = sdk.predict(image_bytes=image)
            src = cv.imread(r'./data/cut.png')
            text = recognize_text(src)
            driver.find_element(By.XPATH, '//*[@id="j_validation_code"]').send_keys(text)
            driver.find_element(By.XPATH, '//*[@id="loginForm"]/div[5]/a').click()
            time.sleep(5)
            try:
                driver.find_element(By.XPATH, '//*[@i="button"]').click()
                driver.find_element(By.XPATH, '//*[@id="j_username"]').clear()
                driver.find_element(By.XPATH, '//*[@id="j_password_show"]').clear()
                driver.find_element(By.XPATH, '//*[@id="codePic"]').click()
                continue
            except Exception as e:
                print(e)
                break
        cookies = driver.get_cookies()
        JSESSIONID = cookies[2]['value']
        List.append(JSESSIONID)
        time.sleep(1)
        driver.quit()
        info['JSESSIONID'] = List
        with open('./data/test.json', 'w') as s:
            json.dump(info, s)


if __name__ == '__main__':
    main()
