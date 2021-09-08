#! /usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: 王琨
# @Date: 2021-08-26 11:06:59
# @LastEditors: 王琨
# @LastEditTime: 2021-08-26 11:06:59
# @FilePath: /python/工作内容/一般纳税人/hebei.py
# @Description: 河北一般纳税人查询


import requests

cookies = {
    '$Cookie: yfx_c_g_u_id_10003705': '_ck21082511031912780275474275377',
    'yfx_f_l_v_t_10003705': 'f_t_1629860599274__r_t_1629860599274__v_t_1629879325297__r_c_0',
    'yfx_c_g_u_id_10003701': '_ck21082609035317355109170220299',
    'yfx_f_l_v_t_10003701': 'f_t_1629939833729__r_t_1629939833729__v_t_1629941954287__r_c_0',
    'yfx_c_g_u_id_10000001': '_ck21082609440017697015816122312',
    'yfx_c_g_u_id_10003677': '_ck21082609440017755969334675337',
    'yfx_c_g_u_id_10000072': '_ck21082609474710681012485153110',
    'yfx_f_l_v_t_10000072': 'f_t_1629942467058__r_t_1629942467058__v_t_1629942467058__r_c_0',
    'yfx_c_g_u_id_10003721': '_ck21082609480210631428587037077',
    'yfx_f_l_v_t_10003721': 'f_t_1629942482056__r_t_1629942482056__v_t_1629942482056__r_c_0',
    'yfx_c_g_u_id_10003712': '_ck21082609481719263376555864767',
    'yfx_f_l_v_t_10003712': 'f_t_1629942497920__r_t_1629942497920__v_t_1629942497920__r_c_0',
    '_gscu_1371427157': '29942650y15ns313',
    '_gscbrs_1371427157': '1',
    'yfx_c_g_u_id_10003139': '_ck21082609505019245183953430995',
    '_trs_uv': 'kss9rqrn_735_hkjz',
    'yfx_f_l_v_t_10003139': 'f_t_1629942650918__r_t_1629942650918__v_t_1629946830565__r_c_0',
    'TOPAPP_COOKIE': '51ca',
    'DZSWJ_TGC': 'a1c812a3b7534d6d9fd6cd2874659efd',
    '_gscs_1371427157': 't29946830vf4p5a13|pv:2',
    'yfx_f_l_v_t_10000001': 'f_t_1629942240757__r_t_1629942240757__v_t_1629947889469__r_c_0',
    'yfx_f_l_v_t_10003677': 'f_t_1629942240772__r_t_1629942240772__v_t_1629947889489__r_c_0',
    'JSESSIONID': 'QuiAisS9a2r_u5sTYxpBPEyT1SGNGUMy-wag-dnfGJnbDwqMesyH\\u00211308592729',
}

headers = {
    'Connection': 'keep-alive',
    'sec-ch-ua': '"Chromium";v="92", " Not A;Brand";v="99", "Google Chrome";v="92"',
    'Accept': 'application/json, text/javascript, */*; q=0.01',
    'X-Requested-With': 'XMLHttpRequest',
    'sec-ch-ua-mobile': '?0',
    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.159 Safari/537.36',
    'Content-Type': 'application/json; charset=UTF-8',
    'Sec-Fetch-Site': 'same-origin',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Dest': 'empty',
    'Referer': 'https://etax.hebei.chinatax.gov.cn/wszx-web/apps/views/bszy/cxybnsrrdxx.html?id=1176&code=ybnsrzgcx&_lot=1565603605381',
    'Accept-Language': 'zh-CN,zh;q=0.9',
}

params = (
    ('nsrsbh', '911301007727529744'),
    ('nsrmc', '\'\''),
    ('pictureVerificationCode', '5'),
    ('_', '1629949325684'),
)

response = requests.get('https://etax.hebei.chinatax.gov.cn/wszx-web/apps/views/bszy/cxybnsrrdxx.html?id=1176&code=ybnsrzgcx&_lot=1565603605381')

#NB. Original query string below. It seems impossible to parse and
#reproduce query strings 100% accurately so the one below is given
#in case the reproduced version is not "correct".
# response = requests.get('https://etax.hebei.chinatax.gov.cn/wszx-web/api/ggfw/cx/ybnsrzgxx?nsrsbh=911301007727529744&nsrmc=%27%27&pictureVerificationCode=5&_=1629949325684', headers=headers, cookies=cookies)
print(response.content.decode('utf-8'))
