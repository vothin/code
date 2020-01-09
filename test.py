# encoding=utf-8

# for i in range(10):
#     print("计数：", i, end=" ")
#     if i % 2 != 0:
#         print("通过if判断：", i)
#         continue
#     i += 2
#     print("没通过if判断后i+2得出的数：", i)


# a = "{0} love {1}".format("I", "you")
# print(a)

# b = "{0} {1} {2}".format("520", "=", "love")
# print(b)


# def fab(n):
#     n1 = 1
#     n2 = 1
#     n3 = 1
#
#     if n < 1:
#         print("输入有误！")
#         return -1
#
#     while (n - 2) > 0:
#         n3 = n2 + n1
#         n1 = n2
#         n2 = n3
#         n -= 1
#
#     return n3
#
# result = fab(5100)
# if result != -1:
#     print("总共有%d对小兔崽子诞生！" % result)

#
# def hanoi(n, x, y, z):
#     if n == 1:
#         print(x, "-->", z)
#     else:
#         hanoi(n - 1, x, z, y)   # 将前n-1个盘子从x移到y上
#         print(x, "-->", z)      # 将最底下的最后一个盘从x移动到z上
#         hanoi(n - 1, y, x, z)   # 将y上的n-1个盘子移动到z上
#
# n = int(input("输入一个数字："))
# hanoi(n, "x", "y", "z")


# dict1 = {1: "one", 2: "two", 3: "three"}
# dict1[4] = "four"
# del dict1[1]
# print(dict1)
#
# a = [1, 2, 3, 4]
# b = ["one", "two", "three", "four"]
# dict2 = dict(zip(a, b))
# del dict2[1]
# print(dict2)
#
#
# for i in dict1.keys():
#     print(i, end=" ")
#
# for i in dict2.values():
#     print(i, end=" ")
#
# for i in dict2.items():
#     print(i, end=" ")


# f = open("D:\\test1.txt", "w")
# f.write("I love you")
# f.close()
# f = open("D:\\test1.txt")
# f.seek(0, 0)
# for i in f:
#     print(i)


# class Test:
#     def test1(self, name):
#         self.name = name
#
#     def test2(self, name2):
#         self.name2 = name2
#         print("狗%s，看我%s今天不打死你！！！" % (self.name2, self.name))
#
#
# t = Test()
# t.test1("墨墨")
# t.test2("兔兔")


# class Test2:
#     def test1(self, name):
#         self.name = name
#
#     def test2(self, action):
#         self.action = action
#         print("啊，我是%s，我正在%s，快来上我啊！！！" % (self.name, self.action))
#
# t = Test2()
# t.test1("骚兔兔")
# t.test2("跳脱衣舞")


# class Test3:
#     def test1(self, name):
#         self.name = name
#
#     def test2(self, name2):
#         self.name2 = name2
#         print("%s, 我%s爱你呀！！！" % (self.name, self.name2))
#
# t = Test3()
# t.test1("华日酱")
# t.test2("墨墨")


# class Test4:
#     def __init__(self, name):
#         self.name = name
#
#     def test2(self):
#         print("%s, 我喜欢你呀！" % self.name)
#
# t = Test4("虫虫")
# t.test2()


# for i in range(1, 5):
#     for x in range(1, 5):
#         for y in range(1, 5):
#             if (i != x) and (i != y) and (x != y):
#                 print(i, x, y)

# a = input("请输入你的名字：")
# print("你好，%s！" % a)

# import random as r
# time = 5
# b = 0
# a = r.randint(1, 100)
# while time > 0:
#     b = input("请输入100以内的数字：")
#     if b.isdigit() == 0:
#         print("请输入数字！！！")
#
#     else:
#         b = int(b)
#         if b < 0 or b > 100:
#             print("你输入的数字不是100以内！！！")
#
#         elif a == b:
#             print("你妹好漂亮^_^")
#             break
#
#         elif a > b:
#             time -= 1
#             print("你大爷好丑，数字小了T_T,还剩%s次" % time)
#
#         elif a < b:
#             time -= 1
#             print("你大爷好丑，数字大了T_T，还剩%s次" % time)
# print("游戏结束！！！")


# a = 1
# print(a)
# b = "2"
# print(b)
# a = b
# print(a)

# print("Let\'s go!")
# print("Let's go!")

# DaysPerYear = 365
# HoursPerDAy = 24
# MinutesPerHour = 60
# SecondsPerMinute = 60
#
# SecondsPerYear = DaysPerYear * HoursPerDAy * MinutesPerHour *SecondsPerMinute
# print(SecondsPerYear)

# print('''
# 11111111
# 12222222
# 33333333
# 44444444''')


# print(2 ** 2 ** 32)


# x = 7
# count = 1
# while 1:
#     if (x % 2 == 1) and (x % 3 == 2) and (x % 5 == 4) and (x % 6 == 5):
#         print("阶级数为", x)
#         print("计数为", count)
#         break
#
#     else:
#         x = 7 * (count + 1)
#         count += 1


# x = 7
# i = 1
# flag = 0
# while i <= 100:
#     if (x%2 == 1) and (x%3 == 2) and (x%5 == 4) and (x%6 == 5):
#         flag = 1
#     else:
#         x = 7 * (i+1)
#     i += 1
# if flag == 1:
#     print('阶梯数是：',x)
# else:
#     print("没有找到答案")

# assert 1 > 2


# count = 3
#
# password = "FishC.com"
#
# while count:
#     passwd = input("请输入密码：")
#
#     if passwd == password:
#         print("密码正确，进入程序...")
#         break
#
#     elif "*" in passwd:
#         print("密码中不能含有*号！您还有", count, "次机会！", end = " ")
#         continue
#
#     else:
#         print("密码输入错误！您还有", count - 1, "次机会！", end = " ")
#         count -= 1

# a = [1, 2, 3, 4, 5]
#
# a.append(6)
# print(a)
#
# a.extend([7, 8, 9])
# print(a)
#
# a.insert(0, 0)
# print(a)
#
# a.pop()
# print(a)
#
# a.reverse()
# print(a)
#
# a.sort()
# print(a)

# list1 = []
# for x in range(10):
#     for y in range(10):
#         if x%2 == 0:
#             if y%2 != 0:
#                 list1.append((x, y))
# print(list1)

# list1 = [1, 56, 878, 12, 43, 48, 121 ,12]
# # print(list1.count(1))
# # print(list1.index(12))
# # print(list1.index(12, 6, 9))
# # list1.reverse()
# # print(list1)
# # list1.sort()
# # print(list1)
# # list1.sort(reverse = True)
# # print(list1)

# str2 = '待卿长发及腰，我必凯旋回朝。\
# 昔日纵马任逍遥，俱是少年英豪。\
# 东都霞色好，西湖烟波渺。\
# 执枪血战八方，誓守山河多娇。\
# 应有得胜归来日，与卿共度良宵。\
# 盼携手终老，愿与子同袍。'
# print(str2)
#
# str1 = '''待我长发及腰，将军归来可好？
# 此身君子意逍遥，怎料山河萧萧。
# 天光乍破遇，暮雪白头老。
# 寒剑默听奔雷，长枪独守空壕。
# 醉卧沙场君莫笑，一夜吹彻画角。
# 江南晚来客，红绳结发梢。'''
# print(str2)

# file1 = open(r"C:\Users\zhangyi\Desktop\test.txt", "w")
# file1.write("我爱你呀！")
# file1.close()
# file1 = open(r"C:\Users\zhangyi\Desktop\test.txt", "r")
# print(file1.read())
# file1.close()

# 数字 = "1234567890"
# 字母 = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
# 符号 = "~!@#$%^&*()_+-=/,.?<>;:[]{}|\\"
#
#
#
# class password:
#     def length(self):
#         global count2
#         length = len(passwd)
#         if len(passwd) <= 8:
#             count2 = 0
#
#         elif 8 < len(passwd) < 16:
#             count2 = 1
#
#         elif len(passwd) >= 16:
#             count2 = 2
#
#     def figure(self):
#         global count1
#         for i in passwd:
#             if i in 数字:
#                 count1 += 1
#                 break
#
#     def letter(self):
#         global count1
#         for i in passwd:
#             if i in 字母:
#                 count1 += 1
#                 break
#
#         if passwd[0] in 字母:
#             count1 += 1
#
#     def symbol(self):
#         global count1
#         for i in passwd:
#             if i in 符号:
#                 count1 += 1
#                 break
#
#     # def com(self):
#     #     global count1
#     #
#     #     count = 0
#     #
#     #     for i in passwd:
#     #         if i in 数字:
#     #             count += 1
#     #             break
#     #
#     #     for i in passwd:
#     #         if i in 字母:
#     #             count += 1
#     #             break
#     #     for i in passwd:
#     #         if i in 符号:
#     #             count += 1
#     #             break
#     #
#     #         if passwd[0] in 字母:
#     #             count += 1
#     #
#     #     count == count1
#
#
#
# while 1:
#     passwd = input("请输入密码：")
#
#     if passwd.isspace() or len(passwd) == 0:
#         print("您输入的密码为空，请重新输入！")
#         continue
#
#     else:
#         while 1:
#             count1 = 0
#             count2 = 0
#             pwd = password()
#             pwd.length()
#             pwd.figure()
#             pwd.letter()
#             pwd.symbol()
#             # pwd.com()
#             print(count1)
#             print(count2)
#
#             if count1 < 2 or count2 < 1:
#                 print("您的密码安全级别评定为：低")
#
#             elif count1 == 4 and count2 == 2:  # and (passwd[0] in 字母):
#                 print("您的密码安全级别评定为：高")
#                 break
#
#             else:
#                 print("您的密码安全级别评定为：中")
#
#             print("请按照以下方式提升您的密码安全级别：\n\
# 1.密码必须由数字、字母及特殊字符三种组合\n\
# 2.密码只能由字母开头\n\
# 3.密码长度不能低于16位")
#

# a = "asdASFA"
# b = "131464613"
# c = "!@##$%^&"
# d = "I\tLove\tYou"
# e = "asdaASDAd1313464"
# f = "         "
# g = "  asdasd"
#
# print(a.capitalize())
# print(a.casefold())
# print(a.center(12))
# print(b.count("6", 0, 9))
# print(c.encode(encoding = "utf-8"))
# print(b.endswith("3"))
# print(b.endswith("6", 1, 7))
# print(d.expandtabs(tabsize = 1))
# print(d.find("I", 0, 10))
# print(e.isalnum())
# print(a.isalpha())
# print(e.isalpha())
# print(b.isdecimal())
# print(b.isdigit())
# print(e.isdigit())
# print(a.islower())
# print(b.isnumeric())
# print(f.isspace())
# print(g.isspace())
# print(a.istitle())
# print(a.isupper())
# print(b.join("aa"))
# print(b.ljust(16))
# print(a.lower())
# print(g.lstrip())


# 字母 = "asdfg"
# count1 = 0
#
# def letter():
#     global count1
#     for i in passwd:
#         if i in 字母:
#             count1 += 1
#             print(count1)
#             break
#
#     if passwd[0] in 字母:
#         count1 += 1
#         print(count1)
#
# passwd = input("：")
# letter()

# a = "{0}"
# print(a.format("a"))
# print("{0}{1:.2f}".format("Pi = ", 3.1415))

# def min(x):
#     least = x[0]            # least =1
#
#     for each in x:          # 同等于range（10）
#         if each < least:    # 当each小于least时
#             least = each    # least = each
#
#     return least            # 返回least值
#
# print(min("987654321"))

# def MyFun(x, y):
#     return x[0] * x[1] - y[0] * y[1]
#
# print(MyFun((3, 4), (1, 2)))

# def findstr(a, b):
#     count = 0
#     length = len(b)
#
#     if a not in b:
#         print("在目标字符串中未找到字符串", a)
#
#     else:
#         for each1 in range(length - 1):
#             if b[each1] == a[0]:
#                 if b[each1 + 1] == a[1]:
#                     count += 1
#
#         print("字符串在目标字符串中共出现%d次" % count)
#
# b = input("请输入目标字符串：")
# a = input("请输入两个字符：")
# findstr(a, b)


# def a():
#     x = 1
#     print(x)
#     def b():
#         x = 2
#         print(x)
#     return b()
#
# a()

# g = lambda x : 2 * x + 1
# print(g(10))
#
# g = list(filter(lambda x : x % 2, range(10)))
# print(g)
#
# g = list(map(lambda x : x * 2, range(10)))
# print(g)

# result = []
# def get_digits(n):
#     if  n > 0:
#         result.insert(0, n % 10)
#         get_digits(n // 10)
#
# get_digits(12345)
# print(result)

# result = []
#
# def get_digits(n):
#     if n.isnumeric() == 1:
#         for i in range(len(n)):
#             result.append(n[i])
#
#     else:
#         print("你输入的不是数字")
#
#
#
# a = input("请输入一个数字:")
# m = get_digits(a)
# print(result)

# def is_palindrome(n, start, end):
#     if start > end:
#         return 1
#
#     else:
#         if n[start] == n[end]:
#             return is_palindrome(n, start + 1, end - 1)
#
#         else:
#             return 0
#
#         # return is_palindrome(n, start + 1, end - 1) if n[start] == n[end] else 0
#
# string = input("请输入一串字符：")
# length = len(string) - 1
#
# if is_palindrome(string, 0, length):
#     print("是回文符", string)
#
# else:
#     print("不是回文符", string)


# def age(n):
#     if n == 1:
#         return 10
#
#     else:
#         return age(n - 1) + 2
#
# print(age(5))

# c = dict(zip(['one', 'two', 'three'], [1, 2, 3]))
# print(c)
# a = zip(["one", "two", "three"], [1, 2, 3])
# for i in a:
#     print(i)

# dict1 = {}
#
# a = dict1.fromkeys((1, 2, 3), ("one", "two", "three"))
# print(a)
#
# a = dict1.fromkeys((1, 3), "数字")
# print(a)
#
# b = a.copy()
# print(b)
#
# a[4] = "four"
# print(a)
# print(b)
#
# a.pop(3)
# print(a)
#
# b.popitem()
# print(b)
#
# a.setdefault(5, "five")
# print(a)
#
# b.update(a)
# print(b)

# f = open(r"C:\Users\zhangyi\Desktop\OpenMe.mp3")
# for each_line in f:
#     print(each_line, end = "")
# f.close()

# def save_file(boy, girl, count):
#     file_name_boy = r"C:\Users\zhangyi\Desktop\boy_" + str(count) + ".txt"
#     file_name_girl = r"C:\Users\zhangyi\Desktop\girl_" + str(count) + ".txt"
#
#     boy_file = open(file_name_boy, "w")
#     girl_file = open(file_name_girl, "w")
#
#     boy_file.writelines(boy)
#     girl_file.writelines(girl)
#
#     boy_file.close()
#     girl_file.close()
#
#
# f = open(r"C:\Users\zhangyi\Desktop\fishc.txt", encoding = "utf-8")
#
# boy = []
# girl = []
# count = 1
#
# for each_line in f:
#     if each_line[:6] != "======":
#         (role, line_spoken) = each_line.split(":", 1)
#         if role == "小甲鱼":
#             boy.append(line_spoken)
#         if role == "小客服":
#             girl.append(line_spoken)
#
#     else:
#         save_file(boy, girl, count)
#
#         boy = []
#         girl = []
#         count += 1
#
# save_file(boy, girl, count)
#
# f.close()


# import os
# # g = os.getcwd()
# print(os.getcwd())
#
# os.chdir("D:\\")
# print(os.getcwd())
# print(os.listdir())
#
# os.mkdir("D:\\B")
# print(os.listdir())
#
# os.removedirs("D:\\B")
# print(os.listdir())
#
# os.makedirs("D:\\A\\B")
# print(os.listdir())
#
# os.rename("D:\\A\\B", "D:\\A\\C")
# os.removedirs("D:\\A\\C")
# print(os.listdir())
#
# f = open("D:\\test.log", "w")
# f.write("123")
# f.close()
# print(os.listdir())
#
# f = open("D:\\test.log")
# print(f.read())
# f.seek(0, 0)
# print(f.readline())
# f.close()
#
# os.remove("D:\\test.log")
# print(os.listdir())


