'''
构造方法：

很多类都倾向于将对象创建为有初始状态的。因此类可能会定义一个名为 __init__() 的特殊方法（构造方法）
（1）、__init__方法的第一参数永远是self，表示创建的类实例本身，因此，在__init__方法内部，就可以把各种属性绑定到self，
因为self就指向创建的实例本身。
（2）、有了__init__方法，在创建实例的时候，就不能传入空的参数了，必须传入与__init__方法匹配的参数，
但self不需要传，Python解释器会自己把实例变量传进去：
'''


class Person:
    '''这是一个描述人的类'''

    # 构造函数
    def __init__(self, name, age, height):   # 初始化的过程
        # print "In __init__ func."
        # 初始化三个属性  很多类都倾向于将对象创建为有初始状态的。因此类可能会定义一个名为 __init__() 的特殊方法（构造方法）
        self.name = name
        self.age = age
        self.height = height
        return

    # 类方法
    # self指代当前对象p
    def eat(self, food):
        print("%s is eating %s!" % (self.name, food))

    def work(self):
        print("%s is working!" % self.name)


if __name__ == '__main__':
    # 创建对象 初始化过程
    p = Person("jack", 17, 1.75)
    p1 = Person("lucy", 27, 1.65)
    p2 = Person("yang", 22, 1.56)
    # print "对象创建成功"


    # 调用类方法: 对象.方法()
    p.eat("apple")
    p1.eat("banana")
    p.work()
    p1.work()

