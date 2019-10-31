#!/usr/bin/env python

# encoding: utf-8
'''
    @author: Vothin
    @software: 自动化测试
    @file: test_cloudDPage.py
    @time: 2019/10/17 15:54
    @desc:
'''
# ********************************************************

from care_user.common.start_end import StartAndEnd
from care_user.businessView.cloudDPageView import CloudDPage
import unittest
import logging, time
import random as r


class TestCloudDPage(StartAndEnd):

    # @unittest.skip
    def test_blogPostAttention(self):
        """
            测试关注
        :return:
        """
        logging.info('=============测试关注=============')
        l = CloudDPage(self.driver)

        self.assertTrue(l.login_cloudD())

        l.blogPostAttention()
        time.sleep(3)
        self.assertTrue(l.check_blogPostAttention())

    # @unittest.skip
    def test_blogPostLike(self):
        """
            测试点赞
        :return:
        """
        logging.info('=============测试点赞=============')
        l = CloudDPage(self.driver)

        self.assertTrue(l.login_cloudD())

        l.blogPostLike()
        time.sleep(3)
        self.assertTrue(l.check_blogPostLike())

    # @unittest.skip
    def test_blogPostRely(self):
        """
            测试回复
        :return:
        """
        logging.info('=============测试回复帖子=============')
        l = CloudDPage(self.driver)

        self.assertTrue(l.login_cloudD())

        l.blogPostReply('hello')
        time.sleep(3)
        self.assertTrue(l.check_blogPostReply())

    # @unittest.skip
    def test_blogPostRelyDel(self):
        """
            测试删除回复
        :return:
        """
        logging.info('=============测试删除=============')
        l = CloudDPage(self.driver)

        self.assertTrue(l.login_cloudD())

        l.blogPostReplyDel()
        time.sleep(3)
        # self.assertTrue(l.check_blogPostReplyDel())

    # @unittest.skip
    def test_blogPostCollect(self):
        """
            测试收藏
        :return:
        """
        logging.info('=============测试收藏=============')
        l = CloudDPage(self.driver)

        self.assertTrue(l.login_cloudD())

        l.blogPostCollect()
        time.sleep(3)
        self.assertTrue(l.check_blogPostCollect())


if __name__ == '__main__':
    unittest.main()