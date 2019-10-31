# 17 1-100猜数字游戏

import random
print("猜拳游戏开始")
print("----------")

rand_1 = random.randint(1, 100)

while 1:
    num = int(input("请输入一个1-100的整数:"))
    if num <= 0:
        print("请重新输入一个正确整数")
    elif rand_1 == num:
        print("恭喜你，答对了，奖励你一个棒棒糖")
        break
    elif num > rand_1:
        print("你输入的值太大了")
    elif num < rand_1:
        print("你输入的值太小了")
    else:
        print("你输入的不是一个整数")
