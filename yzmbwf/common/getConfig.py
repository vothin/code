#!/usr/bin/env python

# encoding: utf-8
'''
    @author: Vothin
    @software: 自动化测试
    @file: getConfig.py
    @time: 2019/10/28 14:38
    @desc:
'''
# ********************************************************

import configparser
from yzmbwf.common.recordlog import logs
from yzmbwf.base.globalpath import config_path

class ConfigData(object):

    def __init__(self):
        self.conf = self.get_config_obj()

    # 读取配置文件config_path
    def get_config_obj(self):
        conf_obj = configparser.ConfigParser()
        conf_obj.read(config_path, encoding='utf-8')
        return conf_obj

    # 获取配置文件的值
    def get_value(self, sec_name, opt_name):
        try:
            return self.conf.get(sec_name, opt_name)
        except Exception as e:
            logs.error(e)

    # 获得邮件
    def get_email(self, optn):
        eml_name = self.conf.sections()[0]
        return self.get_value(eml_name, optn)

    # 获取收件人
    def get_recipients(self, opname):
        rec = self.get_email(opname)
        if rec != None:
            # re = rec.spilt(',')
            re = rec
            return re
        else:
            return None

if __name__ == '__main__':
    c = ConfigData()
    result = c.get_value('email', 'host')
    # result = c.get_value('email', 'sender_email')
    # result = c.get_recipients('recipients')
    # result = c.get_email('subject')
    print(result)