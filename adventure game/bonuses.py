import easygui as g
import random as r


class Bonuses:

    def __init__(self):
        self.bonLevel = 1
        self.random = r.randint(1, 10)
        self.attribute = 0

    def attributeIncrease(self):
        self.attBonuses = self.random * self.bonLevel

class HPBonuses(Bonuses):                       # 血量奖励
    def attributeIncrease(self):
        self.HPB = self.attBonuses * 100

class ATKBonuses(Bonuses):                      # 物攻奖励
    def attributeIncrease(self):
        self.ATKB = self.attBonuses * 10

class DEFBonuses(Bonuses):                      # 物防奖励
    def attributeIncrease(self):
        self.DEFB = self.attBonuses * 10

class SATBonuses(Bonuses):                      # 特攻奖励
    def attributeIncrease(self):
        self.SATB = self.attBonuses * 10

class SDFBonuses(Bonuses):                      # 特防奖励
    def attributeIncrease(self):
        self.SDFB = self.attBonuses * 10

class SPEBonuses(Bonuses):                      # 速度奖励
    def attributeIncrease(self):
        self.SPEB = self.attBonuses * 10

class LUKBonuses(Bonuses):                      # 幸运奖励
    def attributeIncrease(self):
        self.LUKB = (self.random // 2) * 10

class CHABonuses(Bonuses):                      # 魅力奖励
    def attributeIncrease(self):
        self.CHAB = (self.random // 2) * 10

class MonkeyBonuses(Bonuses):                   # 金钱奖励
    def attributeIncrease(self):
        self.Monkey = self.random * 100



if __name__ == '__main__':
    
    import roleAttri

    bonuses_list = ["血量奖励", "物攻奖励", "物防奖励", "特攻奖励", "特防奖励", "速度奖励", "幸运奖励", "魅力奖励", "金钱奖励"]

    count = 0

    g.msgbox("想要我的财宝吗？想要的话可以给你，去找吧！我把一切都放在那里了！")
    msg1 = "测试奖励"
    title1 = "测试奖励"
    choices1 = bonuses_list

    p = Bonuses()

    r = roleAttri.RoleAttribute()
    r.level = 10
    r.level = p.bonLevel

    list_player = ["略略酱", "白菜酱", "依文酱", "兔兔酱", "萌新酱", "小水银酱", "华日酱", ]
    playerdict = {}

    msg2 = ("请选择属于你自己的角色：\n\n"
           "游戏角色分别有：\n\n"
           "略略酱、 白菜酱、依文酱、兔兔酱、萌新酱、小水银酱、华日酱")
    title2 = "欢迎来到狂三真爱团，角色大冒险游戏！！！"

    choices2 = list_player

    while count == 0:

        bonuses = g.choicebox(msg1, title1, choices1)

        if bonuses == bonuses_list[0]:      # 血量  
            p = HPBonuses()
            
        elif bonuses == bonuses_list[1]:    # 物攻
            p = ATKBonuses()
            
        elif bonuses == bonuses_list[2]:    # 物防
            p = DEFBonuses()
        
        elif bonuses == bonuses_list[3]:    # 特攻
            p = SATBonuses()
            
        elif bonuses == bonuses_list[4]:    # 特防
            p = SDFBonuses()
        
        elif bonuses == bonuses_list[5]:    # 速度
            p = SPEBonuses()
            
        elif bonuses == bonuses_list[6]:    # 幸运
            p = LUKBonuses()
        
        elif bonuses == bonuses_list[7]:    # 魅力
            p = CHABonuses()
            
        elif bonuses == bonuses_list[8]:    # 金钱
            p = MonkeyBonuses()
        
        p.attributeIncrease()

        RoleValue = ""
        playerValue = ''




        for each in playerdict:
            RoleValue += ("\n%s：%s\n" % (each, playerdict[each]))

        playerValue = player + "\n" + RoleValue + "\n" + (player + "：" + p.petPhrase())

        if g.ccbox(playerValue, title, choices=("重新选择奖励", "决定就是你了")):
            pass

        else:
            count += 1




        # while count == 0:
        #
        #     player = g.choicebox(msg, title, choices)
        #
        #     if player == list_player[0]:
        #         r = Guolue()  # 选择狗略略的情况
        #
        #     elif player == list_player[1]:
        #         p = Baicai()  # 选择白菜的情况
        #
        #     elif player == list_player[2]:
        #         p = Yiwen()  # 选择依文的情况
        #
        #     elif player == list_player[3]:
        #         p = Tutu()  # 选择兔兔的情况
        #
        #     elif player == list_player[4]:
        #         p = Mengxin()  # 选择萌新的情况
        #
        #     elif player == list_player[5]:
        #         p = Xiaoshuiyin()  # 选择小水银的情况
        #
        #     elif player == list_player[6]:
        #         p = Huari()  # 选择华日的情况
        #
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
        
        
