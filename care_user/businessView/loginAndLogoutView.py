#!/usr/bin/env python

# encoding: utf-8
'''
    @author: Vothin
    @software: 自动化测试
    @file: loginAndLogoutView.py
    @time: 2019/9/23 11:37
    @desc:
'''
# ********************************************************

import time
import logging
from care_user.common.common_fun import Common
from care_user.common.desired_caps import appium_desired
from selenium.webdriver.common.by import By
from PIL import Image
import pytesseract
from selenium.common.exceptions import NoSuchElementException


class LoginAndLogoutView(Common):
    # 引导页
    imageView_class = (By.CLASS_NAME, 'android.widget.ImageView')
    intoLogin_button = (By.ID, 'com.wdkl.capacity_care_user:id/btn_into_login')

    # 登录界面
    username_input = (By.ID, 'com.wdkl.capacity_care_user:id/login_phone_et')
    password_input = (By.ID, 'com.wdkl.capacity_care_user:id/et_psw')
    security_input = (By.ID, 'com.wdkl.capacity_care_user:id/et_img_code')
    securityCode_image = (By.ID, 'com.wdkl.capacity_care_user:id/iv_code1')
    loginBtn_button = (By.ID, 'com.wdkl.capacity_care_user:id/tv_login')

    # 我的界面
    minePage_button = (By.ID, 'com.wdkl.capacity_care_user:id/rl_mine_right')
    username_text = (By.ID, 'com.wdkl.capacity_care_user:id/user_name')
    mineImage_buttons = (By.ID, 'com.wdkl.capacity_care_user:id/image')
    logoutOK_button = (By.ID, 'android:id/button1')


    def imageView(self):
        # 跳过引导页
        logging.info('=============跳过引导界面=============')
        time.sleep(3)
        try:
            image = self.find_elements(*self.imageView_class)
        except NoSuchElementException:
            pass
        else:
            if len(image) > 1:
                logging.info('=============没有引导界面=============')
            else:
                self.swipeLeft()
                self.swipeLeft()
                self.swipeLeft()
                self.swipeLeft()
                try:
                    self.find_element(*self.intoLogin_button)
                except NoSuchElementException:
                    pass
                else:
                    self.find_element(*self.intoLogin_button).click()

    def login_action(self, username, password):
        self.imageView()

        logging.info('=============登录=============')
        try:
            self.find_element(*self.username_input)
        except NoSuchElementException:
            logging.info('=============没有登录界面=============')
        else:
            logging.info('用户名：%s' % username)
            self.find_element(*self.username_input).clear()
            self.find_element(*self.username_input).send_keys(username)

            logging.info('密码：%s' % password)
            self.find_element(*self.password_input).clear()
            self.find_element(*self.password_input).send_keys(password)

            # 获取验证码
            # 截屏
            securityImagePath = r'../image/yanzhengma/yanzhengma.png'
            self.driver.save_screenshot(securityImagePath)

            securityImage = self.find_element(*self.securityCode_image)
            location = securityImage.location    # 获验证码的位置(x, y)
            size = securityImage.size   # 获取验证码的大小

            # 写成我们需要的坐标
            zuobiao = (int(location['x']), int(location['y']), int(location['x'] + size['width']), int(location['y'] + size['height']))

            # 截取验证码，并且重新保存
            image = Image.open(securityImagePath)
            fram4 = image.crop(zuobiao)
            fram4.save(securityImagePath)

            # 识别验证码
            yanzhengmaImage = Image.open(securityImagePath)
            yanzhengmaCode = pytesseract.image_to_string(yanzhengmaImage).replace(" ", "")

            logging.info('验证码：%s' % yanzhengmaCode)
            self.find_element(*self.security_input).send_keys(yanzhengmaCode)

            logging.info('点击登录按钮')
            self.find_element(*self.loginBtn_button).click()

    def check_login(self):
        self.check_cancelBtn()

        logging.info('=============检测用户名=============')
        try:
            self.find_element(*self.minePage_button).click()
            username = self.find_element(*self.username_text)
        except NoSuchElementException:
            logging.error('登录失败')
            self.getScreenShot('登录失败')
            return False
        else:
            logging.info('用户名：' + username.text)
            self.logout_action()
            return True

    def logout_action(self):
        logging.info('=============退出登录=============')
        self.find_elements(*self.mineImage_buttons)[-1].click()
        self.find_element(*self.logoutOK_button).click()


if __name__ == '__main__':
    for i in range(10):
        driver = appium_desired()
        l = LoginAndLogoutView(driver)
        l.login_action('13412345678', '123456')
        l.check_login()