# import pickle
# list1 = [123, 3.14, "xiaojiayu", ["张逸"]]
# pickle_file = open("C:\\Users\\zhangyi\\Desktop\\list1.pkl", "wb")
# pickle.dump(list1, pickle_file)
# pickle_file.close()
#
# pickle_file = open("C:\\Users\\zhangyi\\Desktop\\list1.pkl", "rb")
# list2 = pickle.load(pickle_file)
# print(list2)

# count = 3
#
# def fine_file():
#     global count
#     try:
#         file_name = input("请输入需要打开的文件名：")
#         f = open(file_name)
#         for each_line in f:
#             print(each_line)
#
#         count -= 3
#         return count
#
#     except:
#         if count > 1:
#             count -= 1
#             print("出错啦！")
#             print("你还能输入%s次数" % count)
#
#         else:
#             count -= 1
#             print("出错啦！")
#             print("你已经没有输入机会了")
#         return count
#
#     # except OSError as error:
#     #     print("您输入的文件不存在，请重新输入！\n错误的原因是：" + str(error))
#     #     return count
#
#     # finally:
#     #     if count > 1:
#     #         count -= 1
#     #         print("你还能输入%s次数" % count)
#     #
#     #     else:
#     #         count -= 1
#     #         print("你已经没有输入机会了")
#
#
# while count > 0:
#     fine_file()

# try:
#     sum1 = 1 + "1"
#
# except TypeError as error:
#     print("类型出错啦！\n错误的原因是：" + str(error))

# try:
#     with open(r"C:\Users\zhangyi\Desktop\test.txt", "w") as file:
#         file.write("测试")
#         sum1 = 1 + "1"
#         file.close()
#
# except (OSError, TypeError) as error:
#     print("出错啦！\n出错的原因是：" + str(error))
#
# else:
#     print("没有bug")

# def file_compare(file1, file2):
#     with open(file1) as f1, open(file2) as f2:
#         count = 0
#         differ = []
#
#         for line1 in f1:
#             line2 = f2.readline()
#             count += 1
#             if line1 != line2:
#                 differ.append(count)
#
#     return differ
#
# file1 = input("请输入需要比较的头一个文件名：")
# file2 = input("请输入需要比较的另一个文件名：")
#
# differ = file_compare(file1, file2)
#
# if len(differ) == 0:
#     print("两个文件完全一样！")
#
# else:
#     print("两个文件共有%d处不同" % len(differ))
#     for each in differ:
#         print("第%d行不同" % each)


# import easygui as e
# e.msgbox("我爱你啊！")

# import easygui as e
# import sys
#
# while 1:
#     e.msgbox("嗨，欢迎进入第一个界面小游戏")
#
#     msg = "请问你希望在鱼C工作室学习到什么知识呢？"
#     title = "小游戏互动"
#     choices = ["谈恋爱", "编程", "OOXX", "琴棋书画"]
#
#     choices = e.choicebox(msg, title, choices)
#
#     e.msgbox("你的选择是：" + str(choices), "结果")
#
#     msg = "你希望重新开始小游戏吗？"
#     title = "请选择"
#
#     if e.ccbox(msg, title):
#         pass
#
#     else:
#         sys.exit(0)

# import easygui as e
# # e.egdemo()
# e.msgbox("内容", "标题")
#
# choices = ["1", "2", "3"]
# reply = e.choicebox("x", choices = choices)

# import easygui as e
# import random  as r
#
# e.msgbox("欢迎进入第一个界面小游戏！")
# num = r.randint(1, 10)
#
# msg = "猜一下（1-10）内的数字！"
# title = "数字小游戏"
# guess = e.integerbox(msg, title, lowerbound = 1, upperbound = 10)
#
# while 1:
#     if guess == num:
#         e.msgbox("恭喜你猜中！")
#         e.msgbox("猜中也没奖励！")
#         break
#
#     else:
#         if guess > num:
#             e.msgbox("大了！")
#
#         else:
#             e.msgbox("小了！")
#
#         guess = e.integerbox(msg, title, lowerbound = 1, upperbound = 10)
#
# e.msgbox("游戏结束！")

# import easygui as g
#
# msg = "请填写一下联系方式"
# title = "账号中心"
# fieldNames = ["*用户名", "*真实姓名", "固定电话", "*手机号码", "QQ", "*E-mail"]
# # fieldValues = []
# fieldValues = g.multenterbox(msg, title, fieldNames)
# # print(fieldValues)
#
# while 1:
#     # fieldValues = g.multenterbox(msg, title, fieldNames)
#
#     if fieldValues == None:
#         break
#
#     errmsg = ""
#
#     for i in range(len(fieldNames)):
#         option = fieldNames[i].strip()
#         if fieldValues[i].strip() == "" and option[0] == "*":
#         # if option[0] == "*":
#             errmsg += ("【%s】为必填项。\n\n" % fieldNames[i])
#
#     if errmsg == "":
#         break
#     fieldValues = g.multenterbox(errmsg, title, fieldNames, fieldValues)
#
# print("用户资料如下：%s" % str(fieldValues))

# import easygui as g
# import os
#
# file_path = g.fileopenbox(default = "*.txt")
#
# with open(file_path, encoding = "utf-8") as f:
#     title = os.path.basename(file_path)
#     msg = "文件【%s】的内容如下：" % title
#     text = f.read()
#     g.textbox(msg, title, text)

# import easygui as g
# import os
#
# file_path = g.fileopenbox(default = "*.txt")
#
# with open(file_path, encoding = "utf-8") as old_file:
#     title = os.path.basename(file_path)
#     msg = "文件【%s】的内容如下：" % title
#     text = old_file.read()
#     text_after = g.textbox(msg, title, text)
#
# if text != text_after:
# # if text != text_after[:-1]:
#     choice = g.buttonbox("检测到文件内容发送改变，请选择以下操作：", "警告", ("覆盖保存", "放弃保存", "另存为..."))
#
#     if choice == "覆盖保存":
#         with open(file_path, "w", encoding = "utf-8") as old_file:
#             old_file.write(text_after)
#             # old_file.write(text_after[:-1])
#
#     if choice == "放弃保存":
#         pass
#
#     if choice == "另存为...":
#         another_path = g.filesavebox(default = ".txt")
#
#         if os.path.splitext(another_path)[1] != ".txt":
#             another_path += ".txt"
#
#         with open(another_path, "w", encoding = "utf-8") as new_file:
#             new_file.write(text_after)
#             # nwx_file.write(text_after[:-1])

# class Rectangle:
#     length = 5
#     width = 4
#
#     def setRect(self):
#         print("请输入矩形的长和宽")
#         self.length = float(input("长："))
#         self.width = float(input("宽："))
#
#     def getRect(self):
#         print("这个矩形的长是：%.2f，宽是：%.2f" % (self.length, self.width))
#
#     def getArea(self):
#         print("这个矩形的面积是：%.2f" % (self.length * self.width))
#
# f = Rectangle()
# f.getRect()
# f.getArea()
# f.setRect()
# f.getRect()
# f.getArea()

# class Ball():
#     def __init__(self, name):
#         self.name = name
#
#     def kick(self):
#         print(self.name)
#
# c = Ball("one")
# c.kick()

# class MyClass:
#     name = 'FishC'
#     def myFun(self):
#         print("Hello FishC!")
#
# m = MyClass()
# print(m.name)
# m.myFun()

# class Ticket():
#     def __init__(self, weekend = False, child = False):
#         self.exp = 100
#         if weekend:
#             self.inc = 1.2
#         else:
#             self.inc = 1
#
#         if child:
#             self.discount = 0.5
#         else:
#             self.discount = 1
#
#     def calcPrice(self, num):
#         return self.exp * self.inc * self.discount * num
#
# p = Ticket()
# c = Ticket(child = True)
# print("2个承认 + 1个小孩平日的票价为：%.2f" % (p.calcPrice(2) + c.calcPrice(1)))

# import random as r
#
# legal_x = [0, 10]
# legal_y = [0, 10]
#
# class Turtle:
#     def __init__(self):
#         self.power = 100                            # 初始体力
#
#         self.x = r.randint(legal_x[0], legal_x[1])               # 初始随机位置
#         self.y = r.randint(legal_y[0], legal_y[1])
#         print("乌龟的初始位置：",self.x ,self.y)
#
#     def move(self):
#         new_x = self.x + r.choice([1, 2, -1, -2])   # 随机计算方向并移动到新的位置(x, y)
#         new_y = self.y + r.choice([1, 2, -1, -2])
#
#         if new_x < legal_x[0]:                            # 检查移动后是否超过x轴
#             self.x = legal_x[0] - (new_x - legal_x[0])
#         elif new_x > legal_x[1]:
#             self.x = legal_x[1] - (new_x - legal_x[1])
#         else:
#             self.x = new_x
#
#         if new_y < legal_y[0]:                            # 检查移动后是否超过y轴
#             self.y = legal_y[0] - (new_y - legal_y[0])
#         elif new_y > legal_y[1]:
#             self.y = legal_y[1] - (new_y - legal_y[1])
#         else:
#             self.y = new_y
#
#         self.power -= 1                             # 体力消耗
#         print("乌龟的新位置：", self.x, self.y, "乌龟的体力：", self.power)
#
#         return(self.x, self.y)                      # 返回移动后的新位置
#
#     def eat(self):
#         self.power += 20
#         if self.power > 100:
#             self.power = 100
#         print("乌龟吃小鱼啦，乌龟的体力：", self.power)
#
#
# class Fish:
#     def __init__(self):
#         self.x = r.randint(legal_x[0], legal_x[1])
#         self.y = r.randint(legal_y[0], legal_y[1])
#         print("小鱼的初始位置：", self.x, self.y)
#
#     def move(self):
#         new_x = self.x + r.choice([1, -1])
#         new_y = self.y + r.choice([1, -1])
#
#         if new_x < legal_x[0]:                            # 检查移动后是否超过x轴
#             self.x = legal_x[0] - (new_x - legal_x[0])
#         elif new_x > legal_x[1]:
#             self.x = legal_x[1] - (new_x - legal_x[1])
#         else:
#             self.x = new_x
#
#         if new_y < legal_y[0]:                            # 检查移动后是否超过y轴
#             self.y = legal_y[0] - (new_y - legal_y[0])
#         elif new_y > legal_y[1]:
#             self.y = legal_y[1] - (new_y - legal_y[1])
#         else:
#             self.y = new_y
#
#         print("小鱼移动后的新位置：", self.x, self.y)
#
#         return(self.x, self.y)                      # 返回移动后的新位置
#
# turtle = Turtle()
# fish = []
# for i in range(10):
#     new_fish = Fish()
#     fish.append(new_fish)
#
# while True:
#     if not len(fish):
#         print("鱼儿都吃完啦，游戏结束！")
#         break
#     if not turtle.power:
#         print("乌龟体力耗尽，挂掉了！")
#         break
#
#     pos = turtle.move()
#     for each_fish in fish[:]:
#         if each_fish.move() == pos:
#             turtle.eat()
#             fish.remove(each_fish)
#             print("有一条鱼儿被吃掉了...")

# import random as r
#
# class Fish:
#     def __init__(self):
#         self.x = r.randint(0, 10)
#         self.y = r.randint(0, 10)
#
#     def move(self):
#         self.x -= 1
#         print("我的位置是：", self.x, self.y)
#
# class Goldfish(Fish):
#     pass
#
# class Carp(Fish):
#     pass
#
# class Salmon(Fish):
#     pass
#
# class Shark(Fish):
#     def __init__(self):
#         # Fish.__init__(self)
#         # super().__init__()
#         super(Shark, self).__init__()
#         self.hungry = True
#
#     def eat(self):
#         if self.hungry:
#             print("吃货的梦想就是天天有的吃")
#             self.hungry = False
#         else:
#             print("太撑了，吃不下了！")

# import math
#
# class Point():
#     def __init__(self, x = 0, y = 0):
#         self.x = x
#         self.y = y
#
#     def getx(self):
#         return self.x
#
#     def gety(self):
#         return self.y
#
# class Line():
#     def __init__(self, p1, p2):
#         self.x = p1.getx() - p2.getx()
#         self.y = p1.gety() - p2.gety()
#         self.len = math.sqrt(self.x * self.x + self.y * self.y)
#
#     def getLen(self):
#         return print(self.len)
#
# p1 = Point(1, 1)
# p2 = Point(4, 5)
# line = Line(p1, p2)
# line.getLen()


# import pygame
# # print(pygame.ver)
#
# import sys
# from easygui import *
# if ccbox('和我交往吗？', choices = ('不要，你长得太丑了~','算了吧，要找个比你更好看的~')):
#     msgbox('那我们绝交吧！哼~')
# else:
#     sys.exit(0)
#
# import json, pymysql

# class A:
#     print("hello world!!!")
# class B(A):
#     pass
# class C:
#     pass
# print(issubclass(B, A))
# print(issubclass(A, object))
# b1 = B()
# print(isinstance(b1, B))
# print(isinstance(b1, C))
# print(isinstance(b1, (A, B, C)))

# class C:
#     def __init__(self, x = 0):
#         self.x = x
#
# c1 = C()
#
# print(hasattr(c1, 'x'))
# print(hasattr(c1, 'y'))
# print(getattr(c1, 'x', '您所访问的属性不存在...'))
# print(getattr(c1, 'y', '您所访问的属性不存在...'))
# print(setattr(c1, "y", 'FishC'))
# print(delattr(c1, "y"))

# class C:
#     def __init__(self, size = 10):
#         self.size = size
#
#     def getSize(self):
#         return self.size
#
#     def setSize(self, values):
#         self.size = values
#
#     def delSize(self):
#         del self.size
#
#     x = property(getSize, setSize, delSize)
#
# c1 = C()
# print(c1.getSize())
# print(c1.x)
# c1.x = 18
# print(c1.getSize())
# print(c1.x)
# print(c1.size)
# # del c1.x
# # print(c1.x)

# class CapStr(str):
#     def __new__(cls, string):
#         string = string.upper()
#         return string
#
# a = CapStr("I love FishC.com!")
# print(a)


# class A():
#     def __new__(cls):
#         A = 9 * 3
#         return A
#
#     def __init__(self):
#         self.A = 9
#
#     def method(self):
#         print(self.A)
#
# a = A()
# print(a)
# a.method()

# class A():
#     def __new__(cls):
#         print('new')
#
#     def __init__(self):
#         print("init")
#
# a = A()

# class FileObject:
#     def __init__(self, filename = r"C:\Users\zhangyi\Desktop\sample.txt"):
#         self.new_file = open(filename, "w", encoding = "utf-8")
#
#     def write(self):
#         self.new_file.write("测试文件自动关闭")
#
#     def __del__(self):
#         self.new_file.close()
#         print("文件已经被删除")
#         del self.new_file
#
# file = FileObject()
# file.write()
# del file

# class C2F():
#     def __init__(self, arg):
#         self.c2f = arg * 1.8 + 32
#
#     def transition(self):
#         print("转华氏度为%.2f！" % (self.c2f))
#
# c = C2F(26)
# c.transition()

# class C2F(float):
#     def __new__(cls, arg = 0.0):
#         return float.__new__(cls, arg * 1.8 + 32)
#
# c = C2F(32)
# print(c)

# class Nstr(str):
#     def __sub__(self, other):
#         return self.replace(other, "")
# a = Nstr("I love FishC.com!iiiiiiiiii")
# b = Nstr("i")
# print(a - b)

# class Nstr(str):
#     def __lshift__(self, other):
#         return self[other:] + self[:other]
# 
#     def __rshift__(self, other):
#         return self[-other:] + self[:-other]
#
# a = Nstr("I love FishC.com!")
# print(a >> 5)
# print(a << 5)

