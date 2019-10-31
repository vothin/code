#!/usr/bin/env python

# encoding: utf-8
'''
    @author: Vothin
    @software: 自动化测试
    @file: start_driver.py
    @time: 2019/10/29 15:19
    @desc:
'''
# ********************************************************


from appium import webdriver
from yzmbwf.common.recordlog import logs
from yzmbwf.common.read_YamlConfig import ReadYamlConfig
import os

class StartDriver(object):
    '''获取终端驱动'''
    def __init__(self):
        self.conf = ReadYamlConfig()

    def get_driver(self):
        data = self.conf.get_yamlfile()
        try:
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

            # 设置命令超时时间
            # desired_caps['newCommandTimeout'] = data['newCommandTimeout']

            logs.info('start app...')
            driver = webdriver.Remote('http://%s:%s/wd/hub' % (data['ip'], data['port']), desired_caps)
            # driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)
            driver.implicitly_wait(10)
            return driver

        except Exception as e:
            logs.error('Appium服务未启动或设备devices未连接！', e)
            exit()


    def close_devices(self):
        driver = self.get_driver().close()

if __name__ == '__main__':
    driver = StartDriver()
    driver.get_driver()