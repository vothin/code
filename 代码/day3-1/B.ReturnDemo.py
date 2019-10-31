'''

return [表达式] 语句用于退出函数，选择性地向调用方返回一个表达式。不带参数值的return语句返回None。
'''


def sum(arg1, arg2):
    # 返回2个参数的和."
    total = arg1 + arg2
    print("函数内 : ", total)
    return total


# 调用sum函数
  # total（外部） = total(内部)

# sum(10, 20)     # 返回None
sum1 = sum(10, 20)
print("函数外 : ", sum(10, 20), sum1) #返回一个30的值
