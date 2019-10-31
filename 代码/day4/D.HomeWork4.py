# 16  "1.存储员工信息：" "2.查询员工信息：" "3.所有员工信息：" "4.退出程序"  员工有 name,age,sal

def menu_1():
    print("1.存储员工信息：")
    print("2.查询员工信息：")
    print("3.所有员工信息：")
    print("4.退出程序")
    print()

list_1 = []
ditc_1 = {}
while 1:
    menu_1()
    choose = int(input("请选择[1-4]:"))
    if len(list_1) == 0 and choose != 1:
        print("没有员工信息，请添加员工信息")
    elif choose == 1:
        name = input("请输入员工姓名：")
        age = input("请输入员工年纪：")
        sal = input("请输入员工工资：")
        ditc_1 = {"name": name, "age": age, "sal": sal}
        list_1.append(ditc_1)
    elif choose == 2:
        check = input("请选择查询员工以什么查询(name,age,sal):")
        if check in (list_1[0].keys()):
            name_1 = input("请输入员工" + check + ":")
            count = 0
            for i in range(len(list_1)):
                if name_1 == list_1[i][check]:
                    print([list_1[i]])
                    count = count + 1
                if count == 0:
                    print("该员工不存在")
                else:
                    print("输入有误")
    elif choose == 3:
        for i in range(len(list_1)):
            print("name:%s \t age:%s \t sal:%s \t" % (list_1[i]["name"], list_1[i]["age"], list_1[i]["sal"]))

    elif choose == 4:
        exit()

    else:
        print("输入有误")
