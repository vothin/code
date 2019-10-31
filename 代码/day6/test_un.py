'''
https://blog.csdn.net/wangst4321/article/details/8454118
方法1
1.从unittest.TestCase继承一个子类。
2.定义测试方法，以test开头。
3.调用unittest.main()，这个方法会自动执行所有以test开头的测试方法。

方法2
第2种调用方法：
1 自己创建一个TestSuite，
2 添加需要执行测试的TestCase，
3 然后使用TestRunner().run(suite)执行测试。
'''

from selenium import webdriver
import unittest
import random
import unittest
import sys

sys.path.append(r"C:/Users/Administrator/PycharmProjects/ts16/day6/D.UnittestDemo.py")
# import testclass
class Foo(unittest.TestCase):
    # 执行每个测试用例函数之前会先执行setUp,初始化执行环境
    def setUp(self):
        # print "setUp..."
        #self.m = random.randint(1, 200)
        pass

    def test_add(self):
        # m = self.m
        # ret = m.add(3, 5)
        # self.assertEqual(ret, 8, "3 + 5 != 8")
        print("这是add方法")

    def test_sub(self):
        # m = self.m
        # ret = m.sub(3, 5)
        # self.assertEqual(ret, -2, "3 - 5 != -2")
        print("这是sub方法")

    def test_mul(self):
        # m = self.m
        # ret = m.mul(3, 5)
        # self.assertEqual(ret, 15, "3 * 5 != 15")
        print("这是mul方法")

    # 执行完每个测试用例函数后,会执行tearDown函数,清理执行环境
    def tearDown(self):
        # del self.m
        pass



if __name__ == '__main__':
     unittest.main()

    # 创建测试套件
    # ts = unittest.TestSuite()
    #
    # # 把测试用例添加到测试套件
    # ts.addTest(Foo('test_add'))
    # ts.addTest(Foo('test_mul'))
    #
    # # 创建可以执行测试套件的对象
    # runner = unittest.TextTestRunner()
    # # 执行测试套件
    # # runner.run(ts)
    # runner.run(Foo("test_add"))
