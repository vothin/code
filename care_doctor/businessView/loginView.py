#!/usr/bin/env python

# encoding: utf-8
'''
    @author: Vothin
    @software: 练习自动化测试
    @file: loginView.py
    @time: 2019/8/15 10:23
    @desc:
'''
# ********************************************************


import logging
from care_doctor.common.common_fun import Common
from care_doctor.common.desired_caps import appium_desired
from selenium.webdriver.common.by import By
from PIL import Image
import pytesseract
from selenium.common.exceptions import NoSuchElementException

import sys

path = r'D:\Python3\code\care_doctor\\'
sys.path.append(path)

class LoginView(Common):
    username_type = (By.ID, 'doctor.wdklian.com:id/login_phone_et')     # 用户名
    password_type = (By.ID, 'doctor.wdklian.com:id/et_psw')             # 密码
    security_type = (By.ID, 'doctor.wdklian.com:id/et_img_code')        # 验证码
    security_code = (By.ID, 'doctor.wdklian.com:id/iv_code_img')        # 验证码输入
    loginBtn_type = (By.ID, 'doctor.wdklian.com:id/tv_login')           # 登录按钮
    idPerson_type = (By.ID, 'doctor.wdklian.com:id/id_person')          # 我的界面
    tv_name_type = (By.ID, 'doctor.wdklian.com:id/tv_name')             # 我的界面
    logoutBtn_type = (By.ID, 'doctor.wdklian.com:id/ll_ext_login')      # 退出登录
    logoutOK_type = (By.ID, 'doctor.wdklian.com:id/tv_ok')              # 确认退出


    def login_action(self, username, password):
        # self.check_cancelBtn()
        # self.check_skipBtn()

        logging.info('=============登录=============')
        try:
            self.driver.find_element(*self.username_type)

        except NoSuchElementException:
            logging.info('=============没有登录界面=============')

        else:
            logging.info('用户名：%s' % username)
            self.driver.find_element(*self.username_type).clear()
            self.driver.find_element(*self.username_type).send_keys(username)

            logging.info('密码：%s' % password)
            self.driver.find_element(*self.password_type).clear()
            self.driver.find_element(*self.password_type).send_keys(password)


            ### 获取验证码
            # 截屏
            securityImagePath = r'D:\Python3\code\care_doctor\image\yanzhengma\yanzhengma.png'
            self.driver.save_screenshot(securityImagePath)

            securityImage = self.driver.find_element(*self.security_code)
            location = securityImage.location    # 获取验证码的坐标(x, y)
            size = securityImage.size           # 获取验证码的大小

            # 写成我们需要的坐标
            rangle = (int(location['x']),int(location['y']),int(location['x']+size['width']),int(location['y']+size['height']))

            # 截取验证码，并且重新保存
            image = Image.open(securityImagePath)
            fram4 = image.crop(rangle)
            fram4.save(securityImagePath)

            # 识别验证码
            qq = Image.open(securityImagePath)
            securityCode = pytesseract.image_to_string(qq).replace(" ", "")

            logging.info('验证码：%s' % securityCode)
            self.driver.find_element(*self.security_type).send_keys(securityCode)

            logging.info('点击登录按钮')
            self.driver.find_element(*self.loginBtn_type).click()

    def check_loginStatus(self):
        logging.info('=============检测用户名=============')

        try:
            self.driver.find_element(*self.idPerson_type).click()
            tvName = self.driver.find_element(*self.tv_name_type)
        except NoSuchElementException:
            logging.error('登录失败')
            self.getScreenShot('登录失败')
            return False
        else:
            logging.info('登录成功')
            logging.info('用户名：' + tvName.text)
            self.logout()
            return True

    def logout(self):
        logging.info('=============退出登录=============')
        self.driver.find_element(*self.logoutBtn_type).click()
        self.driver.find_element(*self.logoutOK_type).click()
        logging.info('退出成功')

if __name__ == '__main__':
    driver = appium_desired()
    l = LoginView(driver)
    l.login_action('16212345678', '123456')
    l.check_loginStatus()

