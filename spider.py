# coding:utf-8
#__author__ = 'YuQiangYONG'


# from config import FIREFOX_HEAD_SETTING
import logging
import utils
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import  WebDriverWait
from selenium.webdriver.support import  expected_conditions as EC
from selenium.webdriver.common.proxy import Proxy
from selenium.webdriver.common.proxy import ProxyType
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver import ActionChains
from lxml import etree
import time
import csv


FIREFOX_HEAD_SETTING = "lang=zh_CN.UTF-8" # 火狐浏览器头部设置
TIME_OUT = 50 # selenium超时50s


class Spider(object):

    def __init__(self, url, username, password,  toCity):
        self.url = url
        self.username = username
        self.password = password
        self.toCity = toCity

    def set_argument(self):
        """
        设置浏览器头部
        :return:
        """
        self.options = webdriver.FirefoxOptions()
        self.options.add_argument(FIREFOX_HEAD_SETTING)
        self.options.add_argument(str(utils.get_agent()))

    def set_proxy(self):
        """
        设置ip代理
        :return:
        """
        self.ip = utils.get_ip()['ip']
        self.port = utils.get_ip()['port']
        self.profile = webdriver.FirefoxProfile()
        self.profile.set_preference("network.proxy.type", 1)
        self.profile.set_preference('network.proxy.http', str(self.ip))
        self.profile.set_preference("network.proxy.http_port", str(self.port))
        self.profile.update_preferences()

        self.options.add_argument("--proxy-server=http://" + str(self.ip) + ':' + str(self.port))

        self.proxy = Proxy({
            'proxyType': ProxyType.MANUAL,
            'httpProxy': str(self.ip) + ':' + str(self.port)
        })
        dc = DesiredCapabilities.PHANTOMJS.copy()
        self.proxy.add_to_capabilities(dc)
        self.driver = webdriver.PhantomJS(desired_capabilities=dc)

    def start(self):
        self.login()

    def login(self):
        self.set_argument()
        # self.set_proxy()
        self.driver = webdriver.Firefox(firefox_options=self.options,
                                        # firefox_profile=self.profile,
                                        )
        self.driver.set_window_size(960, 960)
        self.driver.set_page_load_timeout(TIME_OUT)
        self.driver.get(self.url)
        time.sleep(1)
        self.driver.find_element_by_class_name("port-toggler").click() #二维码登陆转为账号密码登陆
        time.sleep(0.6)
        self.usernamePasswordLogin()
        # self.cookiesLogin()

    def usernamePasswordLogin(self):
        """
        自动输入账号密码 手动输入验证码
        :return:
        """
        self.driver.find_element_by_name("username").send_keys(self.username)
        time.sleep(0.5)
        self.driver.find_element_by_name("password").send_keys(self.password)
        vCode = input("输入验证码")
        self.driver.find_element_by_name("vcode").send_keys(vCode)
        time.sleep(0.2)
        self.driver.find_element_by_id("submit").click()
        # a = self.driver.find_element_by_id("errmsg")
        # if self.driver.find_element_by_id("errmsg").text == "图形验证码错误":
        #     self.driver.find_element_by_name("vcode").clear()
        #     vCode = input("验证码错误，请重新输入;")
        #     self.driver.find_element_by_name("vcode").send_keys(vCode)
        #     self.driver.find_element_by_id("submit").click()

        self.driver.implicitly_wait(5)
        self.driver.find_element_by_class_name("qhf_hotel").click() #跳转到酒店页面
        time.sleep(2)
        self.findElement()

    def cookiesLogin(self):
        # self.cookies = self.driver.get_cookies()
        time.sleep(3)
        cookieList = [
            {'name': 'QN43', 'value': '2', 'path': '/', 'domain': '.qunar.com', 'secure': False, 'httpOnly': False,
             'expiry': 1563787329},
            {'name': 'QN42', 'value': 'rxbd7296', 'path': '/', 'domain': '.qunar.com', 'secure': False,
             'httpOnly': False, 'expiry': 1563787329},
            {'name': '_q', 'value': 'U.qxoofvu3936', 'path': '/', 'domain': '.qunar.com', 'secure': False,
             'httpOnly': False, 'expiry': 1563787329},
            {'name': '_t', 'value': '26042962', 'path': '/', 'domain': '.qunar.com', 'secure': False, 'httpOnly': False,
             'expiry': 1563787329},
            {'name': 'csrfToken', 'value': 'hrZQi9btlRjPiCHohOokXwXZui3A7crt', 'path': '/', 'domain': '.qunar.com',
             'secure': False, 'httpOnly': False, 'expiry': 1563787329},
            {'name': '_s', 'value': 's_TGPBRSFWGJMFLTQ75P5Z64OOGA', 'path': '/', 'domain': '.qunar.com',
             'secure': False, 'httpOnly': False, 'expiry': 1563787329},
            {'name': '_v',
             'value': 'SlyhSZvl99Qdnb7xmIB58EqqOGHexrevYTSTyNriHGpGqsf9DLJa_KGC7u4qZL2BTPmUQnCO74Cq9oBwCzvcSI79UJIpH62vcFk3q36uyETbZxV49zentcAXJOiixAg178hoLQwtBe-mbgxzztzDJQBW6qQuigLMsrjGK_awOacu',
             'path': '/', 'domain': '.qunar.com', 'secure': False, 'httpOnly': True, 'expiry': 1563787329},
            {'name': 'QN99', 'value': '6254', 'path': '/', 'domain': '.qunar.com', 'secure': False, 'httpOnly': False,
             'expiry': 3504864012},
            {'name': 'QN300', 'value': 'organic', 'path': '/', 'domain': '.qunar.com', 'secure': False,
             'httpOnly': False, 'expiry': 2186731329},
            {'name': 'QunarGlobal', 'value': '10.86.213.148_-a57a043_16a497b0c16_-29c8|1556011329538', 'path': '/',
             'domain': '.qunar.com', 'secure': False, 'httpOnly': False, 'expiry': 3703494976},
            {'name': 'QN44', 'value': 'qxoofvu3936', 'path': '/', 'domain': '.qunar.com', 'secure': False,
             'httpOnly': False},
            {'name': 'QN267', 'value': '92957984796eb5d6f', 'path': '/', 'domain': '.qunar.com', 'secure': False,
             'httpOnly': False},
            # {'name': '_i', 'value': 'VInJOmzk0mfkIR-1ZDg1UEYNWp2q', 'path': '/', 'domain': '.qunar.com', 'secure': False, 'httpOnly': False, 'expiry': 3703494976},
            {'name': 'QN601', 'value': '82852f28d4480701f084665561002927', 'path': '/', 'domain': '.qunar.com',
             'secure': False, 'httpOnly': True, 'expiry': 4102358400},
            {'name': 'QN269', 'value': '45568FD065A911E980F7FA163E76697D', 'path': '/', 'domain': '.qunar.com',
             'secure': False, 'httpOnly': False, 'expiry': 1558603330},
            {'name': 'QN163', 'value': '0', 'path': '/', 'domain': '.qunar.com', 'secure': False, 'httpOnly': False},
            {'name': 'QN667', 'value': 'B', 'path': '/', 'domain': '.qunar.com', 'secure': False, 'httpOnly': False},
            {'name': 'QN48', 'value': 'bd371bef-984b-42cc-b3eb-edcba0fa6abc', 'path': '/', 'domain': '.qunar.com',
             'secure': False, 'httpOnly': False, 'expiry': 4709611330},
            # {'name': 'QN271', 'value': 'ee38709f-b73a-4185-a439-674293d95577', 'path': '/', 'domain': '.qunar.com', 'secure': False, 'httpOnly': False}]
        ]
        for cookie in cookieList:
            self.driver.add_cookie(cookie)
        time.sleep(5)
        self.driver.get(self.url)
        time.sleep(1)
        self.driver.find_element_by_class_name("port-toggler").click()

    def findElement(self):
        """
        找到四个控件
        :return:
        """
        try:
            self.ele_toCity = self.driver.find_element_by_id("toCity") # 到达城市
            self.ele_search = self.driver.find_element_by_class_name("search-btn") # 搜索按钮
            self.ele_fromDate = self.driver.find_element_by_id("fromDate") # 到店日期
            self.ele_toDate = self.driver.find_element_by_id("toDate") # 离店日期
        except Exception as e:
            print(e)
        else:
            self.sendCity_clickSearch()
    #
    def sendCity_clickSearch(self):
        """
        清空城市框后输入toCity并点击搜索
        :return:
        """
        self.ele_toCity.clear()
        time.sleep(1.5) # 停留2s,否则容易被检测到
        self.ele_toCity.send_keys(self.toCity)
        time.sleep(7)
        # ActionChains(self.driver).move_to_element(self.ele_toDate)
        # time.sleep(1.5)
        # self.driver.execute_script("arguments[0].click();", self.ele_search)
        self.ele_search.click()

    def jsWindowScrollTo(self):
        """
        网页拉到底
        :return:
        """
        js = "window.srrollTo(0,document.body.scrollHeight);"
        self.driver.execute_script(js)
        self.driver.implicitly_wait(4)

    def html_parse(self):
        self.rows = []
        html = etree.HTML(str(self.driver.page_source()))
        div = html.xpath(".//*[@class='item_hotel_info']")
        for each_div in div:
            name = each_div.xpath(".//*[@class='hotel_item']/a/text()")
            price = each_div.xpath(".//*[@class='item_price js_hasprice']/a/b/text()")
            socre = each_div.xpath(".//*[@class='level levelmargin']/a/strong/text()")
            commit = each_div.xpath(".//[@class='level levelmargin']/a/text()")
            recommand = each_div.xpath(".//*[@class='level levelmargin']/a/span/text()")
            address = each_div.xpath(".//[@class='area_contair']/a/span/text()")
            result = (name, address, socre, recommand, commit, price)
            self.rows.append(result)
        self.store_csv()

    def store_csv(self):
        headers = ['酒店名字', '地址', '评分', '推荐度', '点评数', '价格']
        with open("hotel.csv", 'a') as f:
            f_csv = csv.write(f, )
            f_csv.writerow(headers)
            f_csv.writerows(self.rows)


if __name__ == '__main__':
    login_url = 'https://user.qunar.com/passport/login.jsp?ret=https%3A%2F%2Fwww.qunar.com%2F'
    spider = Spider(url= login_url,
                    username='332976499@qq.com',
                    password='fsm19950923',
                    toCity="广州",
                    )
    spider.start()


    # browser = myFox().work()
    # js = 'window.open("https://www.baidu.com")'
    # browser.execute_script(js)
