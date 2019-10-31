'''
* 结束本次循环，继续下一次循环
  continue
'''

set1 = {1, 2, 3, 4}  # 集合
for site in set1:
    if site == 3:
        print("continue")
        continue
    print("循环数据 ", site)
else:
    print("没有循环数据!")
print("完成循环!")