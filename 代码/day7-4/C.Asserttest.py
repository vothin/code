# unittest.main()方法会搜索该模块下所有以test开头的测试用例方法，并自动执行它们。
# 执行顺序是命名顺序：先执行test_case1，再执行test_case2

from selenium import webdriver
import unittest, time


class ut(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(10)
        self.ecshop_url_1 = "http://192.168.3.246/ecshop/user.php"

    def test_login(self):   # 第一个测试用例
        try:

            # 打开主页
            self.driver.get(self.ecshop_url_1)
            # 断言--标题
            self.assertEqual(self.driver.title, "用户中心_ECSHOP演示站 - Powered by ECShop", msg="网页打不开")
            # 输入账号密码
            self.driver.find_element_by_name("username").send_keys("ts161")
            self.driver.find_element_by_name("password").send_keys("123456")

            # 单击登陆
            self.driver.find_element_by_name("submit").click()
            time.sleep(5)
            # 登陆成功的断言3 -- 判断元素是否存在
            self.assertTrue(self.isElementExist(), msg="登陆失败")

        except:
            print("执行--测试用例01-01--出现错误")

    def test_upload(self):     # 第二个测试用例
        try:
            self.test_login()  # 登陆
            time.sleep(3)
            self.driver.find_element_by_xpath("//a[@href='user.php']").click()
            time.sleep(1)
            self.driver.find_element_by_xpath("//a[@href='user.php?act=message_list']").click()
            time.sleep(1)
            # 断言2---网站地址
            self.assertEqual(self.driver.current_url, "http://192.168.3.246/ecshop/user.php?act=message_list", msg="留言列表打不开")
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
        except:
            print("执行--测试用例01-02--出现错误")




    def tearDown(self):
        pass
        self.driver.quit()

    # 断言3 是否存在元素
    def isElementExist(self):
        try:
            self.driver.find_element_by_xpath("//a[@href='user.php']")
            # print("1")
            return True
        except:
            # print("0")
            return False




if __name__ == "__main__":
    unittest.main()