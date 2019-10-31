'''
try-finally 语句
try-finally 语句无论是否发生异常都将执行最后的代码。
'''



try:
    fh = open("test.txt", "r")
    fh.write("这是一个测试文件，用于测试异常!!")
    print("已写入")
except:
    print("这已经出错了好吗")
finally:
    print("Error: 没有找到文件或读取文件失败")