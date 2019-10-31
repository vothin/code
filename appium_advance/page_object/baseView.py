#!/usr/bin/env python

# encoding: utf-8
'''
    @author: Vothin
    @software: 练习自动化测试
    @file: baseView.py
    @time: 2019/8/14 16:21
    @desc:
'''
# ********************************************************

'''
    公共类：
        driver的初始化
        元素定位的封装
'''

class BaseView(object):
    def __init__(self, driver):
        self.driver = driver

    def find_element(self, *loc):
        return self.driver.find_element(*loc)