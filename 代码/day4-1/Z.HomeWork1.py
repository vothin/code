# 2 创建一个VIP的银行类，
# Account 父类, 基类,超类super
# VipAccount 子类,派生类，（取钱）覆写父类方法 override

class Account:
    "这是一个银行账户的类"
    # 类变量,不属于某个对象,属于类
    count = 0

    def __init__(self, name, number, money):
        self.name = name
        self.number = number
        self.money = money
        Account.count += 1
        return

    # 查询余额
    def check(self):
        return self.money

    # 存钱
    def deposit(self, amount):
        "存钱成功返回True,否则返回False"
        if amount <= 0:
            print("存钱失败")
            return False
        self.money += amount
        return True

    # 取钱
    def withdraw(self, amount):
        if amount <= 0:
            # print "取钱金额不能小于等于0"
            return False
        elif amount > self.money:
            # print "余额不足!"
            return False
        else:
            self.money -= amount
            print("取钱成功")
            return True

# Account 父类, 基类,超类super
# VipAccount 子类,派生类

# VIP账户的类
class VipAccount(Account):
    "这是一个VIP账户的类"

    def __init__(self, name, number, money, overdraft):
        self.name = name
        self.number = number
        self.money = money
        self.overdraft = overdraft
        return

    # 覆写父类方法 override
    def withdraw(self, amount):
        if amount <= 0:
            print("取钱金额不能小于等于0")
            #return False
        elif amount > self.money + self.overdraft:
            print("余额不足!")
            #return False
        else:
            self.money -= amount
            # print "取钱成功"
            return True
    # 子类添加新方法
    def order(self, drink):
        print("Give me a %s" % drink)

if __name__ == '__main__':
    v1 = VipAccount("jack", '11223344', 500, 1000)
    print("账户余额是:", v1.check())
    if not v1.withdraw(1500):
        #     if not v1.withdraw(2000):
        print("取钱失败!")
    print("账户余额是:", v1.check())
    v1.deposit(2500)
    print("账户余额是:", v1.check())
    v1.order("java")
