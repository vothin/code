#!/usr/bin/env python

# encoding: utf-8
'''
    @author: Vothin
    @software: 自动化测试
    @file: adviceView.py
    @time: 2019/9/19 14:46
    @desc:
'''
# ********************************************************

from care_user.businessView.businessView import *
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException

class AdviceAndHealthView(Common):
    health_view = (By.ID, 'com.wdkl.capacity_care_user:id/ll_health_left')

    # 健康首页-注意事项
    relativeAdvice_button = (By.ID, 'com.wdkl.capacity_care_user:id/relative_advice')
    adviceTime_text = (By.ID, 'com.wdkl.capacity_care_user:id/advice_send_time')
    adviceContent_text = (By.ID, 'com.wdkl.capacity_care_user:id/advice_send_content')
    adviceDoctorName_text = (By.ID, 'com.wdkl.capacity_care_user:id/advice_doctor_name')

    # 健康首页-健康宣告
    relativeHealth_button = (By.ID, 'com.wdkl.capacity_care_user:id/relative_health')
    healthTime_text = (By.ID, 'com.wdkl.capacity_care_user:id/health_send_time')
    healthContent_text = (By.ID, 'com.wdkl.capacity_care_user:id/health_send_content')
    healthDoctorName_text = (By.ID, 'com.wdkl.capacity_care_user:id/health_doctor_name')


    # 医生界面
    doctorName_text = (By.ID, 'com.wdkl.capacity_care_user:id/doctor_name')

    adviceTime2_text = (By.ID, 'com.wdkl.capacity_care_user:id/send_time')
    adviceContent2_text = (By.ID, 'com.wdkl.capacity_care_user:id/send_content')

    healthTitleName_text = (By.ID, 'com.wdkl.capacity_care_user:id/title_name')
    healthTime2_text = (By.ID, 'com.wdkl.capacity_care_user:id/time_str')


    # 注意事项
    adviceDoctorName = ''
    adviceTime = ''
    adviceTime2 = ''
    adviceContent = ''
    adviceContent2 = ''

    # 医生
    doctorName = ''

    # 健康宣教
    healthTime = ''
    healthTime2 = ''
    healthContent = ''
    healthTitleName = ''

    def advice_action(self):
        logging.info('=============查看注意事项=============')

        try:
            self.find_element(*self.relativeAdvice_button)
        except NoSuchElementException:
            logging.info('=============没有注意事项=============')
        else:
            # 获取健康界面注意事项相关信息
            self.adviceDoctorName = self.find_element(*self.adviceDoctorName_text).text
            self.adviceTime = self.find_element(*self.adviceTime_text).text
            self.adviceContent = self.find_element(*self.adviceContent_text).text

            self.find_element(*self.relativeAdvice_button).click()

            # 点击注意事项
            time.sleep(3)
            logging.info('=============点击注意事项=============')
            self.touch_tap(0.6, 0.465, 500)

            # 获取医生界面注意事项相关信息
            self.doctorName = self.find_element(*self.doctorName_text).text
            self.adviceTime2 = (self.find_elements(*self.adviceTime2_text)[0].text)[:10]
            self.adviceContent2 = self.find_elements(*self.adviceContent2_text)[0].text

            self.back()

    def check_advice(self):
        logging.info('=============健康界面注意事项医生名字：%s=============' % self.adviceDoctorName)
        logging.info('=============健康界面注意事项日期：%s=============' % self.adviceTime)
        logging.info('=============健康界面注意事项内容：%s=============' % self.adviceContent)

        logging.info('=============医生界面医生名字：%s=============' % self.doctorName)
        logging.info('=============医生界面注意事项日期：%s=============' % self.adviceTime2)
        logging.info('=============医生界面注意事项内容：%s=============' % self.adviceContent2)

        # if self.adviceTime == self.adviceTime2 and self.adviceContent == self.adviceContent2 and self.adviceDoctorName == self.doctorName:
        if self.adviceTime == self.adviceTime2 and self.adviceContent == self.adviceContent2:
            logging.info('=============注意事项相关信息相同=============')
            return True

        else:
            self.getScreenShot("医生界面截图-注意事项")
            self.back()
            self.getScreenShot("健康界面截图-注意事项")
            return False



    def health_action(self):
        logging.info('=============查看健康宣教=============')

        try:
            self.find_elements(*self.relativeHealth_button)
        except NoSuchElementException:
            logging.info('=============没有健康宣教=============')
        else:
            # 获取健康界面健康宣教相关信息
            self.healthDoctorName = self.find_element(*self.healthDoctorName_text).text
            self.healthTime = self.find_element(*self.healthTime_text).text
            self.healthContent = self.find_element(*self.healthContent_text).text

            self.find_element(*self.relativeHealth_button).click()

            # 获取医生界面健康宣教相关信息
            self.doctorName = self.find_element(*self.doctorName_text).text
            self.healthTime2 = (self.find_elements(*self.healthTime2_text)[0].text)[:10]
            self.healthTitleName = self.find_elements(*self.healthTitleName_text)[0].text

            # 点击健康宣教
            self.find_elements(*self.healthTitleName_text)[0].click()
            self.back()

            self.back()

    def check_health(self):
        logging.info('=============健康界面健康宣教医生名字：%s=============' % self.healthDoctorName)
        logging.info('=============健康界面健康宣教日期：%s=============' % self.healthTime)
        logging.info('=============健康界面健康宣教标题：%s=============' % self.healthContent)

        logging.info('=============医生界面医生名字：%s=============' % self.doctorName)
        logging.info('=============时间日期：%s=============' % self.healthTime2)
        logging.info('=============医生界面注健康宣教标题：%s=============' % self.healthTitleName)

        # if self.healthTime == self.healthTime2 and self.healthContent == self.healthTitleName and self.healthDoctorName == self.doctorName:
        if self.healthTime == self.healthTime2 and self.healthContent == self.healthTitleName:
            logging.info('=============健康宣教相关信息相同=============')
            return True

        else:
            self.getScreenShot("医生界面截图-健康宣教")
            self.back()
            self.getScreenShot("健康界面截图-健康宣教")
            return False



    def login_health(self):
        l = BusinessView(self.driver)
        a = l.healthView()
        return a


if __name__ == '__main__':
    driver = appium_desired()
    l = AdviceAndHealthView(driver)
    l.login_health()
    l.advice_action()
    l.check_advice()
    l.health_action()
    l.check_health()