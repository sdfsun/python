#! user/bin/env python
# -*- coding: utf-8 -*-
# @Author: 王琨
# @Date: 2021-08-26 14:28:57
# @LastEditors: 王琨
# @LastEditTime: 2021-08-26 14:29:51
# @FilePath: /python/工作内容/一般纳税人/山西.py
# @Description: 山西  滑动验证码 未完成


from selenium.common.exceptions import NoSuchElementException
from selenium import webdriver
from selenium.webdriver import DesiredCapabilities
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.select import Select
from user_agent import generate_user_agent
import requests
import time
import re
import os
from PIL import Image
import muggle_ocr


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
    options.add_argument(
        '--user-agent=' + generate_user_agent())
    options.add_argument('--hide-scrollbars')
    options.add_argument('--disable-bundled-ppapi-flash')
    options.add_argument('--mute-audio')
    # options.add_argument('--proxy-server={}'.format(proxy(headers)))
    browser = webdriver.Chrome(options=options)
    browser.execute_cdp_cmd("Network.enable", {})
    browser.execute_cdp_cmd("Network.setExtraHTTPHeaders", {"headers": {"User-Agent": "browserClientA"}})
    browser.execute_cdp_cmd('Page.addScriptToEvaluateOnNewDocument', {
        "source": """
        Object.defineProperty(navigator, 'webdriver', {
            get: () => undefined
            })
        """
    })

    return browser


def main(identifier):
    desired_capabilities = DesiredCapabilities.CHROME
    desired_capabilities["pageLoadStrategy"] = "none"
    url = 'https://etax.shanxi.chinatax.gov.cn/gzfw/nsrzg'
    driver = getDriver()
    driver.get(url)
    WebDriverWait(driver, 10).until(lambda x: x.find_element_by_xpath('//*[@id="NSR"]'))
    driver.find_element_by_xpath('//*[@id="NSR"]').send_keys(identifier)
    time.sleep(2)
    driver.find_element_by_xpath('//div[@class="search-form-column"]/button').click()

    driver.save_screenshot('./验证码图片/shanxi_picture.png')
    element = driver.find_element_by_xpath('//img[@class="backImg"]')
    print(element.location)
    print(element.size)
    # 真实坐标需要加上iframe的坐标
    left = element.location['x']
    top = element.location['y']
    right = element.location['x'] + element.size['width']
    bottom = element.location['y'] + element.size['height']
    im = Image.open('./验证码图片/shanxi_picture.png')
    im = im.crop((left, top, right, bottom))
    im.save('./验证码图片/shanxi_identifier.png')
    time.sleep(5)


if __name__ == '__main__':
    ID = '911400001123599660'
    main(ID)
