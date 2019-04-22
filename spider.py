# coding:utf-8
#__author__ = 'YuQiangYONG'
# from config import FIREFOX_HEAD_SETTING
from utils import clock
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import  WebDriverWait
from selenium.webdriver.support import  expected_conditions as EC
from lxml import etree


FIREFOX_HEAD_SETTING = "lang=zh_CN.UTF-8" # 火狐浏览器头部设置
TIME_OUT = 50 # selenium超时50s
BROWSER_RECATION = 10 # 浏览器反应10s
URL = "http://hotel.qunar.com/"
AGENT = "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:17.0; Baiduspider-ads) Gecko/17.0 Firefox/17.0" #浏览器agent


class Spider(object):

    def crawl(self, url, agent):
        options = webdriver.FirefoxOptions()
        options.add_argument(FIREFOX_HEAD_SETTING)
        options.add_argument(str(agent))
        self.driver = webdriver.Firefox(firefox_options=options)
        self.driver.set_page_load_timeout(TIME_OUT)
        self.driver.get(url)
        self.driver.maximize_window()
        self.driver.implicitly_wait()
        self.findElement()

    def findElement(self):
        self.ele_toCity = self.driver.find_element_by_name("toCity") # 到达城市
        self.ele_search = self.driver.find_element_by_class_name("search-btn") # 搜索按钮
        self.ele_fromDate = self.driver.find_element_by_id("fromDate") # 到店日期
        self.ele_toDate = self.driver.find_element_by_id("toDate") # 离店日期
        self.sendCity_clickSearch()

    def sendCity_clickSearch(self, tocity="广州"):
        self.ele_toCity.clear()
        self.ele_toCity.send_keys(tocity)
        self.ele_search.click()


if __name__ == '__main__':
    spider = Spider()
    spider.crawl(URL, AGENT)