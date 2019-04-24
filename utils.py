# coding:utf-8
#__author__ = 'YuQiangYONG'
import time
import logging
import requests
import json
from random import choice
from datetime import  datetime


#create logger
logger_name = "Quanr"
logger_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
logger = logging.getLogger(logger_name)
logger.setLevel(logging.DEBUG)
logging.basicConfig(filename='Quanr%s.log' % logger_time, level=logging.INFO)


def clock(func):
    '''
    用来计算爬虫耗时的装饰器
    :param funct:
    :return:
    '''
    def clocked(*args, **kwargs):
        t0 = time.perf_counter()
        result = func(*args, **kwargs)
        elapsed = time.perf_counter() - t0
        print('%s消耗%s秒' % (func, str(elapsed - t0)))
        return result
    return clocked


def get_ip():
    """
    return a ip
    :return:
    """
    ips=[
        {"host": "1.196.158.160", "port": "23064", "country_cn": "中国", "province_cn": "河南", "city_cn": "南阳"},
        {"host": "171.12.165.221", "port": "35656", "country_cn": "中国", "province_cn": "河南", "city_cn": "漯河"},
        {"host": "116.209.142.178", "port": "24393", "country_cn": "中国", "province_cn": "湖北", "city_cn": "黄冈"},
        {"host": "183.163.46.44", "port": "48139", "country_cn": "中国", "province_cn": "安徽", "city_cn": "蚌埠"},
        {"host": "193.112.111.90", "port": 51187},
        {"host": "114.234.200.53", "port": "48374", "country_cn": "中国", "province_cn": "江苏", "city_cn": "徐州"},
        {"host": "180.104.75.28", "port": "31842", "country_cn": "中国", "province_cn": "江苏", "city_cn": "徐州"},
        {"host": "42.59.98.12", "port": "40407", "country_cn": "中国", "province_cn": "辽宁", "city_cn": "鞍山"},
        {"host": "1.180.165.55", "port": "38476", "country_cn": "中国", "province_cn": "内蒙古", "city_cn": "乌兰察布"},
        {"host": "60.189.195.10", "port": "35185", "country_cn": "中国", "province_cn": "浙江", "city_cn": "台州"}]
    url = 'https://api.getproxylist.com/proxy'
    res = requests.get(url)
    if res.status_code == 200:
        return json.loads(res.text)
    else:
        pass


def get_agent():
    """
    return agent
    :return:
    """
    agents = ['Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:66.0) Gecko/20100101 Firefox/66.0',
              'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.103 Safari/537.36'
              "Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US) AppleWebKit/532.5 (KHTML, like Gecko) Chrome/4.0.249.0 Safari/532.5",
              "Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US) AppleWebKit/534.7 (KHTML, like Gecko) Chrome/7.0.514.0 Safari/534.7",
              "Mozilla/5.0 (Windows; U; Windows NT 6.0; en-US) AppleWebKit/534.14 (KHTML, like Gecko) Chrome/9.0.601.0 Safari/534.14",
              "Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US) AppleWebKit/534.14 (KHTML, like Gecko) Chrome/10.0.601.0 Safari/534.14",
              "Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US) AppleWebKit/534.20 (KHTML, like Gecko) Chrome/11.0.672.2 Safari/534.20",
              "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/534.27 (KHTML, like Gecko) Chrome/12.0.712.0 Safari/534.27",
              "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/535.1 (KHTML, like Gecko) Chrome/13.0.782.24 Safari/535.1",
              "Mozilla/5.0 (Windows NT 6.0) AppleWebKit/535.2 (KHTML, like Gecko) Chrome/15.0.874.120 Safari/535.2",
              "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/535.7 (KHTML, like Gecko) Chrome/16.0.912.36 Safari/535.7",
              "Mozilla/5.0 (Windows; U; Windows NT 6.0 x64; en-US; rv:1.9pre) Gecko/2008072421 Minefield/3.0.2pre",
              "Mozilla/5.0 (Windows; U; Windows NT 5.1; zh-CN; rv:1.9b4) Gecko/2008030317 Firefox/3.0b4",
              "Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.9.0.10) Gecko/2009042316 Firefox/3.0.10",
              "Mozilla/5.0 (Windows; U; Windows NT 6.0; en-GB; rv:1.9.0.11) Gecko/2009060215 Firefox/3.0.11 (.NET CLR 3.5.30729)",
              "Mozilla/5.0 (Windows; U; Windows NT 6.0; en-US; rv:1.9.1.6) Gecko/20091201 Firefox/3.5.6 GTB5",
              "Mozilla/5.0 (Windows; U; Windows NT 5.1; tr; rv:1.9.2.8) Gecko/20100722 Firefox/3.6.8 ( .NET CLR 3.5.30729; .NET4.0E)",
              "Mozilla/5.0 (Windows; U; MSIE 6.0; Windows NT 5.1; SV1; .NET CLR 2.0.50727; BIDUBrowser 7.6)",
              "Mozilla/5.0 (Linux; U; Android 2.1; en-us; Nexus One Build/ERD62) AppleWebKit/530.17 (KHTML, like Gecko) Version/4.0 Mobile Safari/530.17",
              "Mozilla/5.0 (Linux; U; Android 2.2; en-us; Sprint APA9292KT Build/FRF91) AppleWebKit/533.1 (KHTML, like Gecko) Version/4.0 Mobile Safari/533.1",
              "Mozilla/5.0 (Linux; U; Android 2.2; en-us; ADR6300 Build/FRF91) AppleWebKit/533.1 (KHTML, like Gecko) Version/4.0 Mobile Safari/533.1",
              "Mozilla/5.0 (Linux; U; Android 2.2; en-ca; GT-P1000M Build/FROYO) AppleWebKit/533.1 (KHTML, like Gecko) Version/4.0 Mobile Safari/533.1",
              "Mozilla/5.0 (Linux; U; Android 3.0.1; fr-fr; A500 Build/HRI66) AppleWebKit/534.13 (KHTML, like Gecko) Version/4.0 Safari/534.13",
              "Mozilla/5.0 (Linux; U; Android 3.0; en-us; Xoom Build/HRI39) AppleWebKit/525.10  (KHTML, like Gecko) Version/3.0.4 Mobile Safari/523.12.2",
              "Mozilla/5.0 (Linux; U; Android 1.6; es-es; SonyEricssonX10i Build/R1FA016) AppleWebKit/528.5  (KHTML, like Gecko) Version/3.1.2 Mobile Safari/525.20.1",
              ]
    return choice(agents)