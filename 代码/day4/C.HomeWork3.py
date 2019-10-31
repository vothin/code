# 14 输入n,输出杨辉三角


def createL(l):  # 生成杨辉三角的一行
    L = [1]
    for x in range(1, len(l)):    # 用循环来控制行数，以递增的形式增长
        L.append(l[x] + l[x - 1])
    L.append(1)
    return L

def printL(L, W):  # 打印
    s = ""
    for x in L:
        s += str(x) + "  "      # 转换成str类型 [1] 1
    print(s.center(W))    # W = 设置打印宽度  center(n)函数， 中间的意思，把字符串放在n个位置

L = [1]
row = int(input("输入行数："))
width = row * 4  # 设置打印宽度
for x in range(row):
    printL(L, width)
    L = createL(L)

# Alt + Shift + F9 运行debug模式  按F8,执行下一行代码
