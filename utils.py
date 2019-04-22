# coding:utf-8
#__author__ = 'YuQiangYONG'
import time
import logging


#create logger
logger_name = "Quanr"
logger = logging.getLogger(logger_name)
logger.setLevel(logging.DEBUG)
logging.basicConfig(filename='logger.log', level=logging.INFO)


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

