#!/usr/bin/env python

# encoding: utf-8
'''
    @author: Vothin
    @software: 自动化测试
    @file: start_end.py
    @time: 2019/9/9 17:38
    @desc:
'''
# ********************************************************

import unittest
from care_user.common.desired_caps import appium_desired
import logging
import time
import warnings

class StartAndEnd(unittest.TestCase):
    def setUp(self):
        '''
            测试用例执行前的操作
        :return:
        '''
        time.sleep(10)
        warnings.simplefilter('ignore', ResourceWarning)
        logging.info('=============用例执行=============')
        self.driver = appium_desired()

    def tearDown(self):
        '''
            测试用例执行完成后的操作
        :return:
        '''
        logging.info('=============执行完成=============')
        self.driver.close_app()