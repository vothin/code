#!/usr/bin/env python

# encoding: utf-8
'''
    @author: Vothin
    @software: 自动化测试
    @file: signsDataView.py
    @time: 2019/9/23 17:04
    @desc:
'''
# ********************************************************

from care_user.businessView.businessView import *
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException


class SignsDataView(Common):

    # 健康界面-体征相关
    healthTodayTitle_text = (By.ID, 'com.wdkl.capacity_care_user:id/tv_health_body_title')
    healthTodayValue_text = (By.ID, 'com.wdkl.capacity_care_user:id/tv_today_other_data')
    healthTodayUnit_text = (By.ID, 'com.wdkl.capacity_care_user:id/tv_today_other_unit')
    healthTodayWrite_button = (By.ID, 'com.wdkl.capacity_care_user:id/img_today_other_two')

    # 体征界面-体征相关
    # 血糖专属
    healthBodyValue00_choose = (By.ID, 'com.wdkl.capacity_care_user:id/et_value')

    healthBodyValue01_input = (By.ID, 'com.wdkl.capacity_care_user:id/et_value01')
    healthBodyValue02_input = (By.ID, 'com.wdkl.capacity_care_user:id/et_value02')

    # 时间
    healthBodyValue03_input = (By.ID, 'com.wdkl.capacity_care_user:id/et_value03')

    healthBodySave_button = (By.ID, 'com.wdkl.capacity_care_user:id/tv_save')
    healthBodyBtn_button = (By.ID, 'com.wdkl.capacity_care_user:id/btnSubmit')

    healthBodyNumber_text = (By.ID, 'com.wdkl.capacity_care_user:id/tv_number')
    healthBodyUnit_text = (By.ID, 'com.wdkl.capacity_care_user:id/tv_unit')
    healthBodyTypeTime_text = (By.ID, 'com.wdkl.capacity_care_user:id/tv_type_time')

    # 健康界面-数值
    healthTodayTitle = ''
    healthTodayValue = ''
    healthTodayUnit = ''

    # 体征界面-数值
    healthBodyTitle = ''
    healthBodyValue = ''
    healthBodyUnit = ''

    # 体征界面-输入
    healthBodyTitleInput = ''
    healthBodyValueInput = ''
    healthBodyUnitInput = ''


    # 血糖
    def bloodGlucose(self, value, b):
        # 进入血糖
        logging.info('=============进入血糖界面===========')
        self.find_elements(*self.healthTodayWrite_button)[0].click()

        # 输入血糖
        # 输入相关数据

        logging.info('=============选择餐前后：%s============' % b)

        logging.info('=============输入血糖值：%s=============' % value)
        self.find_element(*self.healthBodyValue00_choose).click()
        l = self.get_size()
        if b == '餐前半小时':
            self.find_element(*self.healthBodyBtn_button).click()
        elif b == '餐后1小时':
            l = self.get_size()
            x1 = l[0] * 0.5
            y1 = l[1] * 0.9
            y2 = l[1] * 0.88
            self.swipe(x1, y1, x1, y2, 1000)
            self.find_element(*self.healthBodyBtn_button).click()
        elif b == '餐后2小时':
            l = self.get_size()
            x1 = l[0] * 0.5
            y1 = l[1] * 0.9
            y2 = l[1] * 0.8
            self.swipe(x1, y1, x1, y2, 1000)
            self.find_element(*self.healthBodyBtn_button).click()

        self.find_element(*self.healthBodyValue01_input).send_keys(value)

        self.healthBodyTitleInput = '血糖'
        self.healthBodyValueInput = str(float(value))
        self.healthBodyUnitInput = (self.find_element(*self.healthBodyUnit_text).text) \
                                   + ' ' + b

        self.find_element(*self.healthBodySave_button).click()

        # 健康界面-血糖
        self.healthTodayTitle = self.find_elements(*self.healthTodayTitle_text)[0].text
        self.healthTodayValue = self.find_elements(*self.healthTodayValue_text)[0].text
        self.healthTodayUnit = self.find_elements(*self.healthTodayUnit_text)[0].text

        # 体征界面-血糖
        self.find_elements(*self.healthTodayWrite_button)[0].click()
        self.healthBodyTitle = '血糖'
        self.healthBodyValue = str(float(self.find_elements(*self.healthBodyNumber_text)[0].text))
        self.healthBodyUnit = self.find_elements(*self.healthBodyUnit_text)[0].text \
                              + ' ' + (self.find_elements(*self.healthBodyTypeTime_text)[0].text)
        self.back()


    # 血压
    def bloodPressure(self, value1, value2):
        # 进入血压
        logging.info('=============进入血压界面===========')
        self.find_elements(*self.healthTodayWrite_button)[1].click()

        # 输入血压
        logging.info('=============输入舒张压值：%s=============' % value1)
        logging.info('=============输入收缩压值：%s=============' % value2)

        self.find_element(*self.healthBodyValue01_input).send_keys(value1)
        self.find_element(*self.healthBodyValue02_input).send_keys(value2)

        self.healthBodyTitleInput = '血压'
        self.healthBodyValueInput = str(float(value1)) + '/' + str(float(value2))
        self.healthBodyUnitInput = self.find_element(*self.healthBodyUnit_text).text

        self.find_element(*self.healthBodySave_button).click()

        # 健康界面-血压
        self.healthTodayTitle = self.find_elements(*self.healthTodayTitle_text)[1].text
        self.healthTodayValue = self.find_elements(*self.healthTodayValue_text)[1].text
        self.healthTodayUnit = self.find_elements(*self.healthTodayUnit_text)[1].text

        # 体征界面-血压
        self.find_elements(*self.healthTodayWrite_button)[1].click()
        self.healthBodyTitle = '血压'
        self.healthBodyValue = self.find_elements(*self.healthBodyNumber_text)[0].text
        self.healthBodyValue = (self.healthBodyValue).split('/')
        self.healthBodyValue = str(float(self.healthBodyValue[0])) + '/' + str(float(self.healthBodyValue[1]))
        self.healthBodyUnit = self.find_elements(*self.healthBodyUnit_text)[0].text

        self.back()


    # 血氧
    def bloodOxygen(self, value):
        l = self.get_size()
        x1 = l[0] * 0.5
        y1 = l[1] * 0.9
        y2 = l[1] * 0.1
        self.swipe(x1, y1, x1, y2, 1000)

        # 进入血氧
        logging.info('=============进入血氧界面===========')
        self.find_elements(*self.healthTodayWrite_button)[0].click()

        # 输入血氧
        logging.info('=============输入血氧值：%s=============' % value)

        self.find_element(*self.healthBodyValue01_input).send_keys(value)

        self.healthBodyTitleInput = '血氧'
        self.healthBodyValueInput = str(float(value))
        self.healthBodyUnitInput = self.find_element(*self.healthBodyUnit_text).text

        self.find_element(*self.healthBodySave_button).click()

        # 健康界面-血氧
        self.healthTodayTitle = self.find_elements(*self.healthTodayTitle_text)[0].text
        self.healthTodayValue = self.find_elements(*self.healthTodayValue_text)[0].text
        self.healthTodayUnit = self.find_elements(*self.healthTodayUnit_text)[0].text

        # 体征界面-血氧
        self.find_elements(*self.healthTodayWrite_button)[0].click()
        self.healthBodyTitle = '血氧'
        self.healthBodyValue = self.find_elements(*self.healthBodyNumber_text)[0].text
        self.healthBodyValue = str(float(self.healthBodyValue))
        self.healthBodyUnit = self.find_elements(*self.healthBodyUnit_text)[0].text

        self.back()


    # 脉搏
    def pulse(self, value):
        l = self.get_size()
        x1 = l[0] * 0.5
        y1 = l[1] * 0.9
        y2 = l[1] * 0.1
        self.swipe(x1, y1, x1, y2, 1000)

        # 进入脉搏
        logging.info('=============进入脉搏界面===========')
        self.find_elements(*self.healthTodayWrite_button)[1].click()

        # 输入脉搏
        logging.info('=============输入脉搏值：%s=============' % value)

        self.find_element(*self.healthBodyValue01_input).send_keys(value)

        self.healthBodyTitleInput = '脉搏'
        self.healthBodyValueInput = str(float(value))
        self.healthBodyUnitInput = self.find_element(*self.healthBodyUnit_text).text

        self.find_element(*self.healthBodySave_button).click()

        # 健康界面-脉搏
        self.healthTodayTitle = self.find_elements(*self.healthTodayTitle_text)[1].text
        self.healthTodayValue = self.find_elements(*self.healthTodayValue_text)[1].text
        self.healthTodayUnit = self.find_elements(*self.healthTodayUnit_text)[1].text

        # 体征界面-脉搏
        self.find_elements(*self.healthTodayWrite_button)[1].click()
        self.healthBodyTitle = '脉搏'
        self.healthBodyValue = self.find_elements(*self.healthBodyNumber_text)[0].text
        self.healthBodyValue = str(float(self.healthBodyValue))
        self.healthBodyUnit = self.find_elements(*self.healthBodyUnit_text)[0].text

        self.back()


    # 体温
    def animalHeat(self, value):
        l = self.get_size()
        x1 = l[0] * 0.5
        y1 = l[1] * 0.9
        y2 = l[1] * 0.1
        self.swipe(x1, y1, x1, y2, 1000)

        # 进入体温
        logging.info('=============进入体温界面===========')
        self.find_elements(*self.healthTodayWrite_button)[2].click()

        # 输入体温
        logging.info('=============输入体温值：%s=============' % value)

        self.find_element(*self.healthBodyValue01_input).send_keys(value)

        self.healthBodyTitleInput = '体温'
        self.healthBodyValueInput = str(float(value))
        self.healthBodyUnitInput = self.find_element(*self.healthBodyUnit_text).text

        self.find_element(*self.healthBodySave_button).click()

        # 健康界面-体温
        self.healthTodayTitle = self.find_elements(*self.healthTodayTitle_text)[2].text
        self.healthTodayValue = self.find_elements(*self.healthTodayValue_text)[2].text
        self.healthTodayUnit = self.find_elements(*self.healthTodayUnit_text)[2].text

        # 体征界面-体温
        self.find_elements(*self.healthTodayWrite_button)[2].click()
        self.healthBodyTitle = '体温'
        self.healthBodyValue = self.find_elements(*self.healthBodyNumber_text)[0].text
        self.healthBodyValue = str(float(self.healthBodyValue))
        self.healthBodyUnit = self.find_elements(*self.healthBodyUnit_text)[0].text

        self.back()


    # HRV
    def heartRateVariability(self, value):
        l = self.get_size()
        x1 = l[0] * 0.5
        y1 = l[1] * 0.9
        y2 = l[1] * 0.1
        self.swipe(x1, y1, x1, y2, 1000)

        # 进入HRV
        logging.info('=============进入HRV界面===========')
        self.find_elements(*self.healthTodayWrite_button)[3].click()

        # 输入HRV
        logging.info('=============输入HRV值：%s=============' % value)

        self.find_element(*self.healthBodyValue01_input).send_keys(value)

        self.healthBodyTitleInput = 'HRV'
        self.healthBodyValueInput = str(float(value))
        self.healthBodyUnitInput = self.find_element(*self.healthBodyUnit_text).text

        self.find_element(*self.healthBodySave_button).click()

        # 健康界面-HRV
        self.healthTodayTitle = self.find_elements(*self.healthTodayTitle_text)[3].text
        self.healthTodayValue = self.find_elements(*self.healthTodayValue_text)[3].text
        self.healthTodayUnit = self.find_elements(*self.healthTodayUnit_text)[3].text

        # 体征界面-HRV
        self.find_elements(*self.healthTodayWrite_button)[3].click()
        self.healthBodyTitle = 'HRV'
        self.healthBodyValue = self.find_elements(*self.healthBodyNumber_text)[0].text
        self.healthBodyValue = str(float(self.healthBodyValue))
        self.healthBodyUnit = self.find_elements(*self.healthBodyUnit_text)[0].text

        self.back()




    # 检测体征数据
    def check_signsData(self):
        logging.info('=============健康界面-体征数据标题：%s=============' % self.healthTodayTitle)
        logging.info('=============健康界面-体征数据数值：%s=============' % self.healthTodayValue)
        logging.info('=============健康界面-体征数据单位：%s=============' % self.healthTodayUnit)

        logging.info('=============体征界面-体征数据标题：%s=============' % self.healthBodyTitle)
        logging.info('=============体征界面-体征数据数值：%s=============' % self.healthBodyValue)
        logging.info('=============体征界面-体征数据单位：%s=============' % self.healthBodyUnit)

        if self.healthBodyTitleInput == self.healthTodayTitle == self.healthBodyTitle \
                and self.healthBodyValueInput == self.healthTodayValue == self.healthBodyValue \
                and self.healthBodyUnitInput == self.healthTodayUnit == self.healthBodyUnit:
            logging.info('=============体征相关信息相同=============')
            return True

        else:
            if self.healthTodayTitle == '血糖':
                logging.error('血糖相关信息不相同')
                self.getScreenShot('健康界面截图')
                self.find_elements(*self.healthTodayWrite_button)[0].click()
                self.getScreenShot('体征界面截图')
                self.back()
                return False

            elif self.healthTodayTitle == '血压':
                logging.error('血压相关信息不相同')
                self.getScreenShot('健康界面截图')
                self.find_elements(*self.healthTodayWrite_button)[1].click()
                self.getScreenShot('体征界面截图')
                self.back()
                return False

            elif self.healthTodayTitle == '血氧':
                l = self.get_size()
                x1 = l[0] * 0.5
                y1 = l[1] * 0.9
                y2 = l[1] * 0.1
                self.swipe(x1, y1, x1, y2, 1000)

                logging.error('血氧相关信息不相同')
                self.getScreenShot('健康界面截图')
                self.find_elements(*self.healthTodayWrite_button)[0].click()
                self.getScreenShot('体征界面截图')
                self.back()
                return False

            elif self.healthTodayTitle == '脉搏':
                l = self.get_size()
                x1 = l[0] * 0.5
                y1 = l[1] * 0.9
                y2 = l[1] * 0.1
                self.swipe(x1, y1, x1, y2, 1000)

                logging.error('脉搏相关信息不相同')
                self.getScreenShot('健康界面截图')
                self.find_elements(*self.healthTodayWrite_button)[1].click()
                self.getScreenShot('体征界面截图')
                self.back()
                return False

            elif self.healthTodayTitle == '体温':
                l = self.get_size()
                x1 = l[0] * 0.5
                y1 = l[1] * 0.9
                y2 = l[1] * 0.1
                self.swipe(x1, y1, x1, y2, 1000)

                logging.error('体温相关信息不相同')
                self.getScreenShot('健康界面截图')
                self.find_elements(*self.healthTodayWrite_button)[2].click()
                self.getScreenShot('体征界面截图')
                self.back()
                return False

            elif self.healthTodayTitle == 'HRV':
                l = self.get_size()
                x1 = l[0] * 0.5
                y1 = l[1] * 0.9
                y2 = l[1] * 0.1
                self.swipe(x1, y1, x1, y2, 1000)

                logging.error('HRV相关信息不相同')
                self.getScreenShot('健康界面截图')
                self.find_elements(*self.healthTodayWrite_button)[2].click()
                self.getScreenShot('体征界面截图')
                self.back()
                return False


    def login_health(self):
        l = BusinessView(self.driver)
        a = l.healthView()
        return a



if __name__ == '__main__':
    driver = appium_desired()
    l = SignsDataView(driver)
    k = l.login_health()
    if k == False:
        print("登录失败")
    else:
        a = random.randint(1, 3)

        if a == 1:
            b = '餐前半小时'
            c = random.uniform(2, 9)
            l.bloodGlucose(('%.2f' % c), b)
            l.check_signsData()
        elif a == 2:
            b = '餐后1小时'
            c = random.uniform(4, 11)
            l.bloodGlucose(('%.2f' % c), b)
            l.check_signsData()
        elif a == 3:
            b = '餐后2小时'
            c = random.uniform(2, 9)
            l.bloodGlucose(('%.2f' % c), b)
            l.check_signsData()



        c1 = random.randint(30, 120)
        c2 = random.randint(60, 170)
        l.bloodPressure(c1 ,c2)
        l.check_signsData()

        c = random.randint(85, 120)
        l.bloodOxygen(c)
        l.check_signsData()


        c = random.randint(30, 130)
        l.pulse(c)
        l.check_signsData()


        c = random.uniform(34, 39)
        l.animalHeat('%.1f' % c)
        l.check_signsData()


        c = random.randint(30, 120)
        l.heartRateVariability(c)
        l.check_signsData()





