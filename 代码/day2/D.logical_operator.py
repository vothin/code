'''
逻辑运算符

and	x and y	布尔"与" - 如果 x 为 False，x and y 返回 False，否则它返回 y 的计算值。	(a and b) 返回 20。
or	x or y	布尔"或" - 如果 x 是 True，它返回 x 的值，否则它返回 y 的计算值。	(a or b) 返回 10。
not	not x	布尔"非" - 如果 x 为 True，返回 False 。如果 x 为 False，它返回 True。
'''

a = 0
b = 1

if (a and b):
   print('T')   # 二个值进行比较，只要有一个值为false,则返回false,只有当二个值为true时，才回返true
else:
   print('F')


if (a or b):
   print('T')   # 只要其中一个为true时，返回true,否则回返false
else:
   print('F')


# 修改变量 a 的值

print(not (a and b))
print(not (a or b))

print((a and b))
print((a or b))
