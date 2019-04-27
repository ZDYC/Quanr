# coding:utf-8
#__author__ = 'YuQiangYONG'
import pymysql


class DataMemory(object):

    def connect(self):
        self.db = pymysql.connect("localhost", "root", "123456", "QuanrDB" )
        self.cursor = self.db.cursor()
        self.cursor.execute("DROP TABLE IF EXITS DATA")
        sql = """CREATE TABLE DATA (
                name CHAR(30) NOT NULL,
                addr char(30) NOT NULL ,
                score float ,
                )"""