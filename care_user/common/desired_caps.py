#!/usr/bin/env python

# encoding: utf-8
'''
    @author: Vothin
    @software: 自动化测试
    @file: desired_caps.py
    @time: 2019/9/9 11:25
    @desc:
'''
# ********************************************************

'''
    公共类：
        封装aqqium配置信息
        用来启动driver
'''

from appium import webdriver
import yaml
import logging
import logging.config

# 定义信息采集器
CON_LOG = r'../config/log.conf'
logging.config.fileConfig(CON_LOG)
logging = logging.getLogger()   # 任何使用driver的类，都可以用logging.*采集信息

def appium_desired():

    # 模拟器
    with open(r'../config/caps_Moniqi.yaml', 'r', encoding='utf-8') as file:
        data = yaml.load(file, Loader=yaml.FullLoader)  # 调用yaml配置文件

    # # OnePlus
    # with open(r'../config/caps_OnePlus.yaml', 'r', encoding='utf-8') as file:
    #     data = yaml.load(file, Loader=yaml.FullLoader)

    # appium配置信息
    desired_caps = {}
    desired_caps['platformName'] = data['platformName']
    desired_caps['platformVersion'] = data['platformVersion']
    desired_caps['deviceName'] = data['deviceName']

    # 获取APP的路径，然后导入
    # base_dir = os.path.dirname(os.path.dirname(__file__))
    # app_path = os.path.join(base_dir, 'app', data['appname'])
    # desired_caps['appname'] = app_path

    # 直接导入APP
    desired_caps['app'] = data['app']

    # 启动APP的activity
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
    # driver = webdriver.Remote('http://' + str(data['ip']) + ':' + str(data['port']) + '/wd/hub', desired_caps)  # 连接Appium服务器
    driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)  # 连接Appium服务器
    driver.implicitly_wait(10)

    return driver

if __name__ == '__main__':
    appium_desired()
