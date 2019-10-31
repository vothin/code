#!/usr/bin/env python

# encoding: utf-8
'''
    @author: Vothin
    @software: 练习自动化测试
    @file: common_fun.py
    @time: 2019/8/14 16:21
    @desc:
'''
# ********************************************************


'''
    公共类：
        封装所有公共操作，但目前还没完成
'''


from appium_advance.page_object.baseView import BaseView
from appium_advance.page_object.desired_caps import appium_desired
from selenium.common.exceptions import NoSuchElementException
import logging
from selenium.webdriver.common.by import By


class Common(BaseView):
    cencelBtn = (By.ID, 'android:id/button2')
    skipBtn = (By.ID, 'com.tal.kaoyan:id/tv_skip')
    x = 0
    y = 0

    def check_cancelBtn(self):
        logging.info('=============check_cancelBtn=============')

        try:
            cancelBtn = self.driver.find_element(*self.cencelBtn)
        except NoSuchElementException:
            logging.info('no cancelBtn')
        else:
            cancelBtn.click()


    def check_skipBtn(self):
        logging.info('=============check_skipBtn=============')

        try:
            skipBtn = self.driver.find_element(*self.skipBtn)
        except NoSuchElementException:
            logging.info('no skipBtn')
        else:
            skipBtn.click()

    def get_size(self):
        logging.info('=============get_size=============')
        self.x = driver.get_window_size()['width']
        self.y = driver.get_window_size()['height']
        return self.x, self.y

    def swipeLeft(self):
        logging.info('=============swipeLeft=============')
        x1 = int(self.x * 0.9)
        x2 = int(self.x * 0.1)
        y1 = int(self.y * 0.5)
        driver.swipe(x1, y1, x2, y1, 1000)

if __name__ == '__main__':
    driver = appium_desired()
    com = Common(driver)
    com.check_cancelBtn()
    com.check_skipBtn()
