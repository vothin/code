from Config.EcshopConf import *
from Public.EcshopAPI import *
from Public.TestCaseExcel import write_excel_xls_append
from time import sleep
import unittest, time


class ecshoplogin(unittest.TestCase):
    def setUp(self):
        self.driver = Ecshop()  #
        self.driver.wait(10)
        self.base_url = echsop_url

    def test_case(self):
        try:
            driver = self.driver
            driver.open(self.base_url)
            driver.click_text("请登录")

            driver.input_text("name", "username", echsop_username)
            driver.input_text('name', 'password', echsop_passwd)
            driver.click("name", "submit")
            time.sleep(5)
            # driver.assertEqual("http://192.168.1.246/ecshop/", driver.get_url(), msg="标题是否一致")
            write_excel_xls_append(1, "Pass")  # 如果执行成功，则写入测试用例，状态为pass.1表示测试用例
        except:
            driver.save_windows_img(driver.get_image_path())  # 出错的时候，在当前页面进行截图
            write_excel_xls_append(1, "Fail")  # 如果执行失败，则写入测试用例，状态为.1表示测试用例
            print("用例执行失败")

        sleep(2)

    def tearDown(self):
        self.driver.quit()


if __name__ == '__main__':
    unittest.main()
