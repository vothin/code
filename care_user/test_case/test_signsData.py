#!/usr/bin/env python

# encoding: utf-8
'''
    @author: Vothin
    @software: 自动化测试
    @file: test_signsData.py
    @time: 2019/9/25 15:27
    @desc:
'''
# ********************************************************

from care_user.common.start_end import StartAndEnd
from care_user.businessView.signsDataView import SignsDataView
import unittest
import logging
import random

class TestSignsData(StartAndEnd):

    def test_bloodGlucose(self):
        '''
            测试血糖
        :return:
        '''
        logging.info('=============测试血糖=============')
        l = SignsDataView(self.driver)

        self.assertTrue(l.login_health())

        a = random.randint(1, 3)
        if a == 1:
            b = '餐前半小时'
            c = random.uniform(2, 9)
            l.bloodGlucose(('%.2f' % c), b)

            self.assertTrue(l.check_signsData())

        elif a == 2:
            b = '餐后1小时'
            c = random.uniform(4, 11)
            l.bloodGlucose(('%.2f' % c), b)

            self.assertTrue(l.check_signsData())

        elif a == 3:
            b = '餐后2小时'
            c = random.uniform(2, 9)
            l.bloodGlucose(('%.2f' % c), b)

            self.assertTrue(l.check_signsData())

    def test_bloodPressure(self):
        '''
            测试血压
        :return:
        '''
        logging.info('=============测试血压=============')
        l = SignsDataView(self.driver)

        self.assertTrue(l.login_health())

        c1 = random.randint(30, 120)
        c2 = random.randint(60, 170)
        l.bloodPressure(c1 ,c2)

        self.assertTrue(l.check_signsData())


    def test_bloodOxygen(self):
        '''
            测试血氧
        :return:
        '''
        logging.info('=============测试血氧=============')
        l = SignsDataView(self.driver)

        self.assertTrue(l.login_health())

        c = random.randint(85, 120)
        l.bloodOxygen(c)

        self.assertTrue(l.check_signsData())


    def test_pules(self):
        '''
            测试脉搏
        :return:
        '''
        logging.info('=============测试脉搏=============')
        l = SignsDataView(self.driver)

        self.assertTrue(l.login_health())

        c = random.randint(30, 130)
        l.pulse(c)

        self.assertTrue(l.check_signsData())


    def test_animalHeart(self):
        '''
            测试体温
        :return:
        '''
        logging.info('=============测试体温=============')
        l = SignsDataView(self.driver)

        self.assertTrue(l.login_health())

        c = random.uniform(34, 39)
        l.animalHeat('%.1f' % c)

        self.assertTrue(l.check_signsData())


    def test_heartRateVariability(self):
        '''
            测试HRV
        :return:
        '''
        logging.info('=============测试HRV=============')
        l = SignsDataView(self.driver)

        self.assertTrue(l.login_health())

        c = random.randint(30, 120)
        l.heartRateVariability(c)

        self.assertTrue(l.check_signsData())




if __name__ == '__main__':
    unittest.main()