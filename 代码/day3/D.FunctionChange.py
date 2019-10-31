'''
可变对象实例list
'''

def changeme(mylist1):
    # 修改传入的列表
    mylist1.append([1, 2, 3, 4])
    print('append改变后的mylist id=', id(mylist1))

    mylist1 = mylist1 + ([1, 2, 3, 4])
    print("+++函数内取值: ", mylist1, id(mylist1))
    return


# 调用changeme函数
mylist1 = [10, 20, 30]
changeme(mylist1)
print("函数外取值: ", mylist1, id(mylist1))


