'''
from … import 语句

from modname import name1[, name2[, ... nameN]]
'''
# 自定义模块


# def factorial_sum(value1):
#     count = 0
#     num = 1
#     for i in range(1, value1 + 1):
#         num = num * i
#         count = count + num
#     print("%d 阶乘的值的和为%d" % (value1, count))
#
#
# def factorial(value1):
#     count = 0
#     num = 1
#     for i in range(1, value1 + 1):
#         num = num * i
#
#     print("%d 阶乘的值为%d" % (value1, num))


# import test_27
from test_27 import factorial as test
# from test_27 import factorial_sum

test(3)
#factorial(5)