# 15. 点名退出：['小红', '小蓝', '小白', '小叶', '小朱', '小丁', '小刘', '小许', '小罗', '小肖', '小赵', '小黄', '小郭', '小陆', ]
#  小红数1，小蓝数2，小白数3，数到3就退出，重新数
# 直到最后一个人，输出他的名字
# count = 18/3=6  stunde = 6-1=5
# ['小红', '0', '0', '0', '小朱', '0', '小刘', '0', '0', '小肖', '小赵', '0', '0', '小陆', '0']
# student_1 = ['小红', '小蓝', '小白', '小叶', '小朱', '小丁', '小刘', '小许', '小罗', '小肖', '小赵', '小黄', '小郭', '小陆', '小周']
# count = 0
# while count/3 <= len(student_1)-1:
#     for i in range(len(student_1)):
#         if student_1[i]!='0':    # 不为0才统计
#             count = count + 1
#
#         if count % 3 == 0:       # 能被3带队的换为0
#             student_1[i] ='0'
#
# for j in range(len(student_1)):
#     if student_1[j]!='0':
#         print("最后一个人是:",student_1[j])




# for i in range(1, 100):  # 设置循环，开始游戏
#     if len(p) > 2:
#         a = len(p) % 3  # 找出最后数不完3的那组人放入新数组的最前面
#         n = []
#         for j in range(len(p) - a, len(p)):
#             n.append(p[j])
#         del p[len(p) - a:len(p)]  # p数组删掉数不完的人
#         for k in range(0, len(p)):
#             if (k + 1) % 3 != 0:  # 把不是数3的人拼接到新数组
#                 n.append(p[k])
#         p = n  # 把新数组赋予给p，让他继续循环
#         print(p)
#     elif len(p) == 2:  # 新数组最后只有2个人，第一个人必定会数到3，则去掉第一个人
#         p.pop(0)
#     else:
#         print("最后留下来的那个人的编号是：", p[0])
#         break



# 1 查询名字.成功输出名字.否则暂无此人
# 2 查询同姓名字(且只能查询成功后才能查询同姓名字,不包括自己)
# 3 查询同名名字(一个字,二个字.包括第二个字或者第三个字都可以)
# 4 抽奖(随机抽奖-不能重复,如重复中奖则重新抽奖)
# 5 查询中奖名单(如果没有抽奖,则提示没有中奖者,如果有中奖,则打印)
# 6 结束本系统



import random   # 随机


def select_name(name, list1):  # 查询同学姓名
    for s in list1:
        if s == name:
            return "此同学存在:" + s
    else:
        return "此同学不存在,无法查询"


def select_name_top(name, list1):  #
    for t in list1:
        if name[0] == t[0] and name != t:  # 不能等于自己,不能查自己
            print(t)


def select_surname(name, list1):
    for surname in name[1:]:
        for sur in list1:
            if surname in sur and name != sur:
                print(sur)

# 周雪梅    循环: 雪梅



student_27 = ["肖玉成", "徐帆", "彭星辉", "谭家伟", "张宏伟", "周雪梅", "万礼武", "于世龙", "武辉", "彭星荣", "曹星", "欧周华", "黄增高", "邓远洋", "尚培罡",
              "鈡明", "陈明曦", "宋飞影", "周子翔", "石远金", "甘宇鹏", "杨文汉", "张逸", "薛羽", "林明和", "陈福成", "许则和", "杨顺", "刘岳彩", "张晓鹏",
              "张修瑜", "陈万", "凌云锋", "杨壹民", "邓嘉伟", "刘毅", "徐勇", "黄海钧", "范仲龙"]
prize_name = []  # 空列表,用于做中奖名单...
while 1:
    print()
    print("# 1 查询同学名字.")
    print("# 2 查询同姓名字.")
    print("# 3 查询名同字的名字")
    print("# 4 抽奖(随机抽奖-不能重复)")
    print("# 5 查询中奖名单")
    print("# 6 结束本系统")
    num = input("请输入数值(1-6):")  # 1-6中的选择
    if num >= '1' and num <= '6':
        if num == '1':
            s_name = input("请输入想查询的姓名:")
            print(select_name(s_name, student_27))  # 传参数,查询的姓名和同学列表

        elif num == '2':
            s_name_top = input("请输入想查询的姓名:")
            select_name_top(s_name_top, student_27)

        elif num == '3':
            s_surname_top = input("请输入想查询的姓名:")
            select_surname(s_surname_top, student_27)

        elif num == '4':

            # for prize in student_27:
            while 1:
                size = random.randint(0, len(student_27) - 1)    # random.randint(1,20)产生一个1到20的随机数
                if student_27[size] not in prize_name:
                    prize_name.append(student_27[size])
                    print("这次中奖名单:", student_27[size])
                    break
                else:
                    print("%s 已中过奖,重新抽奖" % (student_27[size]))

        elif num == '5':
            if len(prize_name) == 0:
                print("暂无中奖人员,请抽奖")
            else:
                print("中奖名单如下:", prize_name)

        elif num == '6':
            exit()  # 退出整个程序



    else:
        print("输入错误,请重新输入:")

# str = 周雪梅   str[0] == 周   list1 = ['周周','小明']  for i in range(len(list1)):   if str[0] == list1[i][0]