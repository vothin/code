#!/usr/bin/env python

# encoding: utf-8
'''
    @author: Vothin
    @software: 自动化测试
    @file: unittest_fun.py
    @time: 2019/10/30 11:45
    @desc:
'''
# ********************************************************

import unittest, time
from yzmbwf.common.start_driver import StartDriver
from yzmbwf.common.recordlog import logs

class UnittestFun(unittest.TestCase):
    '''unittest框架，继承TsetCase'''

    def setUp(self):
        logs.info('=====setUp=====')
        self.stdri = StartDriver()
        self.driver = self.stdri.get_driver()


    def tearDown(self):
        logs.info('=====tearDown=====')
        time.sleep(5)
        self.driver.quit()