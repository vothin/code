# 1 银行类， 有取钱方法，查钱方法，存钱方法  初始化（姓名，卡号，钱数量）
# 存钱：如果存钱的数量少于0，则失败，否则加上本钱的钱，输出余额
# 查钱：直接查钱
# 取钱：取钱不能少于0，取钱不能大于余额，取钱成功显示余额
# 使用，存钱，取钱，查钱功能，以及统计创建了多少对象

class account():
    # 初始化数据
    count = 0
    def __init__(self, name, card, money_1):
        self.name = name
        self.card = card
        self.money_1 = money_1
        account.count += 1
        return

    # 取钱的方法
    def check(self, money_2):
        if money_2 <= 0:
            print("取钱失败，输入了非法字符")
        elif money_2 > self.money_1:
            print("你的余额不足")
        else:
            self.money_1 = self.money_1 - money_2
            print("取钱后余额为：", self.money_1)

    # 查余额
    def select(self):
        print("%s的余额为:%d" % (self.name, self.money_1))

    # 存钱
    def cun(self, cunmoney):
        if cunmoney <= 0:
            print("存钱失败")
        else:
            self.money_1 = self.money_1 + cunmoney
        print("取钱后余额为：", self.money_1)

if __name__ == "__main__":
    # 创建对象
    ac = account("小强强", "62226666", 8888)
    ac1 = account("小洋洋", "6333333", 7777)
    # 查询余额
    ac.select()

    # 存钱
    ac.cun(500)

    # 取钱
    ac.check(450)

    # 对象的统计
    print("一共创建对象：%d" % (account.count))
