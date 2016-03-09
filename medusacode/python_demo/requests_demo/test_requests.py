#!/usr/bin/env python
# coding:utf-8

import requests
from pprint import pprint
import datetime

HOTEL_SERVICE_HOST = 'X.X.X.X'
HOTEL_SERVICE_PORT = 7777

URL = 'http://%s:%d' % (HOTEL_SERVICE_HOST, HOTEL_SERVICE_PORT)
URL_ihotel_regions = URL+'/ihotel/regions'
URL_ihotel_list = URL+'/ihotel/list'
URL_ihotel_detail = URL+'/ihotel/detail'

# ------------------------------------------------------------------------------------------
# r = requests.get('http://www.baidu.com')
# print r
# print r.url
# print r.history
# print r.status_code
# print r.headers
# print r.encoding
# print r.cookies
# print r.text
# print r.json()
# ------------------------------------------------------------------------------------------
# data = {'regionId': 6046393,
#         'checkInDate': datetime.datetime.now().strftime('%Y-%m-%d'),
#         'checkOutDate': (datetime.datetime.now()+datetime.timedelta(days=1)).strftime('%Y-%m-%d')}
# print data
#
# # r = requests.get('http://www.baidu.com')
# # r = requests.get(URL_ihotel_list, data)
# r = requests.get(URL_ihotel_list, params=data)
#
# print r
# print r.status_code
# print r.headers
# print r.url
# print r.encoding
# print type(r.text), r.text
# print type(r.json()), r.json()
# print type(r.content), r.content
# print type(r.raw), r.raw
# print type(r.cookies), r.cookies
# ------------------------------------------------------------------------------------------
"""
requests 标准使用方法
"""
data = {'regionId': 6046393,
        'checkInDate': datetime.datetime.now().strftime('%Y-%m-%d'),
        'checkOutDate': (datetime.datetime.now()+datetime.timedelta(days=1)).strftime('%Y-%m-%d')}

request = requests.Request(method='GET',
                           url=URL_ihotel_list,
                           params=data)
prepared_request = request.prepare()
print prepared_request
# <PreparedRequest [GET]>
print prepared_request.url
# http://54.223.149.193:7777/ihotel/list?checkInDate=2015-07-31&regionId=6046393&checkOutDate=2015-08-01

session = requests.Session()
print session
# <requests.sessions.Session object at 0x108ec3790>
response = session.send(prepared_request)
print response
# <Response [200]>
print response.json()
# ------------------------------------------------------------------------------------------
