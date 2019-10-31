#!/usr/bin/env python

# encoding: utf-8
'''
    @author: Vothin
    @software: 练习自动化测试
    @file: start_end.py
    @time: 2019/8/21 15:42
    @desc:
'''
# ********************************************************

import unittest
from care_doctor.common.desired_caps import appium_desired
import logging
import time
import warnings

class StartEnd(unittest.TestCase):
    def setUp(self):
        '''
            测试用例执行前的操作
        :return:
        '''
        warnings.simplefilter('ignore', ResourceWarning)
        logging.info('=============用例执行=============')
        self.driver = appium_desired()

    def tearDown(self):
        '''
            测试用例执行完成后的操作
        :return:
        '''
        logging.info('=============执行完成=============')
        time.sleep(5)
        self.driver.close_app()
        time.sleep(5)