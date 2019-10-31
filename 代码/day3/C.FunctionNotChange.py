'''

在 python 中，strings, tuples, 和 numbers 是不可更改的对象，而 list,dict 等则是可以修改的对象。

python 函数的参数传递：

1 不可变类型：类似 c++ 的值传递，如 整数、字符串、元组。如fun（a），传递的只是a的值，没有影响a对象本身。比如在 fun（a）内部修改 a 的值，只是修改另一个复制的对象，不会影响 a 本身。

2 可变类型：类似 c++ 的引用传递，如 列表，字典。如 fun（la），则是将 la 真正的地址传过去，修改后fun外部的la也会受影响

python 中一切都是对象，严格意义我们不能说值传递还是引用传递，我们应该说传不可变对象和传可变对象。
'''

def ChangeInt(a):
    print('未改变值，a=', id(a))
    a = 10
    print('已改变值，a=', id(a))


b = 2
ChangeInt(b)
print(b)
print('b=', id(b))

