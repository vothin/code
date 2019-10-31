#!/usr/bin/env python

# encoding: utf-8
'''
    @author: Vothin
    @software: 自动化测试
    @file: doctorView.py
    @time: 2019/9/27 15:01
    @desc:
'''
# ********************************************************

from care_user.businessView.businessView import *
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException

class DoctorView(Common):

    # 医生界面
    doctorSelect_button = (By.ID, 'com.wdkl.capacity_care_user:id/tv_select')

    doctorName_text = (By.ID, 'com.wdkl.capacity_care_user:id/doctor_name')
    doctorPhone_text = (By.ID, 'com.wdkl.capacity_care_user:id/shp_phone')
    doctorAge_text = (By.ID, 'com.wdkl.capacity_care_user:id/tv_doctor_age')
    doctorSex_text = (By.ID, 'com.wdkl.capacity_care_user:id/shp_name')
    doctorExperience_text = (By.ID, 'com.wdkl.capacity_care_user:id/tv_working_time')

    doctorShopName_text = (By.ID, 'com.wdkl.capacity_care_user:id/tv_shop_name')
    doctorShopMobile_text = (By.ID, 'com.wdkl.capacity_care_user:id/tv_shop_mobile')
    doctorShopAddress_text = (By.ID, 'com.wdkl.capacity_care_user:id/tv_shop_address')

    doctorRight_button = (By.ID, 'com.wdkl.capacity_care_user:id/iv_more')
    doctorSetingChiel_button = (By.ID, 'com.wdkl.capacity_care_user:id/tv_setting_doctor')
    doctorChange_button = (By.ID, 'com.wdkl.capacity_care_user:id/tv_change_doctor')
    doctorUnbinding_button = (By.ID, 'com.wdkl.capacity_care_user:id/tv_unbinding_doctor')

    # 医生详情界面
    doctorDetailName_text = (By.ID, 'com.wdkl.capacity_care_user:id/tv_doctor_name')
    doctorDetailSex_text = (By.ID, 'com.wdkl.capacity_care_user:id/tv_doctor_sex')
    doctorDetailMobile_text = (By.ID, 'com.wdkl.capacity_care_user:id/tv_doctor_mobile')
    doctorDetailExperience_text = (By.ID, 'com.wdkl.capacity_care_user:id/tv_doctor_experience')

    # 机构详情界面
    doctorShopDetailName_text = (By.ID, 'com.wdkl.capacity_care_user:id/tv_shop_name')
    doctorShopDetailMobile_text = (By.ID, 'com.wdkl.capacity_care_user:id/tv_shop_mobile')
    doctorShopDetailAddress_text = (By.ID, 'com.wdkl.capacity_care_user:id/tv_address')


    # 医生通讯录
    doctorShop_type = (By.ID, 'com.wdkl.capacity_care_user:id/layout_shop')
    doctorTitle_text = (By.ID, 'com.wdkl.capacity_care_user:id/tv_doctor_title')
    doctorChiel_button = (By.ID, 'com.wdkl.capacity_care_user:id/layout_doctor')
    doctorTitleName_text = (By.ID, 'com.wdkl.capacity_care_user:id/tv_doctor_name')
    doctorShopTitleName_text = (By.ID, 'com.wdkl.capacity_care_user:id/tv_shop_name')

    # 医生
    doctorName = ''
    doctorPhone = ''
    doctorAge = ''
    doctorSex = ''
    doctorExperience = ''

    doctorShopName = ''
    doctorShopMobile = ''
    doctorShopAddress = ''

    # 医生通讯录
    doctorTitle = ''
    doctorTitleName = ''
    doctorShopTitleName = ''
    doctorFormName = ''
    doctorFormShop = ''

    # 医生详情
    doctorDetailName = ''
    doctorDetailSex = ''
    doctorDetailMobile = ''
    doctorDetailExperience = ''

    # 机构详情
    doctorShopDetailName = ''
    doctorShopDetailMobile = ''
    doctorShopDetailAddress = ''

    def doctorView(self):
        check = self.check_doctor()
        if check == True:

            self.doctorName = self.find_element(*self.doctorName_text).text

            self.doctorPhone = self.find_element(*self.doctorPhone_text).text
            self.doctorSex = self.find_element(*self.doctorSex_text).text
            self.doctorExperience = (self.find_element(*self.doctorExperience_text).text)[2:]

            logging.info('=============医生界面的医生名字为：%s=============' % self.doctorName)
            logging.info('=============医生界面的医生号码为：%s=============' % self.doctorPhone)
            logging.info('=============医生界面的医生性别为：%s=============' % self.doctorSex)
            logging.info('=============医生界面的医生经验为：%s=============' % self.doctorExperience)


            self.doctorShopName = self.find_element(*self.doctorShopTitleName_text).text
            self.doctorShopMobile = self.find_element(*self.doctorShopMobile_text).text
            self.doctorShopAddress = self.find_element(*self.doctorShopAddress_text).text

            logging.info('=============医生界面的机构名称为：%s=============' % self.doctorShopName)
            logging.info('=============医生界面的机构号码为：%s=============' % self.doctorShopMobile)
            logging.info('=============医生界面的机构地址为：%s=============' % self.doctorShopAddress)


            logging.info('=============点击医生详情=============')
            self.find_element(*self.doctorName_text).click()

            self.doctorDetailName = self.find_element(*self.doctorDetailName_text).text
            self.doctorDetailMobile = self.find_element(*self.doctorDetailMobile_text).text
            self.doctorDetailSex = self.find_element(*self.doctorDetailSex_text).text
            self.doctorDetailExperience = self.find_element(*self.doctorDetailExperience_text).text

            logging.info('=============医生详情的医生名字为：%s=============' % self.doctorDetailName)
            logging.info('=============医生详情的医生号码为：%s=============' % self.doctorDetailMobile)
            logging.info('=============医生详情的医生性别为：%s=============' % self.doctorDetailSex)
            logging.info('=============医生详情的医生经验为：%s=============' % self.doctorDetailExperience)


            self.back()

            logging.info('=============点击机构详情=============')
            self.find_element(*self.doctorShopName_text).click()

            self.doctorShopDetailName = self.find_element(*self.doctorShopDetailName_text).text
            self.doctorShopDetailMobile = self.find_element(*self.doctorShopDetailMobile_text).text
            self.doctorShopDetailAddress = self.find_element(*self.doctorShopDetailAddress_text).text

            logging.info('=============机构详情的机构名称为：%s=============' % self.doctorShopDetailName)
            logging.info('=============机构详情的机构号码为：%s=============' % self.doctorShopDetailMobile)
            logging.info('=============机构详情的机构经验为：%s=============' % self.doctorShopDetailAddress)


            self.back()

            logging.info('=============点击右上角=============')
            self.find_element(*self.doctorRight_button).click()

            try:
                self.find_element(*self.doctorSetingChiel_button)
            except NoSuchElementException:
                logging.info('=============当前医生已经是首席医生=============')
                self.find_element(*self.doctorChange_button).click()
            else:
                logging.info('=============当前医生为首席医生=============')
                self.find_element(*self.doctorSetingChiel_button).click()
                self.find_element(*self.doctorRight_button).click()
                self.find_element(*self.doctorChange_button).click()


            finally:
                self.doctorTitleName = self.find_elements(*self.doctorTitleName_text)[0].text
                self.doctorShopTitleName = self.find_elements(*self.doctorShopTitleName_text)[0].text

                logging.info('=============通讯录的首席医生为：%s=============' % self.doctorTitleName)
                logging.info('=============通讯录的首席医生机构为：%s=============' % self.doctorShopTitleName)

                self.find_element(*self.doctorChiel_button).click()


    def check_doctorView(self):

        if self.doctorName == '':
            logging.error('没有绑定医生')
            self.getScreenShot('医生通讯录')
            self.back()
            return False

        elif self.doctorName == self.doctorTitleName == self.doctorDetailName \
            and self.doctorPhone == self.doctorDetailMobile \
            and self.doctorSex == self.doctorDetailSex \
            and self.doctorExperience == self.doctorDetailExperience \
            and self.doctorShopName == self.doctorShopTitleName == self.doctorShopDetailName \
            and self.doctorShopMobile == self.doctorShopDetailMobile \
            and self.doctorShopAddress == self.doctorShopDetailAddress:

            logging.info('=============医生相关数据相同=============')
            return True

        else:
            logging.error('医生相关数据不相同')
            self.getScreenShot('医生通讯录')
            self.back()
            self.getScreenShot('医生界面')
            self.back()
            self.find_element(*self.doctorName_text).click()
            self.getScreenShot('医生详情界面')
            self.back()
            self.find_element(*self.doctorShopName_text).click()
            self.getScreenShot('机构详情界面')
            self.back()
            return False


    def login_doctor(self):
        l = BusinessView(self.driver)
        a = l.doctorView()
        return a

    def check_doctor(self):
        k = BusinessView(self.driver)
        b = k.doctorCheck(-1)
        return b


if __name__ == '__main__':
    driver = appium_desired()
    l = DoctorView(driver)
    l.login_doctor()
    for i in range(1):
        l.doctorView()
        l.check_doctorView()
