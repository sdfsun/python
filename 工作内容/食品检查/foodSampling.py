#! user/bin/env python
# -*- coding: utf-8 -*-
# @Author: 王琨
# @Date: 2021-08-20 10:03:48
# @LastEditors: 王琨
# @LastEditTime: 2021-08-20 13:48:04
# @FilePath: /python/工作内容/食品检查/foodSampling.py
# @Description: 食品抽查

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


os.environ['CUDA_DEVICE_ORDER'] = '0'

def proxy(headers):
    while True:
        proxy_url = 'http://17610040106.v4.dailiyun.com/query.txt?key=NP86444E99&word=&count=1&rand=false&ltime=0&norepeat=false&detail=false'
        response = requests.get(proxy_url, headers=headers)
        proxies = response.text.strip()
        if proxies:
            break
        else:
            time.sleep(15)
    print(proxies)
    return proxies


def getDriver(headers):
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
    options.add_argument('--proxy-server={}'.format(proxy(headers)))
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


def left_info():
    url = 'https://spcjsac.gsxt.gov.cn/'
    headers = {
        'user-agent': generate_user_agent()
    }
    desired_capabilities = DesiredCapabilities.CHROME
    desired_capabilities["pageLoadStrategy"] = "none"
    driver = getDriver(headers)
    driver.get(url)
    WebDriverWait(driver, 5).until(lambda x: x.find_element_by_xpath('//input'))
    time.sleep(1)
    driver.find_element_by_xpath('//input').send_keys('三只松鼠')
    e = driver.find_element_by_xpath('//select')
    select = Select(e)
    select.select_by_value('enterprisename')  # 下拉菜单“企业名称”
    time.sleep(1)
    driver.find_element_by_xpath('//button').click()  # 点击搜索
    WebDriverWait(driver, 15).until(lambda x: x.find_element_by_xpath('//*[@class="halfWidth"][1]//tr[@title][1]'))
    page_text = driver.find_element_by_xpath('//div[@id="pager"]//li[@class="ng-scope"][1]/span').get_attribute(
        'textContent')
    page_num = str(re.findall(r'共(.+?)页', page_text))[0]
    for page in range(int(page_num)):
        for x in range(1, 11):
            driver.find_element_by_xpath('//*[@class="halfWidth"][1]//tr[@title][' + str(x) + ']').click()
            handles = driver.window_handles
            driver.switch_to.window(handles[-1])
            WebDriverWait(driver, 15).until(EC.presence_of_element_located((By.XPATH, '//*[@class="t_data"]/tr')))
            count = driver.find_element_by_xpath('//div[@class="comCon"]/span[1]').get_attribute('textContent')
            print(int(count))
            if int(count) > 10:  # 判断详情页页数
                info_page = int(count) // 10
                last_page = int(count) % 10
                for i in range(1, info_page + 1):
                    text = driver.find_element_by_xpath('//*[@class="t_data"]/tr[' + str(i) + ']').get_attribute('textContent')
                    print(text)
                driver.close()
                print(handles)
                driver.switch_to.window(handles[0])
                for last_num in range(1, last_page + 1):
                    text = driver.find_element_by_xpath('//*[@class="t_data"]/tr[' + str(i) + ']').get_attribute(
                        'textContent')
                    print(text)
                if info_page > 1:
                    for num in range(info_page):
                        driver.find_element_by_xpath('//a[contains(text(), "下一页")]').click()
                else:
                    break

            else:
                info_page = 1
                for num in range(int(count)):
                    text = driver.find_element_by_xpath('//*[@class="t_data"]/tr[' + str(num + 1) + ']').get_attribute(
                        'textContent')


left_info()
