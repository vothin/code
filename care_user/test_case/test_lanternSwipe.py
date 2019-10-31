#!/usr/bin/env python

# encoding: utf-8
'''
    @author: Vothin
    @software: 自动化测试
    @file: test_lanternSwipe.py
    @time: 2019/9/18 15:36
    @desc:
'''
# ********************************************************

from care_user.common.start_end import StartAndEnd
from care_user.businessView.lanternSideView import LanternSideView
import unittest
import logging
import random as r

class TestLanternSwipe(StartAndEnd):
    def test_lanternSwipe_1(self):
        '''
            测试随机左滑
        :return:
        '''
        a = r.randint(1, 10)
        logging.info('=============%s次随机左滑=============' % a)
        l = LanternSideView(self.driver)

        self.assertTrue(l.login_health())

        for i in range(a):
            l.lanternSwipeLeft()
        l.lanternSwipeClick()

    def test_lanternSwipe_2(self):
        '''
            测试随机右滑
        :return:
        '''
        a = r.randint(1, 10)
        logging.info('=============%s次右滑=============' % a)
        l = LanternSideView(self.driver)

        self.assertTrue(l.login_health())

        for i in range(a):
            l.lanternSwipeRight()
        l.lanternSwipeClick()


if __name__ == '__main__':
    unittest.main()

