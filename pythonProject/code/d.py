# -*- coding: utf-8 -*
# @Author: 王琨
# @Date: 2021-08-09 20:39:37
# @LastEditors: 王琨
# @LastEditTime: 2021-08-19 10:57:40
# @FilePath: /pythonProject/d.py
# @Description:


import multiprocessing
import time
import random
import asyncio
from user_agent import generate_user_agent
from pyppeteer import browser, launch


async def run():
    url = 'https://cn.bing.com/search?q=python%e5%90%af%e5%8a%a8%e8%84%9a%e6%9c%ac&qs=HS&pq=python%e5%90%af%e5%8a%a8%e8%84%9a&sc=1-9&cvid=76A8C098B4534F058F5994FDC9CEFEF5&FORM=QBRE&sp=1'
    page = await browser.newPage()
    await page.setJavaScriptEnabled(enabled=False)
    await page.evaluateOnNewDocument('Object.defineProperty(navigator,"webdriver", {get: () => undefined})')
    await page.goto(url, timeout=10000000)
    await asyncio.sleep(10)
    res = await page.content()
    print(res)


async def main():
    global browser
    browser = await launch(headless=False, ignoreHTTPSErrors=True, dumpio=True, args=["--disable-infobars", "--start-maximized", "--no-sandbox", "--user-agent={}".format(generate_user_agent())])
    await asyncio.gather(*[run() for _ in range(5)])
    await browser.close()

asyncio.run(main())
