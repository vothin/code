#!/usr/bin/env python

# encoding: utf-8
'''
    @author: Vothin
    @software: 自动化测试
    @file: test_doctorAdviceAndHealth.py
    @time: 2019/10/11 14:44
    @desc:
'''
# ********************************************************

from care_user.common.start_end import StartAndEnd
from care_user.businessView.doctorAdviceAndHealthView import DoctorAdviceAndHealth
import unittest
import logging
import random

class TestDoctorAdviceAndHealth(StartAndEnd):

    def test_doctorHealth(self):
        '''
            测试医生界面健康宣教
        :return:
        '''

        a = random.randint(1, 10)
        logging.info('=============%s次测试医生界面健康宣教=============' % a)
        l = DoctorAdviceAndHealth(self.driver)

        self.assertTrue(l.login_doctor())

        for i in range(a):
            l.doctorHealth(-1)

    def test_doctorAdvice(self):
        '''
            测试医生界面注意事项
        :return:
        '''

        a = random.randint(1, 10)
        logging.info('=============%s次测试医生界面注意事项=============' % a)
        l = DoctorAdviceAndHealth(self.driver)

        self.assertTrue(l.login_doctor())

        for i in range(a):
            l.doctorAdvice(-1)

if __name__ == '__main__':
    unittest.main()