# 传函数的参数，求阶乘的和

def factorial(value1):
    count = 0
    num = 1
    for i in range(1, value1 + 1):
        num = num * i  # 阶乘
        count = count + num  #阶乘和
    print(count)


value1 = int(input('输请入一个整数n，求n阶乘的和：'))
factorial(value1)  # 函数的调用