# import time as t
#
# class MyTimer():
#
#     def __init__(self):
#         self.unit = ["年", "月", "天", "小时", "分钟", "秒"]
#         self.prompt = "未开始计时！"
#         self.lasted = []
#         self.start = 0
#         self.stop = 0
#
#     def __str__(self):
#         return self.prompt
#
#     __repr__ = __str__
#
#     def __add__(self, other):
#         prompt = "总共运行了"
#         result = []
#         for index in range(6):
#             result.append(self.lasted[index] + other.lasted[index])
#             if result[index]:
#                 prompt += (str(result[index]) + self.unit[index])
#         return prompt
#
#     # 开始计时
#     def start1(self):
#         self.start = t.localtime()
#         self.prompt = "提示：请先调用stop1()停止计时！"
#         print("计时开始...")
#
#     # 停止计时
#     def stop1(self):
#         if not self.start:
#             print("提示：请先调动start1()进行计时！")
#         else:
#             self.stop = t.localtime()
#             self._calc()
#             print("停止计时...")
#
#     # 内部方法，计算运行时间
#     def _calc(self):
#         self.lasted = []
#         self.prompt = "总共运行了"
#         for index in range(6):
#             self.lasted.append(self.stop[index] - self.start[index])
#             if self.lasted[index]:
#                 self.prompt += (str(self.lasted[index]) + self.unit[index])
#
#         # 为下一轮计时初始化变量
#         self.start = 0
#         self.stop = 0
#
#
# t1 = MyTimer()
# t1.start1()
# t.sleep(5)
# t1.stop1()
# # print(t1)
# # t1.stop1()
#
# t2 = MyTimer()
# t2.start1()
# t.sleep(3)
# t2.stop1()
#
# print(t1 + t2)

# import time as t
#
# class MyTimer:
#
#     # 设置默认参数
#     def __init__(self):
#         self.unit = ["年", "月", "天", "小时", "分钟", "秒"]
#         self.borrow = [0, 12, 31, 24, 60, 60]
#         self.prompt = "未开始计时！"
#         self.lasted = []
#         self.begin = 0
#         self.end = 0
#
#     def __str__(self):
#         return self.prompt
#
#     __repr__ = __str__
#
#     def __add__(self, other):
#         prompt = "总共运行了"
#         result = []
#         for index in range(6):
#             result.append(self.lasted[index] + other.lasted[index])
#             if result[index]:
#                 prompt += (str(result[index]) + self.unit[index])
#         return prompt
#
#     def start(self):
#         self.begin = t.localtime()
#         self.prompt = "提示：请先调用stop()停止计时！"
#         print("计时开始...")
#
#     def stop(self):
#         if not self.begin:
#             print("提示：请先调用start()进行计时！")
#         else:
#             self.end = t.localtime()
#             self._calc()
#             print("计时结束！")
#
#     def _calc(self):
#         self.lasted = []
#         self.prompt = "总共运行了"
#         for index in range(6):
#             temp = self.end[index] - self.begin[index]
#
#             # 低位不够减，需向高位借位
#             if temp < 0:
#                 # 测试高位是否有得借，没得借的话再向高位借
#                 i = 1
#                 while self.lasted[index - i] < 1:
#                     self.lasted[index - i] += self.borrow[index - i] - 1
#                     self.lasted[index - i - 1] -= 1
#                     i += 1
#
#                 self.lasted.append(self.borrow[index] + temp)
#                 self.lasted[index - 1] = 1
#
#             else:
#                 self.lasted.append(temp)
#
#         # 由于高位随时会被借位，所以打印要放在最后
#         for index in range(6):
#             if self.lasted[index]:
#                 self.prompt += str(self.lasted[index]) + self.unit[index]
#
#
#         # 为下一轮计时初始化变量
#         self.begin = 0
#         self.end = 0
#
# t1 = MyTimer()
# t1.start()
# t.sleep(30)
# t1.stop()
# print(t1)

# t2 = MyTimer()
# t2.start()
# t.sleep(3)
# t2.stop()
# print(t2)
#
# print(t1 + t2)

# import time
# a1=time.perf_counter()
# a2=time.process_time()
# c=1
# for i in range(1,20000):
#     c*=i
# b1=time.perf_counter()
# b2=time.process_time()
# print(b1-a1,'s')
# print(b2-a2,'s'

# import time as t
#
# class Mytimer:
#     def __init__(self):
#         self.prompt = "未开始计时"
#         self.lasted = 0.0
#         self.begin = 0
#         self.end = 0
#         self.default_time = t.perf_counter
#
#     def __str__(self):
#         return self.prompt
#
#     __repr__ = __str__
#
#     def __add__(self, other):
#         result = self.lasted + other.lasted
#         prompt = "总共运行了%0.2f秒" % result
#         return prompt
#
#     def start(self):
#         self.begin = self.default_time()
#         self.prompt = "提示：请先调用stop()停止计时！"
#         print("计时开始...")
#
#     def stop(self):
#         if not self.begin:
#             print("提示：请先调用start()进行计时！")
#         else:
#             self.end = self.default_time()
#             self._calc()
#             print("计时结束！")
#
#     def _calc(self):
#         self.lasted = self.end - self.begin
#         self.prompt = "总共运行了%0.2f秒" % self.lasted
#
#         self.begin = 0
#         self.end = 0
#
#     def set_timer(self, timer):
#         if timer == "process_time":
#             self.default_time = t.process_time()
#
#         elif timer == "pert_counter":
#             self.default_time = t.perf_counter()
#
#         else:
#             print("输入无效，请输入perf_counter或process_time")
#
#
# t1 = Mytimer()
# t1.set_timer("process_time")
# t1.start()
# t.sleep(5)
# t1.stop()
# print(t1)
#
# t2 = Mytimer()
# t2.set_timer("process_time")
# t2.start()
# t.sleep(3)
# t2.stop()
# print(t2)
#
# print(t1 + t2)


# import time as t
#
#
# class MyTimer:
#     def __init__(self):
#         self.prompt = "未开始计时！"
#         self.lasted = 0.0
#         self.begin = 0
#         self.end = 0
#         self.default_timer = t.perf_counter
#
#     def __str__(self):
#         return self.prompt
#
#     __repr__ = __str__
#
#     def __add__(self, other):
#         result = self.lasted + other.lasted
#         prompt = "总共运行了 %0.2f 秒" % result
#         return prompt
#
#     # 开始计时
#     def start(self):
#         self.begin = self.default_timer()
#         self.prompt = "提示：请先调用 stop() 停止计时！"
#         print("计时开始...")
#
#     # 停止计时
#     def stop(self):
#         if not self.begin:
#             print("提示：请先调用 start() 进行计时！")
#         else:
#             self.end = self.default_timer()
#             self._calc()
#             print("计时结束！")
#
#     # 内部方法，计算运行时间
#     def _calc(self):
#         self.lasted = self.end - self.begin
#         self.prompt = "总共运行了 %0.2f 秒" % self.lasted
#
#         # 为下一轮计时初始化变量
#         self.begin = 0
#         self.end = 0
#
#     # 设置计时器(time.perf_counter() 或 time.process_time())
#     def set_timer(self, timer):
#         if timer == 'process_time':
#             self.default_timer = t.process_time
#         elif timer == 'perf_counter':
#             self.default_timer = t.perf_counter
#         else:
#             print("输入无效，请输入 perf_counter 或 process_time")
#
# t1 = MyTimer()
# t1.start()
# t.sleep(5)
# t1.stop()
# print(t1)

# class C:
#     def __init__(self):
#         self.x = "x-man"
#
# c = C()
# print(c.x)
# print(getattr(c, 'x', '没有这个属性'))
# print(getattr(c, 'y', '没有这个属性'))

# class C:
#     def __init__(self, size = 0):
#         self.size = size
#     def getSize(self):
#         return self.size
#     def setSize(self, value):
#         self.size = value
#     def delSize(self):
#         del self.size
#
#     x = property(getSize, setSize, delSize)
#
# c = C()
# print(c.x)
# c.x = 1
# print(c.size)
# del c.x
# print(c.x)

# class C:
#     def __getattr__(self, name):
#         print("getattr")
#     def __getattribute__(self, name):
#         print("getatteribute")
#         return super().__getattribute__(name)
#     def __setattr__(self, name, value):
#         print("setattr")
#         super().__setattr__(name, value)
#     def __delattr__(self, name):
#         print("delattr")
#         super().__delattr__(name)
#
# c = C()
# c.x
# c.x = 1
# print(c.x)
# del c.x

# class Rectangle:
#     def __init__(self, width = 0, height = 0):
#         self.width = width
#         self.height = height
#
#     def __setattr__(self, name, value):
#         if name == "square":
#             self.width = value
#             self.height = value
#         else:
#             super(Rectangle, self).__setattr__(name, value)
#
#     def getArea(self):
#         return print(self.width * self.height)
#
# r = Rectangle(4, 5)
# r.getArea()
# r.square = 10
# print(r.width)
# print(r.height)
# r.getArea()

# class Counter:
#     def __init__(self):
#         self.counter = 0
#     def __setattr__(self, key, value):
#         self.counter += 1
#         super(Counter, self).__setattr__(key, value)
#     def __delattr__(self, key):
#         self.counter -= 1
#         super(Counter, self).__delattr__(key)
#
# c = Counter()

# class Counter:
#     def __init__(self):
#         # self.counter = 0
#         super(Counter, self).__setattr__("counter", 0)
#
#     def __setattr__(self, name, value):
#         super(Counter, self).__setattr__("counter", self.counter + 1)
#         super(Counter, self).__setattr__(name, value)
#     def __delattr__(self, name):
#         super(Counter, self).__setattr__("counter", self.counter - 1)
#         super(Counter, self).__delattr__(name)
#
# c = Counter()
# c.x = 1
# print(c.counter)
# c.y = 1
# c.z = 1
# print(c.counter)
# del c.x
# print(c.counter)

# class MyProperty:
#     def __init__(self, fget = None, fset = None, fdel = None):
#         self.fget = fget
#         self.fset = fset
#         self.fdel = fdel
#
#     def __get__(self, instance, owner):
#         return self.fget(instance)
#
#     def __set__(self, instance, value):
#         self.fset(instance, value)
#
#     def __delete__(self, instance):
#         self.fdel(instance)
#
# class C:
#     def __init__(self):
#         self._x = None
#
#     def getx(self):
#         return self._x
#
#     def setx(self, value):
#         self._x = value
#
#     def delx(self):
#         del self._x
#
#     x = MyProperty(getx, setx, delx)
#
# c = C()
# c.x = 'x-man'
# print(c.x)
# print(c._x)
# del c.x

# class MyDes:
#     def __get__(self, instance, owner):
#         print("getting...")
#
# class Test:
#     a = MyDes()
#     x = a
#
# t = Test()
# t.a
# t.x

# class MyDes:
#     def __init__(self, initval = None, name = None):
#         self.val = initval
#         self.name = name
#
#     def __get__(self, instance, owner):
#         print("正在获取变量：", self.name)
#         return self.val
#
#     def __set__(self, instance, value):
#         print("正在修改变量：", self.name)
#         self.val = value
#
#     def __delete__(self, instance):
#         print("正在删除变量：", self.name)
#         print("噢~这个变量没法删除~")
#
# class Test:
#     x = MyDes(10, 'x')
#
# t = Test()
# y = t.x
# print(y)
# t.x = 8
# del t.x
# print(t.x)
# print(y)

# import time
#
# class Record:
#     def __init__(self, initval = None, name = None):
#         self.val = initval
#         self.name = name
#         self.filename = r"C:\Users\zhangyi\Desktop\record.txt"
#
#     def __get__(self, instance, owner):
#         with open(self.filename, "a", encoding = 'utf-8') as f:
#             f.write("%s 变量于北京时间 %s 被读取，%s = %s \n" %
#                     (self.name, time.ctime(), self.name, str(self.val)))
#         return self.val
#
#     def __set__(self, instance, value):
#         # filename = "%s_record.txt" % self.name
#         with open(self.filename, 'a', encoding = 'utf-8') as f:
#             f.write("%s 变量于北京时间 %s 被修改，%s = %s \n" %
#                     (self.name, time.ctime(), self.name,str(value)))
#         self.val = value
#
# class Test:
#     x = Record(10, 'x')
#     y = Record(8.8, 'y')
#
# t = Test()
# t.x
# t.y
# t.x = 123
# t.x = 1.23
# t.y = "I love FishC.com!"

# class CountList:
#     def __init__(self, *args):
#         self.values = [x for x in args]
#         self.count = {}.fromkeys(range(len(self.values)), 0)
#
#     def __len__(self):
#         return len(self.values)
#
#     def __getitem__(self, item):
#         self.count[item] += 1
#         return self.values[item]
#
# c1 = CountList(1, 3, 5, 7, 9)
# c2 = CountList(2, 4, 6, 8, 10)
# print(c1[1])
# print(c2[1])
# print(c1[1] + c2[1])
# print(c1.count)
# print(c2.count)

# class CountList(list):
#     def __init__(self, *args):
#         super(CountList, self).__init__(args)
#         self.count = []
#         for i in args:
#             self.count.append(0)
#
#     def __len__(self):
#         return len(self.count)
#
#     def __getitem__(self, key):
#         self.count[key] += 1
#         return super(CountList, self).__getitem__(key)
#
#     def __setitem__(self, key, value):
#         self.count[key] += 1
#         super(CountList, self).__setitem__(key, value)
#
#     def __delitem__(self, key):
#         del self.count[key]
#         super(CountList, self).__delitem__(key)
#
#     def counter(self, key):
#         return self.count[key]
#
#     def append(self, value):
#         self.count.append(0)
#         super(CountList, self).append(value)
#
#     def pop(self, key = -1):
#         del self.count[key]
#         return super(CountList, self).pop(key)
#
#     def remove(self, value):
#         key = super().index(value)
#         del self.count[key]
#         super(CountList, self).remove(value)
#
#     def insert(self, key, value):
#         self.count.insert(key, 0)
#         super(CountList, self).insert(key, value)
#
#     def clear(self):
#         self.count.clear()
#         super(CountList, self).clear()
#
#     def reverse(self):
#         self.count.reverse()
#         super(CountList, self).reverse()
#

# string = "FishC!"
# it = iter(string)
# print(next(it))
#
# while 1:
#     try:
#         each = next(it)
#
#     except:
#         break
#     print(each)

# class Fibs:
#     def __init__(self, n = 20):
#         self.a = 0
#         self.b = 1
#         self.n = n
#
#     def __iter__(self):
#         return self
#
#     def __next__(self):
#         self.a, self.b = self.b, self.a + self.b
#         if self.a > self.n:
#             raise StopIteration
#         return self.a
#
# fibs = Fibs()
# for each in fibs:
#     if each < 10000:
#         print(each)
#
#     else:
#         break

# import  datetime as dt
#
# class LeapYear:
#     def __init__(self):
#         self.now = dt.date.today().year
#
#     def isLeapYear(self, year):
#         if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
#             return True
#         else:
#             return False
#
#     def __iter__(self):
#         return self
#
#     def __next__(self):
#         while not self.isLeapYear(self.now):
#             self.now -= 1
#
#         temp = self.now
#         self.now -= 1
#
#         return temp

# class MyRev:
#     def __init__(self, data):
#         self.data = data
#         self.index = len(data)
#
#     def __iter__(self):
#         return self
#
#     def __next__(self):
#         if self.index == 0:
#             raise StopIteration
#
#         self.index = self.index - 1
#         return self.data[self.index]

# a = [i for i in range(100) if not (i % 2) and (i % 3)]
# print(a)
#
# b = {i : i % 2 == 0 for i in range(10)}
# print(b)
#
# c = {i for i in [1, 1, 2, 3, 4, 5, 5, 6, 7, 8, 3, 2, 1, ]}
# print(c)
#
# d = 'i for i in "I love FishC.com!"'
# print(d)

# e = (i for i in range(10))
# print(e)
# print(next(e))
# print(next(e))
# for i in e:
#     print(i)

# def myGen():
#     print("生成器被执行1")
#     yield 1
#     print("生成器被执行2")
#     yield 2
#     print("生成器被执行3")
#
# m = myGen()
# print(next(m))
# print(next(m))
# print(next(m))

# def fibs():
#     a = 0
#     b = 1
#     while True:
#         a, b = b, a + b
#         yield a, b
#
# f = fibs()
# print(next(f))
# print(next(f))
# print(next(f))

# for each in fibs():
#     if each > 100:
#         break
#     print(each, end = ' ')

# a = [i for i in range(100) if not (i % 2) and (i % 3)]
# print(a)
#
# b = [i for i in range(100)
#      if not (i % 2) and (i % 3)]
# print(b)

