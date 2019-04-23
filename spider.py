# coding:utf-8
#__author__ = 'YuQiangYONG'
# from config import FIREFOX_HEAD_SETTING
from utils import clock
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import  WebDriverWait
from selenium.webdriver.support import  expected_conditions as EC
from lxml import etree
import time
import csv


FIREFOX_HEAD_SETTING = "lang=zh_CN.UTF-8" # 火狐浏览器头部设置
TIME_OUT = 50 # selenium超时50s
BROWSER_RECATION = 10 # 浏览器反应10s
URL = "http://hotel.qunar.com/"
AGENT = 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.103 Safari/537.36'


class Spider(object):

    def __init__(self, url, toCity):
        self.url = url
        self.toCity = toCity

    def start(self, agent):
        options = webdriver.FirefoxOptions()
        options.add_argument(FIREFOX_HEAD_SETTING)
        # options = webdriver.ChromeOptions()
        options.add_argument(str(agent))
        self.driver = webdriver.Firefox(firefox_options=options)
        # self.driver = webdriver.Chrome(chrome_options=options)
        self.driver.set_page_load_timeout(TIME_OUT)
        self.driver.get(self.url)
        self.driver.maximize_window()
        self.driver.implicitly_wait(8)
        self.findElement()

    def findElement(self):
        try:
            self.ele_toCity = self.driver.find_element_by_id("toCity") # 到达城市
            self.ele_search = self.driver.find_element_by_class_name("search-btn") # 搜索按钮
            self.ele_fromDate = self.driver.find_element_by_id("fromDate") # 到店日期
            self.ele_toDate = self.driver.find_element_by_id("toDate") # 离店日期
        except Exception as e:
            print(e)
        else:
            self.sendCity_clickSearch()

    def sendCity_clickSearch(self):
        self.ele_toCity.clear()
        self.ele_toCity.send_keys(self.toCity)
        self.ele_search.click()
        # time.sleep(10)
        # self.driver.quit()

    def jsWindowScrollTo(self):
        js = "window.srrollTo(0,document.body.scrollHeight);" #网页拉到底
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
    spider = Spider(url= "http://hotel.qunar.com/", toCity="广州")
    spider.start(AGENT)