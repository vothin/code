#!/usr/bin/env python

# encoding: utf-8
'''
    @author: Vothin
    @software: 自动化测试
    @file: lantrenSideView.py
    @time: 2019/9/18 15:07
    @desc:
'''
# ********************************************************

from care_user.businessView.businessView import *
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException


class LanternSideView(Common):
    health_view = (By.ID, 'com.wdkl.capacity_care_user:id/ll_health_left')

    imageView_type = (By.CLASS_NAME, 'android.widget.ImageView')

    # 注意事项
    relativeAdvice_type = (By.ID, 'com.wdkl.capacity_care_user:id/relative_advice')

    def lanternSwipeLeft(self):
        # 轮播图左滑
        logging.info('=============左滑=============')
        try:
            self.find_element(*self.relativeAdvice_type)
        except NoSuchElementException:
            logging.info('=============不在健康界面=============')
        else:
            l = self.get_size()
            x1 = l[0] * 0.9
            x2 = l[0] * 0.1
            y1 = l[1] * 0.2
            self.swipe(x1, y1, x2, y1, 1000)

    def lanternSwipeRight(self):
        # 轮播图右滑
        logging.info('=============右滑=============')
        try:
            self.find_element(*self.relativeAdvice_type)
        except NoSuchElementException:
            logging.info('=============不在健康界面=============')
        else:
            l = self.get_size()
            x1 = l[0] * 0.1
            x2 = l[0] * 0.9
            y1 = l[1] * 0.2
            self.swipe(x1, y1, x2, y1, 1000)

    def lanternSwipeClick(self):
        self.find_elements(*self.imageView_type)[1].click()
        time.sleep(5)
        self.getScreenShot('轮播图')
        self.back()


    def login_health(self):
        l = BusinessView(self.driver)
        a = l.healthView()
        return a

if __name__ == '__main__':
    driver = appium_desired()
    l = LanternSideView(driver)
    k = l.login_health()
    if k == False:
        print("登录失败")
    else:
        l.lanternSwipeRight()
        l.lanternSwipeClick()
        l.lanternSwipeLeft()
        l.lanternSwipeClick()