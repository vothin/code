#!/usr/bin/env python

# encoding: utf-8
'''
    @author: Vothin
    @software: 自动化测试
    @file: test_login.py
    @time: 2019/9/11 10:43
    @desc:
'''
# ********************************************************

from care_user.common.start_end import StartAndEnd
from care_user.businessView.loginAndLogoutView import LoginAndLogoutView
import unittest
import logging

class TestLogin(StartAndEnd):
    csv_file = r'../data/login.csv'

    def test_login_1(self):
        '''
            测试登录
                账号：13412345678
                密码：123456
        :return:
        '''
        # logging.info('=============测试登录13412345678=============')
        # l = LoginAndLogoutView(self.driver)
        # data = l.get_csv_data(self.csv_file, 1)
        # l.login_action(data[0], data[1])

        logging.info('=============测试登录13412345678=============')
        l = LoginAndLogoutView(self.driver)
        l.login_action('13412345678', '123456')

        # 断言是否登录成功
        self.assertTrue(l.check_login())

    def test_login_2(self):
        '''
            测试登录
                账号：13512345678
                密码：123456
        :return:
        '''
        # logging.info('=============测试登录13512345678=============')
        # l = LoginAndLogoutView(self.driver)
        # data = l.get_csv_data(self.csv_file, 2)
        # l.login_action(data[0], data[1])

        logging.info('=============测试登录13512345678=============')
        l = LoginAndLogoutView(self.driver)
        l.login_action('13512345678', '123456')

        self.assertTrue(l.check_login())

    def test_login_3(self):
        '''
            测试登录
                账号：15502043438
                密码：123456
        :return:
        '''
        # logging.info('=============测试登录15502043438=============')
        # l = LoginAndLogoutView(self.driver)
        # data = l.get_csv_data(self.csv_file, 3)
        # l.login_action(data[0], data[1])

        logging.info('=============测试登录15502043438=============')
        l = LoginAndLogoutView(self.driver)
        l.login_action('15502043438', '123456')

        self.assertTrue(l.check_login())

    def test_login_4(self):
        '''
            测试错误账号登录
                账号：15161543145
                密码：123456
        :return:
        '''
        # logging.info('=============测试登录15161543145=============')
        # l = LoginAndLogoutView(self.driver)
        # data = l.get_csv_data(self.csv_file, 4)
        # l.login_action(data[0], data[1])

        logging.info('=============测试登录15161543145=============')
        l = LoginAndLogoutView(self.driver)
        l.login_action('15161543145', '123456')

        self.assertTrue(l.check_login())

if __name__ == '__main__':
    unittest.main()