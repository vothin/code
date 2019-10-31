#!/usr/bin/env python

# encoding: utf-8
'''
    @author: Vothin
    @software: 自动化测试
    @file: test.py
    @time: 2019/10/9 18:07
    @desc:
'''
# ********************************************************

from care_user.businessView.businessView import *
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import NoSuchElementException


class CloudDServices(Common):

    cloudServices_button = (By.CLASS_NAME, 'android.widget.TextView')
    cloudServicesView_view = (By.CLASS_NAME, 'android.view.View')


    def test(self):

        self.find_elements(*self.cloudServices_button)[2].click()

        WebDriverWait(self.driver, 5).until(lambda x: x.find_element(*self.cloudServicesView_view))
        contexts = self.driver.contexts
        print(contexts)



    def login_cloudD(self):
       l = BusinessView(self.driver)
       a = l.cloudDView()
       return a

if __name__ == '__main__':
    driver = appium_desired()
    l = CloudDServices(driver)
    l.login_cloudD()
    l.test()