# class Const:
#     def __setattr__(self, key, value):
#         if key in self.__dict__:
#             raise TypeError("常量无法改变！")
#
#         if not key.isupper():
#             raise TypeError("常量名必须由大写字母组成！")
#
#         self.__dict__[key] = value
#
# import sys
# sys.modules[__name__] = Const()

# class A(object):
#     """
#     Class test.
#     """
#
#     a = 0
#     b = 1
#
#     def __init__(self):
#         self.a = 2
#         self.b = 3
#
#     def test(self):
#         print('a normal func.')
#
#     @staticmethod
#     def static_test(self):
#         print('a static func.')
#
#     @classmethod
#     def class_test(self):
#         print('a calss func.')
#
#
# obj = A()
# print(A.__dict__)
# print(obj.__dict__)

# import sys
# s = sys.path
# print(s)

# import time as t
# print(t.__doc__)
# print(dir(t))
# print(t.__file__)

# def c():
#     pass
# b = c()
# print(type(b))

# class A:
#     def __init__(self, x):
#         self.x = x
#
#
# a = A(100)
# a.__dict__['y'] = 50
# a.__dict__['z'] = 0
# print(a.y)
# print(len(a.__dict__))
# print(a.__dict__['x'])
# print(a.__dict__['y'])
# print(a.__dict__['z'])
#
# print(a.y + len(a.__dict__))

# country_counter = {}
#
#
# def addone(country):
#     if country in country_counter:
#         country_counter[country] += 1
#     else:
#         country_counter[country] = 1
#
#
# addone('China')
# addone('Japan')
# addone('China')
# addone("American")
#
# print(len(country_counter))
# print(country_counter['China'])
# print(country_counter['Japan'])

# dict1 = {}
# dict1[1] = 1
# dict1['1'] = 2
# dict1[1.0] = 3
# print(dict1)
#
# result = 0
# for each in dict1:
#     print("字典的值：", dict1[each])
#     result += dict1[each]
#     print("result的值：", result)


# list1 = [1, 2]
# list2 = [3, 4]
#
# dict1 = {'1': list1, '2': list2}
# dict2 = dict1.copy()
#
# dict1['1'][0] = 5
# print(dict1)
# print(dict2)
#
# result = dict1['1'][0] + dict2['1'][0]
# print(result)

# dict1 = {'user': 'runoob', 'num': [1, 2, 3]}
#
# dict2 = dict1  # 浅拷贝: 引用对象
# dict3 = dict1.copy()  # 浅拷贝：深拷贝父对象（一级目录），子对象（二级目录）不拷贝，还是引用
#
# # 修改 data 数据
# dict1['user'] = 'root'
# dict1['num'].remove(1)
#
# # 输出结果
# print(dict1)
# print(dict2)
# print(dict3)

# list1 = [1, 3, 'a', [1, 3, 5], "zzz"]
# list2 = list1.copy()
#
# list1.append(4)
# list1[3].append(4)
#
# print(list1)
# print(list2)

# import urllib.request as url
# u = url.urlopen("http://www.fishc.com")
# html = u.read()
# print(html, end = '\n')
#
# html = html.decode("utf-8")
# print(html, end = '\n')

# import urllib.request as urlr
# import chardet
#
# response = urlr.urlopen("http://www.fishc.com")
# # print(type(response))
# html = response.read()
# print(html.decode('utf-8'))
#
# def bm():
#     url = r"https://www.bilibili.com"
#
#     respense = urlr.urlopen(url)
#     html = respense.read()
#
#     encode = chardet.detect(html)["encoding"]
#     if encode == "GB2312":
#         encode = "GBK"
#
#     print("该网页使用的编码是：%s" % encode)
#
# if __name__ == '__main__':
#     bm()

# import urllib.request as urlr
# import chardet
#
# def main():
#     i = 0
#
#     with open("urls.txt", "r") as f:
#         urls = f.read().splitlines()
#
#     for each_url in urls:
#         response = urlr.urlopen(each_url)
#         html = response.read()
#
#         encode = chardet.detect(html)["encoding"]
#         if encode == "GB2312":
#             encode = "GBK"
#
#         i += 1
#         filename = "url_%d.txt" % i
#
#         with open(filename, 'w', encoding = 'utf-8') as each_file:
#             each_file.write(html.decode(encode, 'ignore'))
#
# if __name__ == '__main__':
#     main()


# str1 = 'ab c\n\nde fg\rkl\r\n'
# str2 = str1
#
# print(str1.splitlines())
# print(str2.splitlines(True))

# a = '你好啊！'
# print(a)
# A = a.encode()
# print(A)
# b = A.decode()
# print(b)
#
# with open(r"C:\Users\zhangyi\Desktop\test.txt", 'a') as f:
#     f.write(a)
# with open(r"C:\Users\zhangyi\Desktop\test.txt", 'wb+') as e:
#     e.write(A)

# import urllib.request as urlr
#
# # response = urlr.urlopen("http://placekitten.com/g/100/100")
# rep = urlr.Request("http://placekitten.com/g/100/100")
# response = urlr.urlopen(rep)
#
# cat_img = response.read()
#
# print(response.geturl())
# print(response.info())
# print(response.getcode())
#
#
# # with open(r"C:\Users\zhangyi\Desktop\cat.jpg", 'wb') as f:
# #     f.write(cat_img)

# import urllib.request as urlr
# import urllib.parse as urlp
# import json
#
# url = 'http://fanyi.youdao.com/translate?smartresult=dict&smartresult=rule'
# data = {}
# data['i'] = 'monkey'
# data['from'] = 'AUTO'
# data['to'] = 'AUTO'
# data['smartresult'] = 'dict'
# data['client'] = 'fanyideskweb'
# data['salt'] = '15601371827906'
# data['sign'] = '714e2fbaafcb1f4c27a1c66a7cf66482'
# data['ts'] = '1560137182790'
# data['bv'] = '140f03b6cc43b5b1fabe089d78dc366f'
# data['doctype'] = 'json'
# data['version'] = '2.1'
# data['keyfrom'] = 'fanyi.web'
# data['action'] = 'FY_BY_CLICKBUTTION'
# data = urlp.urlencode(data).encode('utf-8')
#
# response = urlr.urlopen(url, data)
# html = response.read().decode('utf-8')
#
# print(html)
#
# # tanget = json.loads(html)
# tanget = json.dumps(html)
# print(tanget)

# string1 = "我爱"
# string2 = u'FishC'
# print(string1.encode())
# print(string2)
# print(string1 + string2)
# print(type(string1))
# print(type(string2))

# import easygui as g
# import urllib.request as urlr
#
# def main():
#     msg = '请填写喵的尺寸'
#     title = '下载一只喵'
#     fieldNames = ['宽：', '高：']
#     fieldValues = []
#     size = width, heigh = 400, 600
#     fieldValues = g.multenterbox(msg, title, fieldNames, size)
#
#     while 1:
#         if fieldValues == None:
#             break
#         errmsg = ''
#
#         try:
#             width = int(fieldValues[0].strip())
#         except:
#             errmsg += '宽度必须为整数'
#
#         try:
#             heigh = int(fieldValues[1].strip())
#         except:
#             errmsg += '高度必须为整数'
#
#         if errmsg == '':
#             break
#
#         fieldValues = g.multenterbox(errmsg, title, fieldNames, fieldValues)
#
#     url = 'http://placekitten.com/g/%d/%d' % (width, heigh)
#
#     response = urlr.urlopen(url)
#     cat_img = response.read()
#
#     filepath = g.diropenbox("请选择存放喵的文件夹")
#
#     if filepath:
#         filename = "%s/cat_%d_%d.jpg" % (filepath, width, heigh)
#     else:
#         filename = 'cat_%d_%d.jpg' % (width, heigh)
#
#     with open(filename, 'wb') as f
#         f.write(cat_img)
#
# if __name__ == '__main__':
#     main()

# import re
# import urllib.request
# import urllib.parse
# from http.cookiejar import CookieJar
#
# # 豆瓣的登录url
# loginurl = 'https://www.douban.com/accounts/login'
# cookie = CookieJar()
# opener = urllib.request.build_opener(urllib.request.HTTPCookieProcessor)
#
# data = {
#     "from_email" : "your email",
#     "from_password" : "your password",
#     "source" : "index_nav"
# }
#
#
# data = {}
# data["from_email"] = "你的账号"
# data["from_password"] = "你的密码"
# data["source"] = 'index_nav'
#
# # print(urllib.parse.urlencode(data).encode('utf-8'))
# response = opener.open(loginurl, urllib.parse.urlencode(data).encode("utf-8"))
#
# # 验证成功跳转至登录页
# if response.geturl() == "https://www.douban.com/accouts/login":
#     html = response.read.decode()
#
#     # 验证码图片地址
#     imgurl = re.search('<img id="captcha_image" src="(.+?)" alt="captcha" class="captcha_image"/>', html)
#     if imgurl:
#         url = imgurl.group(1)
#         # 将验证码图片保存至同目录下
#         res = urllib.request.urlretrieve(url, 'v.jpg')
#
#         # 获取captcha-id参数
#         captcha = re.search('<input type="hidden" name="captcha-id" value="(.+?)"/>' ,html)
#
#         if captcha:
#             vcode = input("请输入图片上的验证码：")
#             data['captcha-solution'] = vcode
#             data['captcha-id'] = captcha.group(1)
#             data['user_login'] = '登录'
#
#             # 提交验证码验证
#             response = opener.open(loginurl, urllib.parse.urlencode(data).encode('utf-8'))
#
#             # 登录成功跳转至首页
#             if response.geturl() == "http://www.douban.com/":
#                 print('登录成功！')

# import requests
# import urllib.request
# import json
# import pprint
#
# url = 'https://api.bilibili.com/x/v2/reply?jsonp=jsonp&pn=1&type=1&oid=45382106&sort=2&_=1560328918643'
#
# # response = urllib.request.urlopen(url)
# # html = response.read().decode('utf-8')
# # data = json.loads(html)
# # print(data)
# # pprint.pprint(data)
#
# response = requests.get(url)
# data = json.loads(response.text)
# print(data)
# pprint.pprint(data)


# response = urllib.request.urlopen("https://api.bilibili.com/x/v2/reply?jsonp=jsonp&pn=1&type=1&oid=45382106&sort=2&_=1560328918643")
# r = response.read().decode("utf-8")
# r = requests.get("https://api.bilibili.com/x/v2/reply?jsonp=jsonp&pn=1&type=1&oid=45382106&sort=2&_=1560328918643")
# data = json.loads(r)
# print(data)
# pprint.pprint(data)


# import urllib.request
# import urllib.parse
# import json
# print('----------这是一个Python翻译器------------')
#
# # content = input("请输入需要翻译的内容")
# content = 'I love FishC.com'
#
# url = "http://fanyi.youdao.com/translate?smartresult=dict&smartresult=rule"
# # 直接从审查元素中copy过来的url会报错，必须把translate_o中的_o删除才可以
# # url = "http://fanyi.youdao.com/translate_o?smartresult=dict&smartresult=rule"
#
# head = {}
# head['User-Agent'] = 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'
#
# data = {}
# data['i'] = 'I love FishC.com'
# data['from'] = 'AUTO'
# data['to'] = 'AUTO'
# data['smartresult'] = 'dict'
# data['client'] = 'fanyideskweb'
# data['salt'] = '15608241237857'
# data['sign'] = '1dc2f7d63d3736e82c95e43f85ddeacf'
# data['ts'] = '1560824123785'
# data['bv'] = '140f03b6cc43b5b1fabe089d78dc366f'
# data['doctype'] = 'json'
# data['version'] = '2.1'
# data['keyfrom'] = 'fanyi.web'
# data['action'] = 'FY_BY_CLICKBUTTION'
#
# # 需要使用urllib.parse.urlencode() 把data转换为需要的形式
# data = urllib.parse.urlencode(data).encode('utf-8')
# print('data是：', data)
#
# request = urllib.request.Request(url, data, head)
# response = urllib.request.urlopen(url, data)
# html = response.read().decode('utf-8')
# print('html是：', html)
#
# target = json.loads(html)
#
# print('翻译结果：%s' % (target["translateResult"][0][0]["tgt"]))

# import urllib.request
# import random
# from bs4 import BeautifulSoup
#
# url = 'http://ip.tool.chinaz.com/'
#
# headers = {}
# headers['User-Agent'] = 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'
#
# # ip_list = ['61.187.206.207:39835', '140.143.142.218:1080', '101.200.50.18:8118']
# # proxy_support = urllib.request.ProxyHandler({'http' : random.choice(ip_list)})
#
# proxy_support = urllib.request.ProxyHandler({'http' : '61.187.206.207:39835'})
#
# opener = urllib.request.build_opener(proxy_support)
#
# # urllib.request.install_opener(opener)
#
# red = urllib.request.Request(url, headers = headers)
#
# response = opener.open(red)
#
# html = response.read().decode('utf-8')
#
# soup = BeautifulSoup(html)
#
# print(soup.prettify())

# import urllib.request
# import re
# from bs4 import BeautifulSoup
#
# def main():
#     url = 'https://baike.baidu.com/item/%E7%BD%91%E7%BB%9C%E7%88%AC%E8%99%AB'
#
#     response = urllib.request.urlopen(url)
#     html = response.read()
#     soup = BeautifulSoup(html, 'html.parser')
#     # soup = BeautifulSoup(html)
#
#     # print(soup)
#
#     for each in soup.find_all(href = re.compile('view')):
#         print(each.text, '->', ''.join(["http://baike.baidu.com", each['href']]))
#         print(each.text, soup.find_all(href = re.compile('view') ))
#
# if __name__ == '__main__':
#     main()

# import urllib.request
# import urllib.parse
# import re
# from bs4 import BeautifulSoup
# import chardet
# import time
#
#
# def main():
#     # keyword = input('请输入关键词：')
#     keyword = '猪八戒'
#     keyword = urllib.parse.urlencode({'word' : keyword})
#     # print(keyword)
#     url = "http://baike.baidu.com/search/word?%s" % keyword
#     header = 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'
#
#     req = urllib.request.Request(url)
#     req = req.add_header('User-Agent', header)
#     response = urllib.request.urlopen(req)
#
#     # url = 'https://baike.baidu.com/'
#     # response = urllib.request.urlopen(url, data = keyword)
#
#     html = response.read().decode('utf-8')
#     # c = chardet.detect(html)
#     # print(c)
#
#     soup = BeautifulSoup(html, 'html.parser')
#     # print(soup)
#
#     time.sleep(5)

# for each in soup.find_all(href = re.compile('view')):
#     print(each)
# content = ''.join([each.text])
# url2 = ''.join(["http://baike.baidu.com", each["href"]])
#
# req2 = urllib.request.Request(url2)
# req2 = req2.add_header('User-Agent', header)
#
# try:
#     response2 = urllib.request.urlopen(req2)
#
# except:
#     print(timeout)
#
# html2 = response2.read().decode('utf-8')


# soup2 = BeautifulSoup(html2, 'html.parser')
# if soup2.h2:
#     content = ''.join([content, soup2.h2.text])
# content = ''.join([content, '->', url2])
# print(content)


#
# if __name__ == '__main__':
#     main()

# import re
#
# pattern = re.compile('[a-zA-Z]')
#
# result = pattern.findall('as3SiOP')
#
# print(result)


