#!/usr/bin/env python

# encoding: utf-8
'''
    @author: Vothin
    @software: 自动化测试
    @file: globalpath.py
    @time: 2019/10/25 18:16
    @desc:
'''
# ********************************************************

import os, sys

BIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BIR)

# yaml配置文件的路径
# yamlpath = r'%s\conf\driver_config.yaml' % BIR            # 方法1
yamlpath = os.path.join(BIR, 'conf', 'driver_config.yaml')  # 方法2

# 日志文件
log_path = BIR + '\log\log.log'
screen_path = os.path.join(BIR, 'screenshots')
csv_path = os.path.join(BIR, 'data', 'account.csv')
config_path = os.path.join(BIR, 'conf', 'config.ini')
report_path = os.path.join(BIR, 'report')
testcase_path = os.path.join(BIR, 'test_case')
attach_path = os.path.join(BIR, 'report')   # 邮件附件
appium_log_path = os.path.join(BIR, r'log\appium_log')