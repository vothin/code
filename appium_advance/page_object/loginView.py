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
from appium_advance.page_object.baseView import BaseView
from appium_advance.page_object.common_fun import Common
from appium_advance.page_object.desired_caps import appium_desired
from selenium.webdriver.common.by import By
from PIL import Image
import pytesseract
from selenium.common.exceptions import NoSuchElementException

class LoginView(BaseView):
    username_type = (By.ID, 'doctor.wdklian.com:id/login_phone_et')
    password_type = (By.ID, 'doctor.wdklian.com:id/et_psw')
    security_type = (By.ID, 'doctor.wdklian.com:id/et_img_code')
    security_code = (By.ID, 'doctor.wdklian.com:id/iv_code_img')
    loginBtn_type = (By.ID, 'doctor.wdklian.com:id/tv_login')
    idPerson_type = (By.ID, 'doctor.wdklian.com:id/id_person')
    logoutBtn_type = (By.ID, 'doctor.wdklian.com:id/ll_ext_login')
    logoutOK_type = (By.ID, 'doctor.wdklian.com:id/tv_ok')


    def loin_action(self, username, password):
        # self.check_cancelBtn()
        # self.check_skipBtn()

        logging.info('=============login_action=============')
        try:
            un = self.driver.find_element(*self.username_type)

        except NoSuchElementException:
            logging.info('=============not_login=============')

        else:
            logging.info('用户名：%s' % username)
            self.driver.find_element(*self.username_type).clear()
            self.driver.find_element(*self.username_type).send_keys(username)

            logging.info('密码：%s' % password)
            self.driver.find_element(*self.password_type).send_keys(password)


            ### 获取验证码
            # 截屏
            securityImagePath = r'D:\Python3\code\appium_advance\yanzhengma\yanzhengma01.png'
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
            securityCode = pytesseract.image_to_string(qq).strip()
            print(securityCode)

            logging.info('验证码：%s' % securityCode)
            self.driver.find_element(*self.security_type).send_keys(securityCode)

            logging.info('click loginBtn')
            self.driver.find_element(*self.loginBtn_type).click()

    def logout(self):
        logging.info('=============logout_action=============')

        try:
            idPerson = self.driver.find_element(*self.idPerson_type)

        except NoSuchElementException:
            logging.info('=============not_logout=============')

        else:
            idPerson.click()
            self.driver.find_element(*self.logoutBtn_type).click()
            self.driver.find_element(*self.logoutOK_type).click()
            logging.info('已退出')

if __name__ == '__main__':
    driver = appium_desired()
    l = LoginView(driver)
    l.loin_action('16212345678', '123456')
    l.logout()