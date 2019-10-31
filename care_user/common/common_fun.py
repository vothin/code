#!/usr/bin/env python

# encoding: utf-8
'''
    @author: Vothin
    @software: 自动化测试
    @file: common_fun.py
    @time: 2019/9/9 15:25
    @desc:
'''
# ********************************************************

'''
    公共类：
        封装所有公共操作
'''

from care_user.baseView.baseView import BaseView
from care_user.common.desired_caps import appium_desired
from selenium.common.exceptions import NoSuchElementException
import logging
from selenium.webdriver.common.by import By
import time
import os
import csv

class Common(BaseView):
    cencelBtn = (By.ID, 'android:id/button2')
    skipBtn = (By.ID, 'com.tal.kaoyan:id/tv_skip')
    androidViewBack = (By.ID, 'com.wdkl.capacity_care_user:id/back')

    # 取消按钮
    def check_cancelBtn(self):
        logging.info('=============点击取消按钮=============')

        try:
            cancelBtn = self.driver.find_element(*self.cencelBtn)
        except NoSuchElementException:
            logging.info('没有取消按钮')
        else:
            cancelBtn.click()

    # 跳过按钮
    def check_skipBtn(self):
        logging.info('=============点击跳过按钮=============')

        try:
            skipBtn = self.driver.find_element(*self.skipBtn)
        except NoSuchElementException:
            logging.info('没有跳过按钮')
        else:
            skipBtn.click()

    # 获得屏幕尺寸
    def get_size(self):
        '''
            获得屏幕尺寸
        :return: 宽x 长y
        '''
        x = self.driver.get_window_size()['width']
        y = self.driver.get_window_size()['height']
        return x, y

    def touch_tap(self, x, y, duration):
        '''
            点击操作
        :param x:   横轴x
        :param y:   纵轴y
        :return:
        '''
        l = self.get_size()
        x = float(x) * l[0]
        y = float(y) * l[1]
        self.tap(float(x), float(y), duration)

    # 中间左滑
    def swipeLeft(self):
        '''
            固定中间左滑
            如需改变，需要调试
        :return:
        '''
        logging.info('=============左滑=============')

        l = self.get_size()
        x1 = int(l[0] * 0.9)
        x2 = int(l[0] * 0.1)
        y1 = int(l[1] * 0.5)
        self.swipe(x1, y1, x2, y1, 1000)

    # 中间右滑
    def swipeRight(self):
        '''
            固定中间右滑
            如需改变，需要调试
        :return:
        '''
        logging.info('=============右滑=============')

        l = self.get_size()
        x1 = int(l[0] * 0.1)
        x2 = int(l[0] * 0.9)
        y1 = int(l[1] * 0.5)
        self.swipe(x1, y1, x2, y1, 1000)

    # 获得当前时间
    def getTime(self):
        '''
            获得当前时间
        :return:
        '''
        self.now = time.strftime('%Y-%m-%d %H_%M_%S')
        return self.now

    # 截图保存
    def getScreenShot(self, module):
        '''
            截图保存
        :param module: 保存的名字
        :return:
        '''
        time = self.getTime()
        image_file = r'../scrennshots/%s_%s.png' % (module, time)
        logging.info('get %s screensht' % module)
        self.driver.get_screenshot_as_file(image_file)

    # 数据读取
    def get_csv_data(self, csv_file, line):
        '''
            数据读取
        :param csv_file: 输入需要读取的csv文件
        :param line: 输入需要读取的行数
        :return: 返回具体值,row第二个值
        '''
        with open(csv_file, 'r', encoding='utf-8-sig') as file:
            reader = csv.reader(file)
            for index, row in enumerate(reader, 1):
                if index == line:
                    return row

    # 返回
    def back(self):
        try:
            self.find_element(*self.androidViewBack)
        except NoSuchElementException:
            pass
        else:
            logging.info('=============返回=============')
            self.find_element(*self.androidViewBack).click()


if __name__ == '__main__':
    driver = appium_desired()
    com = Common(driver)
    time.sleep(5)
    com.touch_tap(0.6, 0.5, 500)