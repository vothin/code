'''


无论怎样,Test.py中的"__name__ == '__main__'"都不会成立的!

所以,下一行代码永远不会运行到!

1. 摘要

通俗的理解__name__ == '__main__'：假如你叫小明.py，在朋友眼中，你是小明(__name__ == '小明')；
在你自己眼中，你是你自己(__name__ == '__main__')。

if __name__ == '__main__'的意思是：当.py文件被直接运行时，if __name__ == '__main__'之下的代码块将被运行；
当.py文件以模块形式被导入时，if __name__ == '__main__'之下的代码块不被运行。


2. 程序入口

对于很多编程语言来说，程序都必须要有一个入口，比如C，C++，以及完全面向对象的编程语言Java，C#等。如果你接触过这些语言，
对于程序入口这个概念应该很好理解，C，C++都需要有一个main函数作为程序的入口，也就是程序的运行会从main函数开始。
同样，Java，C#必须要有一个包含Main方法的主类，作为程序入口。

而Python则不同，它属于脚本语言，不像编译型语言那样先将程序编译成二进制再运行，
而是动态的逐行解释运行。也就是从脚本第一行开始运行，没有统一的入口。

一个Python源码文件（.py）除了可以被直接运行外，还可以作为模块（也就是库），被其他.py文件导入。
不管是直接运行还是被导入，.py文件的最顶层代码都会被运行（Python用缩进来区分代码层次），
而当一个.py文件作为模块被导入时，我们可能不希望一部分代码被运行。


if __name__ == '__main__':
   main()

'''

# if __name__ == '__main__':
#     print('程序自身在运行')
# else:
#     print('我来自另一模块')

import test1

test1
