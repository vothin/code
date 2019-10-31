'''
身份运算符
is	is 是判断两个标识符是不是引用自一个对象	x is y, 类似 id(x) == id(y) ,
如果引用的是同一个对象则返回 True，否则返回 False

is not	is not 是判断两个标识符是不是引用自不同对象	x is not y ，
类似 id(a) != id(b)。如果引用的不是同一个对象则返回结果 True，否则返回 False。
'''

a = 20
b = 20

print(a is b)

print(id(a) == id(b))
# 有相同的标识


# 修改变量 b 的值
# b = 30

print(a is not b)

print(not(id(a) == id(b)))