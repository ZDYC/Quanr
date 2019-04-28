# coding:utf-8
#__author__ = 'YuQiangYONG'
from lxml import etree


class HtmlParser(object):
    def parser(self, html_const, tocity):
        html = etree.HTML(str(html_const))
        div = html.xpath(".//*[@class='item_hotel_info']")
        for each_div in div:
            name = each_div.xpath(".//*[@class='hotel_item']/a/text()")[0] #名字
            price = each_div.xpath(".//*[@class='item_price js_hasprice']/a/b/text()")[0] #最低价
            s_pro  = each_div.xpath(".//*[@class='level levelmargin']/a/strong/text()") #评分
            commit = each_div.xpath(".//*[@class='level levelmargin']/a/text()") #评论
            add_pro = each_div.xpath(".//*[@class='area_contair']/a/span/text()")