'''
算术运算符

+	加 - 两个对象相加	a + b 输出结果 31
-	减 - 得到负数或是一个数减去另一个数	a - b 输出结果 -11
*	乘 - 两个数相乘或是返回一个被重复若干次的字符串	a * b 输出结果 210
/	除 - x 除以 y	b / a 输出结果 2.1
%	取模 - 返回除法的余数	b % a 输出结果 1
**	幂 - 返回x的y次幂	a**b 为10的21次方
//	取整除 - 返回商的整数部分	9//2 输出结果 4 , 9.0//2.0 输出结果 4.0
'''

a = 21
b = 10
c = 0

c = a + b
print("a + b 的值为：", c)
# 31

c = a - b
print("a - b 的值为：", c)
# 11

c = a * b
print("a * b 的值为：", c)
# 210

c = a / b
print("a / b 的值为：", c)
# 2.1

c = a % b
print("a % b 的值为：", c)
# 1


# 修改变量 a 、b 、c
a = 2
b = 3
c = a ** b
print("a ** b 的值为：", c)
# 8

a = 10
b = 6
c = a // b
print("a // b 的值为：", c)



