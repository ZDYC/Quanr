# coding:utf-8
#__author__ = 'YuQiangYONG'


class UrlManager(object):
    def __init__(self):
        self.new_urls = set() #未爬取
        self.old_urls = set() #已爬取

    def get_new_url(self):
        '''
        获取一个未爬的url
        :return:
        '''
        new_url = self.new_urls.pop()
        self.olds_urls.add(new_url)
        return new_url

    def add_new_url(self, url):
        '''
        将一个新的url加入到未爬集合中
        :param url:
        :return:
        '''
        if url and url not in self.new_urls and url not in self.old_urls:
            self.new_urls.add(url)
        else:
            return {'err': 'url错误或已存在url集中'}

    def new_url_size(self):
        return len(self.new_urls)

    def old_url_size(self):
        return len(self.old_urls)