# import urllib.request
# import urllib.parse
# from bs4 import BeautifulSoup
# import time
# import re
#
#
# class BaiKePaChong():
#
#     def __init__(self):
#         self.header = {}
#         self.header['User-Agent'] = 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'
#
#     def _testUrl(self, soup):
#         result = soup.find(text=re.compile("百度百科尚未收录词条"))
#         if result:
#             print(result[0 : -1])
#             return False
#         else:
#             return True
#
#     def _summary(self, soup):
#         word = soup.h1.text
#         # 如果存在副标题，一起打印
#         if soup.h2:
#             word += soup.h2.text
#         print(word)
#
#         if soup.find(class_='lemma-summary'):
#             print(soup.find(class_='lemma-summary').text)
#
#     def _getUrls(self, soup):
#         for each in soup.find_all(href=re.compile('view')):
#             if each.text == '':
#                 continue
#             else:
#                 content = ''.join([each.text])
#                 url2 = ''.join(["http://baike.baidu.com", each['href']])
#
#             zhongwen = re.compile(u'[\u4e00-\u9fa5]')
#
#             if zhongwen.search(url2):
#                 pass
#
#             else:
#                 req2 = urllib.request.Request(url2, headers=self.header)
#                 response2 = urllib.request.urlopen(req2)
#                 html2 = response2.read()
#                 soup2 = BeautifulSoup(html2, 'html.parser')
#
#                 if soup2.h2:
#                     content = ''.join([content, soup2.h2.text])
#
#                 content = ''.join([content, ' -> ', url2])
#                 yield content
#
#     def main(self):
#
#         keyword = input("请输入关键词：")
#         keyword = urllib.parse.urlencode({'word': keyword})
#         url = "http://baike.baidu.com/search/word?%s" % keyword
#
#         req = urllib.request.Request(url, headers=self.header)
#         # req = req.add_header(header)
#         response = urllib.request.urlopen(req)
#         html = response.read().decode('utf-8')
#         soup = BeautifulSoup(html, 'html.parser')
#
#         b = BaiKePaChong()
#         if b._testUrl(soup):
#             b._summary(soup)
#
#             print("下边打印相关链接：")
#             each = b._getUrls(soup)
#             while True:
#                 try:
#                     for i in range(10):
#                         print(next(each))
#
#                 except StopIteration:
#                     break
#
#                 command = input("输入任意字符将继续打印，q退出程序：")
#                 if command == 'q':
#                     break
#
#                 else:
#                     continue
#
#
# if __name__ == '__main__':
#     m = BaiKePaChong()
#     m.main()


# import urllib.request
# import os
# import random
#
#
# def url_open(url):  # 打开浏览器地址
#
#     header = {}
#     header[
#         'User-Agent'] = 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'
#
#     # 使用代理
#     # proxies = ['119.6.144.70:81', '111.1.36.9:80', '203.144.144.162:8080']
#     # proxy = random.choice(proxies)
#
#     req = urllib.request.Request(url, headers=header)
#
#     # 使用代理
#     # proxy_support = urllib.request.ProxyHandler({'http' : self.proxy})
#     # opener = urllib.request.build_opener(proxy_support)
#     # urllib.request.install_opener(opener)
#
#     response = urllib.request.urlopen(url)
#     html = response.read()
#
#     return html
#
#
# def get_page(url):  # 得到最新页面的页码数
#     html = url_open(url)
#     html = html.decode('utf-8')  # 因为要以字符串形式查找，所以要decode解码
#
#     # 然后就是查找html中的'current-comment-page'
#     a = html.find('current-comment-page') + 23  # 加上23位偏移就刚到页码数的第一位数字
#     b = html.find(']', a)  # 找到a位置之后的第一个方括号所在位置的索引坐标
#
#     return html[a: b]  # 这就是最新的页码数
#
#
# def find_imgs(url):  # 给一个页面的链接，返回所有图片地址组成的列表
#     html = url_open(url).decode('utf-8')
#     img_addrs = []  # 声明一个保存图片地址的列表
#
#     # 查找图片地址
#     a = html.find('img src=')
#     while a != -1:
#         b = html.find('.jpg', a, a + 255)  # 在a到a+255区间找'.jpg'，防止有不是'.jpg'格式的图片
#         # 如果b找不到，b就返回-1
#         if b != -1:
#             img_addrs.append('http:' + html[a + 9:b + 4])
#         else:
#             b = a + 9
#
#         a = html.find('img src=', b)
#     print(img_addrs)
#
#     return img_addrs
#
#
# def save_imgs(folder, img_addrs):
#     for each in img_addrs:
#         filename = each.split('/')[-1]
#         print(filename)
#         with open(filename, 'wb') as f:
#             img = url_open(each)
#             f.write(img)
#
#
# def download_photo(folder=r'C:\Users\zhangyi\Desktop\Photo', pages=10):
#     os.mkdir(folder)  # 创建文件夹
#     os.chdir(folder)  # 改变工作目录
#
#     url = "http://jandan.net/ooxx/"  # 随手拍栏目的连接，也就是最新页面的连接
#     page_num = int(get_page(url))  # 得到最新页面的页码数
#
#     for i in range(pages):
#         page_url = url + 'page-' + str(page_num) + '#comments'  # 得到要爬取页面的连接
#         print(page_url)
#         img_addrs = find_imgs(page_url)  # 得到页面所有图片的地址，保存为列表
#         save_imgs(folder, img_addrs)  # 保存图片到本地文件夹
#         page_num -= 1  # 逐步找到前几个页面
#
#
# if __name__ == '__main__':
#     download_photo()

# import  re
#
#
# '''1介绍^ . * $的用法
# ^ 匹配输入字符串开始的位置。
# . 匹配除换行符 \n 之外的任何单字符。
# * 匹配前面的子表达式零次或多次。
# $ 匹配输入字符串的结尾位置。
# '''
#
# #需要匹配的字符串
# line = "hello world"
#
# 1.打印 以h 开头的文字

# regex_str = '^h'
# if re.match(regex_str, line):
#     print("1, 打印以h 开头的文字")
#
# #2.打印 以h 开头，后面跟着一个字符串
# regex_str = '^h.'
# if re.match(regex_str, line):
#     print("2, 打印以h 开头，后面跟着一个字符串")
#
# #3.打印以h 开头，跟任意数量字符串
# regex_str = '^h*'
# if re.match(regex_str, line):
#     print("3, 打印以h 开头，后面任意数量的字符串")
#
# #4以d 结尾
# regex_str = '.*d$'
# if re.match(regex_str, line):
#     print("4, 匹配以d 结尾的字符串")
#
# #5 以h 开头，以d 结尾，中间只有任意一个字符串
# regex_str = '^h.d$'
# if re.match(regex_str, line):
#     print("5, 以h 开头， 以d 结尾，中间只有任意一个字符串")
#
# #6 以h 开头， 以d 结尾，中间任意字符串
# regex_str = '^h.*d$'
# if re.match(regex_str, line):
#     print("6, h开头，以d 结尾，中间任意一个字符串")

# import re
#
# a = 'abccccfdsfcbbbbbdefga'
# b = re.search(r"a$", a)
# print(b)
# c = re.findall(r'[n^]', 'FishC.com\n')
# print(c)
#
# d = "<html><title>I love FishC.com</title><html>"
# f = re.search(r"<.+>", d)
# print(f)

# import re
# b = re.findall(r'\bFishC\b', 'FishC.com!FishC_com!(FishC)')
# c = re.findall(r'FishC\B', 'FishC.com!FishC_com!(FishC)')
# print(b)
# print(c)

# import re

# charref = re.compile(r'''
# %[#]                    # 开始数字引用
# (
#     0[0-7]+             # 八进制格式
#    |[0-9]+              # 十进制格式
#    |x[0-9a-fA-F]        # 十六进制格式
# )
# ;                       # 结尾分好
# ''', re.X)

# result = re.search(r" (\w+) (\w+)", 'I love FishC.com!')
# print(result)
# print(result.group())
# print(result.group(1))
# print(result.group(2))

# import urllib.request
# import re
#
# def open_url(url):
#     req = urllib.request.Request(url)
#     req.add_header('User-Agent', 'Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.65 Safari/537.36')
#     response = urllib.request.urlopen(url)
#     html = response.read()
#     return html
#
# def get_img(url):
#     html = open_url(url).decode('utf-8')
#     p = r'<img class="BDE_Image" src="([^"]+\.jpg)"'
#     imglist = re.findall(p, html)
#
#     # for each in imglist:
#     #     print(each)
#
#     for each in imglist:
#         filename = r'C:\Users\zhangyi\Desktop\photodown\\' + each.split('/')[-1]
#         urllib.request.urlretrieve(each, filename, None)
#
# if __name__ == '__main__':
#     url = 'https://tieba.baidu.com/p/4863860271'
#     get_img(url)

# import urllib.request
# import urllib.error
#
# req = urllib.request.Request('http://www.fishc.com/ooxx.html')
# try:
#     urllib.request.urlopen(req)
#
# except ValueError as e:
#     print(e)
#
# except urllib.error.HTTPError as e:
#     print(e.code)
#     print(e.read())
#     print(e.reason)
#
# except urllib.error.URLError as e:
#     print(e.reason)

# import urllib.request
# import urllib.error
#
# req = urllib.request.Request("http://www.fishc.com/ooxx.html")
# try:
#     urllib.request.urlopen(req)
#
# except urllib.error.URLError as e:
#     if hasattr(e, 'reason'):
#         print("Reason:", e.reason)
#
#     if hasattr(e, 'code'):
#         print("Error code:" , e.code)

# import urllib.request
# from bs4 import BeautifulSoup
# import chardet
#
#
# class KPhoto():
#     def __init__(self):
#         self.headers = {}
#         self.headers['User-Agent'] = \
#             'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'
#         self.url = 'http://www.gaoxiaogif.com/tag/xieedongtai/'
#         self.html = ''
#         self.title_list = []
#         self.photo_list = []
#         self.file = r'C:\Users\zhangyi\Desktop\KPhoto\\'
#
#     def _urlOpen(self):
#         req = urllib.request.Request(self.url, headers=self.headers)
#         response = urllib.request.urlopen(req)
#         self.html = response.read()
#
#         return self.html
#
#     def _photoFind(self):
#         if chardet.detect(self.html)['encoding'] == 'GB2312' or chardet.detect(self.html)['encoding'] == 'GBK':
#             soup = self.html.decode('GBK')
#
#         else:
#             soup = self.html.decode('utf-8')
#
#         i = soup.find('class="listgif-giftu"')
#
#         print(i)
#
#     def photoDownload(self):
#         self._urlOpen()
#         self._photoFind()
#
#
# if __name__ == '__main__':
#     i = KPhoto()
#     i.photoDownload()

# import requests
# import bs4
#
# res = requests.get('https://movie.douban.com/top250')
# soup = bs4.BeautifulSoup(res.text, 'html.parser')
# targets = soup.find_all('div', class_='hd')
# for each in targets:
#     print(each.a.span.text)

# import requests
# r = requests.get("http://test.wdklian.com/index.php?app=public", auth=('user', 'pass'))
# print(r.status_code)
# print(r.headers['content-type'])
# print(r.encoding)
# print(r.text)
# print(r.json())

# import requests
#
# # payload = {'key1': 'value1', 'key2': 'value2'}
# payload = {'key1': 'value1', 'key2': ['value2', 'value3']}
# r = requests.get("http://httpbin.org/get", params=payload)
# r = requests.get("https://api.github.com/events")
# print(r.url)
# print(r.text)
# print(r.encoding)
# print(r.content)
# print(r.headers)

# import requests
# import bs4
#
# res = requests.get("https://movie.douban.com/top250")
# soup = bs4.BeautifulSoup(res.text, "html.parser")
# targets = soup.find_all("div", class_='hd')
# for each in targets:
#     print(each.a.span.text)

# import requests
# import bs4
# import re
#
#
# def open_url(url):
#     # 使用代理
#     # proxies = {"http": "127.0.0.1:1080", "https": "127.0.0.1:1080"}
#     headers = {
#         'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/57.0.2987.98 Safari/537.36'}
#
#     # res = requests.get(url, headers=headers, proxies=proxies)
#     res = requests.get(url, headers=headers)
#
#     return res
#
#
# def find_movie(res):
#     soup = bs4.BeautifulSoup(res.text, 'html.parser')
#
#     # 电影名
#     movies = []
#     targets = soup.find_all('div', class_='hd')
#     for each in targets:
#         movies.append(each.a.span.text)
#
#     # 评分
#     ranks = []
#     targets = soup.find_all("span", class_='rating_num')
#     for each in targets:
#         ranks.append("评分：%s" % each.text)
#
#     # 资料
#     message = []
#     targets = soup.find_all("div", class_='bd')
#     for each in targets:
#         try:
#             message.append(each.p.text.split('\n')[1].strip() + each.p.text.split('\n')[2].strip())
#
#         except:
#             continue
#
#     result = []
#     length = len(movies)
#     for i in range(length):
#         result.append(movies[i] + ' ' + ranks[i] + ' ' + message[i] + ' ')
#
#     return result
#
# # 找出一共有多少个页面
# def find_depth(res):
#     soup = bs4.BeautifulSoup(res.text, 'html.parser')
#     depth = soup.find("span", class_='next').previous_sibling.previous_sibling.text
#
#     return int(depth)
#
# def main():
#     host = "https://movie.douban.com/top250"
#     res = open_url(host)
#     depth = find_depth(res)
#
#     for i in range(depth):
#         url = host + '/?start=' + str(25 * i)
#         res = open_url(url)
#         print(find_movie(res))
#
# if __name__ == '__main__':
#     main()

# import requests
# import bs4
# import pprint
#
# headers = {'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}
# params = {'p': '64'}
#
# r = requests.get("https://www.bilibili.com/video/av4050443/", headers=headers, params=params)
# # print(r.url)
#
# soup = bs4.BeautifulSoup(r.text, 'html.parser')
# print(soup)
# print('************************')
# pprint.pprint(r.text)
#
# import requests
# import bs4
# from PIL import Image
# from io import BytesIO
#
# r = requests.get("http://test.wdklian.com/data/upload/2019/0708/21/5d2345ba4499c4c9d7b2_580_auto.png")
# # print(r.content)
#
# # soup = bs4.BeautifulSoup(r.text, 'html.parser')
# # print(soup)
#
# i = Image.open(BytesIO(r.content))
# print(i)
# with open(r'C:\Users\zhangyi\Desktop\photo.jpg', 'wb') as f:
#     f.write(i)
#     print("下载成功")

# import requests
#
# data = (('key1', 'value1'), ('key1', 'value2'))
# # data = {'key1': 'value1', 'key2': 'value2'}
#
# r = requests.post("http://httpbin.org/post", data=data)
# print(r.text)

# import requests
#
# jar = requests.cookies.RequestsCookieJar()
# jar.set('tasty_cookie', 'yum', domain='httpbin.org', path='/cookies')
# jar.set('gross_cookie', 'blech', domain='httpbin.org', path='/elsewhere')
# url = 'http://httpbin.org/cookies'
# r = requests.get(url, cookies=jar)
# print(r.text)

# import requests
# import bs4
# import re
# import openpyxl
#
#
# def open_url(url):
#     headers = {
#         'User-agent': "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36"}
#     res = requests.get(url, headers=headers)
#
#     return res
#
#
# def find_data(res):
#     data = []
#     soup = bs4.BeautifulSoup(res.text, 'html.parser')
#     content = soup.find(id="Cnt-Main-Article-QQ")
#     target = content.find_all("p", style='TEXT-INDENT: 2em')
#     target = iter(target)
#
#     for each in target:
#         if each.text.isnumeric():
#             data.append([
#                 re.search(r'\[(.+)\]', next(target).text).group(1),
#                 re.search(r'\d.*', next(target).text).group(),
#                 re.search(r'\d.*', next(target).text).group(),
#                 re.search(r'\d.*', next(target).text).group()
#             ])
#
#     return data
#
# def to_excel(data):
#     wb = openpyxl.Workbook()
#     wb.guess_types = True
#     ws = wb.active
#     ws.append(['城市', '平均房价', '平均工资', '房价工资比'])
#     for each in data:
#         ws.append(each)
#
#     wb.save(r'C:\Users\zhangyi\Desktop\2017年中国主要城市房价工资比排行榜.xlsx')
#
#
# def main():
#     url = 'https://news.house.qq.com/a/20170702/003985.htm'
#     res = open_url(url)
#     data = find_data(res)
#     to_excel(data)
#
#
# if __name__ == '__main__':
#     main()

# import requests
# import bs4
# import re
#
# class tts():
#     def __init__(self):
#         self.headers = {'User-agent' : "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36"}
#         self.url = r'http://huaban.com/favorite/anime/'
#         self.res = ''
#
#
#     def _openUrl(self):
#         self.res = requests.get(self.url, headers=self.headers)
#         print(self.res.text)
#
#     def _getMassage(self):
#         soup = bs4.BeautifulSoup(self.res.text, 'html.parser')
#         massage = soup.find(id='waterfall')
#
#         print(massage)
#
#     def main(self):
#         self._openUrl()
#         self._getMassage()
#
# if __name__ == '__main__':
#     t = tts()
#     t.main()



