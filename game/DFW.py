import random


list_player = ["狗略略", "狗子月", "狗子霸", "白菜", "狗伊娃", "小水银", "华日酱", "啊兔兔"]
player2 = 0
list2 = []
list3 = ["扣除", "增加", "翻倍", "缩减", "清空", "不变"]
print("欢迎来到文字大富翁游戏！！！")
print("游戏角色分别有：狗略略、狗子月、狗子霸、白菜、狗伊娃、小水银、华日酱、啊兔兔")







# 是否开始游戏

# 选择人物
    # 查看人物属性+技能
        # 角色特有技能
        # 角色不同属性：力量，耐力，智力，精神，舒服，幸运

# 提示游戏玩法

# 提供三次个选项关卡
    # 类型：奖励关，怪物关，商店关，陷阱关，boss关

    # 奖励关：
        # 奖励属性








# class game():
#     def pname(self):    # 检测是否存在角色名字
#         if player1 not in list_player:
#             print("很遗憾呢，您想要的角色并不存在，如果想要这个角色，可以跟开发者提议，但现在还请重新选择角色吧！！！")
#         else:
#             list2.append(player1)
#             return player1  #返回角色名
#
#
#     def pdice(self):    # 创建骰子随机数
#         self.dice = random.randint(1, 6)
#         return self.dice    # 返回骰子点数
#
#     def pmoney(self):   # 创建初始金额
#         self.money = 100000
#         return self.money
#
#     def padventure(self):                   # 随机文字大冒险
#         self.adice = random.random(1, 6)    # 生成随机数进行判断
#         if self.adice == 1:                 # 当随机数为1时，角色获得金额
#             self.amoney = random.randint(1000, 100000)  # 获得的金额
#             self.money = self.money + self.amoney       # 总金额
#             print("哼！这次算是你踩了狗屎运，下次可就没有这个机会了!")
#             print("捡到%s，现在总金额变成%s", (self.amoney,self.money))
#             return self.money       # 返回金额
#
#         if self.adice == 2:
#             self.amoney = random.randint(1000, 100000)
#             if self.money < self.amoney:
#                 self.money = 0
#             else:
#                 self.money = self.money - self.amoney
#             print("哈哈哈！这次轮到你倒大霉了吧！")
#             print("被扣%s，现在总金额只剩%s", (self.amoney,self.money))
#             return self.money
#
#         if self.adice == 3:
#             self.amoney = random.randint(2, 10)
#             self.money = self.money * self.amoney
#             print("我靠！还有没有天理了！！上天快劈死你这个狗东西！！！")
#             print("金额翻%s倍，现在总金额只剩%s", (self.amoney, self.money))
#             return self.money
#
#         if self.adice == 4:
#             self.amoney = random.randint(2, 10)
#             self.money = self.money // self.amoney
#             print("笑死我了！接受制裁吧，狗东西！")
#             print("金额缩水%s倍，现在总金额只剩%s", (self.amoney, self.money))
#             return self.money
#
#         if self.adice == 5:
#             self.money = 0
#             print("啊哈哈哈哈哈！！！狗东西！！！接受上天的制裁吧！！！")
#             print("金额清空，现在总金额为%s",  self.money)
#             return self.money
#
#         if self.adice == 6:
#             self.money = self.money
#             print("切，这次算你走运，没受到什么惩罚，无趣！")
#             print("金额不变，现在总金额为%s",  self.money)
#             return self.money
#
#
#
#
#
#
#
#
# while 1:
#     player1 = input("请选择选择一个角色：")   # 选择角色
#     play = game()   # 调用类game()
#     play.pname()    # 调用角色函数pname()
#     break
#
#
#
#
# for i in range(0, 301):
#     player2 = i
#
#
#     print()



# for i in list_player:
#     print(i)

