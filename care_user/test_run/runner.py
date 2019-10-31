#!/usr/bin/env python

# encoding: utf-8
'''
    @author: Vothin
    @software: 自动化测试
    @file: runner.py
    @time: 2019/9/11 12:23
    @desc:
'''
# ********************************************************

import unittest
from BSTestRunner import BSTestRunner
import time, logging
import sys

path = r'D:\Python3\code\care_user\\'
path2 = r'D:\Python3\code\\'
sys.path.append(path)
sys.path.append(path2)

test_dir = '../test_case'
report_dir = '../reports'

discover = unittest.defaultTestLoader.discover(test_dir, pattern='test_lanternSwipe.py')

now = time.strftime('%Y-%m-%d %H_%M_%S')
report_name = report_dir + '/' + now + 'test_report.html'

with open(report_name, 'wb') as f:
    runner = BSTestRunner(stream=f, title='Test Report', description='Android app test report')
    logging.info('start run test case...')
    runner.run(discover)
