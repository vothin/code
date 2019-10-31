#!/usr/bin/env python

# encoding: utf-8
'''
    @author: Vothin
    @software: 自动化测试
    @file: test_advice.py
    @time: 2019/9/23 10:06
    @desc:
'''
# ********************************************************

from care_user.common.start_end import StartAndEnd
from care_user.businessView.adviceAndHealthView import AdviceAndHealthView
import unittest
import logging
import random as r

class TestAdviceAndHealth(StartAndEnd):

    def test_advice(self):
        """
            测试首页注意事项
        :return:
        """

        a = r.randint(1, 10)
        logging.info('=============%s次测试首页注意事项=============' % a)
        l = AdviceAndHealthView(self.driver)

        self.assertTrue(l.login_health())

        for i in range(a):
            l.advice_action()
            self.assertTrue(l.check_advice())

    @unittest.skip
    def test_health(self):
        '''
            测试首页健康宣教
        :return:
        '''
        a = r.randint(1, 10)
        logging.info('=============%s次测试首页健康宣教=============' % a)
        l = AdviceAndHealthView(self.driver)

        self.assertTrue(l.login_health())

        for i in range(a):
            l.health_action()
            self.assertTrue(l.check_health())

if __name__ == '__main__':
    unittest.main()