# from appium import webdriver
# from selenium.common.exceptions import NoSuchElementException
#
#
# desired_caps = {}
# desired_caps['platformName'] = "Android"    # 安卓
# desired_caps["platformVersion"] = '5.1.1'   # 型号
# desired_caps['deviceName'] = '127.0.0.1:62001'  # 设备连接号
#
# # desired_caps['app'] = r'C:\Users\zhangyi\Desktop\Android\医生端\wdkl.manager.v1.0.14.apk'  # 安装APP
# desired_caps['appPackage'] = 'doctor.wdklian.com'   # APP的包名
# desired_caps['appActivity'] = 'doctor.wdklian.com.ui.activity.SplashActivity'   # APP的Activity
# desired_caps['noReset'] = 'True'    # 测试覆盖开关按钮
#
# # 开启中文输入
# desired_caps['unicodeKeyboard'] = 'True'
# desired_caps['resetKeyboard'] = 'True'
#
# # 开启验证Toast信息
# desired_caps['automationName'] = 'uiautomator2'
#
#
# driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps) # 连接Appium服务器
# driver.implicitly_wait(5)
#
# # 使用xpath定位我的页面
# print('定位我的页面')
# driver.find_element_by_id('doctor.wdklian.com:id/id_person').click()
# driver.find_element_by_id('doctor.wdklian.com:id/tv_message').click()
#
# # 点击进入个人信息界面
# print('进入个人信息界面')
# driver.find_element_by_id('doctor.wdklian.com:id/rl_sex').click()
# driver.find_element_by_id('doctor.wdklian.com:id/btnCancel').click()
#
# # 修改用户名
# print('修改用户名')
# try:
#     driver.find_element_by_id('doctor.wdklian.com:id/tv_name').click()
#     driver.find_element_by_id('doctor.wdklian.com:id/tv_name').clear()
#     driver.find_element_by_id('doctor.wdklian.com:id/tv_name').send_keys('测试自动化')
#     driver.find_element_by_id('doctor.wdklian.com:id/tv_right').click()
#     driver.save_screenshot(r'C:\Users\zhangyi\Desktop\change.png')
#
# except NoSuchElementException:
#     driver.save_screenshot(r'C:\Users\zhangyi\Desktop\change.png')
#     print('出bug了')
# else:
#     print('修改完成')



# import yaml
#
# file = open('test.yaml', 'r', encoding='UTF-8')
# data = yaml.load(file)
#
# # print(data)
# #
# # print(data['name'])
# # print(data['age'])
# #
# # print(data['attribute'])
# # print(data['attribute']['clothes'])
# # print(data['attribute']['petPhrase'])
# #
# # print(data['ability'])
# # print(data['ability'][0]['a'])
# # print(data['ability'][0]['b'])
# # print(data['ability'][1]['a'])
# # print(data['ability'][1]['b'])
#
# slogan = ['welcome', 'to', '51zxw']
# website = {'url': 'www.51zxw.net'}
#
# # python data
# print(slogan)
# print(website)
#
# # yaml data
# print(yaml.dump(slogan))
# print(yaml.dump(website))


# from PIL import Image
# import pytesseract
#
# text = pytesseract.image_to_string(Image.open(r'D:\Python3\code\appium_advance\yanzhengma\yanzhengma01.png'))
# print(text)


# import unittest
#
# class Math:
#     def __init__(self, a, b):
#         self.a = int(a)
#         self.b = int(b)
#
#     def add(self):
#         return self.a + self.b
#
# class TestStarEnd(unittest.TestCase):
#     @classmethod
#     def setUpClass(cls):
#         print("用例开始之前")
#
#     @classmethod
#     def tearDownClass(cls):
#         print("用例结束之后")
#
#     def setUp(self):
#         print('test start')
#
#     def tearDown(self):
#         print('test end')
#
#
# class TestMath(TestStarEnd):
#
#
#     def test_add(self):
#         j = Math(5, 10)
#         self.assertEqual(j.add(), 15)
#         # self.assertEqual(j.add(), 12)
#
#     def test_add2(self):
#         j = Math(5, 10)
#         # self.assertNotEqual(j.add(), 15)
#         self.assertNotEqual(j.add(), 12)
#
#     @unittest.skip("跳过test_add3")
#     def test_add3(self):
#         j = Math(5, 10)
#         # self.assertTrue(j.add() > 10)
#         self.assertFalse(j.add() > 10)
#
#     @unittest.expectedFailure
#     def test_add4(self):
#         # self.assertIn('I', "I love You")
#         self.assertNotIn('I', "I love You")
#
#     def test_add5(self):
#         self.assertIs("I", "I")
#
#
#
#
#
# if __name__ == '__main__':
#     # suite = unittest.TestSuite()
#     # suite.addTest(TestMath('test_add'))
#     # suite.addTest(TestMath('test_add2'))
#     # suite.addTest(TestMath('test_add3'))
#     # suite.addTest(TestMath('test_add4'))
#     # suite.addTest(TestMath('test_add5'))
#     #
#     # runer = unittest.TextTestRunner()
#     # runer.run(suite)
#
#     unittest.main()
#
# class Student():
#     name = ""
#     age  = 0
#
#     def study(self):
#         self.name = '小黑'
#         print(self.name + '正在学习')
#
#
#
# class TestStudent():
#     s = Student()
#     s.name = "张三丰"
#     s.age  = 141
#     s.study()
#
#     def showAge(self):
#         s.name = "666"
#         print("学生" + self.s.name + "的年龄是" + str(self.s.age))
#
# s = TestStudent()
# s.showAge()
#
# class TestStudent2(Student):
#     name = "张思"
#     age  = 14
#
#     def showAge(self):
#         self.name = '账务'
#         print("学生" + self.name + "的年龄是" + str(self.age))
#
# s2 = TestStudent2()
# s2.study()
# s2.showAge()
#
#
#
# a = 'asdasdasda'
# print(a[2:])
#
# import tkinter as tk
#
# app = tk.Tk()
# app.title("FishC Demo")
#
# app2 = tk.Label(app, text='我的第二个窗口程序！')
# app2.pack()
#
# app.mainloop()

# import tkinter as tk
#
# class APP():
#
#     def __init__(self, master):
#         frame = tk.Frame(master)
#         frame.pack(side=tk.LEFT, padx=10, pady=10)
#
#         self.hi_there = tk.Button(frame, text='打招呼',bg='black', fg='blue', command=self.say_hi)
#         self.hi_there.pack()
#
#     def say_hi(self):
#         print('互联网的广大朋友们大家好！')
#
# root = tk.Tk()
# app = APP(root)
#
# root.mainloop()
#
# from tkinter import *
#
# root = Tk()
#
# textLabel = Label(root, text='外加\n图片',
#                   justify=LEFT,
#                   padx=10)
# textLabel.pack(side=LEFT)
#
# photo = PhotoImage(file=r'C:\Users\zhangyi\Desktop\QQ图片20190912143625.png')
# imgLabel = Label(root, image=photo)
# imgLabel.pack(side=RIGHT)
#
# mainloop()

# from tkinter import *
#
# def callback():
#     var.set("啊呸")
#
#
# root = Tk()
#
# frame1 = Frame(root)
# frame2 = Frame(root)
#
# var = StringVar()
# var.set('不知道\n不太喜欢')
# photo = PhotoImage(file=r'C:\Users\zhangyi\Desktop\QQ图片20190912143625.png')
# theLabel = Label(frame1,
#                  textvariable=var,
#                  justify=LEFT,
#                  image=photo,
#                  compound=CENTER,
#                  font=('宋体', 20),
#                  fg='blue')
#
# theLabel.pack()
#
#
# theButton = Button(frame2,
#                    text='乖乖',
#                    command=callback)
# theButton.pack()
#
# frame1.pack(padx=10, pady=10)
# frame2.pack(padx=10, pady=10)
#
#
# mainloop()

# from tkinter import *
#
# root =Tk()
#
# v = IntVar()
#
# c = Checkbutton(root, text='测试一下', variable=v)
# c.pack()
#
# l = Label(root, textvariable=v)
# l.pack()
#
# mainloop()

#
# from tkinter import *
#
# root = Tk()
#
# Girls = [1, 2, 3, 4, 5]
#
# v = []
#
# for girl in Girls:
#     v.append(IntVar())
#     b = Checkbutton(root, text=girl, variable=v[-1])
#     b.pack(anchor=W)
#
# mainloop()

# from tkinter import *
#
# root = Tk()
#
# v = IntVar()
#
# Radiobutton(root, text='One', variable=v, value=1).pack(anchor=W)
# Radiobutton(root, text='Twe', variable=v, value=2).pack(anchor=W)
# Radiobutton(root, text='Three', variable=v, value=3).pack(anchor=W)
#
# mainloop()

# from  tkinter import *
#
# root = Tk()
#
# group = LabelFrame(root, text='脚本语言', padx=5, pady=5)
# group.pack(padx=10, pady=10)
#
# Langs = [
#     ('Python', 1),
#     ('Perl', 2),
#     ('Ruby', 3),
#     ('Lua', 4)
# ]
#
# v = IntVar()
# v.set(1)
#
# for lang, num in Langs:
#     b = Radiobutton(group, text=lang, variable=v, value=num)
#     b.pack(fill=X)
#
# mainloop()

# import os
# a = os.path.abspath(__file__)
# print(a)
# b = os.path.dirname(__file__)
# print(b)
# c = os.path.dirname(os.path.abspath(__file__))
# print(c)
# d = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
# print(d)


# import logging
#
# DATEFMT = "[%Y-%m-%d %H:%M:%S]"
# FORMAT = "%(asctime)s %(thread)d %(message)s"
# logging.basicConfig(level=logging.INFO, format=FORMAT, datefmt=DATEFMT, filename='class_test.log')
#
# root = logging.getLogger()
# print(root.name, type(root), root.parent, id(root))
#
# logger = logging.getLogger(__name__)
# print(logger.name, type(logger), id(logger), id((logger.parent)))
#
# logger1 = logging.getLogger(__name__ + ".ok")
# print(logger1.name, type(logger1), id(logger1), id((logger1.parent)))
#
# print(logger1.parent, id(logger1.parent))


# import uuid
#
# uuid = uuid.uuid4()
# print(uuid)
#
#
# from collections import Counter
#
# def url(asd, *args, **kwargs):
#
#     # b = Counter(asd)
#     # print(dict(b))
#     # print(args)
#     # print(kwargs)
#     # print(kwargs['data'])
#     #
#     # for i in range(b['{']):
#     #     print(args[i])
#     #
#     #     print(asd.format(args[i]))
#
#     c = []
#     d = []
#     print(kwargs)
    # k = kwargs['data'].keys()
    # print(k)
    # for i in k:
    #     c.append(i)
    # v = kwargs['data'].values()
    # print(v)
    # for i in v:
    #     d.append(i)
    #
    # asd = asd + '?'
    # for i in range(len(kwargs['data'])):
    #     print(i)
    #     asd += (c[i] + '=' + c[i] + '&')
    #
    #
    # print(asd)


    # c = []
    #
    # for i in range(len(b)):
    #     if b[i] == '{}':
    #         c.append(b[i])
    #
    #
    #
    # print(asd.format(*args))

#
# data = {
#     'baidu' : 'baidu',
#     'bilibili' : 'bilibili',
#     'youku' : 'youku'
# }
#
# data2 = {
#     'baidu' : 'baidu'
# }
#
# data3 = ('baidu', 'bilibili')
# print(data3[0])
#
# data4 = 'baidu'
# data5 = 'bilibili'
# asd = 'http://www.{}.com'
# u = url(asd, data4)



# suffix = '/goods/{}/area/{}'
#
# a = 1, 2
# b = [1, 2]
# print(a)
# print(suffix.format(b[0], b[1]))


# import requests, time, json, csv
#
# def write_file(item):
#     with open("D://lagou", "a+", encoding="utf-8") as f:
#         file = csv.writer(f)
#         try:
#             file.writerow(item)
#         except:
#             print("-----------------出错了")
#
# def main():
#     start_url = "https://www.lagou.com/jobs/list_%E8%87%AA%E5%8A%A8%E5%8C%96?labelWords=&fromSearch=true&suginput="
#     headers = {
#     "User-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 Safari/537.36",
#     "Accept": "application/json, text/javascript, */*; q=0.01",
#     "Referer": "https://www.lagou.com/jobs/list_%E8%87%AA%E5%8A%A8%E5%8C%96?labelWords=&fromSearch=true&suginput="
#     }
#     url = 'https://www.lagou.com/jobs/positionAjax.json?city=杭州&needAddtionalResult=false'
#     list = []
#     for j in range(20):
#         data = {
#             "first": "false",
#             "pn": str(j),
#             "kd": "软件测试工程师"
# }
#         s = requests.Session()
#         s.get(start_url, headers=headers, timeout=3)
#         cookie = s.cookies
#
#         res = s.post(url, data=data, headers=headers, timeout=3)
#         time.sleep(6)
#         res.encoding = res.apparent_encoding
#         text = json.loads(res.text)   #解析成dict
#         print(text)
#         info = text['content']['positionResult']['result']
#         for i in info:
#             city = i['city']
#             companyFullName = i['companyFullName']
#             positionName = i['positionName']
#             salary = i['salary']
#             workYear = i['workYear']
#             companySize = i['companySize']
#             education = i['education']
#             linestaion = i['linestaion']
#             positionAdvantage = i['positionAdvantage']
#             industryField = i['industryField']
#             companyLabelList = i['companyLabelList']
#             district = i['district']
#             createTime = i['createTime']
#             financeStage = i['financeStage']
#             list = [city, companyFullName, positionName, salary, workYear, companySize,district, education,linestaion, positionAdvantage,
#                     industryField, companyLabelList, financeStage,createTime]
#             print(list)
#             # write_file(list)
#
# if __name__ == '__main__':
#     main()


# import requests
# base_url = 'http://httpbin.org'
#
# form_data = {'uname':'Test00002','pwd':'123456'}
# # 发送POST请求，格式如：requests.post(url,data)
# r = requests.post(base_url+'/post',data=form_data)
# print(r.text)

# 导入requests库
# import requests
#
# # 定义base_url作为基础被测URL
# base_url = 'http://httpbin.org'
#
# # 定义请求所需的参数，参数之间以英文逗号隔开
# param_data = {'uname':'Test00001','pwd':'123456'}
# # 发送GET请求，格式如：requests.get(url,params)
# r = requests.get(base_url+'/get',params=param_data)
# print(r.url)    # 输出请求的url
# print(r.status_code)    #输出响应的状态码


# dict = {
#         'baidu': 'baidu',
#         'bilibili': 'bilibili',
#         'youku': 'youku'
# }
#
#
# for i in dict:
#     print(i)


# import json, time, random, uuid
# import requests
# import hashlib
#
# s = requests.session()
#
# up = {
#     'username' : '13412345678',
#     'password' : 'e10adc3949ba59abbe56e057f20f883e'
# }
# username = '16312345678'
# password = '123456'
#
# h = hashlib.md5()
# h.update(password.encode('utf-8'))
# p = str(h.hexdigest())
#
# login_url = r'http://dev.buyer.wdklian.com/passport/login/noCaptcha?username=%s&password=%s' % (username, p)
# # login_url = r'http://dev.seller.wdklian.com/passport/login/noCaptcha?username=%s&password=%s' % (username, p)
# # login_url = r'http://dev.buyer.wdklian.com/passport/login/noCaptcha?username=13412345678&password=e10adc3949ba59abbe56e057f20f883e'
# # login_url = r'http://dev.buyer.wdklian.com/passport/login/noCaptcha'
#
# # response = requests.get(login_url, params=up)
# response = s.get(login_url)
# print(response)
# print(response.text)
#
#
# js = json.loads(response.text)
#
# uid = str(js['uid'])
# token = str(js['access_token'])
# timestamp = str(int(time.time() * 1000))
# nonce = str(random.randint(100000,999999))
# sign1 = uid + nonce + timestamp + token
# sign = hashlib.md5((uid + nonce + timestamp + token).encode("utf-8")).hexdigest()
# uuid = str(uuid.uuid4())
#
# headers = {
#     'Authorization' : token,
#     'uuid' : uuid
# }
#
# # url = "http://httpbin.org/get"
# # url = "http://httpbin.org/post"
# url = 'http://dev.buyer.wdklian.com/goods/345/area/123129'
# # url = 'http://dev.buyer.wdklian.com/trade/carts/o2o/all'
# # url = 'http://dev.buyer.wdklian.com/passport/trade/carts/o2o'
# # url = 'http://dev.buyer.wdklian.com/care/health_advert/page'
# # url = 'http://dev.buyer.wdklian.com/care//care/health_advert/22'
# url += "?uid="+ uid + "&timestamp=" + timestamp + "&nonce=" + nonce + "&sign=" + sign
#
# must_data = {
#     'uid'       : uid,
#     'timestamp' : timestamp,
#     'nonce'     : nonce,
#     'sign'      : sign
# }
#
# # data = {
# #     'sku_id': '495',
# #     'num': '1'
# # }
#
# data = {
#     'page_no' : '1',
#     'page_size' : '10'
# }
#
# # r = s.post(url, data=data, headers=headers)
# # r = s.post(url, data=must_data, headers=headers)
# # r = s.get(url, params=must_data, headers=headers)
# r = s.get(url, headers=headers)
# print(r)
# print('响应正文：', r.text)
# print('响应头：', r.headers)
# print('响应url：', r.url)
# print('响应对应请求方式：', r.request)


