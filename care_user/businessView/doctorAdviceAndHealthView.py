#!/usr/bin/env python

# encoding: utf-8
'''
    @author: Vothin
    @software: 自动化测试
    @file: doctorAdviceAndHealthView.py
    @time: 2019/10/8 14:48
    @desc:
'''
# ********************************************************

from care_user.businessView.businessView import *
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from appium import webdriver
from selenium.webdriver.support.ui import WebDriverWait

class DoctorAdviceAndHealth(Common):

    # 注意事项
    doctorAdviceContent_text = (By.ID, 'com.wdkl.capacity_care_user:id/send_content')
    doctorAdviceContenttext_text = (By.ID, 'com.wdkl.capacity_care_user:id/contenttext')
    doctorAdviceContentR_button =(By.ID, 'com.wdkl.capacity_care_user:id/exit_button')

    # 健康宣教
    doctorHealthTitle_text = (By.ID, 'com.wdkl.capacity_care_user:id/title_name')
    doctorHealthContent_text = (By.ID, 'com.wdkl.capacity_care_user:id/content')
    doctorHealthView_view = (By.CLASS_NAME, 'android.view.View')


    # 健康宣教
    doctorHealthTitle = ''
    doctorHealthContent = ''

    # 注意事项
    doctorAdviceContenttext = ''



    def doctorAdvice(self, controller):
        check = self.check_doctor()
        if check == True:

            # 点击注意事项
            time.sleep(3)
            logging.info('=============点击注意事项=============')
            self.touch_tap(0.6, 0.465, 500)

            try:
                self.find_element(*self.doctorAdviceContent_text)
            except NoSuchElementException:
                logging.info('=============没有注意事项=============')
                return False
            else:
                value = self.find_elements(*self.doctorAdviceContent_text)
                r = random.randint(1, len(value))

                if controller != -1:  # 控制器
                    self.find_elements(*self.doctorAdviceContent_text)[controller].click()
                else:
                    self.find_elements(*self.doctorAdviceContent_text)[r - 1].click()

                self.doctorAdviceContenttext = self.find_element(*self.doctorAdviceContent_text).text
                logging.info('=============注意事项内容：%s=============' % self.doctorAdviceContenttext)

                logging.info('=============返回=============')
                self.find_element(*self.doctorAdviceContentR_button).click()

                return True

        else:
            return False



    def doctorHealth(self, controller):
        check = self.check_doctor()
        if check == True:

            # 点击健康宣教
            time.sleep(3)
            logging.info('=============点击健康宣教=============')
            self.touch_tap(0.4, 0.465, 500)

            try:
                self.find_element(*self.doctorHealthContent_text)
            except NoSuchElementException:
                logging.info('=============没有健康宣教=============')
                return False
            else:
                value = self.find_elements(*self.doctorHealthContent_text)
                r = random.randint(1, len(value))

                if controller != -1:  # 控制器
                    self.find_elements(*self.doctorHealthContent_text)[controller].click()
                else:
                    self.find_elements(*self.doctorHealthContent_text)[r - 1].click()
                self.back()

                self.doctorHealthContent = self.find_element(*self.doctorHealthContent_text).text
                logging.info('=============健康宣教内容：%s=============' % self.doctorHealthContent)


                return True
        else:
            return False


    def login_doctor(self):
        l = BusinessView(self.driver)
        a = l.doctorView()
        return a

    def check_doctor(self):
        l = BusinessView(self.driver)
        b = l.doctorCheck(2)
        return b


if __name__ == '__main__':
    driver = appium_desired()
    l = DoctorAdviceAndHealth(driver)
    l.login_doctor()
    l.doctorHealth(-1)
    l.doctorAdvice(-1)
