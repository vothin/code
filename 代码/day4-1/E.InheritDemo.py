'''
派生类的定义如下所示:
class DerivedClassName(BaseClassName1):
    <statement-1>
    .
    .
    .
    <statement-N>

需要注意圆括号中基类的顺序，若是基类中有相同的方法名，而在子类使用时未指定，python从左至右搜索 即方法在子类中未找到时，
从左到右查找基类中是否包含方法。

BaseClassName（示例中的基类名）必须与派生类定义在一个作用域内。除了类，还可以用表达式，基类定义在另一个模块中时这一点非常有用:

Inheritance：以普通类为基础建立专门的类对象；如果已经有一个基类，想再建立一个新类，新类中要添加几种新方法，
而又要用原来基类的一些方法，这个时候新类就要继承基类的方法，而又有新的方法，这就是继承；继承的方法就是在新类定义中添加一个基类作为参数。
'''

# 继承是指这样一种能力：它可以使用现有类的所有功能，并在无需重新编写原来的类的情况下对这些功能进行扩展
# 通过继承创建的新类称为“子类”或“派生类”，被继承的类称为“基类”、“父类”或“超类”，继承的过程，就是从一般到特殊的过程

# 当成一个父类/基类/超类
class person_1():

    def talk(self):  # 父类方法
        print("这是父类方法")

# 子类/派生类
class person_2(person_1):
    def walk(self):
        print("这是子类方法")

s = person_2()
s.talk()   # 父类的方法
s.walk()   # 子类本身的方法



























# 构造函数中的继承
# 1 父类名称.__init__(self,参数1,参数2)
# 2 super(子类，self).__init__(参数1,参数2....n)

# 单继承
# class Person:
#     '''这是一个描述人的类'''
#
#     # 构造函数
#     def __init__(self, name, age, height):
#         # print "In __init__ func."
#         # 初始化三个属性  很多类都倾向于将对象创建为有初始状态的。因此类可能会定义一个名为 __init__() 的特殊方法（构造方法）
#         self.name = name
#         self.age = age
#         self.height = height
#         return
#
#     # 类方法
#     # self指代当前对象p
#     def eat(self, food):
#         print("%s is eating %s!" % (self.name, food))
#
#     def work(self):
#         print("%s is working!" % self.name)
#
# class Person_1(Person):
#
#     def __init__(self, n, a, h, c):  # 先继承，再进行重构
#         Person.__init__(self, n, a, h)  #super(Person_1,self).__init__(n,a,h)
#         self.class_1 = c  # 定义自己的类的本身属性
#
#     # 覆写父类的方法
#     def work(self):
#         print("%s is working=子类" % self.name)
#
# s = Person_1("jack", 15, 1.78, "16")
# s.work()