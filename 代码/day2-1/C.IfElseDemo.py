'''
if -else双分支选择语句

if (条件表达式):
一条或者多条语句
当条件表达式结果为true时，会执行if选择分支中的语句
else:
一条或者多条语句
当条件表达式结果为false时，会执行else选择分支中的语句

注意：if和else分支，只会执行一个，并且一定会执行一个
'''

n = int(input('请输入一个数字：'))

if n < 50:
    print('%d 小于数字50' %(n))
else:
    print('%d 大于数字50' %(n))


'''
三元操作符

'''

x, y = 4, 5

if x > y:
    num = x
else:
    num = y

print(num)
# 改成方法1

num = x if x > y else y
print('最大值为：', num)

# 改成方法2
z = 10

num = max(x, y, z)

print('最大值为：', num)
