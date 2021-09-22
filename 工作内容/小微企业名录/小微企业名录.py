# -*- coding: utf-8 -*-
# @Author            : 王琨
# @Email             : 18410065868@163.com
# @Date              : 2021-06-16 10:10:45
# @Last Modified by  : 王琨
# @Last Modified time: 2021-06-23 16:46:25
# @File Path         : D:\Dev\pythonProject\小微企业名录.py
# @Project Name      : pythonProject
# @Description       : 

import time

import ipdb
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.support import expected_conditions as EC
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
    options.add_argument('--user-agent={}'.format(generate_user_agent()))
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

    return browser


def main():
    desired_capabilities = DesiredCapabilities.CHROME
    desired_capabilities["pageLoadStrategy"] = "none"
    driver = getDriver()

    url = 'http://xwqy.gsxt.gov.cn/'
    driver.get(url=url)

    # 点击“小微企业库”
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//span[contains(text(), "小微企业库")]')))
    driver.find_element_by_xpath('//div[2]/ul/li[5]/a/span').click()
    time.sleep(5)

    # 输入企业名称
    value = '华为技术有限公司'
    driver.find_element_by_id('searchtitle').send_keys(value)
    driver.find_element_by_class_name('search_btn').click()  # 点击搜索

    driver.find_element_by_xpath('//td[@class="td_cc"]/a').click()
    handles = driver.window_handles
    driver.switch_to.window(handles[-1])
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME, 'main_con')))
    test = driver.find_element_by_xpath('//div[@class="main_con"]').get_attribute('textContent')

    print(test)
    driver.quit()


if __name__ == '__main__':
    main()
