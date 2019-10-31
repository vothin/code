'''
当内部作用域想修改外部作用域的变量时，就要用到 global
'''

total = 0  # 这是一个全局变量

# 可写函数说明
def sum(arg1, arg2):
    global total
    total = 4
    print(total)
    print('输出k=',total)



# 调用sum函数
total = 1
sum(10, 20)
print("函数外是全局变量 : ", total)