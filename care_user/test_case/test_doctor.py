#!/usr/bin/env python

# encoding: utf-8
'''
    @author: Vothin
    @software: 自动化测试
    @file: test_doctorChange.py
    @time: 2019/9/30 9:48
    @desc:
'''
# ********************************************************

from care_user.common.start_end import StartAndEnd
from care_user.businessView.doctorView import DoctorView
import unittest
import logging
import random as z

class TestDotcorChange(StartAndEnd):

    def test_doctorChange(self):
        """
            测试切换医生
        :return:
        """

        a = z.randint(1, 10)
        logging.info('=============%s次测试首页注意事项=============' % a)
        l = DoctorView(self.driver)

        self.assertTrue(l.login_doctor())

        for i in range(a):
            l.doctorView()
            self.assertTrue(l.check_doctorView())

if __name__ == '__main__':
    unittest.main()