# region = {
#     'province_id': '18',
#     'province': '湖南',
#
#     'city_id': '1482',
#     'city': '长沙市',
#
#     'county_id': '48941',
#     'county': '浏阳市',
#
#     'town_id': '52588',
#     'town': '城区',
# }
#
# url=''
#
# keys_list = []
# valuse_list = []
#
#
# print(region.keys())
# print(region.values())
#
# for i in region.keys():
#     keys_list.append(i)
# print(keys_list)
#
# for i in region.values():
#     valuse_list.append(i)
# print(valuse_list)
#
#
# for i in range(len(region)):
#     url += '&' + keys_list[i] + '=' + valuse_list[i]
# print(url)



# a = '123{0}912{1}431'
#
# b = 'asd'
#
# c = 'dfgd'
#
# d = [b, c]
#
# print(d)
#
#
#
# for i in range(len(b)):
#     pass
#
# a = a.format(*d)
# print(a)
#
# del_data = {
#     'a' : 1
# }
#
# import requests
# r = requests.delete('http://httpbin.org/delete', params=del_data)                                    # DELETE请求
# print(r)
# print(r.text)




# import tkinter as tk
#
# app = tk.Tk()
# app.title('FishC Demo')
#
# v = tk.StringVar()
#
# longtext = '''
# 我的第二个窗口程序！
# 换行
# '''
#
# text = '''
# longtext
# '''
#
# theLabel = tk.Label(
#     app,
#     # text=longtext,
#     textvariable=v,
#     font=('微软雅黑', 20),
#     fg='green',
#     anchor='w',
#     justify='left'
# )
#
# v.set(longtext)
# v.set(text)
#
# theLabel.pack()
#
# app.mainloop()

#
# import tkinter as tk
#
# class APP:
#     def __init__(self, master):
#         frame = tk.Frame(master)
#         frame.pack(side=tk.LEFT, padx=10, pady=10)
#
#         self.hi_there = tk.Button(frame,
#                                   text='打招呼',
#                                   bg='black',
#                                   fg='blue',
#                                   command=self.say_hi)
#         self.hi_there.pack()
#
#
#     def say_hi(self):
#         print('互联网的广大朋友大家好，我是小甲鱼！')
#
#
# root = tk.Tk()
# app = APP(root)
#
# root.mainloop()


# import tkinter as tk
#
# class APP():
#
#     def __init__(self, master, photo):
#         label = tk.Label(master,
#                          image=photo,
#
#                          )
#         label.pack()
#
#
# root = tk.Tk()
# root.title('tkinter的图片！！！')
#
# photo = tk.PhotoImage(file=r'C:\Users\zhangyi\Desktop\QQ图片20191119104244.png')
#
# app = APP(root, photo)
#
# root.mainloop()

# from tkinter import *
#
# root = Tk()
#
# photo = PhotoImage(file=r'C:\Users\zhangyi\Desktop\QQ图片20191119104244.png')
# textLabel = Label(root,
#                   text='你好！',
#                   image=photo,
#                   compound=CENTER,
#                   font=('微软雅黑', 20),
#                   fg='blue'
#                   )
# textLabel.pack()
#
# #
# # imageLabel = Label(root, image=photo)
# # imageLabel.pack()
#
# root.mainloop()



# from tkinter import *
#
# def callback():
#     var.set('关我屁事！')
#
#
# root = Tk()
# root.geometry('400x300')
#
# frame1 = Frame(root)
# frame2 = Frame(root)
#
# var = StringVar()
# var.set('你好！')
#
# photo = PhotoImage(file=r'C:\Users\zhangyi\Desktop\QQ图片20191119104244.png')
#
# textLabel = Label(frame1,
#                   textvariable=var,
#                   # image=photo,
#                   compound=CENTER,
#                   font=('微软雅黑', 20),
#                   fg='blue'
#                   )
# textLabel.pack()
#
#
# theButton = Button(frame2, text='我不好！', command=callback, bg='red', fg='blue')
# theButton.pack(side=LEFT, expand=YES, fill=Y)
#
# frame1.pack()
# frame2.pack(side=LEFT, expand=YES, fill=BOTH)
#
# root.mainloop()


# from tkinter import *
#
# root = Tk()
#
# v = IntVar()
# print(v)
#
# c = Checkbutton(root, text='测试一下', variable=v)
# c.pack()
#
# l = Label(root, textvariable=v)
# l.pack()
#
# root.mainloop()


# from tkinter import *
#
# root = Tk()
#
# group = LabelFrame(root, text='客官，炼铜吗！！！', padx=10, pady=10)
# group.pack(padx=10, pady=10)
#
#
# Girls = ['略略酱', '小白菜', '依文酱', '萌月月', '小水银']
#
# v = []
#
# for girl in Girls:
#     v.append(IntVar())
#     c = Checkbutton(group, text=girl, variable=v[-1],
#                     font=('微软雅黑', 20),
#                     fg='red')
#     c.pack(anchor=W,
#            )
#
#
# root.mainloop()


# def test(*args, **kwargs):
#     return args, kwargs
#
# a = ['nihao', 'buhao']
#
# b = {
#     'nihao' : 1,
#     'buhao' : 2
# }
#
# t = test(a)
# print(t)
#
# t2 = test(b)
# print(t2)
#
# t3 = test(a, b)
# print(t3)



# from tkinter import *
#
# root = Tk()
#
# e = Entry(root)
# e.pack(padx=20, pady=20)
#
#
# e.delete(0, END)
# e.insert(0, '默认文本...')
#
# mainloop()



# from tkinter import *
#
# root = Tk()
#
# f1 = Frame(root)
# f2 = Frame(root)
# f3 = Frame(root)
#
# l1 = Label(f1, text='作品：', font=('微软雅黑', 15))
# l1.pack(side='left', padx=50)
# e1 = Entry(f1)
# e1.pack(side='right', padx=20, fill='x')
#
# l2 = Label(f2, text='作者：', font=('微软雅黑', 15))
# l2.pack(side='left', padx=50)
# e2 = Entry(f2)
# e2.pack(side='right', padx=20, fill='x')
#
#
# b1 = Button(f3, text='获取信息', font=('微软雅黑', 15))
# b1.pack(side='left', padx=50, pady=5)
# b2 = Button(f3, text='退出', font=('微软雅黑', 15))
# b2.pack(side='right', padx=50, pady=5)
#
#
# f1.pack()
# f2.pack()
# f3.pack()


# root.mainloop()


# from tkinter import *
#
# root = Tk()
#
# Label(root, text='账号：').grid(row=0, column=0)
# Label(root, text='密码：').grid(row=1, column=0)
#
# v1 = StringVar()
# v2 = StringVar()
#
# e1 = Entry(root, textvariable=v1)
# e2 = Entry(root, textvariable=v2, show='*')
# e1.grid(row=0, column=1, padx=10, pady=5)
# e2.grid(row=1, column=1, padx=10, pady=5)
#
# def show():
#     print('账号：%s' % e1.get())
#     print('密码：%s' % e2.get())
#
# Button(root, text='芝麻开门', width=10, command=show) \
#     .grid(row=3, column=0, sticky=W, padx=10, pady=5)
# Button(root, text='退出', width=10, command=root.quit) \
#     .grid(row=3, column=1, sticky=E, padx=10, pady=5)
#
#
# mainloop()


# from tkinter import *
#
# master = Tk()
#
# def test():
#     if e1.get() == 'nihao':
#         print('zhengque')
#         return True
#
#     else:
#         print('cuowu')
#         return False

# def test(content):
#     return content.isdigit()
#
# frame = Frame(master)
# frame.pack(padx=10, pady=10)
#
# v1 = StringVar()
# v2 = StringVar()
# v3 = StringVar()
#
# testCMD = master.register(test)
# e1 = Entry(frame, width=10, textvariable=v1, validate='key', validatecommand=(testCMD, '%P')).grid(row=0, column=0)
#
# Label(frame, text='+').grid(row=0, column=1)
#
# e2 = Entry(frame, width=10, textvariable=v2, validate='key', validatecommand=(testCMD, '%P')).grid(row=0, column=2)
#
# Label(frame, text='=').grid(row=0, column=3)
#
# e3 = Entry(frame, width=10, textvariable=v3, state='readonly').grid(row=0, column=4)
#
# def calc():
#     result = int(v1.get()) + int(v2.get())
#     v3.set(str(result))
#
# Button(frame, text='计算结果', command=calc).grid(row=1, column=2, pady=5)
#
#
# mainloop()



# from tkinter import *
#
# master = Tk()
#
# e = Entry(master)
# e.pack(padx=20, pady=20)
#
# e.delete(0, 'end')
# e.insert(0, '1默认文本...')
# e.delete(1, 'end')
# e.insert(3, '2默认文本...')
# print(e.get())
#
# master.mainloop()


# from tkinter import *
#
# master = Tk()
#
# s = StringVar()
# e = Entry(master, textvariable=s)
# e.pack()
#
# s.set('不知道')
#
# mainloop()


# from tkinter import *
#
# master = Tk()
# master.title('tkinter')
#
# Label(master, text='作品：').grid(row=0, column=0)
# Label(master, text='作者：').grid(row=1, column=0)
#
# e1 = Entry(master)
# e2 = Entry(master)
# e1.grid(row=0, column=1, padx=10, pady=5)
# e2.grid(row=1, column=1, padx=10, pady=5)
#
# def show():
#     print("作品：《%s》" % e1.get())
#     print("作者：%s" % e2.get())
#     e1.delete(0, 'end')
#     e2.delete(0, 'end')
#
# Button(master, text='获取信息', width=0, command=show).grid(row=3, column=0, sticky='w', padx=10, pady=5)
# Button(master, text='退出', width=0, command=master.quit).grid(row=3, column=1, sticky='e', padx=10, pady=5)
#
# mainloop()


# from tkinter import *
#
# master = Tk()
#
# def test(content, reson, name):
#     if e1.get() == 'CDSN':
#         print('zhengque', content, reson, name)
#         return True
#
#     else:
#         print('cuowu', content, reson, name)
#         return False
#
#
# def test2():
#     print('wo')
#     return True
#
#
# testCMD = master.register(test)
#
# v = StringVar()
# e1 = Entry(master, textvariable=v, validate='focusout', validatecommand=(testCMD, '%P', '%v', '%W'), invalidcommand=test2)
# e2 = Entry(master)
#
# e1.pack(padx=10, pady=10)
# e2.pack(padx=10, pady=10)
#
# mainloop()


# from tkinter import *
#
# master = Tk()
#
#
# def makesure():
#     if e1.get() == '小王':
#         print('哈喽，恭喜恭喜！')
#         return True
#     else:
#         print('我晕，你是谁？！')
#         e1.delete(0, END)  # 输入错误时，删除错误文本
#         return False
#
#
# def sb():
#     print('sb!')
#
#
# e1 = Entry(master, validate='focusout',
#            validatecommand=makesure, invalidcommand=sb)
# e1.pack(padx=10, pady=10)
#
# e2 = Entry(master, show='*')
# e2.pack(padx=10, pady=10)
#
# mainloop()


# from tkinter import *
#
# master = Tk()
#
# sb = Scrollbar(master)
# sb.pack(side=RIGHT, fill=Y)
#
# theLB = Listbox(master, yscrollcommand=sb.set)
#
# for item in range(100):
#     theLB.insert(END, item)
# theLB.pack(side=LEFT, fill=BOTH)
# sb.config(command=theLB.yview)
#
# theButton = Button(master, text='删除它',
#                    command=lambda x = theLB : x.delete(ACTIVE))
# theButton.pack()
#
#
# mainloop()


# from tkinter import *
#
# root = Tk()
#
# s1 = Scale(root, from_=0, to=42, tickinterval=5, resolutio=5, length=200)
# s1.pack()
# s2 = Scale(root, from_=0, to=200, orient=HORIZONTAL, length=600)
# s2.pack()
#
#
# def show():
#     print(s1.get(), s2.get())
#
# Button(root, text='获取位置', command=show).pack()
#
# mainloop()


# from tkinter import *
#
# master = Tk()
#
# f1 = Frame()
# f2 = Frame()
#
# sb = Scrollbar(f1)
# sb.pack(side='right', fill='y')
#
# theLB = Listbox(f1, selectmode='multiple', yscrollcommand=sb.set)
# theLB.pack()
#
#
# for i in range(100):
#     theLB.insert('end', i)
# sb.config(command=theLB.yview)
#
# theButton = Button(f2, text='删除',
#                    command = lambda x = theLB : x.delete('active'))
# theButton.pack()
#
#
# f1.pack()
# f2.pack()
#
# mainloop()


# from tkinter import *
#
# root = Tk()
#
# Scale(root, from_=52, to=100, tickinterval=5, resolution=5, length=200).pack()
# Scale(root, from_=200, to=500, tickinterval=10, length=1200, orient='horizontal').pack()
#
# mainloop()


# from tkinter import *
#
# root = Tk()
#
# Label(root, text='用户名').grid(row=0, stick='w')
# Label(root, text='密码').grid(row=1, stick='w')
#
# Entry(root).grid(row=0, column=1)
# Entry(root, show='*').grid(row=0, column=1)
#
# photo = PhotoImage(file=r'C:\Users\zhangyi\Desktop\QQ图片20191218154536.png')
# Label(root, image=photo).grid(row=0, column=2, rowspan=3, padx=5, pady=5)
#
# Button(text='提交', width=10).grid(row=2, columnspan=3, pady=5)
#
# mainloop()


# from tkinter import *
#
# root = Tk()
#
# text = Text(root, width=200, height=50)
# text.pack()
#
# # text.insert(INSERT, 'I love \n fishC \n.com!')
#
# photo = PhotoImage(file=r'C:\Users\zhangyi\Desktop\QQ图片20191218154536.png')
#
# def show():
#     text.image_create(END, image=photo)
#
# b1 = Button(text, text='点我点我', command=show)
# text.window_create(INSERT, window=b1)
#
# mainloop()


# from tkinter import *
#
# root = Tk()
#
# text = Text(root, width=30, heigh=2)
# text.pack()
#
# text.insert('insert', 'I love \n')
# text.insert('end', 'FishC.com')
#
# mainloop()


# from tkinter import *
#
# root = Tk()
#
# text = Text(root, width=50, height=10)
# text.pack()
#
# text.insert(INSERT, 'I love FishC.com!')
#
# text.tag_add('tag1', '1.7', '1.12', '1.14')
# text.tag_add('tag2', '1.13', '1.16')
# text.tag_config('tag1', background='yellow', foreground='red')
# text.tag_config('tag2', background='blue', foreground='green')
#
# text.tag_lower('tag2')
#
# mainloop()


