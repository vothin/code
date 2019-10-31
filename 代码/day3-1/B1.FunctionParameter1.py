# 关键字参数

def printme(str):
    "打印任何传入的字符串"
    print(str)
    return


def printinfo(name, age):
    "打印任何传入的字符串"
    print("名字: ", name)
    print("年龄: ", age)
    return

printme(str="呵呵")

printinfo(age=50, name="runoob") # 不需要使用指定顺序