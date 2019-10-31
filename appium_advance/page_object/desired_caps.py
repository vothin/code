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

# 定义信息采集器
CON_LOG = r'D:\Python3\code\appium_advance\log\log.conf'
logging.config.fileConfig(CON_LOG)
logging = logging.getLogger()


def appium_desired():
    file = open(r'../configuration/configuration.yaml', 'r', encoding='utf-8')
    data = yaml.load(file, Loader=yaml.FullLoader)

    # appium配置信息
    desired_caps = {}
    desired_caps['platformName'] = data['platformName']
    desired_caps['platformVersion'] = data['platformVersion']
    desired_caps['deviceName'] = data['deviceName']
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
    driver.implicitly_wait(5)

    return driver

if __name__ == '__main__':
    appium_desired()