# from tkinter import *
# import webbrowser
#
# root = Tk()
#
# text = Text(root, width=40, height=5)
# text.pack()
#
# text.insert('insert', 'I love Python.com!')
#
# text.tag_add('link', '1.7', '1.17')
# text.tag_config('link', foreground='blue', underline=True)
#
# def show_arrow_cursor(event):
#     text.config(cursor='arrow')
#
# def show_xterm_cursor(event):
#     text.config(cursor='xterm')
#
# def click(event):
#     webbrowser.open("https://www.python.org/")
#
#
# text.tag_bind('link', '<Enter>', show_arrow_cursor)
# text.tag_bind('link', '<Leave>', show_xterm_cursor)
# text.tag_bind('link', '<Button-1>', click)
#
# mainloop()


# from tkinter import *
# import hashlib
#
# root = Tk()
#
# text = Text(root, width=30, height=5)
# text.pack()
#
# text.insert(INSERT, "I love FishC.com!")
# contents = text.get('1.0', END)
#
# def getSig(contents):
#     m = hashlib.md5(contents.encode())
#     return m.digest()
#
# sig = getSig(contents)
#
# def check():
#     contents = text.get(1.0, END)
#     if sig != getSig(contents):
#         print('警报：内容发生变动！')
#     else:
#         print('风平浪静~')
#
#
#
# Button(root, text='检查', command=check).pack()

# mainloop()


# from tkinter import *
#
# root = Tk()
#
# text = Text(root, width=30, height=5)
# text.pack()
#
# text.insert(INSERT, 'I love FishC.com!')
#
# start = '1.0'
#
# def getIndex(text, index):
#     return tuple(map(int, str.split(text.index(index), '.')))
#
# while True:
#     pos = text.search('o', start, stopindex=END)
#     if not pos:
#         break
#     print('找到啦，位置是：', getIndex(text, pos))
#     start = pos + '+1c'
#
# mainloop()


# from tkinter import *
#
# root = Tk()
#
# text = Text(root, width=30, height=5, undo=True, autoseparators=False)
# text.pack()
#
# text.insert(INSERT, 'I love FishC.com!')
#
# def callback(event):
#     text.edit_separator()
#
#
# text.bind('<Key>', callback)
#
# def show():
#     text.edit_undo()
#
# Button(root, text='撤销', command=show).pack()
#
# mainloop()


#
# from tkinter import *
#
# root = Tk()
#
# w = Canvas(root, width=200, height=100)
# w.pack()
#
# line1 = w.create_line(0, 50, 200, 50, fill='yellow')
# line2 = w.create_line(100, 0, 100, 100, fill='red', dash=(4, 4))
# rect1 = w.create_rectangle(50, 25, 150, 75, fill='blue')
#
# w.coords(line1, 0, 25, 200, 25)
# w.itemconfig(rect1, fill='green')
# w.delete(line2)
#
# Button(root, text='删除全部', command=(lambda  x = ALL : w.delete((x)))).pack()
#
# mainloop()


# from tkinter import *
#
# root = Tk()
#
# w = Canvas(root, width=200, height=100)
# w.pack()
#
# w.create_line(0, 0, 200, 100, fill='green', width=3)
# w.create_line(200, 0, 0, 100, fill='green', width=3)
# w.create_rectangle(40, 20, 160, 80, fill='green')
# w.create_rectangle(65, 35, 135, 65, fill='yellow')
#
# w.create_text(100, 50, text='FishC')
#
#
# mainloop()


# from tkinter import *
#
# root = Tk()
#
# w = Canvas(root, width=200, height=100)
# w.pack()
#
# w.create_rectangle(40, 20, 160, 80, dash=(4, 4))
# w.create_oval(70, 20, 130, 80, fill='pink')
# w.create_text(100, 50, text='FishC')
#
# mainloop()


# from tkinter import *
#
# root = Tk()
#
# w = Canvas(root, width=200, height=100, background='white')
# w.pack()
#
# line1 = w.create_line(0, 50, 200, 50, fill='yellow')
# line2 = w.create_line(100, 0, 100, 100, fill='red', dash=(4, 4))
# rect1 = w.create_rectangle(50, 25, 150, 75, fill='blue')
#
#
# w.coords(line1, 0, 25, 200, 25)
# w.itemconfig(rect1, fill='green')
# w.delete(line2)
#
# Button(root, text='删除全部', command=(lambda x = ALL : w.delete(x))).pack()
#
# mainloop()



# from tkinter import *
#
# root = Tk()
#
# w = Canvas(root, width=400, height=200)
# w.pack()
#
# def paint(event):
#     x1, y1 = (event.x - 1), (event.y - 1)
#     x2, y2 = (event.x + 1), (event.y + 1)
#     w.create_oval(x1, y1, x2, y2, fill='red')
#
# w.bind('<B1-Motion>', paint)
#
# Label(root, text='按住鼠标左键并移动，开始绘制你的理想蓝图吧......').pack(side=BOTTOM)
#
# mainloop()


# from tkinter import *
#
# root = Tk()
#
# def callback():
#     print('hello')
#
# menubar = Menu(root, tearoff=False)
#
# filemenu = Menu(menubar, tearoff=False)
# filemenu.add_command(label='hello', command=callback)
# filemenu.add_command(label='quit', command=root.quit)
# filemenu.add_separator()
# filemenu.add_command(label='no', command=callback)
# menubar.add_cascade(label='wenjian', menu=filemenu)
#
#
# frame = Frame(root, width=512, height=512)
# frame.pack()
#
#
# menubar.add_command(label='hello', command=callback)
# menubar.add_command(label='quit', command=root.quit)
#
# def popup(event):
#     menubar.post(event.x_root, event.y_root)
#
# frame.bind('<Button-3>', popup)
#
# root.config(menu=menubar)
#
# mainloop()


# from tkinter import *
#
# root = Tk()
#
# mainloop()

# import pygame
# import sys
#
# # 初始化pygame
# pygame.init()
#
# size = width, height = 600, 400
# speed = [-2, 1]
# bg = (255, 255, 255)
#
# # 创建指定大小的窗口
# screen = pygame.display.set_mode(size)
# # 设置窗口标题
# pygame.display.set_caption('初次见面，请大家多多关照！！')
#
# # 加载图片
# image = pygame.image.load(r'C:\Users\zhangyi\Desktop\QQ图片20191218154536.png')
# # 获取图片的位置矩形
# position = image.get_rect()
#
#
# while True:
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             sys.exit()
#
#
#     # 移动图片
#     position = position.move(speed)
#
#     if position.left < 0 or position.right > width:
#         # 翻转图片
#         image = pygame.transform.flip(image, True, False)
#         # 反向移动
#         speed[0] = -speed[0]
#
#     if position.top < 0 or position.bottom > height:
#         speed[1] = -speed[1]
#
#
#     # 填充背景
#     screen.fill(bg)
#
#     # 更新图片
#     screen.blit(image, position)
#
#     # 更新界面
#     pygame.display.flip()
#
#     # 延迟10毫秒
#     pygame.time.delay(10)
#


# import pygame
# import sys
#
# # 初始化pygame
# pygame.init()
#
# size = width, height = 1920, 1080
# speed = [-8, 4]
# bg = [255, 255, 255]
#
# clock = pygame.time.Clock()
#
# # 创建指定大小的窗口
# screen = pygame.display.set_mode(size)
#
# # 设置窗口标题
# pygame.display.set_caption('初次见面，请大家多多关照!!')
#
#
# # 加载图片
# yl = pygame.image.load(r'C:\Users\zhangyi\Desktop\QQ图片20200107164350.jpg')
#
# # 获得图片的位置矩形
# position = yl.get_rect()
#
# while True:
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             sys.exit()
#
#     # 移动图像
#     position = position.move(speed)
#
#     if position.left < 0 or position.right > width:
#         # 翻转图片
#         yl = pygame.transform.flip(yl, True, False)
#         # 反方向移动
#         speed[0] = -speed[0]
#
#     if position.top < 0 or position.bottom > height:
#         speed[1] = -speed[1]
#
#
#     # 填充背景
#     screen.fill(bg)
#     # 更新图片
#     screen.blit(yl, position)
#     # 更新界面
#     pygame.display.flip()
#     # 延迟10毫秒
#     # pygame.time.delay(10)
#     clock.tick(200)


# import pygame
# import sys
#
# pygame.init()
#
# size = width, height = 600, 400
# screen = pygame.display.set_mode(size)
# pygame.display.set_caption('初次见面，请大家多多关照！！')
#
# f = open('record.txt', 'w')
#
# while True:
#     for event in pygame.event.get():
#         f.write(str(event) + '\n')
#
#         if event.type == pygame.QUIT:
#             f.close()
#             sys.exit()


# import pygame
# # import sys
# #
# # pygame.init()
# #
# # size = width, height = 600, 400
# # screen = pygame.display.set_mode(size)
# # pygame.display.set_caption('FishC Demo')
# # bg = (0, 0, 0)
# #
# # position = 0
# #
# # font = pygame.font.Font(None, 20)
# # line_height = font.get_linesize()
# # screen.fill(bg)
# #
# # while True:
# #     for event in pygame.event.get():
# #         if event.type == pygame.QUIT:
# #             sys.exit()
# #
# #
# #         screen.blit(font.render(str(event), True, (0, 255, 0)), (0, position))
# #         position += line_height
# #
# #         if position > height:
# #             position = 0
# #             screen.fill(bg)
# #
# #
# #     pygame.display.flip()


# import pygame
# import sys
# from pygame.locals import *
#
# pygame.init()
#
# size = width, height = 1920, 1080
# speed = [-2, 1]
# bg = (255, 255, 255)
#
# fullscreen = False
#
# size1 = pygame.display.list_modes()[0]
#
# clock = pygame.time.Clock()
#
# screen = pygame.display.set_mode(size, RESIZABLE)
# pygame.display.set_caption('初次见面，请大家多多关照！！')
#
# yl1 = pygame.image.load(r'C:\Users\zhangyi\Desktop\QQ图片20200107164350.jpg')
# yl = yl1
#
#
# ratio = 1.0
#
#
#
# yl1_rect = yl1.get_rect()
# position = yl_rect = yl1_rect
#
# l_head = yl
# r_head = pygame.transform.flip(yl, True, False)
#
# while True:
#     for event in pygame.event.get():
#         if event.type == QUIT:
#             sys.exit()
#
#         if event.type == KEYDOWN:
#             if event.key == K_LEFT:
#                 yl = l_head
#                 speed = [-1, 0]
#             if event.key == K_RIGHT:
#                 yl = r_head
#                 speed = [1, 0]
#             if event.key == K_UP:
#                 speed = [0, -1]
#             if event.key == K_DOWN:
#                 speed = [0, 1]
#
#
#             if event.key == K_F11:
#                 fullscreen = not fullscreen
#                 if fullscreen:
#                     screen = pygame.display.set_mode(size1, FULLSCREEN | HWSURFACE)
#                     width, height = 1920, 1080
#                 else:
#                     screen = pygame.display.set_mode(size)
#
#
#             if event.key == K_EQUALS or event.key == K_MINUS or event.key == K_SPACE:
#                 if event.key == K_EQUALS and ratio < 2:
#                     ratio += 0.1
#                 if event.key == K_MINUS and ratio > 0.5:
#                     ratio -= 0.1
#                 if event.key == K_SPACE:
#                     ratio = 1.0
#
#                 yl = pygame.transform.smoothscale(yl1,
#                                                   (int(yl1_rect.width * ratio),
#                                                    int(yl1_rect.height * ratio)))
#
#                 l_head = yl
#                 r_head = pygame.transform.flip(yl, True, False)
#
#         if event.type == VIDEORESIZE:
#             size = event.size
#             width, height = size
#             screen = pygame.display.set_mode(size, RESIZABLE)
#
#
#
#     position = position.move(speed)
#
#     if position.left < 0 or position.right > width:
#         # 翻转图片
#         yl = pygame.transform.flip(yl, True, False)
#         # 反方向移动
#         speed[0] = -speed[0]
#
#     if position.top < 0 or position.bottom > height:
#         speed[1] = -speed[1]
#
#     # if position.left < 0 or position.right > width:
#     #     yl = pygame.transform.flip(yl, True, False)
#     #     speed[0] = -speed[0]
#     #
#     # if position.top < 0 or position.bottom > height:
#     #     speed[0] = -speed[0]
#
#
#     screen.fill(bg)
#     screen.blit(yl, position)
#     pygame.display.flip()
#     clock.tick(200)
#

# import pygame
# import sys
# from pygame.locals import *
#
# pygame.init()
#
# size = width, height = 1920, 1080
# bg = (255, 255, 255)
# speed = [10, 0]
#
# clock = pygame.time.Clock()
#
# fullscreen = False
#
# screen = pygame.display.set_mode(size)
# pygame.display.set_caption('初次见面，请大家多多关照！！')
#
# yl = pygame.image.load(r'C:\Users\zhangyi\Desktop\QQ图片20200107164350.jpg')
# position = yl.get_rect()
#
# yl_right = pygame.transform.rotate(yl, 90)
# yl_top = pygame.transform.rotate(yl, 180)
# yl_left = pygame.transform.rotate(yl, 270)
# yl_bottom = yl
# yl = yl_top
#
#
# while True:
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             sys.exit()
#
#         if event.type == KEYDOWN:
#             # if event.type == K_F11:
#             #     fullscreen = not fullscreen
#             #     if fullscreen:
#             #         screen = pygame.display.set_mode((1920, 1080),
#             #                                          FULLSCREEN | HWSURFACE)
#             #     else:
#             #         screen = pygame.display.set_mode(size)
#
#             if event.key == K_F11:
#                 fullscreen = not fullscreen
#                 if fullscreen:
#                     size1 = pygame.display.list_modes()[0]
#                     screen = pygame.display.set_mode(size1, FULLSCREEN | HWSURFACE)
#                     width, height = 1920, 1080
#                 else:
#                     screen = pygame.display.set_mode(size)
#
#
#
#     position = position.move(speed)
#
#     if position.right > width:
#         yl = yl_right
#         position = yl_rect = yl.get_rect()
#         position.left = width - yl_rect.width
#         speed = [0, 5]
#
#     if position.bottom > height:
#         yl = yl_bottom
#         position = yl_rect = yl.get_rect()
#         position.left = width - yl_rect.width
#         position.top = height - yl_rect.height
#         speed = [-10, 0]
#
#     if position.left < 0:
#         yl = yl_left
#         position = yl_rect = yl.get_rect()
#         position.top = height - yl_rect.height
#         speed = [0, -10]
#
#     if position.top < 0:
#         yl = yl_top
#         position = yl_rect = yl.get_rect()
#         speed = [10, 0]
#
#     screen.fill(bg)
#     screen.blit(yl, position)
#     pygame.display.flip()
#     clock.tick(200)


# import pygame
# import sys
#
# pygame.init()
#
# size = width, height = 1920, 1080
# bg = (255, 255, 255)
# speed = [-10, 5]
#
# fullscreen = False
#
# clock = pygame.time.Clock()
#
# screen = pygame.display.set_mode(size)
# pygame.display.set_caption("初次见面，请大家多多关照！")
#
# yl = pygame.image.load(r'C:\Users\zhangyi\Desktop\QQ图片20200107164350.jpg')
# position = yl.get_rect()
#
# l_head = yl
# r_head = pygame.transform.flip(yl, True, False)
#
# while True:
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             sys.exit()
#
#
#         if event.type == pygame.KEYDOWN:
#             if event.key == pygame.K_F11:
#                 fullscreen = not fullscreen
#
#                 if fullscreen:
#                     screen = pygame.display.set_mode(size, pygame.FULLSCREEN | pygame.HWSURFACE)
#                     width, height = size
#                 else:
#                     screen = pygame.display.set_mode(size)
#
#
#             if event.key == pygame.K_LEFT:
#                 yl = l_head
#                 speed = [-1, 0]
#             if event.key == pygame.K_RIGHT:
#                 yl = r_head
#                 speed = [1, 0]
#             if event.key == pygame.K_UP:
#                 speed = [0, 1]
#             if event.key == pygame.K_DOWN:
#                 speed = [0, -1]
#
#
#     position = position.move(speed)
#
#     if position.left < 0 or position.right > width:
#         yl = pygame.transform.flip(yl, True, False)
#         speed[0] = -speed[0]
#
#     if position.top < 0 or position.bottom > height:
#         speed[-1] = -speed[1]
#
#
#     screen.fill(bg)
#     screen.blit(yl, position)
#     pygame.display.flip()
#     clock.tick(200)





