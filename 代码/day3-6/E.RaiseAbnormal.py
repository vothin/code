'''
触发异常
语法:
raise [Exception [, args [, traceback]]]
'''

# 定义函数
inputValue=input("please input a int data :")
if type(inputValue)!=type(1):
    raise ValueError
else:
    print(inputValue)