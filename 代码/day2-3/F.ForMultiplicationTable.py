# 循环嵌套
# count ,sum= 1, 0
# for i in range(5):  # 0 1 2 3 4
#     for j in range(5):  # 0 1 2 3 4   总数: 25次
#         print('这是第%d次循环，这时i和j的值是' % (count), i, j)
#         count = count + 1;sum = sum + 1
# print("一共循环了%d次" % (sum))




# for i in range(1, 10):
#     for j in range(1, i + 1):
#         print("%d * %d =%d\t" % (j, i, i * j), end='')
#     print()




# 这是经典的"百马百担"问题，有一百匹马，驮一百担货，大马驮3担，中马驮2担，两只小马驮1担，问有大，中，小马各几匹的方案？

x, y, z = 0, 0, 0
for x in range(0, 34):
    for y in range(0, 51):
        for z in range(0, 201):
            if 3 * x + 2 * y + z / 2 == 100 and x + y + z == 100:
                print("大马:%d 中马:%d 小马:%d" % (x, y, z))
