# -*- coding: utf-8 -*-
# @Author: 王琨
# @Date: 2021-07-26 09:31:49
# @Description: pyppeteer

import asyncio
import csv
import time

import nest_asyncio
import requests
from lxml import etree
from pyppeteer import errors, launch
from user_agent import generate_user_agent

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
    count = '华为技术有限公司'  # 初始申请人
    # browser = await launch(headless=False, args=['--proxy-server={}'.format(ip), '--disable-infobars', '--no-sandbox'], userDataDir='./Temporary')
    browser = await launch(headless=False, args=['--disable-infobars', '--no-sandbox'], userDataDir='./Temporary')
    page1 = await browser.newPage()
    # await stealth(page)
    # await page.setViewport({'width': width, 'height': height})
    await page1.setUserAgent(generate_user_agent())
    await page1.setJavaScriptEnabled(True)

    await page1.goto('http://sbj.cnipa.gov.cn/', timeout=90000)  # 打开网址，设定超时时间
    await asyncio.sleep(10)
    await (await page1.xpath('//*[@class="bscont2 bscont"]//a'))[0].click()  # 点击“商标网上查询”

    await asyncio.sleep(5)
    page_list = await browser.pages()  # 切换焦点网页
    page2 = page_list[-1]
    await (await page2.xpath('//div[@class="TRS_Editor"]//img'))[0].click()  # 我接受

    await page2.waitForNavigation({'timeout': 50000})
    await page2.click('.icon_box>[src="/tmrp/images/icon2.png"]')  # 点击商标综合查询xx
    await asyncio.sleep(5)
    try:
        await page2.type('[name="request:hnc"]', count)  # 输入注册号
        await asyncio.sleep(2)
        await page2.click('#_searchButton')  # 点击查询按钮
        await asyncio.sleep(5)
        page_list = await browser.pages()
        print(page_list)
        page3 = page_list[-1]
        while True:
            await page3.waitForXPath('//tr[@class="ng-scope"]/td', timeout=90000)
            # 获取网页内容并提取数据
            text = await page3.content()
            html = etree.HTML(text)
            for i in range(1, 51):
                img = html.xpath('//tr[@class="ng-scope"][' + str(i) + ']//input/@img')
                info = html.xpath('//tr[@class="ng-scope"][' + str(i) + ']/td//text()')
                if img:  # 将获取到的数据写入文件
                    with open('img.csv', 'a', newline='') as s:
                        s_csv = csv.writer(s)
                        s_csv.writerow(img)
                    with open('info.csv', 'a', newline='') as f:
                        f_csv = csv.writer(f)
                        f_csv.writerow(info)
            await page3.click('#mGrid_listGrid_paginator_0 > ul > li.nextPage > a')  # 点击下一页
            await asyncio.sleep(15)

    except Exception as e:
        print(e)
        await browser.close()


if __name__ == '__main__':
    asyncio.run(run())
