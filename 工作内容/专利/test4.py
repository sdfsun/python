import requests

def get_proxies():
    headers ={
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; ) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/82.0.4068.4 Safari/537.36'
    }
    url='http://17610040106.v4.dailiyun.com/query.txt?key=NP86444E99&word=&count=1&rand=false&ltime=0&norepeat=false&detail=false'
    response = requests.get(url,headers=headers)
    proxy_dly = response.text.strip()
    if proxy_dly:
        proxies = {
          "http": "http://" + proxy_dly,
          "https": "http://" + proxy_dly
        }
        return proxies

cookies = {
    'UM_distinctid': '17abc692f8239e-077a01c3f8f03a-574a2418-144000-17abc692f8365a',
    'ASP.NET_SessionId': 'dvbezpbv1ghobwabqolkkiml',
    'MobilePhone': '18731341598',
    'LoginName': '18731341598',
    'CNZZDATA1275790483': '896244566-1626657114-%7C1626761060',
}

headers = {
    'Connection': 'keep-alive',
    'Pragma': 'no-cache',
    'Cache-Control': 'no-cache',
    'sec-ch-ua': '"Google Chrome";v="89", "Chromium";v="89", ";Not A Brand";v="99"',
    'Accept': 'application/json, text/javascript, */*; q=0.01',
    'X-Requested-With': 'XMLHttpRequest',
    'sec-ch-ua-mobile': '?0',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.72 Safari/537.36',
    'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
    'Origin': 'https://cprs.patentstar.com.cn',
    'Sec-Fetch-Site': 'same-origin',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Dest': 'empty',
    'Referer': 'https://cprs.patentstar.com.cn/Search/ResultList?CurrentQuery=KEDljY7kuLrmioDmnK/mnInpmZDlhazlj7gvUEEp&type=cn',
    'Accept-Language': 'zh-CN,zh;q=0.9',
}

data = {
  'CurrentQuery': 'F XX (@\u534E\u4E3A\u6280\u672F\u6709\u9650\u516C\u53F8/PA)',
  'OrderBy': 'AD',
  'OrderByType': 'DESC',
  'PageNum': '1',
  'DBType': 'CN',
  'RowCount': '5',
  'Filter': '{"CO":"","PT":"","LG":""}',
  'SecSearch': '',
  'IdList': ''
}

response = requests.post('https://cprs.patentstar.com.cn/Search/SearchByQuery', headers=headers, cookies=cookies, data=data)
