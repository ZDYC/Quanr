# coding:utf-8
#__author__ = 'YuQiangYONG'
import time


def clock(funct):
    '''
    用来计算爬虫耗时的装饰器
    :param funct:
    :return:
    '''
    def clocked(*args, **kwargs):
        t0 = time.perf_counter()
        result = funct(*args, **kwargs)
        elapsed = time.perf_counter() - t0
        print('%s消耗%s秒' % (funct, str(elapsed - t0)))
        return result
    return clocked