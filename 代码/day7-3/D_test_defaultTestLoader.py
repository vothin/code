'''

通过该类下面的discover()方法可自动更具测试目录start_dir匹配查找测试用例文件（test*.py），
并将查找到的测试用例组装到测试套件，因此可以直接通过run()方法执行discover。用法如下：
discover=unittest.defaultTestLoader.discover(test_dir, pattern='test_*.py')
'''
import unittest
import os

if __name__ == "__main__":
    test_dir = os.path.join(os.getcwd()+"\\testcase")
    # print(test_dir)
    discover = unittest.defaultTestLoader.discover(test_dir, pattern="test_*.py")  # 创建一个套件,以目录为套件
    runner = unittest.TextTestRunner()  # 创建执行套件
    runner.run(discover)   # 执行