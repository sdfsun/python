#!user/bin/env python
# -*- coding: utf-8 -*-
# @Author: 王琨
# @Date: 2021-07-26 09:31:49
# @LastEditTime: 2021-08-19 14:30:16
# @LastEditors: 王琨
# @FilePath: /pythonProject/Tradmark_Check_pyp.py
# @Description: pyppeteer

import asyncio
from pyppeteer import errors
from pyppeteer import launch
from user_agent import generate_user_agent
import nest_asyncio
import requests
import time
import csv
from lxml import etree


# from pyppeteer_stealth import stealth

nest_asyncio.apply()

# width = 1920w
# height = 1080


# 获取代理IP
def proxy():
    headers = {'User-Agent': generate_user_agent()}
    while True:
        proxy_url = 'http://17610040106.v4.dailiyun.com/query.txt?key=NP86444E99&word=&count=1&rand=false&ltime=0&norepeat=false&detail=false'
        response = requests.get(proxy_url, headers=headers)
        proxies = response.text.strip()
        if proxies:
            break
        else:
            time.sleep(15)
    return proxies


# 主函数
async def run():
    count = 809828  # 初始申请号
    proxies = 0
    while True:
        ip = proxy()
        if proxies == ip:  # 判断代理IP是否变化
            time.sleep(15)
            continue
        else:
            proxies = ip
        browser = await launch(headless=False, args=['--proxy-server={}'.format(ip), '--disable-infobars', '--no-sandbox'], userDataDir='../Temporary')
        page1 = await browser.newPage()
        # await stealth(page)
        # await page.setViewport({'width': width, 'height': height})
        await page1.setUserAgent(generate_user_agent())
        await page1.setJavaScriptEnabled(True)

        await page1.goto('http://wcjs.sbj.cnipa.gov.cn/txnT01.do', timeout=90000)  # 打开网址，设定超时时间
        # await asyncio.sleep(10)
        # await (await page1.xpath('//*[@class="bscont2 bscont"]//a'))[0].click()  # 点击“商标网上查询”
        #
        # await asyncio.sleep(5)
        # page_list = await browser.pages()  # 切换焦点网页
        # page2 = page_list[-1]
        # await (await page2.xpath('//div[@class="TRS_Editor"]//img'))[0].click()  # 我接受
        #
        # await page2.waitForNavigation({'timeout': 50000})
        # await page2.click('.icon_box>[src="/tmrp/images/icon2.png"]')  # 点击商标综合查询
        # await asyncio.sleep(5)
        # try:  # 通过注册号循环查询
        #     await page2.type('[name="request:sn"]', str(count))  # 输入注册号
        #     await asyncio.sleep(2)
        #     await page2.click('#_searchButton')  # 点击查询按钮
        #     await asyncio.sleep(5)
        #     page_list = await browser.pages()
        #     print(page_list)
        #     page3 = page_list[-1]
        #     await page3.waitForXPath('//tr[@class="ng-scope"]/td', timeout=90000)
        #     # 获取网页内容并提取数据
        #     text = await page3.content()
        #     html = etree.HTML(text)
        #     img = html.xpath('//tr[@class="ng-scope"]//input/@img')
        #     info = html.xpath('//tr[@class="ng-scope"]/td//text()')
        #     if img:  # 将获取到的数据写入文件
        #         with open('img.csv', 'a', newline='') as i:
        #             i_csv = csv.writer(i)
        #             i_csv.writerow(img)
        #         with open('info.csv', 'a', newline='') as f:
        #             f_csv = csv.writer(f)
        #             f_csv.writerow(info)
        #     await page3.close()
        #     count += 1
        #     while True:
        #         try:
        #             await page2.evaluate('document.querySelector("[name="request:sn"]").value=""')
        #             # await page2.click('[name="request:sn"]')
        #             # # await page2.keyboard.press('end')
        #             # await page2.keyboard.down('Shift')
        #             # for i in range(len(str(count))):
        #             #     await page2.keyboard.press('ArrowLeft')
        #             # await page2.keyboard.up('Shift')
        #             # await page2.keyboard.press('Backspace')
        #             await page2.type('[name="request:sn"]', str(count))
        #             await page2.click('#_searchButton')
        #             await asyncio.sleep(5)
        #             page_list = await browser.pages()
        #             page3 = page_list[-1]
        #             try:
        #                 await page3.waitForXPath('//tr[@class="ng-scope"]/td')
        #                 text = await page3.content()
        #                 html = etree.HTML(text)
        #                 img = html.xpath('//tr[@class="ng-scope"]//input/@img')
        #                 info = html.xpath('//tr[@class="ng-scope"]/td//text()')
        #                 print(img, info)
        #                 if img:
        #                     with open('img.csv', 'a', newline='') as i:
        #                         i_csv = csv.writer(i)
        #                         i_csv.writerow(img)
        #                     with open('info.csv', 'a', newline='') as f:
        #                         f_csv = csv.writer(f)
        #                         f_csv.writerow(info)
        #
        #             except:
        #                 text = await page3.content()
        #                 if '出错啦!' or '互联网' in text:
        #                     break
        #             await page3.close()
        #             await asyncio.sleep(2)
        #             count += 1
        #         except errors:
        #             await page3.close()
        #             continue
        #
        # except:
        #     await browser.close()
        #     continue


if __name__ == '__main__':
    asyncio.run(run())
