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
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

import getDriver

driver = getDriver.getDriver()

url = 'http://xwqy.gsxt.gov.cn/'
driver.get(url=url)

WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//span[contains(text(), "小微企业库")]')))
driver.find_element_by_xpath('//span[contains(text(), "小微企业库")]').click()
time.sleep(5)

value = input('请输入公司名：')
driver.find_element_by_id('searchtitle').send_keys(value)
driver.find_element_by_class_name('search_btn').click()
ipdb.set_trace()

driver.find_element_by_xpath('//td[@class="td_cc"]/a').click()
handles = driver.window_handles
driver.switch_to.window(handles[-1])
WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME, 'main_con')))
test = driver.find_element_by_xpath('//div[@class="main_con"]').get_attribute('textContent')

print(test)
driver.quit()