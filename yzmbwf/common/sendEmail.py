#!/usr/bin/env python

# encoding: utf-8
'''
    @author: Vothin
    @software: 自动化测试
    @file: sendEmail.py
    @time: 2019/10/31 12:01
    @desc:
'''
# ********************************************************

from yzmbwf.common.getConfig import ConfigData
from yzmbwf.common.recordlog import logs
from yzmbwf.base.globalpath import attach_path

import smtplib
from email.mime.text import MIMEText    # 构建邮件格式
from email.mime.multipart import MIMEMultipart  # 带附件

class SendEmail(object):

    conf = ConfigData()

    def __init__(self):
        self.host = self.conf.get_email('host')
        self.send_eml = self.conf.get_email('sender_email')
        self.passwd = self.conf.get_email('password')
        self.recipient_list = self.conf.get_recipients('recipients')
        self.subject = self.conf.get_email('subject')
        self.contet = self.conf.get_email('emicontent')



