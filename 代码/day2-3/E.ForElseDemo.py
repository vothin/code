'''
当迭代的对象迭代完并为空时，位于else的子句将执行

'''

for i in range(10):
    print('found it! i = %s' %(i))
else:
    print('not found it ...')