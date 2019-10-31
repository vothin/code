#!/usr/bin/env python

# encoding: utf-8
'''
    @author: Vothin
    @software: 练习自动化测试
    @file: test_login.py
    @time: 2019/8/21 15:41
    @desc:
'''
# ********************************************************

from care_doctor.common.start_end import StartEnd
from care_doctor.businessView.loginView import LoginView
import unittest
import logging

class TestLogin(StartEnd):
    csv_file = '../data/login.csv'

    # @unittest.skip('跳过')
    def test_login_1(self):
        '''
            测试登录账号16312345678
        :return:
        '''
        logging.info('=============测试登录16312345678=============')
        l = LoginView(self.driver)
        data = l.get_csv_data(self.csv_file, 2)
        l.login_action(data[0], data[1])

        # 断言是否登录成功
        self.assertTrue(l.check_loginStatus())

    # @unittest.skip('跳过')
    def test_login_2(self):
        '''
            测试登录账号16212345678
        :return:
        '''
        logging.info('=============测试登录16212345678=============')
        l = LoginView(self.driver)
        data = l.get_csv_data(self.csv_file, 1)
        l.login_action(data[0], data[1])

        # 断言是否登录成功
        self.assertTrue(l.check_loginStatus())

    # @unittest.skip('跳过')
    def test_login_3(self):
        '''
            测试登录账号16512345678
        :return:
        '''
        logging.info('=============测试登录16512345678=============')
        l = LoginView(self.driver)
        data = l.get_csv_data(self.csv_file, 3)
        l.login_action(data[0], data[1])

        # 断言是否登录成功
        self.assertTrue(l.check_loginStatus())

    # @unittest.skip('跳过')
    def test_login_4(self):
        '''
            测试登录账号15502043438
        :return:
        '''
        logging.info('=============测试登录15502043438=============')
        l = LoginView(self.driver)
        data = l.get_csv_data(self.csv_file, 4)
        l.login_action(data[0], data[1])

        # 断言是否登录成功
        self.assertTrue(l.check_loginStatus())

    # @unittest.skip('跳过')
    def test_login_error(self):
        '''
            测试错误账号登录
        :return:
        '''
        logging.info('=============测试错误账号登录=============')
        l = LoginView(self.driver)
        data = l.get_csv_data(self.csv_file, 5)
        l.login_action(data[0], data[1])

        # 断言是否登录成功
        self.assertFalse(l.check_loginStatus(), msg='登录失败')

if __name__ == '__main__':
    unittest.main()