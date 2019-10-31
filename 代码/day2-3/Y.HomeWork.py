# 1 1+2+3....10的和
sum = 0 #相加的和
for i in range(1, 11):
    sum = sum + i
print("1+2+3....10:",sum)

# 2 10!阶乘的和..  5! = 1 * 2 * 3 * 4 * 5
sum, count = 0, 1
for i in range(1,11):   # 1 2 3 4 5 6 ...10
    count = count * i     # count = 1*1=1  # count = 1*2  count = !2*3 =3!
    sum = sum + count     # sum = 0 + 1   sum =1! + 2! +3!....10!
print("10!阶乘的和..",sum)

# 3 打印出所有的 "水仙花数 "，所谓 "水仙花数 "是指一个三位数，其各位数字立方和等于该数本身。
#　例如：153是一个 "水仙花数 "，因为153=1的三次方＋5的三次方＋3的三次方。
x, y, z = 0, 0, 0
for i in range(100, 1000):
    x = int(i / 100)
    y = int(i / 10 % 10)
    z = int(i % 10)
    # print(x, y, z)
    if x**3 + y*y*y + z**3 == i:
        print("水仙花数:",i)


# 4 操场上100多人排队，三人一组多1人，四人一组多2人，五人一组多3人，共多少人？
for i in range(101,200):
    if i%3 == 1 and i%4 == 2 and i%5 == 3:
        print("操场上有:",)