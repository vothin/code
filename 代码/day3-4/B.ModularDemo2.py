'''
当解释器遇到 import 语句，如果模块在当前的搜索路径就会被导入。

搜索路径是一个解释器会先进行搜索的所有目录的列表。如想要导入模块 ,需要把命令放在脚本的顶端
'''


import sys
import time


print('命令行参数如下:')
for i in sys.argv:
    print(i)
print('\n\nPython 路径为：', sys.path, '\n')

time.sleep(5)   # 强制睡5秒

print(dir(sys))


