#!/usr/bin/env python

# encoding: utf-8
'''
    @author: Vothin
    @software: 自动化测试
    @file: baseView.py
    @time: 2019/9/9 11:23
    @desc:
'''
# ********************************************************

'''
    公共类：
        driver的初始化
        元素定位的封装
        屏幕尺寸和滑动
'''


class BaseView(object):
    def __init__(self, driver):
        self.driver = driver

    def find_element(self, *loc):   # 元素定位
        return self.driver.find_element(*loc)

    def find_elements(self, *loc):  # 多元素定位
        return self.driver.find_elements(*loc)

    def get_window_size(self):  # 获得屏幕尺寸
        return self.driver.get_window_size()

    def swipe(self, strat_x, start_y, end_x, end_y, duration):  # 滑动
        '''

        :param strat_x:     初始坐标x
        :param start_y:     初始坐标y
        :param end_x:       结束坐标x
        :param end_y:       结束坐标y
        :param duration:    滑动时间毫秒
        :return:            进行滑动
        '''
        return self.driver.swipe(strat_x, start_y, end_x, end_y, duration)

    def tap(self, x, y, duration):
        '''

        :param x:           点击位置的坐标x
        :param y:           点击位置的坐标y
        :param duration:    点击时间毫秒
        :return:            进行点击
        '''
        return self.driver.tap([(x, y), (x, y)], duration)