import random

# 随机生成[0.1)的浮点数
print("random():", random.random())

# 随机生成1000-9999之间的整数 random.randint(a, b)，
# 用于生成一个指定范围内的整数。其中参数a是下限，参数b是上限，生成的随机数n: a <= n <= b
# print random.randint(20, 10)  # 该语句是错误的。下限必须小于上限
print("randint(1000, 9999):", random.randint(1000, 9999), random.randint(20, 20))

# 随机生成0-20之间的偶数
print("randrange(0, 21, 2):", random.randrange(0, 21, 1),random.randrange(0, 21, 2),random.randrange(0, 21, 3))
# [0,3,6,9,12,15,18,21]
# [0,2,4,6,8,10]

# 随机生成0-20之间的浮点数
print("uniform(0, 20):", random.uniform(0, 20))

# 从序列中随机选择一个元素
list_string = ['a', 'b', 'c', 'd', 'e']
print("choice(list):", random.choice(list_string))
print("choice(string):", random.choice('abcd'))

# 对列表元素随机排序
list_number = [1, 2, 3, 4, 5,6,7,8,9]
random.shuffle(list_number)
print("shuffle(list):", list_number)

# 从指定序列中随机获取指定长度的片断
print("sample(sequence):", random.sample('abcdefg', 2),random.sample('abcdefg', 3),random.sample('abcdefg', 4))