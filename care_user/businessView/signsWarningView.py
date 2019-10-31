#!/usr/bin/env python

# encoding: utf-8
'''
    @author: Vothin
    @software: 自动化测试
    @file: signsWarningView.py
    @time: 2019/9/29 9:23
    @desc:
'''
# ********************************************************

from care_user.businessView.businessView import *
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException

class SignsWarningView(Common):

    # 健康界面
    healthTodayTitle_text = (By.ID, 'com.wdkl.capacity_care_user:id/tv_health_body_title')
    healthTodayUnit_text = (By.ID, 'com.wdkl.capacity_care_user:id/tv_today_other_unit')
    healthTodayWrite_button = (By.ID, 'com.wdkl.capacity_care_user:id/img_today_other_two')

    signsWarningYellow1_text = (By.ID, 'com.wdkl.capacity_care_user:id/tv_yellow')
    signsWarningGreen1_text  = (By.ID, 'com.wdkl.capacity_care_user:id/tv_green')
    signsWarningRed1_text    = (By.ID, 'com.wdkl.capacity_care_user:id/tv_red')

    signsWarningYellow2_text = (By.ID, 'com.wdkl.capacity_care_user:id/tv_yellow2')
    signsWarningGreen2_text  = (By.ID, 'com.wdkl.capacity_care_user:id/tv_green2')
    signsWarningRed2_text    = (By.ID, 'com.wdkl.capacity_care_user:id/tv_red2')

    # 体征界面
    signsWarning_button = (By.ID, 'com.wdkl.capacity_care_user:id/img_right')

    # 体征告警界面
    signsWarningTitle1_text = (By.ID, 'com.wdkl.capacity_care_user:id/tv_title01')
    signsWarningTitle2_text = (By.ID, 'com.wdkl.capacity_care_user:id/tv_title02')
    signsWarningTitle3_text = (By.ID, 'com.wdkl.capacity_care_user:id/tv_title03')

    signsWarningDown1_text = (By.ID, 'com.wdkl.capacity_care_user:id/tv_down01')
    signsWarningDown2_text = (By.ID, 'com.wdkl.capacity_care_user:id/tv_down02')
    signsWarningDown3_text = (By.ID, 'com.wdkl.capacity_care_user:id/tv_down03')

    signsWarningUp1_text = (By.ID, 'com.wdkl.capacity_care_user:id/tv_up01')
    signsWarningUp2_text = (By.ID, 'com.wdkl.capacity_care_user:id/tv_up02')
    signsWarningUp3_text = (By.ID, 'com.wdkl.capacity_care_user:id/tv_up03')

    signsWarningOptions1_choose = (By.ID, 'com.wdkl.capacity_care_user:id/options1')
    signsWarningOptions2_choose = (By.ID, 'com.wdkl.capacity_care_user:id/options2')

    signsWarningBtn_button = (By.ID, 'com.wdkl.capacity_care_user:id/btnSubmit')

    test = (By.ID, 'com.wdkl.capacity_care_user:id/tv_alarm_titile')
    test2 = (By.ID, 'com.wdkl.capacity_care_user:id/toolbar_title')
    test3 = (By.CLASS_NAME, 'android.widget.TextView')

    # 健康界面
    healthTodayTitle= ''

    signsWarningYellow1 = ''
    signsWarningYellow2 = ''
    signsWarningGreen1  = ''
    signsWarningGreen2  = ''
    signsWarningRed1    = ''
    signsWarningRed2    = ''

    # 体征告警界面
    signsWarningTitle1 = ''
    signsWarningTitle2 = ''
    signsWarningTitle3 = ''

    signsWarningDown1 = ''
    signsWarningDown2 = ''
    signsWarningDown3 = ''

    signsWarningUp1 = ''
    signsWarningUp2 = ''
    signsWarningUp3 = ''


    def blooseGlucoseWarning(self):
        # 进入体征界面
        logging.info('=============进入血糖界面===========')
        self.find_elements(*self.healthTodayWrite_button)[0].click()

        # 进入体征告警界面
        logging.info('=============进入体征告警界面===========')
        self.find_element(*self.signsWarning_button).click()

        # 设置体征告警
        logging.info('=============设置体征告警===========')
        a = self.find_elements(self.test3)[0].text
        print(a)


        # r = random.randint(81)
        # l = self.get_size()
        # x1 = l[0] * 0.25
        # y1 = l[1] * 0.2
        # y2 = l[1] * 0.3
        # self.swipe(x1, y1, x1, y2, 1000)



    def login_health(self):
        l = BusinessView(self.driver)
        a = l.healthView()
        return a

if __name__ == '__main__':
    driver = appium_desired()
    l = SignsWarningView(driver)
    k = l.login_health()
    if k == False:
        print("登录失败")
    else:
        l.blooseGlucoseWarning()