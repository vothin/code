'''
方法2
第2种调用方法：
1 自己创建一个TestSuite，
2 添加需要执行测试的TestCase，
3 然后使用TestRunner().run(suite)执行测试。
'''

from selenium import webdriver
import unittest
import time


class ut(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(10)
        self.ecshop_url_1 = "http://192.168.2.246/ecshop/user.php"

    def test_login(self):  # 第一个测试用例
        # 打开主页
        self.driver.get(self.ecshop_url_1)

        # 输入账号密码
        self.driver.find_element_by_name("username").send_keys("ts16")
        self.driver.find_element_by_name("password").send_keys("123456")

        # 单击登陆
        self.driver.find_element_by_name("submit").click()

    def test_upload(self):  # 第二个测试用例
        self.test_login()
        time.sleep(3)
        self.driver.find_element_by_xpath("//a[@href='user.php']").click()
        time.sleep(1)
        self.driver.find_element_by_xpath("//a[@href='user.php?act=message_list']").click()
        time.sleep(1)

        # 上传
        self.driver.find_element_by_xpath("//input[@value='1']").click()
        time.sleep(1)
        self.driver.find_element_by_name("msg_title").send_keys("我想上传呀")
        time.sleep(1)
        self.driver.find_element_by_name("msg_content").send_keys("我想上传呀")
        time.sleep(1)
        self.driver.find_element_by_name("message_img").send_keys(r"C:\Users\Administrator\Desktop\每日一讲.png")
        time.sleep(1)
        self.driver.find_element_by_class_name("bnt_bonus").click()

    def quit_1(self):
        pass

    def tearDown(self):
        time.sleep(3)
        self.driver.quit()


if __name__ == "__main__":
    # 构建测试集，创建测试套建
    suite_1 = unittest.TestSuite()

    # 添加测试用例
    suite_1.addTest(ut("test_login"))
    suite_1.addTest(ut("test_upload"))

    # 执行测试  执行的类
    runer = unittest.TextTestRunner()
    # 执行类的执行方法
    runer.run(ut("test_upload"))
    # runner.run(suite_1)
