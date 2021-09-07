#!user/bin/env python
# -*- coding: utf-8 -*-
# @Author: 王琨
# @Date: 2021-09-01 14:50:22
# @LastEditors: 王琨
# @LastEditTime: 2021-09-01 14:50:22
# @FilePath: /python/工作内容/一般纳税人/验证码识别训练/get_picture.py
# @Description: image下载

from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains
from user_agent import generate_user_agent
import time
from PIL import Image


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
    # options.add_argument('--proxy-server={}'.format(proxy(headers)))
    browser = webdriver.Chrome(options=options)
    browser.maximize_window()
    browser.execute_cdp_cmd("Network.enable", {})
    browser.execute_cdp_cmd("Network.setExtraHTTPHeaders", {"headers": {"User-Agent": "browserClientA"}})
    browser.execute_cdp_cmd('Page.addScriptToEvaluateOnNewDocument', {"source": """
        Object.defineProperty(navigator, 'webdriver', {
            get: () => undefined
            })
        """})
    # with open('stealth.min.js') as f:
    #     js = f.read()
    # browser.execute_cdp_cmd("Page.addScriptToEvaluateOnNewDocument", {
    #     "source": js
    # })
    # browser.implicitly_wait(10)

    return browser


def main():
    url = 'https://etax.jiangsu.chinatax.gov.cn/jx/commonquery/20181203/3440.html'
    driver = getDriver()
    driver.get(url)
    WebDriverWait(driver, 10).until(lambda x: x.find_element_by_xpath('//*[@id="mainFrame"]'))

    # 获取iframe位置
    iframe_ele = driver.find_element_by_xpath('//*[@id="mainFrame"]')
    x = iframe_ele.location['x']
    y = iframe_ele.location['y']

    # 切换到iframe中
    driver.switch_to.frame('mainFrame')
    time.sleep(3)

    # 定位元素
    ele = driver.find_element_by_xpath('//*[@class="yidun_tips__text yidun-fallback__tip"]')
    # 执行鼠标悬停
    ActionChains(driver).move_to_element(ele).perform()
    time.sleep(5)
    # 定位验证码在iframe中的坐标
    element = driver.find_element_by_xpath('//*[@class="yidun_bg-img"]')
    # 真实坐标需要加上iframe的坐标
    left = element.location['x'] + x
    top = element.location['y'] + y
    right = element.location['x'] + element.size['width'] + x
    bottom = element.location['y'] + element.size['height'] + y

    for i in range(1000):
        driver.save_screenshot('./jiangsu_picture.png')  # 全屏截图
        im = Image.open('./jiangsu_picture.png')
        im = im.crop((left, top, right, bottom))
        im.save('/home/kerwin/Dev/image/' + str(i) + '.png')
        driver.find_element_by_xpath('//*[@class="yidun_refresh"]').click()
        time.sleep(3)


if __name__ == '__main__':
    main()
