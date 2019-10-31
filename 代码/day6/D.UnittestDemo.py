import unittest  # 导入unittest
from selenium import webdriver
import time

class Foo(unittest.TestCase):
    # 执行每个测试用例函数之前会先执行setUp,初始化执行环境
    def setUp(self):
        b = webdriver.Chrome()
        self.b = b
        # 初始化过程

    def tearDown(self):
        time.sleep(3)
        self.b.quit()

    def test_add(self):    # 测试用例1
        self.b.get("https://www.baidu.com")

    def test_sub(self):    # 测试用例2
        self.b.get("https://www.sohu.com")

    def test_mul(self):    #  测试用例3
        self.b.get("https://www.taobao.com")

    # 执行完每个测试用例函数后,会执行tearDown函数,清理执行环境



if __name__ == '__main__':
    # 第一种main()方法
    # unittest.main()

    # 第二种创建套建方法
    # 创建测试套件
    ts = unittest.TestSuite()

    # 把测试用例添加到测试套件
    ts.addTest(Foo('test_add'))
    ts.addTest(Foo('test_mul'))

    # 创建可以执行测试套件的对象
    runner = unittest.TextTestRunner()
    # 执行测试套件
    runner.run(ts)
    # runner.run(Foo("test_add"))
