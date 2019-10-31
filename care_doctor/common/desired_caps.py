#!/usr/bin/env python

# encoding: utf-8
'''
    @author: Vothin
    @software: 练习自动化测试
    @file: desired_caps.py
    @time: 2019/8/14 16:21
    @desc:
'''
# ********************************************************

'''
    公共类：
        封装aqqium配置信息
'''

from appium import webdriver
import yaml
import logging
import logging.config
import os

# 定义信息采集器
CON_LOG = r'../config/log.conf'
logging.config.fileConfig(CON_LOG)
logging = logging.getLogger()


def appium_desired():

    with open(r'../config/caps.yaml', 'r', encoding='utf-8') as file:
        data = yaml.load(file, Loader=yaml.FullLoader)

    # appium配置信息
    desired_caps = {}
    desired_caps['platformName'] = data['platformName']
    desired_caps['platformVersion'] = data['platformVersion']
    desired_caps['deviceName'] = data['deviceName']

    # base_dir = os.path.dirname(os.path.dirname(__file__))
    # app_path = os.path.join(base_dir, 'app', data['appname'])
    # desired_caps['appname'] = app_path
    desired_caps['app'] = data['app']
    desired_caps['appPackage'] = data['appPackage']
    desired_caps['appActivity'] = data['appActivity']

    # 测试覆盖开关按钮
    desired_caps['noReset'] = data['noReset']

    # 开启中文输入
    desired_caps['unicodeKeyboard'] = data['unicodeKeyboard']
    desired_caps['resetKeyboard'] = data['resetKeyboard']

    # 开启验证Toast信息
    desired_caps['automationName'] = data['automationName']


    logging.info('start app...')
    driver = webdriver.Remote('http://' + str(data['ip']) + ':' + str(data['port']) + '/wd/hub', desired_caps) # 连接Appium服务器
    driver.implicitly_wait(30)

    return driver

if __name__ == '__main__':
    appium_desired()
