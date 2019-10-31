'''
不定长参数

你可能需要一个函数能处理比当初声明时更多的参数。这些参数叫做不定长参数，和上述 2 种参数不同，声明时不会命名。
加了星号 * 的参数会以元组(tuple)的形式导入，存放所有未命名的变量参数。
如果在函数调用时没有指定参数，它就是一个空元组
语法：
def functionname([formal_args,] *var_args_tuple ):
   "函数_文档字符串"
   function_suite
   return [expression]
'''


def printinfo2(arg1, *vartuple):  # 函数  空元组# printinfo2(10)
    "打印任何传入的参数"
    print("输出: ")
    print(arg1)
    print(vartuple)


def printinfo1(arg1, **vardict):  # 函数  双星号 以字典的形式导入printinfo1(1, a=2, b=3)
    "打印任何传入的参数"
    print("输出: ")
    print(arg1)
    print(vardict)


def printinfo(arg1, *vartuple):  # #元组的方法传入值  printinfo(70, 60, 50, 40, 30)
    "打印任何传入的参数"
    print("输出: ")
    # print(arg1)
    for var in vartuple:
        print(var)
    print(vartuple, type(vartuple))
    return


def printinfo4(a, b, *, c):  # 单独出现星号 * 后的参数必须用关键字传入
    return a + b + c


# arg1 = 70
# *vartuple = (60,50,40,30)

# 调用printinfo 函数
printinfo2(70, 60, 50, 40, 30) #元组的方法传入值
#
# # 调用printinfo 函数  空元组
# printinfo2(10)

# 调用printinfo 函数  双星号 以字典的形式导入
printinfo1(1, a=2, b=3)

# 单独出现星号 * 后的参数必须用关键字传入
# printinfo4(1,2,3)   # 报错
print(printinfo4(1, 2, c=3))
