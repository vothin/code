#!/usr/bin/env python

# encoding: utf-8
'''
    @author: Vothin
    @software: 自动化测试
    @file: businessView.py
    @time: 2019/9/24 9:54
    @desc:
'''
# ********************************************************

import time
import random
import logging
from care_user.common.common_fun import Common
from care_user.common.desired_caps import appium_desired
from care_user.businessView.loginAndLogoutView import LoginAndLogoutView
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException

class BusinessView(Common):

    username = '13412345678'
    password = '123456'

    # 五个基础按钮
    health_view = (By.ID, 'com.wdkl.capacity_care_user:id/ll_health_left')
    doctor_view = (By.ID, 'com.wdkl.capacity_care_user:id/ll_doctor_left_center')
    cloudD_view = (By.ID, 'com.wdkl.capacity_care_user:id/ll_cloud_room_docotor_center')
    cloudR_view = (By.ID, 'com.wdkl.capacity_care_user:id/ll_cloud_room_right_center')
    mine_view = (By.ID, 'com.wdkl.capacity_care_user:id/rl_mine_right')

    # 医生通讯录
    doctorShop_type = (By.ID, 'com.wdkl.capacity_care_user:id/layout_shop')
    doctorTitle_text = (By.ID, 'com.wdkl.capacity_care_user:id/tv_doctor_title')
    doctorChiel_button = (By.ID, 'com.wdkl.capacity_care_user:id/layout_doctor')
    doctorTitleName_text = (By.ID, 'com.wdkl.capacity_care_user:id/tv_doctor_name')
    doctorShopTitleName_text = (By.ID, 'com.wdkl.capacity_care_user:id/tv_shop_name')

    # 标题栏
    titlePanel_text = (By.CLASS_NAME, 'android.widget.TextView')

    # 健康页面
    def healthView(self):
        l = LoginAndLogoutView(self.driver)
        time.sleep(3)
        try:
            self.find_element(*self.health_view)
        except NoSuchElementException:
            l.login_action(self.username, self.password)
            self.check_cancelBtn()

            try:
                self.find_element(*self.health_view)
            except NoSuchElementException:
                logging.error('登录失败')
                return False
        else:
            logging.info('=============健康界面=============')
            self.find_element(*self.health_view).click()
            return True


    # 医生界面
    def doctorView(self):
        l = LoginAndLogoutView(self.driver)
        time.sleep(3)
        try:
            self.find_element(*self.doctor_view)
        except NoSuchElementException:
            l.login_action(self.username, self.password)
            self.check_cancelBtn()

            try:
                self.find_element(*self.doctor_view)
            except NoSuchElementException:
                logging.error('登录失败')
                return False
        else:
            logging.info('=============医生界面=============')
            self.find_element(*self.doctor_view).click()
            return True

    # 检测医生是否存在
    def doctorCheck(self, controller):
        self.back()

        logging.info('=============检测医生是否存在=============')
        try:
            self.find_element(*self.doctorShop_type)
        except NoSuchElementException:
            logging.info('=============没有绑定医生=============')
            return False
        else:
            logging.info('=============选择医生=============')

            value = self.find_elements(*self.doctorTitleName_text)
            try:
                self.find_element(*self.doctorChiel_button)
            except NoSuchElementException:
                r = random.randint(1, len(value))
            else:
                r = random.randint(2, len(value))

            if controller != -1:    # 控制器
                self.find_elements(*self.doctorTitleName_text)[controller].click()
            else:
                self.find_elements(*self.doctorTitleName_text)[r - 1].click()
            return True


    # 云医圈界面
    def cloudDView(self):
        l = LoginAndLogoutView(self.driver)
        time.sleep(3)
        try:
            self.find_element(*self.cloudD_view)
        except NoSuchElementException:
            l.login_action(self.username, self.password)
            self.check_cancelBtn()

            try:
                self.find_element(*self.cloudD_view)
            except NoSuchElementException:
                logging.error('登录失败')
                return False
        else:
            logging.info('=============云医圈界面=============')
            self.find_element(*self.cloudD_view).click()
            return True


    # 云医圈各页
    def cloudDEachPageView(self, num):
        a = self.cloudDView()

        if a == True:
            logging.info('=============云医圈主页=============')
            self.find_elements(*self.titlePanel_text)[num].click()
            return a
        else:
            return a


    # 消息界面
    def cloudRView(self):
        l = LoginAndLogoutView(self.driver)
        time.sleep(3)
        try:
            self.find_element(*self.cloudR_view)
        except NoSuchElementException:
            l.login_action(self.username, self.password)
            self.check_cancelBtn()

            try:
                self.find_element(*self.cloudR_view)
            except NoSuchElementException:
                logging.error('登录失败')
                return False
        else:
            logging.info('=============消息界面=============')
            self.find_element(*self.cloudR_view).click()
            return True


    # 我的界面
    def mineView(self):
        l = LoginAndLogoutView(self.driver)
        time.sleep(5)
        try:
            self.find_element(*self.mine_view)
        except NoSuchElementException:
            l.login_action(self.username, self.password)
            self.check_cancelBtn()

            try:
                self.find_element(*self.mine_view)
            except NoSuchElementException:
                logging.error('登录失败')
                return False
        else:
            logging.info('=============我的界面=============')
            self.find_element(*self.mine_view).click()
            return True




if __name__ == '__main__':
    driver = appium_desired()
    l = BusinessView(driver)
    l.healthView()
    l.doctorView()
    l.cloudDView()
    l.cloudRView()
    l.mineView()