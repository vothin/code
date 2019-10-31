#!/usr/bin/env python

# encoding: utf-8
'''
    @author: Vothin
    @software: 练习自动化测试
    @file: desired_caps2.py.py
    @time: 2019/8/23 11:47
    @desc:
'''
# ********************************************************

'''
    公共类：
        封装aqqium配置信息
'''

from appium import webdriver
from time import ctime
import yaml
import logging
import logging.config
import os
import multiprocessing

# 定义信息采集器
CON_LOG = r'../config/log.conf'
logging.config.fileConfig(CON_LOG)
logging = logging.getLogger()

# 两个设备号
# devices_list = ['127.0.0.1:62001', '127.0.0.1:62025']
devices_list = ['127.0.0.1:62001']

def appium_desired(udid, port):
    with open(r'../config/caps.yaml', 'r', encoding='utf-8') as file:
        data = yaml.load(file, Loader=yaml.FullLoader)

    # appium配置信息
    desired_caps = {}
    desired_caps['platformName'] = data['platformName']
    desired_caps['platformVersion'] = data['platformVersion']
    desired_caps['deviceName'] = data['deviceName']
    desired_caps['udid'] = udid

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

    logging.info('start app... port:%s start run %s at %s' % (port, udid, ctime()))
    driver = webdriver.Remote('http://' + str(data['ip']) + ':' + str(port) + '/wd/hub', desired_caps)  # 连接Appium服务器
    driver.implicitly_wait(8)

    return driver


# 构建desired进程组
desired_process = []

# 加载desied进程
for i in range(len(devices_list)):
    port = 4723 + 2 * i
    desired = multiprocessing.Process(target=appium_desired, args=(devices_list[i], port))
    desired_process.append(desired)

if __name__ == '__main__':
    # 启动多设备执行测试
    for desired in desired_process:
        desired.start()
    for desired in desired_process:
        desired.join()