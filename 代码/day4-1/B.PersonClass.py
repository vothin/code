class Person():  # 类名
    name = "xiaoming"   # 属性

    def eat(self):
        print("这是person的eat方法")
        print(self.name)

    def work(self):
        print("这是person的work方法")

# 直接引用
# print(Person.name)  # person的属性
# Person.work()
# Person.eat()

# 实例化引用
x = Person()  # 实例化
x.name = '10'
x.work()
x.eat()

print("这是实例化的属性", x.name)
