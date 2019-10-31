import unittest

class ut(unittest.TestCase):

    def setUp(self):
        self.num = int(input("请输入一个整数："))

    def test_case1(self):   # 第一个测试用例
        print("这是case1")
        self.assertEqual(self.num, 10, msg="你输入的不是10")

    def test_case2(self):     # 第二个测试用例
        print("这是case2")
        self.assertNotEqual(self.num, 20, msg="你输入的是20")

    @unittest.skip("暂时跳过此")
    def test_case3(self):
        print("这是case3")
        self.assertEqual(self.num, 20, msg="你输入的是20")

    def test_case4(self):       # 第四个测试用例
        print("这是case4")
        self.assertTrue(self.num, msg="我输入的值是错误的")

    def tearDown(self):
        pass


if __name__ == "__main__":
    unittest.main()

