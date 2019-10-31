# 如果你需要遍历数字序列，可以使用内置range()函数。它会生成数列

for i in range(0, 6, 2):  # 0 -- 5
    print(i, end='')
print()
# 你也可以使用range指定区间的值：

for i in range(5, 9):  # 步长默认为1
    print(i, end='')
print()
# 也可以使range以指定数字开始并指定不同的增量(甚至可以是负数，有时这也叫做'步长')

for i in range(0, 10, 3):
    print(i, end='')
print()

for i in range(-10, -100, -30):  # -10 -40 -70 -100
    print(i, end='')
print()


# ctrl+alt+l