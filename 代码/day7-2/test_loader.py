"""
方法3
第3种调用方法：
1 自己创建TestCase1，TestCase2二个子类，同时继承unittest.TestCase
2 添加需要执行测试的TestCase，
3 然后使用TestRunner().run(suite)执行测试。
"""

from selenium import webdriver
import unittest
import time


class ut(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(10)
        self.ecshop_url_1 = "http://192.168.2.246/ecshop/user.php"

    def tearDown(self):
        time.sleep(3)
        self.driver.quit()

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
        self.driver.find_element_by_name("message_img").send_keys(r"C:\Users\Administrator\Desktop\timg.jpg")
        time.sleep(1)
        self.driver.find_element_by_class_name("bnt_bonus").click()



class ut1(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(10)
        self.ecshop_url_1 = "http://192.168.2.246/ecshop/user.php"

    def tearDown(self):
        time.sleep(3)
        self.driver.quit()

    def test_login1(self):  # 第一个测试用例
        # 打开主页
        self.driver.get(self.ecshop_url_1)

        # 输入账号密码
        self.driver.find_element_by_name("username").send_keys("ts16")
        self.driver.find_element_by_name("password").send_keys("123456")

        # 单击登陆
        self.driver.find_element_by_name("submit").click()

    def test_upload1(self):  # 第二个测试用例
        self.test_login1()
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
        self.driver.find_element_by_name("message_img").send_keys(r"C:\Users\Administrator\Desktop\timg.jpg")
        time.sleep(1)
        self.driver.find_element_by_class_name("bnt_bonus").click()



if __name__ == "__main__":
    suite_1 = unittest.TestLoader().loadTestsFromTestCase(ut)
    suite_2 = unittest.TestLoader().loadTestsFromTestCase(ut1)
    suite = unittest.TestSuite([suite_1, suite_2])
    unittest.TextTestRunner(verbosity=2).run(suite)