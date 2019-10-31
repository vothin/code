'''

方法1
1.从unittest.TestCase继承一个子类。
2.定义测试方法，以test开头。
3.调用unittest.main()，这个方法会自动执行所有以test开头的测试方法。

'''

import unittest

class ut(unittest.TestCase):

    def setUp(self):
        pass

    def test_hello(self):   # 第一个测试用例
        print("这是一个test_hello方法")

    def test_you(self):     # 第二个测试用例
        print("这是一个you方法")

    def test_i(self):       # 第三个测试用例
        print("这是一个i方法")

    def tearDown(self):
        pass


if __name__ == "__main__":
    unittest.main()


