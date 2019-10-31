'''

E （Enclosing） 闭包函数外的函数中
如果要修改嵌套作用域（enclosing 作用域，外层非全局作用域）中的变量则需要


nonlocal 关键字
'''

num = 99
def outer():
    #  num
    num = 10
    print(num)
    def inner():
        global num  # nonlocal关键字声明
        num = 100
        print('闭包：', num)
    inner()
    print(num)


outer()
print('全局：', num)