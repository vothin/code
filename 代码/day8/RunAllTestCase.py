# coding=utf-8
from Public import HTMLTestRunner as HTMLTestRunner  # 导入官网的测试报告
import unittest, time
from Public.SendMail import *        # 邮件
import os

if __name__ == '__main__':

    # 执行用例部分
    test_dir = os.path.join(os.getcwd(), 'TestCase')   # 用例路径
    test_report = os.path.join(os.getcwd(), 'Report')  # 测试报告存放路径
    discover = unittest.defaultTestLoader.discover(test_dir, pattern='test*.py')

    # 1.定制时间格式，2.测试报告的名字定制
    now = time.strftime("%Y-%m-%d_%H_%M_%S")
    filename = test_report + '/Ecshop_' + now + '.html'

    # 在开这个文件，给于写入权限
    fp = open(filename, 'wb')

    try:
        # stream=fp：文件路径，名字  title:输出测试报告的名字 description：描述名字，相当于备注信息
        runner = HTMLTestRunner.HTMLTestRunner(stream=fp, title="Ecshop自动化测试报告", description='用例执行情况：')
        runner.run(discover)
        fp.close()
        SendMail(filename, "85642914@qq.com")
    except:
        fp.close()
        SendMail(filename, "85642914@qq.com")

