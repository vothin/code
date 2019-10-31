import easygui as g


class RoleAttribute:
    def __init__(self):
        # 创建一个通用角色模板
        self.STR = 10       # 力量
        self.CON = 10       # 体质
        self.INT = 10       # 智力
        self.SPR = 10       # 精神
        self.SPD = 10       # 速度
        self.LUK = 0        # 幸运
        self.CHA = 0        # 魅力
        self.level = 1      # 等级
        self.levelmax = 10  # 满级
        self.EXP = 0        # 经验
        self.EXPmax = 100   # 当前满级经验值
        self.Monkey = 0     # 金钱


    def RoleLevel(self):
        if self.EXP >= self.EXPmax and self.level < self.levelmax:
            self.EXP = self.EXP - self.EXPmax
            self.EXPmax += self.EXPmax
            self.level += 1

        elif self.EXP >= self.EXPmax and self.level == self.levelmax:
            self.EXP = self.EXPmax

        else:
            pass

    def RoleValue(self):
        # 展示角色属性
        self.HP  = (self.CON//2 + self.SPD//5) * self.level * 100     # 生命值，计算公式为：（体质//2 + 速度//5） * 100
        self.ATK = self.STR  * self.level * 10                        # 物攻值，计算公式为：力量 * 10
        self.DEF = self.CON  * self.level * 10                        # 物防值，计算公式为：体质 * 10
        self.SAT = self.INT  * self.level * 10                        # 特攻值，计算公式为：智力 * 10
        self.SDF = self.SPR  * self.level * 10                        # 特防值，计算公式为：精神 * 10
        self.SPE = self.SPD  * self.level * 10                        # 速度值，计算公式为：速度 * 10

        global playerdict
        playerdict = {"血量" : self.HP ,
                      "物攻" : self.ATK,
                      "物防" : self.DEF,
                      "特攻" : self.SAT,
                      "特防" : self.SDF,
                      "速度" : self.SPE,
                      "等级" : self.level,
                      "当前经验" : self.EXP,
                      "升级所需经验" : self.EXPmax - self.EXP,
                      "金钱" : self.Monkey}

class Guolue(RoleAttribute):

    # 创建对象略略酱，我这该死的无处安放的魅力
    def __init__(self):
        super(Guolue, self).__init__()
        self.STR = 5        # 力量
        self.CON = 8        # 体质
        self.INT = 15       # 智力
        self.SPR = 13       # 精神
        self.SPD = 9        # 速度
        self.LUK = 0        # 幸运
        self.CHA = "max"    # 魅力
        self.level = 1      # 等级
        self.EXP = 0        # 经验
        self.EXPmax = 100   # 当前满级经验值
        self.Monkey = 0     # 金钱

    def petPhrase(self):
        return "我这该死的无处安放的魅力"

class Baicai(RoleAttribute):

    # 创建对象白菜酱，白菜色图time！！！
    def __init__(self):
        super(Baicai, self).__init__()
        self.STR = 14       # 力量
        self.CON = 15       # 体质
        self.INT = 8        # 智力
        self.SPR = 8        # 精神
        self.SPD = 5        # 速度
        self.LUK = "max"    # 幸运
        self.CHA = 0        # 魅力
        self.level = 1      # 等级
        self.EXP = 0        # 经验
        self.EXPmax = 100   # 当前满级经验值
        self.Monkey = 0     # 金钱

    def petPhrase(self):
        return "吃我一击「白菜色图time！！！」"

class Yiwen(RoleAttribute):

    # 创建对象依文酱，啊...兔兔不让我走
    def __init__(self):
        super(Yiwen, self).__init__()
        self.STR = 13       # 力量
        self.CON = 6        # 体质
        self.INT = 13       # 智力
        self.SPR = 6        # 精神
        self.SPD = 12       # 速度
        self.LUK = 0        # 幸运
        self.CHA = 0        # 魅力
        self.level = 1      # 等级
        self.EXP = 0        # 经验
        self.EXPmax = 100   # 当前满级经验值
        self.Monkey = 0     # 金钱

    def petPhrase(self):
        return "我要跟兔兔在一起，谁当我谁死！！！"


class Tutu(RoleAttribute):

    # 创建对象兔兔酱，依喵去哪里，我就去哪里
    def __init__(self):
        super(Tutu, self).__init__()
        self.STR = 15       # 力量
        self.CON = 8        # 体质
        self.INT = 8        # 智力
        self.SPR = 7        # 精神
        self.SPD = 12       # 速度
        self.LUK = 0        # 幸运
        self.CHA = 0        # 魅力
        self.level = 1      # 等级
        self.EXP = 0        # 经验
        self.EXPmax = 100   # 当前满级经验值
        self.Monkey = 0     # 金钱

    def petPhrase(self):
        return "我病娇起来，连自己都害怕"

class Mengxin(RoleAttribute):

    # 创建对象萌新酱，虽然我已经老了，但我还是萌新
    def __init__(self):
        super(Mengxin, self).__init__()
        self.STR = 8        # 力量
        self.CON = 8        # 体质
        self.INT = 15       # 智力
        self.SPR = 9        # 精神
        self.SPD = 10       # 速度
        self.LUK = 0        # 幸运
        self.CHA = 0        # 魅力
        self.level = 1      # 等级
        self.EXP = 0        # 经验
        self.EXPmax = 100   # 当前满级经验值
        self.Monkey = 0     # 金钱

    def petPhrase(self):
        return "虽然我已经老了，但我还是萌新"

class Xiaoshuiyin(RoleAttribute):

    # 创建对象小水银酱，我...我...我可是很厉害的！！！
    def __init__(self):
        super(Xiaoshuiyin, self).__init__()
        self.STR = 5        # 力量
        self.CON = 5        # 体质
        self.INT = 11       # 智力
        self.SPR = 11       # 精神
        self.SPD = 18       # 速度
        self.LUK = 0        # 幸运
        self.CHA = 80       # 魅力
        self.level = 1      # 等级
        self.EXP = 0        # 经验
        self.EXPmax = 100   # 当前满级经验值
        self.Monkey = 0     # 金钱

    def petPhrase(self):
        return "我...我...我可是很厉害的！！！"

class Huari(RoleAttribute):

    # 创建对象华日酱，ヽ(*´∀´*)ﾉ 我可是超可爱！！！
    def __init__(self):
        super(Huari, self).__init__()
        self.STR = 8        # 力量
        self.CON = 12       # 体质
        self.INT = 8        # 智力
        self.SPR = 12       # 精神
        self.SPD = 10       # 速度
        self.LUK = 0        # 幸运
        self.CHA = 50       # 魅力
        self.level = 1      # 等级
        self.EXP = 0        # 经验
        self.EXPmax = 100   # 当前满级经验值
        self.Monkey = 0     # 金钱

    def petPhrase(self):
        return "ヽ(*´∀´*)ﾉ 我宇宙无敌第一可爱！！！"


if __name__ == '__main__':

    list_player = ["略略酱", "白菜酱", "依文酱", "兔兔酱", "萌新酱", "小水银酱", "华日酱", ]
    playerdict = {}

    count = 0

    g.msgbox("欢迎来到狂三真爱团，角色大冒险游戏！！！")
    msg = ("请选择属于你自己的角色：\n\n"
           "游戏角色分别有：\n\n"
           "略略酱、 白菜酱、依文酱、兔兔酱、萌新酱、小水银酱、华日酱")
    title = "欢迎来到狂三真爱团，角色大冒险游戏！！！"


    choices = list_player

    p = RoleAttribute()

    while count == 0:


        player = g.choicebox(msg, title, choices)

        if player == list_player[0]:
            p = Guolue()        # 选择狗略略的情况

        elif player == list_player[1]:
            p = Baicai()        # 选择白菜的情况

        elif player == list_player[2]:
            p = Yiwen()         # 选择依文的情况

        elif player == list_player[3]:
            p = Tutu()          # 选择兔兔的情况

        elif player == list_player[4]:
            p = Mengxin()       # 选择萌新的情况

        elif player == list_player[5]:
            p = Xiaoshuiyin()   # 选择小水银的情况

        elif player == list_player[6]:
            p = Huari()         # 选择华日的情况

        p.RoleValue()

        RoleValue = ""
        playerValue = ''

        for each in playerdict:
            RoleValue += ("\n%s：%s\n" %(each, playerdict[each]))

        playerValue = player + "\n" +  RoleValue + "\n" + ( player + "：" +p.petPhrase())

        if g.ccbox(playerValue, title, choices = ("重新选择角色", "决定就是你了")):
            pass

        else:
            count += 1


        #
        # elif player == list_player[1]:
        #
        #     # 选择白菜的情况
        #     p = Baicai()
        #     p.RoleValue()
        #
        #     RoleValue = ""
        #     playerValue = ''
        #
        #     for each in playerdict:
        #         RoleValue += ("\n%s：%s\n" % (each, playerdict[each]))
        #
        #     playerValue = player + "\n" + RoleValue + "\n" + (player + "：" + p.petPhrase())
        #
        #     if g.ccbox(playerValue, title, choices=("重新选择角色", "决定就是你了")):
        #         pass
        #
        #     else:
        #         count += 1
        #
        #
        # elif player == list_player[2]:
        #
        #     # 选择依文的情况
        #     p = Yiwen()
        #     p.RoleValue()
        #
        #     RoleValue = ""
        #     playerValue = ''
        #
        #     for each in playerdict:
        #         RoleValue += ("\n%s：%s\n" % (each, playerdict[each]))
        #
        #     playerValue = player + "\n" + RoleValue + "\n" + (player + "：" + p.petPhrase())
        #
        #     if g.ccbox(playerValue, title, choices=("重新选择角色", "决定就是你了")):
        #         pass
        #
        #     else:
        #         count += 1
        #
        #
        #
        # elif player == list_player[3]:
        #
        #     # 选择兔兔的情况
        #     p = Tutu()
        #     p.RoleValue()
        #
        #     RoleValue = ""
        #     playerValue = ''
        #
        #     for each in playerdict:
        #         RoleValue += ("\n%s：%s\n" % (each, playerdict[each]))
        #
        #     playerValue = player + "\n" + RoleValue + "\n" + (player + "：" + p.petPhrase())
        #
        #     if g.ccbox(playerValue, title, choices=("重新选择角色", "决定就是你了")):
        #         pass
        #
        #     else:
        #         count += 1
        #
        # elif player == list_player[4]:
        #
        #     # 选择萌新的情况
        #     p = Mengxin()
        #     p.RoleValue()
        #
        #     RoleValue = ""
        #     playerValue = ''
        #
        #     for each in playerdict:
        #         RoleValue += ("\n%s：%s\n" % (each, playerdict[each]))
        #
        #     playerValue = player + "\n" + RoleValue + "\n" + (player + "：" + p.petPhrase())
        #
        #     if g.ccbox(playerValue, title, choices=("重新选择角色", "决定就是你了")):
        #         pass
        #
        #     else:
        #         count += 1
        #
        #
        #
        # elif player == list_player[5]:
        #
        #     # 选择小水银的情况
        #     p = Xiaoshuiyin()
        #     p.RoleValue()
        #
        #     RoleValue = ""
        #     playerValue = ''
        #
        #     for each in playerdict:
        #         RoleValue += ("\n%s：%s\n" % (each, playerdict[each]))
        #
        #     playerValue = player + "\n" + RoleValue + "\n" + (player + "：" + p.petPhrase())
        #
        #     if g.ccbox(playerValue, title, choices=("重新选择角色", "决定就是你了")):
        #         pass
        #
        #     else:
        #         count += 1
        #
        #
        # elif player == list_player[6]:
        #
        #     # 选择华日的情况
        #     p = Huari()
        #     p.RoleValue()
        #
        #     RoleValue = ""
        #     playerValue = ''
        #
        #     for each in playerdict:
        #         RoleValue += ("\n%s：%s\n" % (each, playerdict[each]))
        #
        #     playerValue = player + "\n" + RoleValue + "\n" + (player + "：" + p.petPhrase())
        #
        #     if g.ccbox(playerValue, title, choices=("重新选择角色", "决定就是你了")):
        #         pass
        #
        #     else:
        #         count += 1




    # print("欢迎来到狂三真爱团，角色大冒险游戏！！！")
    # print("游戏角色分别有：略略酱、 白菜酱、依文酱、兔兔酱、萌新酱、小水银酱、华日酱")
    #
    # while 1:
    #     player = input("请选择属于你自己的角色：")
    #
    #     if player not in list_player:
    #         print("你所选择的角色并不存在哦！！！")
    #         print("如果有想法的话，可以联系游戏制作人墨墨，制作新的角色！！！")
    #         print("现在请重新输入吧！！！")
    #         continue
    #
    #     else:
    #         if player == list_player[0]:
    #             p = Guolue()
    #             p.attributeValue()
    #             print(playerdict)
    #             print(p.petPhrase())
    #
    #         elif player == list_player[1]:
    #             p = Guolue()
    #             p.attributeValue()
    #             print(playerdict)
    #             print(p.petPhrase())
    #
    #         elif player == list_player[2]:
    #             p = Guolue()
    #             p.attributeValue()
    #             print(playerdict)
    #             print(p.petPhrase())
    #
    #         elif player == list_player[3]:
    #             p = Guolue()
    #             p.attributeValue()
    #             print(playerdict)
    #             print(p.petPhrase())
    #
    #         elif player == list_player[4]:
    #             p = Guolue()
    #             p.attributeValue()
    #             print(playerdict)
    #             print(p.petPhrase())
    #
    #         elif player == list_player[5]:
    #             p = Guolue()
    #             p.attributeValue()
    #             print(playerdict)
    #             print(p.petPhrase())
    #
    #         elif player == list_player[6]:
    #             p = Guolue()
    #             p.attributeValue()
    #             print(playerdict)
    #             print(p.petPhrase